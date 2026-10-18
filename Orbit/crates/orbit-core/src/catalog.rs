use crate::{extension, Engines};
use serde::{Deserialize, Serialize};
use std::{
    env,
    path::{Path, PathBuf},
};

pub const IMAGES: &[&str] = &["jpg", "jpeg", "png", "webp", "tif", "tiff", "bmp"];
pub const WORD: &[&str] = &["doc", "docx", "odt", "rtf"];
pub const SHEETS: &[&str] = &["xls", "xlsx", "ods", "csv", "tsv"];
pub const SLIDES: &[&str] = &["ppt", "pptx", "odp"];

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Format {
    pub id: String,
    pub label: String,
    pub detail: String,
    pub available: bool,
    pub requires: String,
}

pub fn routes(ext: &str) -> Vec<(&'static str, &'static str)> {
    if IMAGES.contains(&ext) {
        vec![
            ("jpg", "Compact photo; transparency becomes white"),
            ("png", "Lossless image with transparency"),
            ("webp", "Lossless WebP image"),
            ("tiff", "TIFF image"),
            ("bmp", "Uncompressed bitmap"),
            ("pdf", "Image on a PDF page"),
            ("txt", "Recognise printed text with OCR"),
        ]
    } else if WORD.contains(&ext) {
        vec![
            ("pdf", "Export document pages"),
            ("docx", "Editable Word document"),
            ("odt", "OpenDocument text"),
            ("rtf", "Basic rich text"),
            ("txt", "Text only; formatting is removed"),
            ("html", "HTML document"),
        ]
    } else if SHEETS.contains(&ext) {
        vec![
            ("pdf", "Export sheets using workbook print settings"),
            ("xlsx", "Excel workbook"),
            ("ods", "OpenDocument spreadsheet"),
            ("csv", "First sheet only; values without formatting"),
            ("tsv", "First sheet only; tab-separated values"),
        ]
    } else if SLIDES.contains(&ext) {
        vec![
            ("pdf", "Static slides without animations"),
            ("pptx", "PowerPoint presentation"),
            ("odp", "OpenDocument presentation"),
        ]
    } else if ext == "pdf" {
        vec![
            (
                "docx",
                "Reconstruct editable content, or preserve page appearance as images",
            ),
            (
                "xlsx",
                "Extract detected tables; original formulas cannot be recovered",
            ),
            ("csv", "One CSV file per detected table"),
            ("jpg", "One image per page"),
            ("png", "One image per page"),
            ("txt", "Extract text; enable OCR for scans"),
        ]
    } else {
        vec![]
    }
}

pub fn formats(path: &Path, engines: &Engines) -> Vec<Format> {
    let ext = extension(path);
    routes(&ext)
        .into_iter()
        .filter(|(f, _)| {
            *f != ext && !(ext == "jpeg" && *f == "jpg") && !(ext == "tif" && *f == "tiff")
        })
        .map(|(id, detail)| {
            let native = IMAGES.contains(&ext.as_str()) && IMAGES.contains(&id);
            let office = WORD.contains(&ext.as_str())
                || SHEETS.contains(&ext.as_str())
                || SLIDES.contains(&ext.as_str());
            let has_worker =
                engines.worker.is_some() || (engines.python.is_some() && engines.script.is_some());
            let image_ocr = IMAGES.contains(&ext.as_str()) && id == "txt";
            let (available, requires) = if native {
                (true, "Rust image engine")
            } else if image_ocr {
                (
                    has_worker && engines.tesseract.is_some(),
                    "PDF/OCR worker and Tesseract",
                )
            } else if office {
                (engines.office.is_some(), "LibreOffice")
            } else {
                (has_worker, "PDF/OCR worker")
            };
            Format {
                id: id.into(),
                label: id.to_ascii_uppercase(),
                detail: detail.into(),
                available,
                requires: requires.into(),
            }
        })
        .collect()
}

pub fn find_program(name: &str, extra: &[PathBuf]) -> Option<PathBuf> {
    if let Some(p) = extra.iter().find(|p| p.is_file()) {
        return Some(p.clone());
    }
    let path = env::var_os("PATH").unwrap_or_default();
    for directory in env::split_paths(&path) {
        let candidate = directory.join(name);
        if candidate.is_file() {
            return Some(candidate);
        }
        if cfg!(windows) {
            let candidate = directory.join(format!("{name}.exe"));
            if candidate.is_file() {
                return Some(candidate);
            }
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn pdf_routes_dont_pretend_to_restore_workbooks() {
        let fs = formats(Path::new("statement.PDF"), &Engines::default());
        let excel = fs.iter().find(|f| f.id == "xlsx").unwrap();
        assert!(excel.detail.contains("formulas"));
        assert!(!excel.available);
        assert!(!fs.iter().any(|f| f.id == "pptx"));
    }
    #[test]
    fn image_routes_work_without_external_engines() {
        let fs = formats(Path::new("a.jpeg"), &Engines::default());
        assert!(!fs.iter().any(|f| f.id == "jpg"));
        assert!(fs.iter().find(|f| f.id == "png").unwrap().available);
        assert!(!fs.iter().find(|f| f.id == "pdf").unwrap().available);
    }
}

//! Local conversion policy, validated requests, native image codecs and process lifecycle.
pub mod catalog;
pub mod convert;
pub mod process;

use serde::{Deserialize, Serialize};
use std::{
    path::PathBuf,
    sync::{
        atomic::{AtomicBool, Ordering},
        Arc,
    },
};

pub const MAX_INPUT_BYTES: u64 = 250 * 1024 * 1024;

/// Keep normal Windows paths compatible with external Office applications.
pub fn canonical_path(path: &std::path::Path) -> std::io::Result<PathBuf> {
    dunce::canonicalize(path)
}

#[derive(Debug, thiserror::Error)]
pub enum Error {
    #[error("{0}")]
    Invalid(String),
    #[error("Required engine unavailable: {0}")]
    MissingEngine(String),
    #[error("Conversion cancelled")]
    Cancelled,
    #[error("Conversion timed out after 10 minutes")]
    Timeout,
    #[error("{0}")]
    Engine(String),
    #[error(transparent)]
    Io(#[from] std::io::Error),
    #[error(transparent)]
    Json(#[from] serde_json::Error),
    #[error(transparent)]
    Image(#[from] image::ImageError),
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(default)]
pub struct Options {
    pub quality: u8,
    pub dpi: u16,
    pub pages: String,
    pub ocr: bool,
    pub language: String,
    pub docx_mode: String,
    pub single_page_sheets: bool,
}
impl Default for Options {
    fn default() -> Self {
        Self {
            quality: 90,
            dpi: 150,
            pages: String::new(),
            ocr: false,
            language: "eng".into(),
            docx_mode: "editable".into(),
            single_page_sheets: false,
        }
    }
}
impl Options {
    pub fn validate(&self) -> Result<(), Error> {
        if !(1..=100).contains(&self.quality) || !(72..=300).contains(&self.dpi) {
            return Err(Error::Invalid(
                "Quality must be 1–100 and DPI 72–300".into(),
            ));
        }
        if self.pages.len() > 256
            || !self
                .pages
                .chars()
                .all(|c| c.is_ascii_digit() || ", -".contains(c))
        {
            return Err(Error::Invalid("Pages must look like 1-3,5".into()));
        }
        if self.language.is_empty()
            || self.language.len() > 64
            || !self
                .language
                .chars()
                .all(|c| c.is_ascii_alphanumeric() || "_+".contains(c))
        {
            return Err(Error::Invalid("Invalid OCR language".into()));
        }
        if !["editable", "page_images"].contains(&self.docx_mode.as_str()) {
            return Err(Error::Invalid("Unknown Word conversion mode".into()));
        }
        Ok(())
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Request {
    pub input: PathBuf,
    pub output_dir: PathBuf,
    pub format: String,
    #[serde(default)]
    pub options: Options,
}

#[derive(Debug, Clone, Default)]
pub struct Engines {
    pub office: Option<PathBuf>,
    /// A packaged worker, preferred over development Python.
    pub worker: Option<PathBuf>,
    pub python: Option<PathBuf>,
    pub script: Option<PathBuf>,
    pub tesseract: Option<PathBuf>,
}

#[derive(Debug, Clone, Default)]
pub struct Cancellation(Arc<AtomicBool>);
impl Cancellation {
    pub fn cancel(&self) {
        self.0.store(true, Ordering::SeqCst);
    }
    pub fn check(&self) -> Result<(), Error> {
        if self.0.load(Ordering::SeqCst) {
            Err(Error::Cancelled)
        } else {
            Ok(())
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Receipt {
    pub directory: PathBuf,
    pub files: Vec<PathBuf>,
    pub warnings: Vec<String>,
}

pub fn extension(path: &std::path::Path) -> String {
    path.extension()
        .and_then(|s| s.to_str())
        .unwrap_or("")
        .to_ascii_lowercase()
}

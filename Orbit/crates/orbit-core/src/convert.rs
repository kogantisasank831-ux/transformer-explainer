use crate::{
    catalog::{self, IMAGES, SHEETS, SLIDES, WORD},
    extension, process, Cancellation, Engines, Error, Receipt, Request, MAX_INPUT_BYTES,
};
use image::{DynamicImage, ImageDecoder, ImageFormat, ImageReader};
use serde::{Deserialize, Serialize};
use std::{fs, io::BufWriter, path::Path, process::Command};

pub fn convert(
    request: &Request,
    engines: &Engines,
    cancel: &Cancellation,
) -> Result<Receipt, Error> {
    cancel.check()?;
    request.options.validate()?;
    let input = crate::canonical_path(&request.input)?;
    if !input.is_file() || fs::metadata(&input)?.len() > MAX_INPUT_BYTES {
        return Err(Error::Invalid(
            "Choose a regular file no larger than 250 MiB".into(),
        ));
    }
    let parent = crate::canonical_path(&request.output_dir)?;
    if !parent.is_dir() {
        return Err(Error::Invalid("Output folder does not exist".into()));
    }
    let format = request.format.to_ascii_lowercase();
    let route = catalog::formats(&input, engines)
        .into_iter()
        .find(|f| f.id == format)
        .ok_or_else(|| Error::Invalid("This input/output conversion is not supported".into()))?;
    if !route.available {
        return Err(Error::MissingEngine(route.requires));
    }
    let ext = extension(&input);
    let stage = tempfile::Builder::new()
        .prefix(".orbit-")
        .tempdir_in(&parent)?;
    let work = stage.path().join("work");
    fs::create_dir(&work)?;
    let out = stage.path().join("output");
    fs::create_dir(&out)?;
    // Work on a neutral, isolated copy. LibreOffice never sees user-controlled option-like names.
    let safe_input = work.join(format!("source.{ext}"));
    fs::copy(&input, &safe_input)?;
    cancel.check()?;
    let native = IMAGES.contains(&ext.as_str()) && IMAGES.contains(&format.as_str());
    let mut warnings = Vec::new();
    if native {
        convert_image(
            &safe_input,
            &out.join(format!("converted.{format}")),
            &format,
            request.options.quality,
        )?;
    } else if WORD.contains(&ext.as_str())
        || SHEETS.contains(&ext.as_str())
        || SLIDES.contains(&ext.as_str())
    {
        office(request, &safe_input, &out, engines, cancel)?;
        warnings.push("Office layout can change when fonts or application-specific features differ. Review the result.".into());
        if ["csv", "tsv"].contains(&format.as_str()) {
            warnings.push(
                "Only the first worksheet is exported; formatting and formulas are not preserved."
                    .into(),
            );
        }
    } else {
        warnings.extend(worker(request, &safe_input, &out, &work, engines, cancel)?);
    }
    cancel.check()?;
    let mut files: Vec<_> = fs::read_dir(&out)?
        .filter_map(Result::ok)
        .map(|e| e.path())
        .filter(|p| p.is_file())
        .collect();
    files.sort();
    if files.is_empty()
        || files
            .iter()
            .any(|p| fs::metadata(p).map(|m| m.len() == 0).unwrap_or(true))
    {
        return Err(Error::Engine("The engine produced no usable output".into()));
    }
    let stem: String = input
        .file_stem()
        .and_then(|s| s.to_str())
        .unwrap_or("converted")
        .chars()
        .map(|c| {
            if c.is_alphanumeric() || "-_ ".contains(c) {
                c
            } else {
                '_'
            }
        })
        .take(50)
        .collect();
    let final_dir = parent.join(format!("{}_orbit_{}", stem, uuid::Uuid::new_v4().simple()));
    // Publishing the entire output folder atomically prevents partial or overwritten files.
    cancel.check()?;
    fs::rename(&out, &final_dir)?;
    let files = files
        .iter()
        .map(|p| final_dir.join(p.file_name().unwrap_or_default()))
        .collect();
    Ok(Receipt {
        directory: final_dir,
        files,
        warnings,
    })
}

fn convert_image(input: &Path, output: &Path, format: &str, quality: u8) -> Result<(), Error> {
    let mut reader = ImageReader::open(input)?.with_guessed_format()?;
    let mut limits = image::Limits::default();
    limits.max_alloc = Some(512 * 1024 * 1024);
    limits.max_image_width = Some(24_000);
    limits.max_image_height = Some(24_000);
    reader.limits(limits);
    let mut decoder = reader.into_decoder()?;
    let orientation = decoder.orientation()?;
    let mut img = DynamicImage::from_decoder(decoder)?;
    img.apply_orientation(orientation);
    if img.width() as u64 * img.height() as u64 > 50_000_000 {
        return Err(Error::Invalid("Images are limited to 50 megapixels".into()));
    }
    let mut file = BufWriter::new(fs::File::create(output)?);
    if format == "jpg" {
        let mut rgb = img.to_rgba8();
        for pixel in rgb.pixels_mut() {
            let a = pixel[3] as u32;
            for c in 0..3 {
                pixel[c] = ((pixel[c] as u32 * a + 255 * (255 - a) + 127) / 255) as u8;
            }
            pixel[3] = 255;
        }
        image::codecs::jpeg::JpegEncoder::new_with_quality(&mut file, quality)
            .encode_image(&DynamicImage::ImageRgba8(rgb).to_rgb8())?;
    } else {
        let f = match format {
            "png" => ImageFormat::Png,
            "webp" => ImageFormat::WebP,
            "tiff" => ImageFormat::Tiff,
            "bmp" => ImageFormat::Bmp,
            _ => return Err(Error::Invalid("Unsupported image output".into())),
        };
        // Restrict output bit depths to widely interoperable eight-bit images.
        DynamicImage::ImageRgba8(img.to_rgba8()).write_to(&mut file, f)?;
    }
    use std::io::Write;
    file.flush()?;
    Ok(())
}

fn office(
    request: &Request,
    input: &Path,
    out: &Path,
    engines: &Engines,
    cancel: &Cancellation,
) -> Result<(), Error> {
    let program = engines
        .office
        .as_ref()
        .ok_or_else(|| Error::MissingEngine("LibreOffice".into()))?;
    let profile = tempfile::tempdir()?;
    let profile_url = file_url(profile.path())?;
    let ext = extension(input);
    let family = if SHEETS.contains(&ext.as_str()) {
        "calc"
    } else if SLIDES.contains(&ext.as_str()) {
        "impress"
    } else {
        "writer"
    };
    let format = request.format.to_ascii_lowercase();
    let export = if format == "pdf" {
        let mut options = serde_json::Map::new();
        if !request.options.pages.trim().is_empty() {
            options.insert(
                "PageRange".into(),
                serde_json::json!({"type":"string","value":request.options.pages}),
            );
        }
        if family == "calc" {
            options.insert(
                "SinglePageSheets".into(),
                serde_json::json!({"type":"boolean","value":request.options.single_page_sheets}),
            );
        }
        format!(
            "pdf:{family}_pdf_Export:{}",
            serde_json::Value::Object(options)
        )
    } else if format == "csv" || format == "tsv" {
        let sep = if format == "tsv" { 9 } else { 44 };
        // UTF-8; quoted strings; export cell values, first sheet only (sheet index 0).
        format!(
            "{format}:Text - txt - csv (StarCalc):{sep},34,76,1,,0,false,true,false,false,false,0"
        )
    } else {
        format.clone()
    };
    let mut command = Command::new(program);
    command
        .arg(format!("-env:UserInstallation={profile_url}"))
        .args([
            "--headless",
            "--nologo",
            "--nodefault",
            "--nolockcheck",
            "--norestore",
            "--convert-to",
        ])
        .arg(export)
        .arg("--outdir")
        .arg(out)
        .arg(input);
    process::run(&mut command, cancel)?;
    if !fs::read_dir(out)?
        .filter_map(Result::ok)
        .any(|e| extension(&e.path()) == format)
    {
        return Err(Error::Engine("LibreOffice could not export this file. Check for corruption, passwords or unsupported content.".into()));
    }
    Ok(())
}

fn file_url(path: &Path) -> Result<String, Error> {
    let path = path.canonicalize()?.to_string_lossy().replace('\\', "/");
    let path = path.strip_prefix("//?/").unwrap_or(&path);
    let mut encoded = String::new();
    for b in path.bytes() {
        if b.is_ascii_alphanumeric() || b"/-_.~:".contains(&b) {
            encoded.push(b as char);
        } else {
            encoded.push_str(&format!("%{b:02X}"));
        }
    }
    Ok(if encoded.starts_with('/') {
        format!("file://{encoded}")
    } else {
        format!("file:///{encoded}")
    })
}

#[derive(Serialize)]
struct WorkerRequest<'a> {
    input: &'a Path,
    output_dir: &'a Path,
    format: &'a str,
    options: &'a crate::Options,
    tesseract: &'a Option<std::path::PathBuf>,
}
#[derive(Deserialize)]
struct WorkerResponse {
    #[serde(default)]
    warnings: Vec<String>,
}

fn worker(
    request: &Request,
    input: &Path,
    out: &Path,
    work: &Path,
    engines: &Engines,
    cancel: &Cancellation,
) -> Result<Vec<String>, Error> {
    let request_path = work.join("request.json");
    let response_path = work.join("response.json");
    fs::write(
        &request_path,
        serde_json::to_vec(&WorkerRequest {
            input,
            output_dir: out,
            format: &request.format.to_ascii_lowercase(),
            options: &request.options,
            tesseract: &engines.tesseract,
        })?,
    )?;
    let mut command = if let Some(binary) = &engines.worker {
        Command::new(binary)
    } else {
        let mut c = Command::new(
            engines
                .python
                .as_ref()
                .ok_or_else(|| Error::MissingEngine("PDF worker".into()))?,
        );
        c.arg(
            engines
                .script
                .as_ref()
                .ok_or_else(|| Error::MissingEngine("PDF worker script".into()))?,
        );
        c
    };
    command
        .arg("--request")
        .arg(request_path)
        .arg("--response")
        .arg(&response_path);
    process::run(&mut command, cancel)?;
    let response: WorkerResponse = serde_json::from_slice(&fs::read(response_path)?)?;
    Ok(response.warnings)
}

#[cfg(test)]
mod tests {
    use super::*;
    use image::GenericImageView;
    #[test]
    fn real_image_conversion_does_not_overwrite_original() {
        let dir = tempfile::tempdir().unwrap();
        let source = dir.path().join("photo.png");
        image::RgbaImage::from_pixel(8, 8, image::Rgba([255, 0, 0, 128]))
            .save(&source)
            .unwrap();
        let before = fs::read(&source).unwrap();
        let req = Request {
            input: source.clone(),
            output_dir: dir.path().into(),
            format: "jpg".into(),
            options: Default::default(),
        };
        let a = convert(&req, &Engines::default(), &Cancellation::default()).unwrap();
        let b = convert(&req, &Engines::default(), &Cancellation::default()).unwrap();
        assert_ne!(a.directory, b.directory);
        assert_eq!(fs::read(source).unwrap(), before);
        let pixel = image::open(&a.files[0]).unwrap().get_pixel(0, 0);
        assert!(pixel[0] > 240 && pixel[1] > 110 && pixel[1] < 145);
    }
    #[test]
    fn cancellation_leaves_no_output() {
        let dir = tempfile::tempdir().unwrap();
        let cancel = Cancellation::default();
        cancel.cancel();
        let req = Request {
            input: dir.path().join("absent"),
            output_dir: dir.path().into(),
            format: "png".into(),
            options: Default::default(),
        };
        assert!(matches!(
            convert(&req, &Engines::default(), &cancel),
            Err(Error::Cancelled)
        ));
        assert_eq!(fs::read_dir(dir.path()).unwrap().count(), 0);
    }
    #[test]
    fn reject_invalid_options_and_unsupported_pair() {
        let mut opts = crate::Options::default();
        opts.language = "eng;malicious".into();
        assert!(opts.validate().is_err());
        let dir = tempfile::tempdir().unwrap();
        let source = dir.path().join("a.txt");
        fs::write(&source, "hello").unwrap();
        let req = Request {
            input: source,
            output_dir: dir.path().into(),
            format: "xlsx".into(),
            options: Default::default(),
        };
        assert!(matches!(
            convert(&req, &Engines::default(), &Cancellation::default()),
            Err(Error::Invalid(_))
        ));
    }
}

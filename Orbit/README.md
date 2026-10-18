# Orbit

A local file converter for Windows and macOS. Drop files, choose a destination
format around a circular wheel, then convert them in a background queue.

**Native Windows x64, Apple Silicon and Intel Mac installers are available in
the [successful build run](https://github.com/kogantisasank831-ux/transformer-explainer/actions/runs/39153907673).** Native build scripts and a GitHub Actions workflow are
included. Rust powers the desktop host, conversion policy, queue, cancellation
and image codecs. A small Python worker handles PDF reconstruction and OCR; it
can be bundled into an executable, so end users of a packaged build do not need
Python. Office conversion uses a separately installed LibreOffice.

## What works

| Input | Output | Engine / behaviour |
| --- | --- | --- |
| JPG/JPEG, PNG, WebP, TIFF, BMP | JPG, PNG, WebP, TIFF, BMP | Native Rust; JPEG quality control; transparent JPEG areas become white |
| Those images | PDF | Bundled PDF worker; one image per PDF |
| Those images | TXT | Tesseract OCR; printed text, not handwriting recognition |
| DOC/DOCX, ODT, RTF | PDF, DOCX, ODT, RTF, TXT, HTML | LibreOffice; the source's own format is excluded |
| XLS/XLSX, ODS, CSV, TSV | PDF, XLSX, ODS, CSV, TSV | LibreOffice; CSV/TSV exports the first sheet as values |
| PPT/PPTX, ODP | PDF, PPTX, ODP | LibreOffice; PDF contains static slides |
| PDF | DOCX | Editable text and tables, or page images that are not editable |
| PDF | XLSX / CSV | Detected tables only; one worksheet/CSV per table |
| PDF | JPG / PNG | One image per selected page; 72–300 DPI |
| PDF | TXT | Embedded text, or optional OCR on pages without extracted text |

The wheel only shows valid routes for that file family. Missing engines disable
their choices. PDF -> Excel does not restore formulas, macros, charts or an
original workbook. Editable PDF -> Word omits embedded pictures and rebuilds
text/tables with simple styling. Use page-image mode when page appearance matters
more than editing. Both modes need review on complex documents.

## Desktop features

- Drag and drop or a native file picker; circular format selection.
- Optional always-on-top drop window. Drop there to open the wheel in the main window.
- Up to 100 files in a selection and 100 active/queued jobs, 250 MiB per input.
- Apply a format to every compatible selected file, with an explicit count of excluded files.
- Serial conversion queue with live states, errors, cancellation and “Show in folder”.
- PDF page ranges, editable/page-image Word mode, OCR toggle/language, JPEG quality and PDF render DPI.
- Excel PDF export using workbook print settings, or one PDF page per sheet.
- Automatic engine detection and executable overrides in Settings.
- Each conversion publishes a new uniquely named output folder. Originals are never overwritten.
- Partial output is staged and removed on error/cancellation. Queue history lasts for the current session.
- Native image EXIF orientation is applied; converted image metadata is not guaranteed to be retained.

There is no account, API key, cloud conversion or automatic model download.
Installing/building dependencies requires internet access; conversions run locally.

## Run from source on Windows

Install these first:

1. [Rust](https://rustup.rs/) using its default MSVC toolchain.
2. Visual Studio Build Tools with **Desktop development with C++**.
3. [Node.js](https://nodejs.org/) 22 LTS and [Python](https://www.python.org/downloads/) 3.12.
4. Microsoft Edge WebView2 Runtime, normally already present on Windows 11.
5. [LibreOffice](https://www.libreoffice.org/download/download-libreoffice/) if you want Office conversion.
6. Tesseract with the desired language data if you want OCR. Tesseract's official
   installation information is at https://tesseract-ocr.github.io/tessdoc/Installation.html.

Open PowerShell in the extracted Orbit folder:

```powershell
.\scripts\setup-dev.ps1
npm run desktop
```

The setup script creates a project-local `.venv`, installs worker dependencies
and runs `npm ci`. It does not install Rust, Office software or system packages.

## Run from source on macOS

Install Apple's command line tools, Rust, Node.js 22 LTS and Python 3.12. Install
LibreOffice for Office conversion and Tesseract for optional OCR.

```bash
xcode-select --install
bash scripts/setup-dev.sh
npm run desktop
```

If an engine is not detected, open **Settings**, choose its executable, then click
**Save & check**. Common LibreOffice paths are:

- Windows: `C:\Program Files\LibreOffice\program\soffice.com`
- macOS: `/Applications/LibreOffice.app/Contents/MacOS/soffice`

For development Python, choose `.venv\Scripts\python.exe` on Windows or
`.venv/bin/python` on macOS. Packaged builds use the bundled worker instead.
The chosen OCR language must be installed in Tesseract (for example, `eng`).

## Convert a file

1. Drop the file into Orbit. The 360-degree wheel opens around its file type.
2. Click a format and review the conversion note.
3. For PDF input, optionally select pages such as `1-3,5`.
4. Choose the save location. The default is each source file's folder.
5. Click **Convert**. Finished jobs have **Show in folder**.

Each job creates a folder similar to `report_orbit_<unique-id>`. Per-page and
per-table conversions can create multiple files inside it. If the source folder
is read-only, choose another output folder before starting.

PDFs are limited to 300 pages per job. Native image inputs are limited to 50
megapixels and 512 MiB of decoder allocation; PDF page rendering is limited to
40 megapixels per page. External conversion commands time out after 10 minutes.
Cancellation kills external process trees. Native image codecs finish their
current codec call before the cancellation check prevents publication.

## Build native installers

For an existing repository with Orbit in a subfolder, see
[`docs/NATIVE_BUILDS.md`](docs/NATIVE_BUILDS.md). The included preparation script
creates a dedicated root workflow without touching other project files.

Build separately on each target operating system and architecture. A worker
compiled on Linux cannot be shipped with a Windows or macOS app.

Windows:

```powershell
.venv\Scripts\python.exe scripts\build-engine.py
npm run package
```

macOS:

```bash
.venv/bin/python scripts/build-engine.py
npm run package
```

Outputs appear under `target/release/bundle/`: NSIS `.exe` / `.msi` on Windows;
`.app` / `.dmg` on macOS. The PDF worker is bundled. LibreOffice, Tesseract and
language data remain separate local installations. First startup may take a few
seconds while the packaged worker extracts its runtime.

The included `.github/workflows/desktop.yml` runs tests and builds native
Windows x64, Apple Silicon and Intel Mac installers. It can be run manually
through GitHub Actions or using an `orbit-v*` tag. It uploads build artifacts;
it does not publish a GitHub release. All three native jobs passed in the linked
build run. Release signing/notarization credentials are not configured.

## Tests

```bash
cargo test -p orbit-core --locked
python -m pytest engine/test_worker.py -q
npm test
npm run build
cargo check -p orbit --locked
```

Use the Python inside `.venv` for Python commands if it is not activated.
For browser interaction checks:

```bash
npx playwright install chromium
npm run test:ui
```

`ORBIT_BROWSER` can point to an already installed Chromium executable. Browser
preview deliberately cannot read local paths or convert files. It provides
sample selections for inspecting the interface; the desktop app performs work.

For integration checks against the real Rust host and local engines:

```bash
cargo build -p orbit-core --bin orbit-convert --locked
python scripts/smoke.py
```

After building the worker, `python scripts/check-packaged.py` runs those checks
against the bundled executable instead of the Python source.

See `docs/VALIDATION.md` for the checks actually performed for this delivery.

## Layout

- `crates/orbit-core/`: Rust request validation, routes, codecs, process management and headless CLI.
- `src-tauri/`: desktop commands, job queue, settings, floating drop window and packaging.
- `ui/`: format wheel and desktop interface in JavaScript/CSS; no frontend conversion logic.
- `engine/worker.py`: validated request/response PDF/OCR worker.
- `scripts/`: setup, native worker build and smoke checks.
- `docs/ARCHITECTURE.md`: code flow and extension points.

This is a first implementation. It does not include a document editor, a
before-conversion content preview, audio/video conversion, HEIC/AVIF, an updater,
OS context-menu integration, or a global wheel that appears over other apps.
The floating drop target opens the wheel in Orbit's main window.


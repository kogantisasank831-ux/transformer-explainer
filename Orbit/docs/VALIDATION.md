# Delivery validation

This report records checks performed in the Linux development environment.
It is not a claim that Windows/macOS installers have been built or tested.

## Completed checks

| Check | Result |
| --- | --- |
| `cargo test -p orbit-core --locked` | 6 passed, including real image conversion, no-overwrite behaviour, request rejection and live subprocess cancellation |
| `python -m pytest engine/test_worker.py -q` | 14 passed, including PDF -> editable Word, page-image Word, Excel cells, CSV, text, page images, image -> PDF and real scanned-page OCR |
| `npm test` | 3 passed: cross-platform paths, compatible batch filtering and late-event job state handling |
| Browser interaction smoke | Passed format-wheel selection, Word modes, Excel PDF options, Settings and no horizontal overflow at 320, 390, 760 and 1120 pixels |
| `npm run build` | Passed; production interface assets generated |
| `cargo check -p orbit --locked` | Passed for the full Tauri desktop application |
| `cargo clippy --workspace --locked -- -D warnings` | Passed |
| `cargo check -p orbit --features custom-protocol --locked` | Passed for embedded production interface assets |
| Real source-worker integration smoke | 19 conversion operations passed through the Rust CLI; source bytes remained unchanged |
| Linux packaged worker | Built successfully with PyInstaller; dependency doctor reported ready |
| Packaged-worker integration smoke | 24 conversion operations passed through the Rust CLI, including reconstructed Word, Excel tables, CSV, OCR-independent PDF text and page rendering |
| Packaged worker borderless-table regression | Passed; headings and right-aligned numeric values stayed in their intended columns |

The source-worker integration checks covered PNG -> JPG/WebP/TIFF/BMP/PDF,
PDF -> PNG, DOCX -> PDF/ODT/RTF/TXT/HTML, PDF -> DOCX/TXT,
XLSX -> PDF/CSV/TSV/ODS, and exported Excel PDF -> XLSX/CSV.

The borderless-table check reproduced a real Excel export with left-aligned
headings and right-aligned numbers. The updated extractor retained `Product`,
`Quantity`, `Apples`, `12`, `Oranges` and `8` in their intended columns. A
regression fixture was added to the worker test suite.

## Environment

- Rust 1.99.1; Tauri Rust 2.12.4; Tauri CLI 2.12.3.
- Node.js 24.19.0; Vite 7.3.7; Playwright 1.64.1.
- Python 3.12.14; Pydantic 2.14.0.
- pdfplumber 0.11.9; pypdfium2 5.14.0.
- python-docx 1.2.0; openpyxl 3.1.5; Pillow 12.3.0.
- PyInstaller 6.22.3; local LibreOffice and Tesseract available.

The desktop compilation used locally extracted GTK/WebKit development
dependencies because this execution environment does not provide a native
Windows or macOS toolchain. Browser checks exercised the actual interface,
using its clearly labelled browser-preview mode. They did not simulate
successful desktop conversions.

## Native validation still required

- Execute the supplied GitHub Actions workflow or build on Windows and macOS.
- Install and open the resulting native installers on the target machines.
- Exercise native drag/drop, executable discovery, floating-window focus,
  cancellation/closing and output-folder opening on those operating systems.
- Review representative real documents, including fonts, merged cells,
  scanned pages and multilingual content.
- Configure signing/notarization for a public release if distributing one.

The supplied workflow builds Windows x64, Apple Silicon and Intel Mac packages.
No repository was changed, no workflow was run remotely and no release was
published during this task.

## Installer preparation follow-up

Added a workflow template for placing Orbit in an existing repository, host
architecture validation, native tool installation, mandatory Office smoke
coverage, cross-platform OCR test fonts, and installer/checksum collection.
Local checks cover preparing the folder layout, preventing overwrites, collecting
the expected installer types, generating matching checksums and parsing the
workflow. These checks do not substitute for native installer execution.

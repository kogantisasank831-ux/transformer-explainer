# How Orbit works

## One job, from drop to output

Tauri receives native file-drop events and the interface asks Rust to inspect
each path. Rust canonicalises paths, checks file size and computes compatible
formats. Nothing is uploaded. The interface renders those choices around a
circle, disables missing engines and exposes format-specific settings.

Clicking Convert creates an explicit Request: source path, output folder,
target format and validated options. The desktop host inserts a queued Job in
its registry, sends it to a bounded channel and returns the job ID. One worker
thread consumes jobs serially. UI events carry job states; the UI also fetches
an initial snapshot so existing session jobs are visible after reload.

The core canonicalises paths again, validates the input/output pair, checks the
250 MiB bound and creates a temporary staging folder inside the destination.
It copies the source under a neutral filename into the work subfolder. This
isolates Office tools from unusual filenames and prevents editing originals.
Windows canonical paths are normalised for compatibility with external Office
applications, while retaining verbatim paths when they are required.

The appropriate engine writes into a separate output subfolder:

- **Rust image codecs:** JPG, PNG, WebP, TIFF and BMP. EXIF orientation is applied.
  JPEG output composites transparency onto white; WebP encoding is lossless.
- **LibreOffice:** invoked headlessly with an isolated profile and explicit
  export filters. Spreadsheet CSV/TSV routes select the first sheet and values.
- **PDF worker:** runs as a bundled executable or through project-local Python
  in development. Requests and responses travel through small JSON files.

After success, the core checks for nonempty outputs and cancellation. It then
renames the whole output directory into a unique final folder on the same
filesystem. A receipt lists the output files and conversion warnings. Temporary
work is removed by RAII. Failure and cancellation leave no published result.

## Cancellation and errors

Each job owns an atomic cancellation token. Queued jobs check it before
starting. Running commands are polled every 80 ms. On Unix they run in a new
process group; cancellation kills that group. Windows uses taskkill with /T /F
to terminate descendants, then waits for the direct child. Commands receive
argument arrays rather than shell-concatenated strings. Output is redirected
to temporary log files to avoid pipe deadlocks; error messages are bounded.

Rust image codecs run synchronously, so cancellation takes effect when the
codec call returns. Closing Orbit cancels jobs and waits for cleanup before
exiting. There are no fabricated percentage estimates: running jobs display
an indeterminate state. Logs include job IDs, conversion formats and failures.

## PDF reconstruction

PDFium rasterises pages. pdfplumber extracts embedded text and finds tables.
Ruled tables use their detected cell boundaries. For unruled tables, the worker
also groups text by lines and whitespace gaps; this handles common documents
whose headings are left-aligned while numbers are right-aligned. Detection is
heuristic and can split or merge cells; extracted tables always need review.

Excel output creates one sheet per detected table using openpyxl. Values are
strings; inferred original numeric types and formulas are not invented.
Formula-like extracted strings are neutralised before CSV/XLSX export.

Editable Word output sorts extracted text lines and tables by vertical position
and writes a DOCX using python-docx. This is content reconstruction, not an
inverse of PDF rendering. It omits pictures, drawings, exact fonts and styling.
The alternative mode embeds raster page images in Word instead.

When enabled, OCR is used on pages with no extracted text, or as a fallback
when table detection found no table. Tesseract reads rendered page images and
returns TSV word boxes. OCR table columns use whitespace heuristics; results
carry an explicit review warning. Mixed pages containing some embedded text
and additional scanned text are not fully reconstructed by this fallback.

## Engine discovery

Settings and ORBIT_* environment overrides are checked, then normal install
locations and PATH. For development the host checks the project's .venv.
A packaged worker is preferred. A worker doctor invocation verifies its imports
before PDF routes are enabled. Office and OCR executable discovery is based on
file presence; execution and language-data errors are reported per conversion.

Environment overrides: ORBIT_OFFICE, ORBIT_ENGINE, ORBIT_ENGINE_PYTHON,
ORBIT_ENGINE_SCRIPT (CLI only), ORBIT_TESSERACT. Settings are stored in Tauri's
platform-specific application configuration folder. Queue history is in memory.
Source contents and converted documents are not stored there.

## Extending formats

Add a route in `catalog.rs`, implement its conversion in the core or worker,
then add settings only when they affect the conversion. Include a real fixture
round trip or content check. A codec's ability to read a format does not imply
that it can write that format. Animated images, colour profiles and metadata
require explicit treatment rather than assuming extension parity.

## Distribution

Tauri uses the operating system's webview for the interface. Only local native
commands and file dialogs are exposed. The production CSP has no external
network destinations. The worker is packaged with PyInstaller on each target
platform and copied to the target-triple filename expected by Tauri's external
binary bundler. The configuration overlay enables this worker for release
packages; development does not require a prebuilt sidecar.

Rust and JavaScript dependencies have lockfiles. Python requirement ranges are
recorded in requirements.txt; `docs/VALIDATION.md` records the environment used
for delivery. Platform installer generation and real Windows/macOS testing
remain distinct from Linux source checks and worker packaging verification.

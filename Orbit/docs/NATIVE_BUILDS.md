# Native installers: prepared next step

Orbit's conversion code has been tested as recorded in VALIDATION.md. Native
Windows and macOS installers have **not** yet been generated for this delivery.
The build workflow needs a repository destination before it can run remotely.

## Standalone repository

Put the contents of the Orbit source folder at the repository root. The existing
`.github/workflows/desktop.yml` builds native installers using Actions.

## Orbit inside an existing repository

Use the additive preparation script to create an isolated source folder and
dedicated root workflow:

```bash
python scripts/prepare-repository.py /path/to/existing-checkout --folder Orbit
```

The script adds `Orbit/` and `.github/workflows/orbit-desktop.yml`. It refuses to
overwrite either location. It does not initialise Git, commit, push, publish or
start a remote build. The workflow template lives in
`docs/github-folder/orbit-desktop.yml` for review before use.

After committing the prepared files to an `orbit-build/*` branch, a push starts
the dedicated workflow. It can also run for pull requests or manually after
the workflow is available on the default branch. The workflow checks out the
Orbit folder rather than unrelated repository directories.

| Build | Runner | Expected artifacts |
| --- | --- | --- |
| Windows x64 | windows-latest | EXE installer and MSI |
| Apple Silicon | macos-14 | DMG |
| Intel Mac | macos-15-intel | DMG |

Each job checks its Rust host architecture, installs LibreOffice and Tesseract,
runs Rust/PDF/OCR/interface tests, bundles the PDF worker and exercises packaged
conversions through Rust. LibreOffice discovery is mandatory for these checks,
so Office conversion coverage cannot silently disappear from the run.

The finished installers have stable filenames and SHA-256 checksums, and are
attached as workflow artifacts for 14 days. The workflow does not create a
public GitHub release. Windows signing and macOS signing/notarization are not
configured; these are development builds, not a signed public distribution.

Installing tools on build runners does not bundle them into Orbit. End users
still install LibreOffice for Office conversions and Tesseract for optional
OCR. The PDF worker is included in Orbit's installer.

## Current status

- Prepared the folder-based workflow, architecture check, installer collection
  and checksum generation.
- Checked preparation without modifying an existing repository, including
  refusal to overwrite existing source/workflow paths.
- Native runner builds, installer execution and OS-specific drag/drop testing
  still require the actual Windows/macOS build run.


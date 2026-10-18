# How the app works

The interface is Python/PySide6. A dedicated C++17 child process owns Sony's SDK connection. Keeping the proprietary SDK behind a small process boundary separates the interface from native callback lifetimes and lets an unresponsive engine be terminated without calling it from the UI thread.

| Component | Responsibility |
| --- | --- |
| `alphalink/gui.py` | Desktop UI, one background job at a time, signals to update progress, pairing/fingerprint dialog and Quick Look. |
| `alphalink/bridge.py` | Launch the worker; serialize commands; parse framed replies; enforce watchdog timeouts; clear connection state after errors. |
| `native/worker.cpp` | Original adapter to Sony SDK 2.02: discover, fingerprint, connect in ContentsTransfer mode, list date folders and contents, download originals, await callbacks, cancel on timeout, disconnect before releasing resources. |
| `alphalink/models.py` | Immutable camera/media values; filename and date-folder validation; camera/metadata identity independent of session-local handles. |
| `alphalink/transfers.py` | Destination validation, disk-space check, staging, size verification, local SHA-256, atomic non-overwriting hard-link publication and SQLite receipts. |
| `alphalink/demo.py` | Explicit simulation with generated BMP test images. It is never a fallback for a failed camera connection. |
| `scripts/build_mac.py` | Compile against a user-supplied Sony SDK, retain Sony's adapter layout, package and ad-hoc sign a local macOS app. |

## Camera session

The adapter uses `Init`, `EnumCameraObjects`, `CreateCameraObjectInfo`, `GetFingerprint` when SSH is supported, and `Connect` with `CrSdkControlMode_ContentsTransfer`. It waits for `OnConnected` rather than assuming a successful initial return means the session is ready.

Card listing uses `GetDateFolderList`, `GetContentsHandleList` and `GetContentsDetailInfo`. The corresponding list allocations are released even when metadata retrieval fails. SDK content objects remain local and are destructed normally.

A download refreshes the file detail first, then calls `PullContentsFile` with `CrPropertyStillImageTransSize_Original` and an explicit staging directory/filename. The main worker thread waits on a condition variable. SDK callback threads signal completion/error; file size is sampled for progress while waiting. This does not invent a percentage from elapsed time.

On timeout the adapter requests cancellation with the documented Down/Up command sequence, waits for callback/closure, and disconnects. Resources are released after disconnection acknowledgement. If safe acknowledgement cannot be established, the worker process exits. Python does not publish the staged file on any error.

No SDK delete, format, capture or camera-configuration-write operation is exposed.

## Process protocol

The parent writes one command at a time to private stdin. Commands use whitespace-separated numeric arguments and hex-encoded UTF-8 strings. Empty strings use `-`. Hex encoding prevents filenames, passwords, spaces and newlines from becoming protocol separators. No shell executes these strings.

Responses are UTF-8 JSON lines prefixed with `@alphalink `. Success is `{"ok":true,"data":...}`, failure is `{"ok":false,"error":...}`, and progress is `{"event":"progress","bytes":...}`. Non-protocol SDK stdout is ignored. The wrapper consumes output on a reader thread and enforces a watchdog while the GUI stays responsive.

## File integrity and recovery

1. Identify the remote media with camera GUID/MAC, date folder, filename, size and capture timestamp. SDK handles identify only the current session.
2. Recheck any matching receipt using local size and SHA-256. A different destination has separate receipts.
3. Download into a unique staging directory under the final date directory.
4. Require successful SDK completion and exact reported byte count.
5. Compute a local SHA-256; sync file contents to disk.
6. Atomically create the final name with a hard link. Collision names use numeric suffixes. Existing files are never overwritten.
7. Commit the receipt, then remove the staging directory.

The checksum is computed on the Mac. Sony's transfer API does not supply a remote checksum here, so this does not provide cryptographic end-to-end verification against a camera checksum. Camera files are not modified. Interrupted imports remain in marked staging directories and start again on retry.

There is a crash window after publication but before receipt commit. In that case a later retry can create a second copy; it will not overwrite or delete the earlier copy. The app makes no multi-process coordination promise beyond non-overwriting publication. Use one AlphaLink instance per camera.

## Concurrency and limits

One SDK session, one UI background job, one download at a time. This avoids competing requests against a single camera and keeps SDK handle ownership clear. Python integers and Qt object signals preserve byte counts for videos larger than 4 GB. Large media content streams through Sony's SDK to disk; Python does not load a whole video into memory.

The UI lists metadata, not remote thumbnails. Directory listing can take time for large cards. It does not record source EXIF timestamps as filesystem creation dates or normalize Sony codecs. UI defaults and destination are currently per launch; receipts persist.

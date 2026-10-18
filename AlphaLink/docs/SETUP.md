# Set up AlphaLink on your Mac

## What you need

- Sony α6700 (ILCE-6700), a charged battery, a card with a few test images, and firmware appropriate to Sony Camera Remote SDK 2.02.00. The current firmware should be checked on Sony's support page; this project does not install camera firmware.
- macOS 14.1 or later. The packaged dependency set targets Python 3.11–3.13. Build separately on Intel or Apple Silicon; this project does not claim to produce a universal app.
- Python from python.org and Apple Command Line Tools. In Terminal: `xcode-select --install`.
- Sony's [Mac Camera Remote SDK download](https://support.d-imaging.sony.co.jp/app/sdk/licenseagreement_d/en-US.html). Use version 2.02.00 for the header version checked here.

## Build the app

Unzip AlphaLink, run Setup.command, and choose the full Sony Mac SDK ZIP when prompted. The script does not download Sony's SDK or accept its terms for you. It unpacks a temporary copy, compiles the original C++ worker, copies the required SDK runtime files into the app, and uses PyInstaller to package the Python/Qt interface.

If double-clicking the script is unavailable, open Terminal in the project directory and run:

```bash
bash Setup.command /absolute/path/to/CrSDK_v2.02.00_20260610a_Mac.zip
```

All paths with spaces should be quoted. Do not run setup with `sudo`. The completed app is `dist/AlphaLink.app`. This setup is intended for your own local build; it does not sign with an Apple Developer identity or notarize a public release.

For a distributable release, the macOS build and hardware acceptance checks need to pass first. Review dependency/SDK distribution terms, sign nested code with your own Developer ID, enable the appropriate release signing configuration, and notarize using Apple's tools.

## Camera connection: direct Wi-Fi

Sony's a6700 instructions use this menu path (names can vary with firmware):

1. End any active connection from Creators’ App or Imaging Edge. Only one client should own the transfer connection.
2. On camera: **MENU → Network → Cnct./PC Remote → PC Remote Function**. Enable **PC Remote** as applicable to your firmware.
3. Open **Wi-Fi Direct Info** to see the SSID and password.
4. On Mac: use the Wi-Fi menu to join that SSID with that password. A camera hotspot might have no internet; that is expected.
5. Open AlphaLink → **Find camera**. Choose the a6700 → **Connect**.
6. Watch the camera display and accept any pairing/connection request. AlphaLink requests the SDK's **Contents Transfer** session. Follow any on-camera instruction to enter the transfer state.

The Mac joins Wi-Fi using macOS. AlphaLink does not change saved Wi-Fi passwords or silently switch your networks.

## Camera connection: existing Wi-Fi

1. Connect the camera to your access point under **Network → Wi-Fi**.
2. Connect the Mac to the same network. Avoid a guest network that isolates devices.
3. Enable **PC Remote** under **Cnct./PC Remote → PC Remote Function**.
4. If the camera requests access authentication, open **Network → Network Option → Access Authen. Info**. For firmware that requires it, check **Access Authen. Settings → Access Authen.**.
5. Find and connect in AlphaLink. When a fingerprint is shown, compare it to the camera display before continuing. Enter the camera's username and password, not your Apple or Sony account password.

Credentials are sent to the native worker through its private stdin pipe, not through shell arguments or a network web server. They are kept for the session and are not written to application settings. This is not a promise of secure-memory erasure in Python.

## Import workflow

Choose a local APFS/HFS+ destination. Use search or the file-type filter, **Select visible** or individual checkboxes, and **Import selected**. The app puts originals into `chosen-folder/YYYY-MM-DD/` and preserves their bytes and camera filename when possible.

When a filename already exists, the imported file receives a numeric suffix. The app never treats an arbitrary same-name file as a verified duplicate. It skips a prior import only when its receipt is for the same camera, metadata and destination, and its local size and SHA-256 still match.

**Stop after current file** allows the current file to finish and stops the remaining queue. It is not an immediate abort. Closing during an operation also requests that queue behavior and asks you to close again after completion.

Double-click a completed import to open Quick Look. Open the import folder in Finder to use Share/AirDrop or your normal editing application.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Setup cannot find Python | Install Python 3.11, 3.12 or 3.13 and rerun. |
| SDK layout not recognized | Choose Sony's full Mac ZIP, not an unrelated SDK or Windows download. Extracted RemoteCli directories also work through `--sdk`. |
| Compiler missing | Complete Apple's Command Line Tools installation. |
| Engine will not launch | Rebuild on this Mac; use the matching Intel/Apple Silicon Python. Check macOS version and bundle signing. |
| No Wi-Fi camera found | Check the Mac's SSID, PC Remote state, power saving, firewall/local network permission and guest-network isolation. Disconnect USB and other camera clients. |
| Pairing times out | Keep the camera screen visible and confirm its request. End old sessions, power-cycle the camera if needed, then scan again. |
| Authentication fails | Compare the fingerprint and use the camera's Access Authen. Info credentials. Do not disable authentication as a workaround. |
| Card listing rejected | Check firmware and Contents Transfer support/state. The app reports Sony's error code. It does not silently fall back to another protocol. |
| Interrupted import | Completed imports remain saved. Reconnect, refresh the card, and select the files again. A failed file is restarted, not resumed. |
| Hidden partial folders | `.alphalink-partial-*` folders under a date directory contain unfinished downloads. Delete them only when AlphaLink is closed and you no longer need the partial data. |
| Drive does not support hard links | Import to the Mac's APFS/HFS+ disk, then copy finished files to that drive. ExFAT/FAT and arbitrary network shares are not supported import destinations in this version. |

Application logs and receipts are under `~/Library/Application Support/AlphaLink/`. Logs do not intentionally include camera passwords. They can contain imported filenames and local error details.

The transfer timeout scales with reported size, from at least five minutes to at most one day per file. A stalled transfer closes the session; reconnect before retrying. Wi-Fi speed depends on camera settings, distance, interference and file size. No speed has been measured on physical hardware for this delivery.

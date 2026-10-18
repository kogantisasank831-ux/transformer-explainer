# Validation record

Delivery version: 0.1.0. Checked 18 October 2026 in a Linux x86_64 environment.

## Completed checks

**43 tests passed** in the final combined run. The normal test suite runs without a camera. Five native integration tests additionally require separately downloaded Sony headers and a C++ compiler; these were enabled for the delivery run.

```bash
SONY_SDK_HEADERS=/path/to/RemoteCli/app/CRSDK \
QT_QPA_PLATFORM=offscreen python -m pytest -q
# 43 passed
```

| Check | Outcome |
| --- | --- |
| Original native worker compiled against actual Sony 2.02.00 headers | Passed syntax/type checks. |
| Native worker linked to original test-only SDK simulator | Passed. This does not link/run the proprietary Sony Mac binary on Linux. |
| Native discovery, JSON escaping, fingerprint, Contents Transfer connection, listing, asynchronous download and disconnect | Passed against simulator. |
| Native connection callback error, transfer callback error and timeout/cancel path | Passed against simulator. |
| Python subprocess protocol, large byte counts, worker crash, error and watchdog timeout | Passed. |
| Original-byte preservation, repeat import, changed handles and deleted local files | Passed. |
| Same-size corruption detection, destination/camera separation and non-overwriting collisions | Passed. |
| Partial transfer, retry, stop-after-current and low disk space | Passed. |
| Unsafe camera names/date folders and symlink import folders | Passed. |
| Qt interface selection, search and >4 GB progress values | Passed in offscreen UI. |
| Full GUI queue and repeat-import behavior | Passed with generated demo images. |
| SDK ZIP traversal and symlink protection, extracted layout discovery | Passed. |
| Actual official Mac SDK ZIP extraction/layout resolution | Passed. |
| Python compilation and command-script shell syntax | Passed. |
| Interface rendering | Rendered offscreen and visually reviewed; `preview.png` shows the actual explicitly labelled demo interface. |

The test-only SDK simulator validates our process protocol, callback logic and transfer lifecycle. It does not prove Sony's runtime behavior, network pairing, firmware compatibility, adapter loading on macOS, performance or camera-specific file availability.

## Still required on physical hardware

1. Run Setup.command on the target Mac, confirm native linking, app packaging and local-network permission behavior.
2. Discover the α6700 over direct Wi-Fi and over a shared access point.
3. Pair/authenticate, compare the fingerprint and browse the card in Contents Transfer mode.
4. Import original JPEG, HEIF and ARW examples. Compare with card-reader originals, ideally using SHA-256.
5. Import a supported video file larger than 4 GB; check byte count, playback and progress.
6. Test battery/power-saving behavior and disconnect/retry during a transfer.
7. Repeat imports and verify skips, collision handling and stop-after-current behavior.
8. Move the built app to Applications and confirm it still finds SDK adapters and opens Quick Look.
9. Measure actual Wi-Fi throughput/latency on the user's camera/network.

No physical α6700, macOS host, Apple Developer signing identity or notarization service was available in this environment. No precompiled Mac app, DMG, measured transfer speed or hardware certification is claimed.

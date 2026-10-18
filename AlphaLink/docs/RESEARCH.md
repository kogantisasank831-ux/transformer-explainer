# Sony reference and implementation basis

Checked 18 October 2026.

## Creators’ App

Public official product/help material was checked and searches were made for the full official iOS/Android application source. No full official source repository was located. No proprietary mobile app source was inspected or copied, and no APK/IPA decompilation was performed. This finding does not assert that every internal component is closed source; it says the full reference app code was unavailable for this work.

The UX reference is the camera-to-device import workflow. The implementation uses Sony's supported desktop developer SDK instead of claiming the mobile protocol was reproduced.

## Official sources

- [Creators’ App product page](https://creatorscloud.sony.net/catalog/en-in/creatorsapp/index.html)
- [Sony Camera Remote SDK overview and change history](https://support.d-imaging.sony.co.jp/app/sdk/en/index.html)
- [Sony SDK license/download page](https://support.d-imaging.sony.co.jp/app/sdk/licenseagreement_d/en-US.html)
- [Official Mac SDK ZIP 2.02.00](https://di.update.sony.net/NEX/Uhfc28896b/CrSDK_v2.02.00_20260610a_Mac.zip)
- [Sony camera-to-computer connection instructions](https://support.d-imaging.sony.co.jp/app/imagingedge/en/instruction/4_1_connection.php), a6700/7CR/7CM2 section
- [ILCE-6700 camera help guide](https://helpguide.sony.net/ilc/2320/v1/en/index.html)
- [Sony Camera Remote Toolkit platform information](https://pro.sony/en_GB/digital-imaging/camera-remote-toolkit)

## Direct SDK inspection

The Mac archive above was downloaded. `RemoteCli.zip` and `CrSDK_API_Reference_v2.02.00.zip` inside it were inspected locally. These files were used for API verification, not copied into the source delivery.

| SDK file | Verified fact |
| --- | --- |
| API reference: `other/compatibility.html` | ILCE-6700 wireless physical-layer support includes R, C and T. |
| API reference: `function_list/api_list.html` | ILCE-6700 supports Contents Transfer listing/detail/thumbnail/download APIs; this project uses listing/detail/download. |
| `CameraRemote_SDK.h` | Exact discovery, SSH fingerprint, Connect, listing, PullContentsFile and release signatures. |
| `IDeviceCallback.h` | Exact OnConnected, OnDisconnected, OnError and OnNotifyContentsTransfer callback signatures. |
| `CrDeviceProperty.h` | Contents Transfer mode, metadata fields and 64-bit content size. |
| API reference: `command/CrCommandId_CancelContentsTransfer.html` | Cancellation requires Down followed by Up. |
| API reference: `api_reference/connection.html` | Wait for OnDisconnected before ReleaseDevice/Release. |
| SDK sample CMake file | macOS adapter layout under worker executable-directory/Contents/Frameworks/CrAdapter. |
| SDK Mach-O libraries | Provided Mac runtime contains arm64 and x86_64 architectures. Build script compiles the worker for the active Mac architecture. |

This is a software compatibility basis. It does not replace the physical α6700 acceptance test.

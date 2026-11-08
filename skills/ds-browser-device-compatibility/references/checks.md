# Browser and device compatibility checks

- Define engine/version policy, OS, device, viewport/density, input, locale/time zone, network, installed mode and webviews from accepted support policy and real usage evidence.
- Tier required, extended, best-effort and unsupported environments with owners, review cadence and end-of-support behavior; map critical journeys and risky features.
- Prefer standards, feature detection and progressive enhancement. Version transpilation targets, compatibility data and polyfills; test native and fallback paths.
- Cover applicable storage/cookies, CORS/redirects, service workers/caches, streaming, files/media/fonts, localization/IME/RTL and DS charts, large data, model downloads or local inference.
- Automate stable journeys in actual engines and use real devices for touch, keyboard, safe area, memory, media, GPU and OS integration. State emulator and cloud-device limits.
- Control visual-test data, fonts, animation, clock and viewport; verify behavior as well as screenshots and review baselines intentionally.
- Capture exact environment/build/state and reduce failures before using a workaround. Retest the matrix and prevent cross-browser regression.
- Gate required support and review field failures and adoption over time. Compatibility metadata or one emulator is not product evidence.

Use the cross-browser [web-platform-tests project](https://web-platform-tests.org/) and the relevant normative web specifications as primary compatibility references. Product support still requires journey-level evidence on the accepted matrix.

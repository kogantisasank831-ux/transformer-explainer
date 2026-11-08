"""Daily resume/profile updater with observable recency verification. Python 3.11+."""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
import sys
import webbrowser
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Iterator
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

import yaml

LOG = logging.getLogger("profile_updater")


class UpdateError(RuntimeError):
    """An update cannot be performed or verified safely."""


@dataclass(frozen=True)
class UpdateResult:
    status: str
    method: str
    timestamp_before: str
    timestamp_after: str
    content_verified: bool
    resume_sha256: str | None = None


def toggle_space(value: str) -> str:
    match = re.search(r"(?<=\S) {1,2}(?=\S)", value)
    if match is None:
        raise UpdateError("Field needs an internal space between two words")
    replacement = "  " if match.group() == " " else " "
    return value[:match.start()] + replacement + value[match.end():]


def next_variant(current: str, variants: list[str]) -> str:
    if not isinstance(variants, list) or len(variants) != 2 or any(not isinstance(v, str) or not v.strip() for v in variants):
        raise UpdateError("Configure exactly two nonempty, accurate text variants")
    if variants[0] == variants[1]:
        raise UpdateError("Text variants must differ")
    if current not in variants:
        raise UpdateError("Current field differs from both approved variants; review it manually")
    return variants[1] if current == variants[0] else variants[0]


def resume_file(profile: dict[str, Any], base: Path) -> Path:
    maximum = profile.get("max_resume_bytes", 2 * 1024 * 1024)
    if type(maximum) is not int or maximum < 1:
        raise UpdateError("max_resume_bytes must be a positive integer")
    if not isinstance(profile.get("resume_path"), str) or not profile["resume_path"].strip():
        raise UpdateError("Configure a nonempty resume_path")
    path = Path(profile.get("resume_path", ""))
    if not path.is_absolute():
        path = base / path
    if not path.is_file() or path.suffix.lower() not in {".pdf", ".doc", ".docx"}:
        raise UpdateError("resume_path must be an existing PDF, DOC or DOCX file")
    if not 0 < path.stat().st_size <= maximum:
        raise UpdateError("Resume is empty or exceeds max_resume_bytes")
    return path.resolve()


def validate_profile(profile: dict[str, Any], base: Path) -> None:
    if profile.get("mode") not in {"auto", "manual", "disabled"}:
        raise UpdateError("mode must be auto, manual or disabled")
    if not isinstance(profile.get("name"), str) or not profile["name"].strip():
        raise UpdateError("Each profile needs a nonempty name")
    if profile["mode"] == "disabled":
        return
    url = urlparse(profile.get("url", ""))
    if url.scheme != "https" or not url.netloc or url.username or url.password:
        raise UpdateError("Use an HTTPS profile URL without embedded credentials")
    if profile["mode"] == "manual":
        return
    method = profile.get("method")
    if method not in {"resume_upload", "text_variants", "whitespace"}:
        raise UpdateError("Choose resume_upload, text_variants or whitespace")
    required = ["last_updated_selector", "success_selector"]
    if method == "resume_upload":
        required += ["file_input_selector", "resume_name_selector"]
        resume_file(profile, base)
    else:
        required += ["field_selector", "save_selector"]
        if method == "text_variants":
            variants = profile.get("variants", [])
            next_variant(variants[0] if variants else "", variants)
    for key in required:
        if not isinstance(profile.get(key), str) or not profile[key].strip():
            raise UpdateError(f"Configure {key}")
    for key in ("edit_steps", "verification_steps"):
        steps = profile.get(key, [])
        if not isinstance(steps, list) or any(not isinstance(s, str) or not s.strip() for s in steps):
            raise UpdateError(f"{key} must be a list of selector strings")
    if not isinstance(profile.get("verification_attempts", 3), int) or not 1 <= profile.get("verification_attempts", 3) <= 10:
        raise UpdateError("verification_attempts must be between 1 and 10")


def load_config(path: Path) -> dict[str, Any]:
    config = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or not isinstance(config.get("profiles"), list) or not config["profiles"]:
        raise UpdateError("Config needs a nonempty profiles list")
    names: set[str] = set()
    try:
        ZoneInfo(config.get("timezone", "Asia/Kolkata"))
    except (KeyError, TypeError, ValueError) as error:
        raise UpdateError("Configure a valid IANA timezone") from error
    for profile in config["profiles"]:
        if not isinstance(profile, dict):
            raise UpdateError("Each profile must be a mapping")
        validate_profile(profile, path.resolve().parent)
        if profile["name"] in names:
            raise UpdateError("Profile names must be unique")
        names.add(profile["name"])
    return config


def save_state(path: Path, state: dict[str, Any]) -> None:
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, indent=2), encoding="utf-8")
    temporary.replace(path)


def should_skip(entry: Any, today: str) -> bool:
    if isinstance(entry, str):  # Legacy once-per-day state.
        return entry == today
    if not isinstance(entry, dict):
        return False
    if entry.get("status") in {"submitted", "needs_review"}:
        return True  # Could already have saved; never resubmit blindly.
    return entry.get("date") == today and entry.get("status") in {"verified", "reminded"}


def unique(page: Any, selector: str, visible: bool = True) -> Any:
    locator = page.locator(selector)
    locator.wait_for(state="visible" if visible else "attached")
    if locator.count() != 1:
        raise UpdateError("Selector must match exactly one element")
    return locator


def navigate(page: Any, profile: dict[str, Any], steps: str) -> None:
    page.goto(profile["url"], wait_until="domcontentloaded")
    for selector in profile.get(steps, []):
        unique(page, selector).click()


def read_timestamp(page: Any, profile: dict[str, Any]) -> str:
    locator = unique(page, profile["last_updated_selector"])
    attribute = profile.get("last_updated_attribute")
    value = locator.get_attribute(attribute) if attribute else locator.inner_text()
    if not value or not value.strip():
        raise UpdateError("Last-updated indicator is empty")
    return " ".join(value.split())


def update(
    context: Any,
    profile: dict[str, Any],
    dry_run: bool,
    base: Path,
    before_submit: Callable[[], None],
) -> UpdateResult:
    validate_profile(profile, base)
    method = profile["method"]
    page = context.new_page()
    page.set_default_timeout(20_000)
    try:
        navigate(page, profile, "verification_steps")
        before = read_timestamp(page, profile)
        navigate(page, profile, "edit_steps")
        proposed = ""
        resume: Path | None = None
        digest: str | None = None
        if method == "resume_upload":
            resume = resume_file(profile, base)
            digest = hashlib.sha256(resume.read_bytes()).hexdigest()
            target = unique(page, profile["file_input_selector"], visible=False)
        else:
            target = unique(page, profile["field_selector"])
            original = target.input_value()
            proposed = next_variant(original, profile["variants"]) if method == "text_variants" else toggle_space(original)
        # Resolve controls before writing anything. File inputs may auto-submit.
        button = unique(page, profile["save_selector"]) if profile.get("save_selector") else None
        success = page.locator(profile["success_selector"])
        if success.is_visible():
            raise UpdateError("Success indicator already visible; choose a post-save-only indicator")
        if dry_run:
            LOG.info("event=dry_run site=%s method=%s", profile["name"], method)
            return UpdateResult("dry_run", method, before, before, False, digest)
        before_submit()  # Durable journal BEFORE any potentially auto-saving action.
        if resume is not None:
            target.set_input_files(str(resume))
        else:
            target.fill(proposed)
        if button is not None:
            button.click()
        success.wait_for(state="visible")
        after = before
        content_verified = False
        for attempt in range(profile.get("verification_attempts", 3)):
            if attempt:
                page.wait_for_timeout(1000)
            navigate(page, profile, "verification_steps")
            after = read_timestamp(page, profile)
            if resume is not None:
                # Confirms visible filename, not a byte comparison with hosted file.
                name = unique(page, profile["resume_name_selector"]).inner_text().strip()
                content_verified = name == profile.get("expected_resume_name", resume.name)
            else:
                navigate(page, profile, "edit_steps")
                content_verified = unique(page, profile["field_selector"]).input_value() == proposed
            if content_verified and after != before:
                return UpdateResult("verified", method, before, after, True, digest)
        # Coarse dates such as "Today" can make this inconclusive even after a save.
        return UpdateResult("needs_review", method, before, after, content_verified, digest)
    finally:
        page.close()


@contextmanager
def run_lock(runtime: Path) -> Iterator[None]:
    runtime.mkdir(mode=0o700, exist_ok=True)
    lock = (runtime / "run.lock").open("a+b")
    try:
        if sys.platform == "win32":
            import msvcrt
            if lock.seek(0, 2) == 0:
                lock.write(b"0")
                lock.flush()
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield
    finally:
        lock.close()


def run_profiles(config: dict[str, Any], base: Path, dry_run: bool, only: str | None) -> int:
    runtime = base / "runtime"
    state_path = runtime / "state.json"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    today = datetime.now(ZoneInfo(config.get("timezone", "Asia/Kolkata"))).date().isoformat()
    autos = []
    failed = False
    for profile in config["profiles"]:
        name = profile["name"]
        if only and name != only:
            continue
        entry = state.get(name)
        if not dry_run and should_skip(entry, today):
            review = isinstance(entry, dict) and entry.get("status") in {"submitted", "needs_review"}
            LOG.info("event=%s site=%s", "review_required" if review else "already_done_today", name)
            failed |= review
            continue
        if profile["mode"] == "manual":
            LOG.info("event=manual_update_reminder site=%s", name)
            if not dry_run:
                if config.get("open_manual_pages", True):
                    webbrowser.open(profile["url"])
                state[name] = {"date": today, "status": "reminded"}
                save_state(state_path, state)
        elif profile["mode"] == "auto":
            autos.append(profile)
    if autos:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as playwright:
            context = playwright.chromium.launch_persistent_context(str(runtime / "browser"), headless=config.get("headless", True))
            try:
                for profile in autos:
                    name = profile["name"]
                    def journal() -> None:
                        state[name] = {"date": today, "status": "submitted", "method": profile["method"]}
                        save_state(state_path, state)
                    try:
                        result = update(context, profile, dry_run, base, journal)
                        if not dry_run:
                            state[name] = {"date": today, **result.__dict__}
                            save_state(state_path, state)
                            failed |= result.status != "verified"
                            LOG.info("event=%s site=%s content_verified=%s", result.status, name, result.content_verified)
                    except Exception as error:
                        if not dry_run and isinstance(state.get(name), dict) and state[name].get("status") == "submitted":
                            state[name]["status"] = "needs_review"
                            save_state(state_path, state)
                        LOG.error("event=update_failed site=%s error_type=%s", name, type(error).__name__)
                        if isinstance(error, UpdateError):
                            LOG.error("event=configuration_hint detail=%s", error)
                        failed = True
            finally:
                context.close()
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "login", "run", "status", "reset"))
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config.yaml"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--inspect", action="store_true")
    parser.add_argument("--site")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s level=%(levelname)s %(message)s")
    base = args.config.resolve().parent
    try:
        # Login/status/reset remain usable before selectors or resume are configured.
        if args.command in {"validate", "run"}:
            config = load_config(args.config)
        else:
            config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
        if args.site and args.site not in {p["name"] for p in config["profiles"]}:
            raise UpdateError("Unknown --site name")
        if args.command == "validate":
            LOG.info("event=config_valid")
            return 0
        with run_lock(base / "runtime"):
            state_path = base / "runtime" / "state.json"
            if args.command in {"status", "reset"}:
                state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
                if args.command == "reset":
                    if not args.site:
                        raise UpdateError("reset requires --site after you review the saved profile")
                    state.pop(args.site, None)
                    save_state(state_path, state)
                print(json.dumps(state, indent=2))
                return 0
            if args.command == "run":
                return run_profiles(config, base, args.dry_run, args.site)
            from playwright.sync_api import sync_playwright
            with sync_playwright() as playwright:
                context = playwright.chromium.launch_persistent_context(str(base / "runtime" / "browser"), headless=False)
                try:
                    for profile in config["profiles"]:
                        if profile.get("mode") == "auto" and (not args.site or args.site == profile["name"]):
                            context.new_page().goto(profile["url"])
                    input("Log in manually (including OTP/CAPTCHA), then press Enter here: ")
                    if args.inspect:
                        for page in context.pages:
                            page.pause()
                finally:
                    context.close()
            return 0
    except Exception as error:
        LOG.error("event=runner_failed error_type=%s", type(error).__name__)
        if isinstance(error, UpdateError):
            LOG.error("event=configuration_hint detail=%s", error)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

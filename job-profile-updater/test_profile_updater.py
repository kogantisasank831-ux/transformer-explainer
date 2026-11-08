import pytest
from profile_updater import UpdateError, toggle_space


@pytest.mark.parametrize("text", ["Senior Data Scientist", "Senior  Data Scientist", " Python developer ", "Data scientist\nML engineer"])
def test_toggle_is_reversible_and_preserves_words(text: str) -> None:
    changed = toggle_space(text)
    assert changed != text
    assert changed.split() == text.split()
    assert toggle_space(changed) == text


@pytest.mark.parametrize("text", ["", "Developer", "Data\tScientist", "Data   Scientist"])
def test_unsupported_fields_fail_without_modification(text: str) -> None:
    with pytest.raises(UpdateError):
        toggle_space(text)

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
from typing import Any
from playwright.sync_api import sync_playwright
import profile_updater as runner
from profile_updater import next_variant, resume_file, validate_profile, should_skip, update


def test_variant_chooses_alternative_and_protects_manual_edits() -> None:
    assert next_variant('A', ['A', 'B']) == 'B'
    assert next_variant('B', ['A', 'B']) == 'A'
    with pytest.raises(UpdateError):
        next_variant('New manual headline', ['A', 'B'])


@pytest.mark.parametrize('variants', [[], ['A'], ['A', 'A'], ['', 'B'], ['A', 'B', 'C']])
def test_invalid_variants(variants: list[str]) -> None:
    with pytest.raises(UpdateError):
        next_variant('A', variants)


def test_resume_size_extension_and_relative_path(tmp_path: Path) -> None:
    file = tmp_path / 'cv.pdf'
    file.write_bytes(b'%PDF test')
    assert resume_file({'resume_path': 'cv.pdf'}, tmp_path) == file
    with pytest.raises(UpdateError):
        resume_file({'resume_path': 'cv.pdf', 'max_resume_bytes': 1}, tmp_path)
    file.write_bytes(b'')
    with pytest.raises(UpdateError):
        resume_file({'resume_path': 'cv.pdf'}, tmp_path)
    with pytest.raises(UpdateError):
        resume_file({'resume_path': 'missing.docx'}, tmp_path)


def test_pending_updates_block_across_days_and_legacy_state_works() -> None:
    assert should_skip({'date': '2026-10-01', 'status': 'submitted'}, '2026-10-03')
    assert should_skip({'date': '2026-10-01', 'status': 'needs_review'}, '2026-10-03')
    assert should_skip({'date': '2026-10-03', 'status': 'verified'}, '2026-10-03')
    assert not should_skip({'date': '2026-10-02', 'status': 'verified'}, '2026-10-03')
    assert should_skip('2026-10-03', '2026-10-03')


class MockLocator:
    def __init__(self, page: Any, selector: str) -> None:
        self.page, self.selector = page, selector
    def wait_for(self, **kwargs: Any) -> None:
        return None
    def count(self) -> int:
        return 2 if ',' in self.selector else 1
    def is_visible(self) -> bool:
        return self.page.success if self.selector == '#success' else True
    def input_value(self) -> str:
        return self.page.snapshot['headline']
    def inner_text(self) -> str:
        return self.page.snapshot['stamp' if self.selector == '#updated' else 'filename']
    def get_attribute(self, name: str) -> str:
        return self.page.snapshot['stamp']
    def fill(self, value: str) -> None:
        self.page.snapshot['headline'] = value
    def click(self) -> None:
        self.page.save(headline=self.page.snapshot['headline'])
    def set_input_files(self, path: str) -> None:
        self.page.save(filename=Path(path).name)


class MockPage:
    def __init__(self, state: dict[str, Any]) -> None:
        self.state = state
        self.snapshot = dict(state)
        self.success = False
    def set_default_timeout(self, timeout: int) -> None:
        return None
    def goto(self, url: str, **kwargs: Any) -> None:
        self.snapshot = dict(self.state)
        self.success = False
    def locator(self, selector: str) -> MockLocator:
        return MockLocator(self, selector)
    def save(self, **payload: str) -> None:
        self.state.update(payload)
        self.state['saves'] += 1
        if self.state['normalize']:
            self.state['headline'] = ' '.join(self.state['headline'].split())
        if self.state['change_date']:
            self.state['stamp'] = '2026-10-03T08:00:01Z'
        self.success = True
    def wait_for_timeout(self, timeout: int) -> None:
        return None
    def close(self) -> None:
        return None


class MockContext:
    def __init__(self, state: dict[str, Any]) -> None:
        self.state = state
    def new_page(self) -> MockPage:
        return MockPage(self.state)


@pytest.fixture(params=['mock', 'chromium'])
def mock_site(request: Any) -> Any:
    """Real Chromium against route-intercepted HTTPS; no platform traffic."""
    state: dict[str, Any] = {'headline': 'A', 'filename': 'old.pdf', 'stamp': '2026-10-01T08:00:00Z', 'saves': 0, 'change_date': True, 'normalize': False}
    if request.param == 'mock':
        yield MockContext(state), state
        return
    with sync_playwright() as p:
        executable = Path(p.chromium.executable_path)
        if not executable.exists():
            pytest.skip('Chromium binary unavailable; run playwright install chromium to enable browser tests')
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        def handle(route: Any) -> None:
            if route.request.url.endswith('/save'):
                payload = route.request.post_data_json
                state['saves'] += 1
                if 'headline' in payload:
                    state['headline'] = ' '.join(payload['headline'].split()) if state['normalize'] else payload['headline']
                if 'filename' in payload:
                    state['filename'] = payload['filename']
                if state['change_date']:
                    state['stamp'] = f"2026-10-03T08:00:{state['saves']:02d}Z"
                route.fulfill(json={'ok': True})
            else:
                html = '''<time id="updated"></time><span id="filename"></span>
                <textarea id="headline"></textarea><input id="file" type="file">
                <button id="save">Save</button><p id="success" hidden>Saved</p>
                <script>
                const initial = INITIAL;
                document.querySelector('#headline').value=initial.headline;
                document.querySelector('#filename').textContent=initial.filename;
                document.querySelector('#updated').setAttribute('datetime',initial.stamp);
                document.querySelector('#updated').textContent=initial.stamp;
                async function save(payload) {
                    await fetch('/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
                    document.querySelector('#success').hidden=false;
                }
                document.querySelector('#save').onclick=()=>save({headline:document.querySelector('#headline').value});
                document.querySelector('#file').onchange=()=>save({filename:document.querySelector('#file').files[0].name});
                </script>'''.replace('INITIAL', json.dumps(state))
                route.fulfill(content_type='text/html', body=html)
        context.route('https://profile.test/**', handle)
        try:
            yield context, state
        finally:
            context.close()
            browser.close()


def text_profile() -> dict[str, Any]:
    return {'name':'test','mode':'auto','method':'text_variants','url':'https://profile.test/',
            'variants':['A','B'],'field_selector':'#headline','save_selector':'#save',
            'success_selector':'#success','last_updated_selector':'#updated',
            'last_updated_attribute':'datetime','verification_attempts':1}


def test_text_browser_save_and_timestamp_verification(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    journal = []
    result = update(context, text_profile(), False, tmp_path, lambda: journal.append('submitted'))
    assert result.status == 'verified'
    assert state['headline'] == 'B'
    assert result.timestamp_after != result.timestamp_before
    assert journal == ['submitted']
    assert state['saves'] == 1


def test_resume_browser_upload(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    (tmp_path / 'resume.pdf').write_bytes(b'%PDF local fixture')
    profile = {**text_profile(), 'method':'resume_upload','resume_path':'resume.pdf',
               'file_input_selector':'#file','resume_name_selector':'#filename','save_selector':''}
    result = update(context, profile, False, tmp_path, lambda: None)
    assert result.status == 'verified'
    assert state['filename'] == 'resume.pdf'
    assert state['saves'] == 1
    assert len(result.resume_sha256 or '') == 64


def test_dry_run_does_not_save_or_journal(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    def journal() -> None:
        pytest.fail('Dry run journaled an edit')
    result = update(context, text_profile(), True, tmp_path, journal)
    assert result.status == 'dry_run'
    assert state['saves'] == 0
    assert state['headline'] == 'A'


def test_saved_content_with_unchanged_timestamp_needs_review(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    state['change_date'] = False
    result = update(context, text_profile(), False, tmp_path, lambda: None)
    assert result.status == 'needs_review'
    assert result.content_verified
    assert state['saves'] == 1


def test_whitespace_normalization_not_reported_as_success(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    state.update(headline='Senior Scientist', normalize=True)
    result = update(context, {**text_profile(), 'method':'whitespace'}, False, tmp_path, lambda: None)
    assert result.status == 'needs_review'
    assert not result.content_verified


def test_external_headline_change_prevents_overwrite(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    state['headline'] = 'My new headline'
    with pytest.raises(UpdateError):
        update(context, text_profile(), False, tmp_path, lambda: pytest.fail('Unexpected journal'))
    assert state['saves'] == 0


def test_duplicate_field_selector_fails_before_save(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    with pytest.raises(UpdateError):
        update(context, {**text_profile(), 'field_selector':'textarea, input'}, False, tmp_path, lambda: pytest.fail('Unexpected journal'))
    assert state['saves'] == 0


def test_exception_after_submission_is_durably_blocked(tmp_path: Path, monkeypatch: Any) -> None:
    runtime = tmp_path / 'runtime'
    runtime.mkdir()
    calls = []
    def fail(context: Any, profile: Any, dry_run: bool, base: Path, journal: Any) -> Any:
        calls.append(1)
        journal()
        raise RuntimeError('Unknown save outcome')
    monkeypatch.setattr(runner, 'update', fail)
    from unittest.mock import MagicMock
    import playwright.sync_api
    monkeypatch.setattr(playwright.sync_api, 'sync_playwright', MagicMock())
    config = {'profiles':[text_profile()], 'headless':True, 'timezone':'Asia/Kolkata'}
    assert runner.run_profiles(config, tmp_path, False, None) == 1
    state = json.loads((runtime/'state.json').read_text())
    assert state['test']['status'] == 'needs_review'
    assert runner.run_profiles(config, tmp_path, False, None) == 1
    assert calls == [1]


def test_validation_missing_timestamp_and_duplicate_names(tmp_path: Path) -> None:
    profile = text_profile()
    profile['last_updated_selector'] = ''
    with pytest.raises(UpdateError):
        validate_profile(profile, tmp_path)
    config = tmp_path/'config.yaml'
    import yaml
    config.write_text(yaml.safe_dump({'profiles':[text_profile(),text_profile()]}))
    with pytest.raises(UpdateError):
        runner.load_config(config)


def test_journal_failure_prevents_auto_upload(mock_site: Any, tmp_path: Path) -> None:
    context, state = mock_site
    (tmp_path / 'resume.pdf').write_bytes(b'%PDF fixture')
    profile = {**text_profile(), 'method':'resume_upload','resume_path':'resume.pdf',
               'file_input_selector':'#file','resume_name_selector':'#filename','save_selector':''}
    def failed_journal() -> None:
        raise OSError('Unable to durably record submission')
    with pytest.raises(OSError):
        update(context, profile, False, tmp_path, failed_journal)
    assert state['saves'] == 0


def test_daily_success_skips_browser_launch(tmp_path: Path, monkeypatch: Any) -> None:
    runtime = tmp_path / 'runtime'
    runtime.mkdir()
    today = datetime.now(ZoneInfo('Asia/Kolkata')).date().isoformat()
    runner.save_state(runtime/'state.json', {'test':{'date':today,'status':'verified'}})
    from unittest.mock import MagicMock
    import playwright.sync_api
    launch = MagicMock()
    monkeypatch.setattr(playwright.sync_api, 'sync_playwright', launch)
    assert runner.run_profiles({'profiles':[text_profile()]}, tmp_path, False, None) == 0
    launch.assert_not_called()

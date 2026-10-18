"""Build a local macOS app from original AlphaLink code and the user's Sony SDK."""
from __future__ import annotations
import argparse
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def extract(archive: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        for entry in z.infolist():
            target = (output / entry.filename).resolve()
            if output.resolve() not in target.parents:
                raise ValueError('SDK archive contains an unsafe path')
            # Reject symbolic-link members as well as path traversal.
            if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('SDK archive contains a symbolic link')
        z.extractall(output)


def sdk_root(source: Path, temp: Path) -> Path:
    if source.is_file():
        extract(source, temp / 'sdk')
        source = temp / 'sdk'
    candidates = list(source.rglob('RemoteCli.zip'))
    if candidates:
        extract(candidates[0], temp / 'remote')
        source = temp / 'remote'
    for header in source.rglob('CameraRemote_SDK.h'):
        remote = header.parents[2]
        if (remote / 'external/crsdk/libCr_Core.dylib').is_file():
            return remote
    raise RuntimeError('Choose the macOS Sony Camera Remote SDK ZIP, or a directory containing extracted RemoteCli.')


def build(source: Path, app: bool) -> None:
    if sys.platform != 'darwin':
        raise RuntimeError('Build on the destination Mac. Sony macOS binaries cannot run on Linux/Windows.')
    version = subprocess.check_output(['sw_vers', '-productVersion'], text=True).strip()
    if tuple(map(int, version.split('.')[:2])) < (14, 1):
        raise RuntimeError('macOS 14.1 or later is required for this SDK-based build.')
    subprocess.run(['xcrun', '--find', 'clang++'], check=True, stdout=subprocess.DEVNULL)
    with tempfile.TemporaryDirectory(prefix='alphalink-sdk-') as work:
        remote = sdk_root(source, Path(work))
        runtime = ROOT / 'runtime'
        if runtime.exists():
            shutil.rmtree(runtime)
        runtime.mkdir()
        sdk_lib = remote / 'external/crsdk'
        for library in sdk_lib.glob('*.dylib'):
            shutil.copy2(library, runtime / library.name)
        shutil.copytree(sdk_lib / 'CrAdapter', runtime / 'Contents/Frameworks/CrAdapter')
        subprocess.run([
            'xcrun', 'clang++', '-std=c++17', '-O2', '-pthread', '-mmacosx-version-min=14.1',
            '-I', str(remote / 'app/CRSDK'), str(ROOT / 'native/worker.cpp'),
            '-L', str(runtime), '-lCr_Core', '-Wl,-rpath,@loader_path',
            '-o', str(runtime / 'alphalink-worker'),
        ], check=True)
        # Sony's sample layout puts adapters under executable-dir/Contents/Frameworks.
        # It is retained inside runtime for both source runs and the app bundle.
        for library in runtime.rglob('*.dylib'):
            subprocess.run(['codesign', '--force', '--sign', '-', str(library)], check=True)
        subprocess.run(['codesign', '--force', '--sign', '-', str(runtime / 'alphalink-worker')], check=True)
        if app:
            subprocess.run([
                sys.executable, '-m', 'PyInstaller', '--noconfirm', '--clean', '--windowed',
                '--name', 'AlphaLink', '--osx-bundle-identifier', 'app.alphalink.importer',
                '--add-data', f'{runtime}:runtime', str(ROOT / 'launch.py'),
            ], cwd=ROOT, check=True)
            bundle = ROOT / 'dist/AlphaLink.app'
            info_file = bundle / 'Contents/Info.plist'
            with info_file.open('rb') as stream:
                info = plistlib.load(stream)
            info.update({
                'CFBundleShortVersionString': '0.1.0', 'CFBundleVersion': '1',
                'LSMinimumSystemVersion': '14.1',
                'NSLocalNetworkUsageDescription': 'AlphaLink discovers your camera and imports selected originals over your local Wi-Fi network.',
                'NSHighResolutionCapable': True,
            })
            with info_file.open('wb') as stream:
                plistlib.dump(info, stream)
            subprocess.run(['codesign', '--force', '--deep', '--sign', '-', str(bundle)], check=True)
            subprocess.run(['codesign', '--verify', '--deep', '--strict', str(bundle)], check=True)
            print(f'Built: {bundle}\nOpen it in Finder. This local build is ad-hoc signed, not notarized.')
        else:
            print('Camera engine built. Launch with: python -m alphalink')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--sdk', type=Path)
    parser.add_argument('--choose-sdk', action='store_true')
    parser.add_argument('--engine-only', action='store_true')
    args = parser.parse_args()
    source = args.sdk
    if args.choose_sdk and source is None:
        from PySide6.QtWidgets import QApplication, QFileDialog
        ui = QApplication([])
        path, _ = QFileDialog.getOpenFileName(None, 'Choose Sony Camera Remote SDK for Mac', str(Path.home() / 'Downloads'), 'Sony SDK (*.zip)')
        if not path:
            raise SystemExit('No SDK selected. Download the Mac SDK from Sony, then run Setup.command again.')
        source = Path(path)
    if source is None:
        parser.error('Provide --sdk PATH or --choose-sdk')
    build(source.expanduser().resolve(), not args.engine_only)


if __name__ == '__main__':
    main()

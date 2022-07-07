# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

# specify pygubu modules
hidden_imports = [
    'pygubu.builder.tkstdwidgets',
    'pygubu.builder.ttkstdwidgets',
    'pygubu.builder.widgets.dialog',
    'pygubu.builder.widgets.editabletreeview',
    'pygubu.builder.widgets.scrollbarhelper',
    'pygubu.builder.widgets.scrolledframe',
    'pygubu.builder.widgets.tkscrollbarhelper',
    'pygubu.builder.widgets.tkscrolledframe',
    'pygubu.builder.widgets.pathchooserinput',
]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
    ('bin/linux/woff2_compress', 'bin/linux/woff2_compress'),
    ('bin/darwin/woff2_compress', 'bin/darwin/woff2_compress'),
    ('bin/windows/woff2_compress.exe', '.'),
    ('bin/windows/libgcc_s_seh-1.dll', '.'),
    ('bin/windows/libstdc++-6.dll', '.'),
    ('bin/windows/libwinpthread-1.dll', '.'),
    ],
    datas=[("main_window.ui", "."), ("icon.png", ".")],
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['test'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Walphabet',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon="icon.png",
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

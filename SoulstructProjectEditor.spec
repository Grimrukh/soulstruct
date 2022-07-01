# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Change this path to point to your downloaded Soulstruct repo.
PATH_EX = "G:\\Dark Souls\\soulstruct-git"

added_files = [
    ("VERSION", "."),
    ("soulstruct\\base\\ai\\lua\\x64\\DSLuaDecompiler.exe", "base\\ai\\lua\\x64"),
    ("soulstruct\\base\\ai\\lua\\x64\\Lua.exe", "base\\ai\\lua\\x64"),
    ("soulstruct\\base\\ai\\lua\\x64\\LuaC.exe", "base\\ai\\lua\\x64"),
    ("soulstruct\\base\\ai\\lua\\x64\\SoulsFormats.dll", "base\\ai\\lua\\x64"),
    ("soulstruct\\base\\ai\\lua\\x86\\lua50.dll", "base\\ai\\lua\\x86"),
    ("soulstruct\\base\\ai\\lua\\x86\\lua50.exe", "base\\ai\\lua\\x86"),
    ("soulstruct\\base\\ai\\lua\\x86\\luac50.exe", "base\\ai\\lua\\x86"),
    ("soulstruct\\base\\ezstate\\esd\\functions.pyi", "base\\ezstate\\esd"),
    ("soulstruct\\darksouls1ptde\\params\\resources\\darksouls1ptde.paramdefbnd", "darksouls1ptde\\params\\resources"),
    ("soulstruct\\darksouls1ptde\\events\\emevd\\ds1-common.emedf.json", "darksouls1ptde\\events\\emevd"),
    ("soulstruct\\darksouls1r\\params\\resources\\darksouls1r.paramdefbnd.dcx", "darksouls1r\\params\\resources"),
    ("soulstruct\\bloodborne\\params\\resources\\bloodborne.paramdefbnd.dcx", "bloodborne\\params\\resources"),
]

a = Analysis(
    ["soulstruct\\__main__.py"],
    pathex=[PATH_EX],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        "soulstruct.darksouls1ptde.project",
        "soulstruct.darksouls1r.project",
        "soulstruct.bloodborne.project",
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
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
    name="SoulstructProjectEditor",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    icon="soulstruct\\base\\project\\resources\\soulstruct.ico",
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
)

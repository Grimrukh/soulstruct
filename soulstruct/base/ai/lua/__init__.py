from __future__ import annotations

__all__ = [
    "LuaError",
    "LuaCompileError",
    "LuaDecompileError",
    "compile_lua",
    "decompile_lua",
]

import logging
import os
import subprocess
from contextlib import contextmanager
from pathlib import Path

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.files import PACKAGE_PATH
from soulstruct.utilities.misc import get_startupinfo

_LOGGER = logging.getLogger("soulstruct")

COMPILER_x64 = str(PACKAGE_PATH("base/ai/lua/x64/LuaC.exe"))
COMPILER_x86 = str(PACKAGE_PATH("base/ai/lua/x86/luac50.exe"))
DECOMPILER_x64 = str(PACKAGE_PATH("base/ai/lua/x64/DSLuaDecompiler.exe"))
# No x86 decompiler.


class LuaError(SoulstructError):
    pass


class LuaCompileError(LuaError):
    pass


class LuaDecompileError(LuaError):
    pass


@contextmanager
def _temp_lua_path(content, as_bytes=False, encoding=None, set_cwd=False):
    temp = PACKAGE_PATH("base/ai/lua/temp")
    if set_cwd:
        previous_cwd = os.getcwd()
        os.chdir(str(temp.parent))
    else:
        previous_cwd = None
    with temp.open(mode="wb" if as_bytes else "w", encoding=encoding) as f:
        f.write(content)
    yield temp
    try:
        os.remove(str(PACKAGE_PATH("base/ai/lua/temp")))
    except FileNotFoundError:
        pass
    if previous_cwd:
        os.chdir(previous_cwd)


def compile_lua(script: str, script_name="<unknown script>", output_path=None, x64=True):
    with _temp_lua_path(script, as_bytes=False, set_cwd=True, encoding="shift_jis_2004") as temp:
        compiler_path = COMPILER_x64 if x64 else COMPILER_x86
        result = subprocess.run(
            [compiler_path, "-o", "temp.lua", temp],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=get_startupinfo(),
        )
        if result.stdout.strip():
            _LOGGER.warning(f"Lua Compiler Warning for script {script_name}: {result.stdout.strip()}")
        if result.returncode != 0:
            raise LuaCompileError(f"Script {script_name}: {result.stderr.strip()}")
        with Path("temp.lua").open("rb") as f:
            bytecode = f.read()
        os.remove("temp.lua")
        if output_path:
            with Path(output_path).open("wb") as o:
                o.write(f.read())
        return bytecode


def decompile_lua(bytecode: bytes, script_name="<unknown script>", output_path=None):
    if output_path:
        output_path = Path(output_path).resolve()  # resolve before changing to temp working dir
    with _temp_lua_path(bytecode, as_bytes=True, set_cwd=True) as temp:
        result = subprocess.run(
            [DECOMPILER_x64, temp],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=get_startupinfo(),
        )
        if result.stdout.strip():
            _LOGGER.warning(f"Lua Decompiler Warning for script {script_name}: {result.stdout.strip()}")
        if result.returncode != 0:
            raise LuaDecompileError(f"Script {script_name}: {result.stderr.strip()}")
        with Path("temp.dec.lua").open("r", encoding="shift_jis_2004") as f:
            script_string = f.read()
        os.remove("temp.dec.lua")
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(exist_ok=True, parents=True)
            with Path(output_path).open("w", encoding="shift_jis_2004") as o:
                o.write(script_string)
                _LOGGER.info(f"Decompiled Lua file written: {str(output_path)}")
        return script_string

"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""

__all__ = ["PACKAGE_PATH", "find_dcx", "create_bak", "find_steam_common_paths", ]

import ctypes
import logging
import shutil
import string
import sys
from pathlib import Path

_LOGGER = logging.getLogger(__name__)


def PACKAGE_PATH(*relative_parts) -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"), *relative_parts)
    return Path(__file__).parent.joinpath("..").resolve().joinpath(*relative_parts)


def find_dcx(file_path):
    """Returns DCX (preferred) or non-DCX version of the given file path.

    It doesn't matter if the file path already ends with '.dcx'. If neither file exists, FileNotFoundError is raised.
    """
    file_path = Path(file_path)
    if file_path.suffix == ".dcx":
        no_dcx, dcx = (file_path.parent / file_path.stem, file_path)
    else:
        no_dcx, dcx = (file_path, file_path.with_suffix(file_path.suffix + ".dcx"))
    if Path(dcx).is_file():
        return dcx
    elif Path(no_dcx).is_file():
        return no_dcx
    raise FileNotFoundError(f"Could not find DCX or non-DCX version of {file_path}.")


def create_bak(file_path, bak_suffix=".bak"):
    file_path = Path(file_path)
    if file_path.is_file():
        bak_path = file_path.with_suffix(file_path.suffix + bak_suffix)
        if not bak_path.is_file():
            shutil.copy2(file_path, bak_path)
            _LOGGER.info(f"Created backup file: '{bak_path}'.")
            return True
    return False


def find_steam_common_paths():
    """Not using anymore. Seems to cause 'WinError 87' OSErrors for some people for some drives."""
    steam_common_paths = []
    for drive in _get_drives():
        for arch in {"", " (x86)"}:
            common_path = Path(drive, f"Program Files{arch}/Steam/steamapps/common/")
            if common_path.is_dir():
                steam_common_paths.append(common_path)
    return steam_common_paths


def _get_drives():
    drives = []
    bit_mask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bit_mask & 1:
            drives.append(letter + ":/")
        bit_mask >>= 1
    return drives

__all__ = [
    "PACKAGE_PATH",
    "find_dcx",
    "create_bak",
    "find_steam_common_paths",
    "import_arbitrary_file",
    "read_json",
    "write_json",
]

import ctypes
import importlib.util
import json
import logging
import os
import re
import shutil
import string
import sys
import types
from pathlib import Path

from soulstruct.exceptions import RestoreBackupError

_LOGGER = logging.getLogger(__name__)
LOG_BACKUP_CREATION = True


def PACKAGE_PATH(*relative_parts) -> Path:
    """Returns resolved path of given files in `soulstruct` package directory (the actual namespace directory containing
    `__init__`, NOT the one above it containing `setup.py`)."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"), *relative_parts)
    return Path(__file__).parent.parent.resolve().joinpath(*relative_parts)


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
            if LOG_BACKUP_CREATION:
                _LOGGER.info(f"Created backup file: '{bak_path}'.")
            return True
    return False


def restore_bak(target=None, delete_baks=False):
    """Restores '.bak' files, deleting whatever they would replace."""
    target = Path(target)
    if target.is_file():
        if target.suffix == ".bak":
            if (target.with_suffix("")).is_file():
                os.remove(str(target.with_suffix("")))
            if delete_baks:
                os.rename(str(target), str(target.with_suffix("")))
            else:
                shutil.copy2(str(target), str(target.with_suffix("")))
        elif not (target.with_suffix(".bak")).is_file():
            raise RestoreBackupError(
                f"Could not find a file '{str(target.with_suffix('.bak'))} to restore. No action taken."
            )
        else:
            os.remove(str(target))
            if delete_baks:
                os.rename(str(target.with_suffix(".bak")), str(target))
            else:
                shutil.copy2(str(target.with_suffix(".bak")), str(target))
    elif target.is_dir():
        count = 0
        for bak_file in target.glob("*.bak"):
            restore_bak(bak_file)
            count += 1
        if count == 0:
            raise RestoreBackupError(
                f"Could not find any '.bak' files to restore in directory '{str(target)}'. No action taken."
            )
        else:
            return count


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


def import_arbitrary_file(path: str | Path) -> types.ModuleType:
    """
    TODO: This does not seem to work with `dataclass(slots=True)`. I think I need to assign `__module__` to each
     imported class manually, or something:
        File "C:\\Program Files\\Python311\\Lib\\dataclasses.py", line 712, in _is_type
          ns = sys.modules.get(cls.__module__).__dict__
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        AttributeError: 'NoneType' object has no attribute '__dict__'. Did you mean: '__dir__'?
    """
    path = Path(path)
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    # noinspection PyUnresolvedReferences
    spec.loader.exec_module(module)
    sys.modules[spec.name] = module
    return module


def read_json(json_path: str | Path, encoding=None) -> dict | list:
    """Read JSON file using given `encoding` into list or dictionary."""
    try:
        return json.loads(Path(json_path).read_text(encoding=encoding))
    except UnicodeDecodeError as ex:
        if pos_match := re.findall(r" in position (\d+):", str(ex)):
            raw = json_path.read_bytes()
            pos = int(pos_match[0])
            line = raw[:pos].count(b"\n") + 1
            pos_context = raw[pos - 100:pos + 100]
            raise ValueError(
                f"Encountered Unicode decode error in JSON file {json_path}: {ex}\n"
                f"   Line number: {line}\n"
                f"   Byte context: {pos_context}"
            )
        raise ValueError(f"Encountered Unicode decode error in JSON file {json_path}: {ex}")
    except json.JSONDecodeError as ex:
        raise ValueError(f"Encountered JSON decode error in file {json_path}: {ex}")


def write_json(
    json_path: str | Path, data: list | dict, indent=4, encoding="utf-8", ensure_ascii=True, encoder=None,
):
    """Write given `data` list or dictionary to JSON file with given `encoding`."""
    json_str = json.dumps(data, indent=indent, ensure_ascii=ensure_ascii, cls=encoder)
    json_bytes = json_str.encode(encoding)
    Path(json_path).write_bytes(json_bytes)

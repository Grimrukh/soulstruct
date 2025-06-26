from __future__ import annotations

__all__ = [
    "PACKAGE_PATH",
    "APPDATA_PATH",
    "create_bak",
    "restore_bak",
    "import_arbitrary_module",
    "read_json",
    "write_json",
    "get_blake2b_hash",
    "get_blake2b_hash_hex",
]

import hashlib
import importlib.util
import json
import logging
import os
import re
import shutil
import sys
import types
from pathlib import Path

from soulstruct.exceptions import RestoreBackupError

_LOGGER = logging.getLogger(__name__)
LOG_BACKUP_CREATION = True


def PACKAGE_PATH(*relative_parts) -> Path:
    """Returns resolved path of given files in `soulstruct` package directory. Path parts must start with "soulstruct"
    or it will be automatically added (for PyInstaller compatibility).
    """
    if not relative_parts:
        # Return package directory.
        relative_path = Path("soulstruct")
    else:
        relative_path = Path(*relative_parts)
        if relative_path.parts[0] != "soulstruct":
            relative_path = Path("soulstruct", relative_path)

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"), relative_path)

    # Standard Python package:
    package_path = Path(__file__).parent.parent.parent.resolve()  # go up three levels to package directory
    return package_path / relative_path


def APPDATA_PATH(*relative_parts) -> Path:
    """Returns resolved path of given files in the `soulstruct` appdata directory. Path parts must start with "soulstruct"
    or it will be automatically added (for PyInstaller compatibility).
    """
    if not relative_parts:
        # Return appdata directory.
        relative_path = Path("soulstruct")
    else:
        relative_path = Path(*relative_parts)
        if relative_path.parts[0] != "soulstruct":
            relative_path = Path("soulstruct", relative_path)

    return Path(os.getenv("AppData", Path.home() / ".soulstruct")) / relative_path


def create_bak(file_path: Path | str, bak_suffix=".bak") -> bool:
    """Create a backup file with the given suffix if it does not already exist.

    If `file_path` does not exist, does nothing.

    Returns `True` if a backup file was created, `False` if it was not.
    """
    file_path = Path(file_path)
    if not file_path.is_file():
        return False

    bak_path = file_path.with_suffix(file_path.suffix + bak_suffix)
    if bak_path.is_file():
        return False  # already exists (we NEVER overwrite here)

    shutil.copy2(file_path, bak_path)
    if LOG_BACKUP_CREATION:
        _LOGGER.info(f"Created backup file: '{bak_path}'.")
    return True  # backup created


def restore_bak(target: Path | str, delete_baks=False, bak_suffix=".bak") -> int:
    """Restores '.bak' files, deleting whatever they would replace.

    `target` can be a file or directory path. If it's a file, it can be the BAK file itself, or the file for which a
    BAK file exists. If it's a directory, all '.bak' files in the directory will be restored (NOT recursive).
    """
    target = Path(target)
    if target.is_file():
        if target.suffix == bak_suffix:
            bak_file = target
            non_bak_file = target.with_suffix("")
        else:
            non_bak_file = target
            bak_file = target.with_suffix(bak_suffix)

        if not bak_file.is_file():
            raise RestoreBackupError(
                f"Could not find a file '{str(bak_file)}' to restore. No action taken."
            )

        if non_bak_file.is_file():
            # Delete existing non-BAK file.
            os.remove(non_bak_file)

        # Either rename BAK file (effectively deleting it) or copy it.
        if delete_baks:
            os.rename(str(bak_file), str(non_bak_file))
        else:
            shutil.copy2(str(bak_file), str(non_bak_file))
        return 1  # one file restored

    if target.is_dir():
        count = 0
        for bak_file in target.glob(f"*{bak_suffix}"):
            count += restore_bak(bak_file)  # recur on file
        if count == 0:
            _LOGGER.warning(f"Could not find any '{bak_suffix}' files to restore in directory '{str(target)}'.")
        return count

    raise RestoreBackupError(
        f"Could not restore backup for target '{str(target)}' because it is not a file or directory."
    )


def import_arbitrary_module(path: str | Path) -> types.ModuleType:
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
    with Path(json_path).open("w", encoding=encoding) as f:
        f.write(json_str)


def get_blake2b_hash(data: bytes | str | Path) -> bytes:
    """Get BLAKE2b hash of given `bytes` or `str`/`Path` of file."""
    if isinstance(data, (str, Path)):
        file_hash = hashlib.blake2b()
        with Path(data).open("rb") as f:
            chunk = f.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(8192)
        return file_hash.digest()

    if isinstance(data, bytes):
        return hashlib.blake2b(data).digest()

    raise TypeError(f"Can only get hash of `bytes` or `str`/`Path` of file, not {type(data)}.")


def get_blake2b_hash_hex(data: bytes | str | Path) -> str:
    """Get BLAKE2b hash of given `bytes` or `str`/`Path` of file."""
    if isinstance(data, (str, Path)):
        file_hash = hashlib.blake2b()
        with Path(data).open("rb") as f:
            chunk = f.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(8192)
        return file_hash.hexdigest()

    if isinstance(data, bytes):
        return hashlib.blake2b(data).hexdigest()

    raise TypeError(f"Can only get hash of `bytes` or `str`/`Path` of file, not {type(data)}.")

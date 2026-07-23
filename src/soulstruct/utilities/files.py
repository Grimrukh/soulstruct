from __future__ import annotations

__all__ = [
    "SOULSTRUCT_PATH",
    "SOULSTRUCT_USER_DATA_PATH",
    "create_bak",
    "restore_bak",
    "import_arbitrary_module",
    "read_json",
    "write_json",
    "get_blake2b_hash_hex",
    "get_md5_hash_hex",
    "sync_file",
    "sync_directory",
    "write_data_to_path",
]

import filecmp
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


def SOULSTRUCT_PATH(*relative_parts) -> Path:
    """Returns resolved path of given files in `soulstruct` namespace package directory."""

    parent = Path(__file__).parent
    while parent.name != "soulstruct":
        parent = parent.parent

    if not relative_parts:
        return parent.resolve()  # 'soulstruct' namespace directory

    return Path(parent, *relative_parts).resolve()


def SOULSTRUCT_USER_DATA_PATH(*relative_parts) -> Path:
    """Returns resolved path of given files in the `soulstruct` AppData directory:

    If environment variable `AppData` is set:
        %USERPROFILE%/AppData/Roaming/soulstruct/{*relative_parts}
    Otherwise:
        ~/.soulstruct/{*relative_parts}
    """
    return Path(os.getenv("AppData", Path.home() / ".soulstruct"), *relative_parts).resolve()


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
            bak_file = target.with_suffix(target.suffix + bak_suffix)

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


def _find_package_chain(directory: Path) -> list[Path]:
    """
    Starting at `directory`, walk upward collecting directories that are Python
    packages (i.e. contain `__init__.py`), stopping at the first ancestor that
    isn't. Returns the chain ordered from the top-most package down to
    `directory` itself. Empty if `directory` is not itself a package.
    """
    if not (directory / "__init__.py").is_file():
        return []
    chain = [directory]
    current = directory.parent
    while (current / "__init__.py").is_file():
        chain.insert(0, current)
        parent = current.parent
        if parent == current:
            break  # reached filesystem root
        current = parent
    return chain


def _ensure_package_imported(package_dir: Path, dotted_name: str) -> types.ModuleType:
    """Ensure the package at `package_dir` is registered in `sys.modules` under `dotted_name`."""
    if dotted_name in sys.modules:
        return sys.modules[dotted_name]
    init_path = package_dir / "__init__.py"
    spec = importlib.util.spec_from_file_location(
        dotted_name, str(init_path), submodule_search_locations=[str(package_dir)]
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create package spec for: {package_dir}")
    module = importlib.util.module_from_spec(spec)  # sets __package__ correctly from spec.parent
    sys.modules[dotted_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        del sys.modules[dotted_name]
        raise
    return module


def import_arbitrary_module(path: str | Path) -> types.ModuleType:
    path = Path(path)
    is_package = path.name == "__init__.py"

    # Walk up from the leaf's own directory to find enclosing packages.
    # If `path` is itself an `__init__.py`, `path.parent` will be the last
    # entry in this chain (since it contains `__init__.py` too).
    chain = _find_package_chain(path.parent)

    # Import/register all *ancestor* packages first (excluding the leaf's own
    # package directory if `path` is itself an `__init__.py` — we exec that below).
    ancestor_chain = chain[:-1] if (is_package and chain) else chain
    dotted_parent = ""
    for i, pkg_dir in enumerate(ancestor_chain):
        dotted_parent = pkg_dir.name if i == 0 else f"{dotted_parent}.{pkg_dir.name}"
        _ensure_package_imported(pkg_dir, dotted_parent)

    if is_package:
        module_name = f"{dotted_parent}.{path.parent.name}" if dotted_parent else path.parent.name
        submodule_search_locations = [str(path.parent)]
    else:
        module_name = f"{dotted_parent}.{path.stem}" if dotted_parent else path.stem
        submodule_search_locations = None

    spec = importlib.util.spec_from_file_location(
        module_name, str(path), submodule_search_locations=submodule_search_locations
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create module spec for path: {path}")

    module = importlib.util.module_from_spec(spec)  # __package__ set automatically via spec.parent
    sys.modules[spec.name] = module  # register BEFORE exec, so relative imports inside it resolve
    try:
        spec.loader.exec_module(module)
    except Exception:
        del sys.modules[spec.name]
        raise
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


def get_md5_hash_hex(data: bytes | str | Path) -> str:
    """Get MD5 hash of given `bytes` or `str`/`Path` of file."""
    if isinstance(data, (str, Path)):
        file_hash = hashlib.md5()
        with Path(data).open("rb") as f:
            chunk = f.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(8192)
        return file_hash.hexdigest()

    if isinstance(data, bytes):
        return hashlib.md5(data).hexdigest()

    raise TypeError(f"Can only get MD5 hash of `bytes` or `str`/`Path` of file, not {type(data)}.")


def sync_file(src: Path | str, dst: Path | str, force_write=False, make_dirs=True) -> bool:
    """Copy `src` to `dst` only if needed.

    If `force_write` is True, always writes. This makes dynamic usage easier.
    """
    src, dst = Path(src), Path(dst)
    if dst.is_file() and not force_write and not _needs_copy(src, dst):
        return False

    if make_dirs and dst.parent:
        dst.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(src, dst)
    return True


def sync_directory(src_dir: Path | str, dst_dir: Path | str, delete_extraneous=False) -> tuple[int, int, int]:
    """Copy `src_dir` to `dst_dir`, only writing files that are new or changed.

    Optionally also delete any files/directories in `dst_dir` that do not exist in `src_dir`.

    Returns (copied, skipped, deleted) file counts.
    """
    src_dir = Path(src_dir)
    dst_dir = Path(dst_dir)
    copied = skipped = deleted = 0

    for src_root, dir_names, file_names in os.walk(src_dir):
        src_root = Path(src_root)
        rel_root = src_root.relative_to(src_dir)
        dst_root = dst_dir / rel_root
        dst_root.mkdir(parents=True, exist_ok=True)

        # Use os.scandir-based dircmp-like size lookups without re-stating.
        for file_name in file_names:
            src_file = src_root / file_name
            dst_file = dst_root / file_name

            if _needs_copy(src_file, dst_file):
                shutil.copy2(src_file, dst_file)
                copied += 1
            else:
                skipped += 1

        if delete_extraneous:
            existing = set(file_names) | set(dir_names)
            if dst_root.exists():
                for entry in os.scandir(dst_root):
                    if entry.name not in existing:
                        if entry.is_dir():
                            shutil.rmtree(entry.path)
                        else:
                            os.remove(entry.path)
                        deleted += 1

    return copied, skipped, deleted


def write_data_to_path(
    data: bytes, dst: Path | str, force=False, make_backup=True, make_dirs=True
) -> bool:
    """Write `data` to `dst`, only touching the file if contents differ.

    If `force` is True, always writes the file regardless of contents. This makes dynamic write calls easier.

    Also makes a backup by default (if write occurs) and makes parent directories.

    Treats `data` as bytes. String data should be encoded first (and handle your own line endings).

    Returns True if written, False if skipped (unchanged).
    """
    dst = Path(dst)

    if force:
        if make_backup:
            create_bak(dst)
        dst.write_bytes(data)
        return True

    if dst.exists():
        d_stat = dst.stat()

        # cheap reject: size mismatch means content differs, no need to read
        if d_stat.st_size == len(data):
            if _bytes_equal_to_file(data, dst):
                return False  # unchanged, skip write
    elif make_dirs:
        dst.parent.mkdir(exist_ok=True, parents=True)

    if make_backup:
        create_bak(dst)
    dst.write_bytes(data)
    return True


def _bytes_equal_to_file(data: bytes, path: Path | str, chunk_size: int = 1024 * 1024) -> bool:
    """Compare bytes to a file's contents without loading the whole file if it differs early."""
    with open(path, "rb") as f:
        offset = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            if data[offset:offset + len(chunk)] != chunk:
                return False
            offset += len(chunk)
    return offset == len(data)


def _needs_copy(src_file: Path, dst_file: Path) -> bool:
    """Check if file contents are different as efficiently as possible."""
    if not dst_file.exists():
        return True

    s_stat = src_file.stat()
    d_stat = dst_file.stat()

    # cheap rejects before touching file contents
    if s_stat.st_size != d_stat.st_size:
        return True

    # same size — do a real byte comparison (short-circuits on first diff)
    return not filecmp.cmp(src_file, dst_file, shallow=False)

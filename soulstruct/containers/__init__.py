"""NOTE: This file is Python 3.9 compatible for Blender 3.X use."""
from __future__ import annotations

__all__ = ["Binder"]

import typing as tp
from pathlib import Path

from .bnd import BND3, BND4
from .bxf import BXF3, BXF4
from .dcx import decompress
from .tpf import TPF


def Binder(
    binder_source=None, dcx_type=None, from_bak=False, create_bak_if_missing=True
) -> tp.Union[BND3, BND4, BXF3, BXF4]:
    """Auto-detects binder format (BND/BXF) and version (3/4) to use when opening the source.

    Args:
        binder_source: path to BND/BXF file or file content. The format and version will be automatically detected.
        dcx_type: optional DCX type.
        from_bak: prefer '.bak' path if it exists.
        create_bak_if_missing: if `from_bak` is given, and `.bak` file does not exist, create it.
    """
    detect_source = binder_source
    if isinstance(binder_source, (str, Path)):
        if not Path(binder_source).is_dir():
            binder_path = Path(binder_source).resolve()
            if not binder_path.is_file():
                raise FileNotFoundError(f"Could not find binder file: {binder_path}")
            if binder_path.suffix == ".dcx":
                # Must unpack DCX archive before detecting BND type.
                if dcx_type:
                    raise ValueError("Cannot specify `dcx_type` manually when passing a DCX source.")
                detect_source, _ = decompress(binder_path)
            else:
                detect_source = binder_path
    for cls in (BND3, BND4, BXF3, BXF4):
        if cls.detect(detect_source):
            if from_bak:
                return cls.from_bak(binder_source, dcx_type=dcx_type, create_bak_if_missing=create_bak_if_missing)
            return cls(binder_source, dcx_type=dcx_type)
    raise TypeError("Data bytes could not be interpreted as `BND3`, `BND4`, `BXF3`, or `BXF4`.")

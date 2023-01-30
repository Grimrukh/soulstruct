from __future__ import annotations

__all__ = [
    "BaseBinder",
    "Binder",
    "BND",
    "BaseBXF",
    "BXF3",
    "BXF4",
    "DCXType",
    "decompress",
    "compress",
    "TPF",
    "TPFTexture",
]

from pathlib import Path

from .base import BaseBinder
from .bnd import BND
from .bxf import BaseBXF, BXF3, BXF4
from .dcx import DCXType, decompress, compress
from .tpf import TPF, TPFTexture


def Binder(
    binder_source=None, dcx_type=None, from_bak=False, create_bak_if_missing=True, bdt_source=None
) -> BND | BXF3 | BXF4:
    """Auto-detects binder format (BND/BXF) and version (3/4) to use when opening the source.

    Args:
        binder_source: path to BND/BXF file or file content. The format and version will be automatically detected.
        dcx_type: optional DCX type.
        from_bak: prefer '.bak' path if it exists.
        create_bak_if_missing: if `from_bak` is given, and `.bak` file does not exist, create it.
        bdt_source: optional BDT source or path, if not next to given `binder_source` BHD.
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
    for cls in (BND, BXF3, BXF4):
        if cls.detect(detect_source):
            if from_bak:
                return cls.from_bak(binder_source, dcx_type=dcx_type, create_bak_if_missing=create_bak_if_missing)
            if cls in (BXF3, BXF4):
                return cls(binder_source, dcx_type=dcx_type, bdt_source=bdt_source)
            elif bdt_source is not None:
                raise ValueError(f"`bdt_source` was given, but `binder_source` is not of BXF type.")
            return cls(binder_source, dcx_type=dcx_type)
    raise TypeError("Data bytes could not be interpreted as `BND3`, `BND4`, `BXF3`, or `BXF4`.")

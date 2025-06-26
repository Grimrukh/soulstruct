"""Describes the structure of a PARTSBND Binder."""
from __future__ import annotations

__all__ = ["PARTSBND"]

from dataclasses import dataclass

from soulstruct.containers import BinderVersion
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_DSR


class PARTSBND(FLVERBinder):
    """NOTE: When present, the '_M' suffix is capitalized, and does not appear in the path folder name or TPF name."""

    DEFAULT_ENTRY_ROOT = f"{DARK_SOULS_DSR.interroot_prefix}\\parts"

    dcx_type: DCXType = DARK_SOULS_DSR.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    def get_flver_entry_path(self, model_stem: str) -> str:
        """Model file's immediate parent directory does not include '_M' suffix."""
        model_stem = model_stem.upper()
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem.removesuffix('_M')}\\{model_stem}.flver"

    def get_tpf_entry_path(self, model_stem: str) -> str:
        """TPF file stem does not include '_M' suffix."""
        model_stem = model_stem.upper().removesuffix("_M")
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem}\\{model_stem}.tpf"

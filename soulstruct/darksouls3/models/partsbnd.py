"""Describes the structure of a PARTSBND Binder."""
from __future__ import annotations

__all__ = ["PARTSBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_3


class PARTSBND(FLVERBinder):):
    """NOTE: When present, the '_L' suffix is capitalized, and does not appear in the path folder name.

    The '_L' suffix also goes after the '_c' cloth suffix in cloth file names.
    """

    # TODO: Have not 100% confirmed that all roots end with 'FullBody'.
    DEFAULT_ENTRY_ROOT = f"{DARK_SOULS_3.interroot_prefix}\\parts\\FullBody"
    TPF_ENTRY_ID: tp.ClassVar[int] = -1  # no TPF

    CLOTH_CLM2_ENTRY_ID: tp.ClassVar[int] = 700
    CLOTH_HKX_ENTRY_ID: tp.ClassVar[int] = 900

    dcx_type: DCXType = DARK_SOULS_3.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.darksouls3_default)

    def get_flver_entry_path(self, model_stem: str) -> str:
        model_stem = model_stem.upper()  # always upper case
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem.removesuffix('_L')}\\{model_stem}.flver"

    def get_cloth_clm2_entry_path(self, model_stem: str) -> str:
        model_stem = model_stem.upper()  # always upper case
        if model_stem.endswith("_L"):
            file_stem = model_stem.removesuffix('_L') + "_c_L"
        else:
            file_stem = model_stem + "_c"
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem.removesuffix('_L')}\\{file_stem}.clm2"

    def get_cloth_hkx_entry_path(self, model_stem: str) -> str:
        model_stem = model_stem.upper()  # always upper case
        if model_stem.endswith("_L"):
            file_stem = model_stem.removesuffix('_L') + "_c_L"
        else:
            file_stem = model_stem + "_c"
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem.removesuffix('_L')}\\{file_stem}.hkx"

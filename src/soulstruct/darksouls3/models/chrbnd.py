"""Describes the structure of a CHRBND Binder."""
from __future__ import annotations

__all__ = ["CHRBND"]

import typing as tp
from dataclasses import field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_3


class CHRBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT = f"{DARK_SOULS_3.interroot_prefix}\\chr"

    RAGDOLL_HKX_ENTRY_ID: tp.ClassVar[int] = 300
    HKXPWV_ENTRY_ID: tp.ClassVar[int] = 500
    CLOTH_HKX_ENTRY_ID: tp.ClassVar[int] = 700
    CLOTH_CLM2_ENTRY_ID: tp.ClassVar[int] = 1200

    dcx_type: DCXType = DARK_SOULS_3.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.darksouls3_default)

    def get_ragdoll_hkx_entry_path(self, model_stem: str) -> str:
        return self.get_default_entry_path(f"{model_stem}\\{model_stem}.HKX")  # suffix is typically uppercase

    def get_hkxpwv_entry_path(self, model_stem: str) -> str:
        return self.get_default_entry_path(f"{model_stem}\\{model_stem}.hkxpwv")

    def get_cloth_hkx_entry_path(self, model_stem: str) -> str:
        return self.get_default_entry_path(f"{model_stem}\\{model_stem}_c.hkx")

    def get_cloth_clm2_entry_path(self, model_stem: str) -> str:
        return self.get_default_entry_path(f"{model_stem}\\{model_stem}_c.clm2")

"""Describes the structure of a OBJBND Binder."""
from __future__ import annotations

__all__ = ["OBJBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_3


@dataclass(slots=True)
class OBJBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT = f"{DARK_SOULS_3.interroot_prefix}\\obj"
    MAX_FLVER_COUNT = 99

    FIRST_COLLISION_HKX_ENTRY_ID: tp.ClassVar[int] = 300  # can be one per FLVER

    dcx_type: DCXType = DARK_SOULS_3.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.darksouls3_default)

    def get_flver_entry_path(self, model_stem: str) -> str:
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem[:3]}\\{model_stem}\\{model_stem}.flver"

    def get_collision_hkx_entry_path(self, model_stem: str) -> str:
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem[:3]}\\{model_stem}\\{model_stem}.hkx"

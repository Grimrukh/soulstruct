"""Describes the structure of a MAPBND Binder."""
from __future__ import annotations

__all__ = ["MAPBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import SEKIRO


class MAPBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{SEKIRO.interroot_prefix}\\map"
    TPF_ENTRY_ID: tp.ClassVar[int] = -1  # no TPF
    FLVER_S_ENTRY_ID: tp.ClassVar[int] = 1100  # second '_S' FLVER entry ID

    dcx_type: DCXType = SEKIRO.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.sekiro_default)

    def get_tpf_entry_path(self, model_stem: str) -> str:
        raise TypeError("MAPBND does not contain TPF files. They are found in 'map/{map_area}' TPFBXFs.")

    def get_flver_entry_path(self, model_stem: str) -> str:
        map_stem = model_stem[:12]
        return f"{self.DEFAULT_ENTRY_ROOT}\\{map_stem}\\{model_stem}\\{model_stem}.flver"

    def get_flver_S_entry_path(self, model_stem: str) -> str:
        map_stem = model_stem[:12]
        return f"{self.DEFAULT_ENTRY_ROOT}\\{map_stem}\\{model_stem}\\{model_stem}_S.flver"

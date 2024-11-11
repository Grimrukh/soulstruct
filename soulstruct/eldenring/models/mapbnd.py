"""Describes the structure of a MAPBND Binder."""
from __future__ import annotations

__all__ = ["MAPBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import ELDEN_RING


@dataclass(slots=True)
class MAPBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{ELDEN_RING.interroot_prefix}\\map"
    TPF_ENTRY_ID: tp.ClassVar[int] = -1  # no TPF
    GRASS_ENTRY_ID: tp.ClassVar[int] = 1200

    dcx_type: DCXType = ELDEN_RING.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.elden_ring_default)

    def get_tpf_entry_path(self, model_stem: str) -> str:
        raise TypeError("MAPBND does not contain TPF files. They are found in 'asset/aet' TPFs (next to Asset 'aeg').")

    def get_flver_entry_path(self, model_stem: str) -> str:
        map_stem = model_stem[:12]
        return f"{self.DEFAULT_ENTRY_ROOT}\\{map_stem}\\{model_stem}\\Model\\{model_stem}.flver"

    def get_grass_entry_path(self, model_stem: str) -> str:
        map_stem = model_stem[:12]
        return f"{self.DEFAULT_ENTRY_ROOT}\\{map_stem}\\{model_stem}\\Model\\{model_stem}.grass"

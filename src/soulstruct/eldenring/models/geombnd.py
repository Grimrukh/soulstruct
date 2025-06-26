"""Describes the structure of a GEOMBND Binder."""
from __future__ import annotations

__all__ = ["GEOMBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import ELDEN_RING


class GEOMBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{ELDEN_RING.interroot_prefix}\\asset\\aeg"
    TPF_ENTRY_ID: tp.ClassVar[int] = -1

    dcx_type: DCXType = ELDEN_RING.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.eldenring_default)

    def get_tpf_entry_path(self, model_stem: str) -> str:
        raise TypeError("GEOMBND does not contain TPF files. These are in `asset/aet` TPFs.")

    def get_flver_entry_path(self, model_stem: str) -> str:
        """Note more complicated path for AEG."""
        return f"{self.DEFAULT_ENTRY_ROOT}\\{model_stem[:6]}\\{model_stem}\\sib\\{model_stem}.flver"

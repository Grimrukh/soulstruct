"""Describes the structure of a OBJBND Binder."""
from __future__ import annotations

__all__ = ["OBJBND"]

from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import BLOODBORNE


@dataclass(slots=True)
class OBJBND(FLVERBinder):

    INTERROOT_STEM = f"{BLOODBORNE.interroot_prefix}\\obj"
    MAX_FLVER_COUNT = 99

    dcx_type: DCXType = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info)  # uses defaults

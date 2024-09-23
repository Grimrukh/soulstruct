"""Describes the structure of a CHRBND Binder."""
from __future__ import annotations

__all__ = ["CHRBND"]

from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import BLOODBORNE
from .flver import FLVER


@dataclass(slots=True)
class CHRBND(FLVERBinder[FLVER]):

    FLVER_CLASS = FLVER
    DEFAULT_ENTRY_ROOT = f"{BLOODBORNE.interroot_prefix}\\chr"

    dcx_type: DCXType = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info)  # uses defaults

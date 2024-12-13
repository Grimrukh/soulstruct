"""Describes the structure of a CHRBND Binder."""
from __future__ import annotations

__all__ = ["CHRBND"]

from dataclasses import dataclass, field

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import ELDEN_RING


class CHRBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT = f"{ELDEN_RING.interroot_prefix}\\chr"

    dcx_type: DCXType = ELDEN_RING.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.eldenring_default)

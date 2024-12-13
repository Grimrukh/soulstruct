"""Describes the structure of a OBJBND Binder."""
from __future__ import annotations

__all__ = ["OBJBND"]

from dataclasses import dataclass

from soulstruct.containers import BinderVersion
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DEMONS_SOULS


class OBJBND(FLVERBinder):):

    DEFAULT_ENTRY_ROOT = f"{DEMONS_SOULS.interroot_prefix}\\obj"
    MAX_FLVER_COUNT = 99

    dcx_type: DCXType = DEMONS_SOULS.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

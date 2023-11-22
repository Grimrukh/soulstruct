"""Describes the structure of a OBJBND Binder."""
from __future__ import annotations

__all__ = ["OBJBND"]

from dataclasses import dataclass

from soulstruct.containers import BinderVersion
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_DSR


@dataclass(slots=True)
class OBJBND(FLVERBinder):

    INTERROOT_STEM = f"{DARK_SOULS_DSR.interroot_prefix}\\obj"

    dcx_type: DCXType = DARK_SOULS_DSR.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

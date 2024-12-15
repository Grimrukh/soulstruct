"""Describes the structure of a PARTSBND Binder."""
from __future__ import annotations

__all__ = ["PARTSBND"]

from dataclasses import dataclass

from soulstruct.containers import BinderVersion
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_PTDE


class PARTSBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT = f"{DARK_SOULS_PTDE.interroot_prefix}\\parts"

    dcx_type: DCXType = DARK_SOULS_PTDE.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

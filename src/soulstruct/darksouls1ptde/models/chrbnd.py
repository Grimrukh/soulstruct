"""Describes the structure of a CHRBND Binder."""
from __future__ import annotations

__all__ = ["CHRBND"]

from dataclasses import dataclass

from soulstruct.containers import BinderVersion
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_PTDE


class CHRBND(FLVERBinder):

    DEFAULT_ENTRY_ROOT = f"{DARK_SOULS_PTDE.interroot_prefix}\\chr"

    version: BinderVersion = BinderVersion.V3

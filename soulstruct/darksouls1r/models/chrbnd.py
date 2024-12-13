"""Describes the structure of a CHRBND Binder."""
from __future__ import annotations

__all__ = ["CHRBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.containers import BinderVersion
from soulstruct.containers.binder_types import FLVERBinder
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_DSR


class CHRBND(FLVERBinder):):

    DEFAULT_ENTRY_ROOT = f"{DARK_SOULS_DSR.interroot_prefix}\\chr"

    # NOTE: ID is defined here, but because the BDT is written outside the CHRBND, reading/writing is not managed here.
    CHRTPFBHD_ENTRY_ID: tp.ClassVar[int] = 800

    dcx_type: DCXType = DARK_SOULS_DSR.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    def get_chrtpfbhd_entry_path(self, model_stem: str) -> str:
        return self.get_default_entry_path(f"{model_stem}\\{model_stem}.chrtpfbhd")

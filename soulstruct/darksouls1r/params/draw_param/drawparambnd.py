from __future__ import annotations

__all__ = ["DrawParamBND"]

import typing as tp
from dataclasses import dataclass
from types import ModuleType

from soulstruct.games import DARK_SOULS_DSR

from soulstruct.darksouls1ptde.params.draw_param import DrawParamBND
from .. import paramdef
from ..paramdef import *


@dataclass(slots=True)
class DrawParamBND(DrawParamBND):
    """Structure that manages double-slots and DrawParam nicknames for one `DrawParamBND` file (i.e. one map "area")."""

    PARAMDEF_MODULE: tp.ClassVar[ModuleType] = paramdef
    GET_BUNDLED_PARAMDEFBND: tp.ClassVar[tp.Callable] = staticmethod(GET_BUNDLED_PARAMDEFBND)

    dcx_type = DARK_SOULS_DSR.default_dcx_type

    @classmethod
    def get_default_entry_path(cls, entry_name: str) -> str:
        return f"N:\\FRPG\\data\\INTERROOT_x64\\param\\DrawParam\\{entry_name}"

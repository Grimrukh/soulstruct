from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.text.msgbnd import MSGBND as _BaseMSGBND
from soulstruct.containers import BinderVersion
from soulstruct.games import DARK_SOULS_PTDE

try:
    Self = tp.Self
except AttributeError:
    Self = "MSGBND"


@dataclass(slots=True)
class MSGBND(_BaseMSGBND):
    """Subclassed by games to set default binder/entry path.

    Does NOT handle FMGs; `MSGDirectory` does that by managing both `item` and `menu` MSGBNDs together.
    """

    dcx_type = DARK_SOULS_PTDE.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    @classmethod
    def get_default_new_entry_path(cls, entry_name: str):
        return f"N:/FRPG/data/Msg/Data_ENGLISH/win32/{entry_name}"

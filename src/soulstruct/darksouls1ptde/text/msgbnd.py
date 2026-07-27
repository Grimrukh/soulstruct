from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.containers import Binder, BinderVersion
from soulstruct.games import DARK_SOULS_PTDE


class MSGBND(Binder):
    """Subclassed by games to set default binder/entry path.

    Does NOT handle FMGs; `MSGDirectory` does that by managing both `item` and `menu` MSGBNDs together.
    """

    IS_SPLIT_BXF: tp.ClassVar[bool] = False
    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = "N:\\FRPG\\data\\Msg\\Data_ENGLISH\\win32"  # NOT interroot

    version: BinderVersion = BinderVersion.V3

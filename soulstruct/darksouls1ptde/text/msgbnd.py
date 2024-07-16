from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.containers import Binder, BinderVersion
from soulstruct.games import DARK_SOULS_PTDE

try:
    Self = tp.Self
except AttributeError:
    Self = "MSGBND"


@dataclass(slots=True)
class MSGBND(Binder):
    """Subclassed by games to set default binder/entry path.

    Does NOT handle FMGs; `MSGDirectory` does that by managing both `item` and `menu` MSGBNDs together.
    """

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{DARK_SOULS_PTDE.interroot_prefix}\\Msb\\Data_ENGLISH\\win32"

    dcx_type = DARK_SOULS_PTDE.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

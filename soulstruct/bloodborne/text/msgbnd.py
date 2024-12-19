from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import field

from soulstruct.containers import Binder, BinderVersion, BinderVersion4Info
from soulstruct.games import BLOODBORNE

class MSGBND(Binder):
    """Subclassed by games to set default binder/entry path."""

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{BLOODBORNE.interroot_prefix}\\msg\\engUS\\64bit"

    dcx_type = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(False, False, True, 0))

from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.text.msgbnd import MSGBND as _BaseMSGBND
from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.games import BLOODBORNE
try:
    Self = tp.Self
except AttributeError:
    Self = "MSGBND"


@dataclass(slots=True)
class MSGBND(_BaseMSGBND):
    """Subclassed by games to set default binder/entry path."""

    dcx_type = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(False, False, True, 0))

    @classmethod
    def get_default_new_entry_path(cls, entry_name: str):
        return f"N:/SPRJ/data/INTERROOT_ps4/msg/engUS/64bit/{entry_name}"

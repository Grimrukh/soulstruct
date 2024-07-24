from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.containers import Binder, BinderVersion, BinderVersion4Info
from soulstruct.games import ELDEN_RING


@dataclass(slots=True)
class MSGBND(Binder):
    """Subclassed by games to set default binder/entry path."""

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{ELDEN_RING.interroot_prefix}\\msg\\engUS"

    dcx_type = ELDEN_RING.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info.elden_ring_default)

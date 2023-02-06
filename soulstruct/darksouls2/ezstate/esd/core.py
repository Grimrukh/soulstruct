from __future__ import annotations

__all__ = ["TalkESD", "ChrESD"]

import abc

from soulstruct.base.ezstate.esd import ESD as _BaseESD, ESDType


class ESD(_BaseESD, abc.ABC):
    VERSION = 2
    VARINT_SIZE = 8


class TalkESD(ESD):
    ESD_TYPE = ESDType.TALK


class ChrESD(ESD):
    ESD_TYPE = ESDType.CHR

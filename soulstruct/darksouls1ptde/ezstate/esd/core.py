from __future__ import annotations

__all__ = ["TalkESD", "ChrESD"]

import abc
import typing as tp
from dataclasses import dataclass

from soulstruct.base.ezstate.esd import ESD as _BaseESD, ESDType
from soulstruct.dcx import DCXType


class ESD(_BaseESD, abc.ABC):
    VERSION: tp.ClassVar[int] = 1
    LONG_VARINTS: tp.ClassVar[bool] = False


class TalkESD(ESD):
    ESD_TYPE: tp.ClassVar[ESDType] = ESDType.TALK
    dcx_type: DCXType = DCXType.Null


class ChrESD(ESD):
    ESD_TYPE: tp.ClassVar[ESDType] = ESDType.CHR

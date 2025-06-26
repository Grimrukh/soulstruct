import abc

from soulstruct.base.ezstate.esd import ESD as _BaseESD, ESDType

__all__ = ["TalkESD", "ChrESD"]


class ESD(_BaseESD, abc.ABC):
    VERSION = 3
    LONG_VARINTS = True


class TalkESD(ESD):
    ESD_TYPE = ESDType.TALK


class ChrESD(ESD):
    ESD_TYPE = ESDType.CHR

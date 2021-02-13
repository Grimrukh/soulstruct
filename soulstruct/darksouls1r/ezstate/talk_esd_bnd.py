__all__ = ["TalkESDBND"]

from soulstruct.containers.bnd import BND3
from soulstruct.base.ezstate.talk_esd_bnd import TalkESDBND as _BaseTalkESDBND

from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND, BND3):
    TALK_ESD_CLASS = TalkESD
    BND_ROOT = "N:\\FRPG\\data\\INTERROOT_win32\\script\\talk"

    def set_default_bnd(self):
        self.version = "BND3"
        self.signature = "07D7R7"
        self.magic = 116
        self.big_endian = False
        self.unknown = False
        self.dcx_magic = (36, 44)

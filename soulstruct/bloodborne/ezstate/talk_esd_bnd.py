from soulstruct.containers.bnd import BND4
from soulstruct.base.ezstate.talk_esd_bnd import TalkESDBND as _BaseTalkESDBND

from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND, BND4):
    TALK_ESD_CLASS = TalkESD
    BND_ROOT = "N:\\SPRJ\\data\\INTERROOT_ps4\\script\\talk"

    def set_default_bnd(self):
        self.version = "BND4"
        self.signature = "07D7R7"
        self.magic = 116
        self.big_endian = False
        self.utf16_paths = True
        self.hash_table_type = 0
        self.flags = (False, False)
        self.dcx_magic = (68, 76)

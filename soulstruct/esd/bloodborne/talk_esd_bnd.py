from soulstruct.bnd import BND4
from soulstruct.esd.base.talk_esd_bnd import TalkESDBND as _BaseTalkESDBND, TalkDirectory as _BaseTalkDirectory
from soulstruct.maps.bloodborne.maps import ALL_MAPS_NO_CHALICE, get_map

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


class TalkDirectory(_BaseTalkDirectory):
    """Does not include Chalice Dungeons."""
    ALL_MAPS = ALL_MAPS_NO_CHALICE
    GET_MAP = staticmethod(get_map)
    IS_DCX = True
    TALKESDBND_CLASS = TalkESDBND

    HuntersDream: TalkESDBND
    AbandonedOldWorkshop: TalkESDBND
    HemwickCharnelLane: TalkESDBND
    OldYharnam: TalkESDBND
    CathedralWard: TalkESDBND
    CentralYharnam: TalkESDBND
    UpperCathedralWard: TalkESDBND  # and Altar of Despair
    CastleCainhurst: TalkESDBND
    NightmareOfMensis: TalkESDBND
    ForbiddenWoods: TalkESDBND
    Yahargul: TalkESDBND
    # ChaliceDungeon: TalkESDBND
    Byrgenwerth: TalkESDBND  # and Lecture Building
    NightmareFrontier: TalkESDBND
    HuntersNightmare: TalkESDBND
    ResearchHall: TalkESDBND
    FishingHamlet: TalkESDBND

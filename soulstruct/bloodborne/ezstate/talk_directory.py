from soulstruct.base.ezstate.talk_directory import TalkDirectory as _BaseTalkDirectory
from soulstruct.bloodborne.ezstate.talk_esd_bnd import TalkESDBND
from soulstruct.bloodborne.maps.constants import ALL_MAPS_NO_CHALICE, get_map


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

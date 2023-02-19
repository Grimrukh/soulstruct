from __future__ import annotations

__all__ = ["TalkDirectory"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.ezstate.talk_directory import TalkDirectory as _BaseTalkDirectory
from soulstruct.base.game_file_directory import map_property
from soulstruct.bloodborne.ezstate.talkesdbnd import TalkESDBND
from soulstruct.bloodborne.maps.constants import *


@dataclass(slots=True)
class TalkDirectory(_BaseTalkDirectory):
    """Does not include Chalice Dungeons."""
    ALL_MAPS: tp.ClassVar = ALL_MAPS_NO_CHALICE
    GET_MAP: tp.ClassVar = staticmethod(get_map)
    FILE_CLASS: tp.ClassVar = TalkESDBND

    Common = map_property(COMMON)  # type: TalkESDBND
    HuntersDream = map_property(HUNTERS_DREAM)  # type: TalkESDBND
    AbandonedOldWorkshop = map_property(ABANDONED_OLD_WORKSHOP)  # type: TalkESDBND
    HemwickCharnelLane = map_property(HEMWICK_CHARNEL_LANE)  # type: TalkESDBND
    OldYharnam = map_property(OLD_YHARNAM)  # type: TalkESDBND
    CathedralWard = map_property(CATHEDRAL_WARD)  # type: TalkESDBND
    CentralYharnam = map_property(CENTRAL_YHARNAM)  # type: TalkESDBND
    UpperCathedralWard = map_property(UPPER_CATHEDRAL_WARD)  # type: TalkESDBND  # and Altar of Despair
    CastleCainhurst = map_property(CASTLE_CAINHURST)  # type: TalkESDBND
    NightmareOfMensis = map_property(NIGHTMARE_OF_MENSIS)  # type: TalkESDBND
    ForbiddenWoods = map_property(FORBIDDEN_WOODS)  # type: TalkESDBND
    Yahargul = map_property(YAHARGUL)  # type: TalkESDBND
    # ChaliceDungeon: map_property(CHALICE_DUNGEON)  # type: TalkESDBND
    Byrgenwerth = map_property(BYRGENWERTH)  # type: TalkESDBND  # and Lecture Building
    NightmareFrontier = map_property(NIGHTMARE_FRONTIER)  # type: TalkESDBND
    HuntersNightmare = map_property(HUNTERS_NIGHTMARE)  # type: TalkESDBND
    ResearchHall = map_property(RESEARCH_HALL)  # type: TalkESDBND
    FishingHamlet = map_property(FISHING_HAMLET)  # type: TalkESDBND

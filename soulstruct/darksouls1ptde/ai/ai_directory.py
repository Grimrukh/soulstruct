from __future__ import annotations

__all__ = ["ScriptDirectory"]

import logging
import typing as tp

from soulstruct.base.ai.ai_directory import ScriptDirectory as _BaseScriptDirectory
from soulstruct.base.game_file_directory import map_property
from soulstruct.darksouls1ptde.maps.constants import *

if tp.TYPE_CHECKING:
    from soulstruct.base.ai.luabnd import LuaBND

_LOGGER = logging.getLogger(__name__)


class ScriptDirectory(_BaseScriptDirectory):
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)

    Common = map_property(COMMON)  # type: LuaBND
    Depths = map_property(DEPTHS)  # type: LuaBND
    UndeadBurg = map_property(UNDEAD_BURG)  # type: LuaBND  # and Undead Parish
    FirelinkShrine = map_property(FIRELINK_SHRINE)  # type: LuaBND
    PaintedWorld = map_property(PAINTED_WORLD)  # type: LuaBND
    DarkrootGarden = map_property(DARKROOT_GARDEN)  # type: LuaBND  # and Darkroot Basin
    Oolacile = map_property(OOLACILE)  # type: LuaBND  # and all DLC
    Catacombs = map_property(CATACOMBS)  # type: LuaBND
    TombOfTheGiants = map_property(TOMB_OF_THE_GIANTS)  # type: LuaBND
    AshLake = map_property(ASH_LAKE)  # type: LuaBND  # and Great Hollow
    Blighttown = map_property(BLIGHTTOWN)  # type: LuaBND
    LostIzalith = map_property(LOST_IZALITH)  # type: LuaBND  # and Demon Ruins
    SensFortress = map_property(SENS_FORTRESS)  # type: LuaBND
    AnorLondo = map_property(ANOR_LONDO)  # type: LuaBND
    NewLondoRuins = map_property(NEW_LONDO_RUINS)  # type: LuaBND  # and Valley of Drakes
    DukesArchives = map_property(DUKES_ARCHIVES)  # type: LuaBND
    KilnOfTheFirstFlame = map_property(KILN_OF_THE_FIRST_FLAME)  # type: LuaBND
    UndeadAsylum = map_property(UNDEAD_ASYLUM)  # type: LuaBND

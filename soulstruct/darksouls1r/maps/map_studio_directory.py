"""Identical to PTDE, but with proper DSR type hints (e.g. `MSB`)."""
from __future__ import annotations

__all__ = ["MapStudioDirectory"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file_directory import map_property
from soulstruct.base.maps.map_studio_directory import MapStudioDirectory as _BaseMapStudioDirectory

from .constants import *
from .msb import MSB


@dataclass(slots=True)
class MapStudioDirectory(_BaseMapStudioDirectory[MSB]):
    """Dark Souls (either version) `MapStudio` directory.

    The format of these files is exactly the same in PTD and DSR. The vanilla DSR files have a few new additions (the
    bonfire near Vamos and lots of Arena-related entries), but you can safely use the exact same MSB files in either
    version of the game if you're not concerned with these differences.

    Note that Darkroot Garden (m12_00) has two MSB files, one ending in '00' (pre-DLC map data) and one ending in
    '01' (post-DLC map data). The PC version of the game will always have the DLC, so the '00' version is completely
    unused and ignored by Soulstruct. (You can even just delete the MSB file.) Note that 'm12_00_00_00.emevd[.dcx]'
    is still used for Darkroot's event scripts, however.
    """

    FILE_CLASS: tp.ClassVar = MSB
    ALL_MAPS: tp.ClassVar = tuple(m for m in ALL_MAPS if m.msb_file_stem)
    GET_MAP: tp.ClassVar = staticmethod(get_map)

    QUIETLY_IGNORED_FILE_STEMS: tp.ClassVar = {
        "m12_00_00_00",  # pre-DLC Darkroot Garden MSB (PC version always has DLC)
        "m99_80_00_00",  # DSR test maps
        "m99_80_00_01",
        "m99_80_00_02",
        "m99_80_10_00",
        "m99_80_10_01",
        "m99_80_10_02",
        "m99_80_20_00",
        "m99_99_97_00",
        "m99_99_98_00",
        "m99_99_98_03",
        "m99_99_98_07",
        "m99_99_98_08",
        "m99_99_98_09",
        "m99_99_98_20",
        "m99_99_98_23",
        "m99_99_98_25",
        "m99_99_99_99",
    }

    # Type hint override.
    files: dict[str, MSB] = field(default_factory=dict)

    Common = map_property(COMMON)  # type: MSB
    Depths = map_property(DEPTHS)  # type: MSB
    UndeadBurg = map_property(UNDEAD_BURG)  # type: MSB  # and Undead Parish
    FirelinkShrine = map_property(FIRELINK_SHRINE)  # type: MSB
    PaintedWorld = map_property(PAINTED_WORLD)  # type: MSB
    DarkrootGarden = map_property(DARKROOT_GARDEN)  # type: MSB  # and Darkroot Basin
    Oolacile = map_property(OOLACILE)  # type: MSB  # and all DLC
    Catacombs = map_property(CATACOMBS)  # type: MSB
    TombOfTheGiants = map_property(TOMB_OF_THE_GIANTS)  # type: MSB
    AshLake = map_property(ASH_LAKE)  # type: MSB  # and Great Hollow
    Blighttown = map_property(BLIGHTTOWN)  # type: MSB
    LostIzalith = map_property(LOST_IZALITH)  # type: MSB  # and Demon Ruins
    SensFortress = map_property(SENS_FORTRESS)  # type: MSB
    AnorLondo = map_property(ANOR_LONDO)  # type: MSB
    NewLondoRuins = map_property(NEW_LONDO_RUINS)  # type: MSB  # and Valley of Drakes
    DukesArchives = map_property(DUKES_ARCHIVES)  # type: MSB
    KilnOfTheFirstFlame = map_property(KILN_OF_THE_FIRST_FLAME)  # type: MSB
    UndeadAsylum = map_property(UNDEAD_ASYLUM)  # type: MSB

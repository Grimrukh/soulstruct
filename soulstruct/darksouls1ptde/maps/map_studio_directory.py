__all__ = ["MapStudioDirectory"]

from soulstruct.base.maps.map_studio_directory import MapStudioDirectory as _BaseMapStudioDirectory
from soulstruct.games import DarkSoulsPTDEType

from .constants import ALL_MAPS, get_map
from .msb import MSB


class MapStudioDirectory(_BaseMapStudioDirectory, DarkSoulsPTDEType):
    """Dark Souls (either version) `MapStudio` directory.

    The format of these files is exactly the same in PTD and DSR. The vanilla DSR files have a few new additions (the
    bonfire near Vamos and lots of Arena-related entries), but you can safely use the exact same MSB files in either
    version of the game if you're not concerned with these differences.

    Note that Darkroot Garden (m12_00) has two MSB files, one ending in '00' (pre-DLC map data) and one ending in
    '01' (post-DLC map data). The PC version of the game will always have the DLC, so the '00' version is completely
    unused and ignored by Soulstruct. (You can even just delete the MSB file.) Note that 'm12_00_00_00.emevd[.dcx]'
    is still used for Darkroot's event scripts, however.
    """

    MSB_CLASS = MSB
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)

    Depths: MSB
    UndeadBurg: MSB  # and Undead Parish
    FirelinkShrine: MSB
    PaintedWorld: MSB
    DarkrootGarden: MSB  # and Darkroot Basin
    Oolacile: MSB  # and Royal Wood and Chasm of the Abyss
    Catacombs: MSB
    TombOfTheGiants: MSB
    AshLake: MSB  # and Great Hollow
    Blighttown: MSB  # and Quelaag's Domain
    LostIzalith: MSB  # and Demon Ruins
    SensFortress: MSB
    AnorLondo: MSB
    NewLondoRuins: MSB  # and Valley of Drakes
    DukesArchives: MSB  # and Crystal Cave
    KilnOfTheFirstFlame: MSB
    UndeadAsylum: MSB

    msbs: dict[str, MSB]

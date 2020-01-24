import logging
from pathlib import Path

from soulstruct.maps.msb import MSB
from soulstruct.utilities.core import BiDict

_LOGGER = logging.getLogger(__name__)


DARK_SOULS_MAP_NAMES = BiDict(
    ('m10_00_00_00', 'Depths'),
    ('m10_01_00_00', 'UndeadBurg'),
    ('m10_02_00_00', 'FirelinkShrine'),
    ('m11_00_00_00', 'PaintedWorld'),
    ('m12_00_00_01', 'DarkrootGarden'),  # note the trailing 1, as in `m12_00_00_01.msb`, the DLC version
    ('m12_01_00_00', 'Oolacile'),
    ('m13_00_00_00', 'Catacombs'),
    ('m13_01_00_00', 'TombOfTheGiants'),
    ('m13_02_00_00', 'AshLake'),
    ('m14_00_00_00', 'Blighttown'),
    ('m14_01_00_00', 'LostIzalith'),
    ('m15_00_00_00', 'SensFortress'),
    ('m15_01_00_00', 'AnorLondo'),
    ('m16_00_00_00', 'NewLondoRuins'),
    ('m17_00_00_00', 'DukesArchives'),
    ('m18_00_00_00', 'KilnOfTheFirstFlame'),
    ('m18_01_00_00', 'UndeadAsylum'),
)


class DarkSoulsMaps(object):

    Depths: MSB
    UndeadBurg: MSB  # and Undead Parish
    FirelinkShrine: MSB
    PaintedWorld: MSB
    DarkrootGarden: MSB  # and Darkroot Basin
    Oolacile: MSB  # and all DLC
    Catacombs: MSB
    TombOfTheGiants: MSB
    AshLake: MSB  # and Great Hollow
    Blighttown: MSB
    LostIzalith: MSB  # and Demon Ruins
    SensFortress: MSB
    AnorLondo: MSB
    NewLondoRuins: MSB  # and Valley of Drakes
    DukesArchives: MSB
    KilnOfTheFirstFlame: MSB
    UndeadAsylum: MSB

    def __init__(self, map_studio_directory=None):
        """Unpack Dark Souls MSB map data files into one single modifiable structure.

        The format of these files is exactly the same in PTD and DSR. The vanilla DSR files have a few new additions
        (the bonfire near Vamos and lots of Arena-related entries), but you can safely use the exact same MSB files in
        either version of the game if you're not concerned with these differences.

        Note that you only need to reload the map (e.g. by saving and quitting, or getting sufficiently far away from
        the map) to see changes in these files while playing the game. You do NOT need to fully restart the game, unlike
        with text and parameter/lighting changes.

        Note that Darkroot Garden (m12_00) has two MSB files, one ending in '00' (pre-DLC map data) and one ending in
        '01' (post-DLC map data). The PC version of the game will always have the DLC, so the '00' version is completely
        unused and ignored by Soulstruct. (You can even just delete the MSB file.) Note that 'm12_00_00_00.emevd[.dcx]'
        is still used for Darkroot's event scripts, however.

        TODO: Discuss/enforce unusual region limit in Duke's Archives (and possibly DSR Undead Asylum).

        Args:
            map_studio_directory: Directory where all the MSB files are stored. This will be inside 'map/MapStudio' in
                your game directory (either version). (Ignore the 'MapStudioNew' folder next to this directory in DSR,
                which does nothing.)
        """
        self._directory = None
        self._data = {}

        if map_studio_directory is None:
            return

        map_studio_directory = Path(map_studio_directory)

        if not map_studio_directory.is_dir():
            raise ValueError("DarkSoulsMaps should be initialized with the directory containing your MSB files.")

        self._directory = map_studio_directory

        for msb_base_name, msb_attr_name in DARK_SOULS_MAP_NAMES.items():
            msb_path = self._directory / (msb_base_name + '.msb')
            try:
                self._data[msb_attr_name] = MSB(msb_path)
                setattr(self, msb_attr_name, self._data[msb_attr_name])
            except FileNotFoundError:
                raise FileNotFoundError(f"Could not find MSB file {repr(msb_base_name)} ({msb_attr_name}) in given "
                                        f"directory.")

    def __getitem__(self, map_name):
        return self._data[map_name]

    def save(self, msb_directory=None):
        if msb_directory is None:
            msb_directory = self._directory
        else:
            msb_directory = Path(msb_directory)
        for msb_name in DARK_SOULS_MAP_NAMES.values():
            msb_path = msb_directory / self._data[msb_name].msb_path.name
            self._data[msb_name].write_packed(msb_path)
        _LOGGER.info("Dark Souls map files (MSB) written successfully.")

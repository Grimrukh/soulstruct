import logging
from pathlib import Path

from soulstruct.maps.msb import MSB
from soulstruct.constants.darksouls1.maps import ALL_MAPS, get_map

_LOGGER = logging.getLogger(__name__)


class DarkSoulsMaps(object):

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

        for game_map in ALL_MAPS:
            if game_map.msb_file_stem is None:
                continue
            msb_path = self._directory / (game_map.msb_file_stem + '.msb')
            try:
                self._data[game_map.name] = MSB(msb_path)
                setattr(self, game_map.name, self._data[game_map.name])
            except FileNotFoundError:
                raise FileNotFoundError(f"Could not find MSB file {repr(game_map.msb_file_stem)} "
                                        f"({game_map.name}) in given directory.")

    def __getitem__(self, map_source):
        game_map = get_map(map_source)
        return self._data[game_map.name]

    def save(self, msb_directory=None):
        if msb_directory is None:
            msb_directory = self._directory
        else:
            msb_directory = Path(msb_directory)
        for msb in self._data.values():
            msb_path = msb_directory / msb.msb_path.name
            msb.write_packed(msb_path)
        _LOGGER.info("Dark Souls map files (MSB) written successfully.")

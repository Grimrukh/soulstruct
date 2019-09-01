import os

from soulstruct.maps.msb import MSB


# TODO: unify with EMEVD constants.
DARK_SOULS_MAP_NAMES = {
    'm10_00_00_00': 'Depths',
    'm10_01_00_00': 'UndeadBurg',
    'm10_02_00_00': 'FirelinkShrine',
    'm11_00_00_00': 'PaintedWorld',
    'm12_00_00_01': 'DarkrootGarden',
    'm12_01_00_00': 'Oolacile',
    'm13_00_00_00': 'Catacombs',
    'm13_01_00_00': 'TombOfTheGiants',
    'm13_02_00_00': 'AshLake',
    'm14_00_00_00': 'Blighttown',
    'm14_01_00_00': 'LostIzalith',
    'm15_00_00_00': 'SensFortress',
    'm15_01_00_00': 'AnorLondo',
    'm16_00_00_00': 'NewLondoRuins',
    'm17_00_00_00': 'DukesArchives',
    'm18_00_00_00': 'KilnOfTheFirstFlame',
    'm18_01_00_00': 'UndeadAsylum',

}


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

    # TODO: should I set up alias names for 'shared' maps (e.g. DemonRuins)?

    def __init__(self, map_studio_directory=None):
        """Unpack Dark Souls MSB map data files into one single modifiable structure.

        The format of these files is exactly the same in PTD and DSR. The vanilla DSR files have a few new additions
        (the bonfire near Vamos and lots of Arena-related entries), but you can safely use the exact same MSB files in
        either version of the game.

        Note that you only need to reload the map (e.g. by saving and quitting) to see changes in these files while
        playing the game. You do NOT need to fully restart the game, unlike text and parameter data.

        Note that Darkroot Garden (m12_00) has two MSB files, one ending in '00' (pre-DLC map data) and one ending in
        '01' (post-DLC map data). The PC version of the game will always have the DLC, so the '00' version is completely
        unused and ignored by Soulstruct. (You can even just delete the MSB file.) There are also plenty of other
        MSB files that are completely unused.

        TODO: Discuss/enforce unusual region limit in Duke's Archives (and possibly DSR Undead Asylum).

        Args:
            map_studio_directory: Directory where all the 'mXX_XX_00_00.msb' files are stored. This will be inside
                'map/MapStudio' in your game directory (either version). (Ignore the 'MapStudioNew' folder next to this
                directory in DSR, which does nothing.)
        """
        if map_studio_directory is None:
            return

        if not os.path.isdir(map_studio_directory):
            raise ValueError("DarkSoulsMaps should be initialized with the directory containing your MSB files.")

        self._directory = map_studio_directory
        self._data = {}

        for msb_base_name, msb_attr_name in DARK_SOULS_MAP_NAMES.items():
            msb_path = os.path.join(self._directory, msb_base_name) + '.msb'
            try:
                self._data[msb_attr_name] = MSB(msb_path)
                setattr(self, msb_attr_name, self._data[msb_attr_name])
            except FileNotFoundError:
                raise FileNotFoundError(f"Could not find MSB file {repr(msb_base_name)} ({msb_attr_name}) in given "
                                        f"directory.")

    def __getitem__(self, map_name):
        return self._data[map_name]

    def save(self):
        for msb_name in DARK_SOULS_MAP_NAMES.values():
            self._data[msb_name].write_packed()
        print("\n# All Dark Souls map files saved successfully.")


if __name__ == '__main__':
    dsm = DarkSoulsMaps('G:/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA/map/MapStudio')

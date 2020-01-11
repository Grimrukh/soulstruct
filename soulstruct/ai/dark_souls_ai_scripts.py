from pathlib import Path

from soulstruct.bnd import BND
from soulstruct.ai.core import LuaBND
from soulstruct.utilities import BiDict

DARK_SOULS_AI_BND_NAMES = BiDict(
    ('aiCommon', 'Common'),
    ('m10_00_00_00', 'Depths'),
    ('m10_01_00_00', 'UndeadBurg'),
    ('m10_02_00_00', 'FirelinkShrine'),
    ('m11_00_00_00', 'PaintedWorld'),
    ('m12_00_00_00', 'DarkrootGarden'),
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


class DarkSoulsAIScripts(object):

    Common: LuaBND  # scripts loaded in all maps; also contains internal functions that should not be edited
    Event: LuaBND  # internal functions; never processed automatically
    Depths: LuaBND
    UndeadBurg: LuaBND  # and Undead Parish
    FirelinkShrine: LuaBND
    PaintedWorld: LuaBND
    DarkrootGarden: LuaBND  # and Darkroot Basin
    Oolacile: LuaBND  # and all DLC
    Catacombs: LuaBND
    TombOfTheGiants: LuaBND
    AshLake: LuaBND  # and Great Hollow
    Blighttown: LuaBND
    LostIzalith: LuaBND  # and Demon Ruins
    SensFortress: LuaBND
    AnorLondo: LuaBND
    NewLondoRuins: LuaBND  # and Valley of Drakes
    DukesArchives: LuaBND
    KilnOfTheFirstFlame: LuaBND
    UndeadAsylum: LuaBND

    def __init__(self, script_directory=None):
        """Unpack Dark Souls MSB AI LuaBND scripts into one single modifiable structure.

        Note that the vanilla game uses pre-compiled Lua bytecode for a minor efficiency upgrade, but uncompiled Lua
        scripts work just as well. Use the `.decompile_all()` method to generate them from any compiled scripts.

        The same script will work in both PTDE and DSR, but decompiling is only offered (with Katalash's
        'DSLuaDecompiler' tool) for DSR. PTDE files have the variable names stripped anyway, which makes them much
        harder to edit even when decompiled. If you want to customize PTDE scripts, I recommend doing all the work in
        DSR and then just copying the scripts over.

        `aiCommon.luabnd` ('Common') contains scripts that are loaded in all maps, which includes internal scripts
        with global functions that are accessed in every script. If you want to decompile these internal scripts, you
        must call `DarkSoulsAIScripts().Common.decompile(battle_or_logic_only=False)`, and similar to recompile them
        (for testing) or save the decompiled scripts into the LuaBND.

        `eventCommon.luabnd` contains scripts that are solely internal. This BND is unpacked in `.event_common_bnd`
        for manual inspection and modification, if you really want, but this shouldn't be necessary. It is written
        automatically by `.save()`.

        Note that you only need to reload the map (e.g. by saving and quitting, or getting sufficiently far away from
        the map) to see changes in these files while playing the game. You do NOT need to fully restart the game, unlike
        with text and parameter/lighting changes, *UNLESS* you need to reload a script in Common.

        Args:
            script_directory: Directory where all the `.luabnd` files are stored. This will be inside 'script' in
                your game directory (either version).
        """
        self._directory = None
        self._data = {}
        self.event_common_bnd = None

        if script_directory is None:
            return
        self._directory = Path(script_directory)
        if not self._directory.is_dir():
            raise ValueError("DarkSoulsAIScripts should be initialized with the directory containing LuaBND files.")

        for luabnd_base_name, luabnd_attr_name in DARK_SOULS_AI_BND_NAMES.items():
            luabnd_path = self._directory / (luabnd_base_name + '.luabnd')
            try:
                self._data[luabnd_attr_name] = LuaBND(luabnd_path)
                setattr(self, luabnd_attr_name, self._data[luabnd_attr_name])
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not find LuaBND file {repr(luabnd_base_name)} ({luabnd_attr_name}) in given directory.")

        event_path = self._directory / "eventCommon.luabnd"
        try:
            self.event_common_bnd = BND(event_path)
        except FileNotFoundError:
            raise FileNotFoundError("Could not find `eventCommon.luabnd[.dcx]` file in given directory.")

    def __getitem__(self, luabnd_name):
        return self._data[luabnd_name]

    def save(self, script_directory=None):
        if script_directory is None:
            script_directory = self._directory
        script_directory = Path(script_directory)
        for luabnd_name in DARK_SOULS_AI_BND_NAMES.values():
            luabnd_path = script_directory / self._data[luabnd_name].bnd.bnd_path.name
            self._data[luabnd_name].write(luabnd_path)
        event_common_path = script_directory / self.event_common_bnd.bnd_path.name
        self.event_common_bnd.write(event_common_path)
        print("\n# INFO: --------> Dark Souls AI script (LuaBND) files saved successfully.")

    def compile_all(self, output_directory=None, including_other=False):
        for bnd_name, luabnd in self._data.items():
            print(f"# INFO: Compiling Lua scripts in {bnd_name}...")
            luabnd.compile_all(output_directory=output_directory, including_other=including_other)

    def decompile_all(self, output_directory=None, including_other=False):
        for bnd_name, luabnd in self._data.items():
            print(f"# INFO: Decompiling Lua scripts in {bnd_name}...")
            luabnd.decompile_all(output_directory=output_directory, including_other=including_other)

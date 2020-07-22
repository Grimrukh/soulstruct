import logging
from pathlib import Path

from soulstruct.bnd import BND
from soulstruct.ai.core import LuaBND
from soulstruct.constants.darksouls1.maps import ALL_MAPS, get_map

__all__ = ["DarkSoulsAIScripts"]
_LOGGER = logging.getLogger(__name__)


class DarkSoulsAIScripts:

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
        """Unpack Dark Souls AI LuaBND scripts into one single modifiable structure.

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

        for game_map in ALL_MAPS:
            luabnd_path = self._directory / (game_map.ai_file_stem + ".luabnd")
            try:
                self._data[game_map.name] = LuaBND(luabnd_path)
                setattr(self, game_map.name, self._data[game_map.name])
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not find LuaBND file {repr(game_map.ai_file_stem)} ({game_map.name}) in given directory."
                )

        event_path = self._directory / "eventCommon.luabnd"
        try:
            self.event_common_bnd = BND(event_path)
        except FileNotFoundError:
            raise FileNotFoundError("Could not find `eventCommon.luabnd[.dcx]` file in given directory.")

    def __getitem__(self, map_source):
        game_map = get_map(map_source)
        return self._data[game_map.name]

    def __iter__(self):
        return iter(self._data)

    def save(self, script_directory=None):
        if script_directory is None:
            script_directory = self._directory
        script_directory = Path(script_directory)
        for luabnd in self._data.values():
            luabnd_path = script_directory / luabnd.bnd.bnd_path.name
            luabnd.write(luabnd_path)
        event_common_path = script_directory / self.event_common_bnd.bnd_path.name
        self.event_common_bnd.write(event_common_path)
        _LOGGER.info("Dark Souls AI script files (LuaBND) written successfully.")

    def compile_all(self, output_directory=None, including_other=False):
        for bnd_name, luabnd in self._data.items():
            _LOGGER.info(f"Compiling Lua scripts in {bnd_name}...")
            luabnd.compile_all(output_directory=output_directory, including_other=including_other)

    def decompile_all(self, output_directory=None, including_other=False):
        for bnd_name, luabnd in self._data.items():
            _LOGGER.info(f"Decompiling Lua scripts in {bnd_name}...")
            luabnd.decompile_all(output_directory=output_directory, including_other=including_other)

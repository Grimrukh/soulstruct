from __future__ import annotations

__all__ = ["ScriptDirectory"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file_directory import GameFileMapDirectory
from .luabnd import LuaBND

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class ScriptDirectory(GameFileMapDirectory, abc.ABC):
    """Unpack LuaBND scripts in a directory (usually `script`) into one single modifiable structure.

    Note that the vanilla game uses pre-compiled Lua bytecode for a minor efficiency upgrade, but uncompiled Lua
    scripts work just as well. Use the `.decompile_all()` method to generate them from any compiled scripts
    (currently does not work for PTDE or Bloodborne).
    TODO: Has Katalash upgraded this decompiler to support Bloodborne?

    The same script will work in both PTDE and DSR, but decompiling is only offered (with Katalash's
    'DSLuaDecompiler' tool) for DSR. PTDE files have the variable names stripped anyway, which makes them much
    harder to edit even when decompiled. If you want to customize PTDE scripts, I recommend doing all the work in
    DSR and then just copying the scripts over.

    `aiCommon.luabnd` ('Common') contains scripts that are loaded in all maps, which includes internal scripts
    with global functions that are accessed in every script. If you want to decompile these internal scripts, you
    must call `ScriptDirectory.Common.decompile(battle_or_logic_only=False)`, and similar to recompile them
    (for testing) or save the decompiled scripts into the LuaBND.

    `eventCommon.luabnd` contains scripts that are solely internal. This BND is unpacked in `.event_common_bnd`
    for manual inspection and modification, if you really want, but this shouldn't be necessary. It is written
    automatically by `.save()`.

    Note that you only need to reload the map (e.g. by saving and quitting, or getting sufficiently far away from
    the map) to see changes in these files while playing the game. You do NOT need to fully restart the game, unlike
    with text and parameter/lighting changes, *UNLESS* you need to reload a script in Common.
    """
    FILE_NAME_PATTERN: tp.ClassVar[str] = r".*\.luabnd"
    FILE_CLASS: tp.ClassVar[tp.Type[LuaBND]] = LuaBND
    FILE_EXTENSION = ".luabnd"
    MAP_STEM_ATTRIBUTE = "ai_file_stem"

    files: dict[str, LuaBND] = field(default_factory=dict)

    def compile_all(self, output_directory=None, include_unknown_scripts=False):
        for luabnd_stem, luabnd in self.files.items():
            _LOGGER.info(f"Compiling Lua scripts in {luabnd_stem}...")
            luabnd.compile_all(output_directory, include_unknown_scripts)

    def decompile_all(self, output_directory=None, include_unknown_scripts=False):
        for luabnd_stem, luabnd in self.files.items():
            _LOGGER.info(f"Decompiling Lua scripts in {luabnd_stem}...")
            luabnd.decompile_all(output_directory, include_unknown_scripts)

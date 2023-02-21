from __future__ import annotations

__all__ = ["AIScriptDirectory"]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file_directory import GameFileMapDirectory
from .luabnd import LuaBND

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class AIScriptDirectory(GameFileMapDirectory, abc.ABC):
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
    must call `AIScriptDirectory.Common.decompile(battle_or_logic_only=False)`, and similar to recompile them
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

    @classmethod
    def from_unpacked_luabnds(cls, directory_path: Path | str):
        """Open a collection of unpacked `LuaBND` binders instead of the binders themselves."""

        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Missing directory: {directory_path}")
        all_map_stems = [getattr(game_map, cls.MAP_STEM_ATTRIBUTE) for game_map in cls.ALL_MAPS]
        all_map_stems = [stem for stem in all_map_stems if stem is not None]
        files = {}
        for file_path in directory_path.glob("*"):
            if file_path.is_dir() and file_path.stem in all_map_stems:
                # Try to load `LuaBND` from unpacked binder.
                files[file_path.stem] = cls.FILE_CLASS.from_unpacked_path(file_path)
                all_map_stems.remove(file_path.stem)
                continue

        if all_map_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_map_stems)}")

        return cls(directory=directory_path, files=files)

    def write_unpacked_luabnds(self, directory_path: Path | str = None):
        if directory_path is None:
            if self.directory is None:
                raise ValueError("Cannot autodetect directory name (`directory` not set).")
            directory_path = self.directory
        directory_path = Path(directory_path)
        all_map_stems = [getattr(game_map, self.MAP_STEM_ATTRIBUTE) for game_map in self.ALL_MAPS]
        directory_path.mkdir(parents=True, exist_ok=True)
        for file_stem, luabnd in self.files.items():
            if file_stem in all_map_stems:
                all_map_stems.remove(file_stem)
            else:
                _LOGGER.warning(f"Writing unknown LuaBND file found in `{self.__class__.__name__}`: {file_stem}")
            luabnd.write_unpacked_directory(directory_path / f"{file_stem}")
        if all_map_stems:
            _LOGGER.warning(
                f"Could not find some file keys while writing `{self.__class__.__name__}` directory: "
                f"{', '.join(all_map_stems)}"
            )
        _LOGGER.info(
            f"`{self.__class__.__name__}` unpacked LuaBNDs written to `{directory_path}` successfully "
            f"({len(self.files)} folders)."
        )

    def compile_all(self, output_directory=None, include_unknown_scripts=False):
        for luabnd_stem, luabnd in self.files.items():
            _LOGGER.info(f"Compiling Lua scripts in {luabnd_stem}...")
            luabnd.compile_all(output_directory, include_unknown_scripts)

    def decompile_all(self, output_directory=None, include_unknown_scripts=False):
        for luabnd_stem, luabnd in self.files.items():
            _LOGGER.info(f"Decompiling Lua scripts in {luabnd_stem}...")
            luabnd.decompile_all(output_directory, include_unknown_scripts)

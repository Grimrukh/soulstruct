from __future__ import annotations

__all__ = ["EventDirectory"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass
from pathlib import Path

from soulstruct.base.game_types.map_types import Map
from soulstruct.base.game_file_directory import GameFileMapDirectory
from .emevd import EMEVD

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class EventDirectory(GameFileMapDirectory[EMEVD], abc.ABC):
    """Load a directory full of any valid `EMEVD` sources, one per map."""

    FILE_NAME_PATTERN: tp.ClassVar[str] = r".*\.(evs\.py|evs|py|emevd|txt)"
    FILE_CLASS: tp.ClassVar[type[EMEVD]] = None
    FILE_EXTENSION = ".emevd"
    MAP_STEM_ATTRIBUTE = "emevd_file_stem"

    # Specify `COMMON_FUNC` game map so that it can be detected in `files` and written first (as other EMEVD files may
    # need to reference it).
    COMMON_FUNC: tp.ClassVar[Map] = None

    @classmethod
    def from_path(cls, directory_path: Path | str):
        """Loads files as appropriate type (EMEVD/EVS/numeric)."""
        if cls.FILE_NAME_PATTERN is None or cls.FILE_CLASS is None:
            raise TypeError(
                f"`GameFileDirectory` subclass `{cls.__name__}` must define `FILE_NAME_PATTERN` and `FILE_CLASS` class "
                f"variables, or override `from_path()` with its own different logic."
            )

        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Missing directory: {directory_path}")
        all_map_stems = [getattr(game_map, cls.MAP_STEM_ATTRIBUTE) for game_map in cls.ALL_MAPS]
        if cls.COMMON_FUNC:
            all_map_stems.append(cls.COMMON_FUNC.emevd_file_stem)
        files = {}
        file_name_re = re.compile(cls.FILE_NAME_PATTERN + r"(\.dcx)?$")
        for file_path in directory_path.glob("*"):
            if file_name_re.match(file_path.name):
                file_stem = file_path.name.split(".")[0]  # `.stem` not good enough with possible double DCX extension
                if file_stem in all_map_stems:
                    # Tries to auto-detect EMEVD, EVS, and numeric (.txt) files appropriately.
                    try:
                        source_type = cls.FILE_CLASS.from_auto_detect_source_type(file_path)
                    except TypeError:
                        _LOGGER.error(f"Cannot read file format in `{cls.__name__}` directory: {file_path.name}")
                        continue
                    match source_type:
                        case "numeric_path":
                            files[file_stem] = cls.FILE_CLASS.from_numeric_path(file_path)
                        case "emevd_path":
                            files[file_stem] = cls.FILE_CLASS.from_path(file_path)
                        case "evs_path":
                            files[file_stem] = cls.FILE_CLASS.from_evs_path(file_path, script_directory=directory_path)
                        case _:
                            _LOGGER.error(f"Cannot open EMEVD source type '{source_type}': {file_path.name}")
                            continue
                    all_map_stems.remove(file_stem)
                else:
                    _LOGGER.warning(f"Ignoring unexpected file in `{cls.__name__}` directory: {file_path.name}")
                    continue

        if all_map_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_map_stems)}")

        return cls(directory=directory_path, files=files)

    def write_evs(
        self,
        evs_directory=None,
        enums_directory: Path | str = None,
        warn_missing_enums=True,
        enums_module_prefix=".",
    ):
        """Write EVS scripts for all EMEVD files.

        If given, `enums_directory` should contain files named `{emevd_path_stem}_enums.py`. The entities module
        matching the map stem for each EMEVD will be available as a star import for that EVS script; all other modules
        with names ending in "_enums.py" present in the directory will be available for non-star import, for the rare
        case where map EMEVD references IDs from other maps (e.g. in `PlayCutscene`).

        See `EMEVD.write_evs()` for argument usage.
        """
        if evs_directory is None:
            evs_directory = self.directory
        evs_directory = Path(evs_directory)
        if enums_directory is not None:
            enums_directory = Path(enums_directory)

        enums_module_paths = list(enums_directory.glob("*_enums.py")) if enums_directory else []

        # Create one `GameEnumsManager` passed to all non-CommonFunc EMEVDs.
        enums_manager = self.FILE_CLASS.ENTITY_ENUMS_MANAGER(enums_module_paths)  # `all_event_ids` set per EMEVD

        common_func_emevd = None  # type: EMEVD | None
        if self.COMMON_FUNC and self.COMMON_FUNC.emevd_file_stem in self.files:
            # Write `common_func` first.
            common_func_emevd = self.files[self.COMMON_FUNC.emevd_file_stem]
            common_func_emevd.write_evs(
                evs_path=evs_directory / f"{common_func_emevd.map_name}.py",  # no '.evs' extension (for importing)
                enums_module_paths=[],
                star_import_module_names=[],
                warn_missing_enums=warn_missing_enums,
                enums_module_prefix=enums_module_prefix,
                event_function_prefix="CommonFunc",
                docstring="Common functions that can be imported and used in other EVS scripts.",
                enums_manager=None,
            )
            _LOGGER.info(f"Wrote EVS for COMMON_FUNC map: {common_func_emevd.map_name}")

        for map_name, emevd in self.files.items():
            if self.COMMON_FUNC and map_name == self.COMMON_FUNC.emevd_file_stem:
                continue  # already done above

            # Reset used and missing enums for each map.
            enums_manager.used_enums.clear()
            enums_manager.missing_enums.clear()

            emevd.write_evs(
                evs_path=evs_directory / f"{emevd.map_name}.evs.py",
                star_import_module_names=[f"{emevd.map_name}_enums"],
                warn_missing_enums=warn_missing_enums,
                enums_module_prefix=enums_module_prefix,
                event_function_prefix="Event",
                docstring=self.GET_MAP(map_name).verbose_name,
                common_func_emevd=common_func_emevd,
                enums_manager=enums_manager,
            )
            _LOGGER.info(f"Wrote EVS for map {emevd.map_name} successfully.")

        _LOGGER.info(f"All EMEVD files written to decompiled EVS scripts successfully in '{evs_directory}'.")

    def write_numeric(self, event_directory=None):
        if event_directory is None:
            event_directory = self.directory
        event_directory = Path(event_directory)
        for emevd in self.files.values():
            emevd.write_numeric(event_directory / emevd.path.name.split(".")[0] + ".txt")
        _LOGGER.info("All EMEVD files written to numeric TXT format successfully.")

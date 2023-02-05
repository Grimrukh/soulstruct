from __future__ import annotations

__all__ = ["EMEVDDirectory"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass
from pathlib import Path

from soulstruct.base.game_types.map_types import Map
from soulstruct.base.game_file_directory import GameFileMapDirectory
from .emevd import EMEVD

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class EMEVDDirectory(GameFileMapDirectory[EMEVD], abc.ABC):
    """Load a directory full of any valid `EMEVD` sources, one per map."""

    FILE_NAME_PATTERN: tp.ClassVar[str] = r".*(\.evs\.py|\.evs|\.py|\.emevd|\.txt)"
    FILE_CLASS: tp.ClassVar[tp.Type[EMEVD]] = None
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
        files = {}
        file_name_re = re.compile(cls.FILE_NAME_PATTERN + r"(\.dcx)?")
        for file_path in directory_path.glob("*"):
            if file_name_re.match(file_path.name):
                file_stem = file_path.name.split(".")[0]  # `.stem` not good enough with possible double DCX extension
                if file_stem in all_map_stems:
                    # Tries to auto-detect EMEVD, EVS, and numeric (.txt) files appropriately.
                    files[file_path.name] = cls.FILE_CLASS.from_auto_detect_source_type(file_path)[0]
                    all_map_stems.remove(file_stem)
                else:
                    _LOGGER.warning(f"Ignoring unexpected file in `{cls.__name__}` directory: {file_path.name}")
                    continue

        if all_map_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_map_stems)}")

        return cls(directory_path, files)

    def write_evs(
        self,
        emevd_directory=None,
        entities_directory=None,
        warn_missing_enums=True,
        entity_module_prefix=".",
    ):
        """Write EVS scripts for all EMEVD files.

        If given, `entities_directory` should contain files named `{emevd_path_stem}_entities.py`. The entities module
        matching the map stem for each EMEVD will be available as a star import for that EVS script; all other modules
        with names ending in "_entities.py" present in the directory will be available for non-star import, for the rare
        case where map EMEVD references IDs from other maps (e.g. in `PlayCutscene`).

        See `EMEVD.write_evs()` for argument usage.
        """
        if emevd_directory is None:
            emevd_directory = self.directory
        emevd_directory = Path(emevd_directory)
        if entities_directory is not None:
            entities_directory = Path(entities_directory)

        common_func_emevd: EMEVD | None
        if self.COMMON_FUNC and self.COMMON_FUNC.name in self.files:
            # Write `common_func` first.
            common_func_emevd = self.files[self.COMMON_FUNC.name]
            common_func_emevd.write_evs(
                evs_path=emevd_directory / f"{common_func_emevd.map_name}.py",  # no '.evs' extension (for importing)
                entity_star_module_paths=[],
                entity_non_star_module_paths=[],
                warn_missing_enums=warn_missing_enums,
                entity_module_prefix=entity_module_prefix,
                event_prefix="CommonFunc",
                docstring="Common functions that can be imported and used in other EVS scripts.",
            )
            _LOGGER.info(f"Wrote EVS for COMMON_FUNC map: {common_func_emevd.map_name}")
        else:
            common_func_emevd = None

        for map_name, emevd in self.files.items():
            if self.COMMON_FUNC and map_name == self.COMMON_FUNC.name:
                continue  # already done above
            entity_star_module_paths = []
            entity_non_star_module_paths = []

            if entities_directory and map_name != "Common":  # TODO: why not allow 'common_entities' import?
                matching_map_module_name = f"{emevd.map_name}_entities.py"
                for module_path in entities_directory.glob("*_entities.py"):
                    if module_path.name == matching_map_module_name:
                        entity_star_module_paths.append(module_path)
                    else:
                        entity_non_star_module_paths.append(module_path)

            emevd.write_evs(
                evs_path=emevd_directory / f"{emevd.map_name}.evs.py",
                entity_star_module_paths=entity_star_module_paths,
                entity_non_star_module_paths=entity_non_star_module_paths,
                warn_missing_enums=warn_missing_enums,
                entity_module_prefix=entity_module_prefix,
                event_prefix="Event",
                docstring=self.GET_MAP(map_name).verbose_name,
                common_func_emevd=common_func_emevd,
            )
            _LOGGER.info(f"Wrote EVS for map {emevd.map_name} successfully.")

        _LOGGER.info("All EMEVD files written to decompiled EVS scripts successfully.")

    def write_numeric(self, emevd_directory=None):
        if emevd_directory is None:
            emevd_directory = self.directory
        emevd_directory = Path(emevd_directory)
        for emevd in self.files.values():
            emevd.write_numeric(emevd_directory / emevd.path.name.split(".")[0] + ".txt")
        _LOGGER.info("All EMEVD files written to numeric TXT format successfully.")

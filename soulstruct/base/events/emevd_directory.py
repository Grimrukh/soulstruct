from __future__ import annotations

__all__ = ["EMEVDDirectory"]

import abc
import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.base.game_types.map_types import Map
from .emevd import EMEVD

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.utilities import GET_MAP_TYPING

_LOGGER = logging.getLogger(__name__)


class EMEVDDirectory(abc.ABC):
    """Load a directory full of any valid `EMEVD` sources, one per map."""

    _FILE_RE = r"{map_name}(\.evs\.py|\.evs|\.py|\.emevd|\.txt)"

    COMMON_FUNC: Map = None
    ALL_MAPS: tuple[Map] = None
    GET_MAP: GET_MAP_TYPING = None
    IS_DCX: bool = None
    EMEVD_CLASS: tp.Type[EMEVD] = None

    def __init__(self, emevd_directory=None):
        """Unpack all EMEVD event scripts into one single modifiable structure.

        Args:
            emevd_directory: Directory where all the `.emevd[.dcx]` files are stored. This will be inside 'event' in
                your game directory.
        """
        self._directory = None
        self.emevds = {}  # type: dict[str, EMEVD]

        if emevd_directory is None:
            return
        self._directory = Path(emevd_directory)
        if not self._directory.is_dir():
            raise ValueError("`EMEVDDirectory` should be initialized with the directory containing '.emevd' files.")
        self.load()

    def __getitem__(self, map_name):
        return self.emevds[map_name]

    def __repr__(self):
        return f"EMEVDDirectory({repr(str(self._directory))})"

    def write(self, emevd_directory=None):
        if emevd_directory is None:
            emevd_directory = self._directory
        emevd_directory = Path(emevd_directory)
        for emevd in self.emevds.values():
            emevd.write(emevd_directory / emevd.path.name)
        _LOGGER.info("All binary EMEVD files written successfully.")

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
            emevd_directory = self._directory
        emevd_directory = Path(emevd_directory)
        if entities_directory is not None:
            entities_directory = Path(entities_directory)

        if self.COMMON_FUNC and self.COMMON_FUNC.name in self.emevds:
            # Write `common_func` first.
            emevd = self.emevds[self.COMMON_FUNC.name]
            emevd.write_evs(
                evs_path=emevd_directory / f"{emevd.map_name}.py",  # no '.evs' extension (for importing)
                entity_star_module_paths=[],
                entity_non_star_module_paths=[],
                warn_missing_enums=warn_missing_enums,
                entity_module_prefix=entity_module_prefix,
                is_common_func=True,
                docstring="Common functions that can be imported and used in other EVS scripts.",
            )
            _LOGGER.info(f"Wrote EVS for COMMON_FUNC map: {emevd.map_name}")

        for map_name, emevd in self.emevds.items():
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
                is_common_func=False,
                docstring=self.GET_MAP(map_name).verbose_name,
            )
            _LOGGER.info(f"Wrote EVS for map {emevd.map_name} successfully.")

        _LOGGER.info("All EMEVD files written to decompiled EVS scripts successfully.")

    def write_numeric(self, emevd_directory=None):
        if emevd_directory is None:
            emevd_directory = self._directory
        emevd_directory = Path(emevd_directory)
        for emevd in self.emevds.values():
            emevd.write_numeric(emevd_directory / emevd.path.with_suffix(".txt").name)
        _LOGGER.info("All EMEVD files written to numeric TXT format successfully.")

    def load(self, emevd_directory=None):
        if emevd_directory is None:
            emevd_directory = self._directory
        emevd_directory = Path(emevd_directory)
        if self._directory is None:
            self._directory = emevd_directory
        missing_map_names = []
        files = list(emevd_directory.glob("*"))

        common_func_emevd = self.load_map_emevd(self.COMMON_FUNC, files) if self.COMMON_FUNC else None

        for game_map in [m for m in self.ALL_MAPS if m.emevd_file_stem]:
            _LOGGER.info(f"Loading EMEVD source for {game_map.emevd_file_stem} ({game_map.verbose_name})")
            emevd = self.load_map_emevd(game_map, files, common_func_emevd)
            if emevd is None:
                missing_map_names.append(game_map.name)
        if missing_map_names:
            _LOGGER.warning(f"Could not find EMEVD source files for {len(missing_map_names)} maps.")

    def load_map_emevd(self, game_map: Map, emevd_files: list[Path], common_func_emevd: EMEVD = None) -> EMEVD | None:
        events_path = re.compile(self._FILE_RE.format(map_name=game_map.emevd_file_stem))
        for file_path in emevd_files:
            if events_path.match(file_path.name):
                try:
                    emevd = self.emevds[game_map.name] = self.EMEVD_CLASS(
                        file_path, common_func_emevd=common_func_emevd
                    )
                except Exception as ex:
                    raise ValueError(f"Error while loading '{file_path}': {ex}")
                setattr(self, game_map.name, self.emevds[game_map.name])
                break
        else:
            return None
        return emevd

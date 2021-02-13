import abc
import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.game_types import Map
from .emevd import EMEVD

_LOGGER = logging.getLogger(__name__)


class EMEVDDirectory(abc.ABC):
    """Load a directory full of any valid `EMEVD` sources, one per map."""

    _FILE_RE = r"{map_name}(\.evs\.py|\.evs|\.py|\.emevd|\.txt)"

    ALL_MAPS: tuple[Map] = None
    GET_MAP: tp.Callable = None
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

    def write_evs(self, emevd_directory=None):
        if emevd_directory is None:
            emevd_directory = self._directory
        emevd_directory = Path(emevd_directory)
        for emevd in self.emevds.values():
            emevd.write_evs(emevd_directory / emevd.path.with_suffix(".evs.py").name)
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
        for game_map in [m for m in self.ALL_MAPS if m.emevd_file_stem]:
            events_path = re.compile(self._FILE_RE.format(map_name=game_map.emevd_file_stem))
            for file_path in emevd_directory.glob("*"):
                if events_path.match(file_path.name):
                    self.emevds[game_map.name] = self.EMEVD_CLASS(file_path)
                    setattr(self, game_map.name, self.emevds[game_map.name])
                    break
            else:
                raise FileNotFoundError(
                    f"Could not find EMEVD file for map {game_map.name} ({game_map.emevd_file_stem} in given directory."
                )

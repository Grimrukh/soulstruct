from __future__ import annotations

__all__ = ["TalkDirectory"]

import abc
import logging
import typing as tp
from pathlib import Path

if tp.TYPE_CHECKING:
    from soulstruct.base.game_types.map_types import Map
    from soulstruct.base.maps.utilities import GET_MAP_TYPING
    from .talk_esd_bnd import TalkESDBND

_LOGGER = logging.getLogger(__name__)


class TalkDirectory(abc.ABC):
    """Directory containing `TalkESDBND` files."""

    ALL_MAPS: tuple[Map] = None
    GET_MAP: GET_MAP_TYPING = None
    IS_DCX: bool = None
    TALKESDBND_CLASS: tp.Type[TalkESDBND] = None

    def __init__(self, talk_directory=None):
        """Unpack all talk ESD state machines into one single modifiable structure.

        Args:
            talk_directory: Directory where all the `.talkesbnd[.dcx]` files are stored. This will be inside
                'script/talk' in your game directory.
        """
        self._directory = None
        self.bnds = {}  # type: dict[str, TalkESDBND]

        if talk_directory is None:
            return
        self._directory = Path(talk_directory)
        if not self._directory.is_dir():
            raise ValueError("`TalkDirectory` should be initialized with the directory containing '.talkesdbnd' files.")
        self.load()

    def __getitem__(self, map_name):
        return self.bnds[map_name]

    def __repr__(self):
        return f"TalkDirectory({repr(str(self._directory))})"

    def write(self, talk_directory=None):
        if talk_directory is None:
            talk_directory = self._directory
        talk_directory = Path(talk_directory)
        for talkesdbnd in self.bnds.values():
            talkesdbnd.write(talk_directory / talkesdbnd.path.name)
        _LOGGER.info("All TalkESDBND files (TalkESDBND) written successfully.")

    def write_esp(self, talk_directory=None):
        if talk_directory is None:
            talk_directory = self._directory
        talk_directory = Path(talk_directory)
        for game_map in [m for m in self.ALL_MAPS if m.esd_file_stem]:
            talkesdbnd = self.bnds[game_map.name]
            talkesdbnd.write_esp(talk_directory=talk_directory / f"{game_map.esd_file_stem}")

    def load(self, talk_directory=None):
        if talk_directory is None:
            talk_directory = self._directory
        talk_directory = Path(talk_directory)
        if self._directory is None:
            self._directory = talk_directory
        for game_map in [m for m in self.ALL_MAPS if m.esd_file_stem]:
            talkesdbnd_path = talk_directory / game_map.esd_file_stem
            file_suffix = ".talkesdbnd"
            if self.IS_DCX:
                file_suffix += ".dcx"
            if (file_path := talkesdbnd_path.with_suffix(file_suffix)).is_file():
                if talkesdbnd_path.exists():
                    _LOGGER.warning(
                        f"Both a TalkESBND file and folder with stem {game_map.esd_file_stem} were found. "
                        f"Using the file."
                    )
                talkesdbnd_path = file_path
            try:
                self.bnds[game_map.name] = self.TALKESDBND_CLASS(talkesdbnd_path)
                setattr(self, game_map.name, self.bnds[game_map.name])
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not find TalkESDBND file {talkesdbnd_path} ({game_map.name}) in given directory."
                )

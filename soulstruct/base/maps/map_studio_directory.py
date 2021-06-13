import abc
import logging
import typing as tp
from pathlib import Path

from soulstruct.base.maps.msb.exceptions import MapError

if tp.TYPE_CHECKING:
    from .msb import MSB
    from soulstruct.game_types.msb_types import Map

_LOGGER = logging.getLogger(__name__)


class MapStudioDirectory(abc.ABC):

    MSB_CLASS = None  # type: tp.Type[MSB]
    ALL_MAPS = ()  # type: tuple[Map]
    GET_MAP = None  # type: tp.Callable[[tp.Union[str, tuple], tp.Optional[int]], Map]
    IS_DCX = False

    directory: tp.Optional[Path]

    def __init__(self, map_studio_directory=None, maps=None):
        """Unpack MSB map data files from a `MapStudio` directory into one single modifiable structure.

        If `MAPS` is defined by a child class or `maps` is given, only `Map` instances that appear in that sequence
        will be loaded (and missing ones will raise an error).

        Note that you only need to reload the map (e.g. by saving and quitting, or getting sufficiently far away from
        the map) to see changes in these files while playing the game. You do NOT need to fully restart the game, unlike
        with text and parameter/lighting changes.

        Args:
            map_studio_directory: Directory where all the MSB files are stored. This will be inside 'map/MapStudio' in
                your game directory (either version). (Ignore the 'MapStudioNew' folder next to this directory in DSR,
                which does nothing.)
        """
        self.directory = None
        self.msbs = {}  # type: dict[str, MSB]

        if map_studio_directory is None:
            return

        if maps is not None:
            self.ALL_MAPS = maps  # instance attribute to override class attribute

        map_studio_directory = Path(map_studio_directory)

        if not map_studio_directory.is_dir():
            raise ValueError(
                "`MapStudioDirectory` should be initialized with the `MapStudio` directory containing the MSB files."
            )

        self.directory = map_studio_directory

        if self.ALL_MAPS is not None:
            self._load_given_msbs()
        else:
            self._load_all_msbs()

    def _load_given_msbs(self):
        """Load requested maps."""
        for game_map in self.ALL_MAPS:
            if game_map.msb_file_stem is None:
                continue
            msb_path = self.directory / (game_map.msb_file_stem + ".msb")
            if self.IS_DCX:
                msb_path = msb_path.with_suffix(msb_path.suffix + ".dcx")
            try:
                self.msbs[game_map.msb_file_stem] = self.MSB_CLASS(msb_path)
                setattr(self, game_map.name, self.msbs[game_map.msb_file_stem])
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not find MSB file {repr(game_map.msb_file_stem)} ({game_map.name}) in given directory."
                )

    def _load_all_msbs(self):
        """Load all MSB files in directory, with keys/attribute names matching the MSB stem."""
        for msb_path in self.directory.glob("*.msb" + (".dcx" if self.IS_DCX else "")):
            self.msbs[msb_path.stem] = self.MSB_CLASS(msb_path)
            setattr(self, msb_path.stem, self.msbs[msb_path.stem])

    def __getitem__(self, map_source: tp.Union[str, tuple]):
        """Look up the MSB corresponding to `map_source` specifier. See `get_map()`."""
        game_map = self.GET_MAP(map_source)
        return self.msbs[game_map.msb_file_stem]

    def __iter__(self):
        return iter(self.msbs)

    def items(self):
        return self.msbs.items()

    def write(self, msb_directory=None):
        msb_directory = self.directory if msb_directory is None else Path(msb_directory)
        for msb in self.msbs.values():
            msb_path = msb_directory / msb.path.name
            try:
                msb.write(msb_path)
            except Exception as e:
                _LOGGER.error(e, exc_info=True)
                raise MapError(f"Error encountered while writing MSB {msb_path.name}:\n\n{e}")
        _LOGGER.info("All map files (MSBs) in MapStudio directory written successfully.")

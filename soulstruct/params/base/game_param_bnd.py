from __future__ import annotations

import abc
import logging
import pickle
import typing as tp
from pathlib import Path

from soulstruct.params.base.paramdef import ParamDefBND
from soulstruct.bnd import BaseBND

if tp.TYPE_CHECKING:
    from soulstruct.games import Game
    from .param import Param


_LOGGER = logging.getLogger(__name__)


class GameParamBND(BaseBND, abc.ABC):

    Param: tp.Type[Param] = None
    GAME: Game = None
    ParamDefBND: tp.Type[ParamDefBND] = None

    PARAM_NICKNAMES = {}  # type: dict[str, str]

    def __init__(self, game_param_bnd_source=None, dcx_magic=(), paramdef_bnd=None):
        """Unpack a `GameParam.gameparambnd[.dcx]` file binder into a single modifiable structure.

        Args:
            game_param_bnd_source: any valid source for GameParam.parambnd[.dcx] (its file path, the directory
                containing it, the unpacked BND directory, or an existing BND instance).
            dcx_magic: optional DCX magic (sequence of two integers).
            paramdef_bnd: previously loaded `ParamDefBND` instance, or source to create it. Can also be automatically
                detected from subclass.
        """

        self._reload_warning_given = True
        self.params = {}
        if paramdef_bnd is None:
            self.paramdef_bnd = self.ParamDefBND()
        self.paramdef_bnd = paramdef_bnd if isinstance(paramdef_bnd, ParamDefBND) else self.ParamDefBND(paramdef_bnd)

        super().__init__(game_param_bnd_source, dcx_magic=dcx_magic)

        for entry in self.entries:
            p = self.params[entry.path] = self.Param(entry.data, self.paramdef_bnd)
            # Preferential nickname source order: `PARAM_NICKNAMES` attribute, `p.nickname`, `BNDEntry` path stem
            nickname = self.PARAM_NICKNAMES.get(entry.stem, entry.stem if p.nickname is None else p.nickname)
            setattr(self, nickname, p)

    def update_bnd_entries(self):
        """Update the `GameParamBND` by packing the current `Param` instances. Called automatically by `write()`."""
        for param_table_entry_path, param_table in self.params.items():
            self.entries_by_path[param_table_entry_path].data = param_table.pack()

    def write(self, file_path: tp.Union[None, str, Path] = None, make_dirs=True, **pack_kwargs):
        """Write the `GameParamBND` file after updating the binary BND entries from the loadewd `Param` instances.

        See `GameFile.write()` for more.
        """
        self.update_bnd_entries()
        super().write(file_path, make_dirs, **pack_kwargs)
        _LOGGER.info("GameParamBND written successfully.")
        if not self._reload_warning_given:
            _LOGGER.info("Remember to reload your game to see changes.")
            self._reload_warning_given = True

    def pickle(self, game_param_pickle_path=None):
        """Save the entire `GameParamBND` to a pickled file, which will be faster to load in future."""
        if game_param_pickle_path is None:
            game_param_pickle_path = self.path
            if game_param_pickle_path is None:
                raise ValueError("Could not automatically determine path to pickle `GameParamBND`.")
            while game_param_pickle_path.suffix in {".dcx", ".parambnd"}:
                game_param_pickle_path = game_param_pickle_path.with_name(game_param_pickle_path.stem)
            if game_param_pickle_path.suffix != ".pickle":
                game_param_pickle_path = game_param_pickle_path.with_suffix(f"{game_param_pickle_path.suffix}.pickle")
        with Path(game_param_pickle_path).open("wb") as f:
            pickle.dump(self, f)

    # TODO: Inherit from some abstract `ProjectData` class that provides this interface.
    def get_range(self, param_nickname, start, count):
        """Get a list of (id, entry) pairs from a certain range inside ID-sorted param dictionary."""
        return getattr(self, param_nickname).get_range(start, count)

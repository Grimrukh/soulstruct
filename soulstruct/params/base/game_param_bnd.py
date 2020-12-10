import logging
import pickle
from pathlib import Path

from soulstruct.bnd import BaseBND, BND
from soulstruct.params.paramdef import ParamDefBND
from soulstruct.params.utilities import GET_BUNDLED_PARAMDEFBND

from .param import Param


_LOGGER = logging.getLogger(__name__)


class GameParamBND:

    Param = Param
    PARAM_NICKNAMES = {}

    def __init__(self, game_param_bnd_source=None, paramdef_bnd=None):
        """Unpack a `GameParam.gameparambnd[.dcx]` file binder into a single modifiable structure.

        Args:
            game_param_bnd_source: any valid source for GameParam.parambnd[.dcx] (its file path, the directory
                containing it, the unpacked BND directory, or an existing BND instance). It will default to the
                DEFAULT_GAME package. The appropriate bundled ParamDef will be loaded automatically, detected based on
                the DCX compression of the BND.
        """
        self._reload_warning_given = True
        self._data = {}

        if game_param_bnd_source is None:
            self._bnd = None
            self.paramdef_bnd = None
            return
        if paramdef_bnd is None:
            raise ValueError("`paramdef_bnd` must be passed to `GameParamBND`. It can also be 'dsr', 'ptde', or 'bb'.")

        if isinstance(game_param_bnd_source, BaseBND):
            self._bnd = game_param_bnd_source
        else:
            if isinstance(game_param_bnd_source, (str, Path)):
                game_param_bnd_source = Path(game_param_bnd_source)
                if game_param_bnd_source.is_dir():
                    if (game_param_bnd_source / "GameParam.parambnd").is_file():
                        game_param_bnd_source = game_param_bnd_source / "GameParam.parambnd"
                    elif (game_param_bnd_source / "GameParam.parambnd.dcx").is_file():
                        game_param_bnd_source = game_param_bnd_source / "GameParam.parambnd.dcx"
            try:
                self._bnd = BND(game_param_bnd_source)
            except TypeError:
                raise TypeError("Could not load GameParamBND from given source.")
        if isinstance(paramdef_bnd, str):
            self.paramdef_bnd = GET_BUNDLED_PARAMDEFBND(paramdef_bnd)
        elif isinstance(paramdef_bnd, ParamDefBND):
            self.paramdef_bnd = paramdef_bnd
        else:
            raise TypeError(f"`paramdef_bnd` must be a `ParamDefBND` instance or a game name: 'dsr', 'ptde', 'bb'")

        for entry in self._bnd:
            p = self._data[entry.path] = self.Param(entry.data, self.paramdef_bnd)
            # Preferential nickname source order: `_PARAM_NICKNAMES` attribute, `p.nickname`, `BNDEntry` path stem
            nickname = self.PARAM_NICKNAMES.get(entry.stem, entry.stem if p.nickname is None else p.nickname)
            setattr(self, nickname, p)

    def update_bnd(self):
        """Update the internal BND by packing the current ParamTables. Called automatically by `save()`."""
        for param_table_entry_path, param_table in self._data.items():
            self._bnd.entries_by_path[param_table_entry_path].data = param_table.pack()

    def save(self, game_param_bnd_path=None, auto_pickle=False):
        """Save the `GameParamBND`. If no path is given, it will attempt to save to the same BND file."""
        self.update_bnd()
        if auto_pickle:
            self.pickle()
        if game_param_bnd_path is not None and Path(game_param_bnd_path).is_dir():
            game_param_bnd_path = Path(game_param_bnd_path) / "GameParam.parambnd"  # dcx remembered by `self._bnd`
        self._bnd.write(game_param_bnd_path)
        _LOGGER.info("GameParamBND written successfully.")
        if not self._reload_warning_given:
            _LOGGER.info("Remember to reload your game to see changes.")
            self._reload_warning_given = True

    def pickle(self, game_param_pickle_path=None):
        """Save the entire `GameParamBND` to a pickled file, which will be faster to load in future."""
        if game_param_pickle_path is None:
            game_param_pickle_path = self._bnd.bnd_path
            if game_param_pickle_path is None:
                raise ValueError("Could not automatically determine path to pickle GameParamBND.")
            while game_param_pickle_path.suffix in {".dcx", ".parambnd"}:
                game_param_pickle_path = game_param_pickle_path.parent / game_param_pickle_path.stem
            if not game_param_pickle_path.suffix != ".pickle":
                game_param_pickle_path = game_param_pickle_path.with_suffix(f"{game_param_pickle_path.suffix}.pickle")
        with Path(game_param_pickle_path).open("wb") as f:
            pickle.dump(self, f)

    def __getitem__(self, param_nickname) -> Param:
        return getattr(self, param_nickname)

    def get_range(self, category, start, count):
        """Get a list of (id, entry) pairs from a certain range inside ID-sorted param dictionary."""
        return self[category].get_range(start, count)

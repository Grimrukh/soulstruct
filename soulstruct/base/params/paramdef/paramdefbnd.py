from __future__ import annotations

__all__ = ["ParamDefBND"]

import abc
import logging
import re
import typing as tp
from dataclasses import field

from soulstruct.containers import Binder
from soulstruct.games import Game, get_game

from .core import ParamDef

_LOGGER = logging.getLogger("soulstruct")

_PARAMDEF_RE = re.compile(r".*\.paramdef")


class ParamDefBND(Binder, abc.ABC):
    """BND container with all the `ParamDef` definitions for a given game.

    The latest versions of these files are included with Soulstruct for some games, and can be loaded simply by
    passing the game name to this constructor. They will also be loaded automatically when needed by `Param`
    instances.

    If you want to modify a `ParamDefBND`, you are far too powerful a modder for Soulstruct, and I cannot make that
    journey with you at this time.
    """

    IS_SPLIT_BXF: tp.ClassVar[bool] = False

    _BUNDLED: tp.ClassVar[dict[Game, ParamDefBND]] = {}

    PARAMDEF_CLASS: tp.ClassVar[type[ParamDef]] = None

    paramdefs: dict[str, ParamDef] = field(default_factory=dict)

    def __post_init__(self):
        if self.paramdefs:
            return

        # Load from binary Binder source.
        for entry in self.entries:
            if not _PARAMDEF_RE.match(entry.name):
                _LOGGER.warning(f"Ignoring unknown entry '{entry.name}' in ParamDefBND Binder.")
                continue
            try:
                paramdef = entry.to_binary_file(self.PARAMDEF_CLASS)
            except Exception as ex:
                _LOGGER.error(f"Could not load ParamDef from entry '{entry.name}'. Error: {ex}")
                raise
            if paramdef.param_type in self.paramdefs:
                _LOGGER.warning(
                    f"ParamDef type {paramdef.param_type} was loaded more than once in ParamDefBND. "
                    f"Only first will be used."
                )
            else:
                self.paramdefs[paramdef.param_type] = paramdef

    @classmethod
    def from_bundled(cls, game_or_name: Game | str) -> tp.Self:
        game = get_game(game_or_name)
        if game in cls._BUNDLED:
            return cls._BUNDLED[game]
        if "PARAMDEFBND" not in game.bundled_resource_paths.items():
            raise FileNotFoundError(f"No bundled PARAMDEFBND found for {game.name}.")
        try:
            paramdefbnd = cls.from_path(game.bundled_resource_paths["PARAMDEF"])
        except Exception as ex:
            raise FileNotFoundError(f"Could not load bundled PARAMDEFBND for {game.name}.") from ex
        cls._BUNDLED[game] = paramdefbnd
        return paramdefbnd

    def __getitem__(self, param_type) -> ParamDef:
        try:
            return self.paramdefs[param_type]
        except KeyError:
            raise KeyError(f"No ParamDef with type {param_type}. The available types are:\n    {list(self.paramdefs)}")

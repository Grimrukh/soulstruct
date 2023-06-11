from __future__ import annotations

__all__ = ["ParamDefBND"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field

from soulstruct.containers import Binder
from soulstruct.utilities.files import PACKAGE_PATH
from soulstruct.games import Game, get_game

from .core import ParamDef

try:
    Self = tp.Self
except AttributeError:
    Self = "ParamDefBND"

_LOGGER = logging.getLogger(__name__)

_PARAMDEF_RE = re.compile(r".*\.paramdef")


@dataclass(slots=True)
class ParamDefBND(Binder, abc.ABC):
    """BND container with all the `ParamDef` definitions for a given game.

    The latest versions of these files are included with Soulstruct for some games, and can be loaded simply by
    passing the game name to this constructor. They will also be loaded automatically when needed by `Param`
    instances.

    If you want to modify a `ParamDefBND`, you are far too powerful a modder for Soulstruct, and I cannot make that
    journey with you at this time.
    """
    PARAMDEF_CLASS: tp.ClassVar[tp.Type[ParamDef]] = None

    paramdefs: dict[str, ParamDef] = field(default_factory=dict)

    def __post_init__(self):
        super(Binder, self).__post_init__()
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
    def from_bundled(cls, game: Game | str = None) -> Self:
        """Load vanilla ParamDefBND bundled with Soulstruct (easiest)."""
        if game is None:
            game = cls.get_game()
        elif isinstance(game, str):
            game = get_game(game)

        if not game.bundled_paramdef_path:
            raise NotImplementedError(
                f"Soulstruct does not have a bundled `paramdefbnd` file for game {game.name}."
            )
        paramdefbnd_path = PACKAGE_PATH(game.bundled_paramdef_path)
        if not paramdefbnd_path.is_file():
            raise FileNotFoundError(
                f"Could not find bundled `paramdefbnd` file for game {game.name} in Soulstruct.\n"
                "Update/reinstall Soulstruct or copy the ParamDef files in yourself."
            )

        return cls.from_path(paramdefbnd_path)

    def __getitem__(self, param_type) -> ParamDef:
        try:
            return self.paramdefs[param_type]
        except KeyError:
            raise KeyError(
                f"No ParamDef with type {param_type}. The available types are:\n    {list(self.paramdefs)}")

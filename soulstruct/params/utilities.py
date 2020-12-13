__all__ = ["GET_BUNDLED_PARAMDEFBND"]

from soulstruct.games import get_game
from soulstruct.params.paramdef import ParamDefBND


_LOADED_PARAMDEFS = {}


def GET_BUNDLED_PARAMDEFBND(game):
    game = get_game(game)
    if game.bundled_paramdef_path:
        return _LOADED_PARAMDEFS.setdefault(game.name, ParamDefBND(game))
    raise ValueError(f"Could not find bundled ParamDef in Soulstruct for {repr(game)}.")

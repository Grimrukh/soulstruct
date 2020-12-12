__all__ = ["GET_BUNDLED_PARAMDEFBND"]

from soulstruct.games import get_game
from soulstruct.params.paramdef import ParamDefBND


_PARAMDEF_BND_PTDE = None
_PARAMDEF_BND_DSR = None
_PARAMDEF_BND_BB = None


def GET_BUNDLED_PARAMDEFBND(game):
    global _PARAMDEF_BND_PTDE, _PARAMDEF_BND_DSR, _PARAMDEF_BND_BB
    game = get_game(game)
    if game.lower() == "ptde":
        if _PARAMDEF_BND_PTDE is None:
            _PARAMDEF_BND_PTDE = ParamDefBND("ptde")
        return _PARAMDEF_BND_PTDE
    elif game.lower() == "dsr":
        if _PARAMDEF_BND_DSR is None:
            _PARAMDEF_BND_DSR = ParamDefBND("dsr")
        return _PARAMDEF_BND_DSR
    elif game.lower() == "bb":
        if _PARAMDEF_BND_BB is None:
            _PARAMDEF_BND_BB = ParamDefBND("bb")
        return _PARAMDEF_BND_BB
    raise ValueError(f"Could not find bundled ParamDef in Soulstruct for game {repr(game)}.")

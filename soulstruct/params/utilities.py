__all__ = ["GET_BUNDLED_PARAMDEFBND"]

from soulstruct.params.paramdef import ParamDefBND


_PARAMDEF_BND_PTDE = None
_PARAMDEF_BND_DSR = None
_PARAMDEF_BND_BB = None


def GET_BUNDLED_PARAMDEFBND(game_name):
    global _PARAMDEF_BND_PTDE, _PARAMDEF_BND_DSR, _PARAMDEF_BND_BB
    if game_name.lower() == "ptde":
        if _PARAMDEF_BND_PTDE is None:
            _PARAMDEF_BND_PTDE = ParamDefBND("ptde")
        return _PARAMDEF_BND_PTDE
    elif game_name.lower() == "dsr":
        if _PARAMDEF_BND_DSR is None:
            _PARAMDEF_BND_DSR = ParamDefBND("dsr")
        return _PARAMDEF_BND_DSR
    elif game_name.lower() == "bb":
        if _PARAMDEF_BND_BB is None:
            _PARAMDEF_BND_BB = ParamDefBND("bb")
        return _PARAMDEF_BND_BB
    raise ValueError(f"Could not find bundled ParamDef in Soulstruct for game {repr(game_name)}.")

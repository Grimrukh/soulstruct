from soulstruct.exceptions import SoulstructError


class LuaError(SoulstructError):
    pass


class LuaCompileError(LuaError):
    pass


class LuaDecompileError(LuaError):
    pass
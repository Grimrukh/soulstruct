
__all__ = [
    "EMEVDObject",
    "Flag",
    "FlagRange",
    "FlagInt",
    "FlagRangeTyping",
]

import typing as tp

from soulstruct.base.events.emevd.emevd_types import (
    BaseEMEVDObject,
    Flag as _BaseFlag,
    FlagRange as _BaseFlagRange,
)


class EMEVDObject(BaseEMEVDObject):

    @classmethod
    def get_enum(cls, enum_cls_name: str, enum_member_name: str):
        from ..events.emevd import enums
        enum_type = getattr(enums, enum_cls_name)
        return getattr(enum_type, enum_member_name)

    @classmethod
    def compile_instruction(cls, instr_name: str, *args, **kwargs) -> list[str]:
        from ..events.emevd.compiler import compile_instruction
        return compile_instruction(instr_name, *args, **kwargs)

    @classmethod
    def get_compile_func(cls, instr_name: str):
        from ..events.emevd.compiler import get_compile_func
        return get_compile_func(instr_name)


class Flag(EMEVDObject, _BaseFlag):
    pass


class FlagRange(EMEVDObject, _BaseFlagRange):
    pass


FlagInt = tp.Union[Flag, int]
FlagRangeTyping = tp.Union[FlagRange, tuple, list]

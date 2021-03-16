__all__ = ["ParamFlags1", "ParamFlags2"]

from soulstruct.utilities.core import Flags8


class ParamFlags1(Flags8):
    @property
    def IntDataOffset(self):
        return self.flags[1]

    @property
    def LongDataOffset(self):
        return self.flags[2]

    @property
    def OffsetParam(self):
        return self.flags[7]


class ParamFlags2(Flags8):
    @property
    def UnicodeRowNames(self):
        return self.flags[0]

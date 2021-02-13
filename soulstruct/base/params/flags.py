__all__ = ["ParamFlags1", "ParamFlags2"]

import abc


class ParamFlagsBase(abc.ABC):
    def __init__(self, byte):
        self.flags = [bool(2 ** i & byte) for i in range(8)]

    def __getitem__(self, i):
        return self.flags[i]

    def pack(self) -> int:
        return sum(2 ** i if enabled else 0 for i, enabled in enumerate(self.flags))

    def __repr__(self):
        return repr(self.flags)


class ParamFlags1(ParamFlagsBase):
    @property
    def IntDataOffset(self):
        return self.flags[1]

    @property
    def LongDataOffset(self):
        return self.flags[2]

    @property
    def OffsetParam(self):
        return self.flags[7]


class ParamFlags2(ParamFlagsBase):
    @property
    def UnicodeRowNames(self):
        return self.flags[0]

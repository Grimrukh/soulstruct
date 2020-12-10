class ParamFlags1:
    def __init__(self, byte):
        self.flags = [bool(2 ** i & byte) for i in range(8)]

    def __getitem__(self, i):
        return self.flags[i]

    @property
    def IntDataOffset(self):
        return self.flags[1]

    @property
    def LongDataOffset(self):
        return self.flags[2]

    @property
    def OffsetParam(self):
        return self.flags[7]

    def pack(self):
        return sum(2 ** i if enabled else 0 for i, enabled in enumerate(self.flags))

    def __repr__(self):
        return repr(self.flags)


class ParamFlags2:
    def __init__(self, byte):
        self.flags = [bool(2 ** i & byte) for i in range(8)]

    def __getitem__(self, i):
        return self.flags[i]

    @property
    def UnicodeRowNames(self):
        return self.flags[0]

    def pack(self):
        return sum(2 ** i if enabled else 0 for i, enabled in enumerate(self.flags))

    def __repr__(self):
        return repr(self.flags)
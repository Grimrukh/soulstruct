from enum import IntEnum


class _UnsignedBase(IntEnum):
    @staticmethod
    def size():
        raise NotImplementedError

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        raise NotImplementedError

    @staticmethod
    def python_type():
        return int

    @staticmethod
    def minimum():
        return 0

    @classmethod
    def maximum(cls):
        return 2 ** cls.bit_size() - 1


class _SignedBase(IntEnum):
    @staticmethod
    def size():
        raise NotImplementedError

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        raise NotImplementedError

    @staticmethod
    def python_type():
        return int

    @classmethod
    def minimum(cls):
        return -2 ** (cls.bit_size() - 1)

    @classmethod
    def maximum(cls):
        return 2 ** (cls.bit_size() - 1) - 1


class UnsignedChar(_UnsignedBase):
    @staticmethod
    def size():
        return 1

    @staticmethod
    def format():
        return '<B'


class SignedChar(_SignedBase):
    @staticmethod
    def size():
        return 1

    @staticmethod
    def format():
        return '<b'


class UnsignedShort(_UnsignedBase):
    @staticmethod
    def size():
        return 2

    @staticmethod
    def format():
        return '<H'


class SignedShort(_SignedBase):
    @staticmethod
    def size():
        return 2

    @staticmethod
    def format():
        return '<h'


class UnsignedInt(_UnsignedBase):
    @staticmethod
    def size():
        return 4

    @staticmethod
    def format():
        return '<I'


class SignedInt(_SignedBase):
    @staticmethod
    def size():
        return 4

    @staticmethod
    def format():
        return '<i'


class Single(object):
    @staticmethod
    def size():
        return 4

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        return '<f'

    @staticmethod
    def python_type():
        return float

    @staticmethod
    def minimum():
        return -float('inf')

    @staticmethod
    def maximum():
        return float('inf')


class Double(object):
    @staticmethod
    def size():
        return 8

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        return '<d'

    @staticmethod
    def python_type():
        return float

    @staticmethod
    def minimum():
        return -float('inf')

    @staticmethod
    def maximum():
        return float('inf')


u8 = UnsignedChar
s8 = SignedChar
u16 = UnsignedShort
s16 = SignedShort
u32 = UnsignedInt
s32 = SignedInt
f32 = Single
f64 = Double

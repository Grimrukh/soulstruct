from enum import IntEnum


class ATKPARAM_ATKATTR_TYPE(IntEnum):
    NoType = 0  # test only
    Blast = 1  # e.g. Iron Golem axe
    Sharp = 3  # e.g. arrows and throwing knives
    Other = 4  # e.g. most bullets


class ATKPARAM_SPATTR_TYPE(IntEnum):
    NoType = 0
    Physical = 1
    Fire = 2
    Magic = 3
    Poison = 4
    # 5 is not used.
    Lightning = 6
    # 7 is not used.
    Crystal = 8

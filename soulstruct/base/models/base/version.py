__all__ = ["FLVERVersion"]

from enum import IntEnum


class FLVERVersion(IntEnum):
    Null = 0x0

    # Old `FLVER0` format:
    DemonsSouls_B = 0x00014  # e.g. c7080
    DemonsSouls = 0x00015

    # Modern `FLVER` format:
    DarkSouls2_Armor9320 = 0x20009
    DarkSouls_PS3_o0700_o0701 = 0x2000B
    DarkSouls_A = 0x2000C
    DarkSouls_B = 0x2000D
    DarkSouls2_NT = 0x2000F
    DarkSouls2 = 0x20010  # includes SOTFS
    Bloodborne_DS3_A = 0x20013
    Bloodborne_DS3_B = 0x20014
    Sekiro_TestChr = 0x20016
    Sekiro_EldenRing = 0x2001A
    # TODO: AC6?

    @classmethod
    def default(cls):
        return cls.Null

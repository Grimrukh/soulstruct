__all__ = ["FLVERVersion"]

from enum import IntEnum


class FLVERVersion(IntEnum):
    Null = 0x0

    # Old `FLVER0` versions:
    DemonsSouls_0x0F = 0x0000F  # e.g. o9993
    DemonsSouls_0x10 = 0x00010  # e.g. c1200
    DemonsSouls_0x14 = 0x00014  # e.g. c7080, 'm07' map pieces
    DemonsSouls = 0x00015  # standard Demon's Souls version

    # NOTE: For whatever reason, there are no `FLVER1` versions in [0x10000, 0x1FFFF] range.

    # Modern `FLVER` versions:
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
    ArmoredCore6 = 0x2001B

    @classmethod
    def default(cls):
        return cls.Null

    def is_flver0(self):
        return self.value <= 0x0FFFF

    def map_pieces_use_normal_w_bones(self):
        """From Bloodborne onwards, Map Piece FLVER vertices store their singular bone indices in the fourth 8-bit
        component of the 'normal_w' vertex array, rather than having a full useless four-bone `bone_indices` field like
        real rigged FLVERs.
        TODO: Possibly from DS2 onwards?
        """
        return self.value >= self.Bloodborne_DS3_A

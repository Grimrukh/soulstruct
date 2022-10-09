from soulstruct.darksouls1r.game_types import *


class Objects(Object):

    # noinspection PyMethodParameters
    def _generate_next_value_(name, start, count, last_values):
        return Object.auto_generate(count, 1000000)

    o0100_0000 = 1001900
    o0100_0001 = 1001901
    o0100_0002 = 1001902
    o0100_0003 = 1001903
    o0100_0004 = 1001904
    o0100_0005 = 1001905
    o0100_0006 = 1001906
    o0100_0007 = 1001907
    o0200_0000 = 1001960  # Bonfire
    o1401_0000 = 1001994  # Entrance fog
    o1402_0000 = 1001996  # Blighttown fog


class VFXEvents(VFXEvent):
    o1401_0000 = 1001995
    o1402_0000 = 1001997


class SoundEvents(SoundEvent):
    BossMusic = 1003800


class ObjActs(ObjActEvent):
    ObjAct_1315_ShortcutDoor = 11000120

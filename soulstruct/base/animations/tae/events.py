from __future__ import annotations

__all__ = [
    "TAEEventData",

    "JumpTable",
    "Unk001",
    "Unk002",
    "Unk005",
    "Unk016",
    "Unk017",
    "Unk024",
    "SwitchWeapon1",
    "SwitchWeapon2",
    "Unk034",
    "Unk035",
    "Unk064",
    "Unk065",
    "CreateSpEffect1",
    "CreateSpEffect2",
    "PlayFFX",
    "Unk110",
    "HitEffect",
    "Unk113",
    "Unk114",
    "Unk115",
    "Unk116",
    "Unk117",
    "Unk118",
    "Unk119",
    "Unk120",
    "Unk121",
    "PlaySound1",
    "PlaySound2",
    "PlaySound3",
    "PlaySound4",
    "PlaySound5",
    "Unk137",
    "CreateDecal",
    "Unk144",
    "Unk145",
    "Unk150",
    "Unk151",
    "Unk161",
    "FadeOut",
    "Unk194",
    "Unk224",
    "DisableStaminaRegen",
    "Unk226",
    "Unk227",
    "RagdollReviveTime",
    "Unk229",
    "SetEventMessageID",
    "Unk232",
    "ChangeDrawMask",
    "RollDistanceReduction",
    "CreateAISound",
    "Unk300",
    "Unk301",
    "AddSpEffectDragonForm",
    "PlayAnimation",
    "BehaviorThing",
    "CreateBehaviorPC",
    "Unk308",
    "Unk310",
    "Unk311",
    "Unk312",
    "Unk320",
    "Unk330",
    "EffectDuringThrow",
    "Unk332",
    "CreateSpEffect",
    "Unk500",
    "Unk510",
    "Unk520",
    "KingOfTheStorm",
    "Unk600",
    "Unk601",
    "DebugAnimSpeed",
    "Unk605",
    "Unk606",
    "Unk700",
    "EnableTurningDirection",
    "FacingAngleCorrection",
    "Unk707",
    "HideWeapon",
    "HideModelMask",
    "DamageLevelModule",
    "ModelMask",
    "DamageLevelFunction",
    "Unk715",
    "CultStart",
    "Unk730",
    "Unk740",
    "IFrameState",
    "BonePos",
    "BoneFixOn1",
    "BoneFixOn2",
    "TurnLowerBody",
    "Unk782",
    "SpawnBulletByCultSacrifice1",
    "Unk786",
    "Unk790",
    "Unk791",
    "HitEffect2",
    "CultSacrifice1",
    "SacrificeEmpty",
    "Toughness",
    "BringCultMenu",
    "CeremonyParamID",
    "CultSingle",
    "CultEmpty2",
    "Unk800",
]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.binary import *

from .enums import TAEEventType


@dataclass(slots=True)
class TAEEventData(BinaryStruct):
    """I prefer to attach the various data types to `TAEEvent` rather than subclassing it, all as direct structs."""
    event_type: tp.ClassVar[TAEEventType]


@dataclass(slots=True)
class JumpTable(TAEEventData):
    """General-purpose event that calls different functions based on the first field."""
    event_type = TAEEventType.JumpTable  # 000

    jump_table_id: int32
    unk_x04: int32
    unk_x08: int32  # used for jump table ID 3
    unk_x0c: int16
    unk_x0e: int16


@dataclass(slots=True)
class Unk001(TAEEventData):
    event_type = TAEEventType.Unk001  # 001

    unk_x00: int32
    unk_x04: int32
    condition: int32
    unk_x0c: byte
    unk_x0d: byte
    state_info: int16


@dataclass(slots=True)
class Unk002(TAEEventData):
    event_type = TAEEventType.Unk002  # 002

    unk_x00: int32
    unk_x04: int32
    chr_asm_style: int32
    unk_x0c: byte
    unk_x0d: byte
    unk_x0e: ushort
    unk_x10: ushort
    _pad: bytes = field(**BinaryPad(6))


@dataclass(slots=True)
class Unk005(TAEEventData):
    event_type = TAEEventType.Unk005  # 005

    unk_x00: int32
    unk_x04: int32


@dataclass(slots=True)
class Unk016(TAEEventData):
    event_type = TAEEventType.Unk016  # 016


@dataclass(slots=True)
class Unk017(TAEEventData):
    event_type = TAEEventType.Unk017  # 017

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class Unk024(TAEEventData):
    event_type = TAEEventType.Unk024  # 024

    unk_x00: int32
    unk_x04: int32
    unk_x08: int32
    unk_x0c: int32


@dataclass(slots=True)
class SwitchWeapon1(TAEEventData):
    event_type = TAEEventType.SwitchWeapon1  # 032

    switch_state: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class SwitchWeapon2(TAEEventData):
    event_type = TAEEventType.SwitchWeapon2  # 033

    switch_state: int32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk034(TAEEventData):
    event_type = TAEEventType.Unk034  # 034

    state: int32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk035(TAEEventData):
    event_type = TAEEventType.Unk035  # 035

    state: int32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk064(TAEEventData):
    event_type = TAEEventType.Unk064  # 064

    unk_x00: int32
    unk_x04: ushort
    unk_x06: ushort
    unk_x08: byte
    unk_x09: byte
    unk_x0a: byte
    unk_x0b: byte
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk065(TAEEventData):
    event_type = TAEEventType.Unk065  # 065

    unk_x00: int32
    unk_x04: byte
    unk_x05: byte
    unk_x06: ushort
    unk_x08: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class CreateSpEffect1(TAEEventData):
    """During attack."""
    event_type = TAEEventType.CreateSpEffect1  # 066

    speffect_id: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class CreateSpEffect2(TAEEventData):
    """During roll."""
    event_type = TAEEventType.CreateSpEffect2  # 067

    speffect_id: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class PlayFFX(TAEEventData):
    event_type = TAEEventType.PlayFFX  # 096

    ffx_id: int32
    unk_x04: int32
    unk_x08: int32
    state_0: sbyte
    state_1: sbyte
    ghost_ffx_condition: sbyte
    unk_x0f: byte


@dataclass(slots=True)
class Unk110(TAEEventData):
    event_type = TAEEventType.Unk110  # 110

    id: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class HitEffect(TAEEventData):
    event_type = TAEEventType.HitEffect  # 112

    size: int32
    unk_x04: int32
    unk_x08: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk113(TAEEventData):
    event_type = TAEEventType.Unk113  # 113

    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class Unk114(TAEEventData):
    event_type = TAEEventType.Unk114  # 114

    unk_x00: int32
    unk_x04: ushort
    unk_x06: ushort
    unk_x08: int32
    unk_x0c: byte
    unk_x0d: sbyte
    unk_x0e: sbyte
    unk_x0f: byte
    unk_x10: byte
    unk_x11: byte
    unk_x12: int16
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk115(TAEEventData):
    event_type = TAEEventType.Unk115  # 115

    unk_x00: int32
    unk_x04: ushort
    unk_x06: ushort
    unk_x08: int32
    unk_x0c: byte
    unk_x0d: byte
    unk_x0e: byte
    unk_x0f: byte
    unk_x10: byte
    unk_x11: byte
    unk_x12: int16
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk116(TAEEventData):
    event_type = TAEEventType.Unk116  # 116

    unk_x00: int32
    unk_x04: int32
    unk_x08: int32
    unk_x0c: int32


@dataclass(slots=True)
class Unk117(TAEEventData):
    event_type = TAEEventType.Unk117  # 117

    unk_x00: int32
    unk_x04: int32
    unk_x08: int32  # -1
    unk_x0c: byte
    unk_x0d: byte
    unk_x0e: byte
    unk_x0f: byte


@dataclass(slots=True)
class Unk118(TAEEventData):
    event_type = TAEEventType.Unk118  # 118

    unk_x00: int32
    unk_x04: ushort
    unk_x06: ushort
    unk_x08: ushort
    unk_x0a: ushort
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk119(TAEEventData):
    event_type = TAEEventType.Unk119  # 119

    unk_x00: int32
    unk_x04: int32
    unk_x08: int32
    unk_x0c: byte  # 0
    _pad: bytes = field(**BinaryPad(3))


@dataclass(slots=True)
class Unk120(TAEEventData):
    event_type = TAEEventType.Unk120  # 120

    chr_type: int32
    ffx_ids: list[int32] = field(**BinaryArray(8))
    unk_x30: int32
    unk_x34: int32
    unk_x38: byte
    _pad: bytes = field(**BinaryPad(7))


@dataclass(slots=True)
class Unk121(TAEEventData):
    event_type = TAEEventType.Unk121  # 121

    unk_x00: int32
    unk_x04: ushort
    unk_x06: byte
    unk_x07: byte
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class PlaySound1(TAEEventData):
    event_type = TAEEventType.PlaySound1  # 128

    sound_type: int32
    sound_id: int32
    # After event version 0x10?
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class PlaySound2(TAEEventData):
    event_type = TAEEventType.PlaySound2  # 129

    sound_type: int32
    sound_id: int32
    unk_x08: int32
    unk_x0c: int32
    # After event version 0x15?
    unk_x10: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class PlaySound3(TAEEventData):
    event_type = TAEEventType.PlaySound3  # 130

    sound_type: int32
    sound_id: int32
    unk_x08: float
    unk_x0c: float  # int -1
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class PlaySound4(TAEEventData):
    event_type = TAEEventType.PlaySound4  # 131

    sound_type: int32
    sound_id: int32
    unk_x08: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class PlaySound5(TAEEventData):
    event_type = TAEEventType.PlaySound5  # 132

    sound_type: int32
    sound_id: int32
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class Unk137(TAEEventData):
    event_type = TAEEventType.Unk137  # 137

    unk_x00: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class CreateDecal(TAEEventData):
    event_type = TAEEventType.CreateDecal  # 138

    decal_param_id: int32
    unk_x04: int32
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class Unk144(TAEEventData):
    event_type = TAEEventType.Unk144  # 144

    unk_x00: ushort
    unk_x02: ushort
    unk_x04: float
    unk_x08: float
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk145(TAEEventData):
    event_type = TAEEventType.Unk145  # 145

    unk_x00: int16
    condition: int16
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk150(TAEEventData):
    event_type = TAEEventType.Unk150  # 150

    unk_x00: int32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk151(TAEEventData):
    event_type = TAEEventType.Unk151  # 151

    dummy_point_id: int32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk161(TAEEventData):
    event_type = TAEEventType.Unk161  # 161

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class FadeOut(TAEEventData):
    event_type = TAEEventType.FadeOut  # 193

    ghost_val_1: float
    ghost_val_2: float


@dataclass(slots=True)
class Unk194(TAEEventData):
    event_type = TAEEventType.Unk194  # 194

    unk_x00: ushort
    unk_x02: ushort
    unk_x04: ushort
    unk_x06: ushort
    unk_x08: float
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk224(TAEEventData):
    event_type = TAEEventType.Unk224  # 224

    unk_x00: float
    unk_x04: int32


@dataclass(slots=True)
class DisableStaminaRegen(TAEEventData):
    event_type = TAEEventType.DisableStaminaRegen  # 225

    # "0x64 - Enables Regen Back" -Pav

    state: byte
    _pad: bytes = field(**BinaryPad(7))


@dataclass(slots=True)
class Unk226(TAEEventData):
    event_type = TAEEventType.Unk226  # 226

    # "x/100 Coefficient" -Pav

    state: byte
    _pad: bytes = field(**BinaryPad(7))


@dataclass(slots=True)
class Unk227(TAEEventData):
    event_type = TAEEventType.Unk227  # 227

    mask: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class RagdollReviveTime(TAEEventData):
    event_type = TAEEventType.RagdollReviveTime  # 228

    unk_x00: float
    revive_timer: float
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class Unk229(TAEEventData):
    event_type = TAEEventType.Unk229  # 229

    unk_x00: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class SetEventMessageID(TAEEventData):
    event_type = TAEEventType.SetEventMessageID  # 231

    event_message_id: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk232(TAEEventData):
    event_type = TAEEventType.Unk232  # 232

    unk_x00: byte
    unk_x01: byte
    unk_x02: byte
    unk_x03: byte
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class ChangeDrawMask(TAEEventData):
    event_type = TAEEventType.ChangeDrawMask  # 233

    draw_mask: list[byte] = field(**BinaryArray(32))


@dataclass(slots=True)
class RollDistanceReduction(TAEEventData):
    event_type = TAEEventType.RollDistanceReduction  # 236

    unk_x00: float
    unk_x04: float
    roll_type: bool
    _pad: bytes = field(**BinaryPad(7))


@dataclass(slots=True)
class CreateAISound(TAEEventData):
    event_type = TAEEventType.CreateAISound  # 237

    ai_sound_id: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk300(TAEEventData):
    event_type = TAEEventType.Unk300  # 300

    jump_table_id_1: int16
    jump_table_id_2: int16
    unk_x04: float
    unk_x08: float
    unk_x0c: int32


@dataclass(slots=True)
class Unk301(TAEEventData):
    event_type = TAEEventType.Unk301  # 301

    unk_x00: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class AddSpEffectDragonForm(TAEEventData):
    event_type = TAEEventType.AddSpEffectDragonForm  # 302

    speffect_id: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class PlayAnimation(TAEEventData):
    event_type = TAEEventType.PlayAnimation  # 303

    animation_id: int32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class BehaviorThing(TAEEventData):
    """"Behavior Thing?" -Pav"""
    event_type = TAEEventType.BehaviorThing  # 304

    unk_x00: ushort
    unk_x02: int16
    behavior_list_id: int32


@dataclass(slots=True)
class CreateBehaviorPC(TAEEventData):
    event_type = TAEEventType.CreateBehaviorPC  # 307

    unk_x00: int16
    unk_x02: int16
    condition: int32
    unk_x08: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk308(TAEEventData):
    event_type = TAEEventType.Unk308  # 308

    unk_x00: float
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk310(TAEEventData):
    """"Behavior?" -Pav"""
    event_type = TAEEventType.Unk310  # 310

    unk_x00: byte
    unk_x01: byte
    _pad: bytes = field(**BinaryPad(6))


@dataclass(slots=True)
class Unk311(TAEEventData):
    event_type = TAEEventType.Unk311  # 311

    unk_x00: byte
    unk_x01: byte
    unk_x02: byte
    _pad: bytes = field(**BinaryPad(13))


@dataclass(slots=True)
class Unk312(TAEEventData):
    event_type = TAEEventType.Unk312  # 312

    behavior_mask: list[byte] = field(**BinaryArray(32))


@dataclass(slots=True)
class Unk320(TAEEventData):
    event_type = TAEEventType.Unk320  # 320

    unk_x00: bool
    unk_x01: bool
    unk_x02: bool
    unk_x03: bool
    unk_x04: bool
    unk_x05: bool
    unk_x06: bool
    _pad: bytes = field(**BinaryPad(9))


@dataclass(slots=True)
class Unk330(TAEEventData):
    event_type = TAEEventType.Unk330  # 330

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class EffectDuringThrow(TAEEventData):
    event_type = TAEEventType.EffectDuringThrow  # 331

    speffect_id_1: int32
    speffect_id_2: int32
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class Unk332(TAEEventData):
    event_type = TAEEventType.Unk332  # 332

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class CreateSpEffect(TAEEventData):
    """"When Landing" -Pav"""
    event_type = TAEEventType.CreateSpEffect  # 401

    speffect_id: int32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk500(TAEEventData):
    event_type = TAEEventType.Unk500  # 500

    unk_x00: byte
    unk_x01: byte
    _pad: bytes = field(**BinaryPad(6))


@dataclass(slots=True)
class Unk510(TAEEventData):
    event_type = TAEEventType.Unk510  # 510

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class Unk520(TAEEventData):
    event_type = TAEEventType.Unk520  # 520

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class KingOfTheStorm(TAEEventData):
    event_type = TAEEventType.KingOfTheStorm  # 522

    unk_x00: float  # 0
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk600(TAEEventData):
    event_type = TAEEventType.Unk600  # 600

    mask: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk601(TAEEventData):
    event_type = TAEEventType.Unk601  # 601

    stay_anim_type: int32
    unk_x04: float
    unk_x08: float
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class DebugAnimSpeed(TAEEventData):
    """"TAE Debug Anim Speed" -Pav"""
    event_type = TAEEventType.DebugAnimSpeed  # 603

    anim_speed: uint32
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk605(TAEEventData):
    event_type = TAEEventType.Unk605  # 605

    unk_x00: bool
    unk_x01: byte
    unk_x02: byte
    unk_x03: byte
    unk_x04: int32
    unk_x08: float
    unk_x0c: float
    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class Unk606(TAEEventData):
    event_type = TAEEventType.Unk606  # 606

    unk_x00: byte  # 0
    _pad_0: bytes = field(**BinaryPad(3))
    unk_x04: byte
    _pad_1: bytes = field(**BinaryPad(1))
    unk_x06: byte
    _pad_2: bytes = field(**BinaryPad(9))


@dataclass(slots=True)
class Unk700(TAEEventData):
    event_type = TAEEventType.Unk700  # 700

    # 6 - head turn

    unk_x00: float
    unk_x04: float
    unk_x08: float
    unk_x0c: float
    unk_x10: int32
    unk_x14: sbyte
    _pad: bytes = field(**BinaryPad(3))
    unk_x18: float
    unk_x1c: float
    unk_x20: float
    unk_x24: float


@dataclass(slots=True)
class EnableTurningDirection(TAEEventData):
    event_type = TAEEventType.EnableTurningDirection  # 703

    state: byte
    _pad: bytes = field(**BinaryPad(15))


@dataclass(slots=True)
class FacingAngleCorrection(TAEEventData):
    event_type = TAEEventType.FacingAngleCorrection  # 705

    correction_rate: float
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class Unk707(TAEEventData):
    event_type = TAEEventType.Unk707  # 707

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class HideWeapon(TAEEventData):
    """Used for Follower's Javelin WA. "Ladder State" -Pav"""

    event_type = TAEEventType.HideWeapon  # 710

    unk_x00: byte
    unk_x01: byte
    unk_x02: byte
    unk_x03: byte
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class HideModelMask(TAEEventData):
    event_type = TAEEventType.HideModelMask  # 711

    mask: list[byte] = field(**BinaryArray(32))


@dataclass(slots=True)
class DamageLevelModule(TAEEventData):
    event_type = TAEEventType.DamageLevelModule  # 712

    mask: list[byte] = field(**BinaryArray(16))
    unk_x10: byte
    unk_x11: byte
    unk_x12: byte
    _pad: bytes = field(**BinaryPad(13))


@dataclass(slots=True)
class ModelMask(TAEEventData):
    event_type = TAEEventType.ModelMask  # 713

    mask: list[byte] = field(**BinaryArray(32))


@dataclass(slots=True)
class DamageLevelFunction(TAEEventData):
    event_type = TAEEventType.DamageLevelFunction  # 714

    unk_x00: byte
    _pad: bytes = field(**BinaryPad(7))


@dataclass(slots=True)
class Unk715(TAEEventData):
    event_type = TAEEventType.Unk715  # 715

    unk_x00: byte
    unk_x01: byte
    unk_x02: byte
    unk_x03: byte
    unk_x04: byte
    unk_x05: byte
    unk_x06: byte
    unk_x07: byte
    _pad: bytes = field(**BinaryPad(24))


@dataclass(slots=True)
class CultStart(TAEEventData):
    event_type = TAEEventType.CultStart  # 720

    cult_type: byte  # 0
    _pad: bytes = field(**BinaryPad(15))


@dataclass(slots=True)
class Unk730(TAEEventData):
    event_type = TAEEventType.Unk730  # 730

    unk_x00: int32
    unk_x04: int32
    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class Unk740(TAEEventData):
    event_type = TAEEventType.Unk740  # 740

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class IFrameState(TAEEventData):
    event_type = TAEEventType.IFrameState  # 760

    unk_x00: byte
    unk_x01: byte
    unk_x02: byte
    unk_x03: byte
    unk_x04: float
    unk_x08: float
    unk_x0c: float
    unk_x10: float
    unk_x14: float


@dataclass(slots=True)
class BonePos(TAEEventData):
    event_type = TAEEventType.BonePos  # 770

    unk_x00: int32
    unk_x04: float
    unk_x08: byte
    _pad: bytes = field(**BinaryPad(7))


@dataclass(slots=True)
class BoneFixOn1(TAEEventData):
    event_type = TAEEventType.BoneFixOn1  # 771

    bone_id: byte
    _pad: bytes = field(**BinaryPad(15))


@dataclass(slots=True)
class BoneFixOn2(TAEEventData):
    event_type = TAEEventType.BoneFixOn2  # 772

    unk_x00: int32
    unk_x04: float
    unk_x08: byte
    _pad: bytes = field(**BinaryPad(7))


@dataclass(slots=True)
class TurnLowerBody(TAEEventData):
    event_type = TAEEventType.TurnLowerBody  # 781

    turn_state: byte
    _pad: bytes = field(**BinaryPad(15))


@dataclass(slots=True)
class Unk782(TAEEventData):
    event_type = TAEEventType.Unk782  # 782

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class SpawnBulletByCultSacrifice1(TAEEventData):
    event_type = TAEEventType.SpawnBulletByCultSacrifice1  # 785

    unk_x00: float
    dummy_point_id: int32
    bullet_id: int32
    unk_x0c: byte
    unk_x0d: byte
    _pad: bytes = field(**BinaryPad(2))


@dataclass(slots=True)
class Unk786(TAEEventData):
    event_type = TAEEventType.Unk786  # 786

    unk_x00: float
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class Unk790(TAEEventData):
    event_type = TAEEventType.Unk790  # 790

    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class Unk791(TAEEventData):
    event_type = TAEEventType.Unk791  # 791

    _pad: bytes = field(**BinaryPad(8))


@dataclass(slots=True)
class HitEffect2(TAEEventData):
    event_type = TAEEventType.HitEffect2  # 792

    unk_x00: int16
    _pad: bytes = field(**BinaryPad(2))
    unk_x04: int32
    unk_x08: int32
    unk_x0c: byte
    unk_x0d: byte
    unk_x0e: byte
    unk_x0f: byte


@dataclass(slots=True)
class CultSacrifice1(TAEEventData):
    event_type = TAEEventType.CultSacrifice1  # 793

    sacrifice_value: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class SacrificeEmpty(TAEEventData):
    event_type = TAEEventType.SacrificeEmpty  # 794

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class Toughness(TAEEventData):
    event_type = TAEEventType.Toughness  # 795

    toughness_param_id: byte
    is_toughness_effective: bool
    _pad: bytes = field(**BinaryPad(2))
    toughness_rate: float


@dataclass(slots=True)
class BringCultMenu(TAEEventData):
    event_type = TAEEventType.BringCultMenu  # 796

    menu_type: byte
    _pad: bytes = field(**BinaryPad(15))


@dataclass(slots=True)
class CeremonyParamID(TAEEventData):
    event_type = TAEEventType.CeremonyParamID  # 797

    param_id: int32
    _pad: bytes = field(**BinaryPad(4))


@dataclass(slots=True)
class CultSingle(TAEEventData):
    event_type = TAEEventType.CultSingle  # 798

    unk_x00: float
    _pad: bytes = field(**BinaryPad(12))


@dataclass(slots=True)
class CultEmpty2(TAEEventData):
    event_type = TAEEventType.CultEmpty2  # 799

    _pad: bytes = field(**BinaryPad(16))


@dataclass(slots=True)
class Unk800(TAEEventData):
    event_type = TAEEventType.Unk800  # 800

    meters_per_tick: float
    meters_on_turn: float
    unk_x08: float
    _pad: bytes = field(**BinaryPad(4))

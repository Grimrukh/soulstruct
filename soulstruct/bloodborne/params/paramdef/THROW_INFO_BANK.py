from __future__ import annotations

__all__ = ["THROW_INFO_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class THROW_INFO_BANK(ParamRow):
    AttackingCharacterModel: int = ParamField(
        int, "AtkChrId", default=0,
        tooltip="Model ID of attacking character.",
    )
    DefendingCharacterModel: int = ParamField(
        int, "DefChrId", default=0,
        tooltip="Model ID of defending character.",
    )
    MaxDistance: float = ParamField(
        float, "Dist", default=0.0,
        tooltip="Maximum distance at which throw can be triggered.",
    )
    MinDifferenceInFacingAngle: float = ParamField(
        float, "DiffAngMin", default=0.0,
        tooltip="Minimum angular difference between attacker's facing direction and defender's facing direction.",
    )
    MaxDifferenceInFacingAngle: float = ParamField(
        float, "DiffAngMax", default=0.0,
        tooltip="Maximum angular difference between attacker's facing direction and defender's facing direction.",
    )
    MaxDistanceAbove: float = ParamField(
        float, "upperYRange", default=0.20000000298023224,
        tooltip="Maximum distance that defender can be above attacker.",
    )
    MaxDistanceBelow: float = ParamField(
        float, "lowerYRange", default=0.20000000298023224,
        tooltip="Maximum distance that defender can be below attacker.",
    )
    MaxAngleToDefender: float = ParamField(
        float, "diffAngMyToDef", default=60.0,
        tooltip="Maximum angular difference between attacker's direction and the direction of the defender.",
    )
    ThrowID: int = ParamField(
        int, "throwTypeId", default=0,
        tooltip="Throw ID that should be specified in Attacks to use this throw.",
    )
    AttackerAnimation: int = ParamField(
        int, "atkAnimId", game_type=Animation, default=0,
        tooltip="Animation played by attacker during throw.",
    )
    DefenderAnimation: int = ParamField(
        int, "defAnimId", game_type=Animation, default=0,
        tooltip="Animation played by defender during throw.",
    )
    MinHPPercentageForEscape: int = ParamField(
        ushort, "escHp", default=0,
        tooltip="Minimum HP percentage required to escape the throw early by mashing buttons. (Not sure if 0 prevents "
                "any escape, or if escapes are disabled by another parameter like",
    )
    EscapeCycleTime: int = ParamField(
        ushort, "selfEscCycleTime", default=0,
        tooltip="Time of escape cycle, in milliseconds. Not sure exactly what it does. Set to 100 milliseconds for "
                "throws that can be escaped, and zero otherwise.",
    )
    SphereCastUpperRadiusRatio: int = ParamField(
        ushort, "sphereCastRadiusRateTop", default=80,
        tooltip="Determines size of upper hemisphere of spherecast. I believe this is a percentage relative to the "
                "model size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's "
                "model size.",
    )
    SphereCastLowerRadiusRatio: int = ParamField(
        ushort, "sphereCastRadiusRateLow", default=80,
        tooltip="Determines size of lower hemisphere of spherecast. I believe this is a percentage relative to the "
                "model size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's "
                "model size.",
    )
    ButtonMashType: int = ParamField(
        byte, "PadType", THROW_PAD_TYPE, default=1,
        tooltip="Determines buttons that can be mashed to escape. Enumeration is unknown, but it is set to 3 for the "
                "Centipede Demon grab, Male Ghost grab, and Dark Hand grab, and 1 for every other throw.",
    )
    AttackEnabled: int = ParamField(
        byte, "AtkEnableState", THROW_ENABLE_STATE, default=0,
        tooltip="Internal description says 'Set the throwable throwable state type' (?). Set to 1 for all player "
                "backstabs and ripostes, and 0 otherwise (including player plunging attacks and all enemy throws).",
    )
    SnapToAttackerModelPoint: int = ParamField(
        byte, "atkSorbDmyId", game_type=ModelDummy, default=0,
        tooltip="Model point ID on attacker that defender will be snapped to. If this is zero, 'Snap To Defender "
                "Model Point' should be non-zero, and vice versa.",
    )
    SnapToDefenderModelPoint: int = ParamField(
        byte, "defSorbDmyId", game_type=ModelDummy, default=0,
        tooltip="Model point ID on defender that attacker will be snapped to. If this is zero, 'Snap To Attacker "
                "Model Point' should be non-zero, and vice versa.",
    )
    ThrowType: int = ParamField(
        byte, "throwType", THROW_TYPE, default=0,
        tooltip="Type of throw. Not sure what uses this, but it could affect various things.",
    )
    EscapeCycleCount: int = ParamField(
        byte, "selfEscCycleCnt", default=0,
        tooltip="Internal description says 'number of self-throwing cycles'. Always set to 1 when EscapeCycleTime is "
                "set to 100 (and MinHPPercentageForEscape is almost always 25). Not sure how it determines *when* you "
                "can escape the throw.",
    )
    ModelPointCharacterDirectionType: int = ParamField(
        byte, "dmyHasChrDirType", THROW_DMY_CHR_DIR_TYPE, default=0,
        tooltip="'Direction of model point possessed character when thrown'. Set to 1 for the Armored Tusk backstab, "
                "255 for the Iron Golem and Gaping Dragon grabs, and 0 otherwise.",
    )
    AttackerTurns: bool = ParamField(
        byte, "isTurnAtker:1", bit_count=1, default=False,
        tooltip="Attacker will turn when throw begins (presumably before model point snapping occurs).",
    )
    SkipAttackerWeaponCategoryCheck: bool = ParamField(
        byte, "isSkipWepCate:1", bit_count=1, default=False,
        tooltip="If True, the weapon category check for the attacker will be skipped. Enabled only for Dark Hand "
                "drain.",
    )
    SkipSphereCast: bool = ParamField(
        byte, "isSkipSphereCast:1", bit_count=1, default=False,
        tooltip="If True, the sphere cast check will be skipped. Usually False, but True for the coffin stab, Armored "
                "Tusk backstab, and a few large enemy grabs. (Presumably, if False, the throw trigger relies on "
                "distance and character angles only and is generally easier to trigger.)",
    )
    _BitPad0: int = ParamBitPad(byte, "pad0:5", bit_count=5)
    _Pad0: bytes = ParamPad(4, "pad1[4]")

from __future__ import annotations

__all__ = ["THROW_INFO_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field
from ..enums import *


THROW_INFO_BANK = {
    "param_type": "THROW_INFO_BANK",
    "file_name": "ThrowParam",
    "nickname": "Throws",
    "fields": [
        ParamFieldInfo("AtkChrId", "AttackingCharacterModel", True, int, "Model ID of attacking character."),
        ParamFieldInfo("DefChrId", "DefendingCharacterModel", True, int, "Model ID of defending character."),
        ParamFieldInfo("Dist", "MaxDistance", True, float, "Maximum distance at which throw can be triggered."),
        ParamFieldInfo(
            "DiffAngMin",
            "MinDifferenceInFacingAngle",
            True,
            float,
            "Minimum angular difference between attacker's facing direction and defender's facing direction.",
        ),
        ParamFieldInfo(
            "DiffAngMax",
            "MaxDifferenceInFacingAngle",
            True,
            float,
            "Maximum angular difference between attacker's facing direction and defender's facing direction.",
        ),
        ParamFieldInfo(
            "upperYRange", "MaxDistanceAbove", True, float, "Maximum distance that defender can be above attacker."
        ),
        ParamFieldInfo(
            "lowerYRange", "MaxDistanceBelow", True, float, "Maximum distance that defender can be below attacker."
        ),
        ParamFieldInfo(
            "diffAngMyToDef",
            "MaxAngleToDefender",
            True,
            float,
            "Maximum angular difference between attacker's direction and the direction of the defender.",
        ),
        ParamFieldInfo(
            "throwTypeId", "ThrowID", True, int, "Throw ID that should be specified in Attacks to use this throw."
        ),
        ParamFieldInfo(
            "atkAnimId",
            "AttackerAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by attacker during throw.",
        ),
        ParamFieldInfo(
            "defAnimId",
            "DefenderAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by defender during throw.",
        ),
        ParamFieldInfo(
            "escHp",
            "MinHPPercentageForEscape",
            True,
            int,
            "Minimum HP percentage required to escape the throw early by mashing buttons. (Not sure if 0 prevents "
            "any escape, or if escapes are disabled by another parameter like ",
        ),
        ParamFieldInfo(
            "selfEscCycleTime",
            "EscapeCycleTime",
            True,
            int,
            "Time of escape cycle, in milliseconds. Not sure exactly what it does. Set to 100 milliseconds for "
            "throws that can be escaped, and zero otherwise.",
        ),
        ParamFieldInfo(
            "sphereCastRadiusRateTop",
            "SphereCastUpperRadiusRatio",
            True,
            int,
            "Determines size of upper hemisphere of spherecast. I believe this is a percentage relative to the "
            "model size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's "
            "model size.",
        ),
        ParamFieldInfo(
            "sphereCastRadiusRateLow",
            "SphereCastLowerRadiusRatio",
            True,
            int,
            "Determines size of lower hemisphere of spherecast. I believe this is a percentage relative to the "
            "model size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's "
            "model size.",
        ),
        ParamFieldInfo(
            "PadType",
            "ButtonMashType",
            True,
            THROW_PAD_TYPE,
            "Determines buttons that can be mashed to escape. Enumeration is unknown, but it is set to 3 for the "
            "Centipede Demon grab, Male Ghost grab, and Dark Hand grab, and 1 for every other throw.",
        ),
        ParamFieldInfo(
            "AtkEnableState",
            "AttackEnabled",
            False,
            THROW_ENABLE_STATE,
            "Internal description says 'Set the throwable throwable state type' (?). Set to 1 for all player "
            "backstabs and ripostes, and 0 otherwise (including player plunging attacks and all enemy throws).",
        ),
        ParamFieldInfo(
            "atkSorbDmyId",
            "SnapToAttackerModelPoint",
            True,
            int,
            "Model point ID on attacker that defender will be snapped to. If this is zero, 'Snap To Defender "
            "Model Point' should be non-zero, and vice versa.",
        ),
        ParamFieldInfo(
            "defSorbDmyId",
            "SnapToDefenderModelPoint",
            True,
            int,
            "Model point ID on defender that attacker will be snapped to. If this is zero, 'Snap To Attacker "
            "Model Point' should be non-zero, and vice versa.",
        ),
        ParamFieldInfo(
            "throwType",
            "ThrowType",
            True,
            THROW_TYPE,
            "Type of throw. Not sure what uses this, but it could affect various things.",
        ),
        ParamFieldInfo(
            "selfEscCycleCnt",
            "EscapeCycleCount",
            True,
            int,
            "Internal description says 'number of self-throwing cycles'. Always set to 1 when EscapeCycleTime is "
            "set to 100 (and MinHPPercentageForEscape is almost always 25). Not sure how it determines *when* you "
            "can escape the throw.",
        ),
        ParamFieldInfo(
            "dmyHasChrDirType",
            "ModelPointCharacterDirectionType",
            False,
            THROW_DMY_CHR_DIR_TYPE,
            "'Direction of model point possessed character when thrown'. Set to 1 for the Armored Tusk backstab, "
            "255 for the Iron Golem and Gaping Dragon grabs, and 0 otherwise.",
        ),
        ParamFieldInfo(
            "isTurnAtker:1",
            "AttackerTurns",
            True,
            bool,
            "Attacker will turn when throw begins (presumably before model point snapping occurs).",
        ),
        ParamFieldInfo(
            "isSkipWepCate:1",
            "SkipAttackerWeaponCategoryCheck",
            True,
            bool,
            "If True, the weapon category check for the attacker will be skipped. Enabled only for Dark Hand "
            "drain.",
        ),
        ParamFieldInfo(
            "isSkipSphereCast:1",
            "SkipSphereCast",
            True,
            bool,
            "If True, the sphere cast check will be skipped. Usually False, but True for the coffin stab, "
            "Armored Tusk backstab, and a few large enemy grabs. (Presumably, if False, the throw trigger relies "
            "on distance and character angles only and is generally easier to trigger.)",
        ),
        ParamFieldInfo("pad0:5", "Pad1", False, bit_pad_field(5), "Null padding."),
        ParamFieldInfo("pad1[4]", "Pad2", False, pad_field(4), "Null padding."),
    ],
}

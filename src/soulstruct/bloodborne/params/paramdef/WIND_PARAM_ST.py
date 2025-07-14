from __future__ import annotations

__all__ = ["WIND_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class WIND_PARAM_ST(ParamRow):
    CommonCapsuleBeginModelPoint: int = ParamField(
        int16, "commonCapsuleBeginDmyId", game_type=ModelDummy, default=0,
        tooltip="TODO",
    )
    CommonCapsuleEndModelPoint: int = ParamField(
        int16, "commonCapsuleEndDmyId", game_type=ModelDummy, default=0,
        tooltip="TODO",
    )
    CommonCapsuleRadius: float = ParamField(
        float32, "commonCapsuleRadius", default=1.0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(120, "commonReserve[120]")
    EnableWindVFX: bool = ParamField(
        uint8, "sfxWindEnable:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    IgnorePlayerVFX: bool = ParamField(
        uint8, "sfxIgnorePlayerSfx:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableVFXCollision: bool = ParamField(
        uint8, "sfxIsCollision:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(3, "sfxPad_0[3]")
    VFXDirectionMinimumPitch: float = ParamField(
        float32, "sfxDirPitchMin", default=0.0,
        tooltip="TODO",
    )
    VFXDirectionMaximumPitch: float = ParamField(
        float32, "sfxDirPitchMax", default=0.0,
        tooltip="TODO",
    )
    VFXDirectionMinimumYaw: float = ParamField(
        float32, "sfxDirYawMin", default=0.0,
        tooltip="TODO",
    )
    VFXDirectionMaximumYaw: float = ParamField(
        float32, "sfxDirYawMax", default=0.0,
        tooltip="TODO",
    )
    VFXMinimumCycle: float = ParamField(
        float32, "sfxCycleMin", default=1.0,
        tooltip="TODO",
    )
    VFXMaximumCycle: float = ParamField(
        float32, "sfxCycleMax", default=1.0,
        tooltip="TODO",
    )
    VFXMinimumSpeed: float = ParamField(
        float32, "sfxSpeedMin", default=1.0,
        tooltip="TODO",
    )
    VFXMaximumSpeed: float = ParamField(
        float32, "sfxSpeedMax", default=1.0,
        tooltip="TODO",
    )
    VFXMaximumDrag: float = ParamField(
        float32, "sfxMaximumDrag", default=1.0,
        tooltip="TODO",
    )
    _Pad2: bytes = ParamPad(88, "sfxReserve[88]")
    EnableClothWind: bool = ParamField(
        uint8, "clothWindEnable:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    ClothVertexWind: bool = ParamField(
        uint8, "clothVertexWind:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    _Pad3: bytes = ParamPad(3, "clothPad_0[3]")
    ClothDirectionMinimumPitch: float = ParamField(
        float32, "clothDirPitchMin", default=0.0,
        tooltip="TODO",
    )
    ClothDirectionMaximumPitch: float = ParamField(
        float32, "clothDirPitchMax", default=0.0,
        tooltip="TODO",
    )
    ClothDirectionMinimumYaw: float = ParamField(
        float32, "clothDirYawMin", default=0.0,
        tooltip="TODO",
    )
    ClothDirectionMaximumYaw: float = ParamField(
        float32, "clothDirYawMax", default=0.0,
        tooltip="TODO",
    )
    ClothMinimumCycle: float = ParamField(
        float32, "clothCycleMin", default=1.0,
        tooltip="TODO",
    )
    ClothMaximumCycle: float = ParamField(
        float32, "clothCycleMax", default=1.0,
        tooltip="TODO",
    )
    ClothMinimumSpeed: float = ParamField(
        float32, "clothSpeedMin", default=1.0,
        tooltip="TODO",
    )
    ClothMaximumSpeed: float = ParamField(
        float32, "clothSpeedMax", default=1.0,
        tooltip="TODO",
    )
    ClothMaximumDrag: float = ParamField(
        float32, "clothMaximumDrag", default=1.0,
        tooltip="TODO",
    )
    _Pad4: bytes = ParamPad(88, "clothReserve[88]")

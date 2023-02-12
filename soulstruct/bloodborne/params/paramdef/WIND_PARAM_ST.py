from __future__ import annotations

__all__ = ["WIND_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WIND_PARAM_ST(ParamRow):
    CommonCapsuleBeginModelPoint: int = ParamField(
        short, "commonCapsuleBeginDmyId", default=0,
        tooltip="TODO",
    )
    CommonCapsuleEndModelPoint: int = ParamField(
        short, "commonCapsuleEndDmyId", default=0,
        tooltip="TODO",
    )
    CommonCapsuleRadius: float = ParamField(
        float, "commonCapsuleRadius", default=1.0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(120, "commonReserve[120]")
    EnableWindVFX: bool = ParamField(
        byte, "sfxWindEnable:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    IgnorePlayerVFX: bool = ParamField(
        byte, "sfxIgnorePlayerSfx:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableVFXCollision: bool = ParamField(
        byte, "sfxIsCollision:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(3, "sfxPad_0[3]")
    VFXDirectionMinimumPitch: float = ParamField(
        float, "sfxDirPitchMin", default=0.0,
        tooltip="TODO",
    )
    VFXDirectionMaximumPitch: float = ParamField(
        float, "sfxDirPitchMax", default=0.0,
        tooltip="TODO",
    )
    VFXDirectionMinimumYaw: float = ParamField(
        float, "sfxDirYawMin", default=0.0,
        tooltip="TODO",
    )
    VFXDirectionMaximumYaw: float = ParamField(
        float, "sfxDirYawMax", default=0.0,
        tooltip="TODO",
    )
    VFXMinimumCycle: float = ParamField(
        float, "sfxCycleMin", default=1.0,
        tooltip="TODO",
    )
    VFXMaximumCycle: float = ParamField(
        float, "sfxCycleMax", default=1.0,
        tooltip="TODO",
    )
    VFXMinimumSpeed: float = ParamField(
        float, "sfxSpeedMin", default=1.0,
        tooltip="TODO",
    )
    VFXMaximumSpeed: float = ParamField(
        float, "sfxSpeedMax", default=1.0,
        tooltip="TODO",
    )
    VFXMaximumDrag: float = ParamField(
        float, "sfxMaximumDrag", default=1.0,
        tooltip="TODO",
    )
    _Pad2: bytes = ParamPad(88, "sfxReserve[88]")
    EnableClothWind: bool = ParamField(
        byte, "clothWindEnable:1", bit_count=1, default=True,
        tooltip="TODO",
    )
    ClothVertexWind: bool = ParamField(
        byte, "clothVertexWind:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    _Pad3: bytes = ParamPad(3, "clothPad_0[3]")
    ClothDirectionMinimumPitch: float = ParamField(
        float, "clothDirPitchMin", default=0.0,
        tooltip="TODO",
    )
    ClothDirectionMaximumPitch: float = ParamField(
        float, "clothDirPitchMax", default=0.0,
        tooltip="TODO",
    )
    ClothDirectionMinimumYaw: float = ParamField(
        float, "clothDirYawMin", default=0.0,
        tooltip="TODO",
    )
    ClothDirectionMaximumYaw: float = ParamField(
        float, "clothDirYawMax", default=0.0,
        tooltip="TODO",
    )
    ClothMinimumCycle: float = ParamField(
        float, "clothCycleMin", default=1.0,
        tooltip="TODO",
    )
    ClothMaximumCycle: float = ParamField(
        float, "clothCycleMax", default=1.0,
        tooltip="TODO",
    )
    ClothMinimumSpeed: float = ParamField(
        float, "clothSpeedMin", default=1.0,
        tooltip="TODO",
    )
    ClothMaximumSpeed: float = ParamField(
        float, "clothSpeedMax", default=1.0,
        tooltip="TODO",
    )
    ClothMaximumDrag: float = ParamField(
        float, "clothMaximumDrag", default=1.0,
        tooltip="TODO",
    )
    _Pad4: bytes = ParamPad(88, "clothReserve[88]")

from __future__ import annotations

__all__ = ["DUNGEON_FEATURE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class DUNGEON_FEATURE_PARAM_ST(ParamRow):
    FeatureNameID: int = ParamField(
        uint, "featureNameId", default=0,
        tooltip="TODO",
    )
    SubFeatureGroupID: int = ParamField(
        byte, "subFeatureGroupId", default=0,
        tooltip="TODO",
    )
    EventFlagID: int = ParamField(
        byte, "eventflagId", game_type=Flag, default=0,
        tooltip="TODO",
    )
    DungeonNamePriority: int = ParamField(
        byte, "dungeonNamePriority", default=0,
        tooltip="TODO",
    )
    ReleaseFlagIDOffset: int = ParamField(
        byte, "releaseFlagIdOffset", default=-1,
        tooltip="TODO",
    )
    CharacterParamOffset: int = ParamField(
        uint, "npcParamIdOffset", default=0,
        tooltip="TODO",
    )
    ItemLotParamOffset: int = ParamField(
        uint, "itemLotParamIdOffset", default=0,
        tooltip="TODO",
    )
    EnemySpecialEffectID: int = ParamField(
        int, "eneSpeffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    GemDropCorrectionParamID: int = ParamField(
        int, "gemDropCorrectParamId", default=-1,
        tooltip="TODO",
    )
    GemGeneratorParamIDOffset: int = ParamField(
        uint, "gemGenParamIdOffset", default=0,
        tooltip="TODO",
    )
    DungeonNameModifierID: int = ParamField(
        int, "dungeonNameModifierId", default=-1,
        tooltip="TODO",
    )
    DungeonShortNameID: int = ParamField(
        int, "dungeonShortNameId", default=-1,
        tooltip="TODO",
    )

from __future__ import annotations

__all__ = ["DUNGEON_FEATURE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class DUNGEON_FEATURE_PARAM_ST(ParamRow):
    FeatureNameID: int = ParamField(
        uint32, "featureNameId", default=0,
        tooltip="TODO",
    )
    SubFeatureGroupID: int = ParamField(
        uint8, "subFeatureGroupId", default=0,
        tooltip="TODO",
    )
    EventFlagID: int = ParamField(
        uint8, "eventflagId", game_type=Flag, default=0,
        tooltip="TODO",
    )
    DungeonNamePriority: int = ParamField(
        uint8, "dungeonNamePriority", default=0,
        tooltip="TODO",
    )
    ReleaseFlagIDOffset: int = ParamField(
        uint8, "releaseFlagIdOffset", default=-1,
        tooltip="TODO",
    )
    CharacterParamOffset: int = ParamField(
        uint32, "npcParamIdOffset", default=0,
        tooltip="TODO",
    )
    ItemLotParamOffset: int = ParamField(
        uint32, "itemLotParamIdOffset", default=0,
        tooltip="TODO",
    )
    EnemySpecialEffectID: int = ParamField(
        int32, "eneSpeffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    GemDropCorrectionParamID: int = ParamField(
        int32, "gemDropCorrectParamId", default=-1,
        tooltip="TODO",
    )
    GemGeneratorParamIDOffset: int = ParamField(
        uint32, "gemGenParamIdOffset", default=0,
        tooltip="TODO",
    )
    DungeonNameModifierID: int = ParamField(
        int32, "dungeonNameModifierId", default=-1,
        tooltip="TODO",
    )
    DungeonShortNameID: int = ParamField(
        int32, "dungeonShortNameId", default=-1,
        tooltip="TODO",
    )

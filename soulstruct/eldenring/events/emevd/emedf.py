"""Dictionary that maps EMEVD instructions `(category, index)` to Soulstruct aliases and "prebaked" variants.

Used in tandem with `*.emedf.json` to compile/decompile EVS <-> EMEVD scripts.
"""
from __future__ import annotations

import typing as tp

from soulstruct.base.events.emevd.emedf import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.maps.constants import get_map_variable_name
from soulstruct.utilities.files import PACKAGE_PATH
from ..enums import *

__all__ = ["EMEDF", "EMEDF_ALIASES", "EMEDF_TESTS", "EMEDF_COMPARISON_TESTS"]


EVENT_RETURN_TYPE = {
    "type": EventReturnType,
    "default": None,
}
FLAG_SETTING = {
    "type": FlagSetting,
    "default": None,
}
RANGE_STATE = {
    "type": RangeState,
    "default": None,
    "hide_name": True,
}
FLAG_TYPE = {
    "type": FlagType,
    "default": None,
}
COMPARISON_TYPE = {
    "type": ComparisonType,
    "default": None,
}
CONDITION_GROUP = {
    "type": ConditionGroup,
    "default": None,
}
CUTSCENE_FLAGS = {
    "type": CutsceneFlags,
    "default": None,
}
AREA_ID = {
    "type": int,
    "default": None,
    "from_evs": lambda args: args["game_map"][0],
}
BLOCK_ID = {
    "type": int,
    "default": None,
    "from_evs": lambda args: args["game_map"][1],
}
CC_ID = {
    "type": int,
    "default": None,
    "from_evs": lambda args: args["game_map"][2],
}
DD_ID = {
    "type": int,
    "default": None,
    "from_evs": lambda args: args["game_map"][3],
}
GAME_MAP_EVS = {
    "type": MapTyping,
    "default": None,
    "to_evs": lambda args: get_map_variable_name((args["area_id"], args["block_id"], args["cc_id"], args["dd_id"])),
}
HOUR = {
    "type": int,
    "default": None,
    "from_evs": lambda args: args["time"][0],
}
MINUTE = {
    "type": int,
    "default": None,
    "from_evs": lambda args: args["time"][1],
}
SECOND = {
    "type": int,
    "default": None,
    "from_evs": lambda args: args["time"][2],
}
TIME_EVS = {
    "type": tuple,
    "default": None,
    "to_evs": lambda args: (args["hour"], args["minute"], args["second"]),
}
ITEM_TYPE = {
    "type": ItemType,
    "default": lambda args: args["item"].get_item_enum(),
    "comment": "Auto-detected from `item` type by default.",
}
FLAG = {
    "type": FlagTyping,
    "default": None,
}
LABEL = {
    "type": Label,
    "default": None,
    "hide_name": True,
}
FLAG_RANGE = {
    "type": FlagRangeTyping,
    "default": None,
    "to_evs": lambda args: FlagRange(args["first_flag"], args["last_flag"]),
}
FLAG_RANGE_FIRST = {
    "type": FlagTyping,
    "default": None,
    "from_evs": lambda args: args["flag_range"][0],
}
FLAG_RANGE_LAST = {
    "type": FlagTyping,
    "default": None,
    "from_evs": lambda args: args["flag_range"][1],
}

TARGET_COMPARISON_TYPE = {
    "type": ComparisonType,
    "default": ComparisonType.Equal,
}
MIN_TARGET_COUNT_INT = {
    "type": int,
    "default": 1,
}
TARGET_COUNT_INT = {
    "type": int,
    "default": 1,
}
TARGET_COUNT_FLOAT = {
    "type": float,
    "default": 1.0,
}


def AUTO_COORD_ENTITY_TYPE(arg_name: str, check_player=False):
    """Functions that retrieve `CoordEntityType` from the given argument name."""
    if check_player:
        return {
            "type": CoordEntityType,
            "default": (
                lambda args: CoordEntityType.Character if args[arg_name] == PLAYER
                else get_coord_entity_type(CoordEntityType, args[arg_name])
            ),
            "comment": f"Auto-detected from `{arg_name}` type by default. Sets `Character` type for `PLAYER`.",
        }
    return {
        "type": CoordEntityType,
        "default": lambda args: get_coord_entity_type(CoordEntityType, args[arg_name]),
        "comment": f"Auto-detected from `{arg_name}` type by default.",
    }


EMEDF = {
    (0, 0): {
        "alias": "IfConditionState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "IfConditionTrue": dict(state=True),
            "IfConditionFalse": dict(state=False),
        },
        "get_evaluated_conditions": lambda kwargs: {kwargs["input_condition"]} if kwargs["condition"] == 0 else set(),
    },
    (0, 1): {
        "alias": "IfValueComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "left": INT,
            "right": INT,
        },
        "partials": {
            "IfValueEqual": dict(comparison_type=ComparisonType.Equal),
            "IfValueNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfValueGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfValueLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfValueGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfValueLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (1, 0): {
        "alias": "IfTimeElapsed",
        "docstring": """
            Time since event started.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "seconds": FLOAT,
        },
    },
    (1, 1): {
        "alias": "IfFramesElapsed",
        "docstring": """
            Frames since event started.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "frames": INT,
        },
    },
    (1, 2): {
        "alias": "IfRandomTimeElapsed",
        "docstring": """
            Not used in vanilla DS1. Requires a random amount of time since event began.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "min_seconds": FLOAT,
            "max_seconds": FLOAT,
        },
    },
    (1, 3): {
        "alias": "IfRandomFramesElapsed",
        "docstring": """
            Not used in vanilla DS1. Requires a random amount of frames since event began.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "min_frames": INT,
            "max_frames": INT,
        },
    },
    (1, 4): {
        "alias": "IfTimeOfDay",
        "docstring": "Checks if current in-game time is EXACTLY the given time, down to the second.",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "hour": HOUR,
            "minute": MINUTE,
            "second": SECOND,
        },
        "evs_args": {
            "condition": {},
            "time": TIME_EVS,
        },
    },
    (1, 5): {
        "alias": "IfTimeOfDayInRange",
        "docstring": """
            Checks if current in-game time is between an earliest and latest time, each specified down to the second.
            
            Note that ranges will loop over midnight as expected, so checking, e.g., if the time is within the three-
            hour range between hour 23 (PM) and hour 2 (AM) is straightforward: `earliest=(23, 0, 0), latest=(2, 0, 0)`.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "earliest_hour": HOUR | {"from_evs": lambda args: args["earliest"][0]},
            "earliest_minute": MINUTE | {"from_evs": lambda args: args["earliest"][1]},
            "earliest_second": SECOND | {"from_evs": lambda args: args["earliest"][2]},
            "latest_hour": HOUR | {"from_evs": lambda args: args["latest"][0]},
            "latest_minute": MINUTE | {"from_evs": lambda args: args["latest"][1]},
            "latest_second": SECOND | {"from_evs": lambda args: args["latest"][2]},
        },
        "evs_args": {
            "condition": {},
            "earliest": TIME_EVS | {
                "to_evs": lambda args: (args["earliest_hour"], args["earliest_minute"], args["earliest_second"]),
            },
            "latest": TIME_EVS | {
                "to_evs": lambda args: (args["latest_hour"], args["latest_minute"], args["latest_second"]),
            },
        },
    },
    (3, 0): {
        "alias": "IfFlagState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": FLAG_SETTING | HIDE_NAME,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "flag": FLAG | HIDE_NAME,
        },
        "partials": {
            "IfFlagEnabled": dict(
                state=FlagSetting.On,
                flag_type=FlagType.Absolute,
            ),
            "IfFlagDisabled": dict(
                state=FlagSetting.Off,
                flag_type=FlagType.Absolute,
            ),
            "IfThisEventFlagEnabled": dict(
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "IfThisEventFlagDisabled": dict(
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "IfThisEventSlotFlagEnabled": dict(
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
            "IfThisEventSlotFlagDisabled": dict(
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
        },
    },
    (3, 1): {
        "alias": "IfFlagRangeState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": RANGE_STATE,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
        },
        "evs_args": {
            "condition": {},
            "state": {},
            "flag_type": {},
            "flag_range": FLAG_RANGE,
        },
        "partials": {
            "IfFlagRangeAllEnabled": dict(state=RangeState.AllOn, flag_type=FlagType.Absolute),
            "IfFlagRangeAllDisabled": dict(state=RangeState.AllOff, flag_type=FlagType.Absolute),
            "IfFlagRangeAnyEnabled": dict(state=RangeState.AnyOn, flag_type=FlagType.Absolute),
            "IfFlagRangeAnyDisabled": dict(state=RangeState.AnyOff, flag_type=FlagType.Absolute),
        },
    },
    (3, 2): {
        "alias": "IfCharacterRegionState",
        "docstring": """
            New argument with unknown purpose. Always 1 in vanilla resources. Probably for debug.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL,
            "character": NO_DEFAULT(CharacterTyping),
            "region": NO_DEFAULT(RegionTyping),
            "min_target_count": MIN_TARGET_COUNT_INT,
        },
        "partials": {
            "IfPlayerInsideRegion": dict(state=True, character=PLAYER),
            "IfPlayerOutsideRegion": dict(state=False, character=PLAYER),
            "IfCharacterInsideRegion": dict(state=True),
            "IfCharacterOutsideRegion": dict(state=False),
        },
    },
    (3, 3): {
        "alias": "IfEntityDistanceState",
        "docstring": """
            Same new argument as region test, with unknown purpose, and again always 1 in EMEVD resources.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL,
            "entity": NO_DEFAULT(CoordEntityTyping),
            "other_entity": NO_DEFAULT(CoordEntityTyping),
            "radius": FLOAT,
            "min_target_count": MIN_TARGET_COUNT_INT,
        },
        "partials": {
            "IfPlayerWithinDistance": dict(state=True, entity=PLAYER),
            "IfPlayerBeyondDistance": dict(state=False, entity=PLAYER),
            "IfEntityWithinDistance": dict(state=True),
            "IfEntityBeyondDistance": dict(state=False),
        },
    },
    (3, 4): {
        "alias": "IfPlayerItemStateExcludingStorage",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "item_type": ITEM_TYPE | HIDE_NAME,
            "item": NO_DEFAULT(ItemTyping),
            "state": BOOL | HIDE_NAME,
        },
        "evs_args": {
            "condition": {},
            "item": {},
            "state": {},
            "item_type": {},
        },
    },
    # (3, 5) removed (old "IfActionButton").
    (3, 6): {
        "alias": "IfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": NO_DEFAULT(MultiplayerState),
        },
        "partials": {
            "IfHost": dict(state=MultiplayerState.Host),
            "IfClient": dict(state=MultiplayerState.Client),
            "IfMultiplayer": dict(state=MultiplayerState.Multiplayer),
            "IfMultiplayerPending": dict(state=MultiplayerState.MultiplayerPending),
            "IfSingleplayer": dict(state=MultiplayerState.Singleplayer),
            "IfInvasion": dict(state=MultiplayerState.Invasion),
            "IfInvasionPending": dict(state=MultiplayerState.InvasionPending),
        },
    },
    (3, 7): {
        "alias": "IfAllPlayersRegionState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "region": NO_DEFAULT(RegionTyping),
        },
        "partials": {
            "IfAllPlayersInsideRegion": dict(state=True),
            "IfAllPlayersOutsideRegion": dict(state=False),
        },
    },
    (3, 8): {
        "alias": "IfMapPresenceState",
        "docstring": """
            Conditions upon player's presence in a particular game map.        
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "condition": {},
            "state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "IfInsideMap": dict(state=True),
            "IfOutsideMap": dict(state=False),
        },
    },
    (3, 9): {
        "alias": "IfMultiplayerEvent",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "event_id": INT,
        },
    },
    (3, 10): {
        "alias": "IfEnabledFlagCountComparison",
        "docstring": """
            Conditions upon a comparison with the number of enabled flags in the given range (inclusive).
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": INT,
        },
        "evs_args": {
            "condition": {},
            "flag_type": {},
            "comparison_type": {},
            "flag_range": FLAG_RANGE,
            "value": {},
        },
        "partials": {
            "IfEnabledFlagCountEqual": dict(comparison_type=ComparisonType.Equal),
            "IfEnabledFlagCountNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfEnabledFlagCountGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfEnabledFlagCountLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfEnabledFlagCountGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfEnabledFlagCountLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (3, 12): {
        "alias": "IfEventValueComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "flag": FLAG,
            "bit_count": BIT_COUNT,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": INT,
        },
        "partials": {
            "IfEventValueEqual": dict(comparison_type=ComparisonType.Equal),
            "IfEventValueNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfEventValueGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfEventValueLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfEventValueGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfEventValueLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    # (3, 13) removed (old "IfActionButtonBoss").
    (3, 14): {
        "alias": "IfAnyItemDroppedInRegion",
        "docstring": """
            Check if any item has been dropped in the specified region. Not sensitive to what the item is.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "region": NO_DEFAULT(RegionTyping),
        },
    },
    (3, 15): {
        "alias": "IfItemDropped",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "item_type": ITEM_TYPE,
            "item": NO_DEFAULT(ItemTyping),
        },
        "evs_args": {
            "condition": {},
            "item": {},
            "item_type": {},
        },
    },
    (3, 16): {
        "alias": "IfPlayerItemStateIncludingStorage",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "item_type": ITEM_TYPE | HIDE_NAME,
            "item": NO_DEFAULT(ItemTyping),
            "state": BOOL | HIDE_NAME,
        },
        "evs_args": {
            "condition": {},
            "item": {},
            "state": {},
            "item_type": {},
        },
    },
    (3, 17): {
        "alias": "IfNewGameCycleComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "completion_count": INT,
        },
        "partials": {
            "IfNewGameCycleEqual": dict(comparison_type=ComparisonType.Equal),
            "IfNewGameCycleNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfNewGameCycleGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfNewGameCycleLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfNewGameCycleGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfNewGameCycleLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    # (3, 18) removed (old "IfActionButtonBasicLineIntersect").
    # (3, 19) removed (old "IfActionButtonBossLineIntersect").
    (3, 20): {
        "alias": "IfEventsComparison",
        "docstring": """
            Check comparison of two event flag values. Haven't bothered adding shortcut functions for this.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "left_flag": FLAG,
            "left_bit_count": INT,
            "comparison_type": COMPARISON_TYPE,
            "right_flag": FLAG,
            "right_bit_count": INT,
        },
    },
    # TODO: (3, 21) not currently used in ER, but preserving in case it is used after DLC release (June 2024).
    # (3, 21): {
    #     "alias": "IfDLCState",
    #     "docstring": "TODO",
    #     "args": {
    #         "condition": CONDITION_GROUP | HIDE_NAME,
    #         "is_owned": BOOL,
    #     },
    #     "partials": {
    #         "IfDLCOwned": dict(is_owned=True),
    #         "IfDLCNotOwned": dict(is_owned=False),
    #     },
    # },
    (3, 22): {
        "alias": "IfOnlineState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "IfOnline": dict(state=True),
            "IfOffline": dict(state=False),
        },
    },
    (4, 0): {
        "alias": "IfCharacterDeathState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "is_dead": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterDead": dict(is_dead=True),  # Note reversed bool.
            "IfCharacterAlive": dict(is_dead=False),
        },
    },
    # (4, 1) removed (old "IfAttacked").
    (4, 2): {
        "alias": "IfHealthRatioComparison",
        "docstring": "Conditions upon a comparison to character health ratio (0-1).",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": FLOAT,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfHealthRatioEqual": dict(comparison_type=ComparisonType.Equal),
            "IfHealthRatioNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfHealthRatioGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfHealthRatioLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfHealthRatioGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfHealthRatioLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (4, 3): {
        "alias": "IfCharacterIsType",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "character_type": NO_DEFAULT(CharacterType),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
    },
    (4, 4): {
        "alias": "IfCharacterTargetingState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "targeting_character": NO_DEFAULT(CharacterTyping),
            "targeted_character": NO_DEFAULT(CharacterTyping),
            "state": BOOL | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterTargeting": dict(state=True),
            "IfCharacterNotTargeting": dict(state=False),
        },
    },
    (4, 5): {
        "alias": "IfCharacterSpecialEffectState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "special_effect": SPECIAL_EFFECT | {"hide_name": True},
            "state": BOOL | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfPlayerHasSpecialEffect": dict(character=PLAYER, state=True),
            "IfPlayerDoesNotHaveSpecialEffect": dict(character=PLAYER, state=False),
            "IfCharacterHasSpecialEffect": dict(state=True),
            "IfCharacterDoesNotHaveSpecialEffect": dict(state=False),
        },
    },
    (4, 6): {
        "alias": "IfCharacterPartHealthComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "npc_part_id": INT,
            "value": FLOAT,
            "comparison_type": COMPARISON_TYPE,
        },
        "partials": {
            "IfCharacterPartHealthLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (4, 7): {
        "alias": "IfCharacterBackreadState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterBackreadEnabled": dict(state=True),
            "IfCharacterBackreadDisabled": dict(state=False),
        },
    },
    (4, 8): {
        "alias": "IfCharacterTAEEventState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "tae_event_id": INT | {"internal_default": -1},
            "state": BOOL | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterHasTAEEvent": dict(state=True),
            "IfCharacterDoesNotHaveTAEEvent": dict(state=False),
        },
    },
    (4, 9): {
        "alias": "IfHasAIStatus",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "ai_status": NO_DEFAULT(AIStatusType),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
    },
    (4, 11): {
        "alias": "IfPlayerClass",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "class_type": NO_DEFAULT(ClassType) | HIDE_NAME,
        },
    },
    (4, 12): {
        "alias": "IfPlayerCovenant",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "covenant": INT,
        },
    },
    (4, 13): {
        "alias": "IfPlayerLevelComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": BIT_COUNT,
        },
        "partials": {
            "IfPlayerLevelEqual": dict(comparison_type=ComparisonType.Equal),
            "IfPlayerLevelNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfPlayerLevelGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfPlayerLevelLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfPlayerLevelGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfPlayerLevelLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (4, 14): {
        "alias": "IfHealthValueComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": INT,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfHealthValueEqual": dict(comparison_type=ComparisonType.Equal),
            "IfHealthValueNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfHealthValueGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfHealthValueLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfHealthValueGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfHealthValueLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (5, 0): {
        "alias": "IfAssetDestructionState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfAssetDestroyed": dict(state=True),
            "IfAssetNotDestroyed": dict(state=False),
        },
    },
    (5, 1): {
        "alias": "IfAssetDamaged",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "attacker": NO_DEFAULT(CharacterTyping),
        },
    },
    (5, 2): {
        "alias": "IfAssetActivated",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "obj_act_id": INT,
        },
    },
    (5, 3): {
        "alias": "IfAssetHealthValueComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": INT,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfAssetHealthValueEqual": dict(comparison_type=ComparisonType.Equal),
            "IfAssetHealthValueNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfAssetHealthValueGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfAssetHealthValueLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfAssetHealthValueGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfAssetHealthValueLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (11, 0): {
        "alias": "IfPlayerMovingOnCollision",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "collision": NO_DEFAULT(CollisionTyping) | HIDE_NAME,
        },
    },
    (11, 1): {
        "alias": "IfPlayerRunningOnCollision",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "collision": NO_DEFAULT(CollisionTyping) | HIDE_NAME,
        },
    },
    (11, 2): {
        "alias": "IfPlayerStandingOnCollision",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "collision": NO_DEFAULT(CollisionTyping) | HIDE_NAME,
        },
    },
    (1000, 0): {
        "alias": "AwaitConditionState",
        "docstring": "Not sure if this is ever really used over `IfConditionState`.",
        "args": {
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP | HIDE_NAME,
        },
        "partials": {
            "AwaitConditionTrue": dict(state=True),
            "AwaitConditionFalse": dict(state=False),
        },
        "get_evaluated_conditions": lambda kwargs: {kwargs["input_condition"]},
    },
    (1000, 1): {
        "alias": "SkipLinesIfConditionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP | HIDE_NAME,
        },
        "partials": {
            "SkipLinesIfConditionTrue": dict(state=True),
            "SkipLinesIfConditionFalse": dict(state=False),
        },
        "get_evaluated_conditions": lambda kwargs: {kwargs["input_condition"]},
    },
    (1000, 2): {
        "alias": "ReturnIfConditionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "EndIfConditionTrue": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfConditionFalse": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfConditionTrue": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfConditionFalse": dict(event_return_type=EventReturnType.Restart, state=False),
        },
        "get_evaluated_conditions": lambda kwargs: {kwargs["input_condition"]},
    },
    (1000, 3): {
        "alias": "SkipLines",
        "docstring": """
            Unconditional line skip.
        """,
        "args": {
            "line_count": INT | HIDE_NAME,
        },
    },
    (1000, 4): {
        "alias": "Return",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
        },
        "partials": {
            "End": dict(event_return_type=EventReturnType.End),
            "Restart": dict(event_return_type=EventReturnType.Restart),
        },
    },
    (1000, 5): {
        "alias": "SkipLinesIfValueComparison",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "left": INT,
            "right": INT,
        },
        "partials": {
            "SkipLinesIfValueEqual": dict(comparison_type=ComparisonType.Equal),
            "SkipLinesIfValueNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "SkipLinesIfValueGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "SkipLinesIfValueLessThan": dict(comparison_type=ComparisonType.LessThan),
            "SkipLinesIfValueGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "SkipLinesIfValueLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (1000, 6): {
        "alias": "ReturnIfValueComparison",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "left": INT,
            "right": INT,
        },
        "partials": {
            "EndIfValueEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.Equal,
            ),
            "EndIfValueNotEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.NotEqual,
            ),
            "EndIfValueGreaterThan": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.GreaterThan,
            ),
            "EndIfValueLessThan": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.LessThan,
            ),
            "EndIfValueGreaterThanOrEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.GreaterThanOrEqual,
            ),
            "EndIfValueLessThanOrEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.LessThanOrEqual,
            ),
            "RestartIfValueEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.Equal,
            ),
            "RestartIfValueNotEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.NotEqual,
            ),
            "RestartIfValueGreaterThan": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.GreaterThan,
            ),
            "RestartIfValueLessThan": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.LessThan,
            ),
            "RestartIfValueGreaterThanOrEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.GreaterThanOrEqual,
            ),
            "RestartIfValueLessThanOrEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.LessThanOrEqual,
            ),
        },
    },
    (1000, 7): {
        "alias": "SkipLinesIfLastConditionResultState",
        "docstring": """
            Skip some number of lines if the last result of the given condition (without re-evaluating) is `state`.
        """,
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "SkipLinesIfLastConditionResultTrue": dict(state=True),
            "SkipLinesIfLastConditionResultFalse": dict(state=False),
        },
    },
    (1000, 8): {
        "alias": "ReturnIfLastConditionResultState",
        "docstring": "End or restart event if last condition result (without re-evaluating) is the given `state`.",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "EndIfLastConditionResultTrue": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfLastConditionResultFalse": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfLastConditionResultTrue": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfLastConditionResultFalse": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    # (1000, 9) removed (old "WaitForNetworkApproval").
    (1001, 0): {
        "alias": "Wait",
        "docstring": """
            Wait for some number of seconds.
        """,
        "args": {
            "seconds": FLOAT | HIDE_NAME,
        },
    },
    (1001, 1): {
        "alias": "WaitFrames",
        "docstring": """
            Wait for some number of frames.
        """,
        "args": {
            "frames": INT,
        },
    },
    (1001, 2): {
        "alias": "WaitRandomSeconds",
        "docstring": """
            Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
        """,
        "args": {
            "min_seconds": FLOAT,
            "max_seconds": FLOAT,
        },
    },
    (1001, 3): {
        "alias": "WaitRandomFrames",
        "docstring": """
            Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
        """,
        "args": {
            "min_frames": INT,
            "max_frames": INT,
        },
    },
    (1003, 0): {
        "alias": "AwaitFlagState",
        "docstring": "Not sure if this is really used rather than `IfFlagState` with MAIN condition (0).",
        "args": {
            "state": FLAG_SETTING | HIDE_NAME,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "flag": FLAG,
        },
        "partials": {
            "AwaitFlagEnabled": dict(state=FlagSetting.On, flag_type=FlagType.Absolute),
            "AwaitFlagDisabled": dict(state=FlagSetting.Off, flag_type=FlagType.Absolute),
            "AwaitThisEventOn": dict(state=FlagSetting.On, flag_type=FlagType.RelativeToThisEvent, flag=0),
            "AwaitThisEventOff": dict(state=FlagSetting.Off, flag_type=FlagType.RelativeToThisEvent, flag=0),
            "AwaitThisEventSlotOn": dict(state=FlagSetting.On, flag_type=FlagType.RelativeToThisEventSlot, flag=0),
            "AwaitThisEventSlotOff": dict(state=FlagSetting.Off, flag_type=FlagType.RelativeToThisEventSlot, flag=0),
        },
    },
    (1003, 1): {
        "alias": "SkipLinesIfFlagState",
        "docstring": """
            Skip some number of lines if the specified flag (absolute, event-relative, or slot-relative) has the 
            specified state.
        """,
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": FLAG_SETTING | HIDE_NAME,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "flag": FLAG | HIDE_NAME,
        },
        "partials": {
            "SkipLinesIfFlagEnabled": dict(
                state=FlagSetting.On,
                flag_type=FlagType.Absolute,
            ),
            "SkipLinesIfFlagDisabled": dict(
                state=FlagSetting.Off,
                flag_type=FlagType.Absolute,
            ),
            "SkipLinesIfThisEventFlagEnabled": dict(
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "SkipLinesIfThisEventFlagDisabled": dict(
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "SkipLinesIfThisEventSlotFlagEnabled": dict(
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
            "SkipLinesIfThisEventSlotFlagDisabled": dict(
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
        },
    },
    (1003, 2): {
        "alias": "ReturnIfFlagState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE | HIDE_NAME,
            "state": FLAG_SETTING | HIDE_NAME,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "flag": FLAG | HIDE_NAME,
        },
        "partials": {
            "EndIfFlagEnabled": dict(
                event_return_type=EventReturnType.End,
                state=FlagSetting.On,
                flag_type=FlagType.Absolute,
            ),
            "EndIfFlagDisabled": dict(
                event_return_type=EventReturnType.End,
                state=FlagSetting.Off,
                flag_type=FlagType.Absolute,
            ),
            "EndIfThisEventFlagEnabled": dict(
                event_return_type=EventReturnType.End,
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "EndIfThisEventFlagDisabled": dict(
                event_return_type=EventReturnType.End,
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "EndIfThisEventSlotFlagEnabled": dict(
                event_return_type=EventReturnType.End,
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
            "EndIfThisEventSlotFlagDisabled": dict(
                event_return_type=EventReturnType.End,
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
            "RestartIfFlagEnabled": dict(
                event_return_type=EventReturnType.Restart,
                state=FlagSetting.On,
                flag_type=FlagType.Absolute,
            ),
            "RestartIfFlagDisabled": dict(
                event_return_type=EventReturnType.Restart,
                state=FlagSetting.Off,
                flag_type=FlagType.Absolute,
            ),
            "RestartIfThisEventFlagEnabled": dict(
                event_return_type=EventReturnType.Restart,
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "RestartIfThisEventFlagDisabled": dict(
                event_return_type=EventReturnType.Restart,
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "RestartIfThisEventSlotFlagEnabled": dict(
                event_return_type=EventReturnType.Restart,
                state=FlagSetting.On,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
            "RestartIfThisEventSlotFlagDisabled": dict(
                event_return_type=EventReturnType.Restart,
                state=FlagSetting.Off,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
        },
    },
    (1003, 3): {
        "alias": "SkipLinesIfFlagRangeState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": RANGE_STATE,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
        },
        "evs_args": {
            "line_count": {},
            "state": {},
            "flag_type": {},
            "flag_range": FLAG_RANGE | HIDE_NAME,
        },
        "partials": {
            "SkipLinesIfFlagRangeAllEnabled": dict(state=RangeState.AllOn, flag_type=FlagType.Absolute),
            "SkipLinesIfFlagRangeAllDisabled": dict(state=RangeState.AllOff, flag_type=FlagType.Absolute),
            "SkipLinesIfFlagRangeAnyEnabled": dict(state=RangeState.AnyOn, flag_type=FlagType.Absolute),
            "SkipLinesIfFlagRangeAnyDisabled": dict(state=RangeState.AnyOff, flag_type=FlagType.Absolute),
        },
    },
    (1003, 4): {
        "alias": "ReturnIfFlagRangeState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": RANGE_STATE,
            "flag_type": FLAG_TYPE | HIDE_NAME,
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
        },
        "evs_args": {
            "event_return_type": {},
            "state": {},
            "flag_type": {},
            "flag_range": FLAG_RANGE,
        },
        "partials": {
            "EndIfFlagRangeAllEnabled": dict(
                event_return_type=EventReturnType.End,
                state=RangeState.AllOn,
                flag_type=FlagType.Absolute,
            ),
            "EndIfFlagRangeAllDisabled": dict(
                event_return_type=EventReturnType.End,
                state=RangeState.AllOff,
                flag_type=FlagType.Absolute,
            ),
            "EndIfFlagRangeAnyEnabled": dict(
                event_return_type=EventReturnType.End,
                state=RangeState.AnyOn,
                flag_type=FlagType.Absolute,
            ),
            "EndIfFlagRangeAnyDisabled": dict(
                event_return_type=EventReturnType.End,
                state=RangeState.AnyOff,
                flag_type=FlagType.Absolute,
            ),
            "RestartIfFlagRangeAllEnabled": dict(
                event_return_type=EventReturnType.Restart,
                state=RangeState.AllOn,
                flag_type=FlagType.Absolute,
            ),
            "RestartIfFlagRangeAllDisabled": dict(
                event_return_type=EventReturnType.Restart,
                state=RangeState.AllOff,
                flag_type=FlagType.Absolute,
            ),
            "RestartIfFlagRangeAnyEnabled": dict(
                event_return_type=EventReturnType.Restart,
                state=RangeState.AnyOn,
                flag_type=FlagType.Absolute,
            ),
            "RestartIfFlagRangeAnyDisabled": dict(
                event_return_type=EventReturnType.Restart,
                state=RangeState.AnyOff,
                flag_type=FlagType.Absolute,
            ),
        },
    },
    # (1003, 5) updated below.
    # (1003, 6) updated below.
    (1003, 7): {
        "alias": "SkipLinesIfMapPresenceState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "line_count": {},
            "state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "SkipLinesIfInsideMap": dict(state=True),
            "SkipLinesIfOutsideMap": dict(state=False),
        },
    },
    (1003, 8): {
        "alias": "ReturnIfMapPresenceState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "event_return_type": {},
            "state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "EndIfInsideMap": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfOutsideMap": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfInsideMap": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfOutsideMap": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1005, 1): {
        "alias": "SkipLinesIfAssetDestructionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
        },
        "partials": {
            "SkipLinesIfAssetDestroyed": dict(state=True),
            "SkipLinesIfAssetNotDestroyed": dict(state=False),
        },
    },
    (1005, 2): {
        "alias": "ReturnIfAssetDestructionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
        },
        "partials": {
            "EndIfAssetDestroyed": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfAssetNotDestroyed": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfAssetDestroyed": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfAssetNotDestroyed": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (2000, 0): {
        "alias": "RunEvent",
        "docstring": "Initialize an instance (slot) of an event script with the given (optional) arguments.",
        "args": {
            "slot": INT | HIDE_NAME,
            "event_id": INT | HIDE_NAME,
            # Default argument is a single 32-bit zero, but more packed data can be passed.
            "args": {
                "type": tuple,  # will be unpacked for numeric
                "default": (0,),
            },
        },
        "evs_args": {  # event ID first
            "event_id": {},
            "slot": {},
            "args": {},
            "arg_types": {
                "type": str,
                "default": "",
            },
        },
    },
    # (2000, 1) removed (old "TerminateEvent").
    (2000, 2): {
        "alias": "SetNetworkSyncState",
        "docstring": "TODO",
        "args": {
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableNetworkSync": dict(state=True),
            "DisableNetworkSync": dict(state=False),
        },
    },
    (2000, 3): {
        "alias": "ClearMainCondition",
        "docstring": """
            Likely clears all conditions currently loaded into the main condition (0).
        """,
        "args": {
            "dummy": INT | {"default": 0},
        },
    },
    # (2000, 4) removed (old "IssuePrefetchRequest").
    (2000, 5): {
        "alias": "SaveRequest",
        "docstring": "Request the game to save player progress.",
        "args": {
            "dummy": INT | {"default": 0},
        },
    },
    (2000, 6): {
        "alias": "RunCommonEvent",
        "docstring": "Initialize an instance of an event script, usually from `common_func`, with the given arguments.",
        "args": {
            "slot": INT,
            "event_id": INT | HIDE_NAME,
            # Default argument is a single 32-bit zero, but more packed data can be passed.
            "args": {
                "type": tuple,  # will be unpacked for numeric
                "default": (0,),
            },
        },
        "evs_args": {  # event ID first
            "event_id": {},
            "slot": {},
            "args": {},
            "arg_types": {
                "type": str,
                "default": "",
            },
        },
    },
    (2000, 7): {
        "alias": "StartPS5Activity",
        "docstring": "TODO",
        "args": {
            "activity_id": INT,
        },
    },
    (2000, 8): {
        "alias": "EndPS5Activity",
        "docstring": "TODO",
        "args": {
            "activity_id": INT,
        },
    },
    (2002, 1): {
        "alias": "PlayCutsceneToAll",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
        },
    },
    (2002, 3): {
        "alias": "PlayCutsceneToPlayer",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "player_id": INT,
        },
    },
    (2002, 4): {
        "alias": "PlayCutsceneToPlayer_Unknown_2002_04",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "region": NO_DEFAULT(RegionTyping),
            "unk_12_16": INT,
            "player_id": INT,
            "unk_20_24": INT,
        },
    },
    (2002, 9): {
        "alias": "PlayCutsceneToPlayer_Unknown_2002_09",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "unk_8_12": INT,
            "unk_12_16": INT,
            "player_id": INT,
            "unk_20_24": INT,
            "unk_24_25": BOOL,
            "unk_25_26": BOOL,
            "unk_28_32": FLOAT,
            "unk_33_34": BOOL,
            "unk_34_35": BOOL,
            "unk_35_36": BOOL,
            "unk_36_37": BOOL,
        },
    },

    (2003, 3): {
        "alias": "SetSpawnerState",
        "docstring": """
            e.g. the baby skeletons in Tomb of the Giants.
        """,
        "args": {
            "entity": NO_DEFAULT(CoordEntityTyping),
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableSpawner": dict(state=True),
            "DisableSpawner": dict(state=False),
        },
    },
    (2003, 4): {
        "alias": "AwardItemLotToAllPlayers",
        "docstring": "TODO",
        "args": {
            "item_lot": INT,
        },
    },
    (2003, 5): {
        "alias": "ShootProjectile",
        "docstring": """
            The owner entity sets the 'team' of the projectile (i.e. who it can hurt).

            You can use this to directly spawn bullets by setting `source_entity` to `owner_entity`.

            Note that the angle arguments are all integers.
        """,
        "args": {
            "owner_entity": NO_DEFAULT(CoordEntityTyping),
            "source_entity": NO_DEFAULT(CoordEntityTyping),
            "dummy_id": INT,
            "behavior_id": INT,
            "launch_angle_x": INT,
            "launch_angle_y": INT,
            "launch_angle_z": INT,
        },
    },
    (2003, 6): {
        "alias": "SetMapCollisionState_2003_06",
        "docstring": "TODO: Unsure how this differs from `SetMapCollisionState`.",
        "args": {
            "collision": NO_DEFAULT(CollisionTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableMapCollision_2003_06": dict(state=True),
            "DisableMapCollision_2003_06": dict(state=False),
        },
    },
    (2003, 7): {
        "alias": "SetMapVisibilityState",
        "docstring": "TODO",
        "args": {
            "map_piece": NO_DEFAULT(MapPieceTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableMapVisibility": dict(state=True),
            "DisableMapVisibility": dict(state=False),
        },
    },
    (2003, 8): {
        "alias": "SetEventSlotState",
        "docstring": "Use to manually END or RESTART a given event ID and slot.",
        "args": {
            "event_id": INT | HIDE_NAME,
            "slot": INT | HIDE_NAME,
            "event_return_type": EVENT_RETURN_TYPE | HIDE_NAME,
        },
        "partials": {
            "EndEventSlot": dict(event_return_type=EventReturnType.End),
            "EndEvent": dict(slot=0, event_return_type=EventReturnType.End),
            "RestartEventSlot": dict(event_return_type=EventReturnType.Restart),
            "RestartEvent": dict(slot=0, event_return_type=EventReturnType.Restart),
        },
    },
    (2003, 9): {
        "alias": "InvertFlag",
        "docstring": """
            Unclear how this differs from calling `ToggleFlag` (which calls `SetEventFlag` with `FlagSetting.Change`).
        """,
        "args": {
            "flag": FLAG | HIDE_NAME,
        },
    },
    (2003, 11): {
        "alias": "SetBossHealthBarState",
        "docstring": """
            Note: slot number can be 0-2 in DS3.
        """,
        "args": {
            "state": BOOL | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "bar_slot": INT | {"default": 0},
            "name": {
                "type": NPCNameTyping,
                "default": 0,  # mainly for `Disable` partial, in which name does not matter
            },
        },
        "partials": {
            "EnableBossHealthBar": dict(
                state=True,
                __docstring="The character's health bar will appear at the bottom of the screen, with a name.",
            ),
            "DisableBossHealthBar": dict(
                state=False,
                __docstring="""
                        The character's health bar will disappear from the bottom of the screen.

                        WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter,
                        so only the first argument actually does anything. You're welcome to specify the name for 
                        clarity anyway (and vanilla events will show it when decompiled).
                    """,
            ),
        },
        "evs_args": {
            "character": {},
            "state": {},
            "name": {},
            "bar_slot": {},
        },
    },
    (2003, 12): {
        "alias": "KillBossAndDisplayBanner",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "banner_type": NO_DEFAULT(BannerType),
        },
    },
    (2003, 13): {
        "alias": "SetNavmeshFaceFlag",
        "docstring": """
            Set given navmesh type.
        """,
        "args": {
            "navmesh_id": {
                "type": NavigationEventTyping,
                "default": None,
            },
            "navmesh_type": {
                "type": NavmeshFlag,
                "default": None,
            },
            "operation": {
                "type": BitOperation,
                "default": None,
            },
        },
        "partials": {
            "AddNavmeshFaceFlag": dict(operation=BitOperation.Add),
            "RemoveNavmeshFaceFlag": dict(operation=BitOperation.Delete),
            "ToggleNavmeshFaceFlag": dict(operation=BitOperation.Invert),
        },
    },
    (2003, 14): {
        "alias": "WarpToMap",
        "docstring": """
            Warp the main player to the given player entity ID, which is in the Players tab of the MSB, in some map. By
            default, this warps to the 'default position' in the map (-1), which is the same point you would spawn at if 
            the game lost track of your stable footing (e.g. in 'wrong warp' glitches).
        """,
        "args": {
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
            "player_start": {
                "type": tp.Union[PlayerStart, int],
                "default": 0,  # must be unsigned
                "internal_default": 0,
            },
            "unk_8_12": INT | {"default": 0},  # weird -- values seen include `61000`, `-11100`, and `11000000`
        },
        "evs_args": {
            "game_map": GAME_MAP_EVS,
            "player_start": {},
            "unk_8_12": {},
        },
    },
    (2003, 15): {
        "alias": "HandleMinibossDefeat",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2003, 16): {
        "alias": "TriggerMultiplayerEvent",
        "docstring": """
            Used to make the Bell of Awakening sounds, for example.
        """,
        "args": {
            "event_id": INT,
        },
    },
    (2003, 17): {
        "alias": "SetRandomFlagInRange",
        "docstring": "Set the state of a random flag from a given range (inclusive).",
        "args": {
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
            "state": FLAG_SETTING,
        },
        "evs_args": {
            "flag_range": FLAG_RANGE,
            "state": {},
        },
        "partials": {
            "EnableRandomFlagInRange": dict(state=FlagSetting.On),
            "DisableRandomFlagInRange": dict(state=FlagSetting.Off),
            "ToggleRandomFlagInRange": dict(state=FlagSetting.Change),
        },
    },
    (2003, 18): {
        "alias": "ForceAnimation",
        "docstring": "Used a lot. Standard way to make a Character or Asset perform an animation.",
        "args": {
            "entity": NO_DEFAULT(AnimatedEntityTyping) | HIDE_NAME,
            "animation_id": {
                "type": int,
                "default": None,
                "hide_name": True,
                "internal_default": -1,
            },
            "loop": BOOL | {"default": False},
            "wait_for_completion": BOOL | {"default": False},
            "skip_transition": BOOL | {"default": False},
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
    },
    (2003, 21): {
        "alias": "IncrementNewGameCycle",
        "docstring": "Increase NG+ level by one.",
        "args": {
            "dummy": {
                "type": int,
                "default": 0,
                "hide_name": True,
            },
        },
    },
    (2003, 22): {
        "alias": "SetFlagRangeState",
        "docstring": "Set the state of an entire flag range (inclusive).",
        "args": {
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
            "state": FLAG_SETTING,
        },
        "evs_args": {
            "flag_range": FLAG_RANGE | HIDE_NAME,
            "state": {},
        },
        "partials": {
            "EnableFlagRange": dict(state=FlagSetting.On),
            "DisableFlagRange": dict(state=FlagSetting.Off),
            "ToggleFlagRange": dict(state=FlagSetting.Change),
        },
    },
    (2003, 23): {
        "alias": "SetRespawnPoint",
        "docstring": """
            Respawn point is an event set in the MSB.
        """,
        "args": {
            "respawn_point": INT,
        },
    },
    (2003, 24): {
        "alias": "RemoveItemFromPlayer",
        "docstring": """
            Item type is automatically detected. This instruction has a 'quantity' argument, but it seems broken, so you
            always have to remove *all* instances of the item. (Strangely, the similar command used in EzState doesn't 
            seem to have this bug.)

            WARNING: don't confuse 'Item' with the specific item type 'Good'.
        """,
        "args": {
            "item_type": ITEM_TYPE | HIDE_NAME,
            "item": NO_DEFAULT(ItemTyping),
            "quantity": INT | {"default": 0},
        },
        "partials": {
            "RemoveWeaponFromPlayer": dict(item_type=ItemType.Weapon),
            "RemoveArmorFromPlayer": dict(item_type=ItemType.Armor),
            "RemoveTalismanFromPlayer": dict(item_type=ItemType.Talisman),
            "RemoveGoodFromPlayer": dict(item_type=ItemType.Good),
        },
        "evs_args": {
            "item": {},
            "quantity": {},
            "item_type": {},
        },
    },
    (2003, 25): {
        "alias": "PlaceSummonSign",
        "docstring": """
            If you set a black summon sign, the specified NPC will try to invade automatically.
            
            New unknown argument in Elden Ring.
        """,
        "args": {
            "sign_type": {
                "type": SummonSignType,
                "default": None,
            },
            "character": NO_DEFAULT(CharacterTyping),
            "region": NO_DEFAULT(RegionTyping),
            "summon_flag": FLAG,
            "dismissal_flag": FLAG,
            "unknown": INT,
        },
    },
    (2003, 26): {
        "alias": "SetSoapstoneMessageState",
        "docstring": """
            Enable or disable developer message. Technically not a 'Soapstone' message anymore, but keeping the name.
        """,
        "args": {
            "message_id": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableSoapstoneMessage": dict(state=True),
            "DisableSoapstoneMessage": dict(state=False),
        },
    },
    (2003, 28): {
        "alias": "AwardAchievement",
        "docstring": """
            For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
            accessibility of existing achievements. This interacts with Steam, which is always dangerous.
        """,
        "args": {
            "achievement_id": INT,
        },
    },
    (2003, 31): {
        "alias": "IncrementEventValue",
        "docstring": """
            You can use a contiguous array of flags as a single value. Use this to increment that value by 1.

            The array begins at `flag` and extends for `bit_count`. For example, a 'bit_count' of 8 gives you a 
            theoretical maximum of 256. You can set a 'max_value' less than that to limit the value. (I'm not sure if it 
            ticks over back to zero if `max_value` is greater than the possible value given the bit count.)
        
            The most significant bit is represented at `flag`, and the least significant bit at `flag + bit_count - 1`.
        
            This is used for counters in the vanilla game, such as the number of bosses killed while Rhea is at Undead 
            Parish.
        """,
        "args": {
            "flag": FLAG | HIDE_NAME,
            "bit_count": BIT_COUNT,
            "max_value": INT,
        },
    },
    (2003, 32): {
        "alias": "ClearEventValue",
        "docstring": """
            Clears the given multi-flag. This is basically like disabling `bit_count` flags in a row, starting at 
            `flag`.
        """,
        "args": {
            "flag": FLAG | HIDE_NAME,
            "bit_count": INT,
        },
    },
    # (2003, 33) removed (old "SetNextSnugglyTrade").
    # (2003, 34) removed (old "SnugglyItemDrop").
    (2003, 35): {
        "alias": "MoveRemains",
        "docstring": """
            Move all bloodstains and dropped items from one region to another (I assume). Used to move your
            remains out of Gwyndolin's endless corridor.
        """,
        "args": {
            "source_region": NO_DEFAULT(RegionTyping),
            "destination_region": NO_DEFAULT(RegionTyping),
        },
    },
    (2003, 36): {
        "alias": "AwardItemLotToHostOnly",
        "docstring": """
            You can simply call AwardItemLot() with the same argument, which will redirect here, as you'll almost never
            *not* want to award an item lot to the host only.
        """,
        "args": {
            "item_lot": INT,
        },
    },
    (2003, 41): {
        "alias": "ActivateKillplaneForModel",
        "docstring": "Not used much. Activates a horizontal killplane that only affects a particular model ID.",
        "args": {
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "y_threshold": FLOAT,
            "target_model_id": INT,
        },
        "evs_args": {
            "game_map": GAME_MAP_EVS,
            "y_threshold": {},
            "target_model_id": {},
        },
    },
    (2004, 1): {
        "alias": "SetAIState",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableAI": dict(state=True),
            "DisableAI": dict(state=False),
        },
    },
    (2004, 2): {
        "alias": "SetTeamType",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "new_team": {
                "type": TeamType,
                "default": None,
                "hide_name": True,
            },
        },
    },
    # (2004, 3) removed (old "MoveToEntity").
    (2004, 4): {
        "alias": "Kill",
        "docstring": """
            Technically a kill 'request.'
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "award_runes": BOOL | {"default": False},
        },
    },
    (2004, 5): {
        "alias": "SetCharacterState",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableCharacter": dict(state=True),
            "DisableCharacter": dict(state=False),
        },
    },
    (2004, 6): {
        "alias": "EzstateAIRequest",
        "docstring": """
            Slot number ranges from 0 to 3.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "command_id": INT,
            "command_slot": INT,
        },
    },
    (2004, 7): {
        "alias": "CreateProjectileOwner",
        "docstring": """
            A 'bullet owner' that will spawn things according to the Spawner section of the MSB.
        """,
        "args": {
            "entity": NO_DEFAULT(CoordEntityTyping),
        },
    },
    (2004, 8): {
        "alias": "AddSpecialEffect",
        "docstring": """
            'Special effect' as in a buff/debuff, not graphical effects (though they may come with one).
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "special_effect": INT | HIDE_NAME,
        },
    },
    # (2004, 9) removed (old "SetStandbyAnimationSettings").
    (2004, 10): {
        "alias": "SetGravityState",
        "docstring": """
            Simply determines if the character loses height as it moves around. They will still gain height by running 
            up slopes.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableGravity": dict(state=True),
            "DisableGravity": dict(state=False),
        },
    },
    (2004, 11): {
        "alias": "SetCharacterEventTarget",
        "docstring": """
            Likely refers to patrolling behavior.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "entity": NO_DEFAULT(CoordEntityTyping),
        },
    },
    (2004, 12): {
        "alias": "SetImmortalityState",
        "docstring": """
            Character will take damage, but not die (i.e. cannot go below 1 HP).
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableImmortality": dict(state=True),
            "DisableImmortality": dict(state=False),
        },
    },
    (2004, 13): {
        "alias": "SetNest",
        "docstring": """
            Home point for entity AI.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "region": NO_DEFAULT(RegionTyping),
        },
    },
    (2004, 14): {
        "alias": "FaceEntityAndForceAnimation",
        "docstring": """
            Rotate a character to face a target map entity of any type, then optionally force an animation.

            WARNING: This may crash an event script if `character` is currently disabled!
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "target_entity": NO_DEFAULT(CoordEntityTyping) | HIDE_NAME,
            "animation": INT | {"default": -1, "internal_default": -1},
            "wait_for_completion": BOOL | {"default": False},
        },
    },
    (2004, 15): {
        "alias": "SetInvincibilityState",
        "docstring": """
            Character cannot take damage or die.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableInvincibility": dict(state=True),
            "DisableInvincibility": dict(state=False),
        },
    },
    (2004, 16): {
        "alias": "ClearTargetList",
        "docstring": """
            Clear list of targets from character AI.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
        },
    },
    (2004, 17): {
        "alias": "AICommand",
        "docstring": """
            The given `command_id` can be accessed in AI Lua scripts with `ai:GetEventRequest(slot)`.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "command_id": INT,
            "command_slot": INT,
        },
    },
    (2004, 18): {
        "alias": "SetEventPoint",
        "docstring": """
            Not sure what the usage of this is, but it is likely used to change patrol behavior.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "region": NO_DEFAULT(RegionTyping),
            "reaction_range": FLOAT,
        },
    },
    (2004, 19): {
        "alias": "SetAIParamID",
        "docstring": """
            Change character's AI parameter index.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "ai_param_id": INT,
        },
    },
    (2004, 20): {
        "alias": "ReplanAI",
        "docstring": """
            Clear current AI goal list and force character to replan it.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
        },
    },
    (2004, 21): {
        "alias": "RemoveSpecialEffect",
        "docstring": """
            'Special effect' as in a buff/debuff, not graphical effects (though they may come with one).
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "special_effect": INT | HIDE_NAME,
        },
    },
    (2004, 22): {
        "alias": "CreateNPCPart",
        "docstring": """
            Complex. Sets specific damage parameters for part of an NPC model. Further changes to the specific part can 
            be made using the events below. The part is specified using the NPCPartType slot. Look at usage in tail cut 
            events to understand these more.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "npc_part_id": INT,
            "part_index": {
                "type": NPCPartType,
                "default": None,
            },
            "part_health": INT,
            "damage_correction": {
                "type": float,
                "default": 1.0,
            },
            "body_damage_correction": {
                "type": float,
                "default": 1.0,
            },
            "is_invincible": BOOL | {"default": False},
            "start_in_stop_state": BOOL | {"default": False},
        },
    },
    (2004, 23): {
        "alias": "SetNPCPartHealth",
        "docstring": """
            You must create the part first.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "npc_part_id": INT,
            "desired_health": INT,
            "overwrite_max": BOOL,
        },
    },
    (2004, 24): {
        "alias": "SetNPCPartEffects",
        "docstring": """
            Attach material effects to an NPC part.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "npc_part_id": INT,
            "material_sfx_id": INT,
            "material_vfx_id": INT,
            "unk_16_20": INT,
            "unk_20_24": INT,
            "unk_24_28": INT,
        },
    },
    (2004, 25): {
        "alias": "SetNPCPartBulletDamageScaling",
        "docstring": """
            Scale the damage dealt to the part. Usually used to set damage to zero, e.g. Smough's hammer.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "npc_part_id": INT,
            "desired_scaling": FLOAT,
        },
    },
    (2004, 26): {
        "alias": "SetDisplayMask",
        "docstring": """
            Different bits correspond to different parts of the character model. You can see the initial values for 
            these in the NPC params. This is generally used to disable tails when they are cut off.

            `switch_type` can be 0 (off), 1 (on), or 2 (change).
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "bit_index": INT,
            "switch_type": {
                "type": OnOffChange,
                "default": None,
            },
        },
    },
    (2004, 27): {
        "alias": "SetCollisionMask",
        "docstring": """
            See above. This affects the NPC's Collision, not appearance.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "bit_index": INT,
            "switch_type": {
                "type": OnOffChange,
                "default": None,
            },
        },
    },
    (2004, 28): {
        "alias": "SetNetworkUpdateAuthority",
        "docstring": """
            Complex; look at existing usage. Authority level must be 'Normal' or 'Forced'.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "authority_level": {
                "type": UpdateAuthority,
                "default": None,
            },
        },
    },
    (2004, 29): {
        "alias": "SetBackreadState",
        "docstring": """
            I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread' 
            of a character has a larger effect on game resources. It is used, for example, to disable the Fair Lady and 
            Eingyi during the Demon Firesage boss fight.

            Also note reversed bool.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "remove": BOOL,
        },
        "partials": {
            "EnableBackread": dict(remove=False),  # Note reversed bool.
            "DisableBackread": dict(remove=True),
        },
    },
    (2004, 30): {
        "alias": "SetHealthBarState",
        "docstring": """
            Normal health bar that appears above character.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableHealthBar": dict(state=True),
            "DisableHealthBar": dict(state=False),
        },
    },
    (2004, 31): {
        "alias": "SetCharacterCollisionState",
        "docstring": """
            Note that the bool is no longer inverted, as in older games.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL,
        },
        "partials": {
            "EnableCharacterCollision": dict(state=True),
            "DisableCharacterCollision": dict(state=False),
        },
    },
    # (2004, 32) removed (old "AIEvent").
    (2004, 33): {
        "alias": "ReferDamageToEntity",
        "docstring": """
            All damage dealt to the first character will *also* (not *only*) be dealt to the target entity. I'm not 100%
            sure if the target entity can be an Asset.

            Only used by the Four Kings in the vanilla game.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "target_entity": {
                "type": CharacterTyping,  # TODO: Can it be an Asset?
                "default": None,
            },
        },
    },
    (2004, 34): {
        "alias": "SetNetworkUpdateRate",
        "docstring": """
            Not sure what 'is_fixed' does. I believe only 'Always' and 'Never' are used in the vanilla game.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "is_fixed": BOOL,
            "update_rate": {
                "type": CharacterUpdateRate,
                "default": None,
            },
        },
    },
    (2004, 35): {
        "alias": "SetBackreadStateAlternate",
        "docstring": """
            I have no idea how this differs from the standard backread function above.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
    },
    (2004, 37): {
        "alias": "DropMandatoryTreasure",
        "docstring": """
            This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
            treasure that has a 100% drop rate, hence the name, but I haven't confirmed this.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
        },
    },
    (2004, 38): {
        "alias": "BetrayCurrentCovenant",
        "docstring": """
            Dummy argument does nothing.
        """,
        "args": {
            "dummy": INT | {"default": 0},
        },
    },
    (2004, 39): {
        "alias": "SetAnimationsState",
        "docstring": "TODO",
        "args": {
            "entity": NO_DEFAULT(AnimatedEntityTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableAnimations": dict(state=True),
            "DisableAnimations": dict(state=False),
        },
    },
    (2004, 40): {
        "alias": "MoveAndSetDrawParent",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "destination_type": AUTO_COORD_ENTITY_TYPE("destination"),
            "destination": NO_DEFAULT(CoordEntityTyping),
            "dummy_id": DUMMY_ID,
            "set_draw_parent": {
                "type": MapPartTyping,
                "default": None,
            },
        },
        "evs_args": {
            "character": {},
            "destination": {},
            "set_draw_parent": {},
            "dummy_id": {},
            "destination_type": {},
        },
    },
    (2004, 41): {
        "alias": "ShortMove",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "destination_type": AUTO_COORD_ENTITY_TYPE("destination"),
            "destination": NO_DEFAULT(CoordEntityTyping),
            "dummy_id": DUMMY_ID,
        },
        "evs_args": {
            "character": {},
            "destination": {},
            "dummy_id": {},
            "destination_type": {},
        },
    },
    (2004, 42): {
        "alias": "MoveAndCopyDrawParent",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "destination_type": AUTO_COORD_ENTITY_TYPE("destination"),
            "destination": NO_DEFAULT(CoordEntityTyping),
            "dummy_id": DUMMY_ID,
            "copy_draw_parent": NO_DEFAULT(AnimatedEntityTyping),
        },
        "evs_args": {
            "character": {},
            "destination": {},
            "copy_draw_parent": {},
            "dummy_id": {},
            "destination_type": {},
        },
    },
    (2004, 43): {
        "alias": "ResetAnimation",
        "docstring": """
            Cancels an animation. Note the inverted bool for controlling interpolation.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "disable_interpolation": BOOL | {"default": False},
        },
    },
    # (2004, 44) removed (old "SetTeamTypeAndExitStandbyAnimation").
    (2004, 47): {
        "alias": "EqualRecovery",
        "docstring": """
            Unknown effect. Only used in Battle of Stoicism, so likely useless to you.
        """,
        "args": {},
    },
    (2005, 1): {
        "alias": "DestroyAsset",
        "docstring": """
            Technically 'requests' the asset's destruction. No idea what the slot number does.
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "request_slot": {
                "type": int,
                "default": 1,
            },
        },
    },
    (2005, 2): {
        "alias": "RestoreAsset",
        "docstring": """
            The opposite of destruction. Restores it to its original MSB coordinates.
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
        },
    },
    (2005, 3): {
        "alias": "SetAssetState",
        "docstring": "TODO",
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableAsset": dict(state=True),
            "DisableAsset": dict(state=False),
        },
    },
    (2005, 4): {
        "alias": "SetTreasureState",
        "docstring": "TODO",
        "args": {
            "asset": NO_DEFAULT(AssetTyping),
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableTreasure": dict(
                state=True,
                __docstring="Enables any treasure attached to this asset by MSB events.",
            ),
            "DisableTreasure": dict(
                state=False,
                __docstring="""
                    Disables any treasure attached to this asset by MSB events.

                    If you want to disable treasure by default, you can do it in the MSB by changing a certain event 
                    value to 255.
                """,
            ),
        },
    },
    (2005, 5): {
        "alias": "ActivateAsset",
        "docstring": """
            Manually call a specific ObjAct event attached to this asset. I believe 'relative_index' refers to the 
            points on the asset at which it can be activated (e.g. which side of a gate you are on).

            Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how 
            the game gets Patches to pull the lever in the Catacombs.
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "obj_act_id": INT,
            "relative_index": INT,
        },
    },
    (2005, 6): {
        "alias": "SetAssetActivation",
        "docstring": """
            Sets whether the asset can be activated (1) or not activated (0).
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "obj_act_id": INT | {"internal_default": -1},
            "state": BOOL | HIDE_NAME,
        },
        # No Enable/Disable partials here because there are custom instructions with those names that merge the `Idx`
        # variant in.
    },
    (2005, 7): {
        "alias": "EndOfAnimation",
        "docstring": """
            Sets entity to whatever state it would have after the given animation. Used often to open doors that have
            already been opened when you reload the map, etc. I doubt it can be used with characters, but haven't 
            confirmed.
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping),
            "animation_id": INT,
        },
    },
    (2005, 8): {
        "alias": "PostDestruction",
        "docstring": """
            Sets the asset to whatever appearance it would have after being destroyed. Again, not sure what 'slot' 
            does, but it's literally *always* 1 in vanilla scripts (and from my testing, the instruction doesn't work 
            with `slot=0`).
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "request_slot": {
                "type": int,
                "default": 1,
            },
        },
    },
    (2005, 9): {
        "alias": "CreateHazard",
        "docstring": """
            Turn an asset into an environmental hazard. It deals damage when touched according to the NPC Behavior 
            params you give it. The dummy_id determines which part of the asset is hazardous (with the given radius 
            and life, relative to the time this instruction occurs).

            An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.

            'target_type' determines what the hazard can damage (Character and/or Map).
        """,
        "args": {
            "asset_flag": FLAG,
            "asset": NO_DEFAULT(AssetTyping),
            "dummy_id": INT,
            "behavior_param_id": INT,
            "target_type": {
                "type": DamageTargetType,
                "default": None,
            },
            "radius": FLOAT,
            "life": FLOAT,
            "repetition_time": FLOAT,
        },
    },
    (2005, 11): {
        "alias": "MoveAssetToCharacter",
        "docstring": "Move an asset to a character.",
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "character": {
                "type": CharacterTyping,
                "default": None,
                "internal_default": 0,
            },
            "dummy_id": DUMMY_ID,
        },
    },
    (2005, 12): {
        "alias": "RemoveAssetFlag",
        "docstring": """
            No idea what this does. I believe it might undo the CreateHazard instruction, at least.
        """,
        "args": {
            "asset_flag": FLAG,
        },
    },
    (2005, 13): {
        "alias": "SetAssetInvulnerabilityState",
        "docstring": """
            1 = invulnerable.
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableAssetInvulnerability": dict(state=True),
            "DisableAssetInvulnerability": dict(state=False),
        },
    },
    (2005, 14): {
        "alias": "SetAssetActivationWithIdx",
        "docstring": """
            Similar to SetAssetActivation, but you can provide the relative index to disable (e.g. one side of a door).
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "obj_act_id": INT | {"internal_default": -1},
            "relative_index": INT,
            "state": BOOL | HIDE_NAME,
        },
        # No partials. Use custom `EnableAssetActivation` instructions with optional `relative_index` argument.
    },
    (2005, 15): {
        "alias": "EnableTreasureCollection",
        "docstring": """
            Forces an asset to spawn its treasure, even if the treasure's ItemLot flag is already enabled.

            Useful if you want some treasure to reappear (after, say, taking it from the player and disabling the 
            ItemLot flag) without the player needing to reload the map.
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping),
        },
    },
    (2006, 1): {
        "alias": "DeleteVFX",
        "docstring": """
            Delete visual VFX. If 'erase_root_only' is True (default), effect particles already emitted will live out 
            the rest of their lifetimes (e.g. making a fog gate disappear organically). The ID is given in the MSB.
        """,
        "args": {
            "vfx_id": NO_DEFAULT(VFXEventTyping) | HIDE_NAME,
            "erase_root_only": {
                "type": bool,
                "default": True,
            },
        },
    },
    (2006, 2): {
        "alias": "CreateVFX",
        "docstring": """
            Create visual VFX. The ID is given in the MSB (e.g. fog effect for boss gates and checkpoints).
        """,
        "args": {
            "vfx_id": NO_DEFAULT(VFXEventTyping) | HIDE_NAME,
        },
    },
    (2006, 3): {
        "alias": "CreateTemporaryVFX",
        "docstring": """
            Create one-off visual VFX (an FFX ID) attached to the given 'anchor_entity'. The VFX, of course, must be
            currently loaded (or in common effects).
        """,
        "args": {
            "anchor_type": AUTO_COORD_ENTITY_TYPE("anchor_entity", check_player=True),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping),
            "dummy_id": DUMMY_ID,
            "vfx_id": INT,
        },
        "evs_args": {
            "vfx_id": {},
            "anchor_entity": {},
            "dummy_id": {},
            "anchor_type": {},
        },
    },
    (2006, 4): {
        "alias": "CreateAssetVFX",
        "docstring": "TODO",
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "dummy_id": INT,
            "vfx_id": INT,
        },
    },
    (2006, 5): {
        "alias": "DeleteAssetVFX",
        "docstring": """
            Note `erase_root` vs. `erase_root_only` for map SFX.
        """,
        "args": {
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "erase_root": {
                "type": bool,
                "default": True,
            },
        },
    },
    (2007, 1): {
        "alias": "DisplayDialog",
        "docstring": """
            Display a dialog box at the bottom of the screen. You can't use this to get player input, but you can 
            display short simple messages. It defaults to a box with no buttons (which is still dismissed when you press 
            A).

            The 'display_distance' argument specifies how far you can move away from the 'anchor_entity' before the 
            message automatically disappears. If `anchor_entity=-1` (default), some kind of default anchor is used 
            (probably just the position where the player was standing).
        """,
        "args": {
            "text": NO_DEFAULT(EventTextTyping),
            "button_type": {
                "type": ButtonType,
                "default": ButtonType.OK_or_Cancel,
            },
            "number_buttons": {
                "type": NumberButtons,
                "default": NumberButtons.NoButton,
            },
            "anchor_entity": {
                "type": CoordEntityTyping,
                "default": 0,
                "internal_default": 0,
            },
            "display_distance": {
                "type": float,
                "default": 3.0,
            },
        },
        "evs_args": {
            "text": {},
            "anchor_entity": {},
            "display_distance": {},
            "button_type": {},
            "number_buttons": {},
        },
    },
    (2007, 2): {
        "alias": "DisplayBanner",
        "docstring": """
            Display a pre-rendered banner. You'll have to change the textures (in menu_local.tpf) to change them.
        """,
        "args": {
            "banner_type": NO_DEFAULT(BannerType) | HIDE_NAME | {"internal_default": 13},
        },
    },
    (2007, 3): {
        "alias": "DisplayStatus",
        "docstring": """
            Displays a large message that appears at the top of the screen, such as the message that tells you how to
            remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get 
            rid of the message until it times out on its own.
        """,
        "args": {
            "text": NO_DEFAULT(EventTextTyping) | HIDE_NAME,
            "pad_enabled": {
                "type": bool,
                "default": True,
            },
        },
    },
    (2007, 4): {
        "alias": "DisplayFlashingMessage",
        "docstring": """
            Displays a flashing messages at the bottom of the screen that does not block player input.
        """,
        "args": {
            "text": NO_DEFAULT(EventTextTyping) | HIDE_NAME,
        },
    },
    (2007, 9): {
        "alias": "DisplayFullScreenMessage",
        "docstring": "TODO",
        "args": {
            "text": NO_DEFAULT(EventTextTyping),
        },
    },
    (2008, 1): {
        "alias": "ChangeCamera",
        "docstring": "TODO",
        "args": {
            "normal_camera_id": INT | {"internal_default": -1},
            "locked_camera_id": INT | {"internal_default": -1},
        },
    },
    (2008, 2): {
        "alias": "SetCameraVibration",
        "docstring": "TODO",
        "args": {
            "vibration_id": INT,
            "anchor_type": AUTO_COORD_ENTITY_TYPE("anchor_entity"),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping),
            "dummy_id": DUMMY_ID,
            "decay_start_distance": {
                "type": float,
                "default": 999.0,
            },
            "decay_end_distance": {
                "type": float,
                "default": 999.0,
            },
        },
        "evs_args": {
            "vibration_id": {},
            "anchor_entity": {},
            "dummy_id": {},
            "decay_start_distance": {},
            "decay_end_distance": {},
            "anchor_type": {},
        },
    },
    (2008, 3): {
        "alias": "SetLockedCameraSlot",
        "docstring": """
            Switch between one of two camera slots associated with the player's current collision in the MSB.
            
            Applies to area and block, not specific map CC/DD values.
        """,
        "args": {
            "area_id": INT,
            "block_id": INT,
            "camera_slot": INT,
        },
    },
    (2009, 0): {
        "alias": "RegisterLadder",
        "docstring": """
            Don't mess with these flags, generally; you can just delay when this is called after map load to disable
            certain ladders (which is kind of weird anyway).
        """,
        "args": {
            "start_climbing_flag": FLAG,
            "stop_climbing_flag": FLAG,
            "asset": NO_DEFAULT(AssetTyping),
        },
    },
    (2009, 3): {
        "alias": "RegisterGrace",
        "docstring": """
            Register a Site of Grace, which creates the VFX and allows you to interact with it via the MSB character 
            with ID `(asset + 1000)`.

            I believe the grace flag tells the game where to keep track of its kindle level, or something like that. I
            don't recommend messing around with this much. The reaction distance, angle, and initial kindle level are 
            all set to their standard defaults.

            You can also use `enemy_block_distance` to set the minimum distance that enemies must be at to allow the
            Grace to be interacted with. 
        """,
        "args": {
            "grace_flag": FLAG,
            "asset": NO_DEFAULT(AssetTyping),
            "reaction_distance": {
                "type": float,
                "default": 0.0,
            },
            "reaction_angle": {
                "type": float,
                "default": 0.0,
            },
            "initial_kindle_level": INT | {"default": 0},
            "enemy_block_distance": FLOAT | {"default": 5.0},
        },
    },
    (2009, 4): {
        "alias": "ActivateMultiplayerBuffs",
        "docstring": """
            Used to strengthen bosses based on the number of summons you have. Not sure if it works for every NPC. It
            could also be tied to certain special effects; haven't checked that yet.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
        },
    },
    (2009, 6): {
        "alias": "NotifyBossBattleStart",
        "docstring": "Sends the message to all summons that the host has challenged the boss.",
        "args": {
            "dummy": INT | {"default": 0},
        },
    },
    (2010, 2): {
        "alias": "PlaySoundEffect",
        "docstring": "Anchor entity determines sound position and the sound type is used to look up the source.",
        "args": {
            "anchor_entity": NO_DEFAULT(CoordEntityTyping) | HIDE_NAME,
            "sound_type": {
                "type": SoundType,
                "default": lambda args: args["sound_id"].get_sound_enum(),
            },
            "sound_id": INT | HIDE_NAME,
        },
        "evs_args": {
            "anchor_entity": {},
            "sound_id": {},
            "sound_type": {},
        },
    },
    (2011, 1): {
        "alias": "SetMapCollisionState",
        "docstring": """
            Enable or disable a map collision (HKX). The ID is specified in the MSB. Note that a Collision doesn't have 
            to be solid ground, but could be anything triggered by collision, such as a kill plane (which this is often 
            used to disable).
        """,
        "args": {
            "collision": NO_DEFAULT(CollisionTyping),
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableMapCollision": dict(state=True),
            "DisableMapCollision": dict(state=False),
        },
    },
    (2011, 2): {
        "alias": "SetMapCollisionBackreadMaskState",
        "docstring": """
            Unused.
        """,
        "args": {
            "collision": NO_DEFAULT(CollisionTyping),
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableMapCollisionBackreadMask": dict(state=True),
            "DisableMapCollisionBackreadMask": dict(state=False),
        },
    },
    (2012, 1): {
        "alias": "SetMapPieceState",
        "docstring": """
            Set the visibility of individual map pieces (e.g. all the crystals in Seath's tower).
        """,
        "args": {
            "map_piece_id": NO_DEFAULT(MapPieceTyping),
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableMapPiece": dict(state=True),
            "DisableMapPiece": dict(state=False),
        },
    },

    # NEW

    (0, 2): {
        "alias": "IfUnsignedComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "left": INT,
            "right": INT,
        },
        "partials": {
            "IfUnsignedEqual": dict(comparison_type=ComparisonType.Equal),
            "IfUnsignedNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfUnsignedGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfUnsignedLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfUnsignedGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfUnsignedLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },

    (3, 23): {
        "alias": "IfAttackedWithDamageType",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "attacked_entity": NO_DEFAULT(CharacterTyping),
            "attacker": {
                "type": CharacterTyping,
                "default": 0,
                "internal_default": 0,
            },
            "damage_type": {
                "type": DamageType,
                "default": DamageType.Unspecified,
            },
        }
    },
    (3, 24): {
        "alias": "IfActionButtonParamActivated",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "action_button_id": INT | {"internal_default": -1},
            "entity": NO_DEFAULT(CoordEntityTyping) | {"internal_default": 2 ** 32 - 1},
        },
    },

    (3, 26): {
        "alias": "IfPlayerOwnWorldState",
        "docstring": """
            Excluding Arena.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "not_in_own_world": BOOL,
        },
        "partials": {
            "IfPlayerInOwnWorld": dict(not_in_own_world=False),
            "IfPlayerNotInOwnWorld": dict(not_in_own_world=True),
        },
    },
    (3, 30): {
        "alias": "IfMapLoaded",
        "docstring": """
            Only used in Radahn fight, I believe, with map tiles.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "condition": {},
            "game_map": GAME_MAP_EVS,
        },
    },
    (3, 31): {
        "alias": "IfWeatherState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "weather": NO_DEFAULT(Weather),
            "unk_4_8": FLOAT,
            "unk_8_12": FLOAT,
        },
    },
    (3, 32): {
        "alias": "IfMapUpdatePermissionState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL,
            "unk_state": BOOL,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "condition": {},
            "state": {},
            "unk_state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "IfMapHasUpdatePermission": dict(state=True),
            "IfMapDoesNotHaveUpdatePermission": dict(state=False),
        }
    },
    (3, 33): {
        "alias": "IfFieldBattleMusicState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "npc_threat_level": INT,
            "state": BOOL,
        },
        "partials": {
            "IfFieldBattleMusicEnabled": dict(state=True),
            "IfFieldBattleMusicDisabled": dict(state=False),
        },
    },
    (3, 34): {
        "alias": "IfPlayerHasArmorEquipped",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "armor_type": NO_DEFAULT(ArmorType),
            "armor": NO_DEFAULT(ArmorTyping),
            "unk_8_12": INT | {"default": -1},
        },
        "partials": {
            "IfPlayerHasHeadArmorEquipped": dict(armor_type=ArmorType.Head),
            "IfPlayerHasBodyArmorEquipped": dict(armor_type=ArmorType.Body),
            "IfPlayerHasArmsArmorEquipped": dict(armor_type=ArmorType.Arms),
            "IfPlayerHasLegsArmorEquipped": dict(armor_type=ArmorType.Legs),
        },
    },
    (3, 35): {
        "alias": "IfCeremonyState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL,
            "ceremony": INT,
        },
        "partials": {
            "IfCeremonyActive": dict(state=True),
            "IfCeremonyInactive": dict(state=False),
        },
    },
    (3, 37): {
        "alias": "IfWeatherLotState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "weather_lot_param_id": INT,
            "state": BOOL,
        },
        "partials": {
            "IfWeatherLotActive": dict(state=True),
            "IfWeatherLotInactive": dict(state=False),
        },
    },
    (3, 38): {
        "alias": "IfPlayerGender",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "gender": NO_DEFAULT(Gender),
        },
    },
    # Arena (Colosseum) instructions added in patch 1.08:
    (3, 39): {
        "alias": "IfArenaMatchReadyState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "ready": BOOL,
        },
    },
    (3, 40): {
        "alias": "IfArenaSoloResult",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "result": NO_DEFAULT(ArenaResult),
        },
    },
    (3, 41): {
        "alias": "IfArenaSoloScoreComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "score": INT,
        },
    },
    (3, 42): {
        "alias": "IfArenaTeamResults",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "result": NO_DEFAULT(ArenaResult),
        },
    },
    (3, 43): {
        "alias": "IfArenaTeamScoreComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "score": INT,
        },
    },
    (3, 44): {
        "alias": "IfArenaMatchType",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "match_type": NO_DEFAULT(ArenaMatchType),
            "has_spirit_summon": BOOL,
        },
    },
    (3, 45): {
        "alias": "IfPlayerRespawnedInArena",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
        },
    },
    
    (4, 15): {
        "alias": "IfCharacterProportionDeathState",
        "docstring": """
            Checks if a proportion (0-1) of given characters (group entity ID) are dead or alive.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_proportion": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterProportionDead": dict(state=True),
            "IfCharacterProportionAlive": dict(state=False),
        },
    },
    (4, 19): {
        "alias": "IfCharacterProportionSpecialEffectState",
        "docstring": """
            Checks if a certain proportion of the given characters (group entity ID) have or do not have a given
            special effect, rather than a certain absolute count.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character_group": NO_DEFAULT(CharacterTyping),
            "special_effect": INT,
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_proportion": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterProportionHasSpecialEffect": dict(state=True),
            "IfCharacterProportionDoesNotHaveSpecialEffect": dict(state=False),
        },
    },
    (4, 28): {
        "alias": "IfPlayerTargeted",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "min_npc_threat_level": INT,
            "max_npc_threat_level": INT,
            "ai_status": NO_DEFAULT(AIStatusType),
        },
    },
    (4, 30): {
        "alias": "IfNPCPartAttackedWithDamageType",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "npc_part_id": INT,
            "attacker": NO_DEFAULT(CharacterTyping) | {"default": 0},
            "damage_type": NO_DEFAULT(DamageType) | {"default": DamageType.Unspecified},
        },
    },
    (4, 31): {
        "alias": "IfCharacterInvadeType",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "invade_type": NO_DEFAULT(CharacterType),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
    },
    (4, 32): {
        "alias": "IfCharacterMountState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "is_mounted": BOOL,
        },
        "partials": {
            "IfCharacterMounted": dict(is_mounted=True),
            "IfCharacterNotMounted": dict(is_mounted=False),
        },
    },
    (4, 34): {
        "alias": "IfCharacterStateInfoState",
        "docstring": "Checks if character has or does not have the given `state_info` (from a SpEffect).",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "state_info": INT,
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterHasStateInfo": dict(state=True),
            "IfCharacterDoesNotHaveStateInfo": dict(state=False),
        },
    },
    (4, 35): {
        "alias": "IfSpecialStandbyEndedFlagState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
        "partials": {
            "IfSpecialStandbyEndedFlagEnabled": dict(state=True),
            "IfSpecialStandbyEndedFlagDisabled": dict(state=False),
        },
    },

    (5, 6): {
        "alias": "IfAssetProportionDestructionState",
        "docstring": "Check if a certain proportion of given assets (group entity ID) have or have not been destroyed.",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL,
            "asset_group": NO_DEFAULT(AssetTyping),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_proportion": TARGET_COUNT_FLOAT,
        },
    },
    (5, 10): {
        "alias": "IfAssetBackreadState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping),
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfAssetBackreadEnabled": dict(state=True),
            "IfAssetBackreadDisabled": dict(state=False),
        },
    },

    (1000, 10): {
        "alias": "SkipLinesIfUnsignedComparison",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "left": INT,
            "right": INT,
        },
        "partials": {
            "SkipLinesIfUnsignedEqual": dict(comparison_type=ComparisonType.Equal),
            "SkipLinesIfUnsignedNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "SkipLinesIfUnsignedGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "SkipLinesIfUnsignedLessThan": dict(comparison_type=ComparisonType.LessThan),
            "SkipLinesIfUnsignedGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "SkipLinesIfUnsignedLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (1000, 11): {
        "alias": "ReturnIfUnsignedComparison",
        "docstring": "TODO",
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
            "comparison_type": NO_DEFAULT(ComparisonType),
            "left": INT,
            "right": INT,
        },
        "partials": {
            "EndIfUnsignedEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.Equal,
            ),
            "EndIfUnsignedNotEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.NotEqual,
            ),
            "EndIfUnsignedGreaterThan": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.GreaterThan,
            ),
            "EndIfUnsignedLessThan": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.LessThan,
            ),
            "EndIfUnsignedGreaterThanOrEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.GreaterThanOrEqual,
            ),
            "EndIfUnsignedLessThanOrEqual": dict(
                event_return_type=EventReturnType.End,
                comparison_type=ComparisonType.LessThanOrEqual,
            ),
            "RestartIfUnsignedEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.Equal,
            ),
            "RestartIfUnsignedNotEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.NotEqual,
            ),
            "RestartIfUnsignedGreaterThan": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.GreaterThan,
            ),
            "RestartIfUnsignedLessThan": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.LessThan,
            ),
            "RestartIfUnsignedGreaterThanOrEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.GreaterThanOrEqual,
            ),
            "RestartIfUnsignedLessThanOrEqual": dict(
                event_return_type=EventReturnType.Restart,
                comparison_type=ComparisonType.LessThanOrEqual,
            ),
        },
    },
    (1000, 101): {
        "alias": "GotoIfConditionState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "required_state": BOOL,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "GotoIfConditionTrue": dict(required_state=True),
            "GotoIfConditionFalse": dict(required_state=False),
        },
        "get_evaluated_conditions": lambda kwargs: {kwargs["input_condition"]},
    },
    (1000, 103): {
        "alias": "Goto",
        "docstring": """
            Unconditional GOTO.
        """,
        "args": {
            "label": LABEL,
        },
    },
    (1000, 105): {
        "alias": "GotoIfValueComparison",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "left": INT,
            "right": INT,
        },
    },
    (1000, 107): {
        "alias": "GotoIfLastConditionResultState",
        "docstring": """
            Go to label if the last result of the given condition (without re-evaluating) is `required_state`.
        """,
        "args": {
            "label": LABEL,
            "required_state": BOOL,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "GotoIfLastConditionResultTrue": dict(required_state=True),
            "GotoIfLastConditionResultFalse": dict(required_state=False),
        }
    },
    (1000, 108): {
        "alias": "GotoIfUnsignedComparison",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "left": INT,
            "right": INT,
        },
        "partials": {
            "GotoIfUnsignedEqual": dict(comparison_type=ComparisonType.Equal),
            "GotoIfUnsignedNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "GotoIfUnsignedGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "GotoIfUnsignedLessThan": dict(comparison_type=ComparisonType.LessThan),
            "GotoIfUnsignedGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "GotoIfUnsignedLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (1001, 5): {
        "alias": "WaitUntilTimeOfDayInRange",
        "docstring": "Pause event script until time of day is between the given earliest/latest times.",
        "args": {
            "earliest_hour": {
                "type": int,
                "default": None,
                "from_evs": lambda args: args["earliest"][0],
            },
            "earliest_minute": {
                "type": int,
                "default": None,
                "from_evs": lambda args: args["earliest"][1],
            },
            "earliest_second": {
                "type": int,
                "default": None,
                "from_evs": lambda args: args["earliest"][2],
            },
            "latest_hour": {
                "type": int,
                "default": None,
                "from_evs": lambda args: args["latest"][0],
            },
            "latest_minute": {
                "type": int,
                "default": None,
                "from_evs": lambda args: args["latest"][1],
            },
            "latest_second": {
                "type": int,
                "default": None,
                "from_evs": lambda args: args["latest"][2],
            },
        },
        "evs_args": {
            "earliest": {
                "type": tuple,
                "default": None,
                "to_evs": lambda args: (args["earliest_hour"], args["earliest_minute"], args["earliest_second"]),
            },
            "latest": {
                "type": tuple,
                "default": None,
                "to_evs": lambda args: (args["latest_hour"], args["latest_minute"], args["latest_second"]),
            },
        },
    },
    (1001, 6): {
        "alias": "WaitRealFrames",
        "docstring": """
            Wait a given number of real frames. Always used after cutscene instructions with argument `frames=1`.
        """,
        "args": {
            "frames": INT,
        },
    },
    (1001, 8): {
        "alias": "WaitUntilArenaHalfTime",
        "docstring": "TODO",
        "args": {
            "match_type": NO_DEFAULT(ArenaMatchType),
            "is_second_half": BOOL,
        },
    },
    (1003, 5): {
        "alias": "SkipLinesIfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": NO_DEFAULT(MultiplayerState),
        },
        "partials": {
            "SkipLinesIfHost": dict(state=MultiplayerState.Host),
            "SkipLinesIfClient": dict(state=MultiplayerState.Client),
            "SkipLinesIfMultiplayer": dict(state=MultiplayerState.Multiplayer),
            "SkipLinesIfMultiplayerPending": dict(state=MultiplayerState.MultiplayerPending),
            "SkipLinesIfSingleplayer": dict(state=MultiplayerState.Singleplayer),
            "SkipLinesIfInvasion": dict(state=MultiplayerState.Invasion),
            "SkipLinesIfInvasionPending": dict(state=MultiplayerState.InvasionPending),
        },
    },
    (1003, 6): {
        "alias": "ReturnIfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": NO_DEFAULT(MultiplayerState),
        },
        "partials": {
            "EndIfHost": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.Host,
            ),
            "EndIfClient": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.Client,
            ),
            "EndIfMultiplayer": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.Multiplayer,
            ),
            "EndIfMultiplayerPending": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.MultiplayerPending,
            ),
            "EndIfSingleplayer": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.Singleplayer,
            ),
            "EndIfInvasion": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.Invasion,
            ),
            "EndIfInvasionPending": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.InvasionPending,
            ),
            "RestartIfHost": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Host,
            ),
            "RestartIfClient": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Client,
            ),
            "RestartIfMultiplayer": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Multiplayer,
            ),
            "RestartIfMultiplayerPending": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.MultiplayerPending,
            ),
            "RestartIfSingleplayer": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Singleplayer,
            ),
            "RestartIfInvasion": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Invasion,
            ),
            "RestartIfInvasionPending": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.InvasionPending,
            ),
        },
    },
    (1003, 9): {
        "alias": "SkipLinesIfCoopClientCountComparison",
        "docstring": """
            Value should be from 0 to 4.
        """,
        "args": {
            "skip_lines": INT | HIDE_NAME,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "value": INT,
        },
    },
    (1003, 10): {
        "alias": "ReturnIfCoopClientCountComparison",
        "docstring": "TODO",
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
            "comparison_type": NO_DEFAULT(ComparisonType),
            "value": INT,
        },
        "partials": {
            "EndIfCoopClientCountComparison": dict(event_return_type=EventReturnType.End),
            "RestartIfCoopClientCountComparison": dict(event_return_type=EventReturnType.Restart),
        },
    },
    (1003, 12): {
        "alias": "SkipLinesIfPlayerOwnWorldState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "not_in_own_world": BOOL,
        },
        "partials": {
            "SkipLinesIfPlayerInOwnWorld": dict(not_in_own_world=False),
            "SkipLinesIfPlayerNotInOwnWorld": dict(not_in_own_world=True),
        },
    },
    (1003, 13): {
        "alias": "GotoIfPlayerOwnWorldState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "not_in_own_world": BOOL,
        },
        "partials": {
            "GotoIfPlayerInOwnWorld": dict(not_in_own_world=False),
            "GotoIfPlayerNotInOwnWorld": dict(not_in_own_world=True),
        },
    },
    (1003, 14): {
        "alias": "ReturnIfPlayerOwnWorldState",
        "docstring": "TODO",
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
            "not_in_own_world": BOOL,
        },
        "partials": {
            "EndIfPlayerInOwnWorld": dict(event_return_type=EventReturnType.End, not_in_own_world=False),
            "EndIfPlayerNotInOwnWorld": dict(event_return_type=EventReturnType.End, not_in_own_world=True),
            "RestartIfPlayerInOwnWorld": dict(event_return_type=EventReturnType.Restart, not_in_own_world=False),
            "RestartIfPlayerNotInOwnWorld": dict(event_return_type=EventReturnType.Restart, not_in_own_world=True),
        },
    },
    (1003, 101): {
        "alias": "GotoIfFlagState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "state": BOOL,
            "flag_type": NO_DEFAULT(FlagType),
            "flag": NO_DEFAULT(FlagTyping),
        },
        "partials": {
            "GotoIfThisEventFlagEnabled": dict(
                state=True,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "GotoIfThisEventFlagDisabled": dict(
                state=False,
                flag_type=FlagType.RelativeToThisEvent,
                flag=0,
            ),
            "GotoIfThisEventSlotFlagEnabled": dict(
                state=True,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
            "GotoIfThisEventSlotFlagDisabled": dict(
                state=False,
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
            ),
            "GotoIfFlagEnabled": dict(
                state=True,
                flag_type=FlagType.Absolute,
            ),
            "GotoIfFlagDisabled": dict(
                state=False,
                flag_type=FlagType.Absolute,
            ),
        },
    },
    (1003, 103): {
        "alias": "GotoIfFlagRangeState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "state": NO_DEFAULT(RangeState) | HIDE_NAME,
            "flag_type": NO_DEFAULT(FlagType) | HIDE_NAME,
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
        },
        "evs_args": {
            "label": {},
            "state": {},
            "flag_type": {},
            "flag_range": FLAG_RANGE,
        },
        "partials": {
            "GotoIfFlagRangeAllEnabled": dict(state=RangeState.AllOn, flag_type=FlagType.Absolute),
            "GotoIfFlagRangeAllDisabled": dict(state=RangeState.AllOff, flag_type=FlagType.Absolute),
            "GotoIfFlagRangeAnyEnabled": dict(state=RangeState.AnyOn, flag_type=FlagType.Absolute),
            "GotoIfFlagRangeAnyDisabled": dict(state=RangeState.AnyOff, flag_type=FlagType.Absolute),
        },
    },
    (1003, 105): {
        "alias": "GotoIfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "state": NO_DEFAULT(MultiplayerState),
        },
        "partials": {
            "GotoIfHost": dict(state=MultiplayerState.Host),
            "GotoIfClient": dict(state=MultiplayerState.Client),
            "GotoIfMultiplayer": dict(state=MultiplayerState.Multiplayer),
            "GotoIfMultiplayerPending": dict(state=MultiplayerState.MultiplayerPending),
            "GotoIfSingleplayer": dict(state=MultiplayerState.Singleplayer),
            "GotoIfInvasion": dict(state=MultiplayerState.Invasion),
            "GotoIfInvasionPending": dict(state=MultiplayerState.InvasionPending),
        },
    },
    (1003, 107): {
        "alias": "GotoIfMapPresenceState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "state": BOOL,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "label": {},
            "state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "GotoIfInsideMap": dict(state=True),
            "GotoIfOutsideMap": dict(state=False),
        },
    },
    (1003, 109): {
        "alias": "GotoIfCoopClientCountComparison",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "value": INT,
        },
    },
    (1003, 200): {
        "alias": "GotoIfCharacterRegionState",
        "docstring": """
            EMEDF does not have the final new argument listed (it's the same as the other region/distance checks).
        """,
        "args": {
            "label": LABEL,
            "state": BOOL,
            "character": NO_DEFAULT(CharacterTyping),
            "region": NO_DEFAULT(RegionTyping),
            "min_target_count": MIN_TARGET_COUNT_INT,
        },
        "partials": {
            "GotoIfPlayerInsideRegion": dict(character=PLAYER, state=True),
            "GotoIfPlayerOutsideRegion": dict(character=PLAYER, state=False),
            "GotoIfCharacterInsideRegion": dict(state=True),
            "GotoIfCharacterOutsideRegion": dict(state=False),
        },
    },
    (1003, 201): {
        "alias": "ReturnIfCharacterRegionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
            "state": BOOL,
            "character": NO_DEFAULT(CharacterTyping),
            "region": NO_DEFAULT(RegionTyping),
            "min_target_count": MIN_TARGET_COUNT_INT,
        },
        "partials": {
            "EndIfPlayerInsideRegion": dict(
                event_return_type=EventReturnType.End, character=PLAYER, state=True
            ),
            "EndIfPlayerOutsideRegion": dict(
                event_return_type=EventReturnType.End, character=PLAYER, state=False
            ),
            "RestartIfPlayerInsideRegion": dict(
                event_return_type=EventReturnType.Restart, character=PLAYER, state=True
            ),
            "RestartIfPlayerOutsideRegion": dict(
                event_return_type=EventReturnType.Restart, character=PLAYER, state=False
            ),
            "EndIfCharacterInsideRegion": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfCharacterOutsideRegion": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfCharacterInsideRegion": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfCharacterOutsideRegion": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1003, 202): {
        "alias": "SkipLinesIfCharacterRegionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL,
            "character": NO_DEFAULT(CharacterTyping),
            "region": NO_DEFAULT(RegionTyping),
            "min_target_count": MIN_TARGET_COUNT_INT,
        },
        "partials": {
            "SkipLinesIfPlayerInsideRegion": dict(state=True, character=PLAYER),
            "SkipLinesIfPlayerOutsideRegion": dict(state=False, character=PLAYER),
            "SkipLinesIfCharacterInsideRegion": dict(state=True),
            "SkipLinesIfCharacterOutsideRegion": dict(state=False),
        },
    },
    (1003, 203): {
        "alias": "SkipLinesIfMapUpdatePermissionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL,
            "unk_state": BOOL,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "line_count": {},
            "state": {},
            "unk_state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "SkipLinesIfMapHasUpdatePermission": dict(state=True),
            "SkipLinesIfMapDoesNotHaveUpdatePermission": dict(state=False),
        },
    },
    (1003, 204): {
        "alias": "GotoIfMapUpdatePermissionState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "state": BOOL,
            "unk_state": BOOL,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "label": {},
            "state": {},
            "unk_state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "GotoIfMapHasUpdatePermission": dict(state=True),
            "GotoIfMapDoesNotHaveUpdatePermission": dict(state=False),
        }
    },
    (1003, 205): {
        "alias": "ReturnIfMapUpdatePermissionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL,
            "unk_state": BOOL,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
        },
        "evs_args": {
            "event_return_type": {},
            "state": {},
            "unk_state": {},
            "game_map": GAME_MAP_EVS,
        },
        "partials": {
            "EndIfMapHasUpdatePermission": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfMapDoesNotHaveUpdatePermission": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfMapHasUpdatePermission": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfMapDoesNotHaveUpdatePermission": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1003, 206): {
        "alias": "SkipLinesIfCeremonyState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL,
            "ceremony": INT,
        },
        "partials": {
            "SkipLinesIfCeremonyActive": dict(state=True),
            "SkipLinesIfCeremonyInactive": dict(state=False),
        },
    },
    (1003, 207): {
        "alias": "GotoIfCeremonyState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "state": BOOL,
            "ceremony": INT,
        },
        "partials": {
            "GotoIfCeremonyActive": dict(state=True),
            "GotoIfCeremonyInactive": dict(state=False),
        },
    },
    (1003, 208): {
        "alias": "ReturnIfCeremonyState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL,
            "ceremony": INT,
        },
        "partials": {
            "EndIfCeremonyActive": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfCeremonyInactive": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfCeremonyActive": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfCeremonyInactive": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1003, 212): {
        "alias": "SkipLinesIfArenaMatchType",
        "docstring": "Skip some number of lines if the current arena match type is the given type.",
        "args": {
            "line_count": INT | HIDE_NAME,
            "match_type": NO_DEFAULT(ArenaMatchType),
            "has_spirit_summon": BOOL,
        },
    },
    (1003, 213): {
        "alias": "GotoLinesIfArenaMatchType",
        "docstring": "Go to label if the current arena match type is the given type.",
        "args": {
            "label": LABEL,
            "match_type": NO_DEFAULT(ArenaMatchType),
            "has_spirit_summon": BOOL,
        },
    },
    (1003, 214): {
        "alias": "ReturnIfArenaMatchType",
        "docstring": "End or restart if the current arena match type is the given type.",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "match_type": NO_DEFAULT(ArenaMatchType),
            "has_spirit_summon": BOOL,
        },
        "partials": {
            "EndIfArenaMatchType": dict(event_return_type=EventReturnType.End),
            "RestartIfArenaMatchType": dict(event_return_type=EventReturnType.Restart),
        },
    },
    (1004, 0): {
        "alias": "SkipLinesIfCharacterSpecialEffectState",
        "docstring": "Note that the same instruction appeared in DS3 as 1003[112].",
        "args": {
            "line_count": INT | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "special_effect": SPECIAL_EFFECT,
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_INT,
        },
        "partials": {
            "SkipLinesIfPlayerHasSpecialEffect": dict(character=PLAYER, state=True),
            "SkipLinesIfPlayerDoesNotHaveSpecialEffect": dict(character=PLAYER, state=False),
            "SkipLinesIfCharacterHasSpecialEffect": dict(state=True),
            "SkipLinesIfCharacterDoesNotHaveSpecialEffect": dict(state=False),
        },
    },
    (1004, 1): {
        "alias": "GotoIfCharacterSpecialEffectState",
        "docstring": "Note that the same instruction appeared in DS3 as 1003[11].",
        "args": {
            "label": LABEL,
            "character": NO_DEFAULT(CharacterTyping),
            "special_effect": INT,
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_INT,
        },
        "partials": {
            "GotoIfPlayerHasSpecialEffect": dict(character=PLAYER, state=True),
            "GotoIfPlayerDoesNotHaveSpecialEffect": dict(character=PLAYER, state=False),
            "GotoIfCharacterHasSpecialEffect": dict(state=True),
            "GotoIfCharacterDoesNotHaveSpecialEffect": dict(state=False),
        },
    },
    (1004, 2): {
        "alias": "ReturnIfCharacterSpecialEffectState",
        "docstring": "Note that the same instruction appeared in DS3 as 1003[111].",
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
            "character": NO_DEFAULT(CharacterTyping),
            "special_effect": INT,
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_INT,
        },
        "partials": {
            "EndIfPlayerHasSpecialEffect": dict(
                event_return_type=EventReturnType.End, character=PLAYER, state=True
            ),
            "EndIfPlayerDoesNotHaveSpecialEffect": dict(
                event_return_type=EventReturnType.End, character=PLAYER, state=False
            ),
            "RestartIfPlayerHasSpecialEffect": dict(
                event_return_type=EventReturnType.Restart, character=PLAYER, state=True
            ),
            "RestartIfPlayerDoesNotHaveSpecialEffect": dict(
                event_return_type=EventReturnType.Restart, character=PLAYER, state=False
            ),
            "EndIfCharacterHasSpecialEffect": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfCharacterDoesNotHaveSpecialEffect": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfCharacterHasSpecialEffect": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfCharacterDoesNotHaveSpecialEffect": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1004, 3): {
        "alias": "SkipLinesIfSpecialStandbyEndedFlagState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
        "partials": {
            "SkipLinesIfSpecialStandbyEndedFlagEnabled": dict(state=True),
            "SkipLinesIfSpecialStandbyEndedFlagDisabled": dict(state=False),
        },
    },
    (1004, 4): {
        "alias": "GotoIfSpecialStandbyEndedFlagState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
        "partials": {
            "GotoIfSpecialStandbyEndedFlagEnabled": dict(state=True),
            "GotoIfSpecialStandbyEndedFlagDisabled": dict(state=False),
        },
    },
    (1004, 5): {
        "alias": "ReturnIfSpecialStandbyEndedFlagState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
        "partials": {
            "EndIffSpecialStandbyEndedFlagEnabled": dict(event_return_type=EventReturnType.End, state=True),
            "EndIffSpecialStandbyEndedFlagDisabled": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIffSpecialStandbyEndedFlagEnabled": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIffSpecialStandbyEndedFlagDisabled": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },

    (1005, 0): {
        "alias": "AwaitAssetDestrucionState",
        "docstring": "TODO",
        "args": {
            "state": BOOL | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "AwaitAssetDestroyed": dict(state=True),
            "AwaitAssetNotDestroyed": dict(state=False),
        },
    },
    (1005, 1): {
        "alias": "SkipLinesIfAssetDestructionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "SkipLinesIfAssetDestroyed": dict(state=True),
            "SkipLinesIfAssetNotDestroyed": dict(state=False),
        },
    },
    (1005, 2): {
        "alias": "ReturnIfAssetDestructionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "asset": NO_DEFAULT(AssetTyping) | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "EndIfAssetDestroyed": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfAssetNotDestroyed": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfAssetDestroyed": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfAssetNotDestroyed": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1005, 101): {
        "alias": "GotoIfAssetDestructionState",
        "docstring": """
            Note change in argument order.
        """,
        "args": {
            "label": LABEL,
            "state": BOOL,
            "asset": NO_DEFAULT(AssetTyping),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "GotoIfAssetDestroyed": dict(state=True),
            "GotoIfAssetNotDestroyed": dict(state=False),
        },
    },
    # All of these `DefineLabel_label()` variants can be generated from custom wrapper `DefineLabel(label)`.
    (1014, 0): {
        "alias": "DefineLabel_0",
        "docstring": "Define position of label 0 for Goto instructions.",
        "args": {},
    },
    (1014, 1): {
        "alias": "DefineLabel_1",
        "docstring": "Define position of label 1 for Goto instructions.",
        "args": {},
    },
    (1014, 2): {
        "alias": "DefineLabel_2",
        "docstring": "Define position of label 2 for Goto instructions.",
        "args": {},
    },
    (1014, 3): {
        "alias": "DefineLabel_3",
        "docstring": "Define position of label 3 for Goto instructions.",
        "args": {},
    },
    (1014, 4): {
        "alias": "DefineLabel_4",
        "docstring": "Define position of label 4 for Goto instructions.",
        "args": {},
    },
    (1014, 5): {
        "alias": "DefineLabel_5",
        "docstring": "Define position of label 5 for Goto instructions.",
        "args": {},
    },
    (1014, 6): {
        "alias": "DefineLabel_6",
        "docstring": "Define position of label 6 for Goto instructions.",
        "args": {},
    },
    (1014, 7): {
        "alias": "DefineLabel_7",
        "docstring": "Define position of label 7 for Goto instructions.",
        "args": {},
    },
    (1014, 8): {
        "alias": "DefineLabel_8",
        "docstring": "Define position of label 8 for Goto instructions.",
        "args": {},
    },
    (1014, 9): {
        "alias": "DefineLabel_9",
        "docstring": "Define position of label 9 for Goto instructions.",
        "args": {},
    },
    (1014, 10): {
        "alias": "DefineLabel_10",
        "docstring": "Define position of label 10 for Goto instructions.",
        "args": {},
    },
    (1014, 11): {
        "alias": "DefineLabel_11",
        "docstring": "Define position of label 11 for Goto instructions.",
        "args": {},
    },
    (1014, 12): {
        "alias": "DefineLabel_12",
        "docstring": "Define position of label 12 for Goto instructions.",
        "args": {},
    },
    (1014, 13): {
        "alias": "DefineLabel_13",
        "docstring": "Define position of label 13 for Goto instructions.",
        "args": {},
    },
    (1014, 14): {
        "alias": "DefineLabel_14",
        "docstring": "Define position of label 14 for Goto instructions.",
        "args": {},
    },
    (1014, 15): {
        "alias": "DefineLabel_15",
        "docstring": "Define position of label 15 for Goto instructions.",
        "args": {},
    },
    (1014, 16): {
        "alias": "DefineLabel_16",
        "docstring": "Define position of label 16 for Goto instructions.",
        "args": {},
    },
    (1014, 17): {
        "alias": "DefineLabel_17",
        "docstring": "Define position of label 17 for Goto instructions.",
        "args": {},
    },
    (1014, 18): {
        "alias": "DefineLabel_18",
        "docstring": "Define position of label 18 for Goto instructions.",
        "args": {},
    },
    (1014, 19): {
        "alias": "DefineLabel_19",
        "docstring": "Define position of label 19 for Goto instructions.",
        "args": {},
    },
    (1014, 20): {
        "alias": "DefineLabel_20",
        "docstring": "Define position of label 20 for Goto instructions.",
        "args": {},
    },

    (2001, 4): {
        "alias": "SetCurrentTime",
        "docstring": "TODO",
        "args": {
            "hour": HOUR,
            "minute": MINUTE,
            "second": SECOND,
            "fade_transition": BOOL,
            "wait_for_completion": BOOL,
            "show_clock": BOOL,
            "clock_start_delay": FLOAT,
            "clock_change_duration": FLOAT,
            "clock_finish_delay": FLOAT,
        },
        "evs_args": {
            "time": TIME_EVS,
            "fade_transition": {},
            "wait_for_completion": {},
            "show_clock": {},
            "clock_start_delay": {},
            "clock_change_duration": {},
            "clock_finish_delay": {},
        },
    },
    (2001, 5): {
        "alias": "SetTimeFreezeState",
        "docstring": "TODO",
        "args": {
            "state": BOOL,
        },
        "partials": {
            "FreezeTime": dict(state=True),
            "UnfreezeTime": dict(state=False),
        },
    },

    (2002, 10): {
        "alias": "PlayCutsceneToPlayerWithWeatherAndTime",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "player_id": INT | {"internal_default": -1},
            "change_weather": BOOL | {"default": False},
            "weather": NO_DEFAULT(Weather) | {"default": 0},
            "weather_duration": FLOAT | {"default": -1.0},
            "change_time": BOOL | {"default": False},
            "hour": HOUR,
            "minute": MINUTE,
            "second": SECOND,
        },
        "evs_args": {
            "cutscene_id": {},
            "cutscene_flags": {},
            "player_id": {},
            "change_weather": {},
            "weather": {},
            "weather_duration": {},
            "change_time": {},
            "time": TIME_EVS | {"default": (0, 0, 0)},
        },
    },
    (2002, 11): {
        "alias": "PlayCutsceneToPlayerAndWarp",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "move_to_region": NO_DEFAULT(RegionTyping),  # TODO: can be 0
            "map_id": INT,  # TODO: e.g., 11050000, a 32-bit encoding of m11_05_00_00 (or 0)
            "player_id": INT | {"internal_default": -1},
            "unk_20_24": INT,  # TODO: either 0 or 13000
            "unk_24_25": BOOL,  # TODO: seems to be True with 13000 above
        },
    },
    (2002, 12): {
        "alias": "PlayCutsceneToPlayerAndWarpWithWeatherAndTime",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "move_to_region": NO_DEFAULT(RegionTyping),
            "map_id": INT,
            "player_id": INT | {"internal_default": -1},
            "unk_20_24": INT,
            "unk_24_25": BOOL,
            "change_weather": BOOL,
            "weather": NO_DEFAULT(Weather) | {"default": 0},
            "weather_duration": FLOAT | {"default": -1.0},
            "change_time": BOOL | {"default": False},
            "hour": HOUR,
            "minute": MINUTE,
            "second": SECOND,
        },
        "evs_args": {
            "cutscene_id": {},
            "cutscene_flags": {},
            "move_to_region": {},
            "map_id": {},
            "player_id": {},
            "unk_20_24": {},
            "unk_24_25": {},
            "change_weather": {},
            "weather": {},
            "weather_duration": {},
            "change_time": {},
            "time": TIME_EVS | {"default": (0, 0, 0)},
        },
    },
    (2002, 13): {
        "alias": "PlayCutsceneToPlayerAndWarpWithStablePositionUpdate",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "move_to_region": NO_DEFAULT(RegionTyping),
            "map_id": INT,
            "player_id": INT | {"internal_default": -1},
            "unk_16_20": INT,
            "unk_20_21": BOOL,
            "update_stable_position": BOOL,
        },
    },
    (2003, 41): {
        "alias": "EventValueOperation",
        "docstring": """
            Performs a binary operation on the source flag and operand value, and stores the result in the target flag.
        """,
        "args": {
            "source_flag": NO_DEFAULT(FlagTyping),
            "source_flag_bit_count": INT,
            "operand": INT,
            "target_flag": NO_DEFAULT(FlagTyping),
            "target_flag_bit_count": INT,
            "calculation_type": NO_DEFAULT(CalculationType),
        },
    },
    (2003, 42): {
        "alias": "StoreItemAmountSpecifiedByFlagValue",
        "docstring": """
            Stores some amount of items read from a flag array.
        """,
        "args": {
            "item_type": NO_DEFAULT(ItemType),
            "item": NO_DEFAULT(ItemTyping),
            "flag": NO_DEFAULT(FlagTyping),
            "bit_count": INT,
        },
    },
    (2003, 43): {
        "alias": "GivePlayerItemAmountSpecifiedByFlagValue",
        "docstring": """
            Gives player some amount of items read from a flag array. Probably used when taking items out of storage
            (i.e. the reverse of the above instruction).
        """,
        "args": {
            "item_type": NO_DEFAULT(ItemType),
            "item": NO_DEFAULT(ItemTyping),
            "flag": NO_DEFAULT(FlagTyping),
            "bit_count": INT,
        },
    },
    (2003, 44): {
        "alias": "SetDirectionDisplay",
        "docstring": "TODO",
        "args": {
            "state": BOOL,
        },
        "partials": {
            "EnableDirectionDisplay": dict(state=True),
            "DisableDirectionDisplay": dict(state=False),
        },
    },
    (2003, 52): {
        "alias": "TriggerAISound",
        "docstring": "TODO",
        "args": {
            "ai_sound_param_id": INT,
            "anchor_entity": NO_DEFAULT(CoordEntityTyping),
            "unk_8_12": INT,
        },
    },
    (2003, 54): {
        "alias": "ForceSpawnerToSpawn",
        "docstring": "TODO",
        "args": {
            "spawner": NO_DEFAULT(tp.Union[SpawnerEvent, int]),
        },
    },
    (2003, 63): {
        "alias": "SetNetworkConnectedFlagRangeState",
        "docstring": "Network-synchronized variant of `SetFlagRangeState` (2003[22]).",
        "args": {
            "first_flag": FLAG_RANGE_FIRST,
            "last_flag": FLAG_RANGE_LAST,
            "state": NO_DEFAULT(FlagSetting),
        },
        "evs_args": {
            "flag_range": FLAG_RANGE,
            "state": {},
        },
        "partials": {
            "EnableNetworkConnectedFlagRange": dict(state=FlagSetting.On),
            "DisableNetworkConnectedFlagRange": dict(state=FlagSetting.Off),
            "ToggleNetworkConnectedFlagRange": dict(state=FlagSetting.Change),
        },
    },
    (2003, 64): {
        "alias": "SetOmissionModeCounts",
        "docstring": "TODO",
        "args": {
            "level_1_count": INT,
            "level_2_count": INT,
        },
    },
    (2003, 65): {
        "alias": "ResetOmissionModeCountsToDefault",
        "docstring": "TODO",
        "args": {},
    },
    (2003, 66): {
        "alias": "SetFlagState",
        "docstring": """
            Predominant flag-setting instruction in Elden Ring. It can set relative flags, unlike the old 2003[2].
        """,
        "args": {
            "flag_type": NO_DEFAULT(FlagType) | HIDE_NAME,
            "flag": FLAG | HIDE_NAME,
            "state": FLAG_SETTING,
        },
        "partials": {
            "EnableFlag": dict(flag_type=FlagType.Absolute, state=FlagSetting.On),
            "DisableFlag": dict(flag_type=FlagType.Absolute, state=FlagSetting.Off),
            "ToggleFlag": dict(flag_type=FlagType.Absolute, state=FlagSetting.Change),
            "SetAbsoluteFlagState": dict(flag_type=FlagType.Absolute),
            "EnableThisSlotFlag": dict(flag_type=FlagType.RelativeToThisEventSlot, flag=0, state=FlagSetting.On),
            "DisableThisSlotFlag": dict(flag_type=FlagType.RelativeToThisEventSlot, flag=0, state=FlagSetting.Off),
        },
    },
    (2003, 68): {
        "alias": "SetWeather",
        "docstring": "TODO",
        "args": {
            "weather": NO_DEFAULT(Weather),
            "duration": FLOAT,
            "immediate_change": BOOL,
        },
    },
    (2003, 69): {
        "alias": "SetNetworkFlagState",
        "docstring": """
            Enable, disable, or toggle (change) a binary flag for all network-connected players.
        """,
        "args": {
            "flag_type": NO_DEFAULT(FlagType) | HIDE_NAME,
            "flag": FLAG | HIDE_NAME,
            "state": FLAG_SETTING,
        },
        "partials": {
            "EnableNetworkFlag": dict(flag_type=FlagType.Absolute, state=FlagSetting.On),
            "DisableNetworkFlag": dict(flag_type=FlagType.Absolute, state=FlagSetting.Off),
            "ToggleNetworkFlag": dict(flag_type=FlagType.Absolute, state=FlagSetting.Change),
            "SetAbsoluteNetworkFlagState": dict(flag_type=FlagType.Absolute),
            "EnableThisNetworkFlag": dict(flag_type=FlagType.RelativeToThisEvent, flag=0, state=FlagSetting.On),
            "DisableThisNetworkFlag": dict(flag_type=FlagType.RelativeToThisEvent, flag=0, state=FlagSetting.Off),
            "EnableThisNetworkSlotFlag": dict(flag_type=FlagType.RelativeToThisEventSlot, flag=0, state=FlagSetting.On),
            "DisableThisNetworSlotFlag": dict(
                flag_type=FlagType.RelativeToThisEventSlot,
                flag=0,
                state=FlagSetting.Off,
            ),
        },
    },
    (2003, 70): {
        "alias": "SetNetworkInteractionState",
        "docstring": "TODO",
        "args": {
            "state": BOOL,
        },
    },
    (2003, 71): {
        "alias": "AwardGesture",
        "docstring": "Awards a Gesture item to player.",
        "args": {
            "gesture_param_id": INT,
        },
    },
    (2003, 72): {
        "alias": "MultiplyBloodstainSouls",
        "docstring": """
            Apply a multiplier to the amount of souls/echoes/runes waiting to be retrieved from the bloodstain with
            the given save slot ID. 
            """,
        "args": {
            "multiplier": FLOAT,
            "bloodstain_save_slot_id": INT,  # always 0 or -1
        },
    },
    (2003, 73): {
        "alias": "IncreaseCharacterSoulReward",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "fixed_increase_amount": INT,
            "soul_amount_load_slot_id": INT,
        },
    },
    (2003, 74): {
        "alias": "IssueEndOfPseudoMultiplayerNotification",
        "docstring": "TODO",
        "args": {
            "success": BOOL,
        },
    },
    (2003, 75): {
        "alias": "UseFarViewCamera",
        "docstring": "TODO",
        "args": {
            "far_view_id": INT,
            "asset": NO_DEFAULT(AssetTyping),
            "dummy_id": DUMMY_ID,
        },
    },
    (2003, 76): {
        "alias": "SetPlayerPositionDisplay",
        "docstring": "TODO",
        "args": {
            "state": BOOL,
            "aboveground": BOOL,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "cc_id": CC_ID,
            "dd_id": DD_ID,
            "x": FLOAT,
            "y": FLOAT,
            "z": FLOAT,
        },
        "evs_args": {
            "state": {},
            "aboveground": {},
            "game_map": GAME_MAP_EVS,
            "x": {},
            "y": {},
            "z": {},
        },
    },
    (2003, 77): {
        "alias": "SetPseudoMultiplayerReturnPosition",
        "docstring": "TODO",
        "args": {
            "region": NO_DEFAULT(RegionTyping),
        },
    },
    (2003, 78): {
        "alias": "OpenWorldMapPoint",
        "docstring": "TODO",
        "args": {
            "world_map_point_param_id": INT,
            "distance": FLOAT,
        },
    },
    (2003, 79): {
        "alias": "SendNPCSummonHome",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2003, 80): {
        "alias": "ShowLoadingScreenText",
        "docstring": "Enable or disable text on loading screens.",
        "args": {
            "state": BOOL,
        },
        "partials": {
            "EnableLoadingScreenText": dict(state=True),
            "DisableLoadingScreenText": dict(state=False),
        }
    },
    (2003, 81): {
        "alias": "RemoveGesture",
        "docstring": "Remove given Gesture from player's inventory'.",
        "args": {
            "gesture_param_id": INT,
        },
    },
    (2003, 82): {
        "alias": "EraseNPCSummonSign",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2003, 83): {
        "alias": "Unknown_2003_83",
        "docstring": "TODO",
        "args": {
            "unk_0_1": BOOL,
        },
    },

    (2004, 48): {
        "alias": "ChangeCharacterCloth",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "bit_count": INT,
            "state_id": INT,
        },
    },
    (2004, 49): {
        "alias": "ChangePatrolBehavior",
        "docstring": """
            I don't know what a 'patrol_information_id' actually is.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "patrol_information_id": INT | {"internal_default": 0},
        },
    },
    (2004, 50): {
        "alias": "SetLockOnPoint",
        "docstring": """
            Presumably changes the point that is locked on to by the player.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "lock_on_dummy_id": INT,
            "state": BOOL,
        },
    },
    (2004, 52): {
        "alias": "ChangePlayerCharacterInitParam",
        "docstring": """
            I assume this affects the player.
        """,
        "args": {
            "character_init_param": INT,
        },
    },
    (2004, 55): {
        "alias": "SetCharacterTalkRange",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "distance": FLOAT | {"internal_default": 17.0},
        },
    },
    (2004, 60): {
        "alias": "ConnectCharacterToCaravan",
        "docstring": "Used to connect trolls to the caravans they pull.",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "caravan_asset": NO_DEFAULT(AssetTyping),
        },
    },
    (2004, 61): {
        "alias": "Unknown_2004_61",
        "docstring": "Used only once: in Stranded Graveyard with argument 9999.",
        "args": {
            "unk_0_4": INT,
        },
    },
    (2004, 63): {
        "alias": "SetCharacterEnableDistance",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "distance": FLOAT,
        },
    },
    (2004, 67): {
        "alias": "CopyPlayerCharacterData",
        "docstring": "Used, for example, to initialize Mimics and set up Gideon's boss loadout.",
        "args": {
            "source_character": NO_DEFAULT(CharacterTyping),
            "dest_character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2004, 68): {
        "alias": "AttachAssetToCharacter",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "dummy_id": INT | {"internal_default": -1},
            "asset": NO_DEFAULT(AssetTyping),
        },
    },
    (2004, 69): {
        "alias": "SetCharacterDisableOnCollisionUnload",
        "docstring": """
            I believe this will, if enabled for a character, cause that character to be disabled when the collision they 
            are standing on (or possibly their draw parent) is unloaded.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
    },
    (2004, 70): {
        "alias": "SetDistanceBasedNetworkAuthorityUpdate",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
    },
    (2004, 71): {
        "alias": "Unknown_2004_71",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,
            "entity_a": NO_DEFAULT(CoordEntityTyping),
            "entity_b": NO_DEFAULT(CoordEntityTyping),
        },
    },
    (2004, 73): {
        "alias": "SetCharacterFadeOnEnable",
        "docstring": "Determines if character will fade-in when enabled, I believe.",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
    },
    (2004, 74): {
        "alias": "MoveCharacterAndCopyDrawParentWithFadeout",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "destination_type": NO_DEFAULT(CoordEntityType),
            "destination": NO_DEFAULT(CoordEntityTyping),
            "dummy_id": DUMMY_ID | {"default": None},
            "copy_draw_parent": NO_DEFAULT(CoordEntityTyping),
            "use_bonfire_effect": BOOL,
            "reset_camera": BOOL,
        },
    },
    (2004, 75): {
        "alias": "SetCharacterFaceParamOverride",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "override_slot": INT,
            "face_param_id": INT,
        },
    },
    (2004, 76): {
        "alias": "Unknown_2004_76",
        "docstring": """
            Unknown. `flag` appears to be a boss death flag and `item_lot` the reward for that boss.
            
            Called on the first line of boss-despawning common event 90005860 if an item lot was passed in.
        """,
        "args": {
            "flag": FLAG,
            "item_lot": INT,
        },
    },
    (2004, 77): {
        "alias": "FadeToBlack",
        "docstring": "TODO",
        "args": {
            "strength": FLOAT,
            "duration": FLOAT,
            "freeze_player": BOOL,
            "freeze_player_delay": FLOAT,
        },
    },
    (2004, 78): {
        "alias": "CopyPlayerCharacterDataFromOnlinePlayers",
        "docstring": "TODO",
        "args": {
            "pool_type": INT,
            "failcase_player_param_id": INT,
            "target_character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2004, 79): {
        "alias": "RequestPlayerCharacterDataFromOnlinePlayers",
        "docstring": "TODO",
        "args": {
            "pool_type": INT,
            "data_count": INT,
        },
    },
    (2004, 80): {
        "alias": "SendPlayerCharacterDataToOnlinePlayers",
        "docstring": "TODO",
        "args": {
            "pool_type": INT,
        },
    },
    (2004, 81): {
        "alias": "ResetCharacterPosition",
        "docstring": "Resets character position to MSB coordinates, I assume.",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2004, 83): {
        "alias": "SetSpecialStandbyEndedFlag",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
    },
    (2004, 84): {
        "alias": "SetCharacterEnableDistanceWithUnknown",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "enable_distance": FLOAT,  # TODO: once with 220.0
            "unknown_distance": FLOAT,  # TODO: once with 40.0
        },
    },

    (2005, 17): {
        "alias": "AttachCaravanToController",
        "docstring": "Attaches caravan to trolls pulling it, presuamably (there is also an inverse event).",
        "args": {
            "caravan_asset": NO_DEFAULT(AssetTyping),
            "character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2005, 18): {
        "alias": "AttachAssetToAsset",
        "docstring": "TODO",
        "args": {
            "child_asset": NO_DEFAULT(AssetTyping),
            "parent_asset": NO_DEFAULT(AssetTyping),
            "parent_dummy_id": DUMMY_ID,
        },
    },
    # (2005, 19) removed (old "DestroyObject_NoSlot", no "Asset" version).
    (2005, 20): {
        "alias": "CreateBigHazardousAsset",
        "docstring": "TODO",
        "args": {
            "asset_flag": FLAG,
            "asset": INT,
            "dummy_id_start": INT | {"internal_default": -1},
            "dummy_id_end": INT | {"internal_default": -1},
            "behaviour_id": INT,
            "target_type": NO_DEFAULT(DamageTargetType),
            "radius": FLOAT,
            "life": FLOAT,
            "repetition_time": FLOAT,
        },
    },

    (2006, 6): {
        "alias": "SetWindVFX",
        "docstring": "Not sure if argument is an MSB VFX Event ID (more likely) or an absolute VFX asset ID.",
        "args": {
            "wind_vfx_id": INT,
        },
    },

    (2007, 10): {
        "alias": "AwaitDialogResponse",
        "docstring": """
            Displays a dialog and enables one of three flags, depending on the player's response. Very useful. `right`
            and `cancel` flags are often identical.
            
            Halts execution until the player responds.
        """,
        "args": {
            "message": NO_DEFAULT(EventTextTyping),
            "button_type": NO_DEFAULT(ButtonType),
            "number_buttons": NO_DEFAULT(NumberButtons),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping) | {"internal_default": 0},
            "display_distance": FLOAT,
            "left_flag": FLAG,
            "right_flag": FLAG,
            "cancel_flag": FLAG,
        },
    },
    (2007, 12): {
        "alias": "DisplayFlashingMessageWithPriority",
        "docstring": "TODO",
        "args": {
            "text": NO_DEFAULT(EventTextTyping),
            "priority": INT,
            "should_interrupt": BOOL,
        },
    },
    (2007, 13): {
        "alias": "DisplaySubareaWelcomeMessage",
        "docstring": "Uses PlaceName FMG.",
        "args": {
            "place_name_id": NO_DEFAULT(PlaceNameTyping),
        },
    },
    (2007, 14): {
        "alias": "DisplayAreaWelcomeMessage",
        "docstring": "Uses PlaceName FMG.",
        "args": {
            "place_name_id": NO_DEFAULT(PlaceNameTyping),
        },
    },
    (2007, 15): {
        "alias": "DisplayTutorialMessage",
        "docstring": "TODO",
        "args": {
            "tutorial_param_id": INT,
            "unk_4_5": BOOL,
            "unk_5_6": BOOL,
        },
    },
    (2007, 16): {
        "alias": "DisplayNetworkMessage",
        "docstring": "TODO",
        "args": {
            "text": NO_DEFAULT(EventTextTyping),  # TODO: Could be a different category
            "unk_4_5": BOOL,
        },
    },

    (2008, 4): {
        "alias": "SetCameraAngle",
        "docstring": "Used very often, presumably to gently push the camera to a specific latitude/longitude.",
        "args": {
            "x_angle": FLOAT,
            "y_angle": FLOAT,
        },
    },

    (2009, 8): {
        "alias": "BanishInvaders",
        "docstring": "TODO",
        "args": {
            "unknown": INT,
        },
    },
    (2009, 11): {
        "alias": "BanishPhantoms",
        "docstring": "TODO",
        "args": {
            "unknown": INT,
        },
    },
    (2009, 12): {
        "alias": "BanishPhantomsAndUpdateServerPvPStats",
        "docstring": "TODO",
        "args": {
            "unknown": INT,
        },
    },

    (2010, 7): {
        "alias": "SuppressSoundEvent",
        "docstring": "TODO",
        "args": {
            "sound_id": NO_DEFAULT(SoundEventTyping),
            "unk_4_8": INT,
            "suppression_active": BOOL,
        },
    },
    (2010, 8): {
        "alias": "UnknownSound_2010_8",
        "docstring": "TODO",
        "args": {
            "sound_id": NO_DEFAULT(SoundEventTyping),
        },
    },
    (2010, 10): {
        "alias": "SetBossMusic",
        "docstring": "TODO",
        "args": {
            "bgm_boss_conv_param_id": INT,
            "state": NO_DEFAULT(BossMusicState),
        },
    },
    (2010, 11): {
        "alias": "SuppressSoundForFogGate",
        "docstring": "TODO",
        "args": {
            "duration": FLOAT,
        },
    },
    (2010, 12): {
        "alias": "SetFieldBattleMusicHeatUp",
        "docstring": "TODO",
        "args": {
            "npc_threat_level": INT | {"internal_default": 2},
            "state": BOOL,
        },
        "partials": {
            "EnableFieldBattleMusicHeatUp": dict(state=True),
            "DisableFieldBattleMusicHeatUp": dict(state=False),
        },
    },

    (2012, 8): {
        "alias": "SetAreaWelcomeMessageState",
        "docstring": "TODO",
        "args": {
            "state": BOOL,
        },
    },
    (2012, 11): {
        "alias": "ActivateGparamOverride",
        "docstring": "TODO",
        "args": {
            "gparam_sub_id": INT,
            "change_duration": FLOAT,
        },
    },
    (2012, 12): {
        "alias": "DeactivateGparamOverride",
        "docstring": "TODO",
        "args": {
            "change_duration": FLOAT,
        },
    },
}


add_common_emedf_info(EMEDF, PACKAGE_PATH("eldenring/events/emevd/er-common.emedf.json"))
EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS = build_emedf_aliases_tests(EMEDF)

# Extra tests that use custom instructions from `compiler`.
EMEDF_TESTS |= {
    "ActionButton": {
        "if": "IfActionButton",
    },
    "PlayerHasWeapon": {
        "if": "IfPlayerHasWeapon",
    },
    "PlayerHasArmor": {
        "if": "IfPlayerHasArmor",
    },
    "PlayerHasTalisman": {
        "if": "IfPlayerHasTalisman",
    },
    "PlayerHasGood": {
        "if": "IfPlayerHasGood",
    },
    "PlayerDoesNotHaveWeapon": {
        "if": "IfPlayerDoesNotHaveWeapon",
    },
    "PlayerDoesNotHaveArmor": {
        "if": "IfPlayerDoesNotHaveArmor",
    },
    "PlayerDoesNotHaveTalisman": {
        "if": "IfPlayerDoesNotHaveTalisman",
    },
    "PlayerDoesNotHaveGood": {
        "if": "IfPlayerDoesNotHaveGood",
    },
}

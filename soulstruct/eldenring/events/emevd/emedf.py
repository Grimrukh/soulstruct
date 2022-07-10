"""Dictionary that maps EMEVD instructions `(category, index)` to Soulstruct aliases and "prebaked" variants.

Used in tandem with `*.emedf.json` to compile/decompile EVS <-> EMEVD scripts.
"""
from __future__ import annotations

import typing as tp

from soulstruct.base.events.emevd.emedf import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.maps.constants import get_map_variable_name
from soulstruct.utilities.files import PACKAGE_PATH
from .enums import *

__all__ = ["EMEDF", "EMEDF_ALIASES", "EMEDF_TESTS"]


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
    "to_evs": lambda args: get_map_variable_name(args["area_id"], args["block_id"], args["cc_id"], args["dd_id"]),
}
ITEM_TYPE = {
    "type": ItemType,
    "default": lambda args: args["item"].get_item_enum(),
    "comment": "Auto-detected from `item` type by default.",
}
FLAG = {
    "type": FlagInt,
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
    "type": FlagInt,
    "default": None,
    "from_evs": lambda args: args["flag_range"][0],
}
FLAG_RANGE_LAST = {
    "type": FlagInt,
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
                else args[arg_name].get_coord_entity_type()
            ),
            "comment": f"Auto-detected from `{arg_name}` type by default. Sets `Character` type for `PLAYER`.",
        }
    return {
        "type": CoordEntityType,
        "default": lambda args: args[arg_name].get_coord_entity_type(),
        "comment": f"Auto-detected from `{arg_name}` type by default.",
    }


# TODO:
#  remaining partials
#  PYI module
#  vanilla test


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
    (1, 5): {
        "alias": "IfTimeOfDay",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
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
            "condition": {},
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
    (3, 5): {
        "alias": "IfActionButtonBasic",
        "docstring": """
            Generates an 'action button' prompt and waits for the player to activate it.

            Basic (not "boss") version with no line intersection check.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "anchor_type": AUTO_COORD_ENTITY_TYPE("anchor_entity"),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping),
            "facing_angle": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 180.0,
            },
            "model_point": MODEL_POINT,
            "max_distance": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 2.0,
            },
            "prompt_text": NO_DEFAULT(EventTextTyping),
            "trigger_attribute": {
                "type": TriggerAttribute,
                "default": TriggerAttribute.Human | TriggerAttribute.Hollow,
            },
            "button": INT | {"default": 0},
        },
        "evs_args": {
            "condition": {},
            "prompt_text": {},
            "anchor_entity": {},
            "anchor_type": {},
            "facing_angle": {},
            "model_point": {},
            "max_distance": {},
            "trigger_attribute": {},
            "button": {},
        },
    },
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
            "IfTryingToCreateSession": dict(state=MultiplayerState.TryingToCreateSession),
            "IfTryingToJoinSession": dict(state=MultiplayerState.TryingToJoinSession),
            "IfLeavingSession": dict(state=MultiplayerState.LeavingSession),
            "IfFailedToCreateSession": dict(state=MultiplayerState.FailedToCreateSession),
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
        "alias": "IfTrueFlagCountComparison",
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
            "IfTrueFlagCountEqual": dict(comparison_type=ComparisonType.Equal),
            "IfTrueFlagCountNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfTrueFlagCountGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfTrueFlagCountLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfTrueFlagCountGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfTrueFlagCountLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
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
    (3, 13): {
        "alias": "IfActionButtonBoss",
        "docstring": """
            Generates an 'action button' prompt and waits for the player to activate it.

            Boss (not "basic") version with no line intersection check.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "anchor_type": AUTO_COORD_ENTITY_TYPE("anchor_entity"),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping),
            "facing_angle": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 180.0,
            },
            "model_point": MODEL_POINT,
            "max_distance": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 2.0,
            },
            "prompt_text": NO_DEFAULT(EventTextTyping),
            "trigger_attribute": {
                "type": TriggerAttribute,
                "default": TriggerAttribute.Human | TriggerAttribute.Hollow,
            },
            "button": INT | {"default": 0},
        },
        "evs_args": {
            "condition": {},
            "prompt_text": {},
            "anchor_entity": {},
            "anchor_type": {},
            "facing_angle": {},
            "model_point": {},
            "max_distance": {},
            "trigger_attribute": {},
            "button": {},
        },
    },
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
    (3, 18): {
        "alias": "IfActionButtonBasicLineIntersect",
        "docstring": """
            Generates an 'action button' prompt and waits for the player to activate it.

            Basic (not "boss") version with a line intersection check.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "anchor_type": AUTO_COORD_ENTITY_TYPE("anchor_entity"),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping),
            "facing_angle": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 180.0,
            },
            "model_point": MODEL_POINT,
            "max_distance": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 2.0,
            },
            "prompt_text": NO_DEFAULT(EventTextTyping),
            "trigger_attribute": {
                "type": TriggerAttribute,
                "default": TriggerAttribute.Human | TriggerAttribute.Hollow,
            },
            "button": INT | {"default": 0},
            "line_intersects": INT,
        },
        "evs_args": {
            "condition": {},
            "prompt_text": {},
            "anchor_entity": {},
            "line_intersects": {},
            "anchor_type": {},
            "facing_angle": {},
            "model_point": {},
            "max_distance": {},
            "trigger_attribute": {},
            "button": {},
        },
    },
    (3, 19): {
        "alias": "IfActionButtonBossLineIntersect",
        "docstring": """
            Generates an 'action button' prompt and waits for the player to activate it.

            Boss (not "basic") version with a line intersection check.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "anchor_type": AUTO_COORD_ENTITY_TYPE("anchor_entity"),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping),
            "facing_angle": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 180.0,
            },
            "model_point": MODEL_POINT,
            "max_distance": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 2.0,
            },
            "prompt_text": NO_DEFAULT(EventTextTyping),
            "trigger_attribute": {
                "type": TriggerAttribute,
                "default": TriggerAttribute.Human | TriggerAttribute.Hollow,
            },
            "button": INT | {"default": 0},
            "line_intersects": INT,
        },
        "evs_args": {
            "condition": {},
            "prompt_text": {},
            "anchor_entity": {},
            "line_intersects": {},
            "anchor_type": {},
            "facing_angle": {},
            "model_point": {},
            "max_distance": {},
            "trigger_attribute": {},
            "button": {},
        },
    },
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
    (3, 21): {
        "alias": "IfDLCState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "is_owned": BOOL,
        },
        "partials": {
            "IfDLCOwned": dict(is_owned=True),
            "IfDLCNotOwned": dict(is_owned=False),
        },
    },
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
    (4, 1): {
        "alias": "IfAttacked",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "attacked_entity": NO_DEFAULT(CharacterTyping),
            "attacker": NO_DEFAULT(CharacterTyping),
        },
    },
    (4, 2): {
        "alias": "IfHealthComparison",
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
            "IfHealthEqual": dict(comparison_type=ComparisonType.Equal),
            "IfHealthNotEqual": dict(comparison_type=ComparisonType.NotEqual),
            "IfHealthGreaterThan": dict(comparison_type=ComparisonType.GreaterThan),
            "IfHealthLessThan": dict(comparison_type=ComparisonType.LessThan),
            "IfHealthGreaterThanOrEqual": dict(comparison_type=ComparisonType.GreaterThanOrEqual),
            "IfHealthLessThanOrEqual": dict(comparison_type=ComparisonType.LessThanOrEqual),
        },
    },
    (4, 3): {
        "alias": "IfCharacterType",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "character_type": NO_DEFAULT(CharacterType),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterHuman": dict(character_type=CharacterType.Human),
            "IfCharacterWhitePhantom": dict(character_type=CharacterType.WhitePhantom),
            "IfCharacterHollow": dict(character_type=CharacterType.Hollow),
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
        "alias": "IfObjectDestructionState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfObjectDestroyed": dict(state=True),
            "IfObjectNotDestroyed": dict(state=False),
        },
    },
    (5, 1): {
        "alias": "IfObjectDamaged",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "attacker": NO_DEFAULT(CharacterTyping),
        },
    },
    (5, 2): {
        "alias": "IfObjectActivated",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "obj_act_id": INT,
        },
    },
    (5, 3): {
        "alias": "IfObjectHealthValueComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": INT,
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
            "condition": CONDITION_GROUP | HIDE_NAME,
        },
        "partials": {
            "AwaitConditionTrue": dict(state=True),
            "AwaitConditionFalse": dict(state=False),
        },
    },
    (1000, 1): {
        "alias": "SkipLinesIfConditionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "condition": CONDITION_GROUP | HIDE_NAME,
        },
        "partials": {
            "SkipLinesIfConditionTrue": dict(state=True),
            "SkipLinesIfConditionFalse": dict(state=False),
        },
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
        "alias": "SkipLinesIfFinishedConditionState",
        "docstring": """
            This command is used instead of 1000[01] when conditions are being checked *after* they have already been
            uploaded into the MAIN condition. For example, you might want to continue MAIN if either AND(01) or AND(02) 
            are true, but then afterwards, act conditionally on exactly which one of those two registers caused you to
            continue.
        """,
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "SkipLinesIfFinishedConditionTrue": dict(state=True),
            "SkipLinesIfFinishedConditionFalse": dict(state=False),
        },
    },
    (1000, 8): {
        "alias": "ReturnIfFinishedConditionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "EndIfFinishedConditionTrue": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfFinishedConditionFalse": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfFinishedConditionTrue": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfFinishedConditionFalse": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1000, 9): {
        "alias": "WaitForNetworkApproval",
        "docstring": """
            Wait for network to approve event (up to `max_seconds` seconds).
        """,
        "args": {
            "max_seconds": FLOAT,
        },
    },
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
        "alias": "SkipLinesIfObjectDestructionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
        },
        "partials": {
            "SkipLinesIfObjectDestroyed": dict(state=True),
            "SkipLinesIfObjectNotDestroyed": dict(state=False),
        },
    },
    (1005, 2): {
        "alias": "ReturnIfObjectDestructionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
        },
        "partials": {
            "EndIfObjectDestroyed": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfObjectNotDestroyed": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfObjectDestroyed": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfObjectNotDestroyed": dict(event_return_type=EventReturnType.Restart, state=False),
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
        "evs_args": {
            "slot": {},
            "event_id": {},
            "args": {},
            "arg_types": {
                "type": str,
                "default": "",
            },
        },
    },
    (2000, 1): {
        "alias": "TerminateEvent",
        "docstring": "Delete an instance (slot) of an event script.",
        "args": {
            "event_slot": INT,
            "event_id": INT,
        },
    },
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
    (2000, 4): {
        "alias": "IssuePrefetchRequest",
        "docstring": """
            No idea what this does.
        """,
        "args": {
            "request_id": INT,
        },
    },
    (2000, 5): {
        "alias": "SaveRequest",
        "docstring": "Request the game to save player progress.",
        "args": {
            "dummy": INT | {"default": 0},
        },
    },
    (2000, 6): {
        "alias": "RunCommonEvent",
        "docstring": "Initialize an instance of an event script from `common_func` with the given arguments.",
        "args": {
            "unknown": INT,
            "event_id": INT | HIDE_NAME,
            # Default argument is a single 32-bit zero, but more packed data can be passed.
            "args": {
                "type": tuple,  # will be unpacked for numeric
                "default": (0,),
            },
        },
        "evs_args": {
            "unknown": {},
            "event_id": {},
            "args": {},
            "arg_types": {
                "type": str,
                "default": "",
            },
        },
    },
    (2000, 7): {
        "alias": "UnknownSystem_07",
        "docstring": "TODO",
        "args": {
            "unknown_slot": INT,
        },
    },
    (2000, 8): {
        "alias": "UnknownSystem_08",
        "docstring": "TODO",
        "args": {
            "unknown_slot": INT,
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
            "item_lot_param_id": INT,
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
            "model_point": INT,
            "behavior_id": INT,
            "launch_angle_x": INT,
            "launch_angle_y": INT,
            "launch_angle_z": INT,
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
        "alias": "SetNavmeshType",
        "docstring": """
            Set given navmesh type.
        """,
        "args": {
            "navmesh_id": {
                "type": NavigationEventTyping,
                "default": None,
            },
            "navmesh_type": {
                "type": NavmeshType,
                "default": None,
            },
            "operation": {
                "type": BitOperation,
                "default": None,
            },
        },
        "partials": {
            "EnableNavmeshType": dict(operation=BitOperation.Add),
            "DisableNavmeshType": dict(operation=BitOperation.Delete),
            "ToggleNavmeshType": dict(operation=BitOperation.Invert),
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
                "default": -1,
                "internal_default": -1,
            },
            "unknown1": INT | {"default": 0},
        },
        "evs_args": {
            "game_map": GAME_MAP_EVS,
            "player_start": {},
            "unknown1": {},
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
        "docstring": "Used a lot. Standard way to make a Character or Object perform an animation.",
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
            "unknown1": INT | {"default": 0},
            "unknown2": FLOAT | {"default": 0.0},
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
            "RemoveRingFromPlayer": dict(item_type=ItemType.Ring),
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
            "item_lot_param_id": INT,
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
    (2004, 3): {
        "alias": "MoveToEntity",
        "docstring": "Basic move. I recommend you use the combined `Move` function.",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "destination_type": AUTO_COORD_ENTITY_TYPE("destination"),
            "destination": NO_DEFAULT(CoordEntityTyping),
            "model_point": MODEL_POINT,
        },
        "evs_args": {
            "character": {},
            "destination": {},
            "model_point": {},
            "destination_type": {},
        },
    },
    (2004, 4): {
        "alias": "Kill",
        "docstring": """
            Technically a kill 'request.'
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "award_souls": BOOL | {"default": False},
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
            "special_effect_id": INT | HIDE_NAME,
        },
    },
    (2004, 9): {
        "alias": "SetStandbyAnimationSettings",
        "docstring": """
            Sets entity's default standby animations. -1 is default for each category.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "standby_animation": {
                "type": int,
                "default": -1,
                "internal_default": -1,
            },
            "damage_animation": {
                "type": int,
                "default": -1,
                "internal_default": -1,
            },
            "cancel_animation": {
                "type": int,
                "default": -1,
                "internal_default": -1,
            },
            "death_animation": {
                "type": int,
                "default": -1,
                "internal_default": -1,
            },
            "standby_exit_animation": {
                "type": int,
                "default": -1,
                "internal_default": -1,
            },
        },
        "partials": {
            "ResetStandbyAnimationSettings": dict(
                standby_animation=-1,
                damage_animation=-1,
                cancel_animation=-1,
                death_animation=-1,
                standby_exit_animation=1,
            ),
        },
    },
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
            "region": NO_DEFAULT(RegionTyping),
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
        "alias": "RotateToFaceEntity",
        "docstring": """
            Rotate a character to face a target map entity of any type.
            WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at
            least.)

            The Bloodborne+ version allows you to force an animation at the same time (post-rotation) and optionally 
            wait until that animation is completed. (I assume a value of -1 avoids it.)
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
        "alias": "CancelSpecialEffect",
        "docstring": """
            'Special effect' as in a buff/debuff, not graphical effects (though they may come with one).
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "special_effect_id": INT | HIDE_NAME,
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
            Note that the bool is inverted from what you might expect.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "is_disabled": BOOL,
        },
        "partials": {
            "EnableCharacterCollision": dict(is_disabled=False),  # Note reversed bool.
            "DisableCharacterCollision": dict(is_disabled=True),
        },
    },
    (2004, 32): {
        "alias": "AIEvent",
        "docstring": """
            I have no idea what this does.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "command_id": INT,
            "command_slot": INT,
            "first_event_flag": FLAG,
            "last_event_flag": FLAG,
        },
    },
    (2004, 33): {
        "alias": "ReferDamageToEntity",
        "docstring": """
            All damage dealt to the first character will *also* (not *only*) be dealt to the target entity. I'm not 100%
            sure if the target entity can be an Object.

            Only used by the Four Kings in the vanilla game.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "target_entity": {
                "type": CharacterTyping,  # TODO: Can it be an Object?
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
            "model_point": MODEL_POINT,
            "set_draw_parent": {
                "type": MapPartTyping,
                "default": None,
            },
        },
        "evs_args": {
            "character": {},
            "destination": {},
            "set_draw_parent": {},
            "model_point": {},
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
            "model_point": MODEL_POINT,
        },
        "evs_args": {
            "character": {},
            "destination": {},
            "model_point": {},
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
            "model_point": MODEL_POINT,
            "copy_draw_parent": NO_DEFAULT(AnimatedEntityTyping),
        },
        "evs_args": {
            "character": {},
            "destination": {},
            "copy_draw_parent": {},
            "model_point": {},
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
    (2004, 44): {
        "alias": "SetTeamTypeAndExitStandbyAnimation",
        "docstring": """
            Two for the price of one. Often used when NPCs with resting animations become hostile.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "team_type": {
                "type": TeamType,
                "default": None,
            },
        },
    },
    (2004, 47): {
        "alias": "EqualRecovery",
        "docstring": """
            Unknown effect. Only used in Battle of Stoicism, so likely useless to you.
        """,
        "args": {},
    },
    (2005, 1): {
        "alias": "DestroyObject",
        "docstring": """
            Technically 'requests' the object's destruction. No idea what the slot number does.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "request_slot": {
                "type": int,
                "default": 1,
            },
        },
    },
    (2005, 2): {
        "alias": "RestoreObject",
        "docstring": """
            The opposite of destruction. Restores it to its original MSB coordinates.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
        },
    },
    (2005, 3): {
        "alias": "SetObjectState",
        "docstring": "TODO",
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableObject": dict(state=True),
            "DisableObject": dict(state=False),
        },
    },
    (2005, 4): {
        "alias": "SetTreasureState",
        "docstring": "TODO",
        "args": {
            "obj": NO_DEFAULT(ObjectTyping),
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableTreasure": dict(
                state=True,
                __docstring="Enables any treasure attached to this object by MSB events.",
            ),
            "DisableTreasure": dict(
                state=False,
                __docstring="""
                    Disables any treasure attached to this object by MSB events.

                    If you want to disable treasure by default, you can do it in the MSB by changing a certain event 
                    value to 255.
                """,
            ),
        },
    },
    (2005, 5): {
        "alias": "ActivateObject",
        "docstring": """
            Manually call a specific ObjAct event attached to this object. I believe 'relative_index' refers to the 
            points on the object at which it can be activated (e.g. which side of a gate you are on).

            Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how 
            the game gets Patches to pull the lever in the Catacombs.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "obj_act_id": INT,
            "relative_index": INT,
        },
    },
    (2005, 6): {
        "alias": "SetObjectActivation",
        "docstring": """
            Sets whether the object can be activated (1) or not activated (0).
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
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
            "obj": NO_DEFAULT(ObjectTyping),
            "animation_id": INT,
        },
    },
    (2005, 8): {
        "alias": "PostDestruction",
        "docstring": """
            Sets the object to whatever appearance it would have after being destroyed. Again, not sure what 'slot' 
            does, but it's literally *always* 1 in vanilla scripts (and from my testing, the instruction doesn't work 
            with `slot=0`).
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "request_slot": {
                "type": int,
                "default": 1,
            },
        },
    },
    (2005, 9): {
        "alias": "CreateHazard",
        "docstring": """
            Turn an object into an environmental hazard. It deals damage when touched according to the NPC Behavior 
            params you give it. The model_point determines which part of the object is hazardous (with the given radius 
            and life, relative to the time this instruction occurs).

            An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.

            'target_type' determines what the hazard can damage (Character and/or Map).
        """,
        "args": {
            "obj_flag": FLAG,
            "obj": NO_DEFAULT(ObjectTyping),
            "model_point": INT,
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
        "alias": "MoveObjectToCharacter",
        "docstring": "Move an object to a character.",
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "character": {
                "type": CharacterTyping,
                "default": None,
                "internal_default": -1,
            },
            "model_point": MODEL_POINT,
        },
    },
    (2005, 12): {
        "alias": "RemoveObjectFlag",
        "docstring": """
            No idea what this does. I believe it might undo the CreateHazard instruction, at least.
        """,
        "args": {
            "obj_flag": FLAG,
        },
    },
    (2005, 13): {
        "alias": "SetObjectInvulnerabilityState",
        "docstring": """
            1 = invulnerable.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableObjectInvulnerability": dict(state=True),
            "DisableObjectInvulnerability": dict(state=False),
        },
    },
    (2005, 14): {
        "alias": "SetObjectActivationWithIdx",
        "docstring": """
            Similar to SetObjectActivation, but you can provide the relative index to disable (e.g. one side of a door).
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "obj_act_id": INT | {"internal_default": -1},
            "relative_index": INT,
            "state": BOOL | HIDE_NAME,
        },
        # No partials. Use custom `EnableObjectActivation` instructions with optional `relative_index` argument.
    },
    (2005, 15): {
        "alias": "EnableTreasureCollection",
        "docstring": """
            Forces an object to spawn its treasure, even if the treasure's ItemLot flag is already enabled.

            Useful if you want some treasure to reappear (after, say, taking it from the player and disabling the 
            ItemLot flag) without the player needing to reload the map.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping),
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
            "model_point": MODEL_POINT,
            "vfx_id": INT,
        },
        "evs_args": {
            "vfx_id": {},
            "anchor_entity": {},
            "model_point": {},
            "anchor_type": {},
        },
    },
    (2006, 4): {
        "alias": "CreateObjectVFX",
        "docstring": "TODO",
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "vfx_id": INT,
            "model_point": INT,
        },
    },
    (2006, 5): {
        "alias": "DeleteObjectVFX",
        "docstring": """
            Note `erase_root` vs. `erase_root_only` for map SFX.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
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
                "default": 2 ** 32 - 1,
                "internal_default": 2 ** 32 - 1,
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
        "alias": "DisplayBattlefieldMessage",
        "docstring": """
            Displays a flashing messages at the bottom of the screen that does not block player input.
        """,
        "args": {
            "text": NO_DEFAULT(EventTextTyping) | HIDE_NAME,
        },
    },
    (2007, 9): {
        "alias": "UnknownText_2007_9",
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
            "model_point": MODEL_POINT,
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
            "model_point": {},
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
            "obj": NO_DEFAULT(ObjectTyping),
        },
    },
    (2009, 3): {
        "alias": "RegisterGrace",
        "docstring": """
            Register a bonfire, which creates the flame VFX and allows you to interact with it (via the MSB entity with 
            ID (obj + 1000).

            I believe the bonfire flag tells the game where to keep track of its kindle level, or something like that. I
            don't recommend messing around with this much. The reaction distance, angle, and initial kindle level are 
            all set to their standard defaults for bonfires.

            Note that, for some reason, kindle level is defined in increments of 10, so the number of Estus Flasks given
            is (initial_kindle_level / 2) + 5.

            There also seems to be an issue with registering a bonfire that has already been registered with a greater 
            initial kindle level. Beware of this, if you find that you can't interact with bonfires or get them to even 
            register.
        """,
        "args": {
            "grace_flag": FLAG,
            "obj": NO_DEFAULT(ObjectTyping),
            "reaction_distance": {
                "type": float,
                "default": 0.0,
            },
            "reaction_angle": {
                "type": float,
                "default": 0.0,
            },
            "initial_kindle_level": INT | {"default": 0},
            "unknown": FLOAT | {"default": 0},  # TODO: often 5.0; maybe new "default distance"
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
                "default": -1,
                "internal_default": -1,
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
    (3, 28): {
        "alias": "IfMapCeremonyState",
        "docstring": "Ceremony states are unused except for Untended Graves, I believe.",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "ceremony_id": INT,
        },
        "evs_args": {
            "condition": {},
            "state": {},
            "game_map": GAME_MAP_EVS,
            "ceremony_id": {},
        },
        "partials": {
            "IfMapInCeremony": dict(state=True),
            "IfMapNotInCeremony": dict(state=False),
        },
    },
    (3, 30): {
        "alias": "IfInsideMapTile",
        "docstring": """
            Note that there is a little bit of funny business with this one. Only really used during Radahn fight.
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
        "alias": "IfUnknownCondition_31",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "hours": INT,
            "unknown1": FLOAT,
            "unknown2": INT,
        },
    },
    (3, 32): {
        "alias": "IfUnknown_3_32",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk_1_2": INT,
            "unk_4_8": INT,
        },
    },
    (3, 33): {
        "alias": "IfUnknownCondition_33",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk_4_8": INT,
            "unk_8_9": BOOL,
        },
    },
    (3, 34): {
        "alias": "IfUnknownCondition_34",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk_4_8": INT,
            "unk_8_12": INT,
        },
    },
    (3, 35): {
        "alias": "IfUnknownCondition_35",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk_1_2": INT,
            "unk_4_8": INT,
        },
    },
    (3, 37): {
        "alias": "IfUnknownFlagCheck_37",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "flag": FLAG,
            "state": FLAG_SETTING,
        },
    },
    (3, 38): {
        "alias": "IfSteamConnectionState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "is_disconnected": BOOL,
        },
    },
    (3, 39): {
        "alias": "IfAllyPhantomCountComparison",
        "docstring": """
            Note that there's a 'comparison_state' bool that can be used to invert the operation (kind of pointless).
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "comparison_state": BOOL,
            "comparison_type": NO_DEFAULT(ComparisonType),
            "value": INT,
        },
    },
    
    (4, 15): {
        "alias": "IfCharacterDrawGroupState",
        "docstring": """
            Tests if character's draw group is currently enabled or disabled.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfCharacterDrawGroupEnabled": dict(state=True),
            "IfCharacterDrawGroupDisabled": dict(state=False),
        },
    },
    (4, 19): {
        "alias": "IfUnknownCharacterCondition_19",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "unk_8_12": INT,
            "unk_12_13": INT,
            "unk_13_14": INT,
            "unk_16_20": FLOAT,
        },
    },
    (4, 27): {
        "alias": "IfCharacterInvadeType",
        "docstring": """
            'invade_type' has an unknown type in the EMEDF. Probably refers to the invader's covenant.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "invade_type": INT,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
    },
    (4, 28): {
        "alias": "IfUnknownCharacterCondition_28",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "unk_8_12": INT,
            "unk_12_16": INT,
        },
    },
    (4, 30): {
        "alias": "IfUnknownCharacterCondition_30",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "npc_part_id": INT,
            "unk_12_16": INT,
            "unk_16_20": INT,
        },
    },
    (4, 31): {
        "alias": "IfUnknownCharacterCondition_31",
        "docstring": "Possibly still 'IfCharacterInvadeType'.",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "unk_4_8": INT,
            "unk_8_12": FLOAT,  # TODO: usually -1
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
        "alias": "IfUnknownCharacterCondition_34",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "unk_8_12": INT,
            "unk_12_16": INT,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
    },
    (4, 35): {
        "alias": "IfUnknownCharacterCondition_35",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "unk_8_12": INT,
        },
    },

    (5, 6): {
        "alias": "IfUnknownObjectCondition_6",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk_4_5": INT,
            "obj": NO_DEFAULT(ObjectTyping),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
    },
    (5, 10): {
        "alias": "IfObjectBackreadState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping),
            "state": BOOL,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "IfObjectBackreadEnabled": dict(state=True),
            "IfObjectBackreadDisabled": dict(state=False),
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
        }
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
        "alias": "GotoIfFinishedConditionState",
        "docstring": """
            Finished version.
        """,
        "args": {
            "label": LABEL,
            "required_state": BOOL,
            "input_condition": CONDITION_GROUP,
        },
        "partials": {
            "GotoIfFinishedConditionTrue": dict(required_state=True),
            "GotoIfFinishedConditionFalse": dict(required_state=False),
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
        "alias": "WaitUntilRandomTimeOfDay",
        "docstring": "Pause event script until a random time of day chosen between the given earliest/latest times.",
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
        "alias": "WaitFramesAfterCutscene",
        "docstring": """Always used after cutscene instructions with argument `frames=1`.""",
        "args": {
            "frames": INT,
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
            "SkipLinesIfTryingToCreateSession": dict(state=MultiplayerState.TryingToCreateSession),
            "SkipLinesIfTryingToJoinSession": dict(state=MultiplayerState.TryingToJoinSession),
            "SkipLinesIfLeavingSession": dict(state=MultiplayerState.LeavingSession),
            "SkipLinesIfFailedToCreateSession": dict(state=MultiplayerState.FailedToCreateSession),
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
            "EndIfTryingToCreateSession": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.TryingToCreateSession,
            ),
            "EndIfTryingToJoinSession": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.TryingToJoinSession,
            ),
            "EndIfLeavingSession": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.LeavingSession,
            ),
            "EndIfFailedToCreateSession": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.FailedToCreateSession,
            ),
            "RestartIfHost": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Host,
            ),
            "RestartIfClient": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Client,
            ),
            "RestartIfTryingToCreateSession": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.TryingToCreateSession,
            ),
            "RestartIfTryingToJoinSession": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.TryingToJoinSession,
            ),
            "RestartIfLeavingSession": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.LeavingSession,
            ),
            "RestartIfFailedToCreateSession": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.FailedToCreateSession,
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
            "flag": NO_DEFAULT(FlagInt),
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
            "GotoIfTryingToCreateSession": dict(state=MultiplayerState.TryingToCreateSession),
            "GotoIfTryingToJoinSession": dict(state=MultiplayerState.TryingToJoinSession),
            "GotoIfLeavingSession": dict(state=MultiplayerState.LeavingSession),
            "GotoIfFailedToCreateSession": dict(state=MultiplayerState.FailedToCreateSession),
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
            "line_count": INT,
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
        "alias": "SkipLinesIfUnknown_203",
        "docstring": "TODO",
        "args": {
            "line_count": INT,
            "state": BOOL,
            "unk_2_3": INT,
            "unk_3_2": INT,
            "unk_4_3": INT,
            "unk_5_4": INT,
            "unk_6_5": INT,
        },
    },
    (1003, 204): {
        "alias": "GotoIfUnknown_204",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "state": BOOL,
            "unk_2_3": INT,
            "unk_3_2": INT,
            "unk_4_3": INT,
            "unk_5_4": INT,
            "unk_6_5": INT,
        },
    },
    (1003, 206): {
        "alias": "SkipOrGotoIfUnknown_206",
        "docstring": "TODO",
        "args": {
            "label_or_goto": INT,  # TODO: figure out
            "unk_4_8": INT,
        },
    },
    (1003, 208): {
        "alias": "ReturnIfUnknown_208",
        "docstring": "TODO",
        "args": {
            "return_type": EVENT_RETURN_TYPE,
            "state": BOOL,
            "unk_2_3": INT,
            "unk_3_2": INT,
            "unk_4_3": INT,
            "unk_5_4": INT,
            "unk_6_5": INT,
        },
    },
    (1004, 0): {
        "alias": "SkipLinesIfCharacterSpecialEffectState",
        "docstring": "Note that the same instruction appeared in DS3 as 1003[112].",
        "args": {
            "line_count": INT,
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
    (1004, 4): {
        "alias": "Unknown_1004_04",
        "docstring": "Probably 'SkipLinesIfCharacterSomething'.",
        "args": {
            "line_count": INT,
            "character": NO_DEFAULT(CharacterTyping),
            "unk_8_12": INT,
        },
    },
    (1004, 5): {
        "alias": "GotoIfUnknown_1004_05",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "character": NO_DEFAULT(CharacterTyping),
            "unk_8_12": BOOL,
        },
    },
    (1005, 1): {
        "alias": "SkipLinesIfObjectDestructionState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "SkipLinesIfObjectDestroyed": dict(state=True),
            "SkipLinesIfObjectNotDestroyed": dict(state=False),
        },
    },
    (1005, 2): {
        "alias": "ReturnIfObjectDestructionState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": BOOL | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "EndIfObjectDestroyed": dict(event_return_type=EventReturnType.End, state=True),
            "EndIfObjectNotDestroyed": dict(event_return_type=EventReturnType.End, state=False),
            "RestartIfObjectDestroyed": dict(event_return_type=EventReturnType.Restart, state=True),
            "RestartIfObjectNotDestroyed": dict(event_return_type=EventReturnType.Restart, state=False),
        },
    },
    (1005, 101): {
        "alias": "GotoIfObjectDestructionState",
        "docstring": """
            Note change in argument order.
        """,
        "args": {
            "label": LABEL,
            "state": BOOL,
            "obj": NO_DEFAULT(ObjectTyping),
            "target_comparison_type": TARGET_COMPARISON_TYPE,
            "target_count": TARGET_COUNT_FLOAT,
        },
        "partials": {
            "GotoIfObjectDestroyed": dict(state=True),
            "GotoIfObjectNotDestroyed": dict(state=False),
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
        "alias": "UnknownTimer_04",
        "docstring": "TODO",
        "args": {
            "hours": INT,
            "minutes": INT,
            "seconds": INT,
            "unknown1": INT,
            "unknown2": INT,
            "unknown3": INT,
            "unknown4": INT,
            "unknown5": INT,
            "unknown6": INT,
        },
    },
    (2001, 5): {
        "alias": "UnknownTimer_05",
        "docstring": "TODO",
        "args": {
            "unknown1": INT,
        },
    },
    (2002, 10): {
        "alias": "UnknownCutscene_10",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "player_id": INT | {"internal_default": -1},
            "hours": INT,
            "unknown1": INT,
            "unknown2": FLOAT,
            "unknown3": INT,
            "unknown4": INT,
            "unknown5": INT,
        },
    },
    (2002, 11): {
        "alias": "UnknownCutscene_11",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "move_to_region": NO_DEFAULT(RegionTyping),  # TODO: can be 0
            "map_base_id": INT,  # TODO: e.g., 11050000, a 32-bit encoding of m11_05_00_00 (or 0)
            "player_id": INT | {"internal_default": -1},
            "unknown2": INT,  # TODO: either 0 or 13000
            "unknown3": INT,  # TODO: probably bool, either 1 (with 13000 above) or 0
        },
    },
    (2002, 12): {
        "alias": "UnknownCutscene_12",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "respawn_point": INT,
            "move_to_region": NO_DEFAULT(RegionTyping),
            "player_id": INT | {"internal_default": -1},
            "unk_20_24": INT,
            "unk_24_25": INT,
            "unk_25_26": INT,
            "unk_26_27": INT,
            "unk_28_32": FLOAT,  # TODO: default -1.0, or can be 200.0 or 300.0
            "unk_32_36": INT,  # TODO: default 0
        },
    },
    (2002, 13): {
        "alias": "UnknownCutscene_13",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "respawn_point": INT,
            "move_to_region": NO_DEFAULT(RegionTyping),
            "player_id": INT | {"internal_default": -1},
            "unk_16_20": INT,
            "unk_20_24": INT,
        },
    },
    (2003, 41): {
        "alias": "EventValueOperation",
        "docstring": """
            Performs a binary operation on the source flag and operand value, and stores the result in the target flag.
        """,
        "args": {
            "source_flag": NO_DEFAULT(FlagInt),
            "source_flag_bit_count": INT,
            "operand": INT,
            "target_flag": NO_DEFAULT(FlagInt),
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
            "flag": NO_DEFAULT(FlagInt),
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
            "flag": NO_DEFAULT(FlagInt),
            "bit_count": INT,
        },
    },
    (2003, 49): {
        "alias": "WarpPlayerToRespawnPoint",
        "docstring": "Not used in vanilla Elden Ring events, but keeping in case it still works (seems useful).",
        "args": {
            "respawn_point_id": INT | HIDE_NAME,
        },
    },
    (2003, 50): {
        "alias": "StartEnemySpawner",
        "docstring": "Not used in vanilla Elden Ring events, but keeping in case it still works (seems useful).",
        "args": {
            "spawner_id": INT | {"internal_default": -1},
        },
    },
    (2003, 51): {
        "alias": "SummonNPC",
        "docstring": "Not used in vanilla Elden Ring events, but keeping in case it still works (seems useful).",
        "args": {
            "sign_type": NO_DEFAULT(SingleplayerSummonSignType) | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "region": NO_DEFAULT(RegionTyping),
            "summon_flag": NO_DEFAULT(FlagInt),
            "dismissal_flag": NO_DEFAULT(FlagInt),
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
        "alias": "MakeEnemyAppear",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
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
            "EnableThisSlotFlag": dict(flag_type=FlagType.RelativeToThisEventSlot, flag=0, state=FlagSetting.Off),
            "DisableThisSlotFlag": dict(flag_type=FlagType.RelativeToThisEventSlot, flag=0, state=FlagSetting.On),
        },
    },
    (2003, 68): {
        "alias": "Unknown_2003_68",
        "docstring": """
            Unknown. Second argument is a float (e.g., 300.0).
        """,
        "args": {
            "unknown1": INT,
            "unknown2": FLOAT,
            "unknown3": INT,
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
            # Haven't bothered with relative flag partials for this one.
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
        "alias": "Unknown_2003_71",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,
        },
    },
    (2003, 72): {
        "alias": "Unknown_2003_72",
        "docstring": "TODO",
        "args": {
            "unk_0_4": FLOAT,
            "unk_4_8": INT,  # always 0 or -1
        },
    },
    (2003, 73): {
        "alias": "Unknown_2003_73",
        "docstring": "TODO",
        "args": {
            "unk_4_8": NO_DEFAULT(CoordEntityTyping),
            "unk_8_12": INT,  # TODO: always zero
            "unk_12_16": INT,  # TODO: always zero
        },
    },
    (2003, 74): {
        "alias": "Unknown_2003_74",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TOOD: always 1
        },
    },
    (2003, 75): {
        "alias": "Unknown_2003_75",
        "docstring": "Unknown. Only called once with arguments 0, 0, -1.",
        "args": {
            "unknown1": INT,  # TODO: zero
            "unknown2": INT,  # TODO: zero
            "unknown3": INT,  # TODO: -1
        },
    },
    (2003, 76): {
        "alias": "Unknown_2003_76",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: possibly BBH
            "unk_4_8": INT,  # TODO: always zero
            "unk_8_12": FLOAT,  # TODO: almost certainly three XYZ angles (deg)
            "unk_12_16": FLOAT,
            "unk_16_20": FLOAT,
        },
    },
    (2003, 77): {
        "alias": "Unknown_2003_77",
        "docstring": "TODO",
        "args": {
            "entity_id": INT,  # TODO: sometimes zero
        },
    },
    (2003, 78): {
        "alias": "Unknown_2003_78",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,
            "unk_4_8": FLOAT,
        },
    },
    (2003, 79): {
        "alias": "Unknown_2003_79",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: always zero
        },
    },
    (2003, 80): {
        "alias": "Unknown_2003_80",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,
        },
    },
    (2003, 81): {
        "alias": "Unknown_2003_81",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: used once with 108 and once with 109 (could be B)
        },
    },
    (2003, 82): {
        "alias": "Unknown_2003_82",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
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
            "patrol_information_id": INT | {"internal_default": -1},
        },
    },
    (2004, 50): {
        "alias": "SetLockOnPoint",
        "docstring": """
            Presumably changes the point that is locked on to by the player.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "lock_on_model_point": INT,
            "state": BOOL,
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
        "alias": "Unknown_2004_60",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "obj": NO_DEFAULT(ObjectTyping),
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
        "alias": "Unknown_2004_63",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: always zero
            "unk_4_8": FLOAT,
        },
    },
    (2004, 67): {
        "alias": "Unknown_2004_67",
        "docstring": "Possibly 'attaches' second entity to first character?",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "entity": NO_DEFAULT(CoordEntityTyping),  # TODO: More limited type?
        },
    },
    (2004, 68): {
        "alias": "AttachObjectToCharacter",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "model_point": INT | {"internal_default": -1},  # TODO: can't use default with `obj` after it
            "obj": NO_DEFAULT(ObjectTyping),
        },
    },
    (2004, 69): {
        "alias": "Unknown_2004_69",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: always zero
            "unk_4_8": INT,  # TODO: always zero
        },
    },
    (2004, 70): {
        "alias": "Unknown_2004_70",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,
            "unk_4_8": INT,  # TODO: always 1
        },
    },
    (2004, 71): {
        "alias": "Unknown_2004_71",
        "docstring": "Unknown. Called once, with all zeroes.",
        "args": {
            "unk_0_4": INT,
            "unk_4_8": INT,
            "unk_8_12": INT,
        },
    },
    (2004, 73): {
        "alias": "Unknown_2004_73",
        "docstring": "TODO",
        "args": {
            "entity": NO_DEFAULT(CoordEntityTyping),
            "unk_4_8": INT,  # TODO: seems to be always 1 or 0
        },
    },
    (2004, 74): {
        "alias": "Unknown_2004_74",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),  # TODO: usually PLAYER
            "unknown1": INT,
            "region": NO_DEFAULT(RegionTyping),
            "unknown2": INT,  # TODO: Always -1?
            "character_2": NO_DEFAULT(CharacterTyping),  # TODO: usually zero or PLAYER
            "unknown3": INT,
            "unknown4": INT,
        },
    },
    (2004, 75): {
        "alias": "Unknown_2004_75",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),  # TODO: always PLAYER
            "unknown1": INT,
            "unknown2": INT,
        },
    },
    (2004, 76): {
        "alias": "Unknown_2004_76",
        "docstring": "TODO",
        "args": {
            "flag": FLAG,  # TODO: always zero
            "item_lot": INT,  # TODO: always zero
        },
    },
    (2004, 77): {
        "alias": "Unknown_2004_77",
        "docstring": "TODO",
        "args": {
            "unknown1": FLOAT,
            "unknown2": FLOAT,
            "unknown3": INT,  # TODO: always 0 or 1
            "unknown4": FLOAT,
        },
    },
    (2004, 78): {
        "alias": "Unknown_2004_78",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: always zero?
            "unk_4_8": INT,
            "unk_8_12": INT,
        },
    },
    (2004, 79): {
        "alias": "Unknown_2004_79",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: 0 or 1
            "unk_4_8": INT,  # TODO: always 3
        },
    },
    (2004, 80): {
        "alias": "Unknown_2004_80",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: 0 or 1
        },
    },
    (2004, 81): {
        "alias": "Unknown_2004_81",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
        },
    },
    (2004, 83): {
        "alias": "Unknown_2004_83",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "unk_4_8": INT,  # TODO: 1
        },
    },
    (2004, 84): {
        "alias": "Unknown_2004_84",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "unk_4_8": FLOAT,  # TODO: once with 220.0
            "unk_8_12": FLOAT,  # TODO: once with 40.0
        },
    },

    (2005, 17): {
        "alias": "Unknown_2005_17",
        "docstring": "TODO",
        "args": {
            "obj_1": NO_DEFAULT(ObjectTyping),  # TODO: once with 0
            "obj_2": NO_DEFAULT(ObjectTyping),  # TODO: once with 0
        },
    },
    (2005, 18): {
        "alias": "Unknown_2005_18",
        "docstring": "TODO",
        "args": {
            "obj_1": NO_DEFAULT(ObjectTyping),
            "obj_2": NO_DEFAULT(ObjectTyping),
            "unk_8_12": INT,  # TODO: always 151
        },
    },
    (2005, 19): {
        "alias": "DestroyObject_NoSlot",
        "docstring": """
            No 'slot' argument here.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping),
        },
    },
    (2005, 20): {
        "alias": "CreateBigHazardousObject",
        "docstring": "TODO",
        "args": {
            "obj_flag": FLAG,
            "obj": INT,
            "model_point_start": INT | {"internal_default": -1},
            "model_point_end": INT | {"internal_default": -1},
            "behaviour_id": INT,
            "target_type": NO_DEFAULT(DamageTargetType),
            "radius": FLOAT,
            "life": FLOAT,
            "repetition_time": FLOAT,
        },
    },

    (2006, 6): {
        "alias": "SetUnknownVFX_06",
        "docstring": "Not known if argument is a VFX Event ID or an absolute VFX asset ID.",
        "args": {
            "vfx_id": INT,
        },
    },

    (2007, 10): {
        "alias": "DisplayDialogAndSetFlags",
        "docstring": """
            Displays a dialog and enables one of three flags, depending on the player's response. Very useful.
        """,
        "args": {
            "message": NO_DEFAULT(EventTextTyping),
            "button_type": NO_DEFAULT(ButtonType),
            "number_buttons": NO_DEFAULT(NumberButtons),
            "anchor_entity": NO_DEFAULT(CoordEntityTyping) | {"internal_default": -1},
            "display_distance": FLOAT,
            "left_flag": FLAG,
            "right_flag": FLAG,
            "cancel_flag": FLAG,
        },
    },
    (2007, 12): {
        "alias": "DisplayUnknownMessage_12",
        "docstring": "Appears to be a variant of DisplayBattlefieldMessage.",
        "args": {
            "text": NO_DEFAULT(EventTextTyping),
            "unknown1": INT,
        },
    },
    (2007, 13): {
        "alias": "DisplayUnknownMessage_13",
        "docstring": "TODO",
        "args": {
            "text": NO_DEFAULT(EventTextTyping),  # TODO: used once with 0
        },
    },
    (2007, 14): {
        "alias": "DisplayUnknownMessage_14",
        "docstring": "TODO",
        "args": {
            "text": NO_DEFAULT(EventTextTyping),
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
        "alias": "DisplayUnknownMessage_16",
        "docstring": "TODO",
        "args": {
            "text": NO_DEFAULT(EventTextTyping),
            "unknown2": INT,
        },
    },

    (2008, 4): {
        "alias": "UnknownCamera_4",
        "docstring": """
            Very common camera instruction with unknown purpose.
            First argument is often 5.0 but can also be negative, so is probably not a distance. 
            Second argument could be an angle (between -180 and 180).
        """,
        "args": {
            "unknown1": FLOAT,
            "unknown2": FLOAT,
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

    (2010, 7): {
        "alias": "SuppressSoundEvent",
        "docstring": "TODO",
        "args": {
            "sound_id": INT,
            "unk_4_8": INT,
            "suppression_active": BOOL,
        },
    },
    (2010, 8): {
        "alias": "UnknownSound_2010_8",
        "docstring": "TODO",
        "args": {
            "sound_id": INT,
        },
    },
    (2010, 10): {
        "alias": "UnknownSound_2010_10",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,
            "unk_4_8": INT,
        },
    },
    (2010, 11): {
        "alias": "UnknownSound_2010_11",
        "docstring": "TODO",
        "args": {
            "unk_0_4": FLOAT,  # TODO: usually 5.0
        },
    },
    (2010, 12): {
        "alias": "UnknownSound_2010_12",
        "docstring": "TODO",
        "args": {
            "entity_id": NO_DEFAULT(CoordEntityTyping) | {"internal_default": 2},
            "unk_4_8": INT,
        },
    },

    (2011, 2): {
        "alias": "UnknownCollision_2011_2",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,  # TODO: once 0
            "unk_4_8": INT,  # TODO: once 0
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
        "alias": "UnknownMap_11",
        "docstring": "TODO",
        "args": {
            "unk_0_4": INT,
            "unk_4_8": FLOAT,
        },
    },
    (2012, 12): {
        "alias": "UnknownMap_12",
        "docstring": "TODO",
        "args": {
            "unk_0_4": FLOAT,
        },
    },
}


add_common_emedf_info(EMEDF, PACKAGE_PATH("eldenring/events/emevd/er-common.emedf.json"))
EMEDF_ALIASES, EMEDF_TESTS = build_emedf_aliases_tests(EMEDF)

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
    "PlayerHasRing": {
        "if": "IfPlayerHasRing",
    },
    "PlayerHasGood": {
        "if": "IfPlayerHasGood",
    },
}

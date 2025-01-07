"""Dictionary that maps EMEVD instructions `(category, index)` to Soulstruct aliases and "prebaked" variants.

Used in tandem with `*.emedf.json` to compile/decompile EVS <-> EMEVD scripts.
"""
from __future__ import annotations

__all__ = ["EMEDF", "EMEDF_ALIASES", "EMEDF_TESTS", "EMEDF_COMPARISON_TESTS"]

import typing as tp

from soulstruct.base.events.emevd.emedf import *
from soulstruct.darksouls1ptde.maps.constants import get_map_variable_name
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.utilities.files import PACKAGE_PATH
from ..enums import *


EVENT_RETURN_TYPE = {
    "type": EventReturnType,
    "default": None,
}
FLAG_SETTING = {
    "type": FlagSetting,
    "default": None,
    "hide_name": True,
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
GAME_MAP_EVS = {
    "type": MapTyping,
    "default": None,
    "to_evs": lambda args: get_map_variable_name((args["area_id"], args["block_id"])),
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
        "input_output_condition_kwargs": ("input_condition", "condition"),  # TODO: remove
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
        "input_output_condition_kwargs": ("", "condition"),  # TODO: remove
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
    (3, 0): {
        "alias": "IfFlagState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": FLAG_SETTING,
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
            Not sure if this works for objects.
        """,
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "character": NO_DEFAULT(AnimatedEntityTyping) | HIDE_NAME,
            "region": NO_DEFAULT(RegionTyping),
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
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "entity": NO_DEFAULT(CoordEntityTyping),
            "other_entity": NO_DEFAULT(CoordEntityTyping),
            "radius": FLOAT,
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
            "dummy_id": DUMMY_ID,
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
            "dummy_id": {},
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
            "state": {
                "type": MultiplayerState,
                "default": None,
            },
        },
        "partials": {
            "IfHost": dict(state=MultiplayerState.Host),
            "IfClient": dict(state=MultiplayerState.Client),
            "IfMultiplayer": dict(state=MultiplayerState.Multiplayer),
            "IfSingleplayer": dict(state=MultiplayerState.Singleplayer),
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
    (3, 11): {
        "alias": "IfWorldTendencyComparison",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "world_tendency_type": {
                "type": WorldTendencyType,
                "default": None,
            },
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": INT,
        },
        "partials": {
            "IfWhiteWorldTendencyComparison": dict(world_tendency_type=WorldTendencyType.White),
            "IfBlackWorldTendencyComparison": dict(world_tendency_type=WorldTendencyType.Black),
            "IfWhiteWorldTendencyGreaterThan": dict(
                world_tendency_type=WorldTendencyType.White, comparison_type=ComparisonType.GreaterThan
            ),
            "IfBlackWorldTendencyGreaterThan": dict(
                world_tendency_type=WorldTendencyType.Black, comparison_type=ComparisonType.GreaterThan
            ),
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
            "dummy_id": DUMMY_ID,
            "max_distance": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 2.0,
            },
            "prompt_text": {
                "type": EventTextTyping,
                "default": None,
            },
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
            "dummy_id": {},
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
            "dummy_id": DUMMY_ID,
            "max_distance": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 2.0,
            },
            "prompt_text": {
                "type": EventTextTyping,
                "default": None,
            },
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
            "dummy_id": {},
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
            "dummy_id": DUMMY_ID,
            "max_distance": {
                "type": float,
                "default": lambda args: 0.0 if args["anchor_type"] == CoordEntityType.Region else 2.0,
            },
            "prompt_text": {
                "type": EventTextTyping,
                "default": None,
            },
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
            "dummy_id": {},
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
            "is_owned": {
                "type": bool,
                "default": None,
            },
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
        "alias": "IfHealthRatioComparison",
        "docstring": "Conditions upon a comparison to character health ratio (0-1).",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "comparison_type": COMPARISON_TYPE | HIDE_NAME,
            "value": FLOAT,
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
            "character_type": {
                "type": CharacterType,
                "default": None,
            },
        },
        "partials": {
            "IfCharacterIsHuman": dict(character_type=CharacterType.Human),
            "IfCharacterIsWhitePhantom": dict(character_type=CharacterType.WhitePhantom),
            "IfCharacterIsHollow": dict(character_type=CharacterType.Hollow),
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
            "ai_status": {
                "type": AIStatusType,
                "default": None,
            },
        },
    },
    (4, 10): {
        "alias": "IfSkullLanternState",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "IfSkullLanternActive": dict(state=True),
            "IfSkullLanternInactive": dict(state=False),
        },
    },
    (4, 11): {
        "alias": "IfPlayerClass",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "class_type": {
                "type": ClassType,
                "default": None,
                "hide_name": True,
            },
        },
    },
    (4, 12): {
        "alias": "IfPlayerCovenant",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "covenant": {
                "type": Covenant,
                "default": None,
                "hide_name": True,
            },
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
            "state": FLAG_SETTING,
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
            "state": FLAG_SETTING,
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
            "event_return_type": EVENT_RETURN_TYPE,
            "state": FLAG_SETTING,
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
    (1003, 5): {
        "alias": "SkipLinesIfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": {
                "type": MultiplayerState,
                "default": None,
            },
        },
        "partials": {
            "SkipLinesIfHost": dict(state=MultiplayerState.Host),
            "SkipLinesIfClient": dict(state=MultiplayerState.Client),
            "SkipLinesIfMultiplayer": dict(state=MultiplayerState.Multiplayer),
            "SkipLinesIfSingleplayer": dict(state=MultiplayerState.Singleplayer),
        },
    },
    (1003, 6): {
        "alias": "ReturnIfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "event_return_type": EVENT_RETURN_TYPE,
            "state": {
                "type": MultiplayerState,
                "default": None,
            },
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
            "EndIfSingleplayer": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.Singleplayer,
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
            "RestartIfSingleplayer": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Singleplayer,
            ),
        },
    },
    (1003, 7): {
        "alias": "SkipLinesIfMapPresenceState",
        "docstring": "TODO",
        "args": {
            "line_count": INT | HIDE_NAME,
            "state": BOOL | HIDE_NAME,
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
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
    (1005, 0): {
        "alias": "AwaitObjectDestructionState",
        "docstring": "TODO",
        "args": {
            "state": BOOL | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
        },
        "partials": {
            "AwaitObjectDestroyed": dict(state=True),
            "AwaitObjectNotDestroyed": dict(state=False),
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
            "event_id": {},
            "slot": {},
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
    (2002, 1): {
        "alias": "PlayCutsceneToAll",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
        },
    },
    (2002, 2): {
        "alias": "PlayCutsceneAndMovePlayer",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "move_to_region": NO_DEFAULT(RegionTyping),
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
        },
        "evs_args": {
            "cutscene_id": {},
            "cutscene_flags": {},
            "move_to_region": {},
            "game_map": GAME_MAP_EVS,
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
        "alias": "PlayCutsceneAndMoveSpecificPlayer",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "move_to_region": NO_DEFAULT(RegionTyping),
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "player_id": INT,
        },
        "evs_args": {
            "cutscene_id": {},
            "cutscene_flags": {},
            "move_to_region": {},
            "game_map": GAME_MAP_EVS,
            "player_id": {},
        },
    },
    (2002, 5): {
        "alias": "PlayCutsceneAndRotatePlayer",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT,
            "cutscene_flags": CUTSCENE_FLAGS,
            "relative_rotation_axis_x": FLOAT | {"default": 0.0},
            "relative_rotation_axis_z": FLOAT | {"default": 0.0},
            "rotation": FLOAT | {"default": 0.0},
            "vertical_translation": FLOAT | {"default": 0.0},
            "player_id": {
                "type": int,
                "default": PLAYER,
            },
        },
    },
    (2003, 1): {
        "alias": "RequestAnimation",
        "docstring": """
            Not used very often, in favor of ForceAnimation below.
        """,
        "args": {
            "entity": NO_DEFAULT(AnimatedEntityTyping) | HIDE_NAME,
            "animation_id": INT,
            "loop": BOOL | {"default": False},
            "wait_for_completion": BOOL | {"default": False},
        },
    },
    (2003, 2): {
        "alias": "SetFlagState",
        "docstring": """
            Enable, disable, or toggle (change) a binary flag.
        """,
        "args": {
            "flag": FLAG | HIDE_NAME,
            "state": FLAG_SETTING,
        },
        "partials": {
            "EnableFlag": dict(state=FlagSetting.On),
            "DisableFlag": dict(state=FlagSetting.Off),
            "ToggleFlag": dict(state=FlagSetting.Change),
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
    # TODO: Could not find [2003, 6]: (De)activate Map Hit. Seems redundant with (2011, 1).
    # TODO: Could not find [2003, 7]: Set Map Visibility. Seems redundant with (2012, 1).
    (2003, 8): {
        "alias": "SetEventState",
        "docstring": """
            Stop or restart a particular slot (default of 0) of the given event ID. Note that you cannot restart events 
            that have already ended.
        """,
        "args": {
            "event_id": INT,
            "event_slot": INT | {"default": 0},
            "event_return_type": EVENT_RETURN_TYPE,
        },
        "partials": {
            "StopEvent": dict(
                event_return_type=EventReturnType.End,
                __docstring="Force a running event to stop.",
            ),
            "RestartEvent": dict(
                event_return_type=EventReturnType.Restart,
                __docstring="""
                    Force a running event to restart. Note that the event must be active (i.e. not finished) for this 
                    to work. If you plan to have an event restarted, make sure it doesn't return until you no longer 
                    need it.
                """,
            ),
        },
        "evs_args": {
            "event_id": {},
            "event_return_type": {},
            "event_slot": {},
        }
    },
    # TODO: Could not find [2003, 9]: Invert Event Flag
    # TODO: Could not find [2003, 10]: Set Event Navimesh
    (2003, 11): {
        "alias": "SetBossHealthBarState",
        "docstring": """
            Note: slot number can be 0-1 in DS1.
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

                    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so 
                    only the first argument actually does anything. You're welcome to specify the name for clarity 
                    anyway (and vanilla events will show it when decompiled).
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
        "alias": "KillBoss",
        "docstring": """
            The name is slightly misleading, as this doesn't actually kill any entity. Instead, it marks that you have
            cleared an 'area', as defined by the Game Area params, and is always manually called in EMEVD when you kill 
            the boss of that area.

            Among other things, this awards your souls for killing the boss (which is why they are delayed and why the 
            game will keep trying to give them to you on map load) and prevents you from summoning other players.

            The Game Area params ID is generally identical to the entity ID of the appropriate boss. This is just 
            convention, but it's one you should stick to for a sensible setup (and for the name of the instruction to 
            make sense).
        """,
        "args": {
            "game_area_param_id": INT,
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
            "player_start": {
                "type": tp.Union[PlayerStart, int],
                "default": 0,  # unsigned
                "internal_default": -1,
            },
        },
        "evs_args": {
            "game_map": GAME_MAP_EVS,
            "player_start": {},
        },
    },
    (2003, 15): {
        "alias": "HandleMinibossDefeat",
        "docstring": """
            Called instead of `KillBoss` for bosses that aren't the final boss of the area.

            Not used in DS1, and I don't know what it would do.
        """,
        "args": {
            "miniboss_id": INT,
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
        },
    },
    (2003, 19): {
        "alias": "SetMapDrawParamSlot",
        "docstring": """
            Each map area (NOT each map) can have two sets of DrawParams (0 and 1), and this can be used to switch
            between them. Originally only used for Dark Anor Londo.

            Note that there's some funny business with how this works in m15 in Dark Souls Remastered, presumably 
            because the developers didn't want to bother modifying both slots when they re-did all the DrawParams.
        """,
        "args": {
            "map_area_id": INT,
            "draw_param_slot": INT,
        },
    },
    # TODO: Could not find [2003, 20]: Set Temporary Player Respawn Point
    (2003, 21): {
        "alias": "IncrementNewGameCycle",
        "docstring": """
            This is manually called at the end of the game. You can call it anytime, but note that there is no way to
            decrement it with events.

            The dummy argument is always 0 or 1; not sure if or how it matters.
        """,
        "args": {
            "dummy_arg": INT,
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
        },
    },
    (2003, 26): {
        "alias": "SetSoapstoneMessageState",
        "docstring": """
            Enable or disable developer message.
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
    # TODO: Could not find [2003, 27]: [[MISSING]]
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
    # TODO: Could not find [2003, 29]: Change World Tendency
    (2003, 30): {
        "alias": "SetVagrantSpawningState",
        "docstring": """
            Note inverted bool.
        """,
        "args": {
            "spawning_disabled": BOOL,
        },
        "partials": {
            "EnableVagrantSpawning": dict(spawning_disabled=False),  # Note reversed bool.
            "DisableVagrantSpawning": dict(spawning_disabled=True),
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
    (2003, 33): {
        "alias": "SetNextSnugglyTrade",
        "docstring": """
            Sets the flag for the next drop based on the item you deposit into the nest.
        """,
        "args": {
            "flag": FLAG,
        },
    },
    (2003, 34): {
        "alias": "SnugglyItemDrop",
        "docstring": """
            Makes Snuggly drop an item. There are complex limitations to this in the engine, so be careful. (The list of
            available Snuggly flags is a hard-coded limit, for example.)
        """,
        "args": {
            "item_lot": {
                "type": ItemLotTyping,
                "default": None,
            },
            "region": NO_DEFAULT(RegionTyping),
            "flag": FLAG,
            "collision": NO_DEFAULT(CollisionTyping),
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
            "item_lot": INT,
        },
    },
    (2003, 37): {
        "alias": "ArenaRankingRequest1v1",
        "docstring": "TODO",
        "args": {},
    },
    (2003, 38): {
        "alias": "ArenaRankingRequest2v2",
        "docstring": "TODO",
        "args": {},
    },
    (2003, 39): {
        "alias": "ArenaRankingRequestFFA",
        "docstring": "TODO",
        "args": {},
    },
    (2003, 40): {
        "alias": "ArenaExitRequest",
        "docstring": "TODO",
        "args": {},
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
        "docstring": """
            Basic move. I recommend you use the combined `Move` function. Valid `dummy_id` MUST be supplied for 
            character destinations (and possibly objects) or no movement will occur.
        """,
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
            "special_effect": INT | HIDE_NAME,
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
                standby_exit_animation=-1,
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
        "alias": "FaceEntity",
        "docstring": """
            Rotate a character to face a target map entity of any type.
            WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at 
            least.)
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "target_entity": NO_DEFAULT(CoordEntityTyping),
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
            "overwrite_max": {
                "type": bool,
                "default": None,
            },
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
            "remove": {
                "type": bool,
                "default": None,
            },
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
            "is_disabled": {
                "type": bool,
                "default": None,
            },
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
            "is_fixed": {
                "type": bool,
                "default": None,
            },
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
    (2004, 36): {
        "alias": "HellkiteBreathControl",
        "docstring": """
            I don't recommend you mess with this. It seems to be used to create the fire VFX and damaging effect when 
            the Hellkite breathes fire on the bridge, with (otherwise invisible) object model o1060. It may simply 
            trigger a certain behavior param ID.

            Unclear whether the animation applies to the character or object (which is probably an invisible "burning" 
            plane).
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "obj": NO_DEFAULT(ObjectTyping),
            "animation_id": INT,
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
    (2004, 45): {
        "alias": "HumanityRegistration",
        "docstring": """
            I believe this designates the first event flag in a range of eight, which tracks how much humanity an NPC 
            has for draining with Dark Hand. These flags are all in the 8000 range, and tightly packed, so you'll need 
            to find your own range if you want to replicate this.

            I can confirm that NOT doing this for a new NPC means you can't drain any humanity from them, rather than 
            being able to drain unlimited humanity.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "event_flag": FLAG,
        },
    },
    (2004, 46): {
        "alias": "IncrementPvPSin",
        "docstring": """
            Normally only happens when you kill an NPC.
        """,
        "args": {
            "dummy": INT | {"default": 0},
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
            params you give it. The dummy_id determines which part of the object is hazardous (with the given radius 
            and life, relative to the time this instruction occurs).

            An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.

            'target_type' determines what the hazard can damage (Character and/or Map).
        """,
        "args": {
            "obj_flag": FLAG,
            "obj": NO_DEFAULT(ObjectTyping),
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
    (2005, 10): {
        "alias": "RegisterStatue",
        "docstring": """
            Creates a petrified or crystallized statue. I believe this is so it can be seen by other players online.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping),
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "statue_type": {
                "type": StatueType,
                "default": None,
            },
        },
        "evs_args": {
            "obj": {},
            "game_map": GAME_MAP_EVS,
            "statue_type": {},
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
            "dummy_id": DUMMY_ID,
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
        "alias": "CreateObjectVFX",
        "docstring": "TODO",
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | HIDE_NAME,
            "vfx_id": INT,
            "dummy_id": INT,
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
                "default": -1,
                "internal_default": -1,
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
            "banner_type": {
                "type": BannerType,
                "default": None,
                "hide_name": True,
            },
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
            "display_location_index": INT,
        },
    },
    (2007, 5): {
        "alias": "ArenaSetNametag1",
        "docstring": "TODO",
        "args": {
            "player_id": INT,
        },
    },
    (2007, 6): {
        "alias": "ArenaSetNametag2",
        "docstring": "TODO",
        "args": {
            "player_id": INT,
        },
    },
    (2007, 7): {
        "alias": "ArenaSetNametag3",
        "docstring": "TODO",
        "args": {
            "player_id": INT,
        },
    },
    (2007, 8): {
        "alias": "ArenaSetNametag4",
        "docstring": "TODO",
        "args": {
            "player_id": INT,
        },
    },
    (2007, 9): {
        "alias": "DisplayArenaDissolutionMessage",
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
        """,
        "args": {
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "camera_slot": INT,
        },
        "evs_args": {
            "game_map": GAME_MAP_EVS,
            "camera_slot": {},
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
    (2009, 1): {
        "alias": "InitializeWanderingDemon",
        "docstring": "Unused. Probably a Demon's Souls remnant.",
        "args": {
            "flag": FLAG,
            "demon_entity": NO_DEFAULT(CharacterTyping),  # guess
            "appearance_flag": FLAG,
        },
    },
    (2009, 2): {
        "alias": "RegisterWanderingDemon",
        "docstring": "Unused. Probably a Demon's Souls remnant.",
        "args": {
            "flag": FLAG,
            "demon_entity": NO_DEFAULT(CharacterTyping),  # guess
            "unknown_entity": NO_DEFAULT(CoordEntityTyping),  # guess
        },
    },
    (2009, 3): {
        "alias": "RegisterBonfire",
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
            "bonfire_flag": FLAG,
            "obj": NO_DEFAULT(ObjectTyping),
            "reaction_distance": {
                "type": float,
                "default": 2.0,
            },
            "reaction_angle": {
                "type": float,
                "default": 180.0,
            },
            "initial_kindle_level": INT | {"default": 0},
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
    (2009, 5): {
        "alias": "RegisterHealingFountain",
        "docstring": """
            No idea what this is. Clearly unused. The Bloodborne version has more arguments.
        """,
        "args": {
            "flag": FLAG,
            "obj": NO_DEFAULT(ObjectTyping),
        },
    },
    (2009, 6): {
        "alias": "NotifyBossBattleStart",
        "docstring": "Sends the message to all summons that the host has challenged the boss.",
        "args": {
            "dummy": INT | {"default": 0},
        },
    },
    (2010, 1): {
        "alias": "SetBackgroundMusic",
        "docstring": "TODO",
        "args": {
            "state": BOOL | HIDE_NAME,
            "music_slot": INT,
            "entity": NO_DEFAULT(CoordEntityTyping),
            "sound_type": {
                "type": SoundType,
                "default": None,
            },
            "sound_id": INT,
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
    (2010, 3): {
        "alias": "SetSoundEventState",
        "docstring": """
            The sound ID is in the MSB. Includes boss music, which is obviously the most common use, and ambiance.
        """,
        "args": {
            "sound_id": NO_DEFAULT(SoundEventTyping),
            "state": BOOL | HIDE_NAME,
        },
        "partials": {
            "EnableSoundEvent": dict(state=True),
            "DisableSoundEvent": dict(state=False),
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
}


add_common_emedf_info(EMEDF, PACKAGE_PATH("darksouls1ptde/events/emevd/ds1-common.emedf.json"))
EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS = build_emedf_aliases_tests(EMEDF)

# Extra tests that use custom instructions from `compiler` (to auto-detect certain arguments from argument types).
EMEDF_TESTS |= {
    "ActionButton": {
        "if": "IfActionButton",
    },
    "PlayerHasWeapon": {
        "if": "IfPlayerHasWeapon",
        "if_not": "IfPlayerDoesNotHaveWeapon",
    },
    "PlayerHasArmor": {
        "if": "IfPlayerHasArmor",
        "if_not": "IfPlayerDoesNotHaveArmor",
    },
    "PlayerHasRing": {
        "if": "IfPlayerHasRing",
        "if_not": "IfPlayerDoesNotHaveRing",
    },
    "PlayerHasGood": {
        "if": "IfPlayerHasGood",
        "if_not": "IfPlayerDoesNotHaveGood",
    },
    "PlayerDoesNotHaveWeapon": {
        "if": "IfPlayerDoesNotHaveWeapon",
        "if_not": "IfPlayerHasWeapon",
    },
    "PlayerDoesNotHaveArmor": {
        "if": "IfPlayerDoesNotHaveArmor",
        "if_not": "IfPlayerHasArmor",
    },
    "PlayerDoesNotHaveRing": {
        "if": "IfPlayerDoesNotHaveRing",
        "if_not": "IfPlayerHasRing",
    },
    "PlayerDoesNotHaveGood": {
        "if": "IfPlayerDoesNotHaveGood",
        "if_not": "IfPlayerHasGood",
    },
}

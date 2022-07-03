"""Dictionary that maps EMEVD instructions `(category, index)` to Soulstruct aliases and "prebaked" variants.

Used in tandem with `*.emedf.json` to compile/decompile EVS <-> EMEVD scripts.
"""
from __future__ import annotations

from soulstruct.base.events.emevd.emedf import *
from soulstruct.darksouls1ptde.events.emevd.emedf import EMEDF as PTDE_EMEDF
from soulstruct.darksouls1r.maps.constants import get_map_variable_name
from soulstruct.darksouls1r.game_types import *
from soulstruct.utilities.files import PACKAGE_PATH
from .enums import *

__all__ = ["EMEDF", "EMEDF_ALIASES"]


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
    "to_evs": lambda args: get_map_variable_name(args["area_id"], args["block_id"]),
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


# Bloodborne uses an extension of the PTDE instruction set.
EMEDF = PTDE_EMEDF | {
    (3, 6): {
        "alias": "IfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "condition": INT | HIDE_NAME,
            "state": NO_DEFAULT(MultiplayerState),
        },
        "partials": {
            "IfHost": dict(
                state=MultiplayerState.Host,
            ),
            "IfClient": dict(
                state=MultiplayerState.Client,
            ),
            "IfMultiplayer": dict(
                state=MultiplayerState.Multiplayer,
            ),
            "IfConnectingMultiplayer": dict(
                state=MultiplayerState.ConnectingMultiplayer,
            ),
            "IfSingleplayer": dict(
                state=MultiplayerState.Singleplayer,
            ),
        },
    },
    (3, 23): {
        "alias": "IfAttackedWithDamageType",
        "docstring": "TODO",
        "args": {
            "condition": INT | HIDE_NAME,
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
        "alias": "IfActionButtonParam",
        "docstring": "TODO",
        "args": {
            "condition": INT | HIDE_NAME,
            "action_button_id": INT | {"internal_default": -1},
            "entity": NO_DEFAULT(CoordEntityTyping) | {"internal_default": -1},
        },
    },
    (3, 25): {
        "alias": "IfPlayerArmorType",
        "docstring": "TODO",
        "args": {
            "condition": INT | HIDE_NAME,
            "armor_type": NO_DEFAULT(ArmorType),
            "required_armor_range_first": NO_DEFAULT(ArmorTyping),
            "required_armor_range_last": NO_DEFAULT(ArmorTyping),
        },
    },
    (3, 26): {
        "alias": "IfPlayerInsightAmountComparison",
        "docstring": "TODO",
        "args": {
            "condition": INT | HIDE_NAME,
            "value": INT,
            "comparison_type": NO_DEFAULT(ComparisonType),
        },
        "partials": {
            "IfPlayerInsightAmountEqual": dict(
                comparison_type=ComparisonType.Equal,
            ),
            "IfPlayerInsightAmountNotEqual": dict(
                comparison_type=ComparisonType.NotEqual,
            ),
            "IfPlayerInsightAmountGreaterThan": dict(
                comparison_type=ComparisonType.GreaterThan,
            ),
            "IfPlayerInsightAmountLessThan": dict(
                comparison_type=ComparisonType.LessThan,
            ),
            "IfPlayerInsightAmountGreaterThanOrEqual": dict(
                comparison_type=ComparisonType.GreaterThanOrEqual,
            ),
            "IfPlayerInsightAmountLessThanOrEqual": dict(
                comparison_type=ComparisonType.LessThanOrEqual,
            ),
        },
    },
    (3, 27): {
        "alias": "IfDialogChoice",
        "docstring": "TODO",
        "args": {
            "condition": INT | HIDE_NAME,
            "dialog_result": NO_DEFAULT(DialogResult),
        },
    },
    (3, 28): {
        "alias": "IfPlayGoState",
        "docstring": """
            Blocks off areas of the game (namely, beyond Father Gascoigne) that have not been downloaded/installed yet.
        """,
        "args": {
            "condition": INT | HIDE_NAME,
            "playgo_state": NO_DEFAULT(PlayGoState),
        },
    },
    (3, 29): {
        "alias": "IfClientTypeCountComparison",
        "docstring": """
            Value should only range between 0 and 4 (the maximum number of clients).
        """,
        "args": {
            "condition": INT | HIDE_NAME,
            "client_type": NO_DEFAULT(ClientType),
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
            "condition": INT | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping),
            "state": BOOL,
        },
        "partials": {
            "IfCharacterDrawGroupEnabled": dict(state=True),
            "IfCharacterDrawGroupDisabled": dict(state=False),
        }
    },
    (1000, 101): {
        "alias": "GotoIfConditionState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "required_state": BOOL,
            "input_condition": INT,
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
            "input_condition": INT,
        },
        "partials": {
            "GotoIfFinishedConditionTrue": dict(required_state=True),
            "GotoIfFinishedConditionFalse": dict(required_state=False),
        }
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
            "SkipLinesIfConnectingMultiplayer": dict(state=MultiplayerState.ConnectingMultiplayer),
            "SkipLinesIfSingleplayer": dict(state=MultiplayerState.Singleplayer),
        }
    },
    (1003, 6): {
        "alias": "ReturnIfMultiplayerState",
        "docstring": "TODO",
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
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
            "EndIfConnectingMultiplayer": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.ConnectingMultiplayer,
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
            "RestartIfConnectingMultiplayer": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.ConnectingMultiplayer,
            ),
            "RestartIfSingleplayer": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.Singleplayer,
            ),
        }
    },
    (1003, 9): {
        "alias": "SkipLinesIfCoopClientCountComparison",
        "docstring": """
            Value should be from 0 to 4.
        """,
        "args": {
            "skip_lines": INT,
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
    (1003, 11): {
        "alias": "SkipLinesIfPlayerGender",
        "docstring": "TODO",
        "args": {
            "skip_lines": INT,
            "gender": NO_DEFAULT(Gender),
        },
    },
    (1003, 12): {
        "alias": "GotoIfPlayerGender",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "gender": NO_DEFAULT(Gender),
        },
    },
    (1003, 13): {
        "alias": "ReturnIfPlayerGender",
        "docstring": "TODO",
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
            "gender": NO_DEFAULT(Gender),
        },
        "partials": {
            "EndIfPlayerGender": dict(event_return_type=EventReturnType.End),
            "RestartIfPlayerGender": dict(event_return_type=EventReturnType.Restart),
        },
    },
    (1003, 14): {
        "alias": "SkipLinesIfClientTypeCountComparison",
        "docstring": """
            Value from 0 to 4.
        """,
        "args": {
            "skip_lines": INT,
            "client_type": NO_DEFAULT(ClientType),
            "comparison_type": NO_DEFAULT(ComparisonType),
            "value": INT,
        },
    },
    (1003, 15): {
        "alias": "GotoIfClientTypeCountComparison",
        "docstring": """
            Value from 0 to 4.
        """,
        "args": {
            "label": LABEL,
            "client_type": NO_DEFAULT(ClientType),
            "comparison_type": NO_DEFAULT(ComparisonType),
            "value": INT,
        },
    },
    (1003, 16): {
        "alias": "ReturnIfClientTypeCountComparison",
        "docstring": """
            Value from 0 to 4.
        """,
        "args": {
            "event_return_type": NO_DEFAULT(EventReturnType),
            "client_type": NO_DEFAULT(ClientType),
            "comparison_type": NO_DEFAULT(ComparisonType),
            "value": INT,
        },
        "partials": {
            "EndIfClientTypeCountComparison": dict(event_return_type=EventReturnType.End),
            "RestartIfClientTypeCountComparison": dict(event_return_type=EventReturnType.Restart),
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
            "GotoIfMultiplayer": dict(state=MultiplayerState.Multiplayer),
            "GotoIfConnectingMultiplayer": dict(state=MultiplayerState.ConnectingMultiplayer),
            "GotoIfSingleplayer": dict(state=MultiplayerState.Singleplayer),
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
    (1005, 101): {
        "alias": "GotoIfObjectDestructionState",
        "docstring": "TODO",
        "args": {
            "label": LABEL,
            "obj": NO_DEFAULT(ObjectTyping),
            "state": BOOL | {"internal_default": -1},
        },
        "evs_args": {
            "label": {},
            "state": {},
            "obj": {},
        }
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
    (2002, 6): {
        "alias": "PlayCutsceneAndMovePlayerAndSetTimePeriod",
        "docstring": """
            Warp a particular player to a region and set the time period. I assume that this must be a map that is
            already loaded, like in DS1, but possibly not.

            It's used only twice: to play the cutscene when you first reach Cathedral Ward (time period 1) and when you 
            examine Laurence's skull after defeating Vicar Amelia (time period 2). It's NOT used after you defeat Rom, 
            when the blood moon begins. The time period ID may in fact be unused.
        """,
        "args": {
            "cutscene": INT | {"internal_default": -1},
            "cutscene_type": NO_DEFAULT(CutsceneFlags),
            "move_to_region": NO_DEFAULT(RegionTyping),
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
            "player_id": INT | {"internal_default": -1},
            "time_period_id": INT,
        },
        "evs_args": {
            "cutscene": {},
            "cutscene_type": {},
            "move_to_region": {},
            "game_map": GAME_MAP_EVS,
            "time_period_id": {},
        },
    },
    (2002, 7): {
        "alias": "PlayCutsceneAndSetTimePeriod",
        "docstring": """
            Probably used when you examine Laurence's skull, etc.
        """,
        "args": {
            "cutscene": INT | {"internal_default": -1},
            "cutscene_type": NO_DEFAULT(CutsceneFlags),
            "player_id": INT | {"internal_default": -1},
            "time_period_id": INT,
        },
    },
    (2002, 8): {
        "alias": "PlayCutsceneAndMovePlayer_Dummy",
        "docstring": "Likely not used, doesn't even take a cutscene ID argument.",
        "args": {
            "move_to_region": NO_DEFAULT(RegionTyping),
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
        },
        "evs_args": {
            "move_to_region": {},
            "game_map": GAME_MAP_EVS,
        },
    },
    (2003, 11): {
        "alias": "SetBossHealthBarState",
        "docstring": """
                Note: slot number can be 0-2 in BB.
            """,
        "args": {
            "state": BOOL | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "slot": INT | {"default": 0},
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
            "slot": {},
        },
    },
    (2003, 15): {
        "alias": "HandleMinibossDefeat",
        "docstring": """
            Called instead of `KillBoss` for bosses that aren't the final boss of the area.
            
            Note that outside of Chalice Dungeons, this is ONLY used when you have defeated Gehrman and are about to 
            fight Moon Presence.
        """,
        "args": {
            "miniboss_id": INT,
        },
    },
    (2003, 27): {
        "alias": "Unknown_2003_27",
        "docstring": """
            No information. Used exactly once, after the cutscene that played when Ludwig's first phase was defeated 
            with the Old Hunters DLC demo flag enabled. Unknown effect. Maybe just terminated the whole DLC demo.
        """,
        "args": {
            "arg1": INT,
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
    (2003, 44): {
        "alias": "SetDirectionDisplayState",
        "docstring": """
            Not sure what this is.
        """,
        "args": {
            "state": BOOL,
        },
        "partials": {
            "EnableDirectionDisplayState": dict(state=True),
            "DisableDirectionDisplayState": dict(state=False),
        },
    },
    (2003, 45): {
        "alias": "SetMapHitGridCorrespondence",
        "docstring": "TODO",
        "args": {
            "collision": NO_DEFAULT(CollisionTyping),
            "level": INT,
            "grid_coord_x": INT,
            "grid_coord_y": INT,
            "state": BOOL,
        },
        "partials": {
            "EnableMapHitGridCorrespondence": dict(state=True),
            "DisableMapHitGridCorrespondence": dict(state=False),
        },
    },
    (2003, 46): {
        "alias": "SetMapContentImageDisplayState",
        "docstring": "TODO",
        "args": {
            "content_image_part_id": INT,
            "state": BOOL,
        },
    },
    (2003, 47): {
        "alias": "SetMapBoundariesDisplay",
        "docstring": "TODO",
        "args": {
            "hierarchy": INT,
            "grid_coord_x": INT,
            "grid_coord_y": INT,
            "state": BOOL,
        },
    },
    (2003, 48): {
        "alias": "SetAreaWind",
        "docstring": "TODO",
        "args": {
            "region": NO_DEFAULT(RegionTyping),
            "state": BOOL,
            "duration": FLOAT,
            "wind_parameter_id": INT,
        },
    },
    (2003, 49): {
        "alias": "WarpPlayerToRespawnPoint",
        "docstring": "TODO",
        "args": {
            "respawn_point_id": INT | HIDE_NAME,
        },
    },
    (2003, 50): {
        "alias": "StartEnemySpawner",
        "docstring": "TODO",
        "args": {
            "spawner_id": INT | {"internal_default": -1},
        },
    },
    (2003, 51): {
        "alias": "SummonNPC",
        "docstring": "TODO",
        "args": {
            "sign_type": NO_DEFAULT(SingleplayerSummonSignType) | HIDE_NAME,
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "region": NO_DEFAULT(RegionTyping),
            "summon_flag": NO_DEFAULT(FlagInt),
            "dismissal_flag": NO_DEFAULT(FlagInt),
        },
    },
    (2003, 52): {
        "alias": "InitializeWarpObject",
        "docstring": "TODO",
        "args": {
            "warp_object_id": INT,
        },
    },
    (2003, 53): {
        "alias": "BossDefeat",
        "docstring": """
            Handle boss defeat and display banner. 'boss_id' is probably similar to GameAreaParam from DS1.
        """,
        "args": {
            "boss_id": INT,
            "banner_type": NO_DEFAULT(BannerType),
        },
    },
    (2003, 54): {
        "alias": "SendNPCSummonHome",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | {"internal_default": -1},
        },
    },
    (2004, 8): {
        "alias": "AddSpecialEffect",
        "docstring": """
            'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
            nothing if the character already has the special effect active (i.e. they do not stack or reset timers).
            
            The Bloodborne version has an additional argument that determines whether any HP changes caused by the 
            special effect should also affect NPC parts, which I set to `True` by default.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "special_effect_id": INT | HIDE_NAME,
            "affect_npc_part_hp": BOOL | {"default": True},
        },
    },
    (2004, 14): {
        "alias": "RotateToFaceEntity",
        "docstring": """
            Rotate a character to face a target map entity of any type.
            WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at
            least.)
            
            The Bloodborne version allows you to force an animation at the same time (post-rotation) and optionally wait
            until that animation is completed. (I assume a value of -1 avoids it.)
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "target_entity": NO_DEFAULT(CoordEntityTyping) | HIDE_NAME,
            "animation": INT | {"default": -1, "internal_default": -1},
            "wait_for_completion": BOOL | {"default": False},
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
        "alias": "SetDistanceLimitForConversationStateChanges",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "distance": FLOAT,
        },
    },
    (2004, 51): {
        "alias": "Test_RequestRagdollRestraint",
        "docstring": "TODO",
        "args": {
            "recipient_character": NO_DEFAULT(CharacterTyping),
            "recipient_target_rigid_index": INT,
            "recipient_model_point": INT,
            "attachment_character": NO_DEFAULT(CharacterTyping),
            "attachment_target_rigid_index": INT,
            "attachment_model_point": INT,
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
    (2004, 53): {
        "alias": "AdaptSpecialEffectHealthChangeToNPCPart",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | {"internal_default": -1},
        },
    },
    (2004, 54): {
        "alias": "SetGravityAndCollisionExcludingOwnWorld",
        "docstring": """
            I assume "own world" refers to the world you're hosting.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | {"internal_default": -1},
            "state": BOOL,
        },
    },
    (2004, 55): {
        "alias": "AddSpecialEffect_WithUnknownEffect",
        "docstring": """
            Unknown additional affect from the standard instruction, presumably.
        """,
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | HIDE_NAME,
            "special_effect": INT | HIDE_NAME,
            "affect_npc_parts_hp": BOOL | {"default": False},
        },
    },
    (2005, 16): {
        "alias": "ActivateObjectWithSpecificCharacter",
        "docstring": """
            The standard version of this 'grabs' the nearest character and uses them in the ObjAct (e.g. Patches pulling
            the lever in the Catacombs in DS1). I presume this version lets you specify which character should be 
            involved in the ObjAct.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | {"internal_default": -1},
            "objact_id": INT,
            "relative_index": INT,
            "character": NO_DEFAULT(CharacterTyping) | {"internal_default": -1},
        },
    },
    (2005, 17): {
        "alias": "SetObjectDamageShieldState",
        "docstring": """
            Not sure how this differs from object invulnerability.
        """,
        "args": {
            "obj": NO_DEFAULT(ObjectTyping) | {"internal_default": -1},
            "state": BOOL,
        },
    },
    (2009, 5): {
        "alias": "RegisterLantern",
        "docstring": """
            Register a Lantern. Used instead of the bonfire registration.
            
            No idea what the 'sword' arguments do, but they default to zero and are always zero when this is called.
        """,
        "args": {
            "flag": NO_DEFAULT(FlagInt),
            "obj": NO_DEFAULT(ObjectTyping),
            "reaction_distance": FLOAT,
            "reaction_angle": FLOAT,
            "initial_sword_number": INT | {"default": 0},
            "sword_level": INT | {"default": 0},
        },
    },
    (2010, 4): {
        "alias": "SetBossMusicState",
        "docstring": """
            Not sure how this differs from the standard map sound instructions, but my guess is that it fades the music 
            out rather than abruptly stopping it.
            
            TODO: Can probably be used to fade out ANY music. Not sure why it would only work for boss music.
            TODO: Argument -1 is sometimes used. Fades out ALL music?
        """,
        "args": {
            "sound_id": INT,
            "state": BOOL,
        },
        "partials": {
            "EnableBossMusic": dict(state=True),
            "DisableBossMusic": dict(state=False),
        },
    },
    (2010, 5): {
        "alias": "NotifyDoorEventSoundDampening",
        "docstring": """
            No idea what this is or what entity the first argument is. Probably the door object.
        """,
        "args": {
            "entity_id": INT,
            "state": NO_DEFAULT(DoorState),
        },
    },
    (2011, 3): {
        "alias": "SetCollisionResState",
        "docstring": """
            No idea what this is.
        """,
        "args": {
            "collision": NO_DEFAULT(CollisionTyping) | {"internal_default": -1},
            "state": BOOL,
        },
    },
    (2013, 1): {
        "alias": "CreatePlayLog",
        "docstring": "TODO",
        "args": {
            "name": NO_DEFAULT(StringOffsetTyping),
        },
    },
    (2013, 2): {
        "alias": "StartPlayLogMeasurement",
        "docstring": "TODO",
        "args": {
            "measurement_id": INT,
            "name": NO_DEFAULT(StringOffsetTyping),
            "overwrite": BOOL,
        },
    },
    (2013, 3): {
        "alias": "StopPlayLogMeasurement",
        "docstring": "TODO",
        "args": {
            "measurement_id": INT,
        },
    },
    (2013, 4): {
        "alias": "PlayLogParameterOutput",
        "docstring": "TODO",
        "args": {
            "category": NO_DEFAULT(PlayerPlayLogParameter),
            "name": NO_DEFAULT(StringOffsetTyping),
            "output_multiplayer_state": NO_DEFAULT(PlayLogMultiplayerType),
        },
    },
}


# Re-sort dictionary by (category, index).
EMEDF = {k: EMEDF[k] for k in sorted(EMEDF.keys())}


add_common_emedf_info(EMEDF, PACKAGE_PATH("bloodborne/events/emevd/bb-common.emedf.json"))

# Retrieve instruction information by EVS instruction alias name (or partial name).
EMEDF_ALIASES = {v["alias"]: (category, index, v) for (category, index), v in EMEDF.items()}
for (category, index), v in EMEDF.items():
    if "partials" in v:
        for partial_name in v["partials"]:
            EMEDF_ALIASES[partial_name] = (category, index, v)

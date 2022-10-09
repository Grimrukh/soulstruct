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

__all__ = ["EMEDF", "EMEDF_ALIASES", "EMEDF_TESTS", "EMEDF_COMPARISON_TESTS"]


EVENT_RETURN_TYPE = {
    "type": EventReturnType,
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
    "to_evs": lambda args: get_map_variable_name(args["area_id"], args["block_id"]),
}
FLAG = {
    "type": FlagInt,
    "default": None,
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


# DSR uses an extension of the PTDE instruction set.
EMEDF = PTDE_EMEDF | {
    (3, 6): {  # more partials for extended `MultiplayerState` enum
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
            "IfUnknownPlayerType4": dict(state=MultiplayerState.UnknownPlayerType4),
            "IfUnknownPlayerType5": dict(state=MultiplayerState.UnknownPlayerType5),
        },
    },
    (3, 23): {
        "alias": "If_Unknown_3_23",
        "docstring": "Unknown command. Second and third arguments appear to both always be zero.",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk1": INT,
            "unk2": INT,
        },
    },
    (3, 24): {
        "alias": "If_Unknown_3_24",
        "docstring": "'If Multiplayer Count', apparently.",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk1": INT,
            "unk2": INT,
        },
    },
    (4, 15): {
        "alias": "Unknown_4_15",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk1": INT,
        },
    },
    (4, 16): {
        "alias": "Unknown_4_16",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
            "unk1": INT,
            "unk2": INT,
            "unk3": INT,
        },
    },
    (4, 17): {
        "alias": "IfArenaMatchmaking",
        "docstring": "TODO",
        "args": {
            "condition": CONDITION_GROUP | HIDE_NAME,
        },
    },
    (1003, 5): {  # more partials for extended `MultiplayerState` enum
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
            "SkipLinesIfUnknownPlayerType4": dict(state=MultiplayerState.UnknownPlayerType4),
            "SkipLinesIfUnknownPlayerType5": dict(state=MultiplayerState.UnknownPlayerType5),
        },
    },
    (1003, 6): {  # more partials for extended `MultiplayerState` enum
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
            "EndIfUnknownPlayerType4": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.UnknownPlayerType4,
            ),
            "EndIfUnknownPlayerType5": dict(
                event_return_type=EventReturnType.End,
                state=MultiplayerState.UnknownPlayerType5,
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
            "RestartIfUnknownPlayerType4": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.UnknownPlayerType4,
            ),
            "RestartIfUnknownPlayerType5": dict(
                event_return_type=EventReturnType.Restart,
                state=MultiplayerState.UnknownPlayerType5,
            ),
        },
    },
    (2000, 6): {
        "alias": "Unknown_2000_6",
        "docstring": "TODO",
        "args": {
            "unk1": INT,
        },
    },
    (2002, 6): {
        "alias": "PlayCutsceneAndRandomlyWarpPlayer_2002_6",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT | HIDE_NAME,
            "cutscene_flags": CUTSCENE_FLAGS,
            "first_region": NO_DEFAULT(RegionTyping),
            "last_region": NO_DEFAULT(RegionTyping),
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
        },
        "evs_args": {
            "cutscene_id": {},
            "cutscene_flags": {},
            "first_region": {},
            "last_region": {},
            "game_map": GAME_MAP_EVS,
        },
    },
    (2002, 7): {
        "alias": "PlayCutsceneAndRandomlyWarpPlayer_2002_7",
        "docstring": "TODO",
        "args": {
            "cutscene_id": INT | HIDE_NAME,
            "cutscene_flags": CUTSCENE_FLAGS,
            "first_region": NO_DEFAULT(RegionTyping),
            "last_region": NO_DEFAULT(RegionTyping),
            "area_id": AREA_ID,
            "block_id": BLOCK_ID,
        },
        "evs_args": {
            "cutscene_id": {},
            "cutscene_flags": {},
            "first_region": {},
            "last_region": {},
            "game_map": GAME_MAP_EVS,
        },
    },
    (2003, 42): {
        "alias": "CopyEventValue",
        "docstring": "TODO",
        "args": {
            "source_flag": FLAG,
            "destination_flag": FLAG,
            "bit_count": BIT_COUNT,
        },
    },
    (2003, 43): {
        "alias": "Unknown_2003_43",
        "docstring": "TODO",
        "args": {
            "flag": FLAG,
            "bit_count": BIT_COUNT,
            "unk1": INT,
            "unk2": INT,
        },
    },
    (2003, 44): {
        "alias": "ForceAnimation_Unknown_2003_44",
        "docstring": "TODO",
        "args": {
            "entity": NO_DEFAULT(AnimatedEntityTyping),
            "animation": INT,
            "loop": BOOL,
            "wait_for_completion": BOOL,
            "skip_transition": BOOL,
            "unk1": INT,
        },
    },
    (2003, 46): {
        "alias": "ForceAnimation_Unknown_2003_46",
        "docstring": "TODO",
        "args": {
            "entity": NO_DEFAULT(AnimatedEntityTyping),
            "animation": INT,
            "loop": BOOL,
            "wait_for_completion": BOOL,
            "skip_transition": BOOL,
            "unk1": INT,
        },
    },
    (2003, 47): {
        "alias": "Unknown_2003_47",
        "docstring": "TODO",
        "args": {},
    },
    (2003, 48): {
        "alias": "Unknown_2003_48",
        "docstring": "TODO",
        "args": {
            "entity": NO_DEFAULT(AnimatedEntityTyping),
            "unk1": INT,
            "model_point": INT,
            "magic_id": INT,
            "launch_angle_x": INT,
            "launch_angle_y": INT,
            "launch_angle_z": INT,
        },
    },
    (2003, 49): {
        "alias": "EraseNPCSummonSign",
        "docstring": "TODO",
        "args": {
            "summoned_character": NO_DEFAULT(CharacterTyping)
        },
    },
    (2004, 48): {
        "alias": "FadeOutCharacter",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "duration": FLOAT,
        },
    },
    (2004, 49): {
        "alias": "FadeInCharacter",
        "docstring": "TODO",
        "args": {
            "character": NO_DEFAULT(CharacterTyping),
            "duration": FLOAT,
        },
    },
    (2004, 50): {
        "alias": "Unknown_2004_50",
        "docstring": "TODO",
        "args": {},
    },
    (2004, 51): {
        "alias": "Unknown_2004_51",
        "docstring": "TODO",
        "args": {
            "unk1": INT,
        },
    },
    (2004, 52): {
        "alias": "Unknown_2004_52",
        "docstring": "TODO",
        "args": {},
    },
    (2007, 10): {
        "alias": "ArenaSetNametag5",
        "docstring": "TODO",
        "args": {
            "player_id": INT,
        },
    },
    (2007, 11): {
        "alias": "ArenaSetNametag6",
        "docstring": "TODO",
        "args": {
            "player_id": INT,
        },
    },
    (2007, 12): {
        "alias": "DisplayConcatenatedMessage",
        "docstring": "TODO",
        "args": {
            "message_id": INT,
            "pad_enabled": BOOL,
            "concatenator_base_flag": FLAG,
            "bit_count": BIT_COUNT,
        },
    },
    (2007, 13): {
        "alias": "Unknown_2007_13",
        "docstring": "TODO",
        "args": {
            "unk1": INT,
        },
    },
    (2008, 4): {
        "alias": "Unknown_2008_04",
        "docstring": "TODO",
        "args": {}
    },
}


# Re-sort dictionary by (category, index) BEFORE adding Nightfall additions.
EMEDF = {k: EMEDF[k] for k in sorted(EMEDF.keys())}


# NIGHTFALL ADDITIONS
# These require the special Nightfall DLL to work and are here for my dev purposes. They occupy unused instruction
# indices in category 2009. Do not try to use them yourself!
EMEDF |= {
    (2009, 7): {
        "alias": "NightfallSendToScript",
        "docstring": "Special instruction added by Horkrux for communication with `DarkSoulsScripting.dll`.",
        "args": {
            "int1": INT | {"internal_type": ArgType.s32},
            "int2": INT | {"internal_type": ArgType.s32},
            "float1": FLOAT | {"internal_type": ArgType.f32},
            "float2": FLOAT | {"internal_type": ArgType.f32},
        },
    },
    (2009, 10): {
        "alias": "NightfallSetSpecialMovement",
        "docstring": "Special instruction added by Meowmaritus for initiating [redacted] in Nightfall.",
        "args": {
            "character": NO_DEFAULT(CharacterTyping) | {"internal_type": ArgType.s32},
            "movement_type": INT | {"internal_type": ArgType.s32},
            "is_active": NO_DEFAULT(OnOffChange) | {"internal_type": ArgType.u8},
        },
        "arg_types": "iiB",
    },
    (2009, 11): {
        "alias": "NightfallClearSpecialMovement",
        "docstring": "Special instruction added by Meowmaritus for stopping [redacted] in Nightfall.",
        "args": {},
        "arg_types": "",
    },
    (2009, 12): {
        "alias": "NightfallCameraResetRequest",
        "docstring": "Special instruction added by Meowmaritus for immediate camera manipulation in Nightfall.",
        "args": {},
        "arg_types": "",
    },
}


add_common_emedf_info(EMEDF, PACKAGE_PATH("darksouls1ptde/events/emevd/ds1-common.emedf.json"))
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
    "PlayerHasRing": {
        "if": "IfPlayerHasRing",
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
    "PlayerDoesNotHaveRing": {
        "if": "IfPlayerDoesNotHaveRing",
    },
    "PlayerDoesNotHaveGood": {
        "if": "IfPlayerDoesNotHaveGood",
    },
}

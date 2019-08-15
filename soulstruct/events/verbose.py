# -*- coding: utf-8 -*-


def get_game_map(area_id, block_id, game_module):
    """ Attempts to get the name of the game map. """
    try:
        area_id = int(area_id)
        block_id = int(block_id)
    except ValueError:
        # Event arg replacement(s).
        return "<VARIABLE>"
    return game_module.verbose.MAP_NAMES.get((int(area_id), int(block_id)), 'UNKNOWN')


ENUM_RESTART_TYPE = {
    0: "Never",
    1: "On Rest",
    2: "UNKNOWN (Skeletons)",
}

ENUM_SOUND_TYPE = {
    0: "a: Ambience",
    1: "c: Character Motion",
    2: "f: Menu SE",
    3: "o: Object",
    4: "p: Cutscene",
    5: "s: SFX",
    6: "m: Music",
    7: "v: Voice",
    8: "x: Floor Material Dependence",
    9: "b: Armor Material Dependence",
    10: "g: Ghost",
}

ENUM_BUTTON_TYPE = {
    0: "YES/NO",
    1: "OK/CANCEL"
}

ENUM_CLASS_TYPE = {
    0: "Warrior",
    1: "Knight",
    2: "Wanderer",
    3: "Thief",
    4: "Bandit",
    5: "Hunter",
    6: "Sorcerer",
    7: "Pyromancer",
    8: "Cleric",
    9: "Deprived",
    # UNUSED:
    20: "Temp: Warrior", 21: "Temp: Knight", 22: "Temp: Sorcerer", 23: "Temp: Pyromancer", 24: "Chi: Warrior",
    25: "Chi: Knight", 26: "Chi: Sorcerer", 27: "Chi: Pyromancer",
}

ENUM_CHARACTER_TYPE = {
    0: "Human",
    1: "White Phantom",
    2: "Black Phantom",
    8: "Hollow",
    12: "Intruder",
}

ENUM_NAVIMESH_TYPE = {
    # Used as display bit masks.
    1: "Solid", 2: "Exit", 4: "Obstacle", 8: "Wall",
    32: "Wall-touching Floor", 64: "Landing Point",
    128: "Event", 256: "Cliff", 512: "Wide", 1024: "Ladder",
    2048: "Hole", 4096: "Door", 8192: "Closed Door",
}

ENUM_TEAM_TYPE = {
    255: "Default",
    0: "Invalid",
    1: "Human",
    2: "White Phantom",
    3: "Black Phantom",
    4: "Hollow",
    5: "Wandering Ghost",  # Vagrant, I believe.
    6: "Enemy",
    7: "Boss",  # Can damage any other team (including Boss).
    8: "Ally",
    9: "Hostile Ally",
    10: "Decoy Enemy",  # Unused.
    11: "Red Child",  # Unused.
    12: "Fighting Ally",
    13: "Intruder",
}

ENUM_AI_STATUS_TYPE = {
    0: "Normal",
    1: "Recognition",
    2: "Alert",
    3: "Battle"
}

ENUM_BOOL = {
    0: "FALSE",
    1: "TRUE",
}

ENUM_ON_OFF = {
    0: "OFF",
    1: "ON",
}

ENUM_ON_OFF_CHANGE = {
    0: "OFF",
    1: "ON",
    2: "CHANGE",
}

ENUM_SIGN_TYPE = {
    0: "Blue Eye Sign",
    1: "Black Eye Sign",
    2: "Red Eye Sign",
    3: "Detection Sign",
    4: "White Help Sign",
    5: "Black Help Sign",
}

ENUM_TENDENCY_TYPE = {
    0: "White Tendency",  # Unused.
    1: "Black Tendency",
}

ENUM_CONTAINED = {
    0: "OUTSIDE",
    1: "INSIDE",
}

ENUM_CATEGORY = {
    0: "Object",
    1: "Region",
    2: "Character",
}

ENUM_CUTSCENE_TYPE = {
    0: "Skippable",
    2: "Unskippable",
    8: "Skippable with Fade-out",
    10: "Unskippable with Fade-out",
}

ENUM_REACTION_ATTRIBUTE = {
    48: "Human & Hollow",
    255: "All",
}

ENUM_FLAG_TYPE = {
    0: "Flag",
    1: "This Event",
    2: "This Event + Slot",
}

ENUM_DAMAGE_TARGET_TYPE = {
    1: "Character",
    2: "Map",
    3: "Character & Map",
}

ENUM_OWN_STATE = {
    0: "Does not own",
    1: "Owns",
}

ENUM_BITOP = {
    0: "Add",
    1: "Delete",
    2: "Invert"
}

ENUM_BUTTON_NUMBER = {
    1: "1 Button",
    2: "2 Button",
    6: "No Button",
}

ENUM_CHARACTER_UPDATE_RATE = {
    -1: "Never",
    0: "Always",
    2: "Every 2 frames",
    5: "Every 5 frames",
}

ENUM_UPDATE_AUTH = {
    0: "Normal",
    4095: "Forced",
}

ENUM_CONDITION = {
    -7: " OR[ 7 ]", -6: " OR[ 6 ]", -5: " OR[ 5 ]", -4: " OR[ 4 ]", -3: " OR[ 3 ]", -2: " OR[ 2 ]", -1: " OR[ 1 ]",
    0: "--> AWAIT",
    1: "AND[ 1 ]", 2: "AND[ 2 ]", 3: "AND[ 3 ]", 4: "AND[ 4 ]", 5: "AND[ 5 ]", 6: "AND[ 6 ]", 7: "AND[ 7 ]",
}

ENUM_CONDITION_STATE = {
    0: "FALSE",
    1: "TRUE",
}

ENUM_DEATH_STATUS = {
    0: "Alive",
    1: "Dead",
}

ENUM_COMPARISON_TYPE = {
    0: "==",
    1: "!=",
    2: ">",
    3: "<",
    4: ">=",
    5: "<=",
}

ENUM_TEXT_BANNER_TYPE = {
    1: "BOSS DEFEATED",
    2: "YOU DIED",
    3: "YOU REVIVED",
    4: "SOULS ACQUIRED",
    5: "TARGET DESTROYED",
    6: "Ghost Death",
    7: "Black Ghost Death",
    8: "<MAP NAME>",
    12: "CONGRATULATIONS",
    15: "YOU WIN",
    16: "YOU LOSE",
    17: "YOU DRAW",
}

ENUM_ENABLE_STATE = {
    0: "DISABLE",
    1: "ENABLE",
}

ENUM_MULTIPLAYER_STATE = {
    0: "Host",
    1: "Client",
    2: "Multiplayer",
    3: "Singleplayer",
}

ENUM_STATUE_TYPE = {
    0: "Petrified",
    1: "Crystallized",
}

ENUM_DAMAGE_STATE = {
    0: "Not Destroyed",
    1: "Destroyed",
}

ENUM_EVENT_END_TYPE = {
    0: "END",
    1: "RESTART",
}

ENUM_ITEM_TYPE = {
    0: "Weapon",
    1: "Armor",
    2: "Ring",
    3: "Good",
}

ENUM_INTERPOLATION_STATE = {
    0: "Interpolated",
    1: "Not Interpolated",
}

ENUM_LOGICAL_OPERATION_TYPE = {
    0: "all ON",
    1: "all OFF",
    2: "any ON",
    3: "any OFF",
}

ENUM_SITE_TYPE = {
    1: "Part 1", 2: "Part 2", 3: "Part 3", 4: "Part 4", 5: "Part 5",
    6: "Part 6", 7: "Weak Point", 8: "Part 7", 9: "Part 8",
}

# ADDED ENUMS:

ENUM_COVENANT_TYPE = {
    0: "None",
    1: "Way of White",
    2: "Princess's Guard",
    3: "Warrior of Sunlight",
    4: "Darkwraith",
    5: "Path of the Dragon",
    6: "Gravelord Servant",
    7: "Forest Hunter",
    8: "Darkmoon Blade",
    9: "Chaos Servant",
}

ENUMS = {
    "ENUM_SOUND_TYPE": ("Sound Type", ENUM_SOUND_TYPE),
    "ENUM_BUTTON_TYPE": ("Button Type", ENUM_BUTTON_TYPE),
    "ENUM_CLASS_TYPE": ("Class Type", ENUM_CLASS_TYPE),
    "ENUM_CHARACTER_TYPE": ("Character Type", ENUM_CHARACTER_TYPE),
    "ENUM_NAVIMESH_TYPE": ("Navimesh Type", ENUM_NAVIMESH_TYPE),
    "ENUM_TEAM_TYPE": ("Team Type", ENUM_TEAM_TYPE),
    "ENUM_AI_STATUS_TYPE": ("AI Status Type", ENUM_AI_STATUS_TYPE),
    "ENUM_BOOL": ("BOOL", ENUM_BOOL),
    "ENUM_ON_OFF": ("ON/OFF", ENUM_ON_OFF),
    "ENUM_ON_OFF_CHANGE": ("ON/OFF/CHANGE", ENUM_ON_OFF_CHANGE),
    "ENUM_SIGN_TYPE": ("Sign Type", ENUM_SIGN_TYPE),
    "ENUM_TENDENCY_TYPE": ("Tendency Type", ENUM_TENDENCY_TYPE),
    "ENUM_CONTAINED": ("Contained", ENUM_CONTAINED),
    "ENUM_CATEGORY": ("Category", ENUM_CATEGORY),
    "ENUM_CUTSCENE_TYPE": ("Cutscene Type", ENUM_CUTSCENE_TYPE),
    "ENUM_REACTION_ATTRIBUTE": ("Reaction Attribute", ENUM_REACTION_ATTRIBUTE),
    "ENUM_FLAG_TYPE": ("Flag Type", ENUM_FLAG_TYPE),
    "ENUM_DAMAGE_TARGET_TYPE": ("Damage Target Type", ENUM_DAMAGE_TARGET_TYPE),
    "ENUM_OWN_STATE": ("Own State", ENUM_OWN_STATE),
    "ENUM_BITOP": ("BitOp", ENUM_BITOP),
    "ENUM_BUTTON_NUMBER": ("Num of Buttons", ENUM_BUTTON_NUMBER),
    "ENUM_CHARACTER_UPDATE_RATE": ("Character Update Rate", ENUM_CHARACTER_UPDATE_RATE),
    "ENUM_UPDATE_AUTH": ("Update Auth", ENUM_UPDATE_AUTH),
    "ENUM_CONDITION": ("Condition", ENUM_CONDITION),
    "ENUM_CONDITION_STATE": ("Condition State", ENUM_CONDITION_STATE),
    "ENUM_DEATH_STATUS": ("Death Status", ENUM_DEATH_STATUS),
    "ENUM_COMPARISON_TYPE": ("Comparison Type", ENUM_COMPARISON_TYPE),
    "ENUM_TEXT_BANNER_TYPE": ("Text Banner Type", ENUM_TEXT_BANNER_TYPE),
    "ENUM_ENABLE_STATE": ("Enable State", ENUM_ENABLE_STATE),
    "ENUM_MULTIPLAYER_STATE": ("Multiplayer State", ENUM_MULTIPLAYER_STATE),
    "ENUM_STATUE_TYPE": ("Statue Type", ENUM_STATUE_TYPE),
    "ENUM_DAMAGE_STATE": ("Damage State", ENUM_DAMAGE_STATE),
    "ENUM_EVENT_END_TYPE": ("Event End Type", ENUM_EVENT_END_TYPE),
    "ENUM_ITEM_TYPE": ("Item Type", ENUM_ITEM_TYPE),
    "ENUM_INTERPOLATION_STATE": ("Interpolation State", ENUM_INTERPOLATION_STATE),
    "ENUM_LOGICAL_OPERATION_TYPE": ("Logical Op Type", ENUM_LOGICAL_OPERATION_TYPE),
    "ENUM_SITE_TYPE": ("Part Type", ENUM_SITE_TYPE),
    "ENUM_COVENANT_TYPE": ("Covenant Type", ENUM_COVENANT_TYPE)
}


def stringify_args(format_string_or_enum_list, arg_list):
    """Applies stringify_arg to each element of arg_list, using the
    respective format or enum string in format_string_or_enum_list.
    """

    return [stringify_arg(format_string_or_enum, arg) for (format_string_or_enum, arg) in
            zip(format_string_or_enum_list, arg_list)]


def stringify_arg(format_string_or_enum, arg):
    """Formats arg in accordance with format_string_or_enum. If it is 
    a format string, arg must be of the correct type. Otherwise, if it
    is an enum, then arg is treated as an index into this enum.
    """

    if format_string_or_enum in ENUMS:
        return parse_enum(arg, format_string_or_enum)
    else:
        if isinstance(arg, str):
            return arg
        else:
            return format_string_or_enum % arg


def parse_enum(value, enum_name):
    """Indexes the enum enum_name using value. If value is not found in
    enum, then a dummy string representation of enum_name[value] is 
    used instead.
    """

    if enum_name not in ENUMS:
        raise ValueError(f"IntEnum name '{enum_name}' is not a known enum...")
    enum_string, enum = ENUMS[enum_name]
    if value not in enum:
        return enum_string + f"[{value}]"
    else:
        return enum[value]


def default_readable(instr_class, instr_index, req_args, opt_args):
    """Creates a default readable representation of the command with
    command instr_class and instr_index with arguments fixed_args and var_args.
    Provides no information about the command's purpose.
    """
    if opt_args:
        arg_array_string = f"({repr(req_args)} | {repr(opt_args)}"
    else:
        arg_array_string = f"({repr(req_args)})"

    return f"{instr_class:04d}[{instr_index:02d}] {arg_array_string}"


def verbose_instruction(instruction_class, instruction_index, req_args, opt_args, game_module):
    """Creates a human-readable representation of the command with
    command instr_class and instr_index with arguments fixed_args and var_args.
    If the command is known, the human-readable representation is
    a string that describes its function. If not, a default representation
    using default_readable is used as a fallback.
    """

    # Commands that make use of varargs come first:

    if opt_args or (instruction_class == 2000 and instruction_index == 0):
        slot, event_id, args = req_args
        return (f"Run Event (ID: {event_id}, Slot: {slot}, "
                f"Arguments: {{{', '.join([f'{args}'] + [f'{s}' for s in opt_args])}}})")

    # Commands that (we assume) do not make use of varargs come second:

    # if opt_args:
    #     raise ValueError(f"Command {instruction_class}[{instruction_index}] has optional arguments when it is "
    #                      f"assumed that it does not. Handle this!")

    if instruction_class == 2000:  # システム
        if instruction_index == 1:  # イベント強制終了
            # 5	0	%d	イベントスロット番号	[-1:1:99](Default: 0)
            # 2	256	%d	起動イベントID	[0:0:0](Default: 0)
            pass
        if instruction_index == 2:
            return "{0} network sync".format(*stringify_args(["ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 3:  # 終了済み条件グループ条件状態クリア
            # 0	0	%d	ダミー	[0:0:0](Default: 0)
            pass
        if instruction_index == 4:
            return "Issue Prefetch Request (Request ID: {0})".format(*stringify_args(["%d"], req_args))
        if instruction_index == 5:
            return "Save Request"
    if instruction_class == 2002:  # ポリ劇
        if instruction_index == 1:  # ポリ劇再生
            # 5	1	%d	ポリ劇ID	[0:1:1000000000](Default: 0)
            # 2	1	%d	再生方法	[ENUM: ENUM_CUTSCENE_TYPE](Default: 0)
            pass
        if instruction_index == 2:
            return ("Play Cutscene (Cutscene ID: {0}, Playback Method: {1}) and Warp Player to (Warp Point ID: {2}, "
                    "Map<{3}><{4}>)"
                    .format(*stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%d", "%d", "%d"], req_args)))
        if instruction_index == 3:
            return "Play Cutscene (Cutscene ID: {0}, Playback Method: {1}) to Player Entity ID: {2}".format(
                *stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%d"], req_args))
        if instruction_index == 4:
            return ("Play Cutscene (Cutscene ID: {0}, Playback Method: {1}) and Warp Player Entity ID: {5} to "
                    "(Warp Point ID: {2}, Map<{3}><{4}>)"
                    .format(*stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%d", "%d", "%d", "%d"], req_args)))
        if instruction_index == 5:
            return ("Play Cutscene (Cutscene ID: {0}, Playback Method: {1}, Player Entity ID: {6}) and Rotate Player "
                    "Around Vertical Axis (Axis X: {2}, Axis Z: {3}, Rotation: {4} degrees, Apply Vertical Translation "
                    "to Player: {5})"
                    .format(*stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%.2f", "%.2f", "%.2f", "%.2f", "%d"],
                                            req_args)))
    if instruction_class == 2003:  # イベント
        if instruction_index == 1:
            return ("Request Animation Playback (Animation ID: {1}, Should loop: {2}, Wait for completion: {3}) for "
                    "Entity ID: {0}"
                    .format(*stringify_args(["%d", "%d", "ENUM_BOOL", "ENUM_BOOL"], req_args)))
        if instruction_index == 2:
            flag_id, state = stringify_args(["%d", "ENUM_ON_OFF"], req_args)
            if state == 'ON':
                return f"ENABLE Event Flag ID {flag_id}"
            elif state == 'OFF':
                return f"DISABLE Event Flag ID {flag_id}"
            else:
                return f"SET Event Flag ID {flag_id} to state {state}"
        if instruction_index == 3:
            return "{1} spawner with Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 4:
            return "Award Items (Item Lot ID: {0})".format(*stringify_args(["%d"], req_args))
        if instruction_index == 5:
            return ("Shoot Projectile (Owner Entity ID: {0}, Projectile Entity ID: {1}, Damipoly ID: {2}, "
                    "Behavior ID: {3}, Launch Angle XYZ: ({4}, {5}, {6}))"
                    .format(*stringify_args(["%d", "%d", "%d", "%d", "%d", "%d", "%d"], req_args)))
        if instruction_index == 6:  # Map当たり有効化
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            # 0	1	%d	無効・有効	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
        if instruction_index == 7:  # Map表示有効化
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            # 0	1	%d	無効・有効	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
        if instruction_index == 8:
            return "{2} Slot Number {1} of Event ID {0}".format(
                *stringify_args(["%d", "%d", "ENUM_EVENT_END_TYPE"], req_args))
        if instruction_index == 9:  # イベントフラグ反転
            # 5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 10:  # イベントナビメッシュ設定
            # 4	1	%d	無効・有効	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
        if instruction_index == 11:
            return "{0} Boss Health Bar of Entity ID: {1} (Slot Number: {2}, Name ID: {3})".format(
                *stringify_args(["ENUM_ENABLE_STATE", "%d", "%d", "%d"], req_args))
        if instruction_index == 12:
            return "Kill Boss (Entity ID: {0})".format(*stringify_args(["%d"], req_args))
        if instruction_index == 13:
            # Modify the fixed args so that the bit# and its meaning can both be printed.
            mod_fix_args = [req_args[0], req_args[1], req_args[1], req_args[2]]
            return "{3} Bit# {1} ({2}) for Navimesh Entity ID: {0}".format(
                *stringify_args(["%d", "%d", "ENUM_NAVIMESH_TYPE", "ENUM_BITOP"], mod_fix_args))
        if instruction_index == 14:
            return "Warp Player to Region Entity ID: {2} in Map<{0}><{1}>".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 15:  # 中ボス撃破処理
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 16:
            return "Trigger Multiplayer Event ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 17:
            return "Randomly SET one of Event Flag ID from {0} to {1} to {2}".format(
                *stringify_args(["%d", "%d", "ENUM_ON_OFF"], req_args))
        if instruction_index == 18:
            return ("Force Entity ID: {0} to play Animation ID: {1} (Loop: {2}, Wait for completion: {3}, Do not wait "
                    "for transition: {4})"
                    .format(*stringify_args(["%d", "%d", "ENUM_BOOL", "ENUM_BOOL", "ENUM_BOOL"], req_args)))
        if instruction_index == 19:
            return "Set Map Texture ParamBank Slot Index (Map ID: {0}, Texture ParamBank Slot Index: {1})".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 20:  # 一時復活ポイント設定
            # 5	1	%d	復活ポイントエンティティID	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 21:
            return "Increment NG+ Counter"
        if instruction_index == 22:
            return "Batch SET Event Flag IDs from {0} to {1} to {2}".format(
                *stringify_args(["%d", "%d", "ENUM_ON_OFF"], req_args))
        if instruction_index == 23:
            return "Set Player respawn point to Point ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 24:
            return "Remove {2} (0=All) of Item (Item Type: {0}, Item ID: {1}) from player".format(
                *stringify_args(["ENUM_ITEM_TYPE", "%d", "%d"], req_args))
        if instruction_index == 25:
            return ("Place Summon Sign for Entity ID: {1} at Point ID: {2} (Sign Type: {0}, When summoned SET Event "
                    "Flag ID: {3}, When dismissed SET Event Flag ID: {4})"
                    .format(*stringify_args(["ENUM_SIGN_TYPE", "%d", "%d", "%d", "%d"], req_args)))
        if instruction_index == 26:
            return "{1} Tip Message (Entity ID: {0})".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 27:  # タイトル抜け
            # 0	1	%d	ダミー	[0:1:1](Default: 0)
            pass
        if instruction_index == 28:
            return "Award Achievement ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 29:  # 傾向値の加算
            # 0	1	%d	傾向タイプ	[ENUM: ENUM_TENDENCY_TYPE](Default: 0)
            # 3	1	%d	加算値	[-100:1:100](Default: 0)
            pass
        if instruction_index == 30:
            return "Disable Vagrant Spawning: {0}".format(*stringify_args(["ENUM_BOOL"], req_args))
        if instruction_index == 31:
            return "Increment Event Flag {0} (Number of Bits: {1}, Maximum: {2})".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 32:
            return "Clear Event Flag {0} (Number of Bits: {1})".format(*stringify_args(["%d", "%d"], req_args))
        if instruction_index == 33:
            return "Set Snuggly Next Trade Event Flag ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 34:
            return ("Snuggly Item Drop: Drop Item Lot ID: {0} (corresponding to Trade Event Flag ID: {2}) at Region "
                    "Entity ID: {1} on Hitbox Entity ID: {3}"
                    .format(*stringify_args(["%d", "%d", "%d", "%d"], req_args)))
        if instruction_index == 35:
            return "Move dropped items & bloodstain from Region Entity ID: {0} to Region Entity ID: {1}".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 36:
            return "Award Items (Item Lot ID: {0}) (HOST ONLY)".format(*stringify_args(["%d"], req_args))
        if instruction_index == 37:
            return "Battle of Stoicism 1v1 Ranking Request"
        if instruction_index == 38:
            return "Battle of Stoicism 2v2 Ranking Request"
        if instruction_index == 39:
            return "Battle of Stoicism FFA Ranking Request"
        if instruction_index == 40:
            return "Request Battle of Stoicism Exit"
        if instruction_index == 41:
            return "Activate player killplane (Target Model ID: {3}) below Y threshold {2} on Map<{0}><{1}>".format(
                *stringify_args(["%d", "%d", "%0.3f", "%d"], req_args))
    if instruction_class == 2004:  # キャラ
        if instruction_index == 1:
            return "{1} AI of Character ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 2:
            return "Switch Character ID: {0} to team {1}".format(
                *stringify_args(["%d", "ENUM_TEAM_TYPE"], req_args))
        if instruction_index == 3:
            return ("Issue Warp request for Character ID: {0} (Warp Destination Type: {1}, Destination Target "
                    "ID: {2}, Damipoly ID: {3})"
                    .format(*stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d"], req_args)))
        if instruction_index == 4:
            return "Kill Character ID: {0} (Yields souls: {1})".format(
                *stringify_args(["%d", "ENUM_BOOL"], req_args))
        if instruction_index == 5:
            return "{1} Character ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 6:
            return "EzState instruction request (Entity ID: {0}, Command: {1}, Slot: {2})".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 7:
            return "Create Spawner (Entity ID: {0})".format(*stringify_args(["%d"], req_args))
        if instruction_index == 8:
            return "Add Special Effect (Character ID: {0}, Special Effect ID: {1})".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 9:
            return ("Set Animation Defaults for Character ID: {0} [Standby: {1}, Damage: {2}, "
                    "Cancel: {3}, Death: {4}, Standby Return: {5}])"
                    .format(*stringify_args(["%d", "%d", "%d", "%d", "%d", "%d"], req_args)))
        if instruction_index == 10:
            return "{1} Gravity for Character ID: {0}".format(
                *stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 11:  # イベントターゲット指定
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            # 5	1	%d	エンティティID2	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 12:
            return "{1} Immortality for Character ID: {0}".format(
                *stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 13:
            return "Set \"Nest\" of Character ID: {0} to Region ID: {1}".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 14:
            return "Rotate Entity ID: {0} to face Entity ID: {1}".format(*stringify_args(["%d", "%d"], req_args))
        if instruction_index == 15:
            return "{1} Invincibility for Character ID: {0}".format(
                *stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 16:
            return "Clear AI Target List of Character ID: {0}".format(
                *stringify_args(["%d"], req_args))
        if instruction_index == 17:
            return ("Issue AI instruction request to Character ID: {0} (Command ID: {1}, Slot Number: {2})"
                    .format(*stringify_args(["%d", "%d", "%d"], req_args)))
        if instruction_index == 18:
            return "Set Event Point (Event Region ID: {1}, Reaction Range: {2}) for Entity ID: {0}".format(
                *stringify_args(["%d", "%d", "%0.3f"], req_args))
        if instruction_index == 19:
            return "Set AI ID: {1} for Character ID: {0}".format(*stringify_args(["%d", "%d"], req_args))
        if instruction_index == 20:
            return "Issue AI Re-plan request to Character ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 21:
            return "Cancel Special Effect (Character ID: {0}, Special Effect ID: {1})".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 22:
            return ("Create multipart-NPC part (Entity ID: {0}, Part NPC Type: {1}, Part Index: {2}, Part HP: {3}, "
                    "Damage Correction: {4}, Body Damage Correction: {5}, Invincible: {6}, "
                    "Starts in stopped state: {7})"
                    .format(*stringify_args(["%d", "%d", "ENUM_SITE_TYPE", "%d", "%d", "%d", "ENUM_BOOL", "ENUM_BOOL"],
                                            req_args)))
        if instruction_index == 23:
            return ("Set HP of multipart-NPC part (Entity ID: {0}, Part NPC Type: {1}) to {2} (Overwrite max HP if "
                    "required: {3})"
                    .format(*stringify_args(["%d", "%d", "%d", "ENUM_BOOL"], req_args)))
        if instruction_index == 24:
            return ("Set multipart-NPC (Entity ID: {0}, Part NPC Type: {1}) defense material SE and SFX (SE ID: {2}, "
                    "SFX ID: {3})"
                    .format(*stringify_args(["%d", "%d", "%d", "%d"], req_args)))
        if instruction_index == 25:
            return "Set multipart-NPC (Entity ID: {0}, Part NPC Type: {1}) bullet damage magnification to {2}".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 26:
            return "Set display mask of character (Entity ID: {0}, Number of Bits: {1}) to {2}".format(
                *stringify_args(["%d", "%d", "ENUM_ON_OFF_CHANGE"], req_args))
        if instruction_index == 27:
            return "Set hitbox mask of character (Entity ID: {0}, Number of Bits: {1}) to {2}".format(
                *stringify_args(["%d", "%d", "ENUM_ON_OFF_CHANGE"], req_args))
        if instruction_index == 28:
            return "Set Network Update Authority of Entity ID: {0} to {1}".format(
                *stringify_args(["%d", "ENUM_UPDATE_AUTH"], req_args))
        if instruction_index == 29:
            return "Disable BackRead (Entity ID: {0}, Should be removed: {1})".format(
                *stringify_args(["%d", "ENUM_BOOL"], req_args))
        if instruction_index == 30:
            return "{1} Health Bar for Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 31:
            entity, state = stringify_args(["%d", "ENUM_BOOL"], req_args)
            if state == 'FALSE':
                return "ENABLE Map Collision for Entity ID: {0}".format(entity)
            elif state == 'TRUE':
                return "DISABLE Map Collision for Entity ID: {0}".format(entity)
        if instruction_index == 32:
            return ("Issue AI Event Request (Entity ID: {0}, Command ID: {1}, Slot Number: {2}, "
                    "Start Event Flag ID: {3}, End Event Flag ID: {4})"
                    .format(*stringify_args(["%d", "%d", "%d", "%d", "%d"], req_args)))
        if instruction_index == 33:
            return "Refer damage from Entity ID: {0} to Entity ID: {1}".format(*stringify_args(["%d", "%d"], req_args))
        if instruction_index == 34:
            return "Set Network Update Frequency of Entity ID: {0} to (Frequency: {2}, Fixed Rate: {1})".format(
                *stringify_args(["%d", "ENUM_BOOL", "ENUM_CHARACTER_UPDATE_RATE"], req_args))
        if instruction_index == 35:
            return "{1} Entity ID: {0} BackRead Status".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 36:
            return "Hellkite Breath Control (Entity ID: {0}, Object Entity ID: {1}, Animation ID: {2})".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 37:
            return "Mandatory treasure at Entity ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 38:
            return "Betray player's current covenant"
        if instruction_index == 39:
            return "{1} Animation of Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 40:
            return ("Issue Warp request for Entity ID: {0} (Warp Destination Type: {1}, Destination Target ID: {2}, "
                    "Damipoly ID: {3}) and SET draw hitbox to Hitbox Entity ID: {4}"
                    .format(*stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d", "%d"], req_args)))
        if instruction_index == 41:
            return ("Issue short-range Warp request for Entity ID: {0} (Warp Destination Type: {1}, "
                    "Destination Target ID: {2}, Damipoly ID: {3})"
                    .format(*stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d"], req_args)))
        if instruction_index == 42:
            return ("Issue Warp request for Entity ID: {0} (Warp Destination Type: {1}, Destination Target ID: {2}, "
                    "Damipoly ID: {3}) and COPY draw hitbox from Entity ID: {4}"
                    .format(*stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d", "%d"], req_args)))
        if instruction_index == 43:
            return ("Issue Animation Reset Request for Entity ID: {0} (Interpolation: {1})"
                    .format(*stringify_args(["%d", "ENUM_INTERPOLATION_STATE"], req_args)))
        if instruction_index == 44:  # チームタイプ切り替え＆強制特殊待機解除
            return "Switch character (Entity ID: {0}) to team {1} and exit forced standby animation".format(
                *stringify_args(["%d", "ENUM_TEAM_TYPE"], req_args))
        if instruction_index == 45:
            return ("Humanity Registration for Entity ID: {0} (Initial Humanity Flag ID: {1})"
                    .format(*stringify_args(["%d", "%d"], req_args)))
        if instruction_index == 46:
            return "Increment player PvP sin"
        if instruction_index == 47:
            return '??? "Equal Recovery"'
    if instruction_class == 2005:  # オブジェクト
        if instruction_index == 1:
            return "Destroy object (Entity ID: {0}, Slot Number: {1})".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 2:
            return "Restore Object (Entity ID: {0})".format(*stringify_args(["%d"], req_args))
        if instruction_index == 3:
            return "{1} Object with Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 4:
            return "{1} Treasure of Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 5:
            return "ObjAct Start (Entity ID: {0}, Object Parameter ID: {1}, Relative IDX: {2})".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 6:
            obj, objact_id, state = stringify_args(["%d", "%d", "ENUM_ENABLE_STATE"], req_args)
            if state == 'ENABLE':
                return "ENABLE Activation of Object ID: {0} (ObjAct Parameter ID: {1})".format(obj, objact_id)
            elif state == 'DISABLE':
                return "DISABLE Activation of Object ID: {0} (ObjAct Parameter ID: {1})".format(obj, objact_id)
        if instruction_index == 7:
            return "Set Object to Post-Animation State (Object Entity ID: {0}, Animation ID: {1})".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 8:
            return "Set Object to Post-Destruction State (Object Entity ID: {0}, Slot Number: {1})".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 9:
            return ("Create Hazard (Event Flag ID: {0}, Entity ID: {1}, Damipoly ID: {2}, "
                    "Behavior ID: {3}, Target Type: {4}, Radius: {5}, Life: {6}, Repetition Time: {7})"
                    .format(*stringify_args(["%d", "%d", "%d", "%d", "ENUM_DAMAGE_TARGET_TYPE", "%0.3f", "%0.3f",
                                             "%0.3f"], req_args)))
        if instruction_index == 10:
            return "Register Statue Object (Entity ID: {0}, Map<{1}><{2}>, Statue Type: {3})".format(
                *stringify_args(["%d", "%d", "%d", "ENUM_STATUE_TYPE"], req_args))
        if instruction_index == 11:
            return "Warp Object ID: {0} to Character (Entity ID: {1}) (Damipoly ID: {2})".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 12:
            return "Remove Object Event Flag ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 13:
            return "{1} invulnerability of object (Entity ID: {0})".format(
                *stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 14:
            return ("ObjAct Activation (IDX Designation) (Entity ID: {0}, Object Parameter ID: {1}, Relative IDX: {2}, "
                    "State: {3})"
                    .format(*stringify_args(["%d", "%d", "%d", "ENUM_ENABLE_STATE"], req_args)))
        if instruction_index == 15:
            return "Treasure Redemption of Entity ID: {0}".format(*stringify_args(["%d"], req_args))
    if instruction_class == 2006:  # SFX
        if instruction_index == 1:
            return "Delete Map SFX (Entity ID: {0}, Deletes only root: {1})".format(
                *stringify_args(["%d", "ENUM_BOOL"], req_args))
        if instruction_index == 2:
            return "Create Map SFX (Entity ID: {0})".format(*stringify_args(["%d"], req_args))
        if instruction_index == 3:
            return "Create One-Off SFX (SFX Type: {0}, Entity ID: {1}, Damipoly ID: {2}, SFX ID: {3})".format(
                *stringify_args(["ENUM_CATEGORY", "%d", "%d", "%d"], req_args))
        if instruction_index == 4:
            return "Create SFX ID: {2} attached to Object (Entity ID: {0}, Damipoly ID: {1})".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 5:
            return "Delete SFX attached to Object (Entity ID: {0}) (Should delete root: {1})".format(
                *stringify_args(["%d", "ENUM_BOOL"], req_args))
    if instruction_class == 2007:  # メッセージ
        if instruction_index == 1:
            return ("Display Dialog (Message ID: {0}, Button Type: {1}, Number of Buttons: {2}, "
                    "Entity ID: {3}, Display Distance: {4})"
                    .format(*stringify_args(["%d", "ENUM_BUTTON_TYPE", "ENUM_BUTTON_NUMBER", "%d", "%.3f"], req_args)))
        if instruction_index == 2:
            return "Display Text Banner (Banner Type: {0})".format(*stringify_args(["ENUM_TEXT_BANNER_TYPE"], req_args))
        if instruction_index == 3:
            return "Display Status Explanation Message (Message ID: {0}, {1} Pad)".format(
                *stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 4:
            return "Display Battlefield Message (Message ID: {0}, Display Location Index: {1})".format(
                *stringify_args(["%d", "%d"], req_args))
        if instruction_index == 5:
            return "Set Battle of Stoicism Participant 1 Name-tag"
        if instruction_index == 6:
            return "Set Battle of Stoicism Participant 2 Name-tag"
        if instruction_index == 7:
            return "Set Battle of Stoicism Participant 3 Name-tag"
        if instruction_index == 8:
            return "Set Battle of Stoicism Participant 4 Name-tag"
        if instruction_index == 9:
            return "Display Battle of Stoicism Dissolution Message (Message ID: {0})".format(
                *stringify_args(["%d"], req_args))
    if instruction_class == 2008:  # カメラ
        if instruction_index == 1:  # メラ変更
            # 5	1	%d	通常カメラID	[-1:1:1000000000](Default: -1)
            # 5	1	%d	ロックカメラID	[-1:1:1000000000](Default: -1)
            pass
        if instruction_index == 2:  # カメラ振動
            # 5	1	%d	振動ID	[0:1:1000000000](Default: 0)
            # 5	1	%d	タイプ	[ENUM: ENUM_CATEGORY](Default: 0)
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            # 5	1	%d	ダミポリID	[-1:1:1000000000](Default: -1)
            # 6	1	%.3f	減衰開始距離	[0.0:0.00999999977648:999.0](Default: 0.0)
            # 6	1	%.3f	減衰完了距離	[0.0:0.00999999977648:999.0](Default: 0.0)
            pass
        if instruction_index == 3:
            return "SET locked camera slot #{2} in Map<{0}><{1}>".format(*stringify_args(["%d", "%d", "%d"], req_args))
    if instruction_class == 2009:  # スクリプト
        if instruction_index == 0:
            return "Register Ladder (Entity ID: {2}, Unknown Event Flag ID: {0}, Unknown Event Flag ID: {1})".format(
                *stringify_args(["%d", "%d", "%d"], req_args))
        if instruction_index == 1:  # 徘徊デーモン初期化
            # 5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            # 5	1	%d	出現用イベントフラグID	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 2:  # 徘徊デーモン登録
            # 5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            # 5	1	%d	エンティティID2	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 3:
            return ("Register Bonfire (Event Flag ID: {0}, Entity ID: {1}, Reaction Distance: {2}, "
                    "Reaction Angle: {3}, Initial Kindle Level: {4})"
                    .format(*stringify_args(["%d", "%d", "%0.3f", "%0.3f", "%d"], req_args)))
        if instruction_index == 4:
            return "Activate buffs for NPC ID: {0}".format(*stringify_args(["%d"], req_args))
        if instruction_index == 5:  # 回復の泉登録
            # 5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 6:  # ボス部屋侵入通知
            return "Issue Boss Room entry notification"
    if instruction_class == 2010:  # サウンド
        if instruction_index == 1:  # BGM再生
            # 0	1	%d	再生設定	[ENUM: ENUM_ON_OFF](Default: 0)
            # 1	1	%.d	スロットNo	[0:1:20](Default: 0)
            # 5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            # 5	1	%d	サウンドタイプ	[ENUM: ENUM_SOUND_TYPE](Default: 0)
            # 5	1	%d	サウンドID	[0:1:1000000000](Default: 0)
            pass
        if instruction_index == 2:
            return "Play Sound Effect (Sound Type: {1}, Sound ID: {2}) at Entity ID: {0}".format(
                *stringify_args(["%d", "ENUM_SOUND_TYPE", "%d"], req_args))
        if instruction_index == 3:
            return "{1} Map Sound (Entity ID: {0})".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
    if instruction_class == 2011:  # ヒット
        if instruction_index == 1:
            return "{1} Hitbox of Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
        if instruction_index == 2:  # ヒットパーツバックリードマスク有効化
            # 5	1	%d	ヒットパーツのエンティティID	[0:1:1000000000](Default: 0)
            # 0	1	%d	有効化設定	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
    if instruction_class == 2012:  # マップ
        if instruction_index == 1:
            return "{1} Map Part ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], req_args))
    if instruction_class == 1000:  # 【実行制御】システム
        if instruction_index == 0:  # 条件グループ条件状態で待機
            # 0	0	%d	条件成立条件状態	[ENUM: ENUM_CONDITION_STATE](Default: 1)
            # 3	0	%d	対象条件グループ	[ENUM: ENUM_CONDITION](Default: 0)
            pass
        if instruction_index == 1:
            return "SKIP {0} lines IF condition {2} is {1}".format(
                *stringify_args(["%d", "ENUM_CONDITION_STATE", "ENUM_CONDITION"], req_args))
        if instruction_index == 2:
            return "{0} event IF condition {2} is {1}".format(
                *stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_CONDITION_STATE", "ENUM_CONDITION"], req_args))
        if instruction_index == 3:
            return "SKIP {0} lines".format(*stringify_args(["%d"], req_args))
        if instruction_index == 4:
            return "{0} event".format(*stringify_args(["ENUM_EVENT_END_TYPE"], req_args))
        if instruction_index == 5:
            return "SKIP {0} lines IF ({2} {1} {3})".format(
                *stringify_args(["%d", "ENUM_COMPARISON_TYPE", "%d", "%d"], req_args))
        if instruction_index == 6:
            return "{0} event IF ({2} {1} {3})".format(
                *stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_COMPARISON_TYPE", "%d", "%d"], req_args))
        if instruction_index == 7:
            return "SKIP {0} lines IF condition {2} is {1} (FINISHED)".format(
                *stringify_args(["%d", "ENUM_CONDITION_STATE", "ENUM_CONDITION"], req_args))
        if instruction_index == 8:
            return "{0} event IF condition {2} is {1} (FINISHED)".format(
                *stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_CONDITION_STATE", "ENUM_CONDITION"], req_args))
        if instruction_index == 9:
            return "WAIT {0}s for network approval".format(*stringify_args(["%0.3f"], req_args))
    if instruction_class == 1001:  # 実行制御】タイマー
        if instruction_index == 0:
            return "WAIT {0}s".format(*stringify_args(["%0.3f"], req_args))
        if instruction_index == 1:
            return "WAIT {0} frames".format(*stringify_args(["%d"], req_args))
        if instruction_index == 2:
            return "WAIT for a random number of seconds (Min: {0}s, Max: {1}s)".format(
                *stringify_args(["%0.3f", "%0.3f"], req_args))
        if instruction_index == 3:  # 経過ランダムフレーム数で待機
            # 5	0	%d	目標フレーム最小値	[0:1:99999](Default: 0)
            # 5	0	%d	目標フレーム最大値	[0:1:99999](Default: 0)
            pass
    if instruction_class == 1003:  # 【実行制御】イベント
        if instruction_index == 0:  # イベントフラグ状態で待機
            # 0	0	%d	条件成立フラグ状態	[ENUM: ENUM_ON_OFF_CHANGE](Default: 1)
            # 0	0	%d	基準イベントフラグIDタイプ	[ENUM: ENUM_FLAG_TYPE](Default: 0)
            # 5	0	%d	対象イベントフラグID	[0:1:100000000](Default: 0)
            pass
        if instruction_index == 1:
            return "SKIP {0} lines IF {2}: {3} is {1}".format(
                *stringify_args(["%d", "ENUM_ON_OFF", "ENUM_FLAG_TYPE", "%d"], req_args))
        if instruction_index == 2:
            return "{0} event IF {2}: {3} is {1}".format(
                *stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_ON_OFF", "ENUM_FLAG_TYPE", "%d"], req_args))
        if instruction_index == 3:
            return "SKIP {0} lines IF {2}: {3} to {4} are {1}".format(
                *stringify_args(["%d", "ENUM_LOGICAL_OPERATION_TYPE", "ENUM_FLAG_TYPE", "%d", "%d"], req_args))
        if instruction_index == 4:
            return "{0} event IF {2}: {3} to {4} are {1}".format(*stringify_args(
                ["ENUM_EVENT_END_TYPE", "ENUM_LOGICAL_OPERATION_TYPE", "ENUM_FLAG_TYPE", "%d", "%d"], req_args))
        if instruction_index == 5:
            return "SKIP {0} lines IF multiplayer status is {1}".format(
                *stringify_args(["%d", "ENUM_MULTIPLAYER_STATE"], req_args))
        if instruction_index == 6:
            return "{0} event IF multiplayer status is {1}".format(
                *stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_MULTIPLAYER_STATE"], req_args))
        if instruction_index == 7:
            skip_lines, value, area_id, block_id = stringify_args(["%d", "ENUM_BOOL", "%d", "%d"], req_args)
            name = get_game_map(area_id, block_id, game_module)
            return "SKIP {0} lines IF it is {1} that player is in Map<{2}><{3}> ({4})".format(
                skip_lines, value, area_id, block_id, name)
        if instruction_index == 8:  # マップIDでイベント終了
            end_type, value, area_id, block_id = stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_BOOL", "%d", "%d"], req_args)
            name = get_game_map(area_id, block_id, game_module)
            return "{0} event IF it is {1} that player is in Map<{2}><{3}> ({4})".format(
                end_type, value, area_id, block_id, name)
    if instruction_class == 1005:  # 【実行制御】オブジェクト
        if instruction_index == 0:  # オブジェクト破壊状態で待機
            # 0	0	%d	条件成立破壊状態	[ENUM: ENUM_DAMAGE_STATE](Default: 1)
            # 5	0	%d	対象オブジェクトのエンティティID	[0:1:100000000](Default: 0)
            pass
        if instruction_index == 1:
            return "SKIP {0} lines IF object (Entity ID: {2}) is {1}".format(
                *stringify_args(["%d", "ENUM_DAMAGE_STATE", "%d"], req_args))
        if instruction_index == 2:
            return "{0} event IF object (Entity ID: {2}) is {1}".format(
                *stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_DAMAGE_STATE", "%d"], req_args))
    if instruction_class == 0:  # 《条件登録》システム
        if instruction_index == 0:
            return " {0} <-- IF condition {2} is {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_CONDITION_STATE", "ENUM_CONDITION"], req_args))
        if instruction_index == 1:  # パラメータ比較状態で判定
            # 3	0	%d	登録条件グループ	[ENUM: ENUM_CONDITION](Default: 0)
            # 3	0	%d	比較タイプ	[ENUM: ENUM_COMPARISON_TYPE](Default: 0)
            # 5	1	%d	左辺値	[-1:1:1000000000](Default: 0)
            # 5	1	%d	右辺値	[-1:1:1000000000](Default: 0)
            pass
    if instruction_class == 1:  # 《条件登録》タイマー
        if instruction_index == 0:
            return " {0} <-- IF {1}s have elapsed".format(*stringify_args(["ENUM_CONDITION", "%0.3f"], req_args))
        if instruction_index == 1:
            return " {0} <-- IF {1} frames have elapsed".format(*stringify_args(["ENUM_CONDITION", "%d"], req_args))
        if instruction_index == 2:  # 経過ランダム秒数で判定
            # 3	0	%d	登録条件グループ	[ENUM: ENUM_CONDITION](Default: 0)
            # 6	0	%0.3f	目標秒数最小値	[0.0:0.00999999977648:9999.0](Default: 0.0)
            # 6	0	%0.3f	目標秒数最大値	[0.0:0.00999999977648:9999.0](Default: 0.0)
            pass
        if instruction_index == 3:  # 経過ランダムフレーム数で判定
            # 3	0	%d	登録条件グループ	[ENUM: ENUM_CONDITION](Default: 0)
            # 5	0	%d	目標フレーム数最小値	[0:1:99999](Default: 0)
            # 5	0	%d	目標フレーム数最大値	[0:1:99999](Default: 0)
            pass
    if instruction_class == 3:  # 《条件登録》イベント
        if instruction_index == 0:
            return " {0} <-- IF {2}: {3} is {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_ON_OFF_CHANGE", "ENUM_FLAG_TYPE", "%d"], req_args))
        if instruction_index == 1:
            return " {0} <-- IF {2}s: {3} to {4} are {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_LOGICAL_OPERATION_TYPE", "ENUM_FLAG_TYPE", "%d", "%d"],
                                req_args))
        if instruction_index == 2:
            return " {0} <-- IF Entity ID: {2} is {1} Region ID: {3}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_CONTAINED", "%d", "%d"], req_args))
        if instruction_index == 3:
            return " {0} <-- IF Entity ID: {2} is {1} radius {4} of Entity ID: {3}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_CONTAINED", "%d", "%d", "%0.3f"], req_args))
        if instruction_index == 4:
            return " {0} <-- IF player {3} Item (Item Type: {1}, Item ID: {2})".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_ITEM_TYPE", "%d", "ENUM_OWN_STATE"], req_args))
        if instruction_index == 5:
            return (" {0} <-- IF Dialog Activated (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, "
                    "Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, Reaction Attribute: {7}, Pad ID: {8})"
                    .format(*stringify_args(["ENUM_CONDITION", "ENUM_CATEGORY", "%d", "%0.3f", "%d", "%0.3f", "%d",
                                             "ENUM_REACTION_ATTRIBUTE", "%d"], req_args)))
        if instruction_index == 6:
            return " {0} <-- IF player Multiplayer State is {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_MULTIPLAYER_STATE"], req_args))
        if instruction_index == 7:
            return " {0} <-- IF all players are {1} Region ID: {2}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_CONTAINED", "%d"], req_args))
        if instruction_index == 8:
            condition, value, area_id, block_id = stringify_args(["ENUM_CONDITION", "ENUM_BOOL", "%d", "%d"], req_args)
            name = get_game_map(area_id, block_id, game_module)
            return " {0} <-- IF it is {1} that player is in Map<{2}><{3}> ({4})".format(
                condition, value, area_id, block_id, name)
        if instruction_index == 9:
            return " {0} <-- IF Multiplayer Event ID: {1} was triggered".format(
                *stringify_args(["ENUM_CONDITION", "%d"], req_args))
        if instruction_index == 10:
            return " {0} <-- IF Number of TRUE {1}s from {2} to {3} is {4} {5}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_FLAG_TYPE", "%d", "%d", "ENUM_COMPARISON_TYPE", "%d"],
                                req_args))
        if instruction_index == 11:
            return " {0} <-- IF Area {1} {2} {3}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_TENDENCY_TYPE", "ENUM_COMPARISON_TYPE", "%d"], req_args))
        if instruction_index == 12:
            return " {0} <-- IF (Event Flag ID: {1}, Number of Bits: {2}) has value {3} {4}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "%d", "ENUM_COMPARISON_TYPE", "%d"], req_args))
        if instruction_index == 13:
            return (" {0} <-- IF Dialog Activated (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, "
                    "Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, Reaction Attribute: {7}, Pad ID: {8}) "
                    "(BOSS ROOM)"
                    .format(*stringify_args(["ENUM_CONDITION", "ENUM_CATEGORY", "%d", "%0.3f", "%d", "%0.3f", "%d",
                                             "ENUM_REACTION_ATTRIBUTE", "%d"], req_args)))
        if instruction_index == 14:
            return " {0} <-- IF an item was dropped in Region ID: {1}".format(
                *stringify_args(["ENUM_CONDITION", "%d"], req_args))
        if instruction_index == 15:
            return " {0} <-- IF dropped item is (Item Type: {1}, Item ID: {2})".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_ITEM_TYPE", "%d"], req_args))
        if instruction_index == 16:
            return " {0} <-- IF player {3} Item (Item Type: {1}, Item ID: {2}) (Including in their BBox)".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_ITEM_TYPE", "%d", "ENUM_OWN_STATE"], req_args))
        if instruction_index == 17:
            return " {0} <-- IF current New Game Cycle is {1} {2}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_COMPARISON_TYPE", "%03d"], req_args))
        if instruction_index == 18:
            return (" {0} <-- IF Dialog Activated (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, "
                    "Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, Reaction Attribute: {7}, Pad ID: {8}) "
                    "and Line Segment Direction (Line Segment Endpoint Entity ID: {9})"
                    .format(*stringify_args(["ENUM_CONDITION", "ENUM_CATEGORY", "%d", "%0.3f", "%d", "%0.3f", "%d",
                                             "ENUM_REACTION_ATTRIBUTE", "%d", "%d"], req_args)))
        if instruction_index == 19:
            return (" {0} <-- IF Dialog Activated (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, "
                    "Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, Reaction Attribute: {7}, Pad ID: {8}) "
                    "and Line Segment Direction (Line Segment Endpoint Entity ID: {9}) (BOSS ROOM VERSION)"
                    .format(*stringify_args(["ENUM_CONDITION", "ENUM_CATEGORY", "%d", "%0.3f", "%d", "%0.3f", "%d",
                                             "ENUM_REACTION_ATTRIBUTE", "%d", "%d"], req_args)))
        if instruction_index == 20:
            return (" {0} <-- IF (Event Flag: {1}, Number of Bits: {2}) {3} (Event Flag: {4}, Number of Bits: {5})"
                    .format(*stringify_args(["ENUM_CONDITION", "%d", "%d", "ENUM_COMPARISON_TYPE", "%d", "%d"],
                                            req_args)))
        if instruction_index == 21:
            return " {0} <-- IF it is {1} that the player owns the DLC".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_BOOL"], req_args))
        if instruction_index == 22:
            return " {0} <-- IF it is {1} that the game is in online mode".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_BOOL"], req_args))
    if instruction_class == 4:  # 《条件登録》キャラ
        if instruction_index == 0:
            return " {0} <-- IF Entity ID: {1} is {2}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "ENUM_DEATH_STATUS"], req_args))
        if instruction_index == 1:
            return " {0} <-- IF Entity ID: {1} is attacked by Entity ID: {2}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "%d"], req_args))
        if instruction_index == 2:
            return " {0} <-- IF Entity ID: {1} has Health Ratio {2} {3}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "ENUM_COMPARISON_TYPE", "%0.3f"], req_args))
        if instruction_index == 3:
            return " {0} <-- IF Entity ID: {1} is of Character Type {2}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "ENUM_CHARACTER_TYPE"], req_args))
        if instruction_index == 4:
            return " {0} <-- IF Entity ID: {1} targeting Entity ID: {2} is {3}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "%d", "ENUM_BOOL"], req_args))
        if instruction_index == 5:
            return " {0} <-- IF Entity ID: {1} has Special Effect ID: {2} is {3}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "%d", "ENUM_BOOL"], req_args))
        if instruction_index == 6:
            return " {0} <-- IF Part NPC ID: {2} of multipart-NPC Entity: {1} has HP {4} {3}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "%d", "%d", "ENUM_COMPARISON_TYPE"], req_args))
        if instruction_index == 7:
            return " {0} <-- IF Entity ID: {1} BackRead status is {2}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "ENUM_BOOL"], req_args))
        if instruction_index == 8:
            return " {0} <-- IF it is {3} that Entity ID: {1} has Event Message ID: {2}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "%d", "ENUM_BOOL"], req_args))
        if instruction_index == 9:
            return " {0} <-- IF Entity ID: {1} has AI State: {2}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "ENUM_AI_STATUS_TYPE"], req_args))
        if instruction_index == 10:
            return " {0} <-- IF player currently using Skull Lantern is {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_BOOL"], req_args))
        if instruction_index == 11:
            return " {0} <-- IF player's class is {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_CLASS_TYPE"], req_args))
        if instruction_index == 12:
            return " {0} <-- IF player's covenant is {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_COVENANT_TYPE"], req_args))
        if instruction_index == 13:
            return " {0} <-- IF player's Soul Level is {1} {2}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_COMPARISON_TYPE", "%d"], req_args))
        if instruction_index == 14:
            return " {0} <-- IF Entity ID: {1} has Health Value {2} {3}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "ENUM_COMPARISON_TYPE", "%d"], req_args))
    if instruction_class == 5:  # 《条件登録》オブジェクト
        if instruction_index == 0:
            return " {0} <-- IF Object Entity ID: {2} is {1}".format(
                *stringify_args(["ENUM_CONDITION", "ENUM_DAMAGE_STATE", "%d"], req_args))
        if instruction_index == 1:
            return " {0} <-- IF Object Entity ID: {1} is damaged by Attacker Entity ID: {2}".format(
                *stringify_args(["ENUM_CONDITION", "%d", "%d"], req_args))
        if instruction_index == 2:
            return " {0} <-- IF ObjAct Execution Event ID: {1}".format(
                *stringify_args(["ENUM_CONDITION", "%d"], req_args))
        if instruction_index == 3:  # オブジェクトのHP状態で判定
            # 3	0	%d	登録条件グループ	[ENUM: ENUM_CONDITION](Default: 0)
            # 5	0	%d	対象エンティティID	[0:1:100000000](Default: 0)
            # 3	0	%d	比較タイプ	[ENUM: ENUM_COMPARISON_TYPE](Default: 4)
            # 5	0	%d	HP閾値	[0:1:1000000000](Default: 0)
            pass
    if instruction_class == 11:  # 《条件登録》ヒット
        if instruction_index == 0:
            return " {0} <-- IF local player is moving on Hitbox Entity ID: {1}".format(
                *stringify_args(["ENUM_CONDITION", "%d"], req_args))
        if instruction_index == 1:
            return " {0} <-- IF local player is running on Hitbox Entity ID: {1}".format(
                *stringify_args(["ENUM_CONDITION", "%d"], req_args))
        if instruction_index == 2:
            return " {0} <-- IF local player is standing on Hitbox Entity ID: {1}".format(
                *stringify_args(["ENUM_CONDITION", "%d"], req_args))

    # If no matching return statement exists, print the default (un-translated) representation.
    return default_readable(instruction_class, instruction_index, req_args, opt_args)

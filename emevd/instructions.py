from typing import Union
from .ds_types import *
from pydses import *


# WAITING


def Wait(seconds):
    return wait(seconds)


def WaitFrames(frames):
    return wait_frames(frames)


def WaitRandomSeconds(min_seconds, max_seconds):
    return wait_random_seconds(min_seconds, max_seconds)


def WaitForNetworkApproval(max_seconds):
    return wait_for_network_approval(max_seconds)


# CHARACTERS


def EnableCharacter(character):
    return chr.enable(character)


def DisableCharacter(character):
    return chr.disable(character)


def EnableAI(character):
    return chr.enable_ai(character)


def DisableAI(character):
    return chr.disable_ai(character)


def SetTeamType(character, new_team):
    return chr.set_team_type(character, new_team)


def Kill(character, award_souls=False):
    return chr.kill(character, award_souls=award_souls)


def EzstateAIRequest(character, command_id, slot_number):
    """ Slot number ranges from 0 to 3. """
    return chr.ezstate_ai_request(character, command_id, slot_number)


def AddSpecialEffect(character, special_effect_id):
    """ This will do nothing if the character already has the special effect active (they do not stack). """
    return chr.set_special_effect(character, special_effect_id)


def CancelSpecialEffect(character, special_effect_id):
    return chr.cancel_special_effect(character, special_effect_id)


def ResetStandbyAnimationSettings(character):
    return chr.set_standby_animation_settings_to_default(character)


def SetStandbyAnimationSettings(character, standby_animation=-1, damage_animation=-1, cancel_animation=-1,
                                death_animation=-1, standby_return_animation=-1):
    """ No point having instructions to set these individually, as they must all be set at once. """
    return chr.set_standby_animation_settings(character, standby_animation, damage_animation, cancel_animation,
                                              death_animation, standby_return_animation)


def EnableGravity(character):
    return chr.enable_gravity(character)


def DisableGravity(character):
    return chr.disable_gravity(character)


def EnableImmortality(character):
    return chr.enable_immortality(character)


def DisableImmortality(character):
    return chr.disable_immortality(character)


def SetNest(character, region):
    return chr.set_nest(character, region)


def RotateToFaceEntity(character, target_entity):
    """ Target entity can be of any type.

    WARNING: This instruction will crash your script (silently) if used on a disabled character.
    """
    return chr.rotate_to_face_entity(character, target_entity)


def EnableInvincibility(character):
    """ Character HP cannot be changed (positively or negatively) by anything. """
    return chr.enable_invincibility(character)


def DisableInvincibility(character):
    return chr.disable_invincibility(character)


def ClearTargetList(character):
    """ Clear list of targets from character AI. """
    return chr.clear_ai_target_list(character)


def AICommand(character, command_id, slot_number):
    """ These instructions can be accessed in AI Lua scripts. """
    return chr.ai_instruction(character, command_id, slot_number)


def SetEventPoint(character, region_id, reaction_range):
    """ Not sure what the usage of this is, but it is likely used to change patrol behavior. """
    return chr.set_event_point(character, region_id, reaction_range)


def SetAIParamID(character, ai_param_id):
    return chr.set_ai_id(character, ai_param_id)


def ReplanAI(character):
    """ Force character to replan their AI. """
    return chr.replan_ai(character)


def CreateNPCPart(character, part_npc_type, part_index, part_health,
                  damage_correction, body_damage_correction, is_invincible, start_in_stop_state):
    """ Obviously complex. Look at tail cut events to understand it. """
    return chr.create_multipart_npc_part(character, part_npc_type, part_index, part_health, damage_correction,
                                         body_damage_correction, is_invincible, start_in_stop_state)


def SetNPCPartHealth(character, part_npc_type, desired_hp, overwrite_max):
    return chr.set_multipart_npc_part_health(character, part_npc_type, desired_hp, overwrite_max)


def SetNPCPartEffects(character, part_npc_type, material_special_effect_id, material_fx_id):
    return chr.set_multipart_npc_part_effects(character, part_npc_type, material_special_effect_id, material_fx_id)


def SetNPCPartBulletDamageScaling(character, part_npc_type, desired_scaling):
    return chr.set_multipart_npc_part_bullet_damage_scaling(character, part_npc_type, desired_scaling)


def SetDisplayMask(character, bit_number, switch_type):
    """ Different bits correspond to different parts of the character model. You can see the initial values for these
    in the NPC params. This is generally used to disable tails when they are cut off.

    'switch_type' can be 0 (off), 1 (on), or 2 (change). """
    return chr.set_display_mask(character, bit_number, switch_type)


def SetHitboxMask(character, bit_number, switch_type):
    """ Different bits correspond to different parts of the character model. You can see the initial values for these
    in the NPC params. This is generally used to disable tails when they are cut off.

    'switch_type' can be 0 (off), 1 (on), or 2 (change). """
    return chr.set_hitbox_mask(character, bit_number, switch_type)


def SetNetworkUpdateAuthority(character, authority_level):
    """ Complex; look at existing usage. This only has two settings: 0 (normal) and 4095 (forced). I'm not going to
    encourage you to mess with this by adding simplified calls to those two settings. """
    return chr.set_network_update_authority(character, authority_level)


def EnableBackread(character):
    """ I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread' of
    a character has more effect on game resource. """
    return chr.enable_backread(character)


def DisableBackread(character):
    """ I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread' of
    a character has more effect on game resource. """
    return chr.disable_backread(character)


def EnableHealthBar(character):
    """ Normal health bar that appears above character. """
    return chr.enable_health_bar(character)


def DisableHealthBar(character):
    """ Normal health bar that appears above character. Note that it is disabled automatically if you give them a
    boss health bar. """
    return chr.disable_health_bar(character)


def EnableBossHealthBar(character, name_id, slot=0):
    """ The character's health bar will appear at the bottom of the screen, with a name. There are two slots, 0 and 1,
    that you can use, but no more. (0 is the lower slot, and the default here.) """
    return boss.enable_boss_health_bar_with_slot(character, name_id, slot)


def DisableBossHealthBar(character):
    """ The character's health bar will disappear from the bottom of the screen.

    WARNING: Disabling either boss health will disable both of them, so there's no 'slot' argument. """
    return boss.enable_boss_health_bar_with_slot(character, 0, 0)


def EnableCollision(character):
    return chr.enable_collision(character)


def DisableCollision(character):
    return chr.disable_collision(character)


def AIEvent(character, command_id, slot_number, first_event_flag, last_event_flag):
    """ I have no idea what this does. """
    return chr.ai_event(character, command_id, slot_number, first_event_flag, last_event_flag)


def ReferDamageToEntity(character, target_entity):
    """ All damage dealt to the first character will also be dealt to the target entity. I'm not 100% sure if the
    target entity can be an Object. Only used by the Four Kings in the vanilla game, but works anywhere. """
    return chr.refer_damage_to_entity(character, target_entity)


def SetNetworkUpdateRate(character, is_fixed, frequency):
    """ Not sure what 'is_fixed' does.

    Frequency:
        -1: "Never",
        0: "Always",
        2: "Every 2 frames",
        5: "Every 5 frames
    """
    return chr.set_network_update_rate(character, is_fixed, frequency)


def __SetBackreadStateAlternate(character, desired_state):
    """ I have no idea how this differs to the standard backread function, so I'm hiding it for now. """
    return chr.set_backread_state_alternate(character, desired_state)


def DropMandatoryTreasure(character):
    """ This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this. """
    return chr.drop_mandatory_treasure(character)


def SetTeamTypeAndExitStandbyAnimation(character, new_team):
    """ Two for the price of one. Often used when NPCs become hostile, for example. """
    return chr.set_team_type_and_exit_standby_animation(character, new_team)


def HumanityRegistration(character, event_flag):
    """ I believe this designates the first event flag in a range of some predefined size, which tracks how much
    humanity an NPC has for draining with Dark Hand. These flags are all in the 8000 range, and tightly packed, so
    you'll need to find your own range if you want to replicate this.

    I can confirm that NOT doing this for a new NPC means you can't drain any humanity from them.
    """
    return chr.humanity_registration(character, event_flag)


def ResetAnimation(character, disable_interpolation=False):
    return chr.reset_animation(character, disable_interpolation)


def ActivateMultiplayerBuffs(character):
    """ Used to strengthen bosses based on the number of summons you have. Not sure if it works for anyone. """
    return chr.activate_npc_buffs(character)


# OBJECTS


def EnableObject(obj):
    return objects.enable(obj)


def DisableObject(obj):
    return objects.disable(obj)


def DestroyObject(obj, slot=0):
    """ Technically 'requests' the object's destruction. No idea what the slot number does. """
    return objects.destroy(obj, slot)


def RestoreObject(obj):
    """ The opposite of destruction. Restores it to its original MSB coordinates. """
    return objects.restore(obj)


def EnableTreasure(obj):
    """ Enables any treasure attached to this object by MSB events. """
    return objects.enable_treasure(obj)


def DisableTreasure(obj):
    """ Disables any treasure attached to this object by MSB events.

    Tip: If you want to disable treasure by default, you can do it in the MSB by changing a certain event value to 255.
    """
    return objects.disable_treasure(obj)


def ActivateObject(obj, objact_param_id, relative_idx):
    """ Manually call a specific ObjAct event attached to this object. I believe 'relative_idx' refers to the locations
    on the object at which it can be activated (e.g. which side of a gate you are on).

    Tip: This will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how the
    game gets Patches to pull the lever in the Catacombs.
    """
    return objects.start_object_activation(obj, objact_param_id, relative_idx)


def EnableObjectActivation(obj, objact_param_id, relative_idx=None):
    """ Allows the given ObjAct to be performed with the object, optionally only at the given relative_idx. I've
    combined two instructions into one here, as they're very similar. """
    if relative_idx is None:
        return objects.enable_activation(obj, objact_param_id)
    return objects.activate_object_with_idx(obj, objact_param_id, relative_idx)


def DisableObjectActivation(obj, objact_param_id, relative_idx=None):
    """ Prevents the given ObjAct from being performed with the object. Used for doors that you can only open once,
    for example. Again, I've combined the relative_idx version here. """
    if relative_idx is None:
        return objects.disable_activation(obj, objact_param_id)
    return objects.deactivate_object_with_idx(obj, objact_param_id, relative_idx)


def PostDestruction(obj, slot):
    """ Sets the object to whatever appearance it would have after being destroyed. Again, not sure what 'slot'
    does. It might affect the way the object is destroyed. """
    return objects.end_destruction(obj, slot)


def CreateHazard(obj_flag, obj, damipoly_id, behavior_param_id, target_type, radius, life, repetition_time):
    """ Turn an object into an environmental hazard. It deals damage when touched according to the NPC Behavior param
    you give it. The damipoly_id determines which part of the object is hazardous (with the given radius and life,
    relative to the time this instruction occurs).

    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.

    'target_type' can be 1 (Character), 2 (Map), or 3 (Character and Map), which determines what it can damage.
    """
    return objects.create_damaging_object(obj_flag, obj, damipoly_id, behavior_param_id,
                                          target_type, radius, life, repetition_time)


def RegisterStatue(obj, game_map: Map, statue_type):
    """ Creates a petrified or crystallized statue. I believe this is so it can be seen by other players online. """
    return objects.register_statue_object(obj, game_map.block_id, game_map.sub_id, statue_type)


def RemoveObjectFlag(obj_flag):
    """ No idea what this does. """
    return objects.remove_object_event_flag(obj_flag)


def EnableObjectInvulnerability(obj):
    return objects.enable_invulnerability(obj)


def DisableObjectInvulnerability(obj):
    return objects.disable_invulnerability(obj)


def EnableTreasureCollection(obj):
    """ Not sure what this does, but if I were to guess, I'd say it would allow the player to pick up some treasure. """
    return objects.enable_treasure_collection(obj)


# FLAGS


def EnableFlag(event_flag):
    return flags.enable(event_flag)


def DisableFlag(event_flag):
    return flags.disable(event_flag)


def EnableRandomFlagInRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return flags.set_random_in_chunk(flag_range, last_flag, 1)
    return flags.set_random_in_chunk(flag_range.first, flag_range.last, 1)


def DisableRandomFlagInRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return flags.set_random_in_chunk(flag_range, last_flag, 0)
    return flags.set_random_in_chunk(flag_range.first, flag_range.last, 0)


def EnableFlagRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return flags.set_flag_chunk_state(flag_range, last_flag, 1)
    return flags.set_flag_chunk_state(flag_range.first, flag_range.last, 1)


def DisableFlagRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return flags.set_flag_chunk_state(flag_range, last_flag, 0)
    return flags.set_flag_chunk_state(flag_range.first, flag_range.last, 0)


def IncrementEventValue(flag, bit_count, max_value):
    """ You can use a contiguous array of flags as a single value. Use this to increment that value. The array begins
    at 'flag' and extends for 'bit_count'. (For example, a 'bit_count' of 4 gives you a theoretical maximum of 256. """
    return flags.increment_event_value(flag, bit_count, max_value)


def ClearEventValue(flag, bit_count):
    """ Clears the given multi-flag. This is basically like disabling 'bit_count' flags in a row, starting at
    'flag'. """
    return flags.clear_event_value(flag, bit_count)


def EnableThisFlag():
    """ Handled by the compiler. """
    pass


def DisableThisFlag():
    """ Handled by the compiler. """
    pass


# EVENTS


def RestartEvent(event_id, slot=0):
    """ Force a running event to restart. Note that the event must be active (i.e. not finished) for this to work. If
    you plan to have an event restarted, make sure it doesn't terminate until you no longer need it. """
    return event.set_event_id_state_with_slot(event_id, slot, 1)


def StopEvent(event_id, slot=0):
    """ Force a running event to stop. """
    return event.set_event_id_state_with_slot(event_id, slot, 0)


# HITBOXES


def EnableHitbox(hitbox_id):
    """ Enable a hitbox (sometimes called a 'collision'). The ID is specified in the MSB. Note that a hitbox doesn't
    have to be solid ground, but could be anything triggered by collision, such as a kill plane. """
    return hitboxes.set_hitbox_state(hitbox_id, 1)


def DisableHitbox(hitbox_id):
    """ Enable a hitbox (sometimes called a 'collision'). The ID is specified in the MSB. Note that a hitbox doesn't
    have to be solid ground, but could be anything triggered by collision, such as a kill plane (which this is often
    used to disable). """
    return hitboxes.set_hitbox_state(hitbox_id, 0)


# ITEMS


def AwardItemLot(item_lot_param_id, host_only=True):
    """ Directly award an item lot to the player. By default, only the host receives the item. """
    if host_only:
        return items.award_item_to_host_only(item_lot_param_id)
    return items.award_item_lot(item_lot_param_id)


def RemoveItemsFromPlayer(item: Item):
    """ Item type is automatically detected. This instruction has a 'quantity' argument, but it seems broken, so you
    always have to remove *all* instances of the item. (Strangely, the similar command used in EzState doesn't seem to
    have this bug.) """
    return items.remove_items_from_player(item.get_type(), item.value, quantity=0)


def SnugglyItemDrop(item_lot_param_id, region: Region, flag: Flag, hitbox: Hitbox):
    """ Makes Snuggly drop an item. There are complex limitations to this in the engine, so be careful. (The list of
    available Snuggly flags is a hard-coded limit, for example.) """
    return items.snuggly_item_drop(item_lot_param_id, region, flag, hitbox)


def SetNextSnugglyTrade(flag: Flag):
    return items.set_snuggly_next_trade(flag)


# ANIMATIONS


def RequestAnimation(entity, animation_id, loop=False, wait_for_completion=False):
    """ Not used very often, in favor of ForceAnimation below. """
    return anim.animation_playback_request(entity, animation_id, loop, wait_for_completion)


def ForceAnimation(entity, animation_id, loop=False, wait_for_completion=False, skip_transition=False):
    return anim.force_animation(entity, animation_id, loop, wait_for_completion, skip_transition)


def EnableAnimations(entity):
    return anim.set_animation_state(entity, 1)


def DisableAnimations(entity):
    return anim.set_animation_state(entity, 0)


def PostAnimation(entity, animation_id):
    """ Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. """
    return anim.end_animation(entity, animation_id)


# FX


def CreateFX(fx_id):
    """ Create visual FX. The ID is given in the MSB. """
    return sfx.create_map_sfx(fx_id)


def DeleteFX(fx_id, erase_root_only=True):
    """ Delete visual FX. If 'erase_root_only' is True (default), FX particles already emitted will live out the rest of
    their lifetimes. The ID is given in the MSB. """
    return sfx.delete_map_sfx(fx_id, erase_root_only)


def CreateTemporaryFX(fx_id, anchor_entity: Entity, damipoly_id):
    """ Create one-off visual FX attached to the given 'anchor_entity'. The FX type argument is determined from the
    Entity category. """
    if anchor_entity.category is None:
        raise ValueError("Anchor entity must be an Object, Region, or Character.")
    return sfx.create_oneoff_sfx(anchor_entity.category, anchor_entity, damipoly_id, fx_id)


def CreateObjectFX(fx_id, obj: Object, damipoly_id):
    return sfx.create_object_sfx(obj, damipoly_id, fx_id)


def DeleteObjectFX(obj: Object, erase_root=True):
    return sfx.delete_object_sfx(obj, erase_root)


# AUDIO


def PlaySoundEffect(anchor_entity: Entity, sound_type, sound_id):
    """ Anchor entity determines the localization of the sound, and the sound type is used to look up the source. """
    return sound.play_sound_effect(anchor_entity, sound_type, sound_id)


def EnableMapSound(sound_id):
    """ The sound ID is in the MSB. Used for boss music and ambiance. """
    return sound.set_map_sound(sound_id, 1)


def DisableMapSound(sound_id):
    """ The sound ID is in the MSB. Used for boss music and ambiance. """
    return sound.set_map_sound(sound_id, 0)


# MAP


def ActivateKillplane(game_map: Map, y_threshold, target_model_id):
    """ Not used much. Not sure why the target is a 'model'. """
    return map.activate_player_killplane(game_map.block_id, game_map.sub_id, y_threshold, target_model_id)


def RegisterLadder(obj: Object, start_climbing_flag, stop_climbing_flag):
    """ I've changed the order of arguments here. Don't mess with these flags, generally; you can just delay when this
    is called after map load to disable certain ladders (which is kind of weird anyway). """
    return map.register_ladder(start_climbing_flag, stop_climbing_flag, obj)


def RegisterBonfire(obj: Object, bonfire_flag: Flag, reaction_distance=2.0, reaction_angle=180.0, kindle_level=0):
    """ I believe the bonfire flag tells the game where to keep track of its kindle level, or something like that. I
    don't recommend messing around with this much. The reaction distance, angle, and initial kindle level are all set
    to their standard defaults.

    Note that, for some reason, kindle level is defined in increments of 10.
    """
    return map.register_bonfire(bonfire_flag, obj, reaction_distance, reaction_angle, kindle_level)


def EnableMapPart(map_part_id):
    """ You can control the visibility of individual map parts (given an ID in the MSB). """
    return map.set_map_part_state(map_part_id, 1)


def DisableMapPart(map_part_id):
    """ You can control the visibility of individual map parts (given an ID in the MSB). """
    return map.set_map_part_state(map_part_id, 0)


# MESSAGES


def PlaceSummonSign(sign_type, character: Character, region: Region, summon_flag: Flag, dismissal_flag: Flag):
    """ If you set a black summon sign, the specified NPC will try to invade. """
    return messages.place_summon_sign(sign_type, character, region, summon_flag, dismissal_flag)


def EnableDeveloperMessage(message_id):
    """ Enable a developer message that has been added to the MSB. The text ID is set in the MSB as well. """
    return messages.set_tip_message_visibility(message_id, 1)


def DisableDeveloperMessage(message_id):
    """ Disable a developer message that has been added to the MSB. The text ID is set in the MSB as well. """
    return messages.set_tip_message_visibility(message_id, 0)


def DisplayDialog(text_id, anchor_entity: Entity, display_distance=3.0, button_type=ButtonType.ok_cancel,
                  number_buttons=NumberButtons.no_button):
    """ Display a dialog box at the bottom of the screen. You can't use this to get player input, but you can display
    short simple messages. It defaults to a box with no buttons (which is still dismissed when you press A).

    The 'display_distance' argument specifies how far you can move away from the 'anchor_entity' (which is required)
    before the message automatically disappears. """
    return messages.dialog(text_id, button_type, number_buttons, anchor_entity, display_distance)


def DisplayBanner(banner_type: TextBannerType):
    """ Display a pre-rendered banner. You'll have to change the textures to modify their content.

    Banner list:
        1: "VICTORY ACHIEVED",
        2: "YOU DIED",
        3: "YOU REVIVED",
        4: "YOU RECOVERED",
        5: "TARGET DESTROYED",
        6: "Ghost Death",
        7: "Black Ghost Death",
        8: "<CURRENT MAP NAME>",
        12: "CONGRATULATIONS",
        15: "YOU WIN",
        16: "YOU LOSE",
        17: "YOU DRAW"
    """
    return messages.banner(banner_type)


def DisplayStatus(text_id, pad_enabled=True):
    """ Displays a large message that appears at the top of the screen, such as the message that tells you how to
    remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get rid of
    the message until it times out on its own. """
    return messages.status_explanation(text_id, pad_enabled)


def DisplayBattlefieldMessage(text_id, display_location_index):
    """ Used in the Battle of Stoicism. Probably useless to you. """
    return messages.battlefield_message(text_id, display_location_index)


# CUTSCENE


def PlayCutscene(cutscene_id, skippable=False, fade_out=False, player_id=None,
                 warp_to_map: Map = None, warp_to_region: Region = None,
                 rotation=0.0, relative_rotation_axis_x=0.0, relative_rotation_axis_z=0.0, vertical_translation=0.0):
    """ Unified instruction for playing cutscenes. You can specify a player (defaults to self), control whether the
    cutscene is skippable (False by default) or fades out (False by default), and add extra warp arguments or
    rotation arguments. (You can't supply both warp and rotation arguments.)

    The warp arguments require both a Map and a Region.

    The 'relative_rotation_axis_x' and 'relative_rotation_axis_z' arguments let you set where the (vertical) rotation
    axis is, relative to the player's current position.
    """
    if skippable:
        cutscene_type = CutsceneType.skippable_with_fade_out if fade_out else CutsceneType.skippable
    else:
        cutscene_type = CutsceneType.unskippable_with_fade_out if fade_out else CutsceneType.unskippable

    if warp_to_map or warp_to_region:
        if not (warp_to_map and warp_to_region):
            raise ValueError("You must set both 'warp_to_map' and 'warp_to_region' for cutscene warps.")
        if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
            raise ValueError("You cannot use warp arguments *and* rotation/translation arguments for cutscenes.")
        if player_id is None:
            return cutscene.play_cutscene_and_warp_player(
                cutscene_id, cutscene_type, warp_to_region, warp_to_map.block_id, warp_to_map.sub_id)
        return cutscene.play_cutscene_and_warp_specific_player(
            cutscene_id, cutscene_type, warp_to_region, warp_to_map.block_id, warp_to_map.sub_id, player_id)

    if player_id is None:
        player_id = 10000

    if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
        return cutscene.play_cutscene_and_rotate_player(
            cutscene_id, cutscene_type, relative_rotation_axis_x, relative_rotation_axis_z, rotation,
            vertical_translation, player_id)

    return cutscene.play_cutscene_to_player(cutscene_id, cutscene_type, player_id)


# NAVIMESH


def EnableNavimeshType(navimesh_id, navimesh_type: NavimeshType):
    """ Mark a given navimesh with the given type, which affects how character AI will interact with it. The navimesh
    ID is set in the MSB. """
    return navimesh.modify_navimesh_collision_bitflags(navimesh_id, navimesh_type, 0)


def DisableNavimeshType(navimesh_id, navimesh_type: NavimeshType):
    """ Remove the given type from the given navimesh. The navimesh ID is set in the MSB. """
    return navimesh.modify_navimesh_collision_bitflags(navimesh_id, navimesh_type, 1)


def ToggleNavimeshType(navimesh_id, navimesh_type: NavimeshType):
    """ Set the given navimesh type to the opposite of whatever it currently is for the given navimesh. """
    return navimesh.modify_navimesh_collision_bitflags(navimesh_id, navimesh_type, 2)


# NETWORK


def EnableNetworkSync():
    return network.set_sync(1)


def DisableNetworkSync():
    return network.set_sync(0)


def IssuePrefetchRequest(request_id):
    """ No idea what this does. """
    return network.issue_prefetch_request(request_id)


def SaveRequest():
    """ The game saves often, but sometimes you need to save immediately, often after changing a spawn point, for
    example. (Sneaky logic will often save the game before the player realizes what's happened.) """
    return network.save_request()


def TriggerMultiplayerEvent(event_id):
    """ Used to make the Bell of Awakening sounds, for example. """
    return network.trigger_multiplayer_event(event_id)


def EnableVagrantSpawning():
    """ Allows Vagrants to spawn at all. """
    return network.set_vagrant_spawning(1)


def DisableVagrantSpawning():
    """ Prevents Vagrants from spawning at all. """
    return network.set_vagrant_spawning(0)


def IncrementPvPSin():
    """ Not recommended. """
    return network.increment_player_pvp_sin()


def NotifyBossBattleStart():
    """ Sends the message to all summons that the host has challenged the boss. """
    return network.notify_boss_room_entry()


# SPAWNER


def EnableSpawner(entity: MapEntity):
    return spawner.set_spawner_state(entity, 1)


def DisableSpawner(entity: MapEntity):
    return spawner.set_spawner_state(entity, 0)


def ShootProjectile(owner_entity: MapEntity, projectile_id, model_point, behavior_id,
                    launch_angle_x=0.0, launch_angle_y=0.0, launch_angle_z=0.0):
    """ The owner entity sets the 'team' of the projectile (i.e. who it can hurt). """
    return spawner.shoot_projectile(owner_entity, projectile_id, model_point, behavior_id,
                                    launch_angle_x, launch_angle_y, launch_angle_z)


def CreateSpawner(entity: MapEntity):
    """ A 'bullet owner' that will spawn things according to the Spawner section of the MSB. """
    return spawner.create_spawner(entity)


# WARP


def WarpToMap(game_map: Map, player_entity_id=-1):
    """ Warp the main player to the given Player entity ID, which is in the Players tab of the MSB, in some map. By
    default, this warps to the 'default position' in the map (-1). """
    return warp.warp_player(game_map.block_id, game_map.sub_id, player_entity_id)


def MoveRemains(source_region: Region, destination_region: Region):
    """ Move all bloodstains and dropped items from one region to another (I assume). """
    return warp.move_dropped_items_and_bloodstains(source_region, destination_region)


def WarpToRegion(character: Character, destination: MapEntity, model_point,
                 copy_draw_hitbox=None, set_draw_hitbox=None, short_warp=False):
    """ Unified instruction for warping to some entity in the same map. Not sure what sort of optimizations 'short'
    makes, but it's used at various times by the game. You can change the owner hitbox of the warped character, which
    changes when it will be drawn. """
    destination_type = destination.category
    if copy_draw_hitbox and set_draw_hitbox:
        raise ValueError("You cannot copy and set the draw hitbox at the same time.")
    if short_warp:
        if copy_draw_hitbox or set_draw_hitbox:
            raise ValueError("You cannot copy or set the draw hitbox during a short warp.")
        return warp.short_warp(character, destination_type, destination, model_point)
    if copy_draw_hitbox:
        return warp.warp_and_copy_floor(character, destination_type, destination, model_point, copy_draw_hitbox)
    if set_draw_hitbox:
        return warp.warp_and_copy_floor(character, destination_type, destination, model_point, set_draw_hitbox)
    return warp.warp(character, destination_type, destination, model_point)


def WarpObjectToCharacter(obj: Object, character: Character, model_point):
    return warp.warp_object_to_character(obj, character, model_point)


def SetRespawnPoint(respawn_point_id):
    """ Respawn point is an event set in the MSB. """
    return warp.set_player_respawn_point(respawn_point_id)


# MISCELLANEOUS


def KillBoss(game_area_param_id):
    """ The name is slightly misleading, as this doesn't actually kill any entity. Instead, it marks that you have
    cleared an 'area', as defined by the Game Area params, and is always manually called in EMEVD when you kill the boss
    of that area.

    Among other things, this awards your souls for killing the boss (which is why they are delayed and why the game will
    keep trying to give them to you on map load) and prevents you from summoning other players.

    The Game Area param ID is generally identical to the entity ID of the appropriate boss, but this is just convention,
    albeit one you should stick to for a sensible setup.
    """
    return boss.kill_boss(game_area_param_id)


def IncrementNewGameCycle():
    return game.increment_new_game_plus_counter()


def AwardAchievement(achievement_id):
    """ For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing events. This interacts with Steam, which is always dangerous. """
    return game.award_achievement(achievement_id)


def BetrayCurrentCovenant():
    """ You'll obviously want to make sure you know what covenant the player has when using this. """
    return game.betray_current_covenant()


def EqualRecovery():
    """ Unknown. HotPocketRemix speculates it may trigger a garbage collection. I'm not sure when it's used. """
    return game.equal_recovery()


def SetLockedCameraSlot(game_map: Map, locked_camera_slot):
    """ This isn't used very often; standard camera control is done with camera params in the MSB. """
    return game.set_locked_camera_slot_number(game_map.block_id, game_map.sub_id, locked_camera_slot)


def HellkiteBreathControl(character, obj, animation_id):
    """ I don't recommend you mess with this. """
    return game.hellkite_breath_control(character, obj, animation_id)


def SetMapDrawParamsSlot(map_block_id, slot):
    """ Each map block (NOT each map) can have two sets of DrawParams (0 and 1), and this can be used to switch
    between them. Originally only used for Dark Anor Londo. Note that """
    if isinstance(map_block_id, Map):
        raise ValueError("DrawParams can only be set for a whole map *block* (e.g. block 15 for Sen's Fortress and "
                         "Anor Londo). I'm making you set the block ID so you don't forget this.")
    return light.set_area_texture_parambank_slot_index(map_block_id, slot)

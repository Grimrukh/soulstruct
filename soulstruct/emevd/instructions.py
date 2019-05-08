from typing import Optional, Union
from soulstruct.emevd.ds_types import *
import soulstruct.emevd.pydses as p
from soulstruct.emevd.pydses.event_enums import *


# TYPING HINTS

CharacterInt = Union[Character, int]
FlagInt = Union[Flag, int]
HitboxInt = Union[Hitbox, int]
MapEntityInt = Union[MapEntity, int]
ObjectInt = Union[Object, int]
RegionInt = Union[Region, int]
TextInt = Union[Text, int]


# RUN

def RunEvent(event_id, slot=0, args=(0,), arg_types=None):
    if arg_types is None:
        arg_types = 'I' * len(args)
    return p.run_event_with_slot(event_id, event_slot_number=slot, args=args, arg_types=arg_types)


# WAITING

def Wait(seconds):
    return p.wait(seconds)


def WaitFrames(frames):
    return p.wait_frames(frames)


def WaitRandomSeconds(min_seconds, max_seconds):
    return p.wait_random_seconds(min_seconds, max_seconds)


def WaitForNetworkApproval(max_seconds):
    return p.wait_for_network_approval(max_seconds)


# CHARACTERS


def EnableCharacter(character: CharacterInt):
    return p.chr.enable(character)


def DisableCharacter(character: CharacterInt):
    return p.chr.disable(character)


def SetCharacterState(character: CharacterInt, state):
    return p.chr.set_character_state(character, state)


def EnableAI(character: CharacterInt):
    return p.chr.enable_ai(character)


def DisableAI(character: CharacterInt):
    return p.chr.disable_ai(character)


def SetAIState(character, state):
    return p.chr.set_ai(character, state)


def SetTeamType(character: CharacterInt, new_team):
    return p.chr.set_team_type(character, new_team)


def Kill(character: CharacterInt, award_souls=False):
    return p.chr.kill(character, award_souls=award_souls)


def EzstateAIRequest(character: CharacterInt, command_id, slot):
    """ Slot number ranges from 0 to 3. """
    return p.chr.ezstate_ai_request(character, command_id, slot)


def AddSpecialEffect(character: CharacterInt, special_effect_id):
    """ This will do nothing if the character already has the special effect active (they do not stack). """
    return p.chr.set_special_effect(character, special_effect_id)


def CancelSpecialEffect(character: CharacterInt, special_effect_id):
    return p.chr.cancel_special_effect(character, special_effect_id)


def ResetStandbyAnimationSettings(character: CharacterInt):
    return p.chr.set_standby_animation_settings_to_default(character)


def SetStandbyAnimationSettings(character: CharacterInt, standby_animation=-1, damage_animation=-1, cancel_animation=-1,
                                death_animation=-1, standby_return_animation=-1):
    """ No point having instructions to set these individually, as they must all be set at once. """
    return p.chr.set_standby_animation_settings(character, standby_animation, damage_animation, cancel_animation,
                                                death_animation, standby_return_animation)


def EnableGravity(character: CharacterInt):
    return p.chr.enable_gravity(character)


def DisableGravity(character: CharacterInt):
    return p.chr.disable_gravity(character)


def SetGravityState(character: CharacterInt, state):
    return p.chr.set_gravity(character, state)


def EnableImmortality(character: CharacterInt):
    return p.chr.enable_immortality(character)


def DisableImmortality(character: CharacterInt):
    return p.chr.disable_immortality(character)


def SetImmortalityState(character: CharacterInt, state):
    return p.chr.set_immortality(character, state)


def SetNest(character: CharacterInt, region: RegionInt):
    return p.chr.set_nest(character, region)


def RotateToFaceEntity(character: CharacterInt, target_entity: MapEntityInt):
    """ Target entity can be of any type.

    WARNING: This instruction will crash its event script (silently) if used on a disabled character.
    """
    return p.chr.rotate_to_face_entity(character, target_entity)


def EnableInvincibility(character: CharacterInt):
    """ Character HP cannot be changed (positively or negatively) by anything. """
    return p.chr.enable_invincibility(character)


def DisableInvincibility(character: CharacterInt):
    return p.chr.disable_invincibility(character)


def SetInvincibilityState(character: CharacterInt, state):
    return p.chr.set_immortality(character, state)


def ClearTargetList(character: CharacterInt):
    """ Clear list of targets from character AI. """
    return p.chr.clear_ai_target_list(character)


def AICommand(character: CharacterInt, command_id, slot):
    """ These instructions can be accessed in AI Lua scripts. """
    return p.chr.ai_instruction(character, command_id, slot)


def SetEventPoint(character: CharacterInt, region_id, reaction_range):
    """ Not sure what the usage of this is, but it is likely used to change patrol behavior. """
    return p.chr.set_event_point(character, region_id, reaction_range)


def SetAIParamID(character: CharacterInt, ai_param_id):
    return p.chr.set_ai_id(character, ai_param_id)


def ReplanAI(character: CharacterInt):
    """ Force character to replan their AI. """
    return p.chr.replan_ai(character)


def CreateNPCPart(character: CharacterInt, part_npc_type, part_index, part_health,
                  damage_correction, body_damage_correction, is_invincible, start_in_stop_state):
    """ Obviously complex. Look at tail cut events to understand it. """
    return p.chr.create_multipart_npc_part(character, part_npc_type, part_index, part_health, damage_correction,
                                           body_damage_correction, is_invincible, start_in_stop_state)


def SetNPCPartHealth(character: CharacterInt, part_npc_type, desired_hp, overwrite_max):
    return p.chr.set_multipart_npc_part_health(character, part_npc_type, desired_hp, overwrite_max)


def SetNPCPartEffects(character: CharacterInt, part_npc_type, material_special_effect_id, material_fx_id):
    return p.chr.set_multipart_npc_part_effects(character, part_npc_type, material_special_effect_id, material_fx_id)


def SetNPCPartBulletDamageScaling(character: CharacterInt, part_npc_type, desired_scaling):
    return p.chr.set_multipart_npc_part_bullet_damage_scaling(character, part_npc_type, desired_scaling)


def SetDisplayMask(character: CharacterInt, bit_index, switch_type):
    """ Different bits correspond to different parts of the character model. You can see the initial values for these
    in the NPC params. This is generally used to disable tails when they are cut off.

    'switch_type' can be 0 (off), 1 (on), or 2 (change). """
    return p.chr.set_display_mask(character, bit_index, switch_type)


def SetHitboxMask(character: CharacterInt, bit_index, switch_type):
    """ Different bits correspond to different parts of the character model. You can see the initial values for these
    in the NPC params. This is generally used to disable tails when they are cut off.

    'switch_type' can be 0 (off), 1 (on), or 2 (change). """
    return p.chr.set_hitbox_mask(character, bit_index, switch_type)


def SetNetworkUpdateAuthority(character: CharacterInt, authority_level):
    """ Complex; look at existing usage. This only has two settings: 0 (normal) and 4095 (forced). I'm not going to
    encourage you to mess with this by adding simplified calls to those two settings. """
    return p.chr.set_network_update_authority(character, authority_level)


def EnableBackread(character: CharacterInt):
    """ I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread' of
    a character has more effect on game resource. """
    return p.chr.enable_backread(character)


def DisableBackread(character: CharacterInt):
    """ I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread' of
    a character has more effect on game resource. """
    return p.chr.disable_backread(character)


def EnableHealthBar(character: CharacterInt):
    """ Normal health bar that appears above character. """
    return p.chr.enable_health_bar(character)


def DisableHealthBar(character: CharacterInt):
    """ Normal health bar that appears above character. Note that it is disabled automatically if you give them a
    boss health bar. """
    return p.chr.disable_health_bar(character)


def SetHealthBarState(character: CharacterInt, state):
    return p.chr.set_health_bar_display(character, state)


def EnableBossHealthBar(character: CharacterInt, name_id, slot=0):
    """ The character's health bar will appear at the bottom of the screen, with a name. There are two slots, 0 and 1,
    that you can use, but no more. (0 is the lower slot, and the default here.) """
    return p.boss.enable_boss_health_bar_with_slot(character, slot, name_id)


def DisableBossHealthBar(character: CharacterInt, name_id=0, slot=0):
    """ The character's health bar will disappear from the bottom of the screen.

    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so only the
    first argument actually does anything. """
    return p.boss.disable_boss_health_bar_with_slot(character, slot, name_id)


def EnableCollision(character: CharacterInt):
    return p.chr.enable_collision(character)


def DisableCollision(character: CharacterInt):
    return p.chr.disable_collision(character)


def SetCollisionState(character: CharacterInt, is_disabled):
    return p.chr.set_collision(character, is_disabled)


def AIEvent(character: CharacterInt, command_id, slot, first_event_flag, last_event_flag):
    """ I have no idea what this does. """
    return p.chr.ai_event(character, command_id, slot, first_event_flag, last_event_flag)


def ReferDamageToEntity(character: CharacterInt, target_entity):
    """ All damage dealt to the first character will also be dealt to the target entity. I'm not 100% sure if the
    target entity can be an Object. Only used by the Four Kings in the vanilla game, but works anywhere. """
    return p.chr.refer_damage_to_entity(character, target_entity)


def SetNetworkUpdateRate(character: CharacterInt, is_fixed, frequency):
    """ Not sure what 'is_fixed' does.

    Frequency:
        -1: "Never",
        0: "Always",
        2: "Every 2 frames",
        5: "Every 5 frames
    """
    return p.chr.set_network_update_rate(character, is_fixed, frequency)


def SetBackreadStateAlternate(character: CharacterInt, desired_state):
    """ I have no idea how this differs to the standard backread function. """
    return p.chr.set_backread_state_alternate(character, desired_state)


def DropMandatoryTreasure(character: CharacterInt):
    """ This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this. """
    return p.chr.drop_mandatory_treasure(character)


def SetTeamTypeAndExitStandbyAnimation(character: CharacterInt, new_team):
    """ Two for the price of one. Often used when NPCs become hostile, for example. """
    return p.chr.set_team_type_and_exit_standby_animation(character, new_team)


def HumanityRegistration(character: CharacterInt, event_flag: FlagInt):
    """ I believe this designates the first event flag in a range of some predefined size, which tracks how much
    humanity an NPC has for draining with Dark Hand. These flags are all in the 8000 range, and tightly packed, so
    you'll need to find your own range if you want to replicate this.

    I can confirm that NOT doing this for a new NPC means you can't drain any humanity from them.
    """
    return p.chr.humanity_registration(character, event_flag)


def ResetAnimation(character, disable_interpolation=False):
    return p.chr.reset_animation(character, disable_interpolation)


def ActivateMultiplayerBuffs(character: CharacterInt):
    """ Used to strengthen bosses based on the number of summons you have. Not sure if it works for anyone. """
    return p.chr.activate_npc_buffs(character)


# OBJECTS


def EnableObject(obj: ObjectInt):
    return p.objects.enable(obj)


def DisableObject(obj: ObjectInt):
    return p.objects.disable(obj)


def SetObjectState(obj: ObjectInt, state):
    return p.objects.set_object_state(obj, state)


def DestroyObject(obj, slot=0):
    """ Technically 'requests' the object's destruction. No idea what the slot number does. """
    return p.objects.destroy(obj, slot)


def RestoreObject(obj: ObjectInt):
    """ The opposite of destruction. Restores it to its original MSB coordinates. """
    return p.objects.restore(obj)


def EnableTreasure(obj: ObjectInt):
    """ Enables any treasure attached to this object by MSB events. """
    return p.objects.enable_treasure(obj)


def DisableTreasure(obj: ObjectInt):
    """ Disables any treasure attached to this object by MSB events.

    Tip: If you want to disable treasure by default, you can do it in the MSB by changing a certain event value to 255.
    """
    return p.objects.disable_treasure(obj)


def SetTreasureState(obj: ObjectInt, state):
    return p.objects.set_treasure_state(obj, state)


def ActivateObject(obj, objact_param_id, relative_idx):
    """ Manually call a specific ObjAct event attached to this object. I believe 'relative_idx' refers to the locations
    on the object at which it can be activated (e.g. which side of a gate you are on).

    Tip: This will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how the
    game gets Patches to pull the lever in the Catacombs.
    """
    return p.objects.start_object_activation(obj, objact_param_id, relative_idx)


def EnableObjectActivation(obj, objact_param_id, relative_idx=None):
    """ Allows the given ObjAct to be performed with the object, optionally only at the given relative_idx. I've
    combined two instructions into one here, as they're very similar. """
    if relative_idx is None:
        return p.objects.enable_activation(obj, objact_param_id)
    return p.objects.activate_object_with_idx(obj, objact_param_id, relative_idx)


def DisableObjectActivation(obj, objact_param_id, relative_idx=None):
    """ Prevents the given ObjAct from being performed with the object. Used for doors that you can only open once,
    for example. Again, I've combined the relative_idx version here. """
    if relative_idx is None:
        return p.objects.disable_activation(obj, objact_param_id)
    return p.objects.deactivate_object_with_idx(obj, objact_param_id, relative_idx)


def PostDestruction(obj, slot):
    """ Sets the object to whatever appearance it would have after being destroyed. Again, not sure what 'slot'
    does. It might affect the way the object is destroyed. """
    return p.objects.end_destruction(obj, slot)


def CreateHazard(obj_flag, obj, model_point, behavior_param_id, target_type, radius, life, repetition_time):
    """ Turn an object into an environmental hazard. It deals damage when touched according to the NPC Behavior param
    you give it. The model_point determines which part of the object is hazardous (with the given radius and life,
    relative to the time this instruction occurs).

    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.

    'target_type' can be 1 (Character), 2 (Map), or 3 (Character and Map), which determines what it can damage.
    """
    return p.objects.create_damaging_object(obj_flag, obj, model_point, behavior_param_id,
                                            target_type, radius, life, repetition_time)


def RegisterStatue(obj, game_map: Map, statue_type):
    """ Creates a petrified or crystallized statue. I believe this is so it can be seen by other players online. """
    return p.objects.register_statue_object(obj, game_map.block_id, game_map.sub_id, statue_type)


def RemoveObjectFlag(obj_flag):
    """ No idea what this does. """
    return p.objects.remove_object_event_flag(obj_flag)


def EnableObjectInvulnerability(obj: ObjectInt):
    return p.objects.enable_invulnerability(obj)


def DisableObjectInvulnerability(obj: ObjectInt):
    return p.objects.disable_invulnerability(obj)


def EnableTreasureCollection(obj: ObjectInt):
    """ Not sure what this does, but if I were to guess, I'd say it would allow the player to pick up some treasure. """
    return p.objects.enable_treasure_collection(obj)


# FLAGS


def EnableFlag(event_flag):
    return p.flags.enable(event_flag)


def DisableFlag(event_flag):
    return p.flags.disable(event_flag)


def SetFlagState(event_flag, state):
    return p.flags.set_flag_state(event_flag, state)


def EnableRandomFlagInRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return p.flags.set_random_in_chunk(flag_range, last_flag, 1)
    return p.flags.set_random_in_chunk(flag_range.first, flag_range.last, 1)


def DisableRandomFlagInRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return p.flags.set_random_in_chunk(flag_range, last_flag, 0)
    return p.flags.set_random_in_chunk(flag_range.first, flag_range.last, 0)


def EnableFlagRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return p.flags.set_flag_chunk_state(flag_range, last_flag, 1)
    return p.flags.set_flag_chunk_state(flag_range.first, flag_range.last, 1)


def DisableFlagRange(flag_range: Union[FlagRange, int], last_flag=None):
    if last_flag:
        return p.flags.set_flag_chunk_state(flag_range, last_flag, 0)
    return p.flags.set_flag_chunk_state(flag_range.first, flag_range.last, 0)


def IncrementEventValue(flag, bit_count, max_value):
    """ You can use a contiguous array of flags as a single value. Use this to increment that value. The array begins
    at 'flag' and extends for 'bit_count'. (For example, a 'bit_count' of 4 gives you a theoretical maximum of 256. """
    return p.flags.increment_event_value(flag, bit_count, max_value)


def ClearEventValue(flag, bit_count):
    """ Clears the given multi-flag. This is basically like disabling 'bit_count' flags in a row, starting at
    'flag'. """
    return p.flags.clear_event_value(flag, bit_count)


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
    return p.event.set_event_id_state_with_slot(event_id, slot, 1)


def StopEvent(event_id, slot=0):
    """ Force a running event to stop. """
    return p.event.set_event_id_state_with_slot(event_id, slot, 0)


# HITBOXES

def EnableHitbox(hitbox_id: HitboxInt):
    """ Enable a hitbox (sometimes called a 'collision'). The ID is specified in the MSB. Note that a hitbox doesn't
    have to be solid ground, but could be anything triggered by collision, such as a kill plane. """
    return p.hitboxes.set_hitbox_state(hitbox_id, 1)


def DisableHitbox(hitbox_id: HitboxInt):
    """ Enable a hitbox (sometimes called a 'collision'). The ID is specified in the MSB. Note that a hitbox doesn't
    have to be solid ground, but could be anything triggered by collision, such as a kill plane (which this is often
    used to disable). """
    return p.hitboxes.set_hitbox_state(hitbox_id, 0)


def SetHitboxState(hitbox_id: HitboxInt, state):
    return p.hitboxes.set_hitbox_state(hitbox_id, state)


# ITEMS

def AwardItemLot(item_lot_param_id, host_only=True):
    """ Directly award an item lot to the player. By default, only the host receives the item. """
    if host_only:
        return p.items.award_item_to_host_only(item_lot_param_id)
    return p.items.award_item_lot(item_lot_param_id)


def RemoveItemFromPlayer(item: Union[Item, int], item_type=None, quantity=0):
    """ Item type is automatically detected. This instruction has a 'quantity' argument, but it seems broken, so you
    always have to remove *all* instances of the item. (Strangely, the similar command used in EzState doesn't seem to
    have this bug.) """
    if item_type is None:
        item_type = item.get_type()
    return p.items.remove_items_from_player(item_type, item, quantity=quantity)


def RemoveWeaponFromPlayer(weapon: Union[Weapon, int], quantity=0):
    """ Weapons only. """
    return p.items.remove_items_from_player(0, weapon, quantity=quantity)


def RemoveArmorFromPlayer(armor: Union[Armor, int], quantity=0):
    """ Armor only. """
    return p.items.remove_items_from_player(1, armor, quantity=quantity)


def RemoveRingFromPlayer(ring: Union[Ring, int], quantity=0):
    """ Rings only. """
    return p.items.remove_items_from_player(2, ring, quantity=quantity)


def RemoveGoodFromPlayer(good: Union[Good, int], quantity=0):
    """ Goods only. """
    return p.items.remove_items_from_player(3, good, quantity=quantity)


def SnugglyItemDrop(item_lot_param_id, region: RegionInt, flag: FlagInt, hitbox: HitboxInt):
    """ Makes Snuggly drop an item. There are complex limitations to this in the engine, so be careful. (The list of
    available Snuggly flags is a hard-coded limit, for example.) """
    return p.items.snuggly_item_drop(item_lot_param_id, region, flag, hitbox)


def SetNextSnugglyTrade(flag: FlagInt):
    return p.items.set_snuggly_next_trade(flag)


# ANIMATIONS

def RequestAnimation(entity, animation_id, loop=False, wait_for_completion=False):
    """ Not used very often, in favor of ForceAnimation below. """
    return p.anim.animation_playback_request(entity, animation_id, loop, wait_for_completion)


def ForceAnimation(entity, animation_id, loop=False, wait_for_completion=False, skip_transition=False):
    return p.anim.force_animation(entity, animation_id, loop, wait_for_completion, skip_transition)


def EnableAnimations(entity):
    return p.anim.set_animation_state(entity, 1)


def DisableAnimations(entity):
    return p.anim.set_animation_state(entity, 0)


def SetAnimationsState(entity, state):
    return p.anim.set_animation_state(entity, state)


def EndOfAnimation(entity, animation_id):
    """ Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. """
    return p.anim.end_animation(entity, animation_id)


# FX

def CreateFX(fx_id):
    """ Create visual FX. The ID is given in the MSB. """
    return p.sfx.create_map_sfx(fx_id)


def DeleteFX(fx_id, erase_root_only=True):
    """ Delete visual FX. If 'erase_root_only' is True (default), FX particles already emitted will live out the rest of
    their lifetimes. The ID is given in the MSB. """
    return p.sfx.delete_map_sfx(fx_id, erase_root_only)


def CreateTemporaryFX(fx_id, anchor_entity: MapEntityInt, model_point, anchor_type=None):
    """ Create one-off visual FX attached to the given 'anchor_entity'. The FX type argument is determined from the
    Entity category. """
    if anchor_type is None:
        try:
            anchor_type = anchor_entity.category
        except AttributeError:
            raise AttributeError("anchor_type not detected. Use the keyword 'anchor_type' or a typed anchor_entity.")
    return p.sfx.create_oneoff_sfx(anchor_type, anchor_entity, model_point, fx_id)


def CreateObjectFX(fx_id, obj: ObjectInt, model_point):
    return p.sfx.create_object_sfx(obj, model_point, fx_id)


def DeleteObjectFX(obj: ObjectInt, erase_root=True):
    return p.sfx.delete_object_sfx(obj, erase_root)


# AUDIO

def PlaySoundEffect(anchor_entity: MapEntityInt, sound_type, sound_id):
    """ Anchor entity determines the localization of the sound, and the sound type is used to look up the source. """
    return p.sound.play_sound_effect(anchor_entity, sound_type, sound_id)


def EnableMapSound(sound_id):
    """ The sound ID is in the MSB. Used for boss music and ambiance. """
    return p.sound.set_map_sound(sound_id, 1)


def DisableMapSound(sound_id):
    """ The sound ID is in the MSB. Used for boss music and ambiance. """
    return p.sound.set_map_sound(sound_id, 0)


def SetMapSoundState(sound_id, state):
    return p.sound.set_map_sound(sound_id, state)


# MAP

def ActivateKillplane(game_map: Map, y_threshold, target_model_id):
    """ Not used much. Not sure why the target is a 'model'. """
    return p.map.activate_player_killplane(game_map.block_id, game_map.sub_id, y_threshold, target_model_id)


def RegisterLadder(start_climbing_flag: FlagInt, stop_climbing_flag: FlagInt,
                   obj: ObjectInt):
    """ I've changed the order of arguments here. Don't mess with these flags, generally; you can just delay when this
    is called after map load to disable certain ladders (which is kind of weird anyway). """
    return p.map.register_ladder(start_climbing_flag, stop_climbing_flag, obj)


def RegisterBonfire(bonfire_flag: FlagInt, obj: ObjectInt, reaction_distance=2.0,
                    reaction_angle=180.0, initial_kindle_level=0):
    """ I believe the bonfire flag tells the game where to keep track of its kindle level, or something like that. I
    don't recommend messing around with this much. The reaction distance, angle, and initial kindle level are all set
    to their standard defaults.

    Note that, for some reason, kindle level is defined in increments of 10.
    """
    return p.map.register_bonfire(bonfire_flag, obj, reaction_distance, reaction_angle, initial_kindle_level)


def EnableMapPart(map_part_id):
    """ You can control the visibility of individual map parts (given an ID in the MSB). """
    return p.map.set_map_part_state(map_part_id, 1)


def DisableMapPart(map_part_id):
    """ You can control the visibility of individual map parts (given an ID in the MSB). """
    return p.map.set_map_part_state(map_part_id, 0)


def SetMapPartState(map_part_id, state):
    return p.map.set_map_part_state(map_part_id, state)


# MESSAGES

def PlaceSummonSign(sign_type, character: CharacterInt, region: RegionInt,
                    summon_flag: FlagInt, dismissal_flag: FlagInt):
    """ If you set a black summon sign, the specified NPC will try to invade. """
    return p.messages.place_summon_sign(sign_type, character, region, summon_flag, dismissal_flag)


def EnableDeveloperMessage(message_id):
    """ Enable a developer message that has been added to the MSB. The text ID is set in the MSB as well. """
    return p.messages.set_tip_message_visibility(message_id, 1)


def DisableDeveloperMessage(message_id):
    """ Disable a developer message that has been added to the MSB. The text ID is set in the MSB as well. """
    return p.messages.set_tip_message_visibility(message_id, 0)


def SetDeveloperMessageState(message_id, visible):
    """ Enable or disable developer message. """
    return p.messages.set_tip_message_visibility(message_id, visible)


def DisplayDialog(text_id, anchor_entity: MapEntityInt, display_distance=3.0, button_type=p.ButtonType.ok_cancel,
                  number_buttons=p.NumberButtons.no_button):
    """ Display a dialog box at the bottom of the screen. You can't use this to get player input, but you can display
    short simple messages. It defaults to a box with no buttons (which is still dismissed when you press A).

    The 'display_distance' argument specifies how far you can move away from the 'anchor_entity' (which is required)
    before the message automatically disappears. """
    return p.messages.dialog(text_id, button_type, number_buttons, anchor_entity, display_distance)


def DisplayBanner(banner_type: p.TextBannerType):
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
    return p.messages.banner(banner_type)


def DisplayStatus(text_id, pad_enabled=True):
    """ Displays a large message that appears at the top of the screen, such as the message that tells you how to
    remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get rid of
    the message until it times out on its own. """
    return p.messages.status_explanation(text_id, pad_enabled)


def DisplayBattlefieldMessage(text_id, display_location_index):
    """ Used in the Battle of Stoicism. Probably useless to you. """
    return p.messages.battlefield_message(text_id, display_location_index)


# CUTSCENE

def PlayCutscene(cutscene_id, skippable=False, fade_out=False, player_id=None,
                 warp_to_map: Map = None, warp_to_region: RegionInt = None,
                 rotation=0.0, relative_rotation_axis_x=0.0, relative_rotation_axis_z=0.0, vertical_translation=0.0):
    """ Unified instruction for playing cutscenes. You can specify a player (defaults to self), control whether the
    cutscene is skippable (False by default) or fades out (False by default), and add extra warp arguments or
    rotation arguments. (You can't supply both warp and rotation arguments.)

    The warp arguments require both a Map and a Region.

    The 'relative_rotation_axis_x' and 'relative_rotation_axis_z' arguments let you set where the (vertical) rotation
    axis is, relative to the player's current position.
    """
    if skippable:
        cutscene_type = p.CutsceneType.skippable_with_fade_out if fade_out else p.CutsceneType.skippable
    else:
        cutscene_type = p.CutsceneType.unskippable_with_fade_out if fade_out else p.CutsceneType.unskippable

    if warp_to_map or warp_to_region:
        if not (warp_to_map and warp_to_region):
            raise ValueError("You must set both 'warp_to_map' and 'warp_to_region' for cutscene warps.")
        if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
            raise ValueError("You cannot use warp arguments *and* rotation/translation arguments for cutscenes.")
        if player_id is None:
            return p.cutscene.play_cutscene_and_warp_player(
                cutscene_id, cutscene_type, warp_to_region, warp_to_map.block_id, warp_to_map.sub_id)
        return p.cutscene.play_cutscene_and_warp_specific_player(
            cutscene_id, cutscene_type, warp_to_region, warp_to_map.block_id, warp_to_map.sub_id, player_id)

    if player_id is None:
        player_id = 10000

    if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
        return p.cutscene.play_cutscene_and_rotate_player(
            cutscene_id, cutscene_type, relative_rotation_axis_x, relative_rotation_axis_z, rotation,
            vertical_translation, player_id)

    return p.cutscene.play_cutscene_to_player(cutscene_id, cutscene_type, player_id)


# NAVIMESH

def EnableNavimeshType(navimesh_id, navimesh_type: p.NavimeshType):
    """ Mark a given navimesh with the given type, which affects how character AI will interact with it. The navimesh
    ID is set in the MSB. """
    return p.navimesh.modify_navimesh_collision_bitflags(navimesh_id, navimesh_type, 0)


def DisableNavimeshType(navimesh_id, navimesh_type: p.NavimeshType):
    """ Remove the given type from the given navimesh. The navimesh ID is set in the MSB. """
    return p.navimesh.modify_navimesh_collision_bitflags(navimesh_id, navimesh_type, 1)


def ToggleNavimeshType(navimesh_id, navimesh_type: p.NavimeshType):
    """ Set the given navimesh type to the opposite of whatever it currently is for the given navimesh. """
    return p.navimesh.modify_navimesh_collision_bitflags(navimesh_id, navimesh_type, 2)


# NETWORK

def EnableNetworkSync():
    return p.network.set_sync(1)


def DisableNetworkSync():
    return p.network.set_sync(0)


def IssuePrefetchRequest(request_id):
    """ No idea what this does. """
    return p.network.issue_prefetch_request(request_id)


def SaveRequest():
    """ The game saves often, but sometimes you need to save immediately, often after changing a spawn point, for
    example. (Sneaky logic will often save the game before the player realizes what's happened.) """
    return p.network.save_request()


def TriggerMultiplayerEvent(event_id):
    """ Used to make the Bell of Awakening sounds, for example. """
    return p.network.trigger_multiplayer_event(event_id)


def EnableVagrantSpawning():
    """ Allows Vagrants to spawn at all. """
    return p.network.set_vagrant_spawning(0)


def DisableVagrantSpawning():
    """ Prevents Vagrants from spawning at all. """
    return p.network.set_vagrant_spawning(1)


def IncrementPvPSin():
    """ Not recommended. """
    return p.network.increment_player_pvp_sin()


def NotifyBossBattleStart():
    """ Sends the message to all summons that the host has challenged the boss. """
    return p.network.notify_boss_room_entry()


# SPAWNER

def EnableSpawner(entity: MapEntity):
    return p.spawner.set_spawner_state(entity, 1)


def DisableSpawner(entity: MapEntity):
    return p.spawner.set_spawner_state(entity, 0)


def ShootProjectile(owner_entity: MapEntity, projectile_id, model_point, behavior_id,
                    launch_angle_x=0.0, launch_angle_y=0.0, launch_angle_z=0.0):
    """ The owner entity sets the 'team' of the projectile (i.e. who it can hurt). """
    return p.spawner.shoot_projectile(owner_entity, projectile_id, model_point, behavior_id,
                                      launch_angle_x, launch_angle_y, launch_angle_z)


def CreateSpawner(entity: MapEntityInt):
    """ A 'bullet owner' that will spawn things according to the Spawner section of the MSB. """
    return p.spawner.create_spawner(entity)


# WARP

def WarpToMap(game_map: Map, player_entity_id=-1):
    """ Warp the main player to the given Player entity ID, which is in the Players tab of the MSB, in some map. By
    default, this warps to the 'default position' in the map (-1). """
    return p.warp.warp_player(game_map.block_id, game_map.sub_id, player_entity_id)


def MoveRemains(source_region: RegionInt, destination_region: Region):
    """ Move all bloodstains and dropped items from one region to another (I assume). """
    return p.warp.move_dropped_items_and_bloodstains(source_region, destination_region)


def WarpToEntity(character: CharacterInt, destination: MapEntityInt, model_point,
                 copy_draw_hitbox=None, set_draw_hitbox=None, short_warp=False, destination_type=None):
    """ Unified instruction for warping to some entity in the same map. Not sure what sort of optimizations 'short'
    makes, but it's used at various times by the game. You can change the owner hitbox of the warped character, which
    changes when it will be drawn. """
    if destination_type is None:
        try:
            destination_type = destination.category
        except AttributeError:
            raise AttributeError("Warp destination has no category. Use 'destination_type' keyword or a "
                                 "typed destination.")
    if copy_draw_hitbox and set_draw_hitbox:
        raise ValueError("You cannot copy and set the draw hitbox at the same time.")
    if short_warp:
        if copy_draw_hitbox or set_draw_hitbox:
            raise ValueError("You cannot copy or set the draw hitbox during a short warp.")
        return p.warp.short_warp(character, destination_type, destination, model_point)
    if copy_draw_hitbox:
        return p.warp.warp_and_copy_floor(character, destination_type, destination, model_point, copy_draw_hitbox)
    if set_draw_hitbox:
        return p.warp.warp_and_set_floor(character, destination_type, destination, model_point, set_draw_hitbox)
    return p.warp.warp(character, destination_type, destination, model_point)


def WarpObjectToCharacter(obj: ObjectInt, character: CharacterInt, model_point):
    return p.warp.warp_object_to_character(obj, character, model_point)


def SetRespawnPoint(respawn_point_id):
    """ Respawn point is an event set in the MSB. """
    return p.warp.set_player_respawn_point(respawn_point_id)


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
    return p.boss.kill_boss(game_area_param_id)


def IncrementNewGameCycle():
    return p.game.increment_new_game_plus_counter()


def AwardAchievement(achievement_id):
    """ For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing events. This interacts with Steam, which is always dangerous. """
    return p.game.award_achievement(achievement_id)


def BetrayCurrentCovenant():
    """ You'll obviously want to make sure you know what covenant the player has when using this. """
    return p.game.betray_current_covenant()


def EqualRecovery():
    """ Unknown. HotPocketRemix speculates it may trigger a garbage collection. I'm not sure when it's used. """
    return p.game.equal_recovery()


def SetLockedCameraSlot(game_map: Map, locked_camera_slot):
    """ This isn't used very often; standard camera control is done with camera params in the MSB. """
    return p.game.set_locked_camera_slot_number(game_map.block_id, game_map.sub_id, locked_camera_slot)


def HellkiteBreathControl(character, obj, animation_id):
    """ I don't recommend you mess with this. """
    return p.game.hellkite_breath_control(character, obj, animation_id)


def SetMapDrawParamSlot(map_block_id, slot):
    """ Each map block (NOT each map) can have two sets of DrawParams (0 and 1), and this can be used to switch
    between them. Originally only used for Dark Anor Londo. Note that """
    if isinstance(map_block_id, Map):
        raise ValueError("DrawParams can only be set for a whole map *block* (e.g. block 15 for Sen's Fortress and "
                         "Anor Londo). I'm making you set the block ID so you don't forget this.")
    return p.light.set_area_texture_parambank_slot_index(map_block_id, slot)


# CONTROL FLOW (LOW LEVEL)

# You can use Python 'if/else' blocks, the Await() instruction, and Condition() assignments for high-level event
# control flow, but in the interest of ensuring line-for-line correspondence with the EMEVD instruction table (and to
# allow 'decompiling'), the low-level control flow instructions are here as well.


# BASIC

def SkipLines(line_count):
    return p.skip(line_count)


def End():
    return p.end()


def Restart():
    return p.restart()


# CONDITIONS

def SkipLinesIfConditionTrue(line_count, condition):
    # TODO: Make sure you can pass condition as a name OR integer at front end (i.e. instruction args should check
    #  for condition name, not just condition/test args).
    return p.skip_if_condition_true(line_count, condition)


def SkipLinesIfFinishedConditionTrue(line_count, condition):
    return p.skip_if_condition_true_finished(line_count, condition)


def SkipLinesIfConditionFalse(line_count, condition):
    return p.skip_if_condition_false(line_count, condition)


def SkipLinesIfFinishedConditionFalse(line_count, finished_condition):
    return p.skip_if_condition_false_finished(line_count, finished_condition)


def EndIfConditionTrue(input_condition):
    return p.end_if_condition_true(input_condition)


def EndIfFinishedConditionTrue(finished_input_condition):
    return p.end_if_condition_true_finished(finished_input_condition)


def EndIfConditionFalse(input_condition):
    return p.end_if_condition_false(input_condition)


def EndIfFinishedConditionFalse(finished_input_condition):
    return p.end_if_condition_false_finished(finished_input_condition)


def RestartIfConditionTrue(input_condition):
    return p.restart_if_condition_true(input_condition)


def RestartIfFinishedConditionTrue(finished_input_condition):
    return p.restart_if_condition_true_finished(finished_input_condition)


def RestartIfConditionFalse(input_condition):
    return p.restart_if_condition_false(input_condition)


def RestartIfFinishedConditionFalse(finished_input_condition):
    return p.restart_if_condition_false_finished(finished_input_condition)


def IfConditionTrue(output_condition, input_condition):
    return p.if_condition_true(output_condition, input_condition)


def IfConditionFalse(output_condition, input_condition):
    return p.if_condition_false(output_condition, input_condition)


# TIME

def IfTimeElapsed(output_condition, seconds):
    """ Time since event started. """
    return p.if_time_elapsed(output_condition, seconds)


def IfFramesElapsed(output_condition, frames):
    """ Frames since event started. """
    return p.if_frames_elapsed(output_condition, frames)


# MAP

def SkipLinesIfInsideMap(line_count, game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.skip_if_inside_area(line_count, block_id, sub_id)


def SkipLinesIfOutsideMap(line_count, game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.skip_if_outside_area(line_count, block_id, sub_id)


def EndIfInsideMap(game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.end_if_inside_map(block_id, sub_id)


def EndIfOutsideMap(game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.end_if_outside_map(block_id, sub_id)


def RestartIfInsideMap(game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.restart_if_inside_map(block_id, sub_id)


def RestartIfOutsideMap(game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.restart_if_outside_map(block_id, sub_id)


def IfInsideMap(output_condition, game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.if_in_world_area(output_condition, block_id, sub_id)


def IfOutsideMap(output_condition, game_map: Map, sub_id=None):
    block_id, sub_id = _resolve_game_map(game_map, sub_id)
    return p.if_not_in_world_area(output_condition, block_id, sub_id)


# MULTIPLAYER

def SkipLinesIfHost(line_count):
    return p.skip_if_host(line_count)


def SkipLinesIfClient(line_count):
    return p.skip_if_client(line_count)


def SkipLinesIfSinglePlayer(line_count):
    return p.skip_if_singleplayer(line_count)


def SkipLinesIfMultiplayer(line_count):
    return p.skip_if_multiplayer(line_count)


def EndIfHost():
    return p.end_if_host()


def EndIfClient():
    return p.end_if_client()


def EndIfSinglePlayer():
    return p.end_if_singleplayer()


def EndIfMultiplayer():
    return p.end_if_multiplayer()


def RestartIfHost():
    return p.restart_if_host()


def RestartIfClient():
    return p.restart_if_client()


def RestartIfSinglePlayer():
    return p.restart_if_singleplayer()


def RestartIfMultiplayer():
    return p.restart_if_multiplayer()


def IfHost(condition: int):
    return p.if_host(condition)


def IfClient(condition: int):
    return p.if_client(condition)


def IfSinglePlayer(condition: int):
    return p.if_singleplayer(condition)


def IfMultiplayer(condition: int):
    return p.if_multiplayer(condition)


def IfMultiplayerEvent(condition: int, event_id: FlagInt):
    return p.if_multiplayer_event(condition, event_id)


# FLAGS

def SkipLinesIfThisEventOn(line_count):
    return p.skip_if_this_event_on(line_count)


def SkipLinesIfThisEventOff(line_count):
    return p.skip_if_this_event_off(line_count)


def SkipLinesIfThisEventSlotOn(line_count):
    return p.skip_if_this_event_slot_on(line_count)


def SkipLinesIfThisEventSlotOff(line_count):
    return p.skip_if_this_event_slot_off(line_count)


def SkipLinesIfFlagOn(line_count, flag: FlagInt):
    return p.skip_if_event_flag_on(line_count, flag)


def SkipLinesIfFlagOff(line_count, flag: FlagInt):
    return p.skip_if_event_flag_off(line_count, flag)


def SkipLinesIfFlagRangeAllOn(line_count, flag_range: Union[FlagRange, FlagInt], last_flag: Optional[FlagInt] = None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.skip_if_event_flag_range_all_on(line_count, first_flag, last_flag)


def SkipLinesIfFlagRangeAllOff(line_count, flag_range: Union[FlagRange, FlagInt], last_flag: Optional[FlagInt] = None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.skip_if_event_flag_range_all_off(line_count, first_flag, last_flag)


def SkipLinesIfFlagRangeAnyOn(line_count, flag_range: Union[FlagRange, FlagInt], last_flag: Optional[FlagInt] = None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.skip_if_event_flag_range_not_all_off(line_count, first_flag, last_flag)


def SkipLinesIfFlagRangeAnyOff(line_count, flag_range: Union[FlagRange, FlagInt], last_flag: Optional[FlagInt] = None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.skip_if_event_flag_range_not_all_on(line_count, first_flag, last_flag)


def EndIfThisEventOn():
    return p.end_if_this_event_on()


def EndIfThisEventOff():
    return p.end_if_this_event_off()


def EndIfThisEventSlotOn():
    return p.end_if_this_event_slot_on()


def EndIfThisEventSlotOff():
    return p.end_if_this_event_slot_off()


def EndIfFlagOn(flag: FlagInt):
    return p.end_if_event_flag_on(flag)


def EndIfFlagOff(flag: FlagInt):
    return p.end_if_event_flag_off(flag)


def EndIfFlagRangeAllOn(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.end_if_event_flag_range_all_on(first_flag, last_flag)


def EndIfFlagRangeAllOff(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.end_if_event_flag_range_all_off(first_flag, last_flag)


def EndIfFlagRangeAnyOn(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.end_if_event_flag_range_not_all_off(first_flag, last_flag)


def EndIfFlagRangeAnyOff(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.end_if_event_flag_range_not_all_on(first_flag, last_flag)


def RestartIfThisEventOn():
    return p.restart_if_this_event_on()


def RestartIfThisEventOff():
    return p.restart_if_this_event_off()


def RestartIfThisEventSlotOn():
    return p.restart_if_this_event_slot_on()


def RestartIfThisEventSlotOff():
    return p.restart_if_this_event_slot_off()


def RestartIfFlagOn(flag: FlagInt):
    return p.restart_if_event_flag_on(flag)


def RestartIfFlagOff(flag: FlagInt):
    return p.restart_if_event_flag_off(flag)


def RestartIfFlagRangeAllOn(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.restart_if_event_flag_range_all_on(first_flag, last_flag)


def RestartIfFlagRangeAllOff(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.restart_if_event_flag_range_all_off(first_flag, last_flag)


def RestartIfFlagRangeAnyOn(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.restart_if_event_flag_range_not_all_off(first_flag, last_flag)


def RestartIfFlagRangeAnyOff(flag_range: FlagRange, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.restart_if_event_flag_range_not_all_on(first_flag, last_flag)


def IfFlagOn(condition: int, flag: FlagInt):
    return p.if_event_flag_on(condition, flag)


def IfFlagOff(condition: int, flag: FlagInt):
    return p.if_event_flag_off(condition, flag)


def IfFlagState(condition: int, flag: FlagInt, state):
    return p.if_event_flag_state(condition, state, 0, flag)


def IfThisEventOn(condition: int):
    return p.if_this_event_on(condition)


def IfThisEventOff(condition: int):
    return p.if_this_event_off(condition)


def IfThisEventState(condition: int, state):
    return p.if_event_flag_state(condition, state, 1, 0)


def IfThisEventSlotOn(condition: int):
    return p.if_this_event_slot_on(condition)


def IfThisEventSlotOff(condition: int):
    return p.if_this_event_slot_off(condition)


def IfThisEventSlotState(condition: int, state):
    return p.if_event_flag_state(condition, state, 2, 0)


def IfTrueFlagCountEqual(condition: int, value: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_number_true_flags_in_range_equal(condition, first_flag, last_flag, value)


def IfTrueFlagCountNotEqual(condition: int, value: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_number_true_flags_in_range_not_equal(condition, first_flag, last_flag, value)


def IfTrueFlagCountGreaterThan(condition: int, value: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_number_true_flags_in_range_greater_than(condition, first_flag, last_flag, value)


def IfTrueFlagCountLessThan(condition: int, value: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_number_true_flags_in_range_less_than(condition, first_flag, last_flag, value)


def IfTrueFlagCountGreaterThanOrEqual(condition: int, value: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_number_true_flags_in_range_greater_than_or_equal(condition, first_flag, last_flag, value)


def IfTrueFlagCountLessThanOrEqual(condition: int, value: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_number_true_flags_in_range_less_than_or_equal(condition, first_flag, last_flag, value)


def IfFlagRangeAnyOn(condition: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_event_flag_range_not_all_off(condition, first_flag, last_flag)


def IfFlagRangeAnyOff(condition: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_event_flag_range_not_all_on(condition, first_flag, last_flag)


def IfFlagRangeAllOn(condition: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_event_flag_range_all_on(condition, first_flag, last_flag)


def IfFlagRangeAllOff(condition: int, flag_range, last_flag=None):
    first_flag, last_flag = _resolve_flag_range(flag_range, last_flag)
    return p.if_event_flag_range_all_off(condition, first_flag, last_flag)


def IfEventValueComparison(condition: int, flag: FlagInt, bit_count, comparison_type_enum, value):
    return p.if_event_value_comparison(condition, flag, bit_count, comparison_type_enum, value)


def IfEventValueEqual(condition: int, flag: FlagInt, bit_count, value):
    return p.if_event_value_equal(condition, flag, bit_count, value)


def IfEventValueGreaterThan(condition: int, flag: FlagInt, bit_count, value):
    return p.if_event_value_greater_than(condition, flag, bit_count, value)


def IfEventComparison(condition: int, left_flag: FlagInt, left_bit_count: int, comparison_type_enum,
                      right_flag: FlagInt, right_bit_count: int):
    return p.if_event_flag_value_comparison(condition, left_flag, left_bit_count, comparison_type_enum,
                                            right_flag, right_bit_count)


# REGIONS / DISTANCE

def IfEntityInsideRegion(condition: int, entity: MapEntityInt, region: RegionInt):
    return p.if_entity_inside_region(condition, entity, region)


def IfEntityOutsideRegion(condition: int, entity: MapEntityInt, region: RegionInt):
    return p.if_entity_outside_region(condition, entity, region)


def IfPlayerInsideRegion(condition: int, region: RegionInt):
    return p.if_entity_inside_region(condition, 10000, region)


def IfPlayerOutsideRegion(condition: int, region: RegionInt):
    return p.if_entity_outside_region(condition, 10000, region)


def IfEntityWithinDistance(condition: int, entity: MapEntityInt, other_entity: MapEntityInt,
                           radius: Union[int, float]):
    return p.if_entity_within_distance(condition, entity, other_entity, radius)


def IfEntityBeyondDistance(condition: int, entity: MapEntityInt, other_entity: MapEntityInt,
                           radius: Union[int, float]):
    return p.if_entity_beyond_distance(condition, entity, other_entity, radius)


def IfPlayerWithinDistance(condition: int, other_entity: MapEntityInt, radius: Union[int, float]):
    return p.if_entity_within_distance(condition, 10000, other_entity, radius)


def IfPlayerBeyondDistance(condition: int, other_entity: MapEntityInt, radius: Union[int, float]):
    return p.if_entity_beyond_distance(condition, 10000, other_entity, radius)


def IfAllPlayersInsideRegion(condition: int, region: RegionInt):
    return p.if_all_players_inside_region(condition, region)


def IfAllPlayersOutsideRegion(condition: int, region: RegionInt):
    return p.if_all_players_outside_region(condition, region)


# ITEMS

def IfPlayerOwnsItem(condition: int, item: Union[Item, int], item_type=None, including_box=True):
    if item_type is None:
        try:
            item_type = item.get_type()
        except AttributeError:
            raise AttributeError("Item type not detected. Use keyword or typed item.")
    if including_box:
        return p.if_player_owns_item(condition, item_type, item)
    else:
        return p.if_player_has_item(condition, item_type, item)


def IfPlayerOwnsWeapon(condition: int, weapon: Union[Weapon, int], including_box=True):
    if including_box:
        return p.if_player_owns_weapon(condition, weapon)
    return p.if_player_has_weapon(condition, weapon)


def IfPlayerOwnsArmor(condition: int, armor: Union[Armor, int], including_box=True):
    if including_box:
        return p.if_player_owns_armor(condition, armor)
    return p.if_player_has_armor(condition, armor)


def IfPlayerOwnsRing(condition: int, ring: Union[Ring, int], including_box=True):
    if including_box:
        return p.if_player_owns_ring(condition, ring)
    return p.if_player_has_ring(condition, ring)


def IfPlayerOwnsGood(condition: int, good: Union[Good, int], including_box=True):
    if including_box:
        return p.if_player_owns_good(condition, good)
    return p.if_player_has_good(condition, good)


def IfPlayerDoesNotOwnItem(condition: int, item: Union[Item, int], item_type=None, including_box=True):
    if item_type is None:
        try:
            item_type = item.get_type()
        except AttributeError:
            raise AttributeError("Item type not detected. Use keyword or typed item.")
    if including_box:
        return p.if_player_does_not_own_item(condition, item_type, item)
    return p.if_player_does_not_have_item(condition, item_type, item)


def IfPlayerDoesNotOwnWeapon(condition: int, weapon: Union[Weapon, int], including_box=True):
    if including_box:
        return p.if_player_does_not_own_weapon(condition, weapon)
    return p.if_player_does_not_have_weapon(condition, weapon)


def IfPlayerDoesNotOwnArmor(condition: int, armor: Union[Armor, int], including_box=True):
    if including_box:
        return p.if_player_does_not_own_armor(condition, armor)
    return p.if_player_does_not_have_armor(condition, armor)


def IfPlayerDoesNotOwnRing(condition: int, ring: Union[Ring, int], including_box=True):
    if including_box:
        return p.if_player_does_not_own_ring(condition, ring)
    return p.if_player_does_not_have_ring(condition, ring)


def IfPlayerDoesNotOwnGood(condition: int, good: Union[Good, int], including_box=True):
    if including_box:
        return p.if_player_does_not_own_good(condition, good)
    return p.if_player_does_not_have_good(condition, good)


def IfAnyItemDroppedInRegion(condition: int, region: RegionInt):
    return p.if_any_item_dropped_in_region(condition, region)


def IfItemDropped(condition: int, item: Union[Item, int], item_type=None):
    if item_type is None:
        try:
            item_type = item.get_type()
        except AttributeError:
            raise AttributeError("Item type not detected. Use keyword or typed item.")
    return p.if_item_dropped(condition, item_type, item)


# OBJECTS

def SkipLinesIfObjectDestroyed(line_count, obj: ObjectInt):
    return p.skip_if_object_destroyed(line_count, obj)


def SkipLinesIfObjectNotDestroyed(line_count, obj: ObjectInt):
    return p.skip_if_object_not_destroyed(line_count, obj)


def EndIfObjectDestroyed(obj: ObjectInt):
    return p.end_if_object_destroyed(obj)


def EndIfObjectNotDestroyed(obj: ObjectInt):
    return p.end_if_object_not_destroyed(obj)


def RestartIfObjectDestroyed(obj: ObjectInt):
    return p.restart_if_object_destroyed(obj)


def RestartIfObjectNotDestroyed(obj: ObjectInt):
    return p.restart_if_object_not_destroyed(obj)


def IfObjectDestroyed(condition: int, obj: ObjectInt):
    return p.if_object_destroyed(condition, obj)


def IfObjectNotDestroyed(condition: int, obj: ObjectInt):
    return p.if_object_not_destroyed(condition, obj)


def IfObjectDamagedBy(condition: int, obj: ObjectInt, attacker: CharacterInt):
    return p.if_object_damaged_by(condition, obj, attacker)


def IfObjectActivated(condition: int, objact_id: int):
    return p.if_object_activated(condition, objact_id)


# HITBOX

def IfMovingOnHitbox(condition: int, hitbox_id: Union[Hitbox, int]):
    return p.if_player_moving_on_hitbox(condition, hitbox_id)


def IfRunningOnHitbox(condition: int, hitbox_id: Union[Hitbox, int]):
    return p.if_player_running_on_hitbox(condition, hitbox_id)


def IfStandingOnHitbox(condition: int, hitbox_id: Union[Hitbox, int]):
    return p.if_player_standing_on_hitbox(condition, hitbox_id)


# VALUE COMPARISONS

def SkipLinesIfEqual(line_count, left_value, right_value):
    return p.skip_if_equal(line_count, left_value, right_value)


def SkipLinesIfNotEqual(line_count, left_value, right_value):
    return p.skip_if_not_equal(line_count, left_value, right_value)


def SkipLinesIfGreaterThan(line_count, left_value, right_value):
    return p.skip_if_greater_than(line_count, left_value, right_value)


def SkipLinesIfGreaterThanOrEqual(line_count, left_value, right_value):
    return p.skip_if_greater_than_or_equal(line_count, left_value, right_value)


def SkipLinesIfLessThan(line_count, left_value, right_value):
    return p.skip_if_less_than(line_count, left_value, right_value)


def SkipLinesIfLessThanOrEqual(line_count, left_value, right_value):
    return p.skip_if_less_than_or_equal(line_count, left_value, right_value)


def EndIfEqual(left_value, right_value):
    return p.end_if_equal(left_value, right_value)


def EndIfNotEqual(left_value, right_value):
    return p.end_if_not_equal(left_value, right_value)


def EndIfGreaterThan(left_value, right_value):
    return p.end_if_greater_than(left_value, right_value)


def EndIfGreaterThanOrEqual(left_value, right_value):
    return p.end_if_greater_than_or_equal(left_value, right_value)


def EndIfLessThan(left_value, right_value):
    return p.end_if_less_than(left_value, right_value)


def EndIfLessThanOrEqual(left_value, right_value):
    return p.end_if_less_than_or_equal(left_value, right_value)


def RestartIfEqual(left_value, right_value):
    return p.restart_if_equal(left_value, right_value)


def RestartIfNotEqual(left_value, right_value):
    return p.restart_if_not_equal(left_value, right_value)


def RestartIfGreaterThan(left_value, right_value):
    return p.restart_if_greater_than(left_value, right_value)


def RestartIfGreaterThanOrEqual(left_value, right_value):
    return p.restart_if_greater_than_or_equal(left_value, right_value)


def RestartIfLessThan(left_value, right_value):
    return p.restart_if_less_than(left_value, right_value)


def RestartIfLessThanOrEqual(left_value, right_value):
    return p.restart_if_less_than_or_equal(left_value, right_value)


# ACTION PROMPT

def IfDialogPromptActivated(condition: int, prompt_text: TextInt, anchor_entity: MapEntityInt,
                            facing_angle=None, max_distance=None, model_point=-1, human_or_hollow_only=True, button=0,
                            boss_version=False, line_intersects=None, anchor_type=None):
    if anchor_type is None:
        try:
            anchor_type = anchor_entity.category
        except AttributeError:
            raise ValueError("Anchor entity must be an Object, Region, or Character instance, or 'anchor_type' keyword "
                             "must be given.")

    if human_or_hollow_only:
        reaction_attribute = ReactionAttribute.human_or_hollow
    else:
        reaction_attribute = ReactionAttribute.all

    if facing_angle is None:
        if anchor_type != Category.region:
            raise ValueError("Facing angle must be greater than zero for Object and Character targets.")
        else:
            facing_angle = 0.0

    if max_distance is None:
        if anchor_type != Category.region:
            raise ValueError("Max distance must be greater than zero for Object and Character targets.")
        else:
            max_distance = 0.0

    args = [condition, anchor_type, anchor_entity, facing_angle, model_point, max_distance,
            prompt_text, reaction_attribute, button]

    if boss_version:
        if line_intersects is None:
            return p.if_action_button_state_in_boss(*args)
        else:
            return p.if_action_button_state_and_line_segment_in_boss(*args, line_intersects)
    else:
        if line_intersects is None:
            return p.if_action_button_state(*args)
        else:
            return p.if_action_button_state_and_line_segment(*args, line_intersects)


# WORLD TENDENCY

def IfWhiteWorldTendencyComparison(condition: int, comparison_type_enum, value):
    return p.if_world_tendency_comparison(condition, TendencyType.white, comparison_type_enum, value)


def IfBlackWorldTendencyComparison(condition: int, comparison_type_enum, value):
    return p.if_world_tendency_comparison(condition, TendencyType.black, comparison_type_enum, value)


def IfWhiteWorldTendencyGreaterThanOrEqual(condition: int, value):
    return p.if_world_tendency_greater_than_or_equal(condition, TendencyType.white, value)


def IfBlackWorldTendencyGreaterThanOrEqual(condition: int, value):
    return p.if_world_tendency_greater_than_or_equal(condition, TendencyType.Black, value)


# NEW GAME CYCLE

def IfNewGameCycleComparison(condition: int, comparison_type_enum, completion_count):
    return p.if_new_game_count_comparison(condition, comparison_type_enum, completion_count)


def IfNewGameCycleEqual(condition: int, completion_count):
    return p.if_new_game_count_equal(condition, completion_count)


def IfNewGameCycleGreaterThanOrEqual(condition: int, completion_count):
    return p.if_new_game_count_greater_than_or_equal(condition, completion_count)


# SYSTEM

def IfDLCOwned(condition: int):
    return p.if_owns_dlc(condition)


def IfDLCNotOwned(condition: int):
    return p.if_does_not_own_dlc(condition)


def IfOnline(condition: int):
    return p.if_online(condition)


def IfOffline(condition: int):
    return p.if_offline(condition)


# CHARACTER

def IfDead(condition: int, character: CharacterInt):
    return p.if_entity_dead(condition, character)


def IfAlive(condition: int, character: CharacterInt):
    return p.if_entity_alive(condition, character)


def IfAttacked(condition: int, attacked_character: CharacterInt, attacking_character: CharacterInt):
    return p.if_entity_attacked_by(condition, attacked_character, attacking_character)


def IfHealthEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_equal(condition, character, value)


def IfHealthNotEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_not_equal(condition, character, value)


def IfHealthGreaterThan(condition: int, character: CharacterInt, value):
    return p.if_entity_health_greater_than(condition, character, value)


def IfHealthLessThan(condition: int, character: CharacterInt, value):
    return p.if_entity_health_less_than(condition, character, value)


def IfHealthGreaterThanOrEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_greater_than_or_equal(condition, character, value)


def IfHealthLessThanOrEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_less_than_or_equal(condition, character, value)


def IfCharacterType(condition: int, character: CharacterInt, character_type: Union[CharacterType, int]):
    return p.if_character_type(condition, character, character_type)


def IfCharacterHollow(condition: int, character: CharacterInt):
    return p.if_character_hollow(condition, character)


def IfCharacterHuman(condition: int, character: CharacterInt):
    return p.if_character_human(condition, character)


def IfCharacterTargeting(condition: int, targeting_character: CharacterInt,
                         targeted_character: CharacterInt, ):
    return p.if_entity_targeting(condition, targeting_character, targeted_character)


def IfCharacterNotTargeting(condition: int, targeting_character: CharacterInt,
                            targeted_character: CharacterInt):
    return p.if_entity_not_targeting(condition, targeting_character, targeted_character)


def IfCharacterHasSpecialEffect(condition: int, character: CharacterInt, special_effect):
    return p.if_entity_has_special_effect(condition, character, special_effect)


def IfCharacterDoesNotHaveSpecialEffect(condition: int, character: CharacterInt, special_effect):
    return p.if_entity_does_not_have_special_effect(condition, character, special_effect)


def IfPlayerHasSpecialEffect(condition: int, special_effect):
    return p.if_player_has_special_effect(condition, special_effect)


def IfPlayerDoesNotHaveSpecialEffect(condition: int, special_effect):
    return p.if_player_does_not_have_special_effect(condition, special_effect)


def IfCharacterPartHealthComparison(condition: int, character: CharacterInt, npc_part_type,
                                    comparison_type_enum, value):
    return p.if_body_part_health_comparison(condition, character, npc_part_type, comparison_type_enum, value)


def IfCharacterPartHealthLessThanOrEqual(condition: int, character: CharacterInt, npc_part_type, value):
    return p.if_body_part_health_less_than_or_equal(condition, character, npc_part_type, value)


def IfBackreadEnabled(condition: int, character: CharacterInt):
    return p.if_entity_backread_enabled(condition, character)


def IfBackreadDisabled(condition: int, character: CharacterInt):
    return p.if_entity_backread_disabled(condition, character)


def IfHasTAEEvent(condition: int, character: CharacterInt, tae_event_id: int):
    return p.if_has_tae_event(condition, character, tae_event_id)


def IfDoesNotHaveTAEEvent(condition: int, character: CharacterInt, tae_event_id: int):
    return p.if_does_not_have_tae_event(condition, character, tae_event_id)


def IfHasAIStatus(condition: int, character: CharacterInt, ai_status: int):
    return p.if_ai_state(condition, character, ai_status)


def IfSkullLanternActive(condition: int):
    return p.if_skull_lantern_activated(condition)


def IfSkullLanternNotActive(condition: int):
    return p.if_skull_lantern_not_activated(condition)


def IfPlayerClass(condition: int, class_type=Union[ClassType, int]):
    return p.if_player_class(condition, class_type)


def IfPlayerCovenant(condition: int, covenant=Union[Covenant, int]):
    return p.if_player_covenant(condition, covenant)


def IfPlayerSoulLevelComparison(condition: int, comparison_type_enum, value):
    return p.if_player_soul_level_comparison(condition, comparison_type_enum, value)


def IfPlayerSoulLevelGreaterThanOrEqual(condition: int, value):
    return p.if_player_soul_level_greater_than_or_equal(condition, value)


def IfPlayerSoulLevelLessThanOrEqual(condition: int, value):
    return p.if_player_soul_level_less_than_or_equal(condition, value)


def IfHealthValueEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_value_equal(condition, character, value)


def IfHealthValueNotEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_value_not_equal(condition, character, value)


def IfHealthValueGreaterThan(condition: int, character: CharacterInt, value):
    return p.if_entity_health_value_greater_than(condition, character, value)


def IfHealthValueLessThan(condition: int, character: CharacterInt, value):
    return p.if_entity_health_value_less_than(condition, character, value)


def IfHealthValueGreaterThanOrEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_value_greater_than_or_equal(condition, character, value)


def IfHealthValueLessThanOrEqual(condition: int, character: CharacterInt, value):
    return p.if_entity_health_value_less_than_or_equal(condition, character, value)


# ARENA (DO NOT USE)

def ArenaRankingRequest1v1():
    return p.game.arena_1v1_request()


def ArenaRankingRequest2v2():
    return p.game.arena_2v2_request()


def ArenaRankingRequestFFA():
    return p.game.arena_FFA_request()


def ArenaExitRequest():
    return p.game.arena_exit_request()


def ArenaSetNametag1():
    return p.game.arena_set_nametag_1()


def ArenaSetNametag2():
    return p.game.arena_set_nametag_2()


def ArenaSetNametag3():
    return p.game.arena_set_nametag_3()


def ArenaSetNametag4():
    return p.game.arena_set_nametag_4()


def DisplayArenaDissolutionMessage(text_id: TextInt):
    return p.game.display_arena_dissolution_message(text_id)


# INTERNAL ONLY

def _resolve_game_map(game_map, sub_id):
    if sub_id is None:
        try:
            block_id = game_map.block_id
            sub_id = game_map.sub_id
        except AttributeError:
            raise TypeError("game_map argument must be a Map instance (or use block_id and sub_id).")
    else:
        block_id = game_map
    return block_id, sub_id


def _resolve_flag_range(flag_range, last_flag):
    if last_flag is None:
        try:
            first_flag = flag_range.first
            last_flag = flag_range.last
        except AttributeError:
            raise TypeError("flag_range argument must be a FlagRange instance (or use last_flag).")
    else:
        first_flag = flag_range
    return first_flag, last_flag

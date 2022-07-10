"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1045330000, obj=1045331950, unknown=5.0)
    RunCommonEvent(0, 9005910, args=(1045331940, 1045330101, 1045330103, 3), arg_types="IIIi")
    RunCommonEvent(0, 9005911, args=(1045331941,))
    RunCommonEvent(0, 9005912, args=(1045330100, 605053), arg_types="Ii")
    RunCommonEvent(0, 90005300, args=(1045330200, 1045330200, 45000000, 0.0, 0), arg_types="IIifi")
    Event_1045332220()
    Event_1045332250(0, flag=1045330200, flag_1=1045330201, flag_2=1045330202, flag_3=1045330205)
    Event_1045332251(0, flag=1045330200, attacked_entity=1045330200)
    Event_1045332251(1, flag=1045330201, attacked_entity=1045330201)
    Event_1045332251(2, flag=1045330202, attacked_entity=1045330202)
    Event_1045332252(0, flag=1045330200, character=1045330200)
    Event_1045332252(1, flag=1045330201, character=1045330201)
    Event_1045332252(2, flag=1045330202, character=1045330202)
    Event_1045332253()
    Event_1045332254()
    Event_1045332255()
    Event_1045332256()
    RunCommonEvent(0, 90005300, args=(1045330200, 1045330200, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1045330201, 1045330201, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1045330202, 1045330202, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005251, args=(1045330201, 0.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1045330900, 1045330900, 1045330400, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1045330210, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330211, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330212, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330213, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330214, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330215, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330216, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330217, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330218, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045330219, 1045332210, 15.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1045330900, 20.0, 0.0, 1700), arg_types="Iffi")
    Event_1045332265(0, vfx_id=1045332200)
    Event_1045332265(1, vfx_id=1045332201)
    Event_1045332265(2, vfx_id=1045332202)
    Event_1045332265(3, vfx_id=1045332203)
    Event_1045332265(4, vfx_id=1045332204)
    Event_1045332265(5, vfx_id=1045332205)
    Event_1045332265(6, vfx_id=1045332206)
    Event_1045332265(7, vfx_id=1045332207)
    Event_1045332265(8, vfx_id=1045332208)
    Event_1045332265(9, vfx_id=1045332209)
    Event_1045332265(10, vfx_id=1045332210)
    Event_1045332265(11, vfx_id=1045332211)
    Event_1045332265(12, vfx_id=1045332212)
    Event_1045332265(13, vfx_id=1045332213)
    Event_1045332265(14, vfx_id=1045332214)
    Event_1045332265(15, vfx_id=1045332215)
    Event_1045332265(16, 1045332216)


@RestartOnRest(1045332220)
def Event_1045332220():
    """Event 1045332220"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=1045330220, radius=30.0)
    IfConditionTrue(AND_1, input_condition=AND_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ForceAnimation(1045330220, 3011, unknown2=1.0)
    Wait(5.0)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1045332220, unk_8_12=1)
    End()


@RestartOnRest(1045332250)
def Event_1045332250(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 1045332250"""
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DeleteObjectVFX(1045331620)
    CreateObjectVFX(1045331620, vfx_id=200, model_point=1500)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagEnabled(AND_1, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_3)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    PlaySoundEffect(1045331620, 1500, sound_type=SoundType.s_SFX)
    DisableObject(1045331620)
    DeleteObjectVFX(1045331620)
    End()


@RestartOnRest(1045332251)
def Event_1045332251(_, flag: uint, attacked_entity: uint):
    """Event 1045332251"""
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(MAIN, attacked_entity=attacked_entity, attacker=PLAYER)
    DisableAnimations(attacked_entity)
    ForceAnimation(attacked_entity, 20008, unknown2=1.0)
    EnableFlag(flag)


@RestartOnRest(1045332252)
def Event_1045332252(_, flag: uint, character: uint):
    """Event 1045332252"""
    DisableCharacter(character)
    EndIfFlagEnabled(flag)
    SkipLinesIfPlayerInOwnWorld(1)
    EnableInvincibility(character)
    IfFlagEnabled(AND_1, 1045332621)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character)
    EnableImmortality(character)
    DisableHealthBar(character)


@RestartOnRest(1045332253)
def Event_1045332253():
    """Event 1045332253"""
    DisableNetworkSync()
    EndIfFlagEnabled(1045330205)
    IfActionButtonParamActivated(OR_1, action_button_id=9320, entity=1033401610)
    IfFlagEnabled(OR_1, 1045330205)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1045330205)
    DisplayDialog(text=20200, anchor_entity=1045331620)
    Wait(1.0)
    Restart()


@RestartOnRest(1045332254)
def Event_1045332254():
    """Event 1045332254"""
    DisableNetworkSync()
    IfActionButtonParamActivated(AND_1, action_button_id=9210, entity=1045331621)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=60011, anchor_entity=1045331621)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(1045332621)
    Wait(1.0)
    Restart()


@RestartOnRest(1045332255)
def Event_1045332255():
    """Event 1045332255"""
    RegisterLadder(start_climbing_flag=45330580, stop_climbing_flag=45330851, obj=1045331580)


@RestartOnRest(1045332256)
def Event_1045332256():
    """Event 1045332256"""
    EndIfFlagEnabled(1045330202)
    EndIfPlayerNotInOwnWorld()
    SetNetworkUpdateAuthority(PLAYER, authority_level=UpdateAuthority.Unknown8192)
    AddSpecialEffect(1045330202, 11434)
    Move(1045330202, destination=1045331202, destination_type=CoordEntityType.Region, short_move=True)
    IfAttackedWithDamageType(AND_1, attacked_entity=1045330202, attacker=PLAYER)
    SkipLinesIfConditionFalse(2, AND_1)
    Kill(1045330202)
    End()
    Wait(7.0)
    Restart()


@RestartOnRest(1045332260)
def Event_1045332260(_, vfx_id: uint, earliest_hour: uchar, earliest_minute: uchar, flag: uint):
    """Event 1045332260"""
    DeleteVFX(vfx_id, erase_root_only=False)
    DisableNetworkFlag(flag)
    EndIfFlagEnabled(1045330900)
    WaitUntilRandomTimeOfDay(earliest=(earliest_hour, earliest_minute, 0), latest=(1, 0, 0))
    EnableNetworkFlag(flag)
    CreateVFX(vfx_id)
    IfTimeOfDay(AND_1, earliest=(1, 0, 1), latest=(20, 59, 59))
    IfHasAIStatus(AND_1, 1045330900, ai_status=AIStatusType.Normal)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, 1045330900)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Restart()


@RestartOnRest(1045332265)
def Event_1045332265(_, vfx_id: uint):
    """Event 1045332265"""
    GotoIfFlagEnabled(Label.L0, flag=1045330900)
    IfCharacterDead(MAIN, 1045330900)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()


@RestartOnRest(1045332900)
def Event_1045332900():
    """Event 1045332900"""
    EndIfFlagEnabled(1045330900)
    WaitFrames(frames=1)
    RestartIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045332901)
    DisableCharacter(1045330900)
    DisableAnimations(1045330900)
    DeleteObjectVFX(1045331900)
    IfTimeOfDay(AND_1, earliest=(0, 0, 0), latest=(1, 0, 0))
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateObjectVFX(1045331900, vfx_id=100, model_point=806901)
    IfTimeOfDay(MAIN, earliest=(1, 0, 1), latest=(23, 59, 59))
    Restart()


@RestartOnRest(1045332920)
def Event_1045332920():
    """Event 1045332920"""
    EndIfFlagEnabled(1045330900)
    WaitFrames(frames=1)
    RestartIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_3)
    IfTimeOfDay(AND_3, earliest=(0, 0, 0), latest=(1, 0, 0))
    IfActionButtonParamActivated(AND_3, action_button_id=9250, entity=1045331901)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Wait(2.0)
    EnableFlag(1045332901)
    DeleteObjectVFX(1045331900)
    CreateTemporaryVFX(vfx_id=806910, anchor_entity=1045331900, anchor_type=CoordEntityType.Object)
    EnableCharacter(1045330900)
    EnableAnimations(1045330900)

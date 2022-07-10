"""
linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31220000, obj=31221950, unknown=5.0)
    Event_31222800()
    Event_31222810()
    Event_31222811()
    Event_31222812()
    Event_31222849()
    Event_31222813(0, character=31220800, flag=31222821)
    Event_31222813(1, character=31220802, flag=31222820)
    RunCommonEvent(0, 900005610, args=(31221200, 100, 800, 0), arg_types="IiiI")
    Event_31222500()
    RunCommonEvent(
        0,
        90005646,
        args=(31220800, 31222840, 31222841, 31221840, 31222840, 31, 22, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005250, args=(31220211, 31222304, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31220212, 31222304, 0.0, 0), arg_types="IIfi")
    Event_31222300()
    Event_31222306()
    Event_31222312()
    Event_31222305()
    Event_31222317()
    Event_31222301()
    Event_31222316()
    Event_31222303()
    Event_31222313()
    Event_31222304()
    Event_31222330()
    Event_31222340(0, 31220400, 31222304, 0.10000000149011612)
    Event_31222340(1, 31220402, 31222305, 0.10000000149011612)
    Event_31222340(2, 31220403, 31222306, 0.10000000149011612)


@RestartOnRest(31222300)
def Event_31222300():
    """Event 31222300"""
    IfThisEventSlotFlagEnabled(OR_5)
    EndIfConditionTrue(input_condition=OR_5)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31222300)
    IfCharacterHasSpecialEffect(AND_1, 31220300, 15007)
    IfCharacterDead(AND_1, 31220304)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableSpawner(entity=31223300)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222301)
def Event_31222301():
    """Event 31222301"""
    EndIfFlagEnabled(31222301)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31222301)
    IfCharacterHasSpecialEffect(AND_1, 31220302, 15007)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableSpawner(entity=31223301)
    EnableNetworkFlag(31222301)


@RestartOnRest(31222303)
def Event_31222303():
    """Event 31222303"""
    IfThisEventSlotFlagEnabled(OR_5)
    EndIfConditionTrue(input_condition=OR_5)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31222303)
    IfCharacterHasSpecialEffect(AND_1, 31220301, 15007)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_5)
    EnableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222304)
def Event_31222304():
    """Event 31222304"""
    IfThisEventSlotFlagEnabled(OR_5)
    EndIfConditionTrue(input_condition=OR_5)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31222302)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_5)
    ForceAnimation(31220303, 3002, wait_for_completion=True, unknown2=1.0)
    EnableSpawner(entity=31223302)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222305)
def Event_31222305():
    """Event 31222305"""
    IfThisEventSlotFlagEnabled(OR_5)
    EndIfConditionTrue(input_condition=OR_5)
    IfHasAIStatus(OR_1, 31220304, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_1, attacked_entity=31220304, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    ForceAnimation(31220304, 3002, wait_for_completion=True, unknown2=1.0)
    EnableSpawner(entity=31223304)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222306)
def Event_31222306():
    """Event 31222306"""
    IfThisEventSlotFlagEnabled(OR_5)
    EndIfConditionTrue(input_condition=OR_5)
    IfHasAIStatus(OR_1, 31220300, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_1, attacked_entity=31220300, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    ForceAnimation(31220300, 3002, wait_for_completion=True, unknown2=1.0)
    EnableSpawner(entity=31223305)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222311)
def Event_31222311():
    """Event 31222311"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfAttackedWithDamageType(OR_5, attacked_entity=31220300, attacker=0)
    IfCharacterDead(OR_5, 31220300)
    IfConditionTrue(MAIN, input_condition=OR_5)
    DisableSpawner(entity=31223300)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222312)
def Event_31222312():
    """Event 31222312"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterDead(MAIN, 31220300)
    Kill(31220201, award_souls=True)
    Kill(31220211, award_souls=True)
    Kill(31220204, award_souls=True)
    Kill(31220212, award_souls=True)
    Kill(31220228, award_souls=True)
    Kill(31220213, award_souls=True)
    Kill(31220403, award_souls=True)
    Kill(31220230, award_souls=True)
    DisableSpawner(entity=31223300)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222317)
def Event_31222317():
    """Event 31222317"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterDead(MAIN, 31220304)
    Kill(31220227, award_souls=True)
    Kill(31220226, award_souls=True)
    Kill(31220200, award_souls=True)
    Kill(31220221, award_souls=True)
    Kill(31220222, award_souls=True)
    Kill(31220402, award_souls=True)
    Kill(31220229, award_souls=True)
    DisableSpawner(entity=31223304)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222314)
def Event_31222314():
    """Event 31222314"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfAttackedWithDamageType(OR_5, attacked_entity=31220301, attacker=0)
    IfCharacterDead(OR_5, 31220301)
    IfConditionTrue(MAIN, input_condition=OR_5)
    DisableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222313)
def Event_31222313():
    """Event 31222313"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterDead(MAIN, 31220301)
    Kill(31220210, award_souls=True)
    Kill(31220202, award_souls=True)
    Kill(31220220, award_souls=True)
    DisableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222315)
def Event_31222315():
    """Event 31222315"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfAttackedWithDamageType(OR_5, attacked_entity=31220302, attacker=0)
    IfCharacterDead(OR_5, 31220302)
    IfConditionTrue(MAIN, input_condition=OR_5)
    DisableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222316)
def Event_31222316():
    """Event 31222316"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterDead(MAIN, 31220302)
    Kill(31220223, award_souls=True)
    Kill(31220224, award_souls=True)
    Kill(31220225, award_souls=True)
    DisableSpawner(entity=31223301)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222330)
def Event_31222330():
    """Event 31222330"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterDead(MAIN, 31220303)
    Kill(31220400, award_souls=True)
    DisableSpawner(entity=31223302)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222340)
def Event_31222340(_, entity: uint, flag: uint, seconds: float):
    """Event 31222340"""
    EndIfThisEventSlotFlagEnabled()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    Wait(seconds)
    ForceAnimation(entity, 60502, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222500)
def Event_31222500():
    """Event 31222500"""
    GotoIfFlagDisabled(Label.L0, flag=31220500)
    DisableObject(31221500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31222500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(31221500)
    EnableFlag(31220500)


@RestartOnRest(31222520)
def Event_31222520(_, flag: uint, flag_1: uint, obj: uint):
    """Event 31222520"""
    EndIfFlagEnabled(flag)
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)


@RestartOnRest(31222800)
def Event_31222800():
    """Event 31222800"""
    EndIfFlagEnabled(31220800)
    IfHealthValueLessThanOrEqual(MAIN, 31220800, value=0)
    Wait(4.0)
    PlaySoundEffect(31220800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31220800)
    KillBossAndDisplayBanner(character=31220800, banner_type=BannerType.DutyFulfilled)
    Kill(31220803)
    DisableCharacter(31220803)
    DisableAnimations(31220803)
    EnableFlag(31220800)
    EnableFlag(9248)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61248)


@RestartOnRest(31222810)
def Event_31222810():
    """Event 31222810"""
    GotoIfFlagDisabled(Label.L0, flag=31220800)
    DisableCharacter(31220801)
    DisableAnimations(31220801)
    Kill(31220801)
    DisableCharacter(31220800)
    DisableAnimations(31220800)
    Kill(31220800)
    DisableCharacter(31220802)
    DisableAnimations(31220802)
    Kill(31220802)
    DisableCharacter(31220803)
    DisableAnimations(31220803)
    Kill(31220803)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31220800)
    DisableAI(31220801)
    IfFlagEnabled(AND_1, 31222805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31222800)
    IfAttackedWithDamageType(OR_1, attacked_entity=31220800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableAnimations(31220801)
    SetNetworkUpdateRate(31220801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31220801, name=903560310)
    Wait(1.5)
    EnableAI(31220801)
    AddSpecialEffect(31220803, 297810)
    DisableAnimations(31220803)
    SetNetworkUpdateRate(31220803, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(31222811)
def Event_31222811():
    """Event 31222811"""
    EndIfFlagEnabled(31220800)
    IfCharacterDead(MAIN, 31220801)
    DisableBossHealthBar(31220801, name=903560310)
    EnableFlag(31222842)
    Wait(5.0)
    EnableSpawner(entity=31223307)
    Wait(0.10000000149011612)
    EnableNetworkFlag(31222820)
    EnableAI(31220802)
    EnableAnimations(31220802)
    SetNetworkUpdateRate(31220802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31220802, name=903570310)


@RestartOnRest(31222812)
def Event_31222812():
    """Event 31222812"""
    EndIfFlagEnabled(31220800)
    IfCharacterDead(MAIN, 31220802)
    DisableBossHealthBar(31220802, name=903570310)
    Wait(5.0)
    EnableSpawner(entity=31223308)
    Wait(0.10000000149011612)
    EnableNetworkFlag(31222821)
    EnableBossHealthBar(31220800, name=904140310)
    EnableAI(31220800)
    EnableAnimations(31220800)
    ForceAnimation(31220800, 3011, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(31220800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31220800, name=904140310)
    Wait(3.0)
    ForceAnimation(31220800, 1702, unknown2=1.0)
    AddSpecialEffect(31220800, 297811)


@RestartOnRest(31222813)
def Event_31222813(_, character: uint, flag: uint):
    """Event 31222813"""
    EndIfFlagEnabled(31220800)
    IfFlagEnabled(AND_1, flag)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(AND_2, input_condition=AND_1)
    IfLeavingSession(AND_3)
    IfConditionFalse(AND_2, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ActivateMultiplayerBuffs(character)
    Wait(3.0)
    IfCharacterHasSpecialEffect(OR_1, character, 7820)
    IfCharacterHasSpecialEffect(OR_1, character, 7821)
    IfCharacterHasSpecialEffect(OR_1, character, 7822)
    SkipLinesIfConditionTrue(1, OR_1)
    Restart()


@RestartOnRest(31222849)
def Event_31222849():
    """Event 31222849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31220800, 31221800, 31222800, 31222805, 31225800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31220800, 31221800, 31222800, 31222805, 31222806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31220800, 31221800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31220800, 356000, 31222805, 31222806, 0, 0, 0, 0), arg_types="IiIIIIii")

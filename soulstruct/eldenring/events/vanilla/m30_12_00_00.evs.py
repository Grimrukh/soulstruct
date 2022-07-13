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
    RegisterGrace(grace_flag=301200, obj=30121950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(30121150, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005201, args=(30120200, 30000, 20000, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(30120201, 30000, 20000, 30122201, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30120250, 30122250, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30120251, 30122250, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30120205, 30122205, 0.0, 3000), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30120208, 30122208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005271, args=(30120209, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(30120210, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(30120211, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(30120212, 0.0, -1), arg_types="Ifi")
    Event_30122300(0, character=30120213)
    Event_30122300(1, character=30120214)
    Event_30122300(2, character=30120215)
    Event_30122300(3, character=30120216)
    Event_30122300(4, character=30120217)
    Event_30122300(5, character=30120218)
    Event_30122300(6, character=30120219)
    Event_30122300(7, character=30120220)
    Event_30122300(8, character=30120221)
    Event_30122300(9, character=30120222)
    Event_30122300(10, character=30120223)
    Event_30122300(11, character=30120224)
    Event_30122502(0, 30120500, 0.0, -1)
    RunCommonEvent(0, 90005250, args=(30120500, 30122502, 0.0, 0), arg_types="IIfi")
    Event_30122500()
    Event_30122501()
    RunCommonEvent(0, 90005650, args=(30120540, 30121540, 30121541, 30123541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30120540, 30121540), arg_types="II")
    Event_30122800()
    Event_30122810()
    Event_30122849()
    Event_30122811()
    RunCommonEvent(
        0,
        90005646,
        args=(30120800, 30122840, 30122841, 30121840, 30122840, 30, 12, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(30122800, 30121695, 5), arg_types="IIi")


@RestartOnRest(30122520)
def Event_30122520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30122520"""
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


@RestartOnRest(30122300)
def Event_30122300(_, character: uint):
    """Event 30122300"""
    Kill(character)
    End()


@RestartOnRest(30122500)
def Event_30122500():
    """Event 30122500"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30122500)
    IfCharacterBackreadEnabled(AND_1, 30120500)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(30122501)
def Event_30122501():
    """Event 30122501"""
    EndIfFlagEnabled(30122502)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30122501)
    IfCharacterBackreadEnabled(AND_1, 30120500)
    IfFlagEnabled(AND_1, 30122500)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(30122502)
    Wait(0.0)
    ForceAnimation(30120500, 3024, loop=True, wait_for_completion=True, unknown2=1.0)
    EnableAI(30120500)
    End()


@RestartOnRest(30122502)
def Event_30122502(_, character: uint, seconds: float, animation_id: int):
    """Event 30122502"""
    EndIfFlagEnabled(30122502)
    DisableAI(character)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableNetworkFlag(30122502)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(30122800)
def Event_30122800():
    """Event 30122800"""
    EndIfFlagEnabled(30120800)
    IfHealthValueLessThanOrEqual(AND_1, 30120800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 30120801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(30100800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 30120800)
    IfCharacterDead(AND_2, 30120801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=30120800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30120800)
    EnableFlag(9211)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61211)


@RestartOnRest(30122810)
def Event_30122810():
    """Event 30122810"""
    GotoIfFlagDisabled(Label.L0, flag=30120800)
    DisableCharacter(30120800)
    DisableAnimations(30120800)
    Kill(30120800)
    DisableCharacter(30120801)
    DisableAnimations(30120801)
    Kill(30120801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30120800)
    DisableAI(30120801)
    ForceAnimation(30120800, 30001, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 30122805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30122800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(30120800, 20001, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30120800)
    SetNetworkUpdateRate(30120800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30120800, name=903460300)
    EnableAI(30120801)
    SetNetworkUpdateRate(30120801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30120801, name=903700300, bar_slot=1)


@RestartOnRest(30122811)
def Event_30122811():
    """Event 30122811"""
    EndIfFlagEnabled(30120800)
    IfHealthRatioLessThanOrEqual(OR_1, 30120800, value=0.6000000238418579)
    IfCharacterDead(OR_1, 30120801)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(30122802)


@RestartOnRest(30122849)
def Event_30122849():
    """Event 30122849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30120800, 30121800, 30122800, 30122805, 30125800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30120800, 30121800, 30122800, 30122805, 30122806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30120800, 30121800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30120800, 930000, 30122805, 30122806, 0, 30122802, 0, 0), arg_types="IiIIIIii")

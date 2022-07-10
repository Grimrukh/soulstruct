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
    RegisterGrace(grace_flag=31060000, obj=31061950, unknown=5.0)
    Event_31062800()
    Event_31062801()
    Event_31062802()
    Event_31062810()
    Event_31062849()
    Event_31062811()
    RunCommonEvent(0, 90005525, args=(31060600, 31061600), arg_types="II")
    RunCommonEvent(0, 90005511, args=(31060540, 31061540, 31063540, 27043, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(31060540, 31062540, 31062541), arg_types="III")
    RunCommonEvent(
        0,
        90005646,
        args=(31060800, 31062840, 31062841, 31061840, 31062840, 31, 6, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(31062800, 31061695, 5), arg_types="IIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31060200, 31062200, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060201, 31062200, 2.0, 1.2000000476837158, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060202, 31062200, 2.0, 1.399999976158142, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060203, 31062203, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060204, 31062203, 2.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060205, 31062205, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060211, 31062211, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060212, 31062211, 2.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060215, 31062215, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060280, 31062280, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060281, 31062281, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060282, 31062281, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060283, 31062283, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31060300, 31062300, 2.0, 0.0, 0), arg_types="IIffi")


@RestartOnRest(31062300)
def Event_31062300():
    """Event 31062300"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterInsideRegion(MAIN, character=31060300, region=31062301)
    Wait(2.0)
    ChangePatrolBehavior(31060300, patrol_information_id=31063301)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31062800)
def Event_31062800():
    """Event 31062800"""
    EndIfFlagEnabled(31060800)
    IfCharacterDead(AND_1, 31060800)
    IfCharacterDead(AND_1, 31060801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    KillBossAndDisplayBanner(character=31060800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31060800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61238)
    EnableFlag(9238)


@RestartOnRest(31062801)
def Event_31062801():
    """Event 31062801"""
    EndIfFlagEnabled(31060800)
    IfHealthValueLessThanOrEqual(MAIN, 31060800, value=0)
    Wait(4.0)
    PlaySoundEffect(31060800, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31062802)
def Event_31062802():
    """Event 31062802"""
    EndIfFlagEnabled(31060800)
    IfHealthValueLessThanOrEqual(MAIN, 31060801, value=0)
    Wait(4.0)
    PlaySoundEffect(31060801, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31062810)
def Event_31062810():
    """Event 31062810"""
    GotoIfFlagDisabled(Label.L0, flag=31060800)
    DisableCharacter(31060800)
    DisableCharacter(31060801)
    DisableAnimations(31060800)
    DisableAnimations(31060801)
    Kill(31060800)
    Kill(31060801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31060800)
    DisableAI(31060801)
    ForceAnimation(31060800, 30000, unknown2=1.0)
    ForceAnimation(31060801, 30000, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31062800)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=31060800, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=31060801, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(31060801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 31062805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31062800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31060800)
    EnableAI(31060801)
    SetNetworkUpdateRate(31060800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(31060801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31060800, name=903350310)
    EnableBossHealthBar(31060801, name=903350311, bar_slot=1)
    ForceAnimation(31060800, 20000, unknown2=1.0)
    ForceAnimation(31060801, 20000, unknown2=1.0)


@RestartOnRest(31062811)
def Event_31062811():
    """Event 31062811"""
    EndIfFlagEnabled(31060800)
    IfCharacterDead(OR_15, 31060800)
    IfCharacterDead(OR_15, 31060801)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableFlag(31062842)


@RestartOnRest(31062849)
def Event_31062849():
    """Event 31062849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31060800, 31061800, 31062800, 31062805, 31065800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31060800, 31061800, 31062800, 31062805, 31062806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31060800, 31061800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005813, args=(31060800, 31061801, 3, 0, 806760), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(31060800, 931000, 31062805, 31062806, 0, 31062842, 0, 0), arg_types="IiIIIIii")

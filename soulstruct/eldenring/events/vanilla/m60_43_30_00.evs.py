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
    RunCommonEvent(0, 9005810, args=(1043300800, 76161, 1043300950, 1043301950, 5.0), arg_types="IIIIf")
    Event_1043302800()
    Event_1043302810()
    Event_1043302849()
    RunCommonEvent(
        0,
        90005780,
        args=(1043300800, 1043302701, 1043302161, 1043300700, 20, 1043302701, 1043319209, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1043300800, 1043302701, 1043302161, 1043300700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005782,
        args=(1043302701, 1043302805, 1043300700, 1043302850, 1043302809, 0),
        arg_types="IIIIIi",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(1043300340, 30001, 20001, 1043302340, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1043302500)
def Event_1043302500():
    """Event 1043302500"""
    EnableCharacter(0)
    EnableAnimations(0)


@RestartOnRest(1043302800)
def Event_1043302800():
    """Event 1043302800"""
    EndIfFlagEnabled(1043300800)
    IfHealthValueLessThanOrEqual(MAIN, 1043300800, value=0)
    Wait(4.0)
    PlaySoundEffect(1043300800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1043300800)
    KillBossAndDisplayBanner(character=1043300800, banner_type=BannerType.Unknown)
    EnableFlag(1043300800)
    EnableFlag(9180)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61180)
    End()


@RestartOnRest(1043302810)
def Event_1043302810():
    """Event 1043302810"""
    GotoIfFlagDisabled(Label.L0, flag=1043300800)
    DisableCharacter(1043300800)
    DisableAnimations(1043300800)
    Kill(1043300800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1043300800)
    SetLockOnPoint(character=1043300800, lock_on_model_point=220, state=False)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1043302805)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1043302850)
    IfAttackedWithDamageType(OR_1, attacked_entity=1043300800, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_1, character=1043300800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1043300800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1043300800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1043300800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1043300800, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableAI(1043300800)
    SetNetworkUpdateRate(1043300800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1043300800, name=903460500)
    SetLockOnPoint(character=1043300800, lock_on_model_point=220, state=True)
    AddSpecialEffect(1043300800, 8089)


@RestartOnRest(1043302849)
def Event_1043302849():
    """Event 1043302849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1043300800, 1043301800, 1043302850, 1043302805, 1043305800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1043300800, 1043301800, 1043302850, 1043302805, 1043302806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1043300800, 1043301800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(1043300800, 950000, 1043302805, 1043302806, 0, 0, 0, 0), arg_types="IiIIIIii")

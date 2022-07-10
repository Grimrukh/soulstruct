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
    RegisterGrace(grace_flag=1048400000, obj=1048401950, unknown=5.0)
    RegisterGrace(grace_flag=1048400001, obj=1048401951, unknown=5.0)
    Event_1048402800()
    Event_1048402810()
    Event_1048402849()
    RunCommonEvent(0, 90005706, args=(1048400700, 30018, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048400700)


@RestartOnRest(1048402800)
def Event_1048402800():
    """Event 1048402800"""
    EndIfFlagEnabled(1048400800)
    IfHealthValueLessThanOrEqual(AND_1, 1048400800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 1048400801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(1048400800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 1048400800)
    IfCharacterDead(AND_2, 1048400801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=1048400800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(1048400800)
    EnableObjectActivation(1048401550, obj_act_id=-1)


@RestartOnRest(1048402810)
def Event_1048402810():
    """Event 1048402810"""
    GotoIfFlagDisabled(Label.L0, flag=1048400800)
    DisableCharacter(1048400800)
    DisableAnimations(1048400800)
    Kill(1048400800)
    DisableCharacter(1048400801)
    DisableAnimations(1048400801)
    Kill(1048400801)
    EnableObjectActivation(1048401550, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(1048400800, 30005, loop=True, unknown2=1.0)
    DisableAI(1048400801)
    DisableAI(1048400800)
    DisableObjectActivation(1048401550, obj_act_id=-1)
    IfFlagEnabled(AND_1, 1048402805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1048402800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableAI(1048400801)
    SetNetworkUpdateRate(1048400801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1048400801, name=904340542)
    ForceAnimation(1048400801, 3012, loop=True, unknown2=1.0)
    SetNetworkUpdateRate(1048400800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1048400800, name=904340541, bar_slot=1)
    Wait(2.200000047683716)
    EnableAI(1048400800)
    ForceAnimation(1048400800, 20005, loop=True, unknown2=1.0)


@RestartOnRest(1048402849)
def Event_1048402849():
    """Event 1048402849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1048400800, 1048401800, 1048402800, 1048402805, 1048405800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1048400800, 1048401800, 1048402800, 1048402805, 1048402806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1048400800, 1048401800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(1048400800, 1048401801, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1048400800, 920900, 1048402805, 1048402806, 0, 1048402802, 0, 0),
        arg_types="IiIIIIii",
    )

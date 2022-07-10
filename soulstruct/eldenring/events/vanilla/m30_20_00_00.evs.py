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
    RegisterGrace(grace_flag=30200000, obj=30201950, unknown=5.0)
    Event_30202800()
    Event_30202810()
    Event_30202811()
    Event_30202829()
    RunCommonEvent(0, 90005616, args=(30207910, 30202700), arg_types="II")
    RunCommonEvent(0, 90005211, args=(30200200, 30002, 20002, 30202200, 1.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30200201, 30002, 20002, 30202201, 1.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30200202, 30002, 20002, 30202202, 1.0, 1.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(30200210, 30202200, 1.0, 0.10000000149011612, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200211, 30202200, 1.0, 0.30000001192092896, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200214, 30202257, 1.0, 0.10000000149011612, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200215, 30202257, 1.0, 0.30000001192092896, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200216, 30202257, 1.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200217, 30202257, 1.0, 0.30000001192092896, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200218, 30202257, 1.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(30200243, 30002, 20002, 30202243, 1.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30200244, 30002, 20002, 30202243, 1.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30200245, 30002, 20002, 30202243, 1.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30200250, 30002, 20002, 30202250, 1.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30200251, 30002, 20002, 30202250, 2.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30200252, 30000, 20000, 30202250, 2.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(30200253, 30202253, 0.0, 0.800000011920929, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200254, 30202254, 0.0, 0.800000011920929, 0), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(30200255, 30001, 20001, 30202202, 1.0, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30200256, 30001, 20001, 30202202, 1.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(30200257, 30202257, 0.0, 0.800000011920929, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200260, 30202260, 1.0, 0.10000000149011612, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200261, 30202260, 1.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200262, 30202260, 1.0, 0.10000000149011612, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30200263, 30202260, 1.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005646,
        args=(30200800, 30202840, 30202841, 30201840, 30202840, 30, 20, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 90005525, args=(30200560, 30201560), arg_types="II")
    RunCommonEvent(
        0,
        90005501,
        args=(30200510, 30200511, 4, 30201510, 30201511, 30201512, 30200512),
        arg_types="IIIIIII",
    )
    Event_30202510()
    RunCommonEvent(0, 90005650, args=(30200540, 30201540, 30201541, 30203541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30200540, 30201540), arg_types="II")
    Event_30202200()


@NeverRestart(30202510)
def Event_30202510():
    """Event 30202510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30200510,
            30200511,
            4,
            30201510,
            30201511,
            30203511,
            30201512,
            30203512,
            30202511,
            30202512,
            30200512,
            30200513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(30202520)
def Event_30202520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30202520"""
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


@RestartOnRest(30202200)
def Event_30202200():
    """Event 30202200"""
    DisableObject(30201200)
    End()


@RestartOnRest(30202800)
def Event_30202800():
    """Event 30202800"""
    EndIfFlagEnabled(30200800)
    IfHealthValueLessThanOrEqual(MAIN, 30200800, value=0)
    Wait(4.0)
    PlaySoundEffect(30208000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30200800)
    KillBossAndDisplayBanner(character=30200800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(30201671, obj_act_id=-1)
    EnableFlag(30200800)
    EnableFlag(9220)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61220)


@RestartOnRest(30202810)
def Event_30202810():
    """Event 30202810"""
    GotoIfFlagDisabled(Label.L0, flag=30200800)
    DisableCharacter(30205800)
    DisableAnimations(30205800)
    Kill(30205800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30205800)
    DisableCharacter(30200800)
    DisableAnimations(30200800)
    DisableHealthBar(30200800)
    DisableObjectActivation(30201671, obj_act_id=-1)
    IfFlagEnabled(AND_2, 30202805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30202800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetNetworkUpdateRate(30200800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(30200801, 20010, unknown2=1.0)
    Unknown_2004_67(character=PLAYER, entity=30200800)
    IfCharacterHasSpecialEffect(MAIN, 30200801, 16307)
    EnableCharacter(30200800)
    EnableAnimations(30200800)
    DisableAnimations(30200801)
    Wait(0.5)
    Move(
        30200800,
        destination=30200801,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=30200801,
    )
    ForceAnimation(30200800, 63010, skip_transition=True, unknown2=1.0)
    Wait(4.0)
    EnableAI(30205800)
    SetNetworkUpdateRate(30205800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30200800, name=903320300)


@RestartOnRest(30202811)
def Event_30202811():
    """Event 30202811"""
    EndIfFlagEnabled(30200800)
    IfHealthLessThanOrEqual(AND_1, 30200800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30202802)


@RestartOnRest(30202829)
def Event_30202829():
    """Event 30202829"""
    RunCommonEvent(
        0,
        9005800,
        args=(30200800, 30201800, 30202800, 30202805, 30205800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30200800, 30201800, 30202800, 30202805, 30202806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30200800, 30201800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30200800, 921100, 30202805, 30202806, 0, 30202802, 0, 0), arg_types="IiIIIIii")

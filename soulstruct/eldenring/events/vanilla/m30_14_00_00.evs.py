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
    RegisterGrace(grace_flag=301400, obj=30141950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(30141150, 100, 800, 0), arg_types="IiiI")
    Event_30142800()
    Event_30142801()
    Event_30142849()
    Event_30142811()
    RunCommonEvent(0, 90005200, args=(30140200, 30001, 20001, 30142262, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140201, 30010, 20010, 30142201, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30140268, 30142251, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30140202, 30142202, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30140252, 30001, 20001, 30142256, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30140251, 30142264, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30140253, 30142261, 0.5, 3004), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30140269, 30001, 20001, 30142265, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30140270, 30001, 20001, 30142265, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30140271, 30001, 20001, 30142265, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140272, 30001, 20001, 30142265, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140261, 30000, 20000, 30142258, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140262, 30010, 20010, 30142258, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140263, 30010, 20010, 30142258, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(30140213, 30009, 20009, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005201,
        args=(30140214, 30009, 20009, 4.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiffIIII",
    )
    RunCommonEvent(0, 90005250, args=(30140216, 30142215, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30140217, 30142215, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30140264, 30142215, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30140210, 30000, 20000, 30142210, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30140211, 30000, 20000, 30142210, 3.299999952316284, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30140212, 30000, 20000, 30142210, 4.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140219, 30009, 20009, 30142219, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140220, 30009, 20009, 30142219, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30140222, 30009, 20009, 30142219, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30140219, 30142219, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30140220, 30142219, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30140222, 30142219, 0.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30140223, 30142223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30140260, 30000, 20000, 30142257, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30140265, 30000, 20000, 30142263, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(30140266, 30000, 20000, 30142263, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30140267, 30000, 20000, 30142263, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005650, args=(30140540, 30141540, 30141541, 30143541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30140540, 30141540), arg_types="II")
    RunCommonEvent(
        0,
        90005501,
        args=(30140510, 30141510, 0, 30141510, 30141511, 30141512, 30140511),
        arg_types="IIIIIII",
    )
    Event_30142510()
    Event_30142580()
    RunCommonEvent(
        0,
        90005646,
        args=(30140800, 30142840, 30142841, 30141840, 30142840, 30, 14, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(30142800, 30141695, 5), arg_types="IIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30140519()


@NeverRestart(30142510)
def Event_30142510():
    """Event 30142510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30140510,
            30141510,
            0,
            30141510,
            30141511,
            30143511,
            30141512,
            30143512,
            30142511,
            30142512,
            30140511,
            30142512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30140519)
def Event_30140519():
    """Event 30140519"""
    EndIfFlagEnabled(30140519)
    EnableFlag(30140510)


@RestartOnRest(30142520)
def Event_30142520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30142520"""
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


@NeverRestart(30142580)
def Event_30142580():
    """Event 30142580"""
    RegisterLadder(start_climbing_flag=30140580, stop_climbing_flag=30140581, obj=30141580)


@RestartOnRest(30142800)
def Event_30142800():
    """Event 30142800"""
    EndIfFlagEnabled(30140800)
    IfHealthValueLessThanOrEqual(AND_1, 30140800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 30140801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(30140800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 30140800)
    IfCharacterDead(AND_2, 30140801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=30140800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30140800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61214)
    EnableFlag(9214)


@RestartOnRest(30142801)
def Event_30142801():
    """Event 30142801"""
    GotoIfFlagDisabled(Label.L0, flag=30140800)
    DisableCharacter(30140800)
    DisableAnimations(30140800)
    Kill(30140800)
    DisableCharacter(30140801)
    DisableAnimations(30140801)
    Kill(30140801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30140800)
    DisableAI(30140801)
    IfFlagEnabled(AND_2, 30142805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30142800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30140800)
    SetNetworkUpdateRate(30140800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30140800, name=904260304)
    EnableAI(30140801)
    SetNetworkUpdateRate(30140801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30140801, name=904260305, bar_slot=1)


@RestartOnRest(30142811)
def Event_30142811():
    """Event 30142811"""
    EndIfFlagEnabled(30140800)
    IfHealthLessThanOrEqual(AND_1, 30140800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30142802)


@RestartOnRest(30142849)
def Event_30142849():
    """Event 30142849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30140800, 30141800, 30142800, 30142805, 30145800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30140800, 30141800, 30142800, 30142805, 30142806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30140800, 30141800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30140800, 930000, 30142805, 30142806, 0, 30142802, 0, 0), arg_types="IiIIIIii")

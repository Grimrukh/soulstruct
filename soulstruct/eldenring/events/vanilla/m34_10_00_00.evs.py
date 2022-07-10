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
    RegisterGrace(grace_flag=34100000, obj=34101950, unknown=5.0)
    RegisterGrace(grace_flag=34100002, obj=34101952, unknown=5.0)
    RunCommonEvent(
        0,
        90005508,
        args=(34100510, 34101510, 0, 34101510, 34101511, 34101512, 34100511),
        arg_types="IIIIIII",
    )
    Event_34102510()
    RunCommonEvent(
        0,
        90005605,
        args=(34101600, 34, 10, 0, 0, 34102600, 0, 34102610, 34102611, 34102612, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(
        0,
        90005110,
        args=(191, 9101, 34101650, 34100500, 8148, 806934, 9080, 60522, 0),
        arg_types="IIIiiiiii",
    )
    RunCommonEvent(0, 90005300, args=(34100300, 34100300, 34100300, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(34100200, 30020, 20020, 34102200, 15.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34100201, 30020, 20020, 34102200, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(34100202, 34102200, 8.0, -1), arg_types="IIfi")


@NeverRestart(34102510)
def Event_34102510():
    """Event 34102510"""
    RunCommonEvent(
        0,
        90005507,
        args=(
            34100510,
            34101510,
            0,
            34101510,
            34101511,
            34102513,
            34101512,
            34102514,
            34102511,
            34102512,
            34100511,
            34102512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(34102690)
def Event_34102690():
    """Event 34102690"""
    DisableNetworkSync()
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=34102690)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=34102691)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfUnknownCondition_31(OR_1, hours=8, unknown1=0.0, unknown2=0)
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    Unknown_2003_68(unknown1=8, unknown2=-1.0, unknown3=0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfUnknownCondition_31(OR_1, hours=11, unknown1=0.0, unknown2=0)
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    Unknown_2003_68(unknown1=11, unknown2=-1.0, unknown3=0)

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(34102800)
def Event_34102800():
    """Event 34102800"""
    EndIfFlagEnabled(34100800)
    IfHealthValueLessThanOrEqual(MAIN, 34100800, value=0)
    Wait(4.0)
    PlaySoundEffect(34108000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 34100800)
    KillBossAndDisplayBanner(character=34100800, banner_type=BannerType.Unknown)
    EnableFlag(9280)
    EnableFlag(34100800)


@RestartOnRest(34102810)
def Event_34102810():
    """Event 34102810"""
    GotoIfFlagDisabled(Label.L0, flag=34100800)
    DisableCharacter(34100800)
    DisableAnimations(34100800)
    Kill(34100800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34100800)
    GotoIfFlagEnabled(Label.L1, flag=34100801)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34102801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=34100800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(34100801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 34102805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=34102800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(34100800)
    SetNetworkUpdateRate(34100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34100800)


@RestartOnRest(34102849)
def Event_34102849():
    """Event 34102849"""
    RunCommonEvent(
        0,
        9005800,
        args=(34100800, 34101800, 34102800, 34102805, 34105800, 10000, 34100801, 34102801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(34100800, 34101800, 34102800, 34102805, 34102806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(34100800, 34101800, 3, 34100801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(34100800, 90003101, 34102805, 34102806, 0, 11002852, 0, 0), arg_types="IiIIIIii")

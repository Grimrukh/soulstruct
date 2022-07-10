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
    RegisterGrace(grace_flag=34150000, obj=34151950, unknown=5.0)
    Event_34152500()
    RunCommonEvent(
        0,
        90005508,
        args=(34150510, 34151510, 0, 34151510, 34151511, 34151512, 34150511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005110,
        args=(196, 9120, 34151599, 34150000, 8153, 806940, 9085, 60525, 0),
        arg_types="IIIiiiiii",
    )


@NeverRestart(34152500)
def Event_34152500():
    """Event 34152500"""
    RunCommonEvent(
        0,
        90005507,
        args=(
            34150510,
            34151510,
            0,
            34151510,
            34151511,
            34152513,
            34151512,
            34152514,
            34152511,
            34152512,
            34150511,
            34152512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(34152800)
def Event_34152800():
    """Event 34152800"""
    EndIfFlagEnabled(34150800)
    IfHealthValueLessThanOrEqual(MAIN, 34150800, value=0)
    Wait(4.0)
    PlaySoundEffect(34150800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 34150800)
    KillBossAndDisplayBanner(character=34150800, banner_type=BannerType.Unknown)
    EnableFlag(34150800)


@RestartOnRest(34152810)
def Event_34152810():
    """Event 34152810"""
    GotoIfFlagDisabled(Label.L0, flag=34150800)
    DisableCharacter(34150800)
    DisableAnimations(34150800)
    Kill(34150800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34150800)
    DisableAnimations(34150800)
    IfFlagEnabled(AND_1, 34152805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34152800)
    IfAttackedWithDamageType(OR_1, attacked_entity=34150800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(34150800)
    EnableAnimations(34150800)
    SetNetworkUpdateRate(34150800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34150800)


@RestartOnRest(34152849)
def Event_34152849():
    """Event 34152849"""
    RunCommonEvent(
        0,
        9005800,
        args=(34150800, 34151800, 34152800, 34152805, 34155800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(34150800, 34151800, 34152800, 34152805, 34152806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(34150800, 34151800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(34150800, 900000, 34152805, 34152806, 0, 11002852, 0, 0), arg_types="IiIIIIii")

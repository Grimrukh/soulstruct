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
    RegisterGrace(grace_flag=34130001, obj=34131951, unknown=5.0)
    RegisterGrace(grace_flag=34130002, obj=34131952, unknown=5.0)
    Event_34132800()
    Event_34132810()
    Event_34132849()
    RunCommonEvent(
        0,
        90005110,
        args=(192, 9130, 34131599, 34130050, 8149, 806930, 9081, 60520, 0),
        arg_types="IIIiiiiii",
    )
    RunCommonEvent(0, 90005920, args=(34130600, 34131600, 34133600), arg_types="III")
    RunCommonEvent(
        0,
        90005646,
        args=(34130800, 34132840, 34132841, 34131840, 1049410300, 60, 49, 41, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(
        0,
        90005508,
        args=(34130510, 34131510, 0, 34131510, 34131511, 34131512, 34130511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005508,
        args=(34130515, 34131515, 0, 34131515, 34131516, 34131517, 34130516),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005508,
        args=(34130520, 34131520, 1, 34131520, 34131521, 34131522, 34130521),
        arg_types="IIIIIII",
    )
    Event_34132510()
    Event_34132515()
    Event_34132520()
    Event_34132580()
    RunCommonEvent(0, 90005511, args=(34130560, 34131560, 34133560, 227010, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(34130560, 34132560, 34132561), arg_types="III")
    Event_34132590(0, entity=34131590, region=34132590, animation_id=1, obj=34131592)
    Event_34132590(1, entity=34131591, region=34132591, animation_id=1000001, obj=34131593)
    RunCommonEvent(0, 90005690, args=(34132592,))
    RunCommonEvent(0, 90005691, args=(34132592,))
    RunCommonEvent(0, 90005690, args=(34132593,))
    RunCommonEvent(0, 90005691, args=(34132593,))
    RunCommonEvent(0, 90005250, args=(34130299, 34132299, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(34130298, 10.0, 0.0, -1), arg_types="Iffi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_34130519()


@NeverRestart(34132510)
def Event_34132510():
    """Event 34132510"""
    RunCommonEvent(
        0,
        90005507,
        args=(
            34130510,
            34131510,
            0,
            34131510,
            34131511,
            34132513,
            34131512,
            34132514,
            34132511,
            34132512,
            34130511,
            34132512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(34132515)
def Event_34132515():
    """Event 34132515"""
    RunCommonEvent(
        0,
        90005507,
        args=(
            34130515,
            34131515,
            0,
            34131515,
            34131516,
            34132518,
            34131517,
            34132519,
            34132516,
            34132517,
            34130516,
            34132517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(34132520)
def Event_34132520():
    """Event 34132520"""
    RunCommonEvent(
        0,
        90005507,
        args=(
            34130520,
            34131520,
            1,
            34131520,
            34131521,
            34132523,
            34131522,
            34132524,
            34132521,
            34132522,
            34130521,
            34132522,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(34130519)
def Event_34130519():
    """Event 34130519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(34130520)


@NeverRestart(34132580)
def Event_34132580():
    """Event 34132580"""
    RegisterLadder(start_climbing_flag=34130580, stop_climbing_flag=34130581, obj=34131580)


@RestartOnRest(34132590)
def Event_34132590(_, entity: uint, region: uint, animation_id: int, obj: uint):
    """Event 34132590"""
    ForceAnimation(entity, 0, unknown2=1.0)
    SkipLinesIfObjectNotDestroyed(1, obj)
    RestoreObject(obj)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    DestroyObject(obj, request_slot=0)
    ForceAnimation(entity, animation_id, unknown2=1.0)


@RestartOnRest(34132800)
def Event_34132800():
    """Event 34132800"""
    EndIfFlagEnabled(34130800)
    IfHealthValueLessThanOrEqual(MAIN, 34130800, value=0)
    Wait(4.0)
    PlaySoundEffect(34130800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 34130800)
    KillBossAndDisplayBanner(character=34130800, banner_type=BannerType.Unknown)
    EnableFlag(34130800)
    EnableFlag(9173)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61173)


@RestartOnRest(34132810)
def Event_34132810():
    """Event 34132810"""
    GotoIfFlagDisabled(Label.L0, flag=34130800)
    DisableCharacter(34130800)
    DisableAnimations(34130800)
    Kill(34130800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34130800)
    DisableAnimations(34130800)
    IfFlagEnabled(AND_1, 34132805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34132800)
    IfAttackedWithDamageType(OR_1, attacked_entity=34130800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableAI(34130800)
    EnableAnimations(34130800)
    SetNetworkUpdateRate(34130800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34130800, name=903560000)


@RestartOnRest(34132849)
def Event_34132849():
    """Event 34132849"""
    RunCommonEvent(
        0,
        9005800,
        args=(34130800, 34131800, 34132800, 34132805, 34135800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(34130800, 34131800, 34132800, 34132805, 34132806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(34130800, 34131800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(34130800, 930000, 34132805, 34132806, 0, 34132802, 0, 0), arg_types="IiIIIIii")
    RunCommonEvent(
        0,
        9005800,
        args=(34130800, 31121800, 34132800, 34132805, 31125800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(34130800, 31121800, 34132800, 34132805, 31122806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(34130800, 34131800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005812, args=(34130800, 34131801, 3, 0, 0), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(34130800, 356000, 34132805, 34132806, 0, 0, 0, 0), arg_types="IiIIIIii")

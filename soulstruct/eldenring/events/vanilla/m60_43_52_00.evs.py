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
    Event_1043522500(
        0,
        character=1043520700,
        character_1=1043520701,
        flag=1043520505,
        region=1043522500,
        flag_1=1043522500
    )
    Event_1043522505(0, flag=1043520505, character=1043520700, character_1=1043520701, flag_1=1043522500)
    Event_1043522510()
    Event_1043522515()
    RunCommonEvent(0, 90005300, args=(1043520506, 1043520701, 1043520500, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1043520400, 1043520400, 40316, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005631, args=(1043521401, 61032), arg_types="Ii")
    RunCommonEvent(0, 90005705, args=(1043520710,))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043520705)
    DisableBackread(1043520710)


@RestartOnRest(1043522500)
def Event_1043522500(_, character: uint, character_1: uint, flag: uint, region: uint, flag_1: uint):
    """Event 1043522500"""
    DisableCharacter(character_1)
    DisableGravity(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    EndIfFlagEnabled(flag)
    ForceAnimation(character, 30029, loop=True, skip_transition=True, unknown2=1.0)
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterBackreadEnabled(AND_1, character)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.5)
    IfHealthValueEqual(AND_15, character, value=0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_15)
    EnableAI(character)
    ForceAnimation(character, 20030, loop=True, skip_transition=True, unknown2=1.0)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    AddSpecialEffect(character, 9730)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=636615, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    ForceAnimation(character, 20030, skip_transition=True, unknown2=1.0)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        short_move=True,
    )
    Wait(1.0)
    ForceAnimation(character, 20030, skip_transition=True, unknown2=1.0)
    Wait(1.0)
    ForceAnimation(character, 20030, skip_transition=True, unknown2=1.0)
    Wait(1.0)
    EnableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(1043522506)
    End()


@RestartOnRest(1043522505)
def Event_1043522505(_, flag: uint, character: uint, character_1: uint, flag_1: uint):
    """Event 1043522505"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 1043522700)
    IfFlagDisabled(AND_1, 1043522506)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    EnableGravity(character_1)
    AddSpecialEffect(character_1, 9732)
    Kill(character)
    DisableGravity(character)
    DisableCharacter(character)
    DisableAI(character)
    Wait(0.4000000059604645)
    EnableAI(character_1)
    EnableAnimations(character_1)
    IfCharacterDead(MAIN, character_1)
    Move(
        character,
        destination=character_1,
        destination_type=CoordEntityType.Character,
        model_point=900,
        short_move=True,
    )
    EnableCharacter(character)
    EnableAnimations(character)
    EnableGravity(character)
    EnableFlag(flag)
    End()


@RestartOnRest(1043522510)
def Event_1043522510():
    """Event 1043522510"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, 1043522700)
    EnableNetworkFlag(1043522700)
    IfFlagDisabled(MAIN, 1043522700)
    DisableNetworkFlag(1043522700)
    End()


@RestartOnRest(1043522515)
def Event_1043522515():
    """Event 1043522515"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043520505)
    SetCharacterTalkRange(character=1043520700, distance=150.0)
    SetCharacterTalkRange(character=1043520701, distance=150.0)
    AwaitFlagEnabled(flag=1043520505)
    SetCharacterTalkRange(character=1043520700, distance=17.0)
    SetCharacterTalkRange(character=1043520701, distance=17.0)
    End()

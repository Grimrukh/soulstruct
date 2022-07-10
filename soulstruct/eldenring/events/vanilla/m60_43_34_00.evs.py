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
    RegisterGrace(grace_flag=1043340000, obj=1043341950, unknown=5.0)
    RunCommonEvent(0, 90005461, args=(1043340204,))
    RunCommonEvent(1, 90005462, args=(1043340204,))
    RunCommonEvent(0, 90005460, args=(1043340204,))
    Event_1043342220(0, character=1043340220, obj=1043341220, region=1043342220)
    Event_1043342220(1, character=1043340221, obj=1043341221, region=1043342220)
    Event_1043342220(2, character=1043340222, obj=1043341222, region=1043342220)
    Event_1043342220(3, character=1043340223, obj=1043341223, region=1043342223)
    Event_1043342220(4, character=1043340224, obj=1043341224, region=1043342223)
    Event_1043342220(5, character=1043340225, obj=1043341225, region=1043342223)
    RunCommonEvent(0, 90005683, args=(62150, 1043341684, 210, 78196, 78196), arg_types="IIiII")
    RunCommonEvent(0, 90005300, args=(1043340340, 1043340340, 1043340400, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005706, args=(1043340700, 930025, 1043341700), arg_types="IiI")
    RunCommonEvent(0, 90005771, args=(1043340950, 1043342700), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043340700)
    RunCommonEvent(0, 90005201, args=(1043340210, 30004, 20004, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1043340212, 30004, 20004, 1043342212, 10.0, 2.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1043340213, 30004, 20004, 1043342212, 10.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1043340214, 30004, 20004, 1043342212, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005250, args=(1043340300, 1043342300, 0.0, 3031), arg_types="IIfi")


@RestartOnRest(1043342220)
def Event_1043342220(_, character: uint, obj: uint, region: uint):
    """Event 1043342220"""
    EnableObject(obj)
    DisableCharacter(character)
    EndIfFlagEnabled(1044342300)
    IfCharacterDead(AND_5, character)
    EndIfConditionTrue(input_condition=AND_5)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1044342300)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableObject(obj)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1043343700)
def Event_1043343700(_, character: uint):
    """Event 1043343700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023, unknown2=1.0)
    End()

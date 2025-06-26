"""
Land of Shadow 12-12 SE SE

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
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=2051480000, asset=2051481950)
    RegisterGrace(grace_flag=2051480001, asset=2051481951)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_205148200(0, character=2051480200, animation_id=30003, animation_id_1=20003, seconds=1.0, flag=2051482290)
    Event_205148200(1, character=2051480201, animation_id=30003, animation_id_1=20003, seconds=0.5, flag=2051482290)
    Event_205148200(2, character=2051480202, animation_id=30003, animation_id_1=20003, seconds=0.0, flag=2051482292)
    Event_205148200(
        3,
        character=2051480203,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.20000000298023224,
        flag=2051482291,
    )
    Event_205148200(
        4,
        character=2051480204,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.800000011920929,
        flag=2051482291,
    )
    Event_205148200(
        5,
        character=2051480205,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.4000000059604645,
        flag=2051482292,
    )
    Event_205148200(6, character=2051480206, animation_id=30003, animation_id_1=20003, seconds=0.0, flag=2051482296)
    Event_205148200(
        7,
        character=2051480207,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.6000000238418579,
        flag=2051482293,
    )
    Event_205148200(8, character=2051480208, animation_id=30003, animation_id_1=20003, seconds=0.5, flag=2051482294)
    Event_205148200(
        9,
        character=2051480209,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.699999988079071,
        flag=2051482294,
    )
    Event_205148200(
        10,
        character=2051480210,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.6000000238418579,
        flag=2051482293,
    )
    Event_205148200(
        11,
        character=2051480211,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.10000000149011612,
        flag=2051482293,
    )
    Event_205148200(
        12,
        character=2051480212,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.30000001192092896,
        flag=2051482295,
    )
    Event_205148200(
        13,
        character=2051480213,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.8999999761581421,
        flag=2051482295,
    )
    Event_205148200(
        14,
        character=2051480214,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.30000001192092896,
        flag=2051482296,
    )
    Event_205148200(
        15,
        character=2051480215,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.30000001192092896,
        flag=2051482296,
    )
    Event_205148200(
        16,
        character=2051480216,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.30000001192092896,
        flag=2051482295,
    )


@RestartOnRest(205148200)
def Event_205148200(_, character: uint, animation_id: int, animation_id_1: int, seconds: float, flag: Flag | int):
    """Event 205148200"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    ForceAnimation(character, animation_id, loop=True)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableFlag(flag)
    Wait(0.10000000149011612)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    Wait(seconds)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

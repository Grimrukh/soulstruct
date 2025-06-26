"""
Land of Shadow 11-10 SW NE

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=2045410000, asset=2045411950, enemy_block_distance=0.0)
    CommonFunc_90005790(
        0,
        right=0,
        flag=2045410180,
        summon_flag=2045412181,
        dismissal_flag=2045412182,
        character=2045410700,
        sign_type=23,
        region=2045412700,
        region_1=2045412701,
        seconds=0.0,
        right_1=2045429293,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2045410180, flag_1=2045412181, flag_2=2045412182, character=2045410700)
    CommonFunc_90005792(
        0,
        flag=2045410180,
        flag_1=2045412181,
        flag_2=2045412182,
        character=2045410700,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2045410180,
        flag_1=2045412181,
        flag_2=2045412182,
        character=2045410700,
        other_entity=2045412700,
        region=0,
        left=0,
    )
    CommonFunc_90005774(0, flag=2045410180, item_lot=116401, flag_1=400645)
    CommonFunc_90005557(0, entity=2045411680)
    CommonFunc_90005557(0, entity=2045411681)
    CommonFunc_90005557(0, entity=2045411682)
    CommonFunc_90005557(0, entity=2045411683)
    CommonFunc_90005557(0, entity=2045411684)
    CommonFunc_90005557(0, entity=2045411685)
    CommonFunc_90005557(0, entity=2045411686)
    CommonFunc_90005557(0, entity=2045411687)
    CommonFunc_90005557(0, entity=2045411688)
    CommonFunc_90005556(0, asset=2045411689, flag=2045417900)
    CommonFunc_90005639(0, flag=2045410500, asset=2045411500, asset_1=2045411501, asset_2=2045411502, seconds=2.0)
    CommonFunc_90005766(0, flag=2045412181, character=2045410700, distance=100.0, flag_1=2045429277, flag_2=4963)
    CommonFunc_90005767(
        0,
        flag=2045429280,
        first_flag=4380,
        last_flag=4383,
        character=2045410700,
        flag_1=4901,
        character_1=2045410701,
        flag_2=2045429297,
    )
    CommonFunc_90005777(0, character=2045410701, flag=4963, flag_1=4383, flag_2=2045412181)
    CommonFunc_90005774(0, flag=2045429297, item_lot=116401, flag_1=400645)
    CommonFunc_90005757(
        0,
        character=2045400700,
        character_1=2045400701,
        flag=4385,
        flag_1=4953,
        flag_2=2045422710,
        flag_3=4383,
    )
    CommonFunc_90005759(
        0,
        flag=2045429280,
        flag_1=4385,
        flag_2=4963,
        character=2045400700,
        flag_3=4953,
        flag_4=2045429293,
        first_flag=4950,
        last_flag=4956,
        flag_5=2045429281,
        flag_6=2045429282,
        flag_7=4901,
        seconds=1.0,
        flag_8=2045429343,
        radius=30.0,
    )
    CommonFunc_90005778(0, flag=2045402700, flag_1=4953, flag_2=400753, attacked_entity=2045400700)
    CommonFunc_90005779(0, character=2045400700, flag=4953, animation_id=20016, flag_1=4385, flag_2=4383)
    CommonFunc_90005744(0, entity=2045400700, flag=2045409200, flag_1=2045409200, animation_id=20015)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_2045412300(
        0,
        character=2045410211,
        character_1=2045415300,
        animation_id=30000,
        animation_id_1=20000,
        radius=9.0,
    )
    Event_2045412300(
        1,
        character=2045410209,
        character_1=2045415300,
        animation_id=30000,
        animation_id_1=20000,
        radius=9.0,
    )
    Event_2045412300(
        2,
        character=2045410206,
        character_1=2045415300,
        animation_id=30001,
        animation_id_1=20001,
        radius=9.0,
    )
    Event_2045412300(
        3,
        character=2045410218,
        character_1=2045415301,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
    )
    Event_2045412300(
        4,
        character=2045410210,
        character_1=2045415301,
        animation_id=30001,
        animation_id_1=20001,
        radius=10.0,
    )
    Event_2045412300(
        5,
        character=2045410221,
        character_1=2045415302,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
    )
    Event_2045412300(
        6,
        character=2045410227,
        character_1=2045415302,
        animation_id=30001,
        animation_id_1=20001,
        radius=8.0,
    )
    CommonFunc_90005200(
        0,
        character=2045410202,
        animation_id=30002,
        animation_id_1=20002,
        region=2045412202,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(2045412300)
def Event_2045412300(_, character: uint, character_1: uint, animation_id: int, animation_id_1: int, radius: float):
    """Event 2045412300"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    OR_9.Add(OR_1)
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(OR_2)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=radius))
    OR_9.Add(AND_3)
    
    MAIN.Await(OR_9)
    
    Wait(0.10000000149011612)
    ForceAnimation(character, animation_id_1)
    EnableAI(character)
    SetSpecialStandbyEndedFlag(character=character, state=True)

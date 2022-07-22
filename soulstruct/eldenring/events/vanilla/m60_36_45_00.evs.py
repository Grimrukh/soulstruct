"""
East Liurnia (SW) (NW)

linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_36_45_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036450000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005261(
        0,
        character=Characters.DeathRiteBird,
        region=1036452340,
        radius=10.0,
        seconds=0.0,
        animation_id=1700,
    )
    CommonFunc_90005860(
        0,
        flag=1036450800,
        left=0,
        character=Characters.DeathRiteBird,
        left_1=0,
        item_lot=1036450400,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.DeathRiteBird, name=904980604, npc_threat_level=24)
    CommonFunc_90005605(
        0,
        1036451620,
        60,
        34,
        48,
        0,
        1034482620,
        0,
        1036452620,
        1036452621,
        1036452622,
        0,
        0,
        0.0,
        0.0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Skeleton0, region=1036452220, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Skeleton1, region=1036452220, radius=10.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Skeleton2, region=1036452220, radius=10.0, seconds=0.5, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Skeleton3, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Skeleton4, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Skeleton5, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1036450226, region=1036452226, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1036450227, region=1036452226, radius=0.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(0, character=1036450228, region=1036452226, radius=0.0, seconds=0.5, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=1036450229,
        region=1036452226,
        radius=0.0,
        seconds=0.30000001192092896,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=1036450230, region=1036452226, radius=0.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(0, character=1036450231, region=1036452226, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Skeleton6, region=1036452250, radius=0.0, seconds=0.5, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton7,
        region=1036452250,
        radius=0.0,
        seconds=0.30000001192092896,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=Characters.Skeleton8, region=1036452250, radius=0.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(0, 1036450250, 1036452250, 0.0, 0.0, -1)


@RestartOnRest(1036452200)
def Event_1036452200(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1036452200"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AddSpecialEffect(character, 8560)
    DisableCharacter(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    EnableCharacter(character)

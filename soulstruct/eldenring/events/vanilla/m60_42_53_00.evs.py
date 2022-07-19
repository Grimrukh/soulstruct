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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_42_53_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(0, flag=1042530501, character=1042530501, item_lot_param_id=1042530300, seconds=0.0, left=0)
    CommonFunc_90005390(
        0,
        flag=1042530350,
        flag_1=1042532350,
        anchor_entity=Characters.WanderingNoble,
        character=Characters.LionGuardian,
        left=0,
        item_lot_param_id=1043530100,
    )
    CommonFunc_90005391(0, 1042530350, 1042532350, 1042530365, 1042530350, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=1042530202, region=1042532202, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=1042530201,
        animation_id=30002,
        animation_id_1=20002,
        region=1042532300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellFootSoldier1,
        animation_id=30010,
        animation_id_1=20010,
        region=1042532305,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellFootSoldier6,
        animation_id=30010,
        animation_id_1=20010,
        region=1042532305,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellFootSoldier7,
        animation_id=30010,
        animation_id_1=20010,
        region=1042532305,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=1042530319, region=1042532202, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=1042530320, region=1042532202, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=1042530323, region=1042532202, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=1042530300,
        animation_id=30005,
        animation_id_1=20021,
        region=1042532300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1042530308,
        animation_id=30010,
        animation_id_1=20010,
        region=1042532300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1042530309,
        animation_id=30010,
        animation_id_1=20010,
        region=1042532300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=1042530322, region=1042532300, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier5,
        animation_id=30005,
        animation_id_1=20021,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier0,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier2,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier3,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier4,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1042532365(0, 1042530365)


@RestartOnRest(1042532365)
def Event_1042532365(_, character: uint):
    """Event 1042532365"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableAI(character)
    ForceAnimation(character, 30012, loop=True)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
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
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    
    MAIN.Await(OR_1)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    EnableAI(character)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy1,
        character_1=Characters.LeyndellFootSoldier0,
        asset=Assets.AEG110_181_9001,
        asset_1=0,
        obj_act_id=0,
        region=1042532402,
        left=0,
    )
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy3,
        character_1=Characters.LeyndellFootSoldier2,
        asset=Assets.AEG110_181_9003,
        asset_1=0,
        obj_act_id=0,
        region=1042532406,
        left=1,
    )
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy4,
        character_1=Characters.LeyndellFootSoldier3,
        asset=Assets.AEG110_181_9004,
        asset_1=0,
        obj_act_id=0,
        region=1042532408,
        left=1,
    )
    CommonFunc_90005490(0, 1042530412, 1042530413, 1042531412, 0, 0, 1042532412, 1)

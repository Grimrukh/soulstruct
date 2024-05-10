"""
West Weeping Peninsula (NE) (SE)

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
from .enums.m60_43_34_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043340000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005461(0, character=1043340204)
    CommonFunc_90005462(1, character=1043340204)
    CommonFunc_90005460(0, character=1043340204)
    Event_1043342220(0, character=Characters.DemiHuman0, asset=1043341220, region=1043342220)
    Event_1043342220(1, character=Characters.DemiHuman1, asset=1043341221, region=1043342220)
    Event_1043342220(2, character=Characters.DemiHuman2, asset=1043341222, region=1043342220)
    Event_1043342220(3, character=Characters.DemiHuman3, asset=1043341223, region=1043342223)
    Event_1043342220(4, character=Characters.DemiHuman4, asset=1043341224, region=1043342223)
    Event_1043342220(5, character=1043340225, asset=1043341225, region=1043342223)
    CommonFunc_90005683(0, flag=62150, asset=Assets.AEG099_055_1001, vfx_id=210, flag_1=78196, flag_2=78196)
    CommonFunc_90005300(
        0,
        flag=1043340340,
        character=Characters.DemiHumanQueen,
        item_lot=1043340400,
        seconds=0.0,
        item_is_dropped=0,
    )
    CommonFunc_90005706(0, character=Characters.Commoner, animation_id=930025, left=Assets.AEG099_590_9000)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy0, flag=1043342700)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Commoner)
    CommonFunc_90005201(
        0,
        character=Characters.ErdtreeGuardian0,
        animation_id=30004,
        animation_id_1=20004,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeGuardian1,
        animation_id=30004,
        animation_id_1=20004,
        region=1043342212,
        radius=10.0,
        seconds=2.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeGuardian2,
        animation_id=30004,
        animation_id_1=20004,
        region=1043342212,
        radius=10.0,
        seconds=1.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeGuardian3,
        animation_id=30004,
        animation_id_1=20004,
        region=1043342212,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=1043340300, region=1043342300, seconds=0.0, animation_id=3031)


@RestartOnRest(1043342220)
def Event_1043342220(_, character: uint, asset: uint, region: uint):
    """Event 1043342220"""
    EnableAsset(asset)
    DisableCharacter(character)
    if FlagEnabled(1044342300):
        return
    AND_5.Add(CharacterDead(character))
    if AND_5:
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(1044342300)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableAsset(asset)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1043343700)
def Event_1043343700(_, character: uint):
    """Event 1043343700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023)
    End()

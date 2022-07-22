"""
West Weeping Peninsula (SE) (NE)

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
from .entities.m60_43_33_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=1043330000, asset=1043331950, enemy_block_distance=5.0, character=1043330480)
    CommonFunc_90005870(0, character=Characters.ErdtreeAvatar, name=904810600, npc_threat_level=18)
    CommonFunc_90005860(
        0,
        flag=1043330800,
        left=0,
        character=Characters.ErdtreeAvatar,
        left_1=0,
        item_lot__item_lot_param_id=30185,
        seconds=0.0,
    )
    CommonFunc_90005251(0, character=Characters.ErdtreeAvatar, radius=20.0, seconds=0.0, animation_id=0)
    CommonFunc_90005872(0, character=Characters.ErdtreeAvatar, npc_threat_level=18, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, model_point=800, right=1043338600)
    CommonFunc_90005550(0, flag=1043330530, asset=1043331530, obj_act_id=1043333530)
    Event_1043332270()
    Event_1043332270(slot=1)
    CommonFunc_90005724(
        0,
        flag=1043330290,
        character=1043330290,
        item_lot_param_id=70500,
        seconds=0.0,
        left=1,
        character_1=1043335291,
    )
    CommonFunc_90005722(0, character=1043330290, character_1=1043330291)
    CommonFunc_90005720(0, character=1043330290, character_1=1043330292, special_effect=10961, model_point=181)
    CommonFunc_90005720(0, character=1043330290, character_1=1043330293, special_effect=10961, model_point=182)
    CommonFunc_90005721(0, character=1043330290, character_1=1043330292)
    CommonFunc_90005721(0, character=1043330290, character_1=1043330293)
    CommonFunc_90005723(0, character=1043330290)
    Event_1043332230(0, character=Characters.Bat0, region=1043332230)
    Event_1043332230(1, character=Characters.Bat1, region=1043332230)
    Event_1043332230(2, character=Characters.Bat2, region=1043332230)
    Event_1043332230(3, character=Characters.Bat3, region=1043332233)
    Event_1043332230(4, character=Characters.Bat4, region=1043332233)
    Event_1043332230(5, character=Characters.Bat5, region=1043332233)
    Event_1043332230(6, character=Characters.Bat6, region=1043332233)
    Event_1043332230(7, character=Characters.Bat7, region=1043332233)
    Event_1043332230(8, character=Characters.Bat8, region=1043332233)
    Event_1043332230(9, character=Characters.Bat9, region=1043332233)
    Event_1043332230(10, character=Characters.Bat10, region=1043332233)
    Event_1043332230(11, character=Characters.Bat11, region=1043332233)
    CommonFunc_90005300(0, 1043330221, 1043330221, 40136, 0.0, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1043330050()
    CommonFunc_90005261(0, character=1043330210, region=1043332210, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1043330211, region=1043332211, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Rat0, radius=5.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=Characters.Rat1, region=1043332200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat2, region=1043332200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat3, region=1043332200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat4, region=1043332200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(0, 1043330250, 30000, 20000, 10.0, 0.0, 0, 0, 0, 0)


@ContinueOnRest(1043330050)
def Event_1043330050():
    """Event 1043330050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(1043330610)


@RestartOnRest(1043332230)
def Event_1043332230(_, character: uint, region: uint):
    """Event 1043332230"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AddSpecialEffect(character, 8080)


@RestartOnRest(1043332270)
def Event_1043332270():
    """Event 1043332270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1043332270))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101210,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101220,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101230,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101240,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101250,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101260,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043332271,
            model_point=900,
            behavior_id=802101270,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@ContinueOnRest(1043332650)
def Event_1043332650():
    """Event 1043332650"""
    CommonFunc_90005500(
        0,
        1043330650,
        1043330651,
        0,
        1043331650,
        1043331651,
        1043332651,
        1043331652,
        1043332652,
        1043332651,
        1043332652,
        1043330652,
        1043332653,
        0,
    )


@ContinueOnRest(1043330510)
def Event_1043330510():
    """Event 1043330510"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(1043330650)


@RestartOnRest(1043332520)
def Event_1043332520():
    """Event 1043332520"""
    RegisterLadder(start_climbing_flag=1043330530, stop_climbing_flag=1043330531, asset=1043331653)


@RestartOnRest(1043332680)
def Event_1043332680():
    """Event 1043332680"""
    MAIN.Await(FlagEnabled(1043338600))
    
    CreateAssetVFX(Assets.AEG099_090_9003, vfx_id=100, model_point=800)

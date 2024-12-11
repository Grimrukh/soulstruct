"""
Land of Shadow 12-10 SW SW

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
    Event_2048402200(0, owner_entity=2048400200, region=2048402200, source_entity=2048402201)
    Event_2048402200(1, owner_entity=2048400201, region=2048402200, source_entity=2048402202)
    CommonFunc_90005639(0, flag=2048400500, asset=2048401500, asset_1=2048401501, asset_2=2048401502, seconds=2.0)
    CommonFunc_90005790(
        0,
        right=0,
        flag=2048400180,
        summon_flag=2048402181,
        dismissal_flag=2048402182,
        character=2048400700,
        sign_type=23,
        region=2048402180,
        region_1=2048402181,
        seconds=0.0,
        right_1=2045429295,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2048400180, flag_1=2048402181, flag_2=2048402182, character=2048400700)
    CommonFunc_90005792(
        0,
        flag=2048400180,
        flag_1=2048402181,
        flag_2=2048402182,
        character=2048400700,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2048400180,
        flag_1=2048402181,
        flag_2=2048402182,
        character=2048400700,
        other_entity=2048402180,
        region=2048402182,
        left=0,
    )
    CommonFunc_90005774(0, flag=2048400180, item_lot=116401, flag_1=400645)
    CommonFunc_90005757(
        0,
        character=2048400710,
        character_1=2048400711,
        flag=4385,
        flag_1=4955,
        flag_2=2045422710,
        flag_3=4383,
    )
    CommonFunc_90005759(
        0,
        flag=2045429280,
        flag_1=4385,
        flag_2=4965,
        character=2048400710,
        flag_3=4955,
        flag_4=2045429295,
        first_flag=4950,
        last_flag=4956,
        flag_5=2045429281,
        flag_6=2045429282,
        flag_7=4901,
        seconds=1.0,
        flag_8=2045429345,
        radius=30.0,
    )
    CommonFunc_90005778(0, flag=2048412700, flag_1=4955, flag_2=400754, attacked_entity=2048400710)
    CommonFunc_90005779(0, character=2048400710, flag=4955, animation_id=20016, flag_1=4385, flag_2=4383)
    CommonFunc_90005744(0, entity=2048400710, flag=2048419200, flag_1=2048419200, animation_id=20015)
    CommonFunc_90005766(0, flag=2048402181, character=2048400700, distance=100.0, flag_1=2045429277, flag_2=4965)
    CommonFunc_90005767(
        0,
        flag=2045429280,
        first_flag=4380,
        last_flag=4383,
        character=2048400700,
        flag_1=4901,
        character_1=2048400701,
        flag_2=2045429297,
    )
    CommonFunc_90005777(0, character=2048400701, flag=4965, flag_1=4383, flag_2=2048402181)
    CommonFunc_90005774(0, flag=2045429297, item_lot=116401, flag_1=400645)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005271(0, character=2048400256, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=2048400250, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=2048400251, seconds=0.0, animation_id=-1)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005430(0, character=2248400200)
    CommonFunc_90005432(0, character=2248400200, flag=2248402200)
    CommonFunc_90005435(
        0,
        character=2248400200,
        flag=2248402201,
        flag_1=2248402202,
        flag_2=2248402203,
        flag_3=2248402204,
    )
    CommonFunc_90005433(0, character=2248400200, flag=2248402205, flag_1=2248402206, flag_2=2248402207)
    CommonFunc_90005434(0, character=2248400200, flag=2248402205, flag_1=2248402206, flag_2=2248402207)
    CommonFunc_90005437(0, character=2248400200, flag=2248402208, flag_1=2248402209)
    CommonFunc_90005301(0, flag=2048400200, character=2248400200, item_lot__unk1=2048400020, seconds=4.0, unk1=0)


@RestartOnRest(2048402200)
def Event_2048402200(_, owner_entity: uint, region: Region | int, source_entity: uint):
    """Event 2048402200"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    GotoIfFlagEnabled(Label.L0, flag=70)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308110,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308120,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308130,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308140,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308150,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308160,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804308170,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318110,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318120,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318130,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318140,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318150,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318160,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804318170,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()

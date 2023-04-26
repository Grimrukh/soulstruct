"""
Northwest Liurnia (NE) (SE)

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
from .enums.m60_35_50_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1035500002, asset=Assets.AEG099_060_9003)
    CommonFunc_90005100(
        0,
        flag=76214,
        flag_1=76214,
        asset=Assets.AEG099_090_9053,
        source_flag=77220,
        value=4,
        flag_2=78220,
        flag_3=78221,
        flag_4=78222,
        flag_5=78223,
        flag_6=78224,
        flag_7=78225,
        flag_8=78226,
        flag_9=78227,
        flag_10=78228,
        flag_11=78229,
    )
    RegisterGrace(grace_flag=1035500000, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=1035500001, asset=Assets.AEG099_060_9001)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=0)
    Event_1035502200(0, region=1035502700)
    CommonFunc_9005810(
        0,
        flag=1035500800,
        grace_flag=76232,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005300(0, flag=1035500322, character=Characters.Scarab1, item_lot=40220, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1035500320, character=Characters.Scarab0, item_lot=40250, seconds=0.0, left=0)
    Event_1035502580()
    CommonFunc_90005501(
        0,
        flag=1035500510,
        flag_1=1035500511,
        left=4,
        asset=Assets.AEG030_858_2002,
        asset_1=Assets.AEG099_026_2002,
        asset_2=Assets.AEG099_026_2000,
        flag_2=1035500512,
    )
    Event_1035502510()
    Event_1035502500()
    CommonFunc_90005511(0, flag=1035500560, asset=1035501560, obj_act_id=1035503560, obj_act_id_1=99020, left=0)
    CommonFunc_90005512(0, flag=1035500560, region=1035502560, region_1=1035502561)
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper0,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper1,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper2,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.LesserFingercreeper3, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper4,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper5,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=10.0,
        seconds=5.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper6,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper8,
        animation_id=30003,
        animation_id_1=20003,
        region=1035502222,
        radius=16.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper9,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=10.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper10,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=10.0,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper11,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=7.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper12,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper13,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=10.0,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper14,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=6.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper15,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=10.0,
        seconds=5.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.LesserFingercreeper16,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502200,
        radius=10.0,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper17,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper18,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper19,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper20,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper21,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper22,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper23,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LesserFingercreeper24,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot2,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot4,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot5,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot6,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallLivingPot7,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1035500284,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot0,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502299,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot1,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502291,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot2,
        animation_id=30000,
        animation_id_1=20000,
        region=1035502292,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=1035500303, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Page0, region=1035502311, radius=18.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Page1, region=1035502313, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Page2, region=1035502314, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BigWolf, region=1035502342, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper0,
        animation_id=30003,
        animation_id_1=20003,
        region=1035502350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.Fingercreeper2,
        animation_id=30003,
        animation_id_1=20003,
        region=1035502354,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.Fingercreeper3,
        animation_id=30003,
        animation_id_1=20003,
        region=1035502354,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper5,
        animation_id=30003,
        animation_id_1=20003,
        region=1035502356,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LargeCrabSnow, region=1035502390, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LiurniaTroll, region=1035502391, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.IronVirgin, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier0, region=1035502400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier1, region=1035502400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier2, region=1035502402, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier5, region=1035502409, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(
        0,
        character=Characters.RayaLucariaSoldier6,
        region=1035502410,
        radius=42.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier7, region=1035502411, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier8, region=1035502412, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier9, region=1035502412, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.RayaLucariaSoldier10,
        animation_id=30006,
        animation_id_1=20006,
        region=1035502414,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.RayaLucariaSoldier11, radius=17.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaSoldier12, region=1035502416, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(
        0,
        character=Characters.RayaLucariaSoldier17,
        region=1035502410,
        radius=40.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_1035502401()
    Event_1035502400(0, character=Characters.RayaLucariaSoldier3, region=1035502407, seconds=0.0, animation_id=-1)
    Event_1035502400(1, character=Characters.RayaLucariaSoldier4, region=1035502407, seconds=0.0, animation_id=-1)
    Event_1035502400(2, character=Characters.RayaLucariaSoldier13, region=1035502419, seconds=0.0, animation_id=-1)
    Event_1035502400(3, character=Characters.RayaLucariaSoldier14, region=1035502420, seconds=0.0, animation_id=-1)
    Event_1035502400(4, character=Characters.RayaLucariaSoldier15, region=1035502420, seconds=0.0, animation_id=-1)
    Event_1035502400(5, character=Characters.RayaLucariaSoldier16, region=1035502422, seconds=0.0, animation_id=-1)
    Event_1035502400(6, character=Characters.RayaLucariaSoldier18, region=1035502422, seconds=5.0, animation_id=-1)
    Event_1035502400(7, character=Characters.RayaLucariaSoldier19, region=1035502425, seconds=0.0, animation_id=-1)
    Event_1035502400(8, character=Characters.RayaLucariaSoldier20, region=1035502420, seconds=0.0, animation_id=-1)
    Event_1035502400(9, character=Characters.RayaLucariaSoldier21, region=1035502419, seconds=0.0, animation_id=-1)
    Event_1035502400(10, character=Characters.RayaLucariaSoldier22, region=1035502420, seconds=0.0, animation_id=-1)
    Event_1035502849()
    Event_1035500800()
    Event_1035502810()
    Event_1035502840()
    Event_1035502841()
    Event_1035502842()
    Event_1035502210(0, asset=1035501600, flag=1035502600, owner_entity=Characters.Dummy)
    Event_1035502210(1, asset=1035501601, flag=1035502601, owner_entity=Characters.Dummy)
    Event_1035502210(2, asset=1035501602, flag=1035502602, owner_entity=Characters.Dummy)
    Event_1035502210(3, asset=1035501603, flag=1035502603, owner_entity=Characters.Dummy)
    Event_1035502210(4, asset=1035501604, flag=1035502604, owner_entity=Characters.Dummy)
    Event_1035502210(5, asset=1035501605, flag=1035502605, owner_entity=Characters.Dummy)
    Event_1035502210(6, asset=1035501606, flag=1035502606, owner_entity=Characters.Dummy)
    Event_1035502210(7, asset=1035501608, flag=1035502608, owner_entity=Characters.Dummy)
    Event_1035500700(
        0,
        character=Characters.AlbinauricLookout0,
        character_1=Characters.RayaLucariaSoldier23,
        character_2=Characters.RayaLucariaSoldier25,
        character_3=Characters.RayaLucariaSoldier27,
        asset=Assets.AEG110_302_2208,
    )
    Event_1035500701(
        0,
        character=Characters.AlbinauricLookout1,
        character_1=Characters.RayaLucariaSoldier24,
        character_2=Characters.RayaLucariaSoldier26,
        character_3=Characters.RayaLucariaSoldier28,
        asset=Assets.AEG099_428_9000,
    )
    Event_1035500702()
    Event_1035500703(0, flag=1035502705, region=1035502720)
    Event_1035500703(1, flag=1035502706, region=1035502721)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4110,
        item_lot=101490,
        first_flag=400149,
        last_flag=400149,
        flag=1035509215,
        model_point=0,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4110,
        item_lot=101495,
        first_flag=400149,
        last_flag=400149,
        flag=1035509216,
        model_point=0,
    )
    CommonFunc_90005706(0, character=Characters.CariaManorSilentSpirit, animation_id=90102, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.AlbinauricLookout0)
    DisableBackread(Characters.AlbinauricLookout1)
    DisableBackread(Characters.RayaLucariaSoldier23)
    DisableBackread(Characters.RayaLucariaSoldier24)
    DisableBackread(Characters.RayaLucariaSoldier25)
    DisableBackread(Characters.RayaLucariaSoldier26)
    DisableBackread(Characters.RayaLucariaSoldier27)
    DisableBackread(Characters.RayaLucariaSoldier28)
    DisableBackread(Characters.CariaManorSilentSpirit)
    EnableAssetInvulnerability(Assets.AEG110_302_2208)
    Event_1035502514()


@RestartOnRest(1035502200)
def Event_1035502200(_, region: uint):
    """Event 1035502200"""
    DisableNetworkSync()
    Wait(0.10000000149011612)
    AND_1.Add(CharacterInsideRegion(character=20000, region=region))
    OR_1.Add(Invasion())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    OR_2.Add(CharacterOutsideRegion(character=20000, region=region))
    OR_2.Add(Invasion())
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(1035502210)
def Event_1035502210(_, asset: uint, flag: uint, owner_entity: uint):
    """Event 1035502210"""
    if FlagEnabled(flag):
        return
    if AssetDestroyed(asset):
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_2.Add(EntityWithinDistance(entity=asset, other_entity=20000, radius=2.0))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DestroyAsset(asset, request_slot=0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    End()


@RestartOnRest(1035502401)
def Event_1035502401():
    """Event 1035502401"""
    EnableNetworkSync()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1035502499))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1035502499)


@RestartOnRest(1035502400)
def Event_1035502400(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 1035502400"""
    EnableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(FlagEnabled(1035502499))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(AND_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@ContinueOnRest(1035502510)
def Event_1035502510():
    """Event 1035502510"""
    CommonFunc_90005500(
        0,
        flag=1035500510,
        flag_1=1035500511,
        left=4,
        asset=Assets.AEG030_858_2002,
        asset_1=Assets.AEG099_026_2002,
        obj_act_id=1035503511,
        asset_2=Assets.AEG099_026_2000,
        obj_act_id_1=1035503512,
        region=1035502511,
        region_1=1035502512,
        flag_2=1035500512,
        flag_3=1035500513,
        left_1=0,
    )


@ContinueOnRest(1035502514)
def Event_1035502514():
    """Event 1035502514"""
    if FlagEnabled(1035500514):
        return
    EnableFlag(1035500514)
    DisableFlag(1035500510)


@ContinueOnRest(1035502580)
def Event_1035502580():
    """Event 1035502580"""
    RegisterLadder(start_climbing_flag=1035500580, stop_climbing_flag=1035500581, asset=Assets.AEG030_822_2001)
    RegisterLadder(start_climbing_flag=1035500582, stop_climbing_flag=1035500583, asset=Assets.AEG030_003_2001)
    RegisterLadder(start_climbing_flag=1035500584, stop_climbing_flag=1035500585, asset=Assets.AEG030_888_2000)
    RegisterLadder(start_climbing_flag=1035500586, stop_climbing_flag=1035500587, asset=1035501586)


@RestartOnRest(1035502500)
def Event_1035502500():
    """Event 1035502500"""
    DisableAsset(1035501200)
    DisableAsset(1035501201)
    DisableAsset(1035506400)


@RestartOnRest(1035500800)
def Event_1035500800():
    """Event 1035500800"""
    if FlagEnabled(1035500800):
        return
    
    MAIN.Await(HealthValue(Characters.Loretta) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Loretta, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Loretta))
    
    KillBossAndDisplayBanner(character=Characters.Loretta, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(1035500800)
    EnableFlag(9181)
    if PlayerInOwnWorld():
        EnableFlag(61181)


@RestartOnRest(1035502810)
def Event_1035502810():
    """Event 1035502810"""
    GotoIfFlagDisabled(Label.L0, flag=1035500800)
    DisableCharacter(Characters.Loretta)
    DisableAnimations(Characters.Loretta)
    Kill(Characters.Loretta)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Loretta)
    GotoIfFlagEnabled(Label.L1, flag=1035500801)
    DisableCharacter(Characters.Loretta)
    ForceAnimation(Characters.Loretta, 30000, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1035502801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Loretta, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(1035500801)
    EnableCharacter(Characters.Loretta)
    ForceAnimation(Characters.Loretta, 20010, skip_transition=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1035502800))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1035502802))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1035502805))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Loretta)
    SetNetworkUpdateRate(Characters.Loretta, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Loretta, name=903253500)


@RestartOnRest(1035502840)
def Event_1035502840():
    """Event 1035502840"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1035500800):
        return
    AND_1.Add(CharacterInsideRegion(character=Characters.Loretta, region=1035502840))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1035502841))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1035502842))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1035502843))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1035502844))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1035502845))
    AND_1.Add(FlagDisabled(1035502821))
    AND_1.Add(FlagDisabled(1035502822))
    AND_1.Add(FlagDisabled(1035502823))
    AND_1.Add(FlagDisabled(1035502824))
    AND_1.Add(FlagDisabled(1035502825))
    AND_1.Add(FlagDisabled(1035502826))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=1035502841)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=1035502842)
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=1035502843)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=1035502844)
    GotoIfCharacterInsideRegion(Label.L4, character=PLAYER, region=1035502845)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(1035502839):
        EnableNetworkFlag(1035502822)
    if FlagDisabled(1035502839):
        EnableNetworkFlag(1035502824)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1035502839):
        EnableNetworkFlag(1035502821)
    if FlagDisabled(1035502839):
        EnableNetworkFlag(1035502823)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    if FlagEnabled(1035502839):
        EnableNetworkFlag(1035502825)
    if FlagDisabled(1035502839):
        EnableNetworkFlag(1035502826)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@RestartOnRest(1035502841)
def Event_1035502841():
    """Event 1035502841"""
    if FlagEnabled(1035500800):
        return
    OR_1.Add(FlagEnabled(1035502821))
    OR_1.Add(FlagEnabled(1035502822))
    OR_1.Add(FlagEnabled(1035502823))
    OR_1.Add(FlagEnabled(1035502824))
    OR_1.Add(FlagEnabled(1035502825))
    OR_1.Add(FlagEnabled(1035502826))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(Characters.Loretta, 13806)
    DisableAnimations(Characters.Loretta)
    Wait(1.0)
    GotoIfFlagEnabled(Label.L1, flag=1035502821)
    GotoIfFlagEnabled(Label.L2, flag=1035502822)
    GotoIfFlagEnabled(Label.L3, flag=1035502823)
    GotoIfFlagEnabled(Label.L4, flag=1035502824)
    GotoIfFlagEnabled(Label.L5, flag=1035502825)
    GotoIfFlagEnabled(Label.L6, flag=1035502826)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(Characters.Loretta, destination=1035502821, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(Characters.Loretta, destination=1035502822, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(Characters.Loretta, destination=1035502823, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    Move(Characters.Loretta, destination=1035502824, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(Characters.Loretta, destination=1035502825, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 6 --- #
    DefineLabel(6)
    Move(Characters.Loretta, destination=1035502826, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableAnimations(Characters.Loretta)
    RemoveSpecialEffect(Characters.Loretta, 13806)
    ForceAnimation(Characters.Loretta, 20010)
    Wait(1.0)
    if PlayerInOwnWorld():
        DisableNetworkFlag(1035502821)
        DisableNetworkFlag(1035502822)
        DisableNetworkFlag(1035502823)
        DisableNetworkFlag(1035502824)
        DisableNetworkFlag(1035502825)
        DisableNetworkFlag(1035502826)
    Restart()


@RestartOnRest(1035502842)
def Event_1035502842():
    """Event 1035502842"""
    if FlagEnabled(1035500800):
        return
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(1035502810))
    
    EnableNetworkFlag(1035502839)
    Wait(3.0)
    DisableNetworkFlag(1035502839)
    Wait(5.0)
    EnableNetworkFlag(1035502839)
    Wait(4.0)
    DisableNetworkFlag(1035502839)
    Wait(1.0)
    EnableNetworkFlag(1035502839)
    Wait(6.0)
    DisableNetworkFlag(1035502839)
    Wait(7.0)
    Restart()


@RestartOnRest(1035502849)
def Event_1035502849():
    """Event 1035502849"""
    CommonFunc_9005800(
        0,
        flag=1035500800,
        entity=Assets.AEG099_003_9000,
        region=1035502800,
        flag_1=1035502805,
        character=1035505800,
        action_button_id=10000,
        left=1035500801,
        region_1=1035502801,
    )
    CommonFunc_9005801(
        0,
        flag=1035500800,
        entity=Assets.AEG099_003_9000,
        region=1035502800,
        flag_1=1035502805,
        flag_2=1035502806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1035500800, asset=Assets.AEG099_003_9000, model_point=3, right=1035500801)
    CommonFunc_9005813(0, flag=1035500800, asset=Assets.AEG099_003_9001, model_point=3, right=0, model_point_1=3)
    CommonFunc_9005822(
        0,
        flag=1035500800,
        bgm_boss_conv_param_id=920200,
        flag_1=1035502805,
        flag_2=1035502806,
        right=1035500801,
        flag_3=0,
        left=0,
        left_1=0,
    )


@RestartOnRest(1035500700)
def Event_1035500700(_, character: uint, character_1: uint, character_2: uint, character_3: uint, asset: uint):
    """Event 1035500700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
    if FlagEnabled(1035509205):
        EnableRandomFlagInRange(flag_range=(1035502700, 1035502702))
    else:
        EnableNetworkFlag(1035502701)
    if FlagEnabled(1035509202):
        DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
        EnableNetworkFlag(1035502700)
    if FlagEnabled(1035509203):
        DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
        EnableNetworkFlag(1035502701)
    if FlagEnabled(1035509204):
        DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
        EnableNetworkFlag(1035502702)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=3565)
    GotoIfFlagEnabled(Label.L6, flag=3566)
    GotoIfFlagEnabled(Label.L7, flag=3567)
    GotoIfFlagEnabled(Label.L8, flag=3568)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableAssetInvulnerability(asset)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3565, 3568)))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)

    # --- Label 6 --- #
    DefineLabel(6)

    # --- Label 7 --- #
    DefineLabel(7)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(character)
    EnableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    ForceAnimation(character_1, 930010)
    ForceAnimation(character_2, 930010)
    ForceAnimation(character_3, 930010)
    EnableAssetInvulnerability(asset)
    RestoreAsset(asset)
    if FlagEnabled(1035502700):
        ForceAnimation(character, 930024)
    if FlagEnabled(1035502701):
        ForceAnimation(character, 930026)
    if FlagEnabled(1035502702):
        ForceAnimation(character, 930028)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(3565, 3568)))
    
    Restart()


@RestartOnRest(1035500701)
def Event_1035500701(_, character: uint, character_1: uint, character_2: uint, character_3: uint, asset: uint):
    """Event 1035500701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3569)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(3569))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableCharacter(character)
    EnableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    EnableAsset(asset)
    ForceAnimation(character_1, 930009)
    ForceAnimation(character_2, 930009)
    ForceAnimation(character_3, 930009)
    ForceAnimation(character, 30019)
    SetCharacterTalkRange(character=character, distance=100.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3569))
    
    Restart()


@RestartOnRest(1035500702)
def Event_1035500702():
    """Event 1035500702"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(1035509208)
    AND_1.Add(EventValue(flag=67470, bit_count=8) >= 1)
    AND_1.Add(EventValue(flag=66450, bit_count=8) >= 1)
    AND_1.Add(EventValue(flag=130290, bit_count=8) >= 3)
    AND_1.Add(EventValue(flag=130300, bit_count=8) >= 2)
    AND_1.Add(EventValue(flag=130340, bit_count=8) >= 1)
    AND_1.Add(EventValue(flag=130350, bit_count=8) >= 1)
    AND_1.Add(EventValue(flag=130360, bit_count=8) >= 1)
    AND_1.Add(EventValue(flag=130370, bit_count=8) >= 2)
    AND_1.Add(EventValue(flag=130380, bit_count=8) >= 1)
    AND_1.Add(EventValue(flag=130390, bit_count=8) >= 1)
    AND_1.Add(EventValue(flag=69900, bit_count=8) >= 1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(1035509208)
    End()


@RestartOnRest(1035500703)
def Event_1035500703(_, flag: uint, region: uint):
    """Event 1035500703"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(3569))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)

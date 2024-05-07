"""
West Altus Plateau (NW) (SW)

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
from .enums.m60_36_54_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(1, grace_flag=76352, asset=Assets.AEG099_060_9000, enemy_block_distance=5.0, character=0)
    CommonFunc_90005100(
        0,
        flag=71602,
        flag_1=76352,
        asset=Assets.AEG099_060_9002,
        source_flag=77350,
        value=3,
        flag_2=78350,
        flag_3=78351,
        flag_4=78352,
        flag_5=78353,
        flag_6=78354,
        flag_7=78355,
        flag_8=78356,
        flag_9=78357,
        flag_10=78358,
        flag_11=78359,
    )
    CommonFunc_90005600(2, grace_flag=76353, asset=Assets.AEG099_060_9001, enemy_block_distance=5.0, character=0)
    CommonFunc_90005261(
        0,
        character=Characters.FallingstarBeast,
        region=1036542805,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_FieldBattleHealthBar(0, boss=Characters.FallingstarBeast, name=904680603, npc_threat_level=19)
    CommonFunc_90005860(
        0,
        flag=1036540800,
        left=0,
        character=Characters.FallingstarBeast,
        left_1=0,
        item_lot=30375,
        seconds=0.0,
    )
    Event_1036542350(0, region=1036542450, special_effect=16488, special_effect_1=16489)
    CommonFunc_90005300(0, flag=1036540498, character=Characters.Scarab, item_lot=40334, seconds=0.0, item_is_dropped=0)
    CommonFunc_90005261(
        0,
        character=Characters.Marionette0,
        region=1036542210,
        radius=5.0,
        seconds=0.30000001192092896,
        animation_id=0,
    )
    CommonFunc_90005261(
        2,
        character=Characters.Marionette8,
        region=1036542210,
        radius=5.0,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Marionette5, region=1036542220, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Marionette2, region=1036542425, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(1, character=Characters.Marionette7, region=1036542425, seconds=2.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Avionette, region=1036542414, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Marionette3,
        animation_id=30010,
        animation_id_1=20010,
        region=1036542410,
        radius=10.0,
        seconds=7.099999904632568,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Marionette4,
        animation_id=30010,
        animation_id_1=20010,
        region=1036542410,
        radius=10.0,
        seconds=7.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        2,
        character=Characters.Marionette9,
        animation_id=30010,
        animation_id_1=20010,
        region=1036542410,
        radius=10.0,
        seconds=7.199999809265137,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        3,
        character=Characters.Marionette6,
        animation_id=30010,
        animation_id_1=20010,
        region=1036542410,
        radius=10.0,
        seconds=7.5,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        4,
        character=Characters.Troll,
        animation_id=30000,
        animation_id_1=20000,
        region=1036542410,
        radius=5.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.LeyndellSoldier, region=1036542305, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(1, character=Characters.LeyndellFootSoldier0, region=1036542305, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(2, character=Characters.LeyndellFootSoldier1, region=1036542305, seconds=0.0, animation_id=-1)
    CommonFunc_90005391(
        0,
        flag=1036540350,
        flag_1=1036542350,
        character=Characters.PutridCorpse,
        character_1=Characters.WormfaceLarge,
        left=1,
    )
    Event_1036542250(
        0,
        flag=1036540350,
        flag_1=1036542350,
        anchor_entity=Characters.PutridCorpse,
        character=Characters.WormfaceLarge,
        left=1,
        item_lot=1036540100,
    )
    Event_1036542580()
    Event_1036542240(0, asset=1036541200, entity=1036541201, flag=82032)
    Event_1036542301()
    Event_1036542300(0, source_entity=Assets.AEG099_048_9001, seconds=0.800000011920929)
    Event_1036542300(1, source_entity=Assets.AEG099_048_9002, seconds=0.0)
    Event_1036542300(2, source_entity=Assets.AEG099_048_9003, seconds=4.400000095367432)
    Event_1036542300(3, source_entity=Assets.AEG099_048_9004, seconds=1.100000023841858)
    Event_1036542300(4, source_entity=Assets.AEG099_048_9005, seconds=6.0)
    Event_1036542300(5, source_entity=Assets.AEG099_048_9006, seconds=7.0)
    Event_1036542300(6, source_entity=Assets.AEG099_048_9007, seconds=1.0)
    Event_1036542300(7, source_entity=Assets.AEG099_048_9008, seconds=1.5)
    Event_1036542300(8, source_entity=1036541308, seconds=3.5999999046325684)
    Event_1036542300(9, source_entity=1036541309, seconds=5.0)
    Event_1036542300(10, source_entity=1036541310, seconds=3.5)
    Event_1036542300(11, source_entity=1036541311, seconds=6.0)
    Event_1036542300(12, source_entity=1036541312, seconds=4.0)
    Event_1036542300(13, source_entity=1036541313, seconds=4.099999904632568)
    Event_1036542300(14, source_entity=1036541314, seconds=7.400000095367432)
    Event_1036542300(15, source_entity=1036541315, seconds=4.400000095367432)
    Event_1036542300(16, source_entity=1036541316, seconds=6.5)
    Event_1036542300(17, source_entity=1036541317, seconds=7.599999904632568)
    Event_1036542300(18, source_entity=1036541318, seconds=6.599999904632568)
    Event_1036542300(19, source_entity=1036541319, seconds=7.0)
    Event_1036542300(20, source_entity=1036541320, seconds=7.099999904632568)
    Event_1036542300(21, source_entity=1036541321, seconds=7.5)
    Event_1036542300(22, source_entity=Assets.AEG099_048_9000, seconds=0.30000001192092896)
    Event_1036542300(23, source_entity=1036541323, seconds=4.199999809265137)
    Event_1036542300(24, source_entity=1036541324, seconds=0.0)
    Event_1036542300(25, source_entity=1036541325, seconds=1.0)
    Event_1036542500()
    Event_1036542450(0, asset=Assets.AEG007_434_9000)
    Event_1036542450(1, asset=Assets.AEG007_434_9001)
    Event_1036542450(2, asset=Assets.AEG007_434_9002)
    Event_1036542450(3, asset=Assets.AEG007_434_9003)
    Event_1036542450(4, asset=Assets.AEG007_434_9004)
    Event_1036542450(5, asset=Assets.AEG007_434_9005)
    Event_1036542450(6, asset=Assets.AEG007_434_9006)
    Event_1036542450(7, asset=Assets.AEG007_434_9007)
    Event_1036542450(8, asset=Assets.AEG007_434_9008)
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930021, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble)


@ContinueOnRest(1036542580)
def Event_1036542580():
    """Event 1036542580"""
    RegisterLadder(start_climbing_flag=1036540580, stop_climbing_flag=1036540851, asset=Assets.AEG004_183_1001)


@RestartOnRest(1036542200)
def Event_1036542200(_, character: uint):
    """Event 1036542200"""
    Kill(character)
    End()


@RestartOnRest(1036542240)
def Event_1036542240(_, asset: uint, entity: uint, flag: uint):
    """Event 1036542240"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateAssetVFX(asset, vfx_id=200, dummy_id=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1036542250)
def Event_1036542250(_, flag: uint, flag_1: uint, anchor_entity: uint, character: uint, left: int, item_lot: int):
    """Event 1036542250"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        dummy_id=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        dummy_id=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(5.0)
    DisableCharacter(character)
    if PlayerNotInOwnWorld():
        return
    if ValueNotEqual(left=item_lot, right=0):
        AwardItemLot(item_lot, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(1036542400)
def Event_1036542400(_, character: uint, region: uint, seconds: float):
    """Event 1036542400"""
    DisableAI(character)
    DisableGravity(character)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    Wait(seconds)
    ForceAnimation(character, 3032, wait_for_completion=True)
    EnableAI(character)
    Wait(2.799999952316284)
    EnableGravity(character)
    End()


@RestartOnRest(1036542450)
def Event_1036542450(_, asset: uint):
    """Event 1036542450"""
    DisableAsset(asset)
    End()


@ContinueOnRest(1036542500)
def Event_1036542500():
    """Event 1036542500"""
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542350,
            asset=Assets.AEG007_557_1000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542351,
            asset=Assets.AEG007_557_1001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542352,
            asset=Assets.AEG007_557_1002,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542353,
            asset=Assets.AEG007_557_1003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542354,
            asset=Assets.AEG007_557_1004,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542355,
            asset=Assets.AEG007_557_1005,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542356,
            asset=Assets.AEG007_557_1006,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542357,
            asset=Assets.AEG007_557_1007,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036542358,
            asset=Assets.AEG007_557_1008,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )


@RestartOnRest(1036542300)
def Event_1036542300(_, source_entity: uint, seconds: float):
    """Event 1036542300"""
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=70.0))
    
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    Wait(seconds)
    EnableThisSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803210,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803220,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803230,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803240,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803250,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803260,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=802803270,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(8.0)
    RestartIfConditionTrue(input_condition=MAIN)


@RestartOnRest(1036542301)
def Event_1036542301():
    """Event 1036542301"""
    CreateProjectileOwner(entity=Characters.Dummy)


@RestartOnRest(1036542350)
def Event_1036542350(_, region: uint, special_effect: int, special_effect_1: int):
    """Event 1036542350"""
    if FlagEnabled(1036540800):
        return
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(20000, special_effect)
    Wait(0.10000000149011612)
    AND_2.Add(CharacterOutsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_2)
    
    Wait(0.10000000149011612)
    AddSpecialEffect(20000, special_effect_1)
    Restart()


@RestartOnRest(1036542800)
def Event_1036542800():
    """Event 1036542800"""
    if FlagEnabled(1036540800):
        return
    DisableAI(Characters.FallingstarBeast)
    DisableCharacter(Characters.FallingstarBeast)
    GotoIfFlagEnabled(Label.L0, flag=1036540805)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1036542800))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9000, entity=Assets.AEG003_316_9001))
    
    MAIN.Await(AND_1)
    
    DisableAsset(Assets.AEG003_316_9001)
    EnableCharacter(Characters.FallingstarBeast)
    ForceAnimation(Characters.FallingstarBeast, 20016, wait_for_completion=True)
    EnableAI(Characters.FallingstarBeast)
    SetNetworkUpdateRate(Characters.FallingstarBeast, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=1036542800))
    
    DisableAI(Characters.FallingstarBeast)
    ForceAnimation(Characters.FallingstarBeast, 3030, loop=True, wait_for_completion=True, skip_transition=True)
    Wait(3.4000000953674316)
    Move(
        Characters.FallingstarBeast,
        destination=1036542801,
        destination_type=CoordEntityType.Region,
        dummy_id=0,
        short_move=True,
    )
    DisableCharacter(Characters.FallingstarBeast)
    EnableNetworkFlag(1036540805)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1036542802))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1036542800))
    
    MAIN.Await(AND_2)
    
    Move(
        Characters.FallingstarBeast,
        destination=1036542801,
        destination_type=CoordEntityType.Region,
        dummy_id=0,
        short_move=True,
    )
    Wait(3.0)
    EnableCharacter(Characters.FallingstarBeast)
    ForceAnimation(Characters.FallingstarBeast, 20016, wait_for_completion=True)
    EnableAI(Characters.FallingstarBeast)
    SetNetworkUpdateRate(Characters.FallingstarBeast, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=1036542800))
    
    DisableAI(Characters.FallingstarBeast)
    ForceAnimation(Characters.FallingstarBeast, 3030, loop=True, wait_for_completion=True, skip_transition=True)
    Wait(3.4000000953674316)
    Move(
        Characters.FallingstarBeast,
        destination=1036542801,
        destination_type=CoordEntityType.Region,
        dummy_id=0,
        short_move=True,
    )
    DisableCharacter(Characters.FallingstarBeast)
    Restart()


@RestartOnRest(1036542801)
def Event_1036542801():
    """Event 1036542801"""
    if FlagEnabled(1036540800):
        return
    
    MAIN.Await(HealthValue(Characters.FallingstarBeast) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.FallingstarBeast, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.FallingstarBeast))
    
    KillBossAndDisplayBanner(character=Characters.FallingstarBeast, banner_type=BannerType.EnemyFelled)
    EnableFlag(1036540800)


@RestartOnRest(1036542810)
def Event_1036542810():
    """Event 1036542810"""
    GotoIfFlagDisabled(Label.L0, flag=1036540800)
    DisableCharacter(Characters.FallingstarBeast)
    DisableAnimations(Characters.FallingstarBeast)
    Kill(Characters.FallingstarBeast)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.FallingstarBeast)
    DisableCharacter(Characters.FallingstarBeast)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1036542800))
    
    EnableCharacter(Characters.FallingstarBeast)
    ForceAnimation(Characters.FallingstarBeast, 20016, wait_for_completion=True)
    EnableAI(Characters.FallingstarBeast)
    SetNetworkUpdateRate(Characters.FallingstarBeast, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableNetworkFlag(1036540801)


@RestartOnRest(1036542849)
def Event_1036542849():
    """Event 1036542849"""
    CommonFunc_9005822(
        0,
        flag=1036540800,
        bgm_boss_conv_param_id=90003101,
        flag_1=0,
        flag_2=0,
        right=0,
        flag_3=0,
        left=0,
        left_1=0,
    )

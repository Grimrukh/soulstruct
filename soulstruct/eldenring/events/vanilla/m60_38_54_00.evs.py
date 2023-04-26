"""
West Altus Plateau (NE) (SW)

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
from .enums.m60_38_54_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(
        0,
        grace_flag=1038540000,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
        character=1038540480,
    )
    CommonFunc_90005100(
        0,
        flag=71602,
        flag_1=76351,
        asset=Assets.AEG099_060_9001,
        source_flag=77350,
        value=2,
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
    CommonFunc_90005870(0, character=1038540800, name=904680601, npc_threat_level=19)
    CommonFunc_90005860(0, flag=1038540800, left=1038540800, character=1038540800, left_1=0, item_lot=0, seconds=0.0)
    CommonFunc_90005250(0, character=Characters.Dog, region=1038542229, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(1, character=1038540227, region=1038542229, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(2, character=Characters.SmallerDog1, region=1038542229, seconds=6.0, animation_id=-1)
    Event_1038542260(0, character=Characters.Dog)
    Event_1038542260(1, character=1038540227)
    Event_1038542260(2, character=Characters.SmallerDog1)
    CommonFunc_90005261(
        0,
        character=Characters.SmallerDog0,
        region=1038542220,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        1,
        character=Characters.SmallerDog2,
        region=1038542220,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=1038540410,
        summon_flag=1038542410,
        dismissal_flag=1038542411,
        character=Characters.AnastasiaTarnishedEater,
        sign_type=22,
        region=1038542701,
        region_1=1038542700,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(
        0,
        flag=1038540410,
        flag_1=1038542410,
        flag_2=1038542411,
        character=Characters.AnastasiaTarnishedEater,
    )
    CommonFunc_90005792(
        0,
        flag=1038540410,
        flag_1=1038542410,
        flag_2=1038542411,
        character=Characters.AnastasiaTarnishedEater,
        item_lot=1038540700,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1038540410,
        flag_1=1038542410,
        flag_2=1038542411,
        character=Characters.AnastasiaTarnishedEater,
        other_entity=1038542701,
        region=1038542702,
        left=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellFootSoldier2,
        region=1038542370,
        radius=5.0,
        seconds=3.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        1,
        character=Characters.LeyndellFootSoldier3,
        region=1038542370,
        radius=5.0,
        seconds=3.0999999046325684,
        animation_id=-1,
    )
    CommonFunc_90005261(
        2,
        character=Characters.LeyndellFootSoldier1,
        region=1038542370,
        radius=5.0,
        seconds=3.200000047683716,
        animation_id=-1,
    )
    Event_1038542270(0, character=Characters.LeyndellFootSoldier2)
    Event_1038542270(1, character=Characters.LeyndellFootSoldier3)
    Event_1038542270(2, character=Characters.LeyndellFootSoldier1)
    CommonFunc_90005261(0, character=Characters.Eagle2, region=1038542380, radius=5.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(1, character=Characters.Eagle0, region=1038542381, radius=5.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(2, character=Characters.Eagle3, region=1038542382, radius=5.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(3, character=Characters.Eagle1, region=1038542383, radius=5.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(4, character=Characters.Eagle4, region=1038542384, radius=5.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(5, character=Characters.Eagle5, region=1038542385, radius=5.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005211(
        4,
        character=Characters.MadPumpkinHead,
        animation_id=30005,
        animation_id_1=20005,
        region=1038542370,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540211,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier2,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier1,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540268,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier9,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier10,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier11,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier12,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier13,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier0,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier4,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier5,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier6,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier7,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier8,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540280,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540281,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540282,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540283,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540284,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540285,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540286,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540287,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540288,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540289,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540290,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540291,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540292,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540294,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540295,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540296,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540297,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1038540298,
        animation_id=30007,
        animation_id_1=20007,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellFootSoldier0,
        animation_id=30010,
        animation_id_1=20010,
        region=1038542205,
        radius=10.0,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=1038540206,
        animation_id=30010,
        animation_id_1=20010,
        region=1038542205,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038542250(0, attacker__character=1038545200, region=1038542200)
    CommonFunc_90005261(0, character=1038540340, region=1039532350, radius=10.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(1, character=1038540341, region=1039532350, radius=10.0, seconds=0.0, animation_id=-1)
    Event_1038542340()
    CommonFunc_90005251(0, character=Characters.LeyndellSoldier3, radius=8.0, seconds=0.0, animation_id=-1)
    Event_1038542580()
    CommonFunc_90005300(
        0,
        flag=1038540400,
        character=Characters.MaleighMarais,
        item_lot=1038540100,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.GuardianGolem,
        animation_id=30020,
        animation_id_1=20020,
        region=1038542390,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038542400()
    Event_1038542500()
    Event_1038542450(0, asset=Assets.AEG007_434_9000)
    Event_1038542450(1, asset=Assets.AEG007_434_9001)
    Event_1038542450(2, asset=Assets.AEG007_434_9002)
    Event_1038542450(3, asset=Assets.AEG007_434_9003)


@ContinueOnRest(1038542580)
def Event_1038542580():
    """Event 1038542580"""
    RegisterLadder(start_climbing_flag=1038540580, stop_climbing_flag=1038540581, asset=Assets.AEG004_183_1000)
    RegisterLadder(start_climbing_flag=1038540582, stop_climbing_flag=1038540583, asset=Assets.AEG110_182_1000)
    RegisterLadder(start_climbing_flag=1038540584, stop_climbing_flag=1038540585, asset=Assets.AEG110_182_1001)
    RegisterLadder(start_climbing_flag=1038540586, stop_climbing_flag=1038540587, asset=Assets.AEG110_183_1000)
    RegisterLadder(start_climbing_flag=1038540588, stop_climbing_flag=1038540589, asset=Assets.AEG110_184_1000)
    RegisterLadder(start_climbing_flag=1038540590, stop_climbing_flag=1038540591, asset=Assets.AEG110_184_1001)


@RestartOnRest(1038542250)
def Event_1038542250(_, attacker__character: uint, region: uint):
    """Event 1038542250"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5660)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1050562200):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5660)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=35000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000, attacker=attacker__character))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=attacker__character, state_info=260))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=35000, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=35000, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1050562200)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5660)


@RestartOnRest(1038542260)
def Event_1038542260(_, character: uint):
    """Event 1038542260"""
    AddSpecialEffect(character, 8087)
    End()


@RestartOnRest(1038542270)
def Event_1038542270(_, character: uint):
    """Event 1038542270"""
    AddSpecialEffect(character, 8092)
    End()


@RestartOnRest(1038542340)
def Event_1038542340():
    """Event 1038542340"""
    MAIN.Await(CharacterInsideRegion(character=1038540340, region=1038542340))
    
    ChangePatrolBehavior(1038540340, patrol_information_id=1038543340)
    End()


@RestartOnRest(1038542400)
def Event_1038542400():
    """Event 1038542400"""
    OR_1.Add(CharacterDead(Characters.MaleighMarais))
    OR_1.Add(CharacterDead(Characters.GuardianGolem))
    if OR_1:
        return
    SetTeamType(Characters.MaleighMarais, TeamType.ArchEnemyTeam)
    SetTeamType(Characters.GuardianGolem, TeamType.ArchEnemyTeam)
    End()


@RestartOnRest(1038542450)
def Event_1038542450(_, asset: uint):
    """Event 1038542450"""
    DisableAsset(asset)
    End()


@ContinueOnRest(1038542500)
def Event_1038542500():
    """Event 1038542500"""
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1038542200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1038542201,
            asset=Assets.AEG007_557_1079,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1038542202,
            asset=Assets.AEG007_557_1080,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1038542203,
            asset=Assets.AEG007_557_1081,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )

"""
West Altus Plateau (NW) (SE)

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
from .entities.m60_37_54_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005250(0, character=Characters.GraftedScion, region=1037542341, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.GraftedScion, region=1037542342, seconds=0.0, animation_id=0)
    Event_1037542500()
    CommonFunc_90005300(0, flag=1037540341, character=Characters.GraftedScion, item_lot_param_id=0, seconds=3.0, left=0)
    CommonFunc_90005271(0, character=Characters.LeyndellSoldier0, seconds=0.0, animation_id=-1)
    Event_1037542260()
    CommonFunc_90005250(0, character=Characters.Marionette2, region=1037542250, seconds=0.0, animation_id=0)
    CommonFunc_90005250(1, character=Characters.Marionette3, region=1037542250, seconds=0.0, animation_id=0)
    CommonFunc_90005250(2, character=Characters.Marionette4, region=1037542250, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Marionette0,
        animation_id=30010,
        animation_id_1=20010,
        region=1037542350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=1037540235, region=1037542235, radius=5.0, seconds=0.0, animation_id=3004)
    CommonFunc_90005261(
        0,
        character=Characters.Marionette1,
        region=1037542351,
        radius=0.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(1, character=1037540352, region=1037542351, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Basilisk0, region=1037542210, seconds=0.0, animation_id=0)
    CommonFunc_90005250(1, character=Characters.Basilisk2, region=1037542210, seconds=0.0, animation_id=0)
    CommonFunc_90005250(
        2,
        character=Characters.Basilisk3,
        region=1037542210,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005250(3, character=1037540213, region=1037542210, seconds=0.10000000149011612, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Basilisk1,
        animation_id=30001,
        animation_id_1=20001,
        region=1037542215,
        seconds=1.399999976158142,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.Basilisk4,
        animation_id=30001,
        animation_id_1=20001,
        region=1037542215,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1037542220(0, character=Characters.PutridCorpse0, region=1037542360, destination=1037542260, seconds=0.0)
    Event_1037542220(1, character=Characters.PutridCorpse1, region=1037542360, destination=1037542261, seconds=1.0)
    Event_1037542220(2, character=Characters.PutridCorpse2, region=1037542360, destination=1037542262, seconds=2.0)
    Event_1037542220(
        3,
        character=Characters.PutridCorpse3,
        region=1037542360,
        destination=1037542263,
        seconds=0.20000000298023224,
    )
    Event_1037542220(
        4,
        character=Characters.PutridCorpse4,
        region=1037542360,
        destination=1037542264,
        seconds=0.10000000149011612,
    )
    Event_1037542220(
        5,
        character=Characters.PutridCorpse5,
        region=1037542360,
        destination=1037542265,
        seconds=1.100000023841858,
    )
    Event_1037542220(
        6,
        character=Characters.PutridCorpse6,
        region=1037542360,
        destination=1037542266,
        seconds=0.30000001192092896,
    )
    Event_1037542220(7, character=1037540267, region=1037542360, destination=1037542267, seconds=0.10000000149011612)
    Event_1037542220(8, character=1037540268, region=1037542360, destination=1037542268, seconds=2.0999999046325684)
    Event_1037542220(9, character=1037540269, region=1037542360, destination=1037542269, seconds=2.299999952316284)
    Event_1037542220(10, character=1037540270, region=1037542360, destination=1037542270, seconds=2.5999999046325684)
    Event_1037542220(11, character=1037540271, region=1037542360, destination=1037542271, seconds=2.4000000953674316)
    Event_1037542220(12, character=1037540272, region=1037542360, destination=1037542272, seconds=2.700000047683716)
    Event_1037542220(13, character=1037540273, region=1037542360, destination=1037542273, seconds=2.5)
    Event_1037542220(14, character=1037540274, region=1037542360, destination=1037542274, seconds=2.0999999046325684)
    Event_1037542220(15, character=1037540275, region=1037542360, destination=1037542275, seconds=2.200000047683716)
    CommonFunc_90005251(0, character=Characters.LeyndellFootSoldier2, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellSoldier1,
        region=1037542304,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellSoldier2,
        region=1037542304,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellSoldier3,
        region=1037542306,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        1,
        character=Characters.LeyndellKnight1,
        region=1037542306,
        radius=15.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_1037542250(0, character=Characters.LeyndellFootSoldier0)
    Event_1037542250(1, character=Characters.LeyndellFootSoldier1)
    Event_1037542250(2, character=Characters.LeyndellKnight1)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellKnight0,
        animation_id=30000,
        animation_id_1=20000,
        region=1037542304,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1037542250(3, character=Characters.LeyndellSoldier3)
    Event_1037542300()
    CommonFunc_90005250(1, character=1037540440, region=1037542810, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.UlceratedTreeSpirit,
        animation_id=30000,
        animation_id_1=20000,
        region=1037542810,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=Characters.UlceratedTreeSpirit, name=904640600, npc_threat_level=18)
    CommonFunc_90005860(
        0,
        flag=1037540810,
        left=0,
        character=Characters.UlceratedTreeSpirit,
        left_1=0,
        item_lot__item_lot_param_id=30380,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.UlceratedTreeSpirit, npc_threat_level=18, right=0)
    Event_1037542255()
    Event_1037542270(0, attacker__character=1037545810, region=1037542810)
    Event_1037542580()
    CommonFunc_90005620(
        0,
        flag=1037540570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1037542571,
        cancel_flag__right_flag=1037542572,
        right=1037542573,
    )
    Event_1037542569(0, flag=1037540570, asset=Assets.AEG099_271_9000)
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61033)
    Event_1037543700(0, character=Characters.Patches0)
    Event_1037543704(0, character=Characters.Patches1)
    Event_1037543701()
    Event_1037543702(
        0,
        character=Characters.Patches0,
        flag=1037542701,
        flag_1=1037549201,
        character_1=Characters.Patches1,
        flag_2=1037549216,
    )
    Event_1037543703()
    Event_1037543705()
    Event_1037543706()
    CommonFunc_90005704(0, attacked_entity=Characters.Patches0, flag=3681, flag_1=3680, flag_2=1037549201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Patches0,
        flag=3681,
        flag_1=3682,
        flag_2=1037549201,
        flag_3=3681,
        first_flag=3680,
        last_flag=3684,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Patches0, flag=3683, first_flag=3680, last_flag=3684)
    CommonFunc_90005704(0, attacked_entity=Characters.Patches1, flag=3681, flag_1=3680, flag_2=1037549216, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Patches1,
        flag=3681,
        flag_1=3682,
        flag_2=1037549216,
        flag_3=3681,
        first_flag=3680,
        last_flag=3684,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Patches1, flag=3683, first_flag=3680, last_flag=3684)
    CommonFunc_90005725(
        0,
        flag=4770,
        flag_1=4771,
        flag_2=4773,
        flag_3=1037549255,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1037546700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4771,
        flag_1=4772,
        flag_2=1037549256,
        flag_3=4771,
        first_flag=4770,
        last_flag=4774,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4771, flag_1=4770, flag_2=1037549256, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4773, first_flag=4770, last_flag=4774)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4771,
        flag_1=4772,
        flag_2=1037549257,
        flag_3=4771,
        first_flag=4770,
        last_flag=4774,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4771, flag_1=4770, flag_2=1037549257, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1037542716, flag_1=1037542717)
    CommonFunc_90005727(
        0,
        flag=4771,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4770,
        last_flag=4773,
    )
    CommonFunc_90005729(0, flag=1037549250, character=Characters.Merchant, distance=36.0, flag_1=1037542712)
    Event_1037542350()
    Event_1037542351(0, flag=1037547060, flag_1=1037540220)
    Event_1037542351(1, flag=1037547080, flag_1=1037540221)
    Event_1037542351(2, flag=1037547090, flag_1=1037540222)
    Event_1037542351(3, flag=1037547070, flag_1=1037540223)
    Event_1037542505()
    Event_1037542450(0, asset=Assets.AEG007_434_9000)
    Event_1037542450(1, asset=Assets.AEG007_434_9001)
    Event_1037542450(2, asset=Assets.AEG007_434_9002)
    Event_1037542450(3, asset=Assets.AEG007_434_9003)
    Event_1037542450(4, asset=Assets.AEG007_434_9004)
    Event_1037542450(5, asset=Assets.AEG007_434_9005)
    Event_1037542450(6, asset=Assets.AEG007_434_9006)
    Event_1037542450(7, asset=Assets.AEG007_434_9007)
    Event_1037542450(8, 1037541408)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Patches0)
    DisableBackread(Characters.Patches1)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)
    CommonFunc_90005261(0, character=Characters.Avionette0, region=1037542450, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Avionette1, region=1037542452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(1, character=Characters.Avionette2, region=1037542452, radius=5.0, seconds=0.0, animation_id=-1)
    Event_1037542400(0, character=Characters.Avionette0)
    Event_1037542400(2, character=Characters.Avionette1)
    Event_1037542400(3, character=Characters.Avionette2)
    Event_1037542210(0, character__targeting_character=Characters.Avionette0, region=1037542460)
    Event_1037542210(1, character__targeting_character=Characters.Avionette1, region=1037542461)
    Event_1037542210(2, 1037540362, 1037542461)


@RestartOnRest(1037542210)
def Event_1037542210(_, character__targeting_character: uint, region: uint):
    """Event 1037542210"""
    DisableNetworkSync()
    AND_1.Add(CharacterDead(character__targeting_character))
    if AND_1:
        return
    AND_1.Add(CharacterTargeting(targeting_character=character__targeting_character, targeted_character=20000))
    AND_1.Add(CharacterOutsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(character__targeting_character)
    Wait(5.0)
    Restart()


@RestartOnRest(1037542220)
def Event_1037542220(_, character: uint, region: uint, destination: uint, seconds: float):
    """Event 1037542220"""
    DisableCharacter(character)
    DisableInvincibility(character)
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        End()
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_1.Add(PlayerInOwnWorld())
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    DisableThisSlotFlag()
    Wait(seconds)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    EnableInvincibility(character)
    Wait(3.0)
    DisableInvincibility(character)
    End()


@NeverRestart(1037542505)
def Event_1037542505():
    """Event 1037542505"""
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1037542410,
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
            asset_flag=1037542410,
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
            asset_flag=1037542410,
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
            asset_flag=1037542410,
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
            asset_flag=1037542410,
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
            asset_flag=1037542410,
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
            asset_flag=1037542410,
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
            asset_flag=1037542410,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542411,
            asset=Assets.AEG007_557_1001,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542412,
            asset=Assets.AEG007_557_1002,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542413,
            asset=Assets.AEG007_557_1003,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542414,
            asset=Assets.AEG007_557_1004,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542415,
            asset=Assets.AEG007_557_1005,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542416,
            asset=Assets.AEG007_557_1006,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542417,
            asset=Assets.AEG007_557_1007,
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
            asset_flag=1037542418,
            asset=Assets.AEG007_557_1008,
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
            asset_flag=1037542418,
            asset=Assets.AEG007_557_1008,
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
            asset_flag=1037542418,
            asset=Assets.AEG007_557_1008,
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
            asset_flag=1037542418,
            asset=Assets.AEG007_557_1008,
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
            asset_flag=1037542418,
            asset=Assets.AEG007_557_1008,
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
            asset_flag=1037542418,
            asset=Assets.AEG007_557_1008,
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
            asset_flag=1037542418,
            asset=Assets.AEG007_557_1008,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(0, 1037542418, 1037541308, 200, 0, 802003200, 1.0, 0.0, 1.0)


@NeverRestart(1037542580)
def Event_1037542580():
    """Event 1037542580"""
    RegisterLadder(start_climbing_flag=1037540580, stop_climbing_flag=1037540851, asset=Assets.AEG004_180_1000)
    RegisterLadder(start_climbing_flag=1037540582, stop_climbing_flag=1037540853, asset=1037541582)
    RegisterLadder(start_climbing_flag=1037540584, stop_climbing_flag=1037540855, asset=Assets.AEG004_181_1001)
    RegisterLadder(start_climbing_flag=1037540586, stop_climbing_flag=1037540857, asset=Assets.AEG004_181_1002)
    RegisterLadder(start_climbing_flag=1037540588, stop_climbing_flag=1037540859, asset=Assets.AEG004_182_1000)
    RegisterLadder(start_climbing_flag=1037540590, stop_climbing_flag=1037540861, asset=1037541590)
    RegisterLadder(start_climbing_flag=1037540592, stop_climbing_flag=1037540863, asset=Assets.AEG004_183_1000)
    RegisterLadder(start_climbing_flag=1037540594, stop_climbing_flag=1037540865, asset=Assets.AEG004_182_1002)
    RegisterLadder(start_climbing_flag=1037540596, stop_climbing_flag=1037540867, asset=1037541596)
    RegisterLadder(start_climbing_flag=1037540598, stop_climbing_flag=1037540869, asset=1037541598)
    RegisterLadder(start_climbing_flag=1037540600, stop_climbing_flag=1037540871, asset=1037541600)
    RegisterLadder(start_climbing_flag=1037540602, stop_climbing_flag=1037540873, asset=1037541602)
    RegisterLadder(start_climbing_flag=1037540604, stop_climbing_flag=1037540875, asset=1037541604)


@RestartOnRest(1037542250)
def Event_1037542250(_, character: uint):
    """Event 1037542250"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8087)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542255)
def Event_1037542255():
    """Event 1037542255"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(Characters.UlceratedTreeSpirit, 8087)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542260)
def Event_1037542260():
    """Event 1037542260"""
    SetTeamType(Characters.Marionette2, TeamType.Enemy)
    SetTeamType(Characters.Marionette3, TeamType.Enemy)
    SetTeamType(Characters.Marionette4, TeamType.Enemy)
    SetTeamType(Characters.LeyndellSoldier0, TeamType.Enemy2)
    End()


@RestartOnRest(1037542270)
def Event_1037542270(_, attacker__character: uint, region: uint):
    """Event 1037542270"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5661)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1050562200):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5661)
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
    RemoveSpecialEffect(attacker__character, 5661)


@RestartOnRest(1037542300)
def Event_1037542300():
    """Event 1037542300"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(HasAIStatus(Characters.LeyndellKnight0, ai_status=AIStatusType.Battle))
    
    Wait(1.2999999523162842)
    ForceAnimation(Characters.LeyndellKnight0, 3014)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542350)
def Event_1037542350():
    """Event 1037542350"""
    DisableNetworkSync()
    DeleteVFX(1037542220, erase_root_only=False)
    DeleteVFX(1037542221, erase_root_only=False)
    DeleteVFX(1037542222, erase_root_only=False)
    DeleteVFX(1037542223, erase_root_only=False)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1037542225))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfPlayerNotInOwnWorld(8)
    SkipLinesIfFlagEnabled(1, 1037540220)
    CreateVFX(1037542220)
    SkipLinesIfFlagEnabled(1, 1037540221)
    CreateVFX(1037542221)
    SkipLinesIfFlagEnabled(1, 1037540222)
    CreateVFX(1037542222)
    SkipLinesIfFlagEnabled(1, 1037540223)
    CreateVFX(1037542223)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=1037542225))

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(1037542220, erase_root_only=False)
    DeleteVFX(1037542221, erase_root_only=False)
    DeleteVFX(1037542222, erase_root_only=False)
    DeleteVFX(1037542223, erase_root_only=False)
    Restart()


@RestartOnRest(1037542351)
def Event_1037542351(_, flag: uint, flag_1: uint):
    """Event 1037542351"""
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)
    End()


@RestartOnRest(1037542400)
def Event_1037542400(_, character: uint):
    """Event 1037542400"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, 30010, loop=True, skip_transition=True)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 20010, skip_transition=True)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542450)
def Event_1037542450(_, asset: uint):
    """Event 1037542450"""
    DisableAsset(asset)
    End()


@RestartOnRest(1037542500)
def Event_1037542500():
    """Event 1037542500"""
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1037542342))
    
    RemoveSpecialEffect(Characters.GraftedScion, 16283)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=1037542342))
    
    AddSpecialEffect(Characters.GraftedScion, 16283)
    Restart()


@NeverRestart(1037542569)
def Event_1037542569(_, flag: uint, asset: uint):
    """Event 1037542569"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=101, model_point=806043)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableAsset(asset)


@RestartOnRest(1037542801)
def Event_1037542801():
    """Event 1037542801"""
    if FlagEnabled(1037540810):
        return
    
    MAIN.Await(HealthValue(Characters.UlceratedTreeSpirit) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.UlceratedTreeSpirit, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.UlceratedTreeSpirit))
    
    KillBossAndDisplayBanner(character=Characters.UlceratedTreeSpirit, banner_type=BannerType.EnemyFelled)
    EnableFlag(1037540810)


@RestartOnRest(1037542810)
def Event_1037542810():
    """Event 1037542810"""
    DisableAI(Characters.UlceratedTreeSpirit)
    DisableCharacter(Characters.UlceratedTreeSpirit)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1037542810))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableCharacter(Characters.UlceratedTreeSpirit)
    EnableAI(Characters.UlceratedTreeSpirit)
    EnableFlag(1037542810)
    End()


@RestartOnRest(1037543700)
def Event_1037543700(_, character: uint):
    """Event 1037543700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3688)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3688))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3688))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1037543701)
def Event_1037543701():
    """Event 1037543701"""
    WaitFrames(frames=1)
    if FlagEnabled(1037549210):
        return
    if FlagEnabled(3683):
        return
    EndIfFlagRangeAnyEnabled(flag_range=(3689, 3697))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1045522710))
    AND_1.Add(FlagEnabled(3680))
    AND_1.Add(FlagEnabled(3688))
    AND_1.Add(CharacterNotMounted(character=PLAYER))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(1037549210)
    AND_2.Add(CharacterMounted(character=PLAYER))
    SkipLinesIfConditionFalse(1, AND_2)
    Move(40000, destination=1045522712, destination_type=CoordEntityType.Region, short_move=True)
    EnableFlag(9021)
    GotoIfPlayerInOwnWorld(Label.L1)
    OR_3.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_3.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_3.Add(PlayerNotInOwnWorld())
    AND_3.Add(OR_3)
    GotoIfConditionTrue(Label.L2, input_condition=AND_3)
    OR_4.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_4.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_4.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_4.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    AND_4.Add(PlayerNotInOwnWorld())
    AND_4.Add(OR_4)
    GotoIfConditionTrue(Label.L3, input_condition=AND_4)
    Goto(Label.L4)

    # --- Label 1 --- #
    DefineLabel(1)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=60370000,
        cutscene_flags=0,
        move_to_region=1045522712,
        map_id=60375400,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(3698)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=60370000,
        cutscene_flags=0,
        move_to_region=1037542720,
        map_id=60375400,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
    )
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    PlayCutscene(60370000, cutscene_flags=0, player_id=10000)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    End()


@RestartOnRest(1037543702)
def Event_1037543702(_, character: uint, flag: uint, flag_1: uint, character_1: uint, flag_2: uint):
    """Event 1037543702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3683):
        return
    AND_1.Add(FlagDisabled(3685))
    AND_1.Add(FlagDisabled(3686))
    AND_1.Add(FlagDisabled(3687))
    AND_1.Add(FlagDisabled(3688))
    AND_1.Add(FlagDisabled(3693))
    if AND_1:
        return
    GotoIfFlagDisabled(Label.L1, flag=3681)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(3681))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(FlagEnabled(3688))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    AND_3.Add(FlagEnabled(3693))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=5.0))
    OR_4.Add(AND_2)
    OR_4.Add(AND_3)
    AND_4.Add(CharacterHasSpecialEffect(PLAYER, 9700))
    AND_4.Add(OR_4)
    
    MAIN.Await(AND_4)
    
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    if FlagEnabled(3693):
        DisableNetworkFlag(flag_2)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ClearTargetList(character_1)
    ReplanAI(character)
    ReplanAI(character_1)
    End()


@RestartOnRest(1037543703)
def Event_1037543703():
    """Event 1037543703"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(31009206):
        return
    if FlagEnabled(1037549211):
        return
    AND_1.Add(FlagDisabled(3685))
    AND_1.Add(FlagDisabled(3686))
    AND_1.Add(FlagDisabled(3687))
    AND_1.Add(FlagDisabled(3688))
    AND_1.Add(FlagDisabled(3693))
    if AND_1:
        return
    EnableFlag(1037549211)
    WaitFrames(frames=1)
    EnableFlag(3698)
    End()


@RestartOnRest(1037543704)
def Event_1037543704(_, character: uint):
    """Event 1037543704"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3693)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3693))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3693))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1037543705)
def Event_1037543705():
    """Event 1037543705"""
    WaitFrames(frames=1)
    if FlagEnabled(1037542705):
        CreateVFX(1045522711)
        CreateVFX(1037542710)
        CreateVFX(1037542711)
        CreateVFX(1037542712)
        CreateVFX(1037542713)
        EnableFlag(1037549212)
        End()
    DeleteVFX(1045522711, erase_root_only=False)
    DeleteVFX(1037542710, erase_root_only=False)
    DeleteVFX(1037542711, erase_root_only=False)
    DeleteVFX(1037542712, erase_root_only=False)
    DeleteVFX(1037542713, erase_root_only=False)
    DisableFlag(1037549212)
    if FlagEnabled(3683):
        return
    EndIfFlagRangeAnyEnabled(flag_range=(3689, 3697))
    OR_3.Add(FlagEnabled(3688))
    
    MAIN.Await(OR_3)
    
    CreateVFX(1045522711)
    CreateVFX(1037542710)
    CreateVFX(1037542711)
    CreateVFX(1037542712)
    CreateVFX(1037542713)
    EnableFlag(1037549212)
    OR_4.Add(FlagEnabled(3688))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1037543706)
def Event_1037543706():
    """Event 1037543706"""
    if FlagEnabled(3683):
        return
    EndIfFlagRangeAnyEnabled(flag_range=(3689, 3697))
    AND_1.Add(FlagEnabled(3688))
    AND_1.Add(FlagEnabled(3683))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1037542705)
    End()

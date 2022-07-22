"""
Siofra River

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
from .entities.m12_02_00_00_entities import *
from .entities.m60_35_45_00_entities import Characters as m60_35_Characters
from .entities.m60_49_40_00_entities import Assets as m60_49_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=71223, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=71224, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=71226, asset=Assets.AEG099_060_9006)
    RegisterGrace(grace_flag=71227, asset=Assets.AEG099_060_9007)
    RegisterGrace(grace_flag=71228, asset=Assets.AEG099_060_9008)
    RegisterGrace(grace_flag=71229, asset=Assets.AEG099_060_9009)
    CommonFunc_9005810(
        0,
        flag=12020850,
        grace_flag=71221,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    CommonFunc_9005810(
        0,
        flag=12020800,
        grace_flag=71220,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_12022503()
    Event_12022580()
    CommonFunc_90005920(0, flag=12020900, asset=12021900, obj_act_id=12023900)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, model_point=800, right=0)
    Event_12022800()
    Event_12022810()
    Event_12022849()
    Event_12022820()
    Event_12022821()
    Event_12022850()
    Event_12022860()
    Event_12022865(0, character=Characters.SilverTear4, character_1=Characters.MimicTear, region=63010)
    Event_12022899()
    CommonFunc_90005501(
        0,
        flag=12020520,
        flag_1=12021520,
        left=5,
        asset=Assets.AEG239_010_0501,
        asset_1=m60_49_Assets.AEG239_020_2000,
        asset_2=Assets.AEG239_021_0501,
        flag_2=12020522,
    )
    CommonFunc_90005620(
        0,
        flag=12020570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=12022570,
        cancel_flag__right_flag=12022571,
        right=12022572,
    )
    Event_12022567(0, flag=12020570, region=12022570)
    Event_12022569(0, flag=12020524, flag_1=12020570)
    Event_12020500()
    CommonFunc_90005620(
        0,
        flag=12020575,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9001,
        asset_2=0,
        left_flag=12022575,
        cancel_flag__right_flag=12022576,
        right=12022577,
    )
    Event_12022568(0, flag=12020575, asset=Assets.AEG099_271_9000)
    Event_12020510()
    Event_12022670()
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9001,
        area_id=12,
        block_id=2,
        cc_id=0,
        dd_id=0,
        player_start=12022203,
        unk_8_12=12020000,
        flag=12022203,
        left_flag=12022210,
        cancel_flag__right_flag=12022211,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9002,
        area_id=12,
        block_id=2,
        cc_id=0,
        dd_id=0,
        player_start=12022204,
        unk_8_12=12020000,
        flag=12022204,
        left_flag=12022212,
        cancel_flag__right_flag=12022213,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9003,
        area_id=12,
        block_id=2,
        cc_id=0,
        dd_id=0,
        player_start=12022205,
        unk_8_12=12020000,
        flag=12022205,
        left_flag=12022215,
        cancel_flag__right_flag=12022206,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_12022600()
    Event_12022609()
    Event_12022620()
    Event_12022629()
    Event_12022601(0, flag=12020600, asset=Assets.AEG237_055_1000, asset_1=Assets.AEG237_039_9004)
    Event_12022601(1, flag=12020601, asset=Assets.AEG237_055_9000, asset_1=Assets.AEG237_039_9007)
    Event_12022601(2, flag=12020602, asset=Assets.AEG237_055_9001, asset_1=Assets.AEG237_039_9001)
    Event_12022601(3, flag=12020603, asset=Assets.AEG237_055_9002, asset_1=Assets.AEG237_039_9000)
    Event_12022601(4, flag=12020604, asset=Assets.AEG237_055_9003, asset_1=Assets.AEG237_039_9002)
    Event_12022601(5, flag=12020605, asset=Assets.AEG237_055_9004, asset_1=Assets.AEG237_039_9005)
    Event_12022601(6, flag=12020606, asset=Assets.AEG237_055_9005, asset_1=Assets.AEG237_039_9003)
    Event_12022601(7, flag=12020607, asset=Assets.AEG237_055_9006, asset_1=Assets.AEG237_039_9006)
    Event_12022621(0, flag=12020620, asset=Assets.AEG237_055_9007, asset_1=Assets.AEG237_039_3006)
    Event_12022621(1, flag=12020621, asset=Assets.AEG237_055_9008, asset_1=Assets.AEG237_039_3007)
    Event_12022621(2, flag=12020622, asset=Assets.AEG237_055_9009, asset_1=Assets.AEG237_039_3005)
    Event_12022621(3, flag=12020623, asset=Assets.AEG237_055_9010, asset_1=Assets.AEG237_039_3002)
    Event_12022621(4, flag=12020624, asset=Assets.AEG237_055_9011, asset_1=Assets.AEG237_039_3004)
    Event_12022621(5, flag=12020625, asset=Assets.AEG237_055_9012, asset_1=Assets.AEG237_039_3001)
    Event_12022621(6, flag=12020626, asset=12021626, asset_1=12021636)
    Event_12022621(7, flag=12020627, asset=12021627, asset_1=12021637)
    CommonFunc_90005250(0, character=Characters.NoxFighter, region=12022211, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=12020220, region=12022220, radius=70.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.RedWolf, region=12022220, radius=70.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(0, flag=12020221, character=Characters.RedWolf, item_lot=0, seconds=0.0, left=-1)
    Event_12022300(0, character=12020300, region=12022300, seconds=0.0)
    Event_12022300(1, character=12020301, region=12022300, seconds=0.0)
    Event_12022300(2, character=Characters.AncestralFollower3, region=12022302, seconds=0.0)
    CommonFunc_90005250(0, character=Characters.AncestralFollower3, region=12022302, seconds=0.0, animation_id=3006)
    Event_12022300(3, character=12025303, region=12022303, seconds=0.0)
    Event_12022300(4, character=12025304, region=12022304, seconds=0.0)
    CommonFunc_90005250(0, character=Characters.Dummy0, region=12022304, seconds=0.0, animation_id=-1)
    Event_12022300(5, character=12025305, region=12022305, seconds=0.0)
    CommonFunc_90005250(0, character=Characters.AncestralFollower6, region=12022305, seconds=2.0, animation_id=3011)
    Event_12022300(6, character=12025306, region=12022306, seconds=0.0)
    Event_12022300(7, character=12025307, region=12022307, seconds=0.0)
    Event_12022300(8, character=12025308, region=12022308, seconds=0.0)
    Event_12022300(9, character=12025309, region=12022309, seconds=0.0)
    CommonFunc_90005251(0, character=Characters.Springhare0, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Springhare1, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Springhare2, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Springhare3, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Springhare4, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=0, region=0, radius=0.0, seconds=0.0, animation_id=0)
    Event_12022300(10, character=12025310, region=12022310, seconds=0.0)
    Event_12022300(11, character=12025311, region=12022311, seconds=0.0)
    Event_12022300(12, character=12025312, region=12022312, seconds=0.0)
    Event_12022300(13, character=Characters.AncestralFollower2, region=12022313, seconds=0.0)
    Event_12022300(15, character=12025315, region=12022315, seconds=0.0)
    Event_12022300(16, character=Characters.AncestralFollower5, region=12022316, seconds=0.0)
    CommonFunc_90005250(0, character=Characters.AncestralFollower5, region=12022316, seconds=0.0, animation_id=3006)
    Event_12022300(17, character=Characters.AncestralFollower4, region=12022317, seconds=0.0)
    Event_12022300(18, character=12025318, region=12022318, seconds=0.0)
    Event_12022300(19, character=Characters.AncestralFollower0, region=12022319, seconds=0.0)
    CommonFunc_90005250(0, character=Characters.AncestralFollower0, region=12022319, seconds=0.0, animation_id=-1)
    Event_12022300(20, character=Characters.AncestralFollower7, region=12022331, seconds=0.0)
    Event_12022300(21, character=Characters.AncestralFollower9, region=12022334, seconds=0.0)
    Event_12022300(22, character=Characters.AncestralFollower10, region=12022334, seconds=0.0)
    Event_12022300(23, character=12020336, region=12022336, seconds=3.0)
    Event_12022300(24, character=Characters.AncestralFollower8, region=12022336, seconds=0.0)
    CommonFunc_90005250(0, character=12020336, region=12022336, seconds=0.0, animation_id=3006)
    CommonFunc_90005250(0, character=Characters.AncestralFollower8, region=12022336, seconds=0.0, animation_id=3006)
    Event_12022300(25, character=12025324, region=12022314, seconds=0.0)
    Event_12022300(26, character=12025325, region=12022314, seconds=0.0)
    Event_12022300(29, character=12025329, region=12022329, seconds=0.0)
    CommonFunc_90005201(
        0,
        character=Characters.AncestralFollower25,
        animation_id=30011,
        animation_id_1=20011,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.AncestralFollower26,
        animation_id=30011,
        animation_id_1=20011,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.AncestralFollower28,
        animation_id=30011,
        animation_id_1=20011,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.AncestralFollower29,
        animation_id=30011,
        animation_id_1=20011,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=12020348, radius=100.0, seconds=0.0, animation_id=-1)
    Event_12022350(0, character=12020390, character_1=12025350)
    Event_12022360(0, character=12020390, character_1=12025350)
    Event_12022370()
    Event_12022371()
    CommonFunc_90005250(0, character=12020390, region=12022350, seconds=3.0, animation_id=-1)
    Event_12022372()
    Event_12022373()
    Event_12022350(1, character=Characters.AncestralFollowerShaman0, character_1=12025351)
    Event_12022360(1, character=Characters.AncestralFollowerShaman0, character_1=12025351)
    Event_12022350(2, character=Characters.AncestralFollowerShaman1, character_1=12025352)
    Event_12022360(2, character=Characters.AncestralFollowerShaman1, character_1=12025352)
    CommonFunc_90005250(0, character=Characters.AncestralFollower11, region=12022350, seconds=3.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AncestralFollower12, region=12022350, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AncestralFollower16, region=12022366, seconds=0.0, animation_id=3006)
    CommonFunc_90005250(0, character=Characters.AncestralFollower16, region=12022368, seconds=0.0, animation_id=-1)
    CommonFunc_90005860(
        0,
        flag=12020830,
        left=0,
        character=Characters.DragonkinSoldier,
        left_1=1,
        item_lot=30620,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.DragonkinSoldier, name=904650600, npc_threat_level=25)
    CommonFunc_90005251(0, character=Characters.GiantOctopus, radius=30.0, seconds=0.0, animation_id=3009)
    CommonFunc_90005300(0, flag=12020470, character=Characters.Scarab2, item_lot=40648, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12020472, character=Characters.Scarab0, item_lot=40630, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12020474, character=Characters.Scarab4, item_lot=40610, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12020477, character=Characters.Scarab3, item_lot=40642, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12020479, character=Characters.Scarab1, item_lot=40646, seconds=1.5, left=0)
    CommonFunc_90005250(0, character=12020420, region=12022420, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=12020421, radius=60.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Dummy1, radius=100.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Dummy3, region=12022422, radius=45.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Dummy1, radius=60.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.CrucibleKnight1, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(
        0,
        flag=12020430,
        character=Characters.CrucibleKnight0,
        item_lot=12020435,
        seconds=1.5,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=12020431,
        character=Characters.CrucibleKnight1,
        item_lot=12020445,
        seconds=1.5,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=12020434,
        character=Characters.CrucibleKnight2,
        item_lot=0,
        seconds=1.5,
        left=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FallenHawksSoldier0,
        region=12022440,
        radius=15.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FallenHawksSoldier2,
        region=12022442,
        radius=15.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_12022440(
        0,
        character=Characters.CrucibleKnight1,
        character_1=Characters.FallenHawksSoldier0,
        patrol_information_id=12023440,
    )
    Event_12022440(
        1,
        character=Characters.CrucibleKnight1,
        character_1=Characters.FallenHawksSoldier1,
        patrol_information_id=12023440,
    )
    Event_12022440(
        2,
        character=Characters.CrucibleKnight1,
        character_1=Characters.FallenHawksSoldier2,
        patrol_information_id=12023440,
    )
    Event_12022440(
        3,
        character=Characters.FallenHawksSoldier6,
        character_1=Characters.FallenHawksSoldier3,
        patrol_information_id=12023444,
    )
    Event_12022440(
        4,
        character=Characters.FallenHawksSoldier6,
        character_1=Characters.FallenHawksSoldier4,
        patrol_information_id=12023444,
    )
    Event_12022440(
        5,
        character=Characters.FallenHawksSoldier6,
        character_1=Characters.FallenHawksSoldier5,
        patrol_information_id=12023444,
    )
    Event_12022440(
        6,
        character=Characters.FallenHawksSoldier6,
        character_1=Characters.FallenHawksSoldier7,
        patrol_information_id=12023444,
    )
    Event_12022440(
        7,
        character=Characters.FallenHawksSoldier6,
        character_1=Characters.FallenHawksSoldier8,
        patrol_information_id=12023444,
    )
    CommonFunc_90005250(0, character=Characters.Rat0, region=12022450, seconds=1.5, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat1, region=12022450, seconds=2.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat2, region=12022450, seconds=3.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat3, region=12022450, seconds=2.5, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat4, region=12022450, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat5, region=12022450, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=12025461, radius=20.0, seconds=0.0, animation_id=-1)
    Event_12022419(0, character=Characters.SilverTear5, character_1=Characters.Troll, region=12022400)
    Event_12022400(1, character=Characters.SilverTear6, character_1=Characters.SilverTear0, region=12022401)
    CommonFunc_90005261(0, character=Characters.SilverTear6, region=12022411, radius=20.0, seconds=0.0, animation_id=-1)
    Event_12022400(2, character=Characters.SilverTear7, character_1=Characters.SilverTear1, region=12022402)
    CommonFunc_90005261(0, character=Characters.SilverTear7, region=12022412, radius=20.0, seconds=0.0, animation_id=-1)
    Event_12022400(3, character=12020403, character_1=12020493, region=12022403)
    Event_12022400(4, character=12020404, character_1=12020494, region=12022404)
    Event_12022400(5, character=12020405, character_1=12020495, region=12022405)
    Event_12022400(6, character=Characters.SilverTear8, character_1=Characters.SilverTear2, region=12022406)
    Event_12022400(7, character=Characters.SilverTear9, character_1=Characters.SilverTear3, region=12022407)
    Event_12022400(10, character=12020410, character_1=12020480, region=12022410)
    CommonFunc_90005702(0, character=Characters.DHunteroftheDead, flag=4063, first_flag=4060, last_flag=4063)
    Event_12020700(
        0,
        character=Characters.DHunteroftheDead,
        asset=Assets.AEG232_547_5000,
        asset_1=Assets.AEG099_320_9001,
    )
    Event_12020701(0, entity=12022716)
    CommonFunc_90005752(0, asset=Assets.AEG099_320_9001, vfx_id=200, model_point=120, seconds=3.0)
    Event_12023720(0, character=Characters.Blaidd)
    CommonFunc_90005703(
        0,
        character=Characters.Blaidd,
        flag=3601,
        flag_1=3602,
        flag_2=12029151,
        flag_3=3603,
        first_flag=3600,
        last_flag=3603,
        right=-1,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Blaidd, flag=3601, flag_1=3600, flag_2=12029151, right=3)
    CommonFunc_90005702(0, character=Characters.Blaidd, flag=3603, first_flag=3600, last_flag=3603)
    Event_12023721(0, other_entity=Assets.AEG099_631_9000, radius=3.0, special_effect_id=9710, flag=1034509410)
    Event_12023710(0, character=12020700, character_1=12020701)
    CommonFunc_90005725(
        0,
        flag=4800,
        flag_1=4801,
        flag_2=4803,
        flag_3=12029105,
        character=Characters.Merchant,
        character_1=m60_35_Characters.NomadMule,
        asset=12026700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4801,
        flag_1=4802,
        flag_2=12029106,
        flag_3=4801,
        first_flag=4800,
        last_flag=4804,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4801, flag_1=4800, flag_2=12029106, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4803, first_flag=4800, last_flag=4804)
    CommonFunc_90005706(0, character=Characters.Commoner, animation_id=930023, left=0)
    CommonFunc_90005780(
        0,
        flag=12020800,
        summon_flag=12022160,
        dismissal_flag=12022161,
        character=Characters.Human,
        sign_type=20,
        region=12022716,
        right=12029019,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=12020800, flag_1=12022160, flag_2=12022161, character=Characters.Human)
    Event_12022699()
    Event_12022698()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(12020700)
    DisableBackread(Characters.Blaidd)
    DisableBackread(Characters.Commoner)
    DisableAsset(Assets.AEG099_320_9001)
    Event_12020519()
    RunEvent(12020050, slot=0, args=(0,))


@RestartOnRest(12022699)
def Event_12022699():
    """Event 12022699"""
    MAIN.Await(FlagEnabled(12022805))
    
    AND_1.Add(CharacterInsideRegion(character=Characters.Human, region=12022717))
    GotoIfConditionTrue(Label.L10, input_condition=AND_1)
    CommonFunc_90005784(
        0,
        flag=12022160,
        flag_1=12022805,
        character=Characters.Human,
        region=12022800,
        region_1=12022809,
        animation=0,
    )
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    End()


@RestartOnRest(12022698)
def Event_12022698():
    """Event 12022698"""
    if FlagEnabled(12020800):
        return
    OR_1.Add(FlagEnabled(12022160))
    
    MAIN.Await(OR_1)
    
    DisableMapCollision(collision=12021698)


@RestartOnRest(12022569)
def Event_12022569(_, flag: uint, flag_1: uint):
    """Event 12022569"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)
    Restart()


@ContinueOnRest(12022568)
def Event_12022568(_, flag: uint, asset: uint):
    """Event 12022568"""
    DisableNetworkSync()
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


@ContinueOnRest(12022567)
def Event_12022567(_, flag: uint, region: uint):
    """Event 12022567"""
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@RestartOnRest(12022600)
def Event_12022600():
    """Event 12022600"""
    GotoIfFlagDisabled(Label.L0, flag=12020609)
    DeleteAssetVFX(Assets.AEG237_062_1000)
    CreateAssetVFX(Assets.AEG237_062_1000, vfx_id=200, model_point=812600)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_15.Add(FlagEnabled(12020600))
    AND_15.Add(FlagEnabled(12020601))
    AND_15.Add(FlagEnabled(12020602))
    AND_15.Add(FlagEnabled(12020603))
    AND_15.Add(FlagEnabled(12020604))
    AND_15.Add(FlagEnabled(12020605))
    AND_15.Add(FlagEnabled(12020606))
    AND_15.Add(FlagEnabled(12020607))
    
    MAIN.Await(AND_15)
    
    EnableNetworkFlag(12020609)
    DeleteAssetVFX(Assets.AEG237_062_1000)
    CreateAssetVFX(Assets.AEG237_062_1000, vfx_id=200, model_point=812600)
    Wait(3.0)
    DisplayDialog(text=30010, anchor_entity=0, display_distance=5.0)


@RestartOnRest(12022601)
def Event_12022601(_, flag: uint, asset: uint, asset_1: uint):
    """Event 12022601"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, vfx_id=200, model_point=812070)
    CreateAssetVFX(asset, vfx_id=201, model_point=812070)
    CreateAssetVFX(asset_1, vfx_id=200, model_point=812070)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAnimations(PLAYER)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9524, entity=asset))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    DisableAnimations(PLAYER)
    RotateToFaceEntity(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.2999999523162842)
    EnableNetworkFlag(flag)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, vfx_id=200, model_point=812070)
    CreateAssetVFX(asset, vfx_id=201, model_point=812070)
    CreateAssetVFX(asset_1, vfx_id=200, model_point=812070)
    Wait(2.0)
    EnableAnimations(PLAYER)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(1.2999999523162842)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, vfx_id=200, model_point=812070)
    CreateAssetVFX(asset, vfx_id=201, model_point=812070)
    CreateAssetVFX(asset_1, vfx_id=200, model_point=812070)
    End()


@ContinueOnRest(12022609)
def Event_12022609():
    """Event 12022609"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    GotoIfFlagDisabled(Label.L1, flag=12020609)
    DisableNetworkFlag(12022610)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9525, entity=Assets.AEG237_062_1000))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(12022610)
    RotateToFaceEntity(PLAYER, Assets.AEG237_062_1000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(0.4000000059604645)
    BanishInvaders(unknown=0)
    Wait(1.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12082400,
        model_point=-1,
        copy_draw_parent=0,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(12020609))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_15:
        return
    
    MAIN.Await(FlagEnabled(12022610))
    
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12022202,
        model_point=-1,
        copy_draw_parent=0,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Wait(5.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12082401,
        model_point=-1,
        copy_draw_parent=0,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Restart()


@RestartOnRest(12022620)
def Event_12022620():
    """Event 12022620"""
    GotoIfFlagDisabled(Label.L0, flag=12020629)
    DeleteAssetVFX(Assets.AEG237_062_3000)
    CreateAssetVFX(Assets.AEG237_062_3000, vfx_id=200, model_point=812600)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_15.Add(FlagEnabled(12020620))
    AND_15.Add(FlagEnabled(12020621))
    AND_15.Add(FlagEnabled(12020622))
    AND_15.Add(FlagEnabled(12020623))
    AND_15.Add(FlagEnabled(12020624))
    AND_15.Add(FlagEnabled(12020625))
    
    MAIN.Await(AND_15)
    
    EnableNetworkFlag(12020629)
    DeleteAssetVFX(Assets.AEG237_062_3000)
    CreateAssetVFX(Assets.AEG237_062_3000, vfx_id=200, model_point=812600)
    Wait(3.0)
    DisplayDialog(text=30010, anchor_entity=0, display_distance=5.0)


@RestartOnRest(12022621)
def Event_12022621(_, flag: uint, asset: uint, asset_1: uint):
    """Event 12022621"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, vfx_id=200, model_point=812070)
    CreateAssetVFX(asset, vfx_id=201, model_point=812070)
    CreateAssetVFX(asset_1, vfx_id=200, model_point=812070)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    EnableAnimations(PLAYER)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9524, entity=asset))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    RotateToFaceEntity(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    DisableAnimations(PLAYER)
    Wait(1.2999999523162842)
    EnableNetworkFlag(flag)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, vfx_id=200, model_point=812070)
    CreateAssetVFX(asset, vfx_id=201, model_point=812070)
    CreateAssetVFX(asset_1, vfx_id=200, model_point=812070)
    Wait(2.0)
    EnableAnimations(PLAYER)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(1.2999999523162842)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, vfx_id=200, model_point=812070)
    CreateAssetVFX(asset, vfx_id=201, model_point=812070)
    CreateAssetVFX(asset_1, vfx_id=200, model_point=812070)
    End()


@ContinueOnRest(12022629)
def Event_12022629():
    """Event 12022629"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    GotoIfFlagDisabled(Label.L1, flag=12020629)
    DisableNetworkFlag(12022630)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9525, entity=Assets.AEG237_062_3000))
    
    MAIN.Await(AND_2)
    
    RotateToFaceEntity(PLAYER, Assets.AEG237_062_3000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    EnableNetworkFlag(12022630)
    Wait(0.4000000059604645)
    SkipLinesIfSingleplayer(4)
    if FlagEnabled(12090800):
        BanishPhantoms(unknown=0)
    else:
        BanishInvaders(unknown=0)
    Wait(2.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12092400,
        model_point=-1,
        copy_draw_parent=0,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(12020629))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_15:
        return
    
    MAIN.Await(FlagEnabled(12022630))
    
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12022209,
        model_point=-1,
        copy_draw_parent=0,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Wait(5.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12092401,
        model_point=-1,
        copy_draw_parent=0,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Restart()


@ContinueOnRest(12022670)
def Event_12022670():
    """Event 12022670"""
    if ThisEventSlotFlagDisabled():
        DeleteAssetVFX(Assets.AEG099_510_9000)
        CreateAssetVFX(Assets.AEG099_510_9000, vfx_id=200, model_point=806870)
    DisableFlag(12022670)
    DisableFlag(12022671)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=Assets.AEG099_510_9000))
    
    MAIN.Await(AND_1)
    
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=Assets.AEG099_510_9000,
        display_distance=3.0,
        left_flag=12022670,
        right_flag=12022671,
        cancel_flag=12022671,
    )
    GotoIfFlagEnabled(Label.L6, flag=12022670)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableNetworkFlag(12022670)
    BanishInvaders(unknown=0)
    RotateToFaceEntity(PLAYER, Assets.AEG099_510_9000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    Wait(3.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12022670,
        model_point=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(12022670))
    
    Wait(3.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12022671,
        model_point=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=False,
    )
    Restart()


@RestartOnRest(12022580)
def Event_12022580():
    """Event 12022580"""
    RegisterLadder(start_climbing_flag=12020580, stop_climbing_flag=12020581, asset=Assets.AEG239_042_0500)
    RegisterLadder(start_climbing_flag=12020582, stop_climbing_flag=12020583, asset=Assets.AEG239_043_0500)
    RegisterLadder(start_climbing_flag=12020584, stop_climbing_flag=12020585, asset=Assets.AEG239_044_0500)


@RestartOnRest(12022680)
def Event_12022680():
    """Event 12022680"""
    CreateAssetVFX(Assets.AEG099_090_9002, vfx_id=100, model_point=800)
    CreateAssetVFX(Assets.AEG099_090_9003, vfx_id=100, model_point=800)


@RestartOnRest(12022200)
def Event_12022200(_, region: uint, character: uint, special_effect_id: int):
    """Event 12022200"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(OR_1)
    AND_4.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_4)
    
    RemoveSpecialEffect(character, special_effect_id)


@RestartOnRest(12022404)
def Event_12022404():
    """Event 12022404"""
    if ThisEventSlotFlagEnabled():
        return
    OR_15.Add(HasAIStatus(12020404, ai_status=AIStatusType.Battle))
    OR_15.Add(HasAIStatus(12020494, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_15)
    
    ChangePatrolBehavior(12020405, patrol_information_id=12023405)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(12022300)
def Event_12022300(_, character: uint, region: uint, seconds: float):
    """Event 12022300"""
    if ThisEventSlotFlagEnabled():
        EnableCharacter(character)
        End()
    DisableCharacter(character)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(OR_1)
    AND_4.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_4)
    
    Wait(seconds)
    EnableCharacter(character)
    End()


@RestartOnRest(12022350)
def Event_12022350(_, character: uint, character_1: uint):
    """Event 12022350"""
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=60.0))
    AND_1.Add(CharacterHasSpecialEffect(character, 5080))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=30)
    AddSpecialEffect(character_1, 13190)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12022360)
def Event_12022360(_, character: uint, character_1: uint):
    """Event 12022360"""
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=60.0))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character_1, 13190)
    WaitFrames(frames=30)
    Restart()


@RestartOnRest(12022370)
def Event_12022370():
    """Event 12022370"""
    if ThisEventSlotFlagEnabled():
        return
    OR_15.Add(HasAIStatus(Characters.AncestralFollower11, ai_status=AIStatusType.Battle))
    OR_15.Add(HasAIStatus(Characters.AncestralFollower12, ai_status=AIStatusType.Battle))
    OR_15.Add(HasAIStatus(12020390, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_15)
    
    ForceAnimation(12020390, 30003, loop=True)
    End()


@RestartOnRest(12022371)
def Event_12022371():
    """Event 12022371"""
    EndIffSpecialStandbyEndedFlagEnabled(character=12020390)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=12020390, radius=6.0))
    AND_1.Add(CharacterBackreadEnabled(12020390))
    OR_11.Add(CharacterHasSpecialEffect(12020390, 5080))
    OR_11.Add(CharacterHasSpecialEffect(12020390, 5450))
    AND_1.Add(OR_11)
    AND_4.Add(CharacterHasSpecialEffect(12020390, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90160))
    AND_5.Add(CharacterHasSpecialEffect(12020390, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90162))
    AND_6.Add(CharacterHasSpecialEffect(12020390, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90161))
    AND_7.Add(CharacterHasSpecialEffect(12020390, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90162))
    AND_8.Add(CharacterHasSpecialEffect(12020390, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(12020390, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=12020390, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=12020390, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=12020390, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=12020390, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=12020390, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=12020390, state_info=260))
    OR_2.Add(CharacterDead(Characters.AncestralFollower12))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetSpecialStandbyEndedFlag(character=12020390, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(12020390, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(12020390, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(0.0)
    ForceAnimation(12020390, 20003, loop=True)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(12022372)
def Event_12022372():
    """Event 12022372"""
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.AncestralFollowerShaman0)
    ForceAnimation(Characters.AncestralFollowerShaman0, 30003, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.AncestralFollowerShaman0, radius=6.0))
    AND_1.Add(CharacterBackreadEnabled(Characters.AncestralFollowerShaman0))
    OR_11.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman0, 5080))
    OR_11.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman0, 5450))
    AND_1.Add(OR_11)
    AND_4.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman0, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman0, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman0, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman0, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman0, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AncestralFollowerShaman0, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman0, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman0, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman0, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman0, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman0, state_info=260))
    AND_13.Add(CharacterDead(12020360))
    AND_13.Add(CharacterDead(Characters.AncestralFollower20))
    AND_13.Add(CharacterDead(Characters.AncestralFollower21))
    OR_2.Add(AND_13)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=Characters.AncestralFollowerShaman0, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman0, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(0.0)
    ForceAnimation(Characters.AncestralFollowerShaman0, 20003, loop=True)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(12022373)
def Event_12022373():
    """Event 12022373"""
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.AncestralFollowerShaman1)
    ForceAnimation(Characters.AncestralFollowerShaman1, 30003, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.AncestralFollowerShaman1, radius=6.0))
    AND_1.Add(CharacterBackreadEnabled(Characters.AncestralFollowerShaman1))
    OR_11.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman1, 5080))
    OR_11.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman1, 5450))
    AND_1.Add(OR_11)
    AND_4.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman1, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman1, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman1, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman1, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.AncestralFollowerShaman1, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AncestralFollowerShaman1, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.AncestralFollowerShaman1, state_info=260))
    AND_13.Add(CharacterDead(Characters.AncestralFollower22))
    AND_13.Add(CharacterDead(Characters.AncestralFollower23))
    AND_13.Add(CharacterDead(Characters.AncestralFollower24))
    OR_2.Add(AND_13)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=Characters.AncestralFollowerShaman1, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.AncestralFollowerShaman1, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(0.0)
    ForceAnimation(Characters.AncestralFollowerShaman1, 20003, loop=True)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(12022400)
def Event_12022400(_, character: uint, character_1: uint, region: uint):
    """Event 12022400"""
    AND_15.Add(CharacterAlive(character_1))
    SkipLinesIfConditionTrue(1, AND_15)
    DisableCharacter(character)
    AND_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(PlayerNotInOwnWorld())
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16307))
    
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    DisableAnimations(character)
    WaitFrames(frames=5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 63010, skip_transition=True)
    AddSpecialEffect(character_1, 16316)
    Wait(4.400000095367432)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    EnableAI(character_1)
    SetNest(character_1, region=region)


@RestartOnRest(12022419)
def Event_12022419(_, character: uint, character_1: uint, region: uint):
    """Event 12022419"""
    AND_15.Add(CharacterAlive(character_1))
    SkipLinesIfConditionTrue(1, AND_15)
    DisableCharacter(character)
    AND_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(PlayerNotInOwnWorld())
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16309))
    
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    DisableAnimations(character)
    WaitFrames(frames=10)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 20015, skip_transition=True)
    AddSpecialEffect(character_1, 16316)
    Wait(5.199999809265137)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    SetNest(character_1, region=region)


@RestartOnRest(12022440)
def Event_12022440(_, character: uint, character_1: uint, patrol_information_id: uint):
    """Event 12022440"""
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ReplanAI(character_1)
    AddSpecialEffect(character_1, 5000)
    ChangePatrolBehavior(character_1, patrol_information_id=patrol_information_id)


@ContinueOnRest(12022502)
def Event_12022502():
    """Event 12022502"""
    DisableNetworkSync()
    AND_2.Add(FlagEnabled(12020800))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9710, entity=Assets.AEG237_018_5000))
    
    MAIN.Await(AND_2)
    
    EnableFlag(12020502)
    Wait(0.10000000149011612)
    EnableFlag(9021)
    SetRespawnPoint(respawn_point=12032502)
    SaveRequest()
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=12020000,
        cutscene_flags=0,
        move_to_region=12032502,
        map_id=12030000,
        player_id=10000,
        unk_20_24=12020000,
        unk_24_25=False,
    )
    PlayCutscene(12020001, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFrames(frames=1)
    Wait(1.0)
    DisplayAreaWelcomeMessage(text=12030)


@ContinueOnRest(12022503)
def Event_12022503():
    """Event 12022503"""
    if FlagEnabled(12020502):
        DeleteAssetVFX(Assets.AEG099_060_9000, erase_root=False)
        End()
    
    MAIN.Await(FlagEnabled(71220))
    
    DeleteAssetVFX(Assets.AEG099_060_9000)
    CreateAssetVFX(Assets.AEG099_060_9000, vfx_id=100, model_point=6400)


@ContinueOnRest(12020510)
def Event_12020510():
    """Event 12020510"""
    CommonFunc_90005500(
        0,
        flag=12020520,
        flag_1=12020521,
        left=5,
        asset=Assets.AEG239_010_0501,
        asset_1=m60_49_Assets.AEG239_020_2000,
        obj_act_id=1049403521,
        asset_2=Assets.AEG239_021_0501,
        obj_act_id_1=12023522,
        region=12022521,
        region_1=12022522,
        flag_2=12020522,
        flag_3=12022523,
        left_1=12020524,
    )
    CommonFunc_90005500(
        0,
        12020525,
        12020526,
        4,
        12021525,
        1045371526,
        1045373526,
        12021527,
        12023527,
        1045372526,
        12022527,
        12020527,
        12020528,
        0,
    )


@ContinueOnRest(12020519)
def Event_12020519():
    """Event 12020519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(12020510)
    DisableFlag(12020520)
    EnableFlag(12020525)
    EnableFlag(12020530)


@ContinueOnRest(12020500)
def Event_12020500():
    """Event 12020500"""
    if FlagEnabled(12020570):
        return
    Wait(0.5)
    DisableAssetActivation(m60_49_Assets.AEG239_020_2000, obj_act_id=239020)
    
    MAIN.Await(FlagEnabled(12020570))
    
    EnableAssetActivation(m60_49_Assets.AEG239_020_2000, obj_act_id=239020)


@RestartOnRest(12022850)
def Event_12022850():
    """Event 12022850"""
    if FlagEnabled(12020850):
        return
    OR_1.Add(HealthValue(Characters.MimicTear) <= 0)
    OR_1.Add(HealthValue(Characters.SilverTear4) <= 0)
    
    MAIN.Await(OR_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.MimicTear, 888880000, sound_type=SoundType.s_SFX)
    OR_5.Add(CharacterDead(Characters.MimicTear))
    OR_5.Add(CharacterDead(Characters.SilverTear4))
    
    MAIN.Await(OR_5)
    
    Kill(Characters.MimicTear, award_runes=True)
    WaitFrames(frames=1)
    KillBossAndDisplayBanner(character=Characters.MimicTear, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(12020850)
    EnableFlag(9134)
    if PlayerInOwnWorld():
        EnableFlag(91134)


@RestartOnRest(12022860)
def Event_12022860():
    """Event 12022860"""
    GotoIfFlagDisabled(Label.L0, flag=12020850)
    DisableCharacter(Characters.MimicTear)
    DisableAnimations(Characters.MimicTear)
    Kill(Characters.MimicTear)
    DisableCharacter(Characters.SilverTear4)
    DisableAnimations(Characters.SilverTear4)
    Kill(Characters.SilverTear4)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_10.Add(ThisEventSlotFlagEnabled())
    AND_10.Add(PlayerNotInOwnWorld())
    if AND_10:
        return
    if PlayerInOwnWorld():
        EnableThisSlotFlag()
    DisableAI(Characters.MimicTear)
    DisableAI(Characters.SilverTear4)
    GotoIfFlagEnabled(Label.L1, flag=12020851)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12022851))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.SilverTear4, attacker=0))
    OR_1.Add(CharacterHasStateInfo(character=Characters.SilverTear4, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.SilverTear4, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.SilverTear4, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.SilverTear4, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.SilverTear4, state_info=260))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(12020851)
    GotoIfPlayerNotInOwnWorld(Label.L15)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(12025850, authority_level=UpdateAuthority.Forced)

    # --- Label 15 --- #
    DefineLabel(15)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(12022855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12022850))
    
    MAIN.Await(AND_2)
    
    GotoIfPlayerNotInOwnWorld(Label.L16)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(12025850, authority_level=UpdateAuthority.Forced)

    # --- Label 16 --- #
    DefineLabel(16)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    SetAIParamID(Characters.MimicTear, ai_param_id=90603100)
    EnableAI(Characters.SilverTear4)
    ForceAnimation(Characters.SilverTear4, 20010)
    if PlayerInOwnWorld():
        CopyPlayerCharacterData(source_character=PLAYER, dest_characterentity=Characters.MimicTear)
    SetNetworkUpdateRate(Characters.MimicTear, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNest(Characters.MimicTear, region=12022852)
    Wait(8.0)
    DisableCharacter(Characters.SilverTear4)
    DisableAI(Characters.SilverTear4)
    EnableAI(Characters.MimicTear)
    AND_8.Add(CharacterDead(Characters.MimicTear))
    SkipLinesIfConditionTrue(1, AND_8)
    EnableBossHealthBar(Characters.MimicTear, name=903320000)
    EnableNetworkFlag(12022858)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(12022865)
def Event_12022865(_, character: uint, character_1: uint, region: uint):
    """Event 12022865"""
    AND_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(PlayerNotInOwnWorld())
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16307))
    
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    SetNest(character_1, region=region)
    DisableAnimations(character)
    WaitFrames(frames=15)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 63010, skip_transition=True)
    AddSpecialEffect(character_1, 16316)
    Wait(4.0)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)


@RestartOnRest(12022869)
def Event_12022869(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 12022869"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(FlagEnabled(left))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(flag):
        return RESTART
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(flag):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    BanishInvaders(unknown=0)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))
    
    MAIN.Await(AND_10)
    
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(12022899)
def Event_12022899():
    """Event 12022899"""
    Event_12022869(
        0,
        flag=12020850,
        entity=Assets.AEG099_002_9000,
        region=12022850,
        flag_1=12022855,
        character=12025850,
        action_button_id=10000,
        left=0,
        region_1=12022851,
    )
    CommonFunc_9005801(
        0,
        flag=12020850,
        entity=Assets.AEG099_002_9000,
        region=12022850,
        flag_1=12022855,
        flag_2=12022856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=12020850, asset=Assets.AEG099_002_9000, model_point=8, right=0)
    CommonFunc_9005812(0, flag=12020850, asset=Assets.AEG099_002_9001, model_point=8, right=0, model_point_1=0)
    CommonFunc_9005822(0, 12020850, 921100, 12022855, 12022856, 12022858, 12022852, 0, 0)


@RestartOnRest(12022800)
def Event_12022800():
    """Event 12022800"""
    if FlagEnabled(12020800):
        return
    AND_1.Add(HealthValue(Characters.Gargoyle0) <= 0)
    AND_1.Add(HealthValue(Characters.Gargoyle1) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Gargoyle0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.Gargoyle0))
    AND_2.Add(CharacterDead(Characters.Gargoyle1))
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.Gargoyle0, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(12020800)
    EnableFlag(9110)
    if PlayerInOwnWorld():
        EnableFlag(61110)


@RestartOnRest(12022810)
def Event_12022810():
    """Event 12022810"""
    GotoIfFlagDisabled(Label.L0, flag=12020800)
    DisableCharacter(Characters.Gargoyle0)
    DisableAnimations(Characters.Gargoyle0)
    Kill(Characters.Gargoyle0)
    DisableCharacter(Characters.Gargoyle1)
    DisableAnimations(Characters.Gargoyle1)
    Kill(Characters.Gargoyle1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Gargoyle0)
    DisableAI(Characters.Gargoyle1)
    SetNetworkUpdateRate(Characters.Gargoyle0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.Gargoyle0, 30002)
    GotoIfFlagEnabled(Label.L1, flag=12020801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12022801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Gargoyle0, attacker=0))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Gargoyle0, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Gargoyle0, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Gargoyle0, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Gargoyle0, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.Gargoyle0, state_info=260))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(12020801)
    ForceAnimation(Characters.Gargoyle0, 20002)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(12022805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12022800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.Gargoyle0, 20002)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Gargoyle0)
    EnableBossHealthBar(Characters.Gargoyle0, name=904770000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(12022820)
def Event_12022820():
    """Event 12022820"""
    if FlagEnabled(12020800):
        return
    ForceAnimation(Characters.Gargoyle1, 30003, loop=True)
    DisableFlag(12022820)
    AND_1.Add(HealthRatio(Characters.Gargoyle0) <= 0.550000011920929)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Characters.Gargoyle1, 20003, loop=True)
    WaitFrames(frames=1)
    EnableAI(Characters.Gargoyle1)
    SetNetworkUpdateRate(Characters.Gargoyle1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(5.0)
    EnableBossHealthBar(Characters.Gargoyle1, name=904770001, bar_slot=1)
    AddSpecialEffect(Characters.Gargoyle0, 17648)
    AddSpecialEffect(Characters.Gargoyle1, 17648)
    EnableFlag(12022820)


@RestartOnRest(12022821)
def Event_12022821():
    """Event 12022821"""
    if FlagEnabled(12020800):
        return
    AND_1.Add(FlagEnabled(12022820))
    OR_1.Add(CharacterDead(Characters.Gargoyle0))
    OR_1.Add(CharacterDead(Characters.Gargoyle1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(Characters.Gargoyle0, 17648)
    RemoveSpecialEffect(Characters.Gargoyle1, 17648)


@RestartOnRest(12022849)
def Event_12022849():
    """Event 12022849"""
    CommonFunc_9005811(0, flag=12020800, asset=Assets.AEG099_002_9003, model_point=5, right=12020801)
    CommonFunc_9005822(
        0,
        flag=12020800,
        bgm_boss_conv_param_id=931000,
        flag_1=12022805,
        flag_2=12022806,
        right=0,
        flag_3=12022820,
        left=0,
        left_1=0,
    )
    CommonFunc_9005800(
        0,
        flag=12020800,
        entity=Assets.AEG099_002_9002,
        region=12022800,
        flag_1=12022805,
        character=12025800,
        action_button_id=10000,
        left=12020801,
        region_1=12022801,
    )
    CommonFunc_9005801(
        0,
        flag=12020800,
        entity=Assets.AEG099_002_9002,
        region=12022800,
        flag_1=12022805,
        flag_2=12022806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=12020800, asset=Assets.AEG099_002_9002, model_point=3, right=12020801)
    CommonFunc_9005822(0, 12020800, 931000, 12022805, 12022806, 0, 12022802, 0, 0)


@RestartOnRest(12020700)
def Event_12020700(_, character: uint, asset: uint, asset_1: uint):
    """Event 12020700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4060):
        DisableFlag(12029002)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4065)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    DisableAsset(asset_1)
    
    MAIN.Await(FlagEnabled(4065))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=4060)
    GotoIfFlagEnabled(Label.L2, flag=4062)
    GotoIfFlagEnabled(Label.L3, flag=4063)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90107)
    EnableAsset(asset)
    EnableAsset(asset_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableAsset(asset)
    DisableAsset(asset_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    DisableAsset(asset_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4065))
    
    Restart()


@RestartOnRest(12020701)
def Event_12020701(_, entity: uint):
    """Event 12020701"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(4066, 4077))
    AND_1.Add(FlagEnabled(4065))
    AND_1.Add(FlagEnabled(12029016))
    AND_1.Add(FlagEnabled(4048))
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(4078)


@RestartOnRest(12023710)
def Event_12023710(_, character: uint, character_1: uint):
    """Event 12023710"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)


@RestartOnRest(12023711)
def Event_12023711(_, other_entity: uint, flag: uint):
    """Event 12023711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3503):
        return
    if FlagEnabled(12029060):
        return
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=5.0))
    
    EnableFlag(flag)
    
    MAIN.Await(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=5.0))
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(12023720)
def Event_12023720(_, character: uint):
    """Event 12023720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3600):
        DisableFlag(12029152)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L10, flag=3610)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3610))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3610))
    
    Restart()


@RestartOnRest(12023721)
def Event_12023721(_, other_entity: uint, radius: float, special_effect_id: int, flag: uint):
    """Event 12023721"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=radius))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, special_effect_id)
    Wait(3.0)
    Restart()

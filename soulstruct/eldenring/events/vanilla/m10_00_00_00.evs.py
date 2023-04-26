"""
Stormveil Castle

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
from .enums.m10_00_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=10000002, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=10000003, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=10000004, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=10000005, asset=Assets.AEG099_060_9005)
    RegisterGrace(grace_flag=10000006, asset=Assets.AEG099_060_9006)
    RegisterGrace(grace_flag=10000007, asset=Assets.AEG099_060_9007)
    RegisterGrace(grace_flag=10000008, asset=Assets.AEG099_060_9008)
    CommonFunc_90005100(
        0,
        flag=71001,
        flag_1=71002,
        asset=Assets.AEG099_090_9001,
        source_flag=77100,
        value=4,
        flag_2=78100,
        flag_3=78101,
        flag_4=78102,
        flag_5=78103,
        flag_6=78104,
        flag_7=78105,
        flag_8=78106,
        flag_9=78107,
        flag_10=78108,
        flag_11=78109,
    )
    CommonFunc_9005810(
        0,
        flag=10000800,
        grace_flag=10000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_9005810(
        0,
        flag=10000850,
        grace_flag=10000001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005511(
        0,
        flag=10000560,
        asset=Assets.AEG219_000_0500,
        obj_act_id=10003560,
        obj_act_id_1=219000,
        left=0,
    )
    CommonFunc_90005512(0, flag=10000560, region=10002560, region_1=10002561)
    CommonFunc_90005511(
        0,
        flag=10000562,
        asset=Assets.AEG219_000_0501,
        obj_act_id=10003562,
        obj_act_id_1=1219000,
        left=0,
    )
    CommonFunc_90005511(
        0,
        flag=10000566,
        asset=Assets.AEG219_000_0503,
        obj_act_id=10003566,
        obj_act_id_1=219000,
        left=0,
    )
    CommonFunc_90005512(0, flag=10000566, region=10002566, region_1=10002567)
    CommonFunc_90005510(
        0,
        flag=10000564,
        asset=Assets.AEG219_000_0502,
        obj_act_id=10003564,
        obj_act_id_1=219003,
        text=208010,
        left=0,
    )
    Event_10002580()
    Event_10002500()
    Event_10002501()
    Event_10002510()
    CommonFunc_90005501(
        0,
        flag=10000510,
        flag_1=10000511,
        left=0,
        asset=Assets.AEG219_020_0500,
        asset_1=Assets.AEG219_010_0504,
        asset_2=Assets.AEG219_010_0503,
        flag_2=10000512,
    )
    CommonFunc_90005501(
        0,
        flag=10000515,
        flag_1=10000516,
        left=1,
        asset=Assets.AEG219_020_0501,
        asset_1=Assets.AEG219_010_0502,
        asset_2=Assets.AEG219_010_0501,
        flag_2=10000517,
    )
    CommonFunc_90005501(
        0,
        flag=10000520,
        flag_1=10000521,
        left=0,
        asset=Assets.AEG219_023_0500,
        asset_1=Assets.AEG219_010_0506,
        asset_2=Assets.AEG219_010_0505,
        flag_2=10000522,
    )
    CommonFunc_90005502(0, flag=10000514, asset=Assets.AEG219_010_0504, region=10002512)
    CommonFunc_90005502(0, flag=10000524, asset=Assets.AEG219_010_0506, region=10002522)
    CommonFunc_90005690(0, region=10002610)
    CommonFunc_90005691(0, region=10002610)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005632(0, flag=580040, asset=Assets.AEG099_388_5000, item_lot=80040)
    CommonFunc_90005570(0, flag=60836, gesture_param_id=94, asset=Assets.AEG099_610_9048, left=0, left_1=1, right=0)
    CommonFunc_90005560(0, flag=10000698, asset=Assets.AEG099_635_9000, left=0)
    Event_10002690()
    CommonFunc_90005620(
        0,
        flag=10000570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=10002570,
        cancel_flag__right_flag=10002571,
        right=10002572,
    )
    CommonFunc_90005621(0, flag=10000570, asset=Assets.AEG099_272_9000)
    CommonFunc_90005621(0, flag=10000570, asset=Assets.AEG099_272_9003)
    CommonFunc_90005620(
        0,
        flag=10000575,
        asset=Assets.AEG027_079_9001,
        asset_1=Assets.AEG027_216_9001,
        asset_2=0,
        left_flag=10002575,
        cancel_flag__right_flag=10002576,
        right=10002577,
    )
    CommonFunc_90005621(0, flag=10000575, asset=Assets.AEG099_272_9001)
    CommonFunc_90005621(0, flag=10000575, asset=Assets.AEG099_272_9002)
    Event_10002800()
    Event_10002810()
    Event_10002811()
    Event_10002849()
    Event_10002820(0, region=10002820, special_effect=14790, special_effect_1=14791)
    Event_10002821(0, region=10002821, special_effect=14792, special_effect_1=14793)
    Event_10002824(0, region=10002824, special_effect=14794, special_effect_1=14795)
    Event_10002825(0, region=10002825, special_effect=14796, special_effect_1=14797)
    Event_10002850()
    Event_10002860()
    Event_10002861()
    Event_10002870()
    Event_10002889()
    Event_10002350(0, character=Characters.CastleGuard43, region=10002430, seconds=0.0, flag=10002350)
    Event_10002350(10, character=Characters.Commoner6, region=10002234, seconds=0.0, flag=10002360)
    Event_10002350(1, character=10000603, region=10002263, seconds=0.0, flag=10002351)
    Event_10002350(2, character=10005680, region=10002205, seconds=0.0, flag=10002352)
    Event_10002350(3, character=Characters.BanishedKnight2, region=10002206, seconds=0.0, flag=10002353)
    Event_10002350(4, character=Characters.Dog0, region=10002202, seconds=0.0, flag=10002354)
    Event_10002350(5, character=Characters.SmallerDog, region=10002202, seconds=1.0, flag=10002355)
    Event_10002350(8, character=Characters.GraftedScion, region=10002280, seconds=0.0, flag=10002358)
    Event_10002350(9, character=10005370, region=10002217, seconds=0.0, flag=10002359)
    Event_10002350(11, character=10005360, region=10002219, seconds=0.0, flag=10002361)
    Event_1002200()
    Event_10002330(0, character=Characters.BladedTalonEagle6, asset=Assets.AEG217_063_9053)
    Event_10002330(1, character=Characters.BladedTalonEagle7, asset=Assets.AEG217_063_9054)
    Event_10002330(2, character=Characters.BladedTalonEagle8, asset=Assets.AEG217_063_9055)
    Event_10002330(3, character=Characters.BladedTalonEagle9, asset=Assets.AEG217_063_9056)
    Event_10002340(0, character=Characters.BladedTalonEagle6, asset=Assets.AEG217_063_9053)
    Event_10002340(1, character=Characters.BladedTalonEagle7, asset=Assets.AEG217_063_9054)
    Event_10002340(2, character=Characters.BladedTalonEagle8, asset=Assets.AEG217_063_9055)
    Event_10002340(3, character=Characters.BladedTalonEagle9, asset=Assets.AEG217_063_9056)
    Event_10002290(0, character=Characters.SmallLivingPot0)
    Event_10002290(1, character=Characters.SmallLivingPot1)
    Event_10002290(2, character=Characters.SmallLivingPot2)
    Event_10002290(3, character=Characters.SmallLivingPot3)
    Event_10002290(4, character=Characters.SmallLivingPot4)
    Event_10002290(5, character=Characters.SmallLivingPot5)
    Event_10002290(6, character=Characters.SmallLivingPot6)
    Event_10002310()
    Event_10002480()
    Event_10002423(0, character=Characters.CastleGuard39)
    Event_10002423(1, character=Characters.CastleGuard40)
    Event_10002423(2, character=Characters.CastleGuard41)
    Event_10002423(3, character=Characters.CastleGuard42)
    Event_10002311(
        0,
        character=Characters.CastleGuard12,
        animation_id=30006,
        animation_id_1=20006,
        region=10002311,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_10002311(
        1,
        character=Characters.CastleGuard13,
        animation_id=30006,
        animation_id_1=20006,
        region=10002311,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_10002311(
        2,
        character=Characters.CastleGuard14,
        animation_id=30006,
        animation_id_1=20006,
        region=10002311,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_10002311(
        3,
        character=Characters.CastleGuard15,
        animation_id=30007,
        animation_id_1=20007,
        region=10002311,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(0, flag=10000280, character=Characters.GraftedScion, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=10000289, character=Characters.LionGuardian, item_lot=10001085, seconds=1.0, left=0)
    Event_11002291(0, character=Characters.UlceratedTreeSpirit, region=10002291, seconds=3.0)
    CommonFunc_90005300(
        0,
        flag=10000291,
        character=Characters.UlceratedTreeSpirit,
        item_lot=10001095,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(0, flag=10000498, character=Characters.CrucibleKnight, item_lot=10001295, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=10000495, character=Characters.Scarab0, item_lot=40170, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=10000496, character=Characters.Scarab1, item_lot=40172, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=10000497, character=Characters.Scarab2, item_lot=40174, seconds=0.0, left=0)
    CommonFunc_90005780(
        0,
        flag=10000800,
        summon_flag=10002160,
        dismissal_flag=10002161,
        character=Characters.NepheliLoux2,
        sign_type=20,
        region=10002730,
        right=10009709,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=10000800, flag_1=10002160, flag_2=10002161, character=Characters.NepheliLoux2)
    CommonFunc_90005782(
        0,
        flag=10002160,
        region=10002805,
        character=Characters.NepheliLoux2,
        target_entity=10002805,
        region_1=10002809,
        animation=0,
    )
    CommonFunc_90005780(
        0,
        flag=10000850,
        summon_flag=10002164,
        dismissal_flag=10002165,
        character=Characters.SorcererRogier2,
        sign_type=20,
        region=10002722,
        right=10009614,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=10000850, flag_1=10002164, flag_2=10002165, character=Characters.SorcererRogier2)
    CommonFunc_90005782(
        0,
        flag=10002164,
        region=10002855,
        character=Characters.SorcererRogier2,
        target_entity=10002855,
        region_1=10002859,
        animation=0,
    )
    CommonFunc_90005785(
        0,
        flag=10000850,
        flag_1=10002164,
        flag_2=10002165,
        character=Characters.SorcererRogier2,
        other_entity=10002722,
        region=0,
        radius=75.0,
    )
    Event_10002910()
    CommonFunc_90005703(
        0,
        character=Characters.GatekeeperGostoc0,
        flag=3261,
        flag_1=3262,
        flag_2=10009504,
        flag_3=3261,
        first_flag=3260,
        last_flag=3263,
        right=-1,
    )
    CommonFunc_90005703(
        0,
        character=Characters.GatekeeperGostoc1,
        flag=3261,
        flag_1=3262,
        flag_2=10009385,
        flag_3=3261,
        first_flag=3260,
        last_flag=3263,
        right=-1,
    )
    CommonFunc_90005703(
        0,
        character=Characters.GatekeeperGostoc2,
        flag=3261,
        flag_1=3262,
        flag_2=10009386,
        flag_3=3261,
        first_flag=3260,
        last_flag=3263,
        right=-1,
    )
    CommonFunc_90005703(
        0,
        character=Characters.GatekeeperGostoc3,
        flag=3261,
        flag_1=3262,
        flag_2=10009387,
        flag_3=3261,
        first_flag=3260,
        last_flag=3263,
        right=-1,
    )
    CommonFunc_90005703(
        0,
        character=Characters.GatekeeperGostoc4,
        flag=3261,
        flag_1=3262,
        flag_2=10009388,
        flag_3=3261,
        first_flag=3260,
        last_flag=3263,
        right=-1,
    )
    CommonFunc_90005703(
        0,
        character=Characters.GatekeeperGostoc5,
        flag=3261,
        flag_1=3262,
        flag_2=10009505,
        flag_3=3261,
        first_flag=3260,
        last_flag=3263,
        right=-1,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.GatekeeperGostoc0,
        flag=3261,
        flag_1=3260,
        flag_2=10009504,
        right=3,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.GatekeeperGostoc1,
        flag=3261,
        flag_1=3260,
        flag_2=10009385,
        right=3,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.GatekeeperGostoc2,
        flag=3261,
        flag_1=3260,
        flag_2=10009386,
        right=3,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.GatekeeperGostoc3,
        flag=3261,
        flag_1=3260,
        flag_2=10009387,
        right=3,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.GatekeeperGostoc4,
        flag=3261,
        flag_1=3260,
        flag_2=10009388,
        right=3,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.GatekeeperGostoc5,
        flag=3261,
        flag_1=3260,
        flag_2=10009505,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.GatekeeperGostoc0, flag=3263, first_flag=3260, last_flag=3263)
    CommonFunc_90005702(0, character=Characters.GatekeeperGostoc1, flag=3263, first_flag=3260, last_flag=3263)
    CommonFunc_90005702(0, character=Characters.GatekeeperGostoc2, flag=3263, first_flag=3260, last_flag=3263)
    CommonFunc_90005702(0, character=Characters.GatekeeperGostoc3, flag=3263, first_flag=3260, last_flag=3263)
    CommonFunc_90005702(0, character=Characters.GatekeeperGostoc4, flag=3263, first_flag=3260, last_flag=3263)
    CommonFunc_90005702(0, character=Characters.GatekeeperGostoc5, flag=3263, first_flag=3260, last_flag=3263)
    Event_10003724()
    Event_10003726()
    Event_10003728(0, region=10002716)
    RunCommonEvent(10003710)
    Event_10003711(0, first_flag=10002732, last_flag=10002735, flag=10002732, region=10002700)
    Event_10003711(1, first_flag=10002732, last_flag=10002735, flag=10002733, region=10002702)
    Event_10003711(2, first_flag=10002732, last_flag=10002735, flag=10002734, region=10002704)
    Event_10003711(3, first_flag=10002732, last_flag=10002735, flag=10002735, region=10002706)
    Event_10003715(
        0,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002732,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002736,
        region=10002701,
    )
    Event_10003715(
        1,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002733,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002737,
        region=10002703,
    )
    Event_10003715(
        2,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002734,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002738,
        region=10002705,
    )
    Event_10003715(
        3,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002735,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002739,
        region=10002707,
    )
    Event_10003720(0, flag=10009510, flag_1=10009390)
    Event_10003720(1, flag=10009511, flag_1=10009391)
    Event_10003720(2, flag=10009512, flag_1=10009392)
    Event_10003720(3, flag=10009513, flag_1=10009393)
    Event_10003729(0, region=10002701)
    Event_10003730()
    Event_10003734()
    Event_10003731()
    Event_10003732()
    Event_10003733()
    Event_10003738()
    Event_10000739()
    Event_10003736()
    Event_10003737()
    Event_10003775(0, character=Characters.NepheliLoux0, character_1=Characters.BanishedKnight7)
    CommonFunc_90005704(0, attacked_entity=Characters.NepheliLoux0, flag=4221, flag_1=4220, flag_2=10009701, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.NepheliLoux0,
        flag=4221,
        flag_1=4222,
        flag_2=10009701,
        flag_3=4221,
        first_flag=4220,
        last_flag=4224,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.NepheliLoux0, flag=4223, first_flag=4220, last_flag=4224)
    Event_10003776(0, character=Characters.NepheliLoux1)
    CommonFunc_90005704(0, attacked_entity=Characters.NepheliLoux1, flag=4221, flag_1=4220, flag_2=10009701, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.NepheliLoux1,
        flag=4221,
        flag_1=4222,
        flag_2=10009701,
        flag_3=4221,
        first_flag=4220,
        last_flag=4224,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.NepheliLoux1, flag=4223, first_flag=4220, last_flag=4224)
    Event_10003777()
    Event_10003778()
    Event_10003779()
    Event_10003780()
    Event_10003790(0, character=Characters.KennethHaight)
    Event_10000760(0, character=Characters.SorcererRogier0)
    Event_10000761()
    Event_10000762()
    Event_10000763(0, asset=Assets.AEG099_090_9004, radius=15.0)
    Event_10000764(0, character=Characters.SorcererRogier1, entity=Assets.AEG099_090_9004)
    Event_10003770(0, flag=78104, other_entity=Characters.TalkDummy2, flag_1=10009650)
    Event_10003771(0, other_entity=Characters.TalkDummy2, flag=10009650)
    Event_10003772(0, other_entity=Characters.TalkDummy2, flag=10009651)
    Event_10003773(0, other_entity=Characters.TalkDummy2, flag=10009651)
    Event_10003740(0, character=Characters.GodricktheGrafted, special_effect=9600, flag=10009204, seconds=0.5)
    Event_10003741(0, character=Characters.GodricktheGrafted, special_effect=9601, flag=10009201, seconds=0.5)
    Event_10003742(0, character=Characters.GodricktheGrafted, special_effect=9602, flag=10009202, seconds=0.5)
    Event_10003743(0, character=Characters.GodricktheGrafted, special_effect=9603, flag=10009203, seconds=0.5)
    Event_10003744(0, character=Characters.GodricktheGrafted, character_1=0, flag=9101, flag_1=10002805, distance=105.0)
    Event_10003745(0, character=Characters.DefeatedGodrick)
    CommonFunc_90005706(0, character=Characters.Commoner25, animation_id=930018, left=0)
    Event_10003500(0, region=10002740)
    Event_10003500(1, region=10002741)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.GatekeeperGostoc0)
    DisableBackread(Characters.GatekeeperGostoc1)
    DisableBackread(Characters.GatekeeperGostoc2)
    DisableBackread(Characters.GatekeeperGostoc3)
    DisableBackread(Characters.GatekeeperGostoc4)
    DisableBackread(Characters.GatekeeperGostoc5)
    DisableBackread(Characters.GatekeeperGostoc6)
    DisableBackread(Characters.SorcererRogier0)
    DisableBackread(Characters.DefeatedGodrick)
    DisableBackread(Characters.KennethHaight)
    DisableBackread(Characters.NepheliLoux0)
    DisableBackread(Characters.BanishedKnight7)
    DisableBackread(Characters.NepheliLoux1)
    DisableBackread(Characters.Commoner25)
    Event_10000519()
    CommonFunc_90005260(0, character=Characters.Dummy1, region=0, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner0, region=10002218, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner1, region=10002218, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Commoner2, region=10002233, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner3, region=10002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Commoner4, region=10002233, radius=3.0, seconds=3.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner5, region=10002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner6, region=10002231, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner7, region=10002236, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Commoner8, region=10002209, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=10000210, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=10000211, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(0, character=10000220, animation_id=30001, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=10000221, animation_id=30002, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=10000222, animation_id=30001, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(
        0,
        character=Characters.Commoner9,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(0, character=10000224, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=10000225, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(
        0,
        character=Characters.Commoner10,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005261(0, character=10000227, region=10002255, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=10000228, region=10002255, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=10000229, region=10002255, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=10000230, region=10002255, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=10000231, region=10002255, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=10000232, region=10002255, radius=1.0, seconds=0.0, animation_id=-1)
    Event_10002240(
        0,
        character=Characters.Commoner11,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_10002240(
        1,
        character=Characters.Commoner12,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_10002240(
        2,
        character=Characters.Commoner13,
        animation_id=30001,
        animation_id_1=20001,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=1,
    )
    CommonFunc_90005251(0, character=Characters.Commoner14, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Commoner17, region=10002208, seconds=2.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner18, region=10002208, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner19, region=10002208, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner20, region=10002208, seconds=2.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner21, region=10002208, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner22, region=10002208, seconds=3.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner23, region=10002208, seconds=2.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner24, region=10002208, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard0, region=10002300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard1, region=10002300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard3, region=10002301, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.CastleGuard6, region=10002306, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.CastleGuard7, region=10002306, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard8, region=10002311, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.CastleGuard9, region=10002313, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.CastleGuard10,
        region=10002313,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005251(0, character=10000325, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.CastleGuard20, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=10000323, region=10002323, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.CastleGuard16, radius=4.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=10005334, region=10002230, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.CastleGuard17,
        region=10002330,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.CastleGuard18,
        region=10002330,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.CastleGuard19,
        region=10002334,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.CastleGuard21, region=10002351, seconds=2.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard22, region=10002351, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard23, region=10002351, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard24, region=10002351, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard25, region=10002351, seconds=2.0, animation_id=-1)
    CommonFunc_90005250(0, character=10000355, region=10002351, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1000393, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1000394, radius=5.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.CastleGuard27, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.CastleGuard28, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(0, character=10000405, animation_id=30000, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=10000406, animation_id=30000, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=10000407, animation_id=30000, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005201(
        0,
        character=Characters.CastleGuard32,
        animation_id=30006,
        animation_id_1=20006,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CastleGuard33, region=10002416, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard34, region=10002416, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard35, region=10002416, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.CastleGuard36,
        region=10002425,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.CastleGuard38, region=10002214, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.CastleGuard32,
        animation_id=30006,
        animation_id_1=20006,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CastleGuard31, region=10002616, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard44, region=10002238, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.CastleGuard45,
        animation_id=30006,
        animation_id_1=20006,
        region=10002207,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CastleGuard46,
        animation_id=30006,
        animation_id_1=20006,
        region=10002207,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.CastleGuard47,
        animation_id=30006,
        animation_id_1=20006,
        region=10002446,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.CastleGuard48, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CastleGuard49, region=10002214, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight0, region=10002260, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight1, region=10002710, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.BanishedKnight2,
        region=10002267,
        radius=5.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005250(0, character=Characters.BanishedKnight3, region=10002609, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight4, region=10002609, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight5, region=10002274, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight6, region=10002616, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle0, region=10002460, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.BladedTalonEagle1,
        region=10002461,
        radius=2.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.BladedTalonEagle2,
        region=10002461,
        radius=2.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle3, region=10002463, seconds=0.5, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle4, region=10002463, seconds=0.0, animation_id=3009)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle5, region=10002463, seconds=3.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle6, region=10002470, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle7, region=10002471, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle8, region=10002471, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle9, region=10002473, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle10, region=10002475, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=10000476, region=10002475, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle11, region=10002477, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle13, region=10002274, seconds=1.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.BladedTalonEagle14,
        animation_id=30010,
        animation_id_1=20010,
        region=10002486,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.GiantRat, region=10002285, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=10000285, region=10002285, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Bat, region=10002544, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Omen, region=10002213, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LionGuardian, region=10002220, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.CrucibleKnight, region=10002498, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle0, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle1, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle2, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle3, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle4, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle5, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle6, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle7, region=10002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=10000588, region=10002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle8, region=10002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle9, region=10002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle10, region=10002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle11, region=10002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle12, region=10002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle13, region=10002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Eagle14, region=10002212, seconds=0.0, animation_id=-1)
    Event_10003700(0, character=Characters.GatekeeperGostoc0, asset=Assets.AEG217_016_1000)
    Event_10003702(0, character=Characters.GatekeeperGostoc5)
    Event_10003703(0, character=Characters.GatekeeperGostoc6)
    Event_10003701(
        0,
        character=Characters.GatekeeperGostoc1,
        asset=Assets.AEG217_016_2000,
        flag=10009510,
        flag_1=10009390,
    )
    Event_10003701(
        1,
        character=Characters.GatekeeperGostoc2,
        asset=Assets.AEG217_016_4000,
        flag=10009511,
        flag_1=10009391,
    )
    Event_10003701(
        2,
        character=Characters.GatekeeperGostoc3,
        asset=Assets.AEG217_016_4001,
        flag=10009512,
        flag_1=10009392,
    )
    Event_10003701(
        3,
        character=Characters.GatekeeperGostoc4,
        asset=Assets.AEG217_016_5000,
        flag=10009513,
        flag_1=10009393,
    )
    Event_10003705(0, entity=Characters.GatekeeperGostoc0)
    Event_10003705(1, entity=Characters.GatekeeperGostoc1)
    Event_10003705(2, entity=Characters.GatekeeperGostoc2)
    Event_10003705(3, entity=Characters.GatekeeperGostoc3)
    Event_10003705(4, entity=Characters.GatekeeperGostoc4)
    Event_10003705(5, entity=Characters.GatekeeperGostoc5)
    Event_10003705(6, entity=Characters.GatekeeperGostoc6)


@RestartOnRest(10002281)
def Event_10002281(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 10002281"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    EnableInvincibility(character)
    AddSpecialEffect(character, 16296)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
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
    DisableInvincibility(character)


@ContinueOnRest(10002580)
def Event_10002580():
    """Event 10002580"""
    RegisterLadder(start_climbing_flag=10000580, stop_climbing_flag=10000581, asset=Assets.AEG219_060_0500)
    RegisterLadder(start_climbing_flag=10000582, stop_climbing_flag=10000583, asset=Assets.AEG219_061_4000)
    RegisterLadder(start_climbing_flag=10000584, stop_climbing_flag=10000585, asset=Assets.AEG219_064_0500)
    RegisterLadder(start_climbing_flag=10000586, stop_climbing_flag=10000587, asset=Assets.AEG219_065_0500)
    RegisterLadder(start_climbing_flag=10000588, stop_climbing_flag=10000589, asset=Assets.AEG219_066_0500)
    if FlagDisabled(2001):
        RegisterLadder(start_climbing_flag=10000590, stop_climbing_flag=10000591, asset=Assets.AEG219_067_4000)
    RegisterLadder(start_climbing_flag=10000592, stop_climbing_flag=10000593, asset=Assets.AEG219_068_0501)
    RegisterLadder(start_climbing_flag=10000594, stop_climbing_flag=10000595, asset=Assets.AEG219_069_0500)
    RegisterLadder(start_climbing_flag=10000596, stop_climbing_flag=10000597, asset=Assets.AEG219_070_0500)
    RegisterLadder(start_climbing_flag=10000598, stop_climbing_flag=10000599, asset=Assets.AEG219_071_0500)


@ContinueOnRest(10002500)
def Event_10002500():
    """Event 10002500"""
    AND_1.Add(FlagDisabled(10000500))
    AND_1.Add(FlagDisabled(10000501))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    EndOfAnimation(asset=Assets.AEG219_050_0500, animation_id=1)
    EndOfAnimation(asset=Assets.AEG219_030_0500, animation_id=1)
    DisableAssetActivation(Assets.AEG219_030_0500, obj_act_id=219030)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetActivation(Assets.AEG219_030_0500, obj_act_id=219030)
    
    MAIN.Await(FlagEnabled(10009355))
    
    EnableNetworkFlag(10000500)
    EnableFlag(10009355)
    Wait(2.0)
    DisableAssetActivation(Assets.AEG219_030_0500, obj_act_id=219030)
    Wait(2.0)
    ForceAnimation(Assets.AEG219_030_0500, 1)
    Wait(2.0)
    ForceAnimation(Assets.AEG219_050_0500, 1)


@ContinueOnRest(10002501)
def Event_10002501():
    """Event 10002501"""
    AND_1.Add(FlagDisabled(10000500))
    AND_1.Add(FlagDisabled(10000501))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    EndOfAnimation(asset=Assets.AEG219_050_0500, animation_id=1)
    DisableAssetActivation(Assets.AEG219_030_0500, obj_act_id=219030)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetActivation(Assets.AEG219_030_0500, obj_act_id=219030)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(AssetActivated(obj_act_id=10003501))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(10000501)
    EnableFlag(10009354)
    Wait(3.0)
    DisableAssetActivation(Assets.AEG219_030_0500, obj_act_id=219030)
    ForceAnimation(Assets.AEG219_050_0500, 1)


@ContinueOnRest(10002510)
def Event_10002510():
    """Event 10002510"""
    CommonFunc_90005500(
        0,
        flag=10000510,
        flag_1=10000511,
        left=0,
        asset=Assets.AEG219_020_0500,
        asset_1=Assets.AEG219_010_0504,
        obj_act_id=10003511,
        asset_2=Assets.AEG219_010_0503,
        obj_act_id_1=10003512,
        region=10002511,
        region_1=10002512,
        flag_2=10000512,
        flag_3=10000513,
        left_1=10000514,
    )
    CommonFunc_90005500(
        0,
        flag=10000515,
        flag_1=10000516,
        left=1,
        asset=Assets.AEG219_020_0501,
        asset_1=Assets.AEG219_010_0502,
        obj_act_id=10003516,
        asset_2=Assets.AEG219_010_0501,
        obj_act_id_1=10003517,
        region=10002516,
        region_1=10002517,
        flag_2=10000517,
        flag_3=10000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=10000520,
        flag_1=10000521,
        left=0,
        asset=Assets.AEG219_023_0500,
        asset_1=Assets.AEG219_010_0506,
        obj_act_id=10003521,
        asset_2=Assets.AEG219_010_0505,
        obj_act_id_1=10003522,
        region=10002521,
        region_1=10002522,
        flag_2=10000522,
        flag_3=10000523,
        left_1=10000524,
    )


@ContinueOnRest(10000519)
def Event_10000519():
    """Event 10000519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(10000515)
    EnableThisSlotFlag()


@RestartOnRest(1002200)
def Event_1002200():
    """Event 1002200"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.CastleGuard29, 10180))
    
    Wait(1.0)
    ForceAnimation(Characters.CastleGuard30, 3010)
    EnableThisSlotFlag()


@RestartOnRest(10002240)
def Event_10002240(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    left_4: uint,
):
    """Event 10002240"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    AND_9.Add(UnsignedEqual(left=left_4, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    if UnsignedNotEqual(left=left_4, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(10002290)
def Event_10002290(_, character: uint):
    """Event 10002290"""
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)


@RestartOnRest(11002291)
def Event_11002291(_, character: uint, region: uint, seconds: float):
    """Event 11002291"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, 30002)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20002)


@RestartOnRest(10002310)
def Event_10002310():
    """Event 10002310"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(Characters.LivingPot)
    ForceAnimation(Characters.LivingPot, 30000, loop=True)
    AND_1.Add(HasAIStatus(10005231, ai_status=AIStatusType.Battle))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10002222, min_target_count=0))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.LivingPot)
    EnableThisSlotFlag()
    ForceAnimation(Characters.LivingPot, 20000, wait_for_completion=True)
    ForceAnimation(Characters.LivingPot, 3004)


@RestartOnRest(10002311)
def Event_10002311(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 10002311"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_3.Add(CharacterHasSpecialEffect(PLAYER, 10000))
    AND_3.Add(OR_3)
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(AND_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(10002320)
def Event_10002320():
    """Event 10002320"""
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(10000294)
    DisableAI(10000294)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10002294))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=10000294))
    OR_2.Add(CharacterHasStateInfo(character=10000294, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=10000294, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=10000294, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=10000294, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=10000294, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableCharacter(10000294)
    EnableAI(10000294)
    ForceAnimation(10000294, 20000, wait_for_completion=True)


@RestartOnRest(10002330)
def Event_10002330(_, character: uint, asset: uint):
    """Event 10002330"""
    if ThisEventSlotFlagEnabled():
        return
    EnableNetworkSync()
    EnableAsset(asset)
    AttachAssetToCharacter(character=character, model_point=50, asset=asset)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 10941))
    
    DisableAsset(asset)
    DestroyAsset(asset, request_slot=0)
    EnableThisSlotFlag()


@RestartOnRest(10002340)
def Event_10002340(_, character: uint, asset: uint):
    """Event 10002340"""
    if ThisEventSlotFlagEnabled():
        return
    EnableNetworkSync()
    AddSpecialEffect(character, 10940)
    AddSpecialEffect(character, 10943)
    
    MAIN.Await(AssetDestroyed(asset))
    
    RemoveSpecialEffect(character, 10940)
    RemoveSpecialEffect(character, 10943)
    SkipLinesIfCharacterHasSpecialEffect(2, character=character, special_effect=10941)
    SkipLinesIfCharacterHasSpecialEffect(1, character=character, special_effect=10936)
    ForceAnimation(character, 20005)


@RestartOnRest(10002350)
def Event_10002350(_, character: uint, region: uint, seconds: float, flag: uint):
    """Event 10002350"""
    if FlagEnabled(flag):
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)


@RestartOnRest(10002423)
def Event_10002423(_, character: uint):
    """Event 10002423"""
    Kill(character)


@RestartOnRest(10002460)
def Event_10002460():
    """Event 10002460"""
    MAIN.Await(TimeOfDayInRange(earliest=(19, 0, 0), latest=(5, 59, 0)))
    
    AddSpecialEffect(10005460, 10930)
    WaitUntilRandomTimeOfDay(earliest=(6, 0, 0), latest=(18, 59, 0))
    RemoveSpecialEffect(10005460, 10930)
    Restart()


@RestartOnRest(10002480)
def Event_10002480():
    """Event 10002480"""
    Kill(Characters.BladedTalonEagle12)


@ContinueOnRest(1002700)
def Event_1002700(_, character: uint, flag: uint, flag_1: uint):
    """Event 1002700"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@ContinueOnRest(1002680)
def Event_1002680():
    """Event 1002680"""
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=10002680))
    AND_1.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    
    MAIN.Await(AND_1)
    
    EnableFlag(10002681)
    Wait(2.0)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=10002680))
    AND_2.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    
    MAIN.Await(not AND_2)
    
    DisableFlag(10002681)
    Wait(2.0)
    Restart()


@RestartOnRest(10002670)
def Event_10002670(_, tutorial_param_id: int, flag: uint):
    """Event 10002670"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    OR_15.Add(PlayerHasWeapon(33000000, including_storage=True))
    OR_15.Add(PlayerHasWeapon(33210000, including_storage=True))
    OR_15.Add(PlayerHasWeapon(34000000, including_storage=True))
    OR_15.Add(PlayerHasWeapon(34040000, including_storage=True))
    if OR_15:
        return
    OR_1.Add(PlayerHasWeapon(33000000, including_storage=True))
    OR_1.Add(PlayerHasWeapon(33210000, including_storage=True))
    OR_1.Add(PlayerHasWeapon(34000000, including_storage=True))
    OR_1.Add(PlayerHasWeapon(34040000, including_storage=True))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    Wait(1.0)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9101, flag=flag, bit_count=1)


@RestartOnRest(10002671)
def Event_10002671(_, tutorial_param_id: int, flag: uint):
    """Event 10002671"""
    if Multiplayer():
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    AND_1.Add(Singleplayer())
    AND_1.Add(PlayerDoesNotHaveGood(9111, including_storage=True))
    AND_1.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(10002672)
def Event_10002672(_, tutorial_param_id: int, flag: uint):
    """Event 10002672"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerHasGood(9500))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    AND_1.Add(PlayerDoesNotHaveGood(9114))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9114, flag=flag, bit_count=1)


@RestartOnRest(10002673)
def Event_10002673(_, tutorial_param_id: int, flag: uint, flag_1: uint, tutorial_param_id_1: int):
    """Event 10002673"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    AND_1.Add(PlayerDoesNotHaveGood(9116, including_storage=True))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    EnableFlag(flag_1)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9116, flag=flag, bit_count=1)


@RestartOnRest(10002680)
def Event_10002680():
    """Event 10002680"""
    CreateAssetVFX(Assets.AEG099_090_9002, vfx_id=100, model_point=800)


@RestartOnRest(10002690)
def Event_10002690():
    """Event 10002690"""
    if FlagDisabled(2001):
        return
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(2001))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9980, entity=Assets.AEG099_090_9000))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=90000, anchor_entity=Assets.AEG099_090_9000)
    Wait(1.0)
    Restart()


@RestartOnRest(10002691)
def Event_10002691():
    """Event 10002691"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(10007490):
        return
    
    MAIN.Await(FlagState(FlagSetting.On, FlagType.RelativeToThisEventSlot, 10007490))
    
    AwardGesture(gesture_param_id=94)


@RestartOnRest(10003500)
def Event_10003500(_, region: uint):
    """Event 10003500"""
    DisableNetworkSync()
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


@ContinueOnRest(10002800)
def Event_10002800():
    """Event 10002800"""
    if FlagEnabled(10000800):
        return
    
    MAIN.Await(HealthRatio(Characters.GodricktheGrafted) <= 0.0)
    
    Kill(10005810)
    Kill(10005820)
    CreateVFX(10003820)
    CreateVFX(10003821)
    CreateVFX(10003822)
    Wait(4.0)
    PlaySoundEffect(Characters.GodricktheGrafted, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.GodricktheGrafted))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(10000800))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=Characters.GodricktheGrafted, banner_type=BannerType.DemigodFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    EnableNetworkFlag(10000800)
    EnableFlag(9101)
    if PlayerInOwnWorld():
        EnableFlag(61101)
    if FlagEnabled(10002802):
        EnableFlag(10000802)
    SetWeather(weather=Weather.Default, duration=1000.0, immediate_change=False)
    DeleteVFX(10003810)
    DeleteVFX(10003811)
    EnableAssetActivation(Assets.AEG219_001_0500, obj_act_id=219001)
    AND_9.Add(PlayerStandingOnCollision(10003840))
    
    MAIN.Await(not AND_9)
    
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=False)


@RestartOnRest(10002810)
def Event_10002810():
    """Event 10002810"""
    GotoIfFlagDisabled(Label.L0, flag=10000800)
    DisableCharacter(Characters.GodricktheGrafted)
    DisableAnimations(Characters.GodricktheGrafted)
    Kill(Characters.GodricktheGrafted)
    DisableAsset(Assets.AEG210_290_8500)
    EnableAsset(Assets.AEG210_291_8500)
    DisableAsset(Assets.AEG099_330_9000)
    GotoIfFlagEnabled(Label.L10, flag=10000802)
    EnableAsset(Assets.AEG210_025_8500)
    DisableAsset(Assets.AEG210_027_8500)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableAsset(Assets.AEG210_025_8500)
    EnableAsset(Assets.AEG210_027_8500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(Assets.AEG219_001_0500, obj_act_id=219001)
    DisableAI(Characters.GodricktheGrafted)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=10000801)
    ForceAnimation(Characters.GodricktheGrafted, 30000, loop=True)
    EnableAsset(Assets.AEG210_290_8500)
    DisableAsset(Assets.AEG210_291_8500)
    EnableAsset(Assets.AEG210_025_8500)
    DisableAsset(Assets.AEG210_027_8500)
    AND_2.Add(FlagEnabled(10002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=10002800))
    
    MAIN.Await(AND_2)
    
    DeleteVFX(10003830)
    DeleteVFX(10003831)
    DeleteVFX(10003832)
    DeleteVFX(10003833)
    DeleteVFX(10003834)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=10000020,
            cutscene_flags=0,
            move_to_region=10002810,
            map_id=10000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(10000020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=19.0, y_angle=137.8300018310547)
    CreateVFX(10003830)
    CreateVFX(10003831)
    CreateVFX(10003832)
    CreateVFX(10003833)
    CreateVFX(10003834)
    DisableAsset(Assets.AEG210_290_8500)
    EnableAsset(Assets.AEG210_291_8500)
    Move(
        Characters.GodricktheGrafted,
        destination=Assets.AEG003_316_9001,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        short_move=True,
    )
    DisableAsset(Assets.AEG099_330_9000)
    ForceAnimation(Characters.GodricktheGrafted, 20000)
    EnableNetworkFlag(10000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(Assets.AEG210_290_8500)
    EnableAsset(Assets.AEG210_291_8500)
    EnableAsset(Assets.AEG210_025_8500)
    DisableAsset(Assets.AEG210_027_8500)
    DisableAsset(Assets.AEG099_330_9000)
    Move(
        Characters.GodricktheGrafted,
        destination=Assets.AEG003_316_9001,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        short_move=True,
    )
    AND_2.Add(FlagEnabled(10002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=10002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GodricktheGrafted)
    SetNetworkUpdateRate(10005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GodricktheGrafted, name=904750000)


@RestartOnRest(10002811)
def Event_10002811():
    """Event 10002811"""
    if FlagEnabled(10000800):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.GodricktheGrafted, 14785))
    OR_1.Add(FlagEnabled(10000800))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(10000800):
        return
    AND_14.Add(HealthValue(PLAYER) <= 0)
    AND_14.Add(CharacterOutsideRegion(character=PLAYER, region=10002156))
    if AND_14:
        return
    AND_15.Add(HealthValue(PLAYER) <= 0)
    AND_15.Add(CharacterInsideRegion(character=PLAYER, region=10002156))
    GotoIfConditionTrue(Label.L15, input_condition=AND_15)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=10000030,
            cutscene_flags=0,
            move_to_region=10002811,
            map_id=10000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(10000030, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(10002802)
    Move(
        Characters.GodricktheGrafted,
        destination=Assets.AEG003_316_9001,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        short_move=True,
    )
    AddSpecialEffect(Characters.GodricktheGrafted, 14750)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=20, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=28, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=29, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=30, switch_type=OnOffChange.Off)
    DisableAsset(Assets.AEG210_025_8500)
    EnableAsset(Assets.AEG210_027_8500)
    ForceAnimation(Characters.GodricktheGrafted, 20011, wait_for_completion=True)
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    if PlayerInOwnWorld():
        PlayCutscene(10000030, cutscene_flags=0, player_id=10000)
    else:
        PlayCutscene(10000030, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(10002802)
    AddSpecialEffect(Characters.GodricktheGrafted, 14750)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=20, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=28, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=29, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.GodricktheGrafted, bit_index=30, switch_type=OnOffChange.Off)
    DisableAsset(Assets.AEG210_025_8500)
    EnableAsset(Assets.AEG210_027_8500)
    ForceAnimation(Characters.GodricktheGrafted, 20011, wait_for_completion=True)
    End()


@RestartOnRest(10002820)
def Event_10002820(_, region: uint, special_effect: int, special_effect_1: int):
    """Event 10002820"""
    if FlagEnabled(10000800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterInsideRegion(character=Characters.GodricktheGrafted, region=region))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.GodricktheGrafted, special_effect)
    Wait(0.10000000149011612)
    AND_2.Add(CharacterOutsideRegion(character=Characters.GodricktheGrafted, region=region))
    
    MAIN.Await(AND_2)
    
    Wait(0.10000000149011612)
    AddSpecialEffect(Characters.GodricktheGrafted, special_effect_1)
    Restart()


@RestartOnRest(10002821)
def Event_10002821(_, region: uint, special_effect: int, special_effect_1: int):
    """Event 10002821"""
    if FlagEnabled(10000800):
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


@RestartOnRest(10002824)
def Event_10002824(_, region: uint, special_effect: int, special_effect_1: int):
    """Event 10002824"""
    if FlagEnabled(10000800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterInsideRegion(character=Characters.GodricktheGrafted, region=region))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.GodricktheGrafted, special_effect)
    Wait(0.10000000149011612)
    AND_2.Add(CharacterOutsideRegion(character=Characters.GodricktheGrafted, region=region))
    
    MAIN.Await(AND_2)
    
    Wait(0.10000000149011612)
    AddSpecialEffect(Characters.GodricktheGrafted, special_effect_1)
    Restart()


@RestartOnRest(10002825)
def Event_10002825(_, region: uint, special_effect: int, special_effect_1: int):
    """Event 10002825"""
    if FlagEnabled(10000800):
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


@RestartOnRest(10002849)
def Event_10002849():
    """Event 10002849"""
    CommonFunc_9005800(
        0,
        flag=10000800,
        entity=Assets.AEG099_002_9000,
        region=10002800,
        flag_1=10002805,
        character=10005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=10000800,
        entity=Assets.AEG099_002_9000,
        region=10002800,
        flag_1=10002805,
        flag_2=10002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=10000800, asset=Assets.AEG099_002_9000, model_point=5, right=0)
    CommonFunc_9005822(
        0,
        flag=10000800,
        bgm_boss_conv_param_id=475000,
        flag_1=10002805,
        flag_2=10002806,
        right=0,
        flag_3=10002802,
        left=1,
        left_1=1,
    )


@ContinueOnRest(10002850)
def Event_10002850():
    """Event 10002850"""
    if FlagEnabled(10000850):
        return
    
    MAIN.Await(HealthValue(Characters.Margit) <= 0)
    
    Wait(2.0)
    PlaySoundEffect(Characters.Margit, 77777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Margit))
    
    Kill(Characters.Margit)
    KillBossAndDisplayBanner(character=Characters.Margit, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(10000850)
    EnableFlag(9100)
    if PlayerInOwnWorld():
        EnableFlag(61100)


@RestartOnRest(10002860)
def Event_10002860():
    """Event 10002860"""
    GotoIfFlagDisabled(Label.L0, flag=10000850)
    DisableCharacter(Characters.Margit)
    DisableAnimations(Characters.Margit)
    Kill(Characters.Margit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Margit)
    if PlayerInOwnWorld():
        DisableThisSlotFlag()
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.Unknown7))
    if OR_15:
        return
    GotoIfThisEventSlotFlagEnabled(Label.L2)
    GotoIfFlagEnabled(Label.L1, flag=10000851)
    DisableCharacter(Characters.Margit)
    SetCharacterFadeOnEnable(character=Characters.Margit, state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=Characters.Margit, other_entity=PLAYER, radius=25.0))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Margit))
    AND_10.Add(OR_1)
    AND_10.Add(FlagDisabled(10000850))
    
    MAIN.Await(AND_10)
    
    SetCharacterFadeOnEnable(character=Characters.Margit, state=False)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=10000010,
            cutscene_flags=0,
            move_to_region=10002852,
            map_id=10000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(10000010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableCharacter(Characters.Margit)
    ForceAnimation(Characters.Margit, 20000)
    EnableNetworkFlag(10000851)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(10002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=10002850))
    
    MAIN.Await(AND_2)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Margit)
    SetNetworkUpdateRate(Characters.Margit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Margit, name=902130000)
    EnableThisNetworkSlotFlag()


@RestartOnRest(10002861)
def Event_10002861():
    """Event 10002861"""
    if FlagEnabled(10000850):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.Margit, 16205))
    
    MAIN.Await(AND_1)
    
    EnableFlag(10002852)


@RestartOnRest(10002870)
def Event_10002870():
    """Event 10002870"""
    if FlagEnabled(10000850):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(Characters.Margit) == 0)
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(Characters.Margit, True)
    AND_2.Add(FlagEnabled(10002705))
    AND_2.Add(TimeElapsed(seconds=50.0))
    
    MAIN.Await(AND_2)
    
    SetBackreadStateAlternate(Characters.Margit, False)


@RestartOnRest(10002889)
def Event_10002889():
    """Event 10002889"""
    CommonFunc_9005800(
        0,
        flag=10000850,
        entity=Assets.AEG099_002_9001,
        region=10002850,
        flag_1=10002855,
        character=Characters.Margit,
        action_button_id=10000,
        left=10000851,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=10000850,
        entity=Assets.AEG099_002_9001,
        region=10002850,
        flag_1=10002855,
        flag_2=10002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=10000850, asset=Assets.AEG099_002_9001, model_point=3, right=10000851)
    CommonFunc_9005813(
        0,
        flag=10000850,
        asset=Assets.AEG099_002_9002,
        model_point=3,
        right=10000851,
        model_point_1=806760,
    )
    CommonFunc_9005822(
        0,
        flag=10000850,
        bgm_boss_conv_param_id=213000,
        flag_1=10002855,
        flag_2=10002856,
        right=0,
        flag_3=10002852,
        left=0,
        left_1=0,
    )


@RestartOnRest(10003700)
def Event_10003700(_, character: uint, asset: uint):
    """Event 10003700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    DisableNetworkFlag(10009350)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3260):
        DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3265, 3268)))
    AND_1.Add(FlagEnabled(10009514))
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(3265, 3268)))
    AND_2.Add(FlagEnabled(10009514))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(asset)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_10.Add(FlagRangeAnyEnabled(flag_range=(3265, 3268)))
    AND_10.Add(FlagEnabled(10009514))
    
    MAIN.Await(not AND_10)
    
    Restart()


@RestartOnRest(10003701)
def Event_10003701(_, character: uint, asset: uint, flag: uint, flag_1: uint):
    """Event 10003701"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3260):
        DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3265, 3268)))
    AND_1.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(3265, 3268)))
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_5.Add(FlagEnabled(flag_1))
    AND_5.Add(FlagEnabled(9000))
    GotoIfConditionTrue(Label.L20, input_condition=AND_5)
    if FlagEnabled(10009510):
        EnableFlag(10009390)
    if FlagEnabled(10009511):
        EnableFlag(10009391)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930014)
    if FlagEnabled(10009512):
        ForceAnimation(character, 930015)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_10.Add(FlagRangeAnyEnabled(flag_range=(3265, 3268)))
    AND_10.Add(FlagEnabled(flag))
    
    MAIN.Await(not AND_10)
    
    Restart()


@RestartOnRest(10003702)
def Event_10003702(_, character: uint):
    """Event 10003702"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3260):
        DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3269)
    OR_1.Add(FlagEnabled(3269))
    
    MAIN.Await(OR_1)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930020)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(3269))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(10003703)
def Event_10003703(_, character: uint):
    """Event 10003703"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3260):
        DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3270)
    OR_1.Add(FlagEnabled(3270))
    AwaitConditionTrue(OR_1)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(3270))
    AwaitConditionTrue(OR_10)
    Restart()
    End()


@RestartOnRest(10003705)
def Event_10003705(_, entity: uint):
    """Event 10003705"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3263):
        return
    
    MAIN.Await(FlagEnabled(3261))
    
    ForceAnimation(entity, 20019)


@RestartOnRest(10003710)
def Event_10003710():
    """Event 10003710"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=10002709))
    
    EnableNetworkFlag(10002765)
    EnableNetworkFlag(3278)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=10002709))
    
    Restart()


@RestartOnRest(10003711)
def Event_10003711(_, first_flag: uint, last_flag: uint, flag: uint, region: uint):
    """Event 10003711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3261):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(FlagEnabled(10009397))
    
    if CharacterOutsideRegion(character=PLAYER, region=10002704):
        if FlagEnabled(10009360):
            return
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    Restart()


@RestartOnRest(10003715)
def Event_10003715(
    _,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    first_flag_1: uint,
    last_flag_1: uint,
    flag_1: uint,
    region: uint,
):
    """Event 10003715"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3261):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(FlagEnabled(10009397))
    
    if FlagEnabled(flag):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
        DisableNetworkConnectedFlagRange(flag_range=(first_flag_1, last_flag_1))
        EnableNetworkFlag(flag_1)
        EnableNetworkFlag(3278)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    Restart()


@RestartOnRest(10003720)
def Event_10003720(_, flag: uint, flag_1: uint):
    """Event 10003720"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkFlag(10009389)
    if FlagEnabled(flag):
        EnableNetworkFlag(flag_1)
    
    MAIN.Await(FlagEnabled(10009389))
    
    Restart()


@RestartOnRest(10003724)
def Event_10003724():
    """Event 10003724"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3260):
        return
    if FlagEnabled(10009351):
        return
    if FlagEnabled(10002722):
        return
    GotoIfFlagDisabled(Label.L0, flag=10002720)
    GotoIfFlagEnabled(Label.L1, flag=10002720)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=10002715))
    
    EnableFlag(10002769)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(10002769)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_1.Add(TimeElapsed(seconds=18.0))
    OR_2.Add(FlagEnabled(10009351))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10002716))
    AND_1.Add(TimeElapsed(seconds=8.0))
    OR_3.Add(AND_1)
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=10002716))
    OR_15.Add(OR_1)
    OR_15.Add(OR_2)
    OR_15.Add(OR_3)
    OR_15.Add(OR_4)
    
    MAIN.Await(OR_15)
    
    GotoIfFinishedConditionTrue(Label.L3, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=OR_4)

    # --- Label 3 --- #
    DefineLabel(3)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableFlag(10002721)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(10002722)
    End()


@RestartOnRest(10003726)
def Event_10003726():
    """Event 10003726"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10000755))
    AND_1.Add(FlagEnabled(3260))
    AND_1.Add(FlagDisabled(3261))
    AND_1.Add(FlagEnabled(10002731))
    AND_1.Add(FlagDisabled(10009354))
    AND_1.Add(FlagDisabled(10009355))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(10009500)


@RestartOnRest(10003728)
def Event_10003728(_, region: uint):
    """Event 10003728"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(10009502):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagEnabled(10009351))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(10009502)
    End()


@RestartOnRest(10003729)
def Event_10003729(_, region: uint):
    """Event 10003729"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    EnableNetworkFlag(10009356)
    End()


@RestartOnRest(10003730)
def Event_10003730():
    """Event 10003730"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    GotoIfFlagEnabled(Label.L20, flag=10009373)
    DisableNetworkFlag(10009370)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.GatekeeperGostoc3, radius=24.0))
    AND_3.Add(FlagEnabled(10009512))
    AND_3.Add(FlagEnabled(3260))
    AND_3.Add(FlagDisabled(3261))
    
    MAIN.Await(AND_3)
    
    EnableNetworkFlag(10009370)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(10003731)
def Event_10003731():
    """Event 10003731"""
    AND_1.Add(FlagDisabled(10009374))
    AND_1.Add(FlagDisabled(10009377))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(10009374))
    AND_2.Add(FlagDisabled(10009377))
    GotoIfConditionTrue(Label.L5, input_condition=AND_2)
    if FlagEnabled(10009377):
        return
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(10009374))
    OR_2.Add(FlagEnabled(10009377))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    EndIfFinishedConditionTrue(input_condition=OR_2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkFlag(10000562)
    DisableNetworkFlag(10008562)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=10000050,
            cutscene_flags=0,
            move_to_region=10002712,
            map_id=10000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
        Goto(Label.L2)
    OR_1.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.WhitePhantom))
    OR_1.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.Unknown7))
    SkipLinesIfConditionFalse(2, OR_1)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=10000050,
        cutscene_flags=0,
        move_to_region=10002713,
        map_id=10000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
    )
    Goto(Label.L2)
    PlayCutsceneToAll(cutscene_id=10000050, cutscene_flags=0)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(10009374)
    DisableNetworkFlag(10000562)
    DisableNetworkFlag(10008562)
    if PlayerInOwnWorld():
        DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=0)
        DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=1)
        DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=2)
        DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=3)
    EndOfAnimation(asset=Assets.AEG219_000_0501, animation_id=1)
    Wait(3.0)
    DisableNetworkFlag(10000562)
    DisableNetworkFlag(10008562)
    EndOfAnimation(asset=Assets.AEG219_000_0501, animation_id=1)
    AND_5.Add(CharacterOutsideRegion(character=PLAYER, region=10002711))
    AND_5.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_5.Add(CharacterDead(Characters.BanishedKnight1))
    OR_5.Add(AND_5)
    
    MAIN.Await(OR_5)
    
    EnableNetworkFlag(10009377)
    EnableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=0)
    EnableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=1)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=2)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=3)
    
    MAIN.Await(AssetActivated(obj_act_id=10003562))
    
    EnableFlag(10000562)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=0)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=1)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=2)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=3)
    End()


@RestartOnRest(10003732)
def Event_10003732():
    """Event 10003732"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L1, flag=10009374)
    AND_1.Add(FlagEnabled(10009374))
    AND_1.Add(FlagDisabled(10009377))
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)
    if FlagEnabled(10009377):
        return

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(FlagEnabled(10009374))
    OR_2.Add(FlagEnabled(10009377))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_1)
    EndIfFinishedConditionTrue(input_condition=OR_2)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    OR_4.Add(ActionButtonParamActivated(action_button_id=9000, entity=Assets.AEG219_000_0501))
    OR_4.Add(FlagEnabled(10009377))
    
    MAIN.Await(OR_4)
    
    if FlagEnabled(10009377):
        return
    if FlagDisabled(10009377):
        DisplayDialog(
            text=4001,
            anchor_entity=Assets.AEG219_000_0501,
            display_distance=1.0,
            number_buttons=NumberButtons.OneButton,
        )
        Restart()
    End()


@RestartOnRest(10003733)
def Event_10003733():
    """Event 10003733"""
    GotoIfFlagDisabled(Label.L0, flag=10009374)
    AND_1.Add(FlagEnabled(10009374))
    AND_1.Add(FlagDisabled(10009377))
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)
    if FlagEnabled(10009377):
        return

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(10009374))
    OR_2.Add(CharacterDead(Characters.BanishedKnight1))
    OR_3.Add(FlagEnabled(3263))
    OR_4.Add(FlagRangeAllDisabled(flag_range=(3265, 3268)))
    OR_5.Add(OR_1)
    OR_5.Add(OR_2)
    OR_5.Add(OR_3)
    OR_5.Add(OR_4)
    
    MAIN.Await(OR_5)
    
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_1)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(10009377)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_6.Add(CharacterOutsideRegion(character=PLAYER, region=10002711))
    AND_6.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_6.Add(CharacterDead(Characters.BanishedKnight1))
    OR_6.Add(AND_6)
    
    MAIN.Await(OR_6)
    
    EnableNetworkFlag(10009377)
    DisableNetworkFlag(10000562)
    EnableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=0)
    EnableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=1)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=2)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=3)
    
    MAIN.Await(AssetActivated(obj_act_id=10003562))
    
    EnableFlag(10000562)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=0)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=1)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=2)
    DisableAssetActivation(Assets.AEG219_000_0501, obj_act_id=1219000, relative_index=3)
    End()


@RestartOnRest(10003734)
def Event_10003734():
    """Event 10003734"""
    AND_1.Add(FlagDisabled(3263))
    AND_1.Add(FlagEnabled(10009397))
    AND_1.Add(FlagDisabled(10009374))
    AND_1.Add(CharacterDead(10000651, target_comparison_type=ComparisonType.NotEqual))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10002710))
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(FlagDisabled(10009377))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(10009374)
    End()


@RestartOnRest(10003735)
def Event_10003735():
    """Event 10003735"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(10009374))
    AND_1.Add(FlagDisabled(10009377))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(10009374))
    AND_2.Add(FlagDisabled(10009377))
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(10009374))
    OR_1.Add(FlagEnabled(10009377))
    
    MAIN.Await(OR_1)
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 4283))
    
    AddSpecialEffect(PLAYER, 4282)
    OR_2.Add(FlagDisabled(10009374))
    OR_2.Add(FlagEnabled(10009377))
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(PLAYER, 4283)
    Restart()


@RestartOnRest(10003736)
def Event_10003736():
    """Event 10003736"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(InsideMap(game_map=STORMVEIL_CASTLE))
    
    MultiplyBloodstainSouls(multiplier=0.0, bloodstain_save_slot_id=-1)
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(10009510, 10009513)))
    AND_1.Add(FlagEnabled(10009360))
    AND_1.Add(FlagEnabled(10009362))
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(3263))
    OR_2.Add(FlagRangeAllDisabled(flag_range=(3265, 3268)))
    OR_3.Add(OutsideMap(game_map=STORMVEIL_CASTLE))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(OR_3)
    
    MAIN.Await(OR_4)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_2)
    MultiplyBloodstainSouls(multiplier=0.0, bloodstain_save_slot_id=-1)
    End()
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_3)
    MultiplyBloodstainSouls(multiplier=0.0, bloodstain_save_slot_id=-1)
    Restart()
    MultiplyBloodstainSouls(multiplier=0.30000001192092896, bloodstain_save_slot_id=0)
    OR_5.Add(FlagRangeAllDisabled(flag_range=(10009510, 10009513)))
    AND_5.Add(FlagEnabled(10009360))
    AND_5.Add(FlagEnabled(10009362))
    OR_6.Add(AND_5)
    OR_6.Add(FlagEnabled(3263))
    OR_6.Add(FlagRangeAllDisabled(flag_range=(3265, 3268)))
    OR_7.Add(OutsideMap(game_map=STORMVEIL_CASTLE))
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    OR_8.Add(OR_7)
    
    MAIN.Await(OR_8)
    
    MultiplyBloodstainSouls(multiplier=0.0, bloodstain_save_slot_id=-1)
    EndIfFinishedConditionTrue(input_condition=OR_6)
    Restart()


@RestartOnRest(10003737)
def Event_10003737():
    """Event 10003737"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3263):
        return
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(2600, 2629)))
    
    IncreaseCharacterSoulReward(
        character=Characters.GatekeeperGostoc0,
        fixed_increase_amount=0,
        soul_amount_load_slot_id=0,
    )
    IncreaseCharacterSoulReward(
        character=Characters.GatekeeperGostoc1,
        fixed_increase_amount=0,
        soul_amount_load_slot_id=0,
    )
    IncreaseCharacterSoulReward(
        character=Characters.GatekeeperGostoc2,
        fixed_increase_amount=0,
        soul_amount_load_slot_id=0,
    )
    IncreaseCharacterSoulReward(
        character=Characters.GatekeeperGostoc3,
        fixed_increase_amount=0,
        soul_amount_load_slot_id=0,
    )
    IncreaseCharacterSoulReward(
        character=Characters.GatekeeperGostoc4,
        fixed_increase_amount=0,
        soul_amount_load_slot_id=0,
    )
    End()


@RestartOnRest(10003738)
def Event_10003738():
    """Event 10003738"""
    DisableAsset(Assets.AEG099_003_9000)
    OR_1.Add(FlagEnabled(10009377))
    OR_1.Add(FlagEnabled(10003738))
    if OR_1:
        return
    SkipLinesIfHost(2)
    EnableAsset(Assets.AEG099_003_9000)
    CreateAssetVFX(Assets.AEG099_003_9000, vfx_id=101, model_point=3)
    AND_5.Add(CharacterOutsideRegion(character=PLAYER, region=10002711))
    AND_5.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_6.Add(FlagEnabled(10009377))
    AND_6.Add(AND_5)
    
    MAIN.Await(AND_6)
    
    DisableAsset(Assets.AEG099_003_9000)
    DeleteAssetVFX(Assets.AEG099_003_9000)
    End()


@RestartOnRest(10000739)
def Event_10000739():
    """Event 10000739"""
    EnableInvincibility(Characters.BanishedKnight1)
    OR_1.Add(FlagEnabled(10009374))
    OR_1.Add(FlagEnabled(10009377))
    OR_1.Add(FlagEnabled(10000379))
    
    MAIN.Await(OR_1)
    
    DisableInvincibility(Characters.BanishedKnight1)
    End()


@RestartOnRest(10003740)
def Event_10003740(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003740"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003741)
def Event_10003741(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003741"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003742)
def Event_10003742(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003742"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003743)
def Event_10003743(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003743"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003744)
def Event_10003744(_, character: uint, character_1: uint, flag: uint, flag_1: uint, distance: float):
    """Event 10003744"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=character, distance=17.0)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=17.0)
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetCharacterTalkRange(character=character, distance=distance)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(10003745)
def Event_10003745(_, character: uint):
    """Event 10003745"""
    DisableCharacter(character)
    DisableBackread(character)
    if FlagDisabled(10000800):
        return
    EnableCharacter(character)
    EnableBackread(character)
    DisableAnimations(character)
    ForceAnimation(character, 930000)
    End()


@RestartOnRest(10000760)
def Event_10000760(_, character: uint):
    """Event 10000760"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(3905))
    AND_1.Add(FlagDisabled(10002164))
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    AND_2.Add(FlagEnabled(3905))
    AND_2.Add(FlagDisabled(10002164))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3900)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_3.Add(FlagEnabled(3905))
    AND_3.Add(FlagDisabled(10002164))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(10000761)
def Event_10000761():
    """Event 10000761"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(9101):
        return
    
    MAIN.Await(FlagEnabled(9101))
    
    EnableFlag(3918)


@RestartOnRest(10000762)
def Event_10000762():
    """Event 10000762"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11109528):
        return
    
    MAIN.Await(FlagEnabled(10000291))
    
    EnableFlag(11109528)


@ContinueOnRest(10000763)
def Event_10000763(_, asset: uint, radius: float):
    """Event 10000763"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=10009610)
    OR_1.Add(FlagEnabled(10009617))
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(3907, 3917)))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    AND_1.Add(FlagDisabled(10002164))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(10009610)
    EnableFlag(3918)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=100, model_point=42)


@RestartOnRest(10000764)
def Event_10000764(_, character: uint, entity: uint):
    """Event 10000764"""
    DisableNetworkSync()
    DisableCharacter(character)
    DisableBackread(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5005)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=10009610)
    
    MAIN.Await(FlagEnabled(10009610))
    
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=6511, entity=entity))
    
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetAnimation(character, disable_interpolation=True)
    Wait(0.6000000238418579)
    ForceAnimation(character, 90203)
    Wait(8.0)
    ResetCharacterPosition(character=character)
    DisableCharacter(character)
    DisableBackread(character)
    Restart()


@RestartOnRest(10003770)
def Event_10003770(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 10003770"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372701)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(10003771)
def Event_10003771(_, other_entity: uint, flag: uint):
    """Event 10003771"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4680):
        return
    
    MAIN.Await(FlagEnabled(4680))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(10003772)
def Event_10003772(_, other_entity: uint, flag: uint):
    """Event 10003772"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    
    MAIN.Await(FlagEnabled(1042379203))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(10003773)
def Event_10003773(_, other_entity: uint, flag: uint):
    """Event 10003773"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379207):
        return
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372702)
    
    MAIN.Await(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    
    DisableFlag(1042372702)
    Restart()


@RestartOnRest(10003775)
def Event_10003775(_, character: uint, character_1: uint):
    """Event 10003775"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4220):
        DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(4225))
    OR_1.Add(FlagDisabled(10002160))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    AND_2.Add(FlagEnabled(4225))
    OR_2.Add(FlagDisabled(10002160))
    AND_2.Add(OR_2)
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 30015)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    EnableCharacter(Characters.BanishedKnight7)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableCharacter(Characters.BanishedKnight7)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(Characters.BanishedKnight7)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagDisabled(4225))
    OR_15.Add(FlagEnabled(10002160))
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(10003776)
def Event_10003776(_, character: uint):
    """Event 10003776"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4220):
        DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4229)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4229))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(4229))
    
    Restart()
    End()


@RestartOnRest(10003777)
def Event_10003777():
    """Event 10003777"""
    if FlagEnabled(9101):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(10002160))
    AND_1.Add(FlagEnabled(9101))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(10009707)
    End()


@RestartOnRest(10003778)
def Event_10003778():
    """Event 10003778"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=Characters.NepheliLoux0, distance=17.0)
    if FlagEnabled(10009705):
        return
    SetCharacterTalkRange(character=Characters.NepheliLoux0, distance=40.0)
    AND_1.Add(FlagEnabled(4225))
    AND_1.Add(FlagDisabled(10009705))
    AND_1.Add(FlagDisabled(10002785))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10002735))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(10002784)
    End()


@RestartOnRest(10003779)
def Event_10003779():
    """Event 10003779"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(4221, 4223)))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(10009709)
    End()


@RestartOnRest(10003780)
def Event_10003780():
    """Event 10003780"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(9101):
        AwaitFlagEnabled(flag=9101)
        EnableNetworkFlag(10002786)
    OR_1.Add(FlagEnabled(4229))
    OR_1.Add(FlagDisabled(9101))
    OR_1.Add(FlagDisabled(9104))
    OR_1.Add(FlagDisabled(11109921))
    OR_1.Add(FlagEnabled(10009722))
    OR_1.Add(FlagEnabled(10002786))
    if OR_1:
        return
    if FlagDisabled(10009720):
        EnableNetworkFlag(10009720)
        Goto(Label.L20)
    if FlagDisabled(10009721):
        EnableNetworkFlag(10009721)
        Goto(Label.L20)
    if FlagDisabled(10009722):
        EnableNetworkFlag(10009722)
        Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableNetworkFlag(10002786)
    End()


@RestartOnRest(10003790)
def Event_10003790(_, character: uint):
    """Event 10003790"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3580):
        DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3587)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(3587))
    AwaitConditionTrue(AND_1)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3580)
    GotoIfFlagEnabled(Label.L2, flag=3581)
    GotoIfFlagEnabled(Label.L4, flag=3583)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    AND_15.Add(FlagDisabled(3587))
    AwaitConditionTrue(AND_15)
    Restart()
    End()


@RestartOnRest(10002910)
def Event_10002910():
    """Event 10002910"""
    if FlagEnabled(10000800):
        return
    OR_1.Add(FlagEnabled(10002160))
    
    MAIN.Await(OR_1)
    
    DisableMapCollision(collision=10004910)

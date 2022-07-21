"""
Academy of Raya Lucaria

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
from .entities.m14_00_00_00_entities import *
from .entities.m31_06_00_00_entities import Assets as m31_06_Assets
from .entities.m60_35_46_00_entities import Assets as m60_35_Assets


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=14000002, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=14000003, asset=Assets.AEG099_060_9003)
    CommonFunc_9005810(
        0,
        flag=14000800,
        grace_flag=14000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_9005810(
        0,
        flag=14000850,
        grace_flag=14000001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    Event_14002080()
    Event_14002665()
    DisableMapCollisionBackreadMask(collision=0)
    Event_14002800()
    Event_14002810()
    Event_14002811()
    Event_14002849()
    Event_140028121()
    Event_140028122(0, character=Characters.RennalaPhaseTwo, special_effect=14585, special_effect_1=14575)
    Event_14002606()
    Event_14002689()
    Event_14003500(0, region=14002700, flag=14000800)
    Event_14002850()
    Event_14002860()
    Event_14002889()
    Event_14003801(
        0,
        flag=14003800,
        character=Characters.RennalaPhaseOne0,
        character_1=14005810,
        character_2=Characters.RennalaStudent0,
        character_3=Characters.RennalaStudent1,
        character_4=Characters.RennalaStudent2,
        character_5=Characters.RennalaStudent3,
        character_6=Characters.RennalaStudent4,
        character_7=Characters.RennalaStudent5,
        character_8=Characters.RennalaStudent6,
        character_9=Characters.RennalaStudent7,
        character_10=Characters.RennalaStudent8,
        character_11=Characters.RennalaStudent9,
        character_12=Characters.RennalaStudent10,
        character_13=Characters.RennalaStudent11,
        character_14=Characters.RennalaStudent12,
        character_15=Characters.RennalaStudent13,
        character_16=Characters.RennalaStudent14,
        character_17=Characters.RennalaStudent15,
        character_18=Characters.RennalaStudent16,
        character_19=Characters.RennalaStudent17,
        character_20=Characters.RennalaStudent18,
        character_21=Characters.RennalaStudent19,
        character_22=140008230,
        character_23=Characters.RennalaStudent21,
        character_24=Characters.RennalaStudent22,
        character_25=Characters.RennalaStudent23,
    )
    Event_14003825(0, flag=14003800, character=Characters.RennalaPhaseOne0, character_1=14005810)
    Event_14003805(0, flag=14003806, character=Characters.RennalaPhaseOne0, character_1=14005810, character_2=14005811)
    Event_14003807(0, character=Characters.RennalaPhaseOne0, character_1=14005810)
    Event_14003808(0, flag=14003800, character=Characters.RennalaPhaseOne0)
    Event_14003817(0, character__character_group=14005810)
    Event_14003809(0, flag=14003810, character=Characters.RennalaPhaseOne0)
    Event_14003811(
        0,
        flag=14003810,
        character=14005810,
        character_1=Characters.RennalaStudent0,
        character_2=Characters.RennalaStudent1,
        character_3=Characters.RennalaStudent2,
        character_4=Characters.RennalaStudent3,
        character_5=Characters.RennalaStudent4,
        character_6=Characters.RennalaStudent5,
        character_7=Characters.RennalaStudent6,
        character_8=Characters.RennalaStudent7,
        character_9=Characters.RennalaStudent8,
        character_10=Characters.RennalaStudent9,
        character_11=Characters.RennalaStudent10,
        character_12=Characters.RennalaStudent11,
        character_13=Characters.RennalaStudent12,
        character_14=Characters.RennalaStudent13,
        character_15=Characters.RennalaStudent14,
        character_16=Characters.RennalaStudent15,
        character_17=Characters.RennalaStudent16,
        character_18=Characters.RennalaStudent17,
        character_19=Characters.RennalaStudent18,
        character_20=Characters.RennalaStudent19,
        character_21=140008230,
        character_22=Characters.RennalaStudent21,
        character_23=Characters.RennalaStudent22,
        character_24=Characters.RennalaStudent23,
    )
    Event_14003814(0, destination=Characters.RennalaPhaseOne0, character=Characters.Dummy0)
    Event_14003815(0, character=Characters.RennalaPhaseOne0, anchor_entity=Characters.Dummy0)
    Event_14003892(0, character=Characters.RennalaPhaseOne0, character_1=14005810)
    Event_14003893(0, character=Characters.RennalaPhaseOne0, character_1=14005810)
    Event_14003894(0, character=Characters.RennalaPhaseOne0, character_1=14005810)
    Event_14003820(0, asset=Assets.AEG250_260_9000)
    Event_14003820(1, asset=Assets.AEG250_260_5004)
    Event_14003820(2, asset=Assets.AEG250_260_5003)
    Event_14003820(3, asset=Assets.AEG250_260_9003)
    Event_14003820(5, asset=Assets.AEG250_260_9004)
    Event_14003820(6, asset=14001826)
    Event_14003820(8, asset=Assets.AEG250_260_9006)
    Event_14003820(9, asset=14001829)
    Event_14003950(0, flag=14003820, asset=Assets.AEG250_260_9000)
    Event_14003950(1, flag=14003821, asset=Assets.AEG250_260_5004)
    Event_14003950(2, flag=14003822, asset=Assets.AEG250_260_5003)
    Event_14003950(3, flag=14003823, asset=Assets.AEG250_260_9003)
    Event_14003950(4, flag=14003825, asset=Assets.AEG250_260_9004)
    Event_14003950(5, flag=14003826, asset=14001826)
    Event_14003950(6, flag=14003828, asset=Assets.AEG250_260_9006)
    Event_14003950(7, flag=14003829, asset=14001829)
    Event_14003834(0, asset=14006810)
    Event_14003834(1, asset=14006811)
    Event_14003834(2, asset=14006812)
    Event_14003834(3, asset=14006813)
    Event_14003834(4, asset=14006814)
    Event_14003840(
        0,
        character=Characters.RennalaStudent18,
        left=Assets.AEG250_260_5004,
        left_1=0,
        left_2=0,
        flag=14003821,
        flag_1=0,
        flag_2=0,
    )
    Event_14003840(
        1,
        character=Characters.RennalaStudent19,
        left=Assets.AEG250_260_5003,
        left_1=0,
        left_2=0,
        flag=14003822,
        flag_1=0,
        flag_2=0,
    )
    Event_14003840(
        2,
        character=Characters.RennalaStudent20,
        left=Assets.AEG250_260_9000,
        left_1=0,
        left_2=0,
        flag=14003820,
        flag_1=0,
        flag_2=0,
    )
    Event_14003840(
        3,
        character=Characters.RennalaStudent21,
        left=Assets.AEG250_260_9003,
        left_1=0,
        left_2=0,
        flag=14003823,
        flag_1=0,
        flag_2=0,
    )
    Event_14003845(
        0,
        character=Characters.RennalaStudent18,
        asset=Assets.AEG250_260_5004,
        asset_1=0,
        asset_2=0,
        asset_3=14003821,
        asset_4=0,
        asset_5=0,
    )
    Event_14003845(
        1,
        character=Characters.RennalaStudent19,
        asset=Assets.AEG250_260_5003,
        asset_1=0,
        asset_2=0,
        asset_3=14003822,
        asset_4=0,
        asset_5=0,
    )
    Event_14003845(
        2,
        character=Characters.RennalaStudent20,
        asset=Assets.AEG250_260_9000,
        asset_1=0,
        asset_2=0,
        asset_3=14003820,
        asset_4=0,
        asset_5=0,
    )
    Event_14003845(
        3,
        character=Characters.RennalaStudent21,
        asset=Assets.AEG250_260_9003,
        asset_1=0,
        asset_2=0,
        asset_3=14003823,
        asset_4=0,
        asset_5=0,
    )
    Event_14003850(
        0,
        character=Characters.RennalaStudent22,
        asset=14006810,
        asset_1=14006811,
        asset_2=14006812,
        asset_3=14006813,
        asset_4=14006814,
        flag=14003834,
        flag_1=14003835,
        flag_2=14003836,
        flag_3=14003837,
        flag_4=14003838,
        asset__asset_flag=Assets.AEG257_031_5004,
        asset__asset_flag_1=Assets.AEG257_031_5003,
        asset__asset_flag_2=Assets.AEG257_031_5002,
        asset__asset_flag_3=Assets.AEG257_031_5001,
        asset__asset_flag_4=Assets.AEG257_031_5000,
        region=14002815,
        region_1=14002816,
        region_2=14002817,
        region_3=14002818,
        region_4=14002819,
    )
    Event_14003850(
        1,
        character=Characters.RennalaStudent23,
        asset=14006810,
        asset_1=14006811,
        asset_2=14006812,
        asset_3=14006813,
        asset_4=14006814,
        flag=14003834,
        flag_1=14003835,
        flag_2=14003836,
        flag_3=14003837,
        flag_4=14003838,
        asset__asset_flag=Assets.AEG257_031_5004,
        asset__asset_flag_1=Assets.AEG257_031_5003,
        asset__asset_flag_2=Assets.AEG257_031_5002,
        asset__asset_flag_3=Assets.AEG257_031_5001,
        asset__asset_flag_4=Assets.AEG257_031_5000,
        region=14002815,
        region_1=14002816,
        region_2=14002817,
        region_3=14002818,
        region_4=14002819,
    )
    Event_14003922(0, flag=14003920, character=Characters.RennalaPhaseTwo, character_1=Characters.BloodhoundKnight)
    Event_14003923(
        0,
        flag=14003920,
        flag_1=14003921,
        character=Characters.BloodhoundKnight,
        character_1=Characters.RennalaPhaseTwo,
    )
    Event_14003924(0, flag=14003920, flag_1=14003921, character=Characters.BloodhoundKnight)
    Event_14003925(0, flag=14003920, character=Characters.BloodhoundKnight)
    Event_14003926(0, character=Characters.BloodhoundKnight)
    Event_14003962(0, flag=14003960, character=Characters.RennalaPhaseTwo, character_1=Characters.Troll)
    Event_14003963(
        0,
        flag=14003960,
        flag_1=14003961,
        character=Characters.Troll,
        character_1=Characters.RennalaPhaseTwo,
    )
    Event_14003964(0, flag=14003960, flag_1=14003961, character=Characters.Troll)
    Event_14003965(0, flag=14003960, character=Characters.Troll)
    Event_14003966(0, character=Characters.Troll)
    Event_14003937(
        0,
        flag=14003935,
        character=Characters.RennalaPhaseTwo,
        character_1=Characters.Wolf0,
        character_2=Characters.Wolf1,
        character_3=Characters.Wolf2,
        character_4=Characters.Wolf3,
    )
    Event_14003938(
        0,
        flag=14003935,
        flag_1=14003936,
        character=Characters.Wolf0,
        character_1=Characters.Wolf1,
        character_2=Characters.Wolf2,
        character_3=Characters.Wolf3,
        character_4=Characters.RennalaPhaseTwo,
    )
    Event_14003939(
        0,
        flag=14003935,
        flag_1=14003936,
        character=Characters.Wolf0,
        character_1=Characters.Wolf1,
        character_2=Characters.Wolf2,
        character_3=Characters.Wolf3,
    )
    Event_14003940(0, flag=14003935, character=Characters.Wolf0)
    Event_14003940(1, flag=14003935, character=Characters.Wolf1)
    Event_14003940(2, flag=14003935, character=Characters.Wolf2)
    Event_14003940(3, flag=14003935, character=Characters.Wolf3)
    Event_14003945(0, character=Characters.Wolf0)
    Event_14003945(1, character=Characters.Wolf1)
    Event_14003945(2, character=Characters.Wolf2)
    Event_14003945(3, character=Characters.Wolf3)
    Event_14003972(0, flag=14003970, character=Characters.RennalaPhaseTwo, character_1=Characters.FlyingDragon)
    Event_14003973(
        0,
        flag=14003970,
        flag_1=14003971,
        character=Characters.FlyingDragon,
        character_1=Characters.RennalaPhaseTwo,
    )
    Event_14003974(0, flag=14003970, flag_1=14003971, character=Characters.FlyingDragon)
    Event_14003975(0, flag=14003970, character=Characters.FlyingDragon)
    Event_14003976(0, character=Characters.FlyingDragon)
    Event_14003977(0, character=Characters.RennalaPhaseTwo, character_1=14005820)
    Event_14003978()
    Event_14003915()
    CommonFunc_90005511(
        0,
        flag=14000560,
        asset=Assets.AEG257_013_0501,
        obj_act_id=14003560,
        obj_act_id_1=257013,
        left=0,
    )
    CommonFunc_90005512(0, flag=14000560, region=14002550, region_1=14002551)
    CommonFunc_90005511(
        0,
        flag=14000562,
        asset=Assets.AEG257_013_0500,
        obj_act_id=14003562,
        obj_act_id_1=257013,
        left=0,
    )
    CommonFunc_90005512(0, flag=14000562, region=14002552, region_1=14002553)
    CommonFunc_90005515(0, flag=14008550, anchor_entity=Assets.AEG257_018_0500)
    CommonFunc_90005515(0, flag=14008552, anchor_entity=Assets.AEG257_018_0501)
    CommonFunc_90005501(
        0,
        flag=14000510,
        flag_1=14000511,
        left=0,
        asset=Assets.AEG257_009_0500,
        asset_1=Assets.AEG257_002_0500,
        asset_2=m60_35_Assets.AEG257_002_2001,
        flag_2=14000512,
    )
    Event_14002510()
    CommonFunc_90005501(
        0,
        flag=14000515,
        flag_1=14000516,
        left=0,
        asset=Assets.AEG257_010_0500,
        asset_1=Assets.AEG257_002_0502,
        asset_2=Assets.AEG257_002_0503,
        flag_2=14000517,
    )
    CommonFunc_90005501(
        0,
        flag=14000520,
        flag_1=14000521,
        left=0,
        asset=Assets.AEG257_011_0500,
        asset_1=Assets.AEG257_002_0504,
        asset_2=m31_06_Assets.AEG257_002_1000,
        flag_2=14000522,
    )
    Event_14002580()
    CommonFunc_90005520(
        0,
        flag=14000546,
        asset=Assets.AEG257_008_0500,
        start_climbing_flag=14000544,
        stop_climbing_flag=14000545,
    )
    Event_14002498()
    Event_14002590()
    Event_14002592()
    Event_14002594()
    CommonFunc_90005300(
        0,
        flag=14000276,
        character=Characters.RayaLucariaScholar23,
        item_lot_param_id=0,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=14000277,
        character=Characters.RayaLucariaScholar24,
        item_lot_param_id=0,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005525(0, flag=14000610, asset=Assets.AEG257_035_3000)
    CommonFunc_90005525(0, flag=14000611, asset=Assets.AEG257_035_3001)
    CommonFunc_90005525(0, flag=14000612, asset=Assets.AEG257_039_1000)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=37,
        cc_id=46,
        dd_id=0,
        player_start=1037462650,
        unk_8_12=14000000,
        flag=14002660,
        left_flag=14002661,
        cancel_flag__right_flag=14002662,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_14002328(0, character=Characters.PutridCorpse29)
    Event_14002328(1, character=Characters.PutridCorpse30)
    Event_14002328(2, character=Characters.PutridCorpse31)
    Event_14002328(3, character=Characters.PutridCorpse32)
    Event_14002328(4, character=Characters.PutridCorpse33)
    Event_14002328(5, character=Characters.PutridCorpse34)
    Event_14002328(6, character=Characters.PutridCorpse35)
    Event_14002328(7, character=Characters.PutridCorpse36)
    Event_14002328(8, character=Characters.PutridCorpse37)
    Event_14002328(9, character=Characters.PutridCorpse38)
    Event_14002328(10, character=Characters.PutridCorpse39)
    Event_14002328(11, character=Characters.PutridCorpse40)
    Event_14002328(12, character=Characters.PutridCorpse26)
    Event_14002328(13, character=Characters.PutridCorpse27)
    Event_14002328(14, character=Characters.PutridCorpse28)
    Event_14002328(15, character=Characters.PutridCorpseBare6)
    CommonFunc_90005300(
        0,
        flag=14000633,
        character=Characters.SmallCrabCrystal0,
        item_lot_param_id=14000005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(0, flag=14000634, character=14000634, item_lot_param_id=14000015, seconds=0.0, left=0)
    CommonFunc_90005300(
        0,
        flag=14000637,
        character=Characters.SmallCrabCrystal1,
        item_lot_param_id=14000025,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=14000638,
        character=Characters.SmallCrabCrystal2,
        item_lot_param_id=14000035,
        seconds=0.0,
        left=0,
    )
    Event_14002491(0, character=Characters.Avionette2, region=14002492, radius=15.0, seconds=0.0, animation_id=3032)
    Event_14002491(1, character=Characters.Avionette3, region=14002493, radius=15.0, seconds=0.0, animation_id=3032)
    Event_14002491(2, character=Characters.Avionette4, region=14002493, radius=15.0, seconds=0.0, animation_id=3032)
    Event_14002490(0, character=Characters.Avionette0, region=14002490, seconds=0.0, animation_id=3032)
    Event_14002490(1, character=Characters.Avionette1, region=14002491, seconds=0.0, animation_id=3032)
    Event_14002490(2, character=Characters.Avionette6, region=14002496, seconds=0.0, animation_id=3032)
    Event_14002490(3, character=Characters.Avionette7, region=14002496, seconds=1.0, animation_id=3032)
    CommonFunc_90005300(0, flag=14000486, character=Characters.Scarab, item_lot_param_id=40272, seconds=0.0, left=0)
    CommonFunc_90005300(
        0,
        flag=14000499,
        character=Characters.MoongrumCarianKnight,
        item_lot_param_id=14000980,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005780(
        0,
        flag=14000850,
        summon_flag=14002160,
        dismissal_flag=14002161,
        character=Characters.SorceressSellen3,
        sign_type=20,
        region=14002731,
        right=1034509259,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=14000850, flag_1=14002160, flag_2=14002161, character=Characters.SorceressSellen3)
    CommonFunc_90005782(
        0,
        flag=14002160,
        region=14002855,
        character=Characters.SorceressSellen3,
        target_entity=14002850,
        region_1=14002859,
        animation=0,
    )
    CommonFunc_90005795(
        0,
        flag=7608,
        flag_1=0,
        flag_2=1051369239,
        left_flag=14002141,
        cancel_flag__right_flag=14002142,
        message=80609,
        action_button_id=9000,
        asset=Assets.AEG099_090_9001,
        model_point=30010,
    )
    SkipLinesIfCeremonyInactive(line_count=2, ceremony=20)
    CommonFunc_90005796(0, flag=7608, character=Characters.SorceressSellen2, banner_type=5, region=14002141)
    Event_14002145()
    CommonFunc_90005795(
        0,
        flag=7609,
        flag_1=0,
        flag_2=1034509269,
        left_flag=14002143,
        cancel_flag__right_flag=14002144,
        message=80608,
        action_button_id=9000,
        asset=Assets.AEG099_090_9002,
        model_point=30000,
    )
    SkipLinesIfCeremonyInactive(line_count=2, ceremony=30)
    Event_14002155()
    Event_14002165(0, flag=7609, character=Characters.WitchHunterJerren1, banner_type=7, region=14002151)
    Event_14002495()
    Event_14000700()
    Event_14000701()
    Event_14000702()
    Event_14000703()
    Event_14000710(0, asset__character=14000710, asset__character_1=14000711)
    Event_14000711()
    CommonFunc_90005702(0, character=Characters.SorceressSellen2, flag=3463, first_flag=3460, last_flag=3463)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9003,
        action_button_id=4110,
        item_lot_param_id=101070,
        first_flag=400107,
        last_flag=400107,
        flag=3469,
        model_point=0,
    )
    Event_14000712()
    Event_14000713()
    Event_14000714()
    Event_14000720()
    Event_14000730(0, character=Characters.WitchHunterJerren2)
    CommonFunc_90005703(
        0,
        character=Characters.WitchHunterJerren2,
        flag=3361,
        flag_1=3362,
        flag_2=14009351,
        flag_3=3361,
        first_flag=3360,
        last_flag=3363,
        right=-1,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.WitchHunterJerren2,
        flag=3361,
        flag_1=3360,
        flag_2=14009351,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.WitchHunterJerren2, flag=3363, first_flag=3360, last_flag=3363)
    CommonFunc_90005702(0, character=Characters.WitchHunterJerren1, flag=3363, first_flag=3360, last_flag=3363)
    Event_14000731()
    Event_14000740(0, character=Characters.BoctheSeamster)
    Event_14000741(0, character=Characters.DemiHumanShaman)
    Event_14000742()
    Event_14000750(0, character=Characters.SorcererThops, asset=14006700)
    CommonFunc_90005750(0, 14001720, 4110, 103600, 400360, 400362, 3806, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.RennalaPhaseOne1)
    DisableBackread(Characters.RennalaPhaseOne2)
    DisableBackread(Characters.SorceressSellen0)
    DisableBackread(Characters.GravenSchool)
    DisableBackread(Characters.SorceressSellen1)
    DisableBackread(Characters.SorceressSellen2)
    DisableBackread(Characters.WitchHunterJerren0)
    DisableBackread(Characters.WitchHunterJerren1)
    DisableBackread(Characters.WitchHunterJerren2)
    DisableBackread(Characters.BoctheSeamster)
    DisableBackread(Characters.DemiHumanShaman)
    DisableBackread(Characters.SorcererThops)
    DisableAsset(14006710)
    Event_14000519()
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar0, region=14002200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar1, region=14002200, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.RayaLucariaScholar2,
        animation_id=30000,
        animation_id_1=20000,
        region=14002451,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.RayaLucariaScholar6,
        animation_id=30000,
        animation_id_1=20000,
        region=14002228,
        radius=15.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar7, region=14002228, seconds=0.0, animation_id=-1)
    CommonFunc_90005210(
        0,
        character=Characters.RayaLucariaScholar8,
        animation_id=30000,
        animation_id_1=20000,
        region=14002228,
        radius=15.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar9, region=14002228, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar3, region=14002222, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar11, region=14002222, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar13, region=14002251, seconds=0.5, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar14, region=14002251, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar15, region=14002252, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=14000260, region=14002260, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=14000261, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar17, region=14002260, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=14000263, region=14002260, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar16, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar18, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar20, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar19, region=14002266, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar21,
        region=14002268,
        radius=3.0,
        seconds=1.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar22,
        region=14002268,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar23, region=14002276, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar24, region=14002276, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar25, region=14002285, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar26, region=14002285, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar27, region=14002285, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse0, region=14002300, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse1,
        animation_id=30005,
        animation_id_1=20005,
        region=14002305,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.PutridCorpse2, region=14002310, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse3,
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
        character=Characters.PutridCorpse4,
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
        character=Characters.PutridCorpse5,
        animation_id=30005,
        animation_id_1=20005,
        region=14002315,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse6,
        animation_id=30000,
        animation_id_1=20000,
        region=14002315,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse7,
        animation_id=30006,
        animation_id_1=20006,
        region=14002315,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse8,
        animation_id=30000,
        animation_id_1=20000,
        region=14002315,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse9,
        animation_id=30000,
        animation_id_1=20000,
        region=14002315,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse10,
        animation_id=30000,
        animation_id_1=20000,
        region=14002315,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse11,
        animation_id=30000,
        animation_id_1=20000,
        region=14002315,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.PutridCorpse12, region=14002323, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse13,
        animation_id=30000,
        animation_id_1=20000,
        region=14002325,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse14,
        animation_id=30000,
        animation_id_1=20000,
        region=14002325,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse18,
        region=14002335,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse15,
        animation_id=30000,
        animation_id_1=20000,
        region=14002325,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse16,
        animation_id=30000,
        animation_id_1=20000,
        region=14002325,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse17,
        animation_id=30000,
        animation_id_1=20000,
        region=14002325,
        seconds=1.7999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse19,
        animation_id=30006,
        animation_id_1=20006,
        region=14002340,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=14000341,
        animation_id=30000,
        animation_id_1=20000,
        region=14002340,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=14000342,
        animation_id=30000,
        animation_id_1=20000,
        region=14002340,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse20,
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
        character=Characters.PutridCorpse21,
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
        character=Characters.PutridCorpse22,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=14000355,
        animation_id=30000,
        animation_id_1=20000,
        region=14002355,
        radius=5.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=14000356,
        animation_id=30000,
        animation_id_1=20000,
        region=14002355,
        radius=5.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse23,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse24,
        animation_id=30006,
        animation_id_1=20006,
        region=14002361,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse25,
        animation_id=30006,
        animation_id_1=20006,
        region=14002361,
        seconds=1.399999976158142,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.PutridCorpseBare0, radius=16.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare2, region=14002345, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=14000392,
        animation_id=30000,
        animation_id_1=20000,
        region=14002355,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpseBare4,
        animation_id=30006,
        animation_id_1=20006,
        region=14002361,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpseBare5,
        animation_id=30001,
        animation_id_1=20001,
        region=14002396,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpseBare7,
        animation_id=30001,
        animation_id_1=20001,
        region=14002396,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpseBare8,
        animation_id=30001,
        animation_id_1=20001,
        region=14002396,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.SmallerDog0, region=14002345, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.SmallerDog1,
        animation_id=30001,
        animation_id_1=20001,
        region=14002345,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallerDog3,
        animation_id=30001,
        animation_id_1=20001,
        region=14002345,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallerDog4,
        animation_id=30001,
        animation_id_1=20001,
        region=14002345,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble0,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble1,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble2,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble3,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble4,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble8,
        animation_id=30001,
        animation_id_1=20001,
        region=14002267,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble9,
        animation_id=30001,
        animation_id_1=20001,
        region=14002267,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble10,
        animation_id=30001,
        animation_id_1=20001,
        region=14002267,
        seconds=1.7999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble11,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005250(0, character=Characters.WanderingNoble13, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble12,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot,
        animation_id=30000,
        animation_id_1=20000,
        region=14002228,
        seconds=10.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot5,
        animation_id=30000,
        animation_id_1=20000,
        region=14002410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot6,
        animation_id=30000,
        animation_id_1=20000,
        region=14002410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot7,
        animation_id=30000,
        animation_id_1=20000,
        region=14002410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot8,
        animation_id=30000,
        animation_id_1=20000,
        region=14002410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot9,
        animation_id=30000,
        animation_id_1=20000,
        region=14002410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot10,
        animation_id=30000,
        animation_id_1=20000,
        region=14002410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot0,
        animation_id=30000,
        animation_id_1=20000,
        region=14002252,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot1,
        animation_id=30000,
        animation_id_1=20000,
        region=14002252,
        seconds=6.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot2,
        animation_id=30000,
        animation_id_1=20000,
        region=14002252,
        seconds=7.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        region=14002252,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot4,
        animation_id=30000,
        animation_id_1=20000,
        region=14002252,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LargeCrabSnow0,
        animation_id=30001,
        animation_id_1=20001,
        region=14002635,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LargeCrabSnow1,
        animation_id=30001,
        animation_id_1=20001,
        region=14002636,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Marionette0,
        animation_id=30010,
        animation_id_1=20010,
        region=14002450,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Marionette1,
        animation_id=30010,
        animation_id_1=20010,
        region=14002451,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Marionette3,
        animation_id=30010,
        animation_id_1=20010,
        region=14002451,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Marionette2,
        animation_id=30010,
        animation_id_1=20010,
        region=14002452,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Marionette4, region=14002461, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Marionette9, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Marionette10, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Marionette7,
        animation_id=30010,
        animation_id_1=20010,
        region=14002472,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Marionette8,
        animation_id=30010,
        animation_id_1=20010,
        region=14002472,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Marionette11, region=14002487, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Marionette12, region=14002487, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Avionette5,
        animation_id=30000,
        animation_id_1=20001,
        region=14002495,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Avionette8, region=14002396, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Avionette9, region=14002396, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Page, region=14002675, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.MadPumpkinHead, region=14002276, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.IronVirgin0, region=14002293, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.IronVirgin1, region=14002294, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, 14000499, 14002499, 0.0, -1)


@NeverRestart(14002080)
def Event_14002080():
    """Event 14002080"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002080))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 14307))
    
    MAIN.Await(AND_1)
    
    SetRespawnPoint(respawn_point=16002080)
    SaveRequest()
    EnableFlag(16000540)


@RestartOnRest(14002145)
def Event_14002145():
    """Event 14002145"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=20)
    EnableBackread(Characters.SorceressSellen2)
    EnableBackread(Characters.WitchHunterJerren0)
    SetTeamType(Characters.SorceressSellen2, TeamType.Human)
    SetTeamType(Characters.WitchHunterJerren0, TeamType.Enemy)
    DeleteAssetVFX(14006710)
    CreateAssetVFX(14006710, vfx_id=200, model_point=806700)


@RestartOnRest(14002155)
def Event_14002155():
    """Event 14002155"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=30)
    EnableBackread(Characters.WitchHunterJerren1)
    EnableBackread(Characters.SorceressSellen1)
    SetTeamType(Characters.WitchHunterJerren1, TeamType.Enemy)
    SetTeamType(Characters.SorceressSellen1, TeamType.Human)
    DeleteAssetVFX(14006700)
    CreateAssetVFX(14006700, vfx_id=200, model_point=806700)


@RestartOnRest(14002165)
def Event_14002165(_, flag: uint, character: uint, banner_type: uchar, region: uint):
    """Event 14002165"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterProportionDead(character=character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayBanner(banner_type)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    AddSpecialEffect(20000, 4822)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(14002580)
def Event_14002580():
    """Event 14002580"""
    RegisterLadder(start_climbing_flag=14000530, stop_climbing_flag=14000531, asset=Assets.AEG257_037_0500)
    RegisterLadder(start_climbing_flag=14000532, stop_climbing_flag=14000533, asset=Assets.AEG257_004_0500)
    RegisterLadder(start_climbing_flag=14000534, stop_climbing_flag=14000535, asset=Assets.AEG257_005_0500)
    RegisterLadder(start_climbing_flag=14000536, stop_climbing_flag=14000537, asset=Assets.AEG257_006_0500)
    RegisterLadder(start_climbing_flag=14000538, stop_climbing_flag=14000539, asset=Assets.AEG257_003_0500)
    RegisterLadder(start_climbing_flag=14000540, stop_climbing_flag=14000541, asset=Assets.AEG257_007_0500)
    RegisterLadder(start_climbing_flag=14000542, stop_climbing_flag=14000543, asset=Assets.AEG257_015_0500)


@NeverRestart(14002510)
def Event_14002510():
    """Event 14002510"""
    CommonFunc_90005500(
        0,
        flag=14000510,
        flag_1=14001511,
        left=0,
        asset=Assets.AEG257_009_0500,
        asset_1=Assets.AEG257_002_0500,
        obj_act_id=14003511,
        asset_2=m60_35_Assets.AEG257_002_2001,
        obj_act_id_1=1035463512,
        region=14002511,
        region_1=14002512,
        flag_2=14000512,
        flag_3=14000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=14000515,
        flag_1=14000516,
        left=0,
        asset=Assets.AEG257_010_0500,
        asset_1=Assets.AEG257_002_0502,
        obj_act_id=14003516,
        asset_2=Assets.AEG257_002_0503,
        obj_act_id_1=14003517,
        region=14002516,
        region_1=14002517,
        flag_2=14000517,
        flag_3=14000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        14000520,
        14000521,
        0,
        14001520,
        14001521,
        14003521,
        14001522,
        14003522,
        14002521,
        14002522,
        14000522,
        14000523,
        0,
    )


@NeverRestart(14000519)
def Event_14000519():
    """Event 14000519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableThisSlotFlag()


@RestartOnRest(14002498)
def Event_14002498():
    """Event 14002498"""
    GotoIfFlagEnabled(Label.L0, flag=14000546)
    EnableNavmeshType(navmesh_id=14002498, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(FlagEnabled(14000546))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNavmeshType(navmesh_id=14002498, navmesh_type=NavmeshType.Solid)
    End()


@RestartOnRest(14003500)
def Event_14003500(_, region: uint, flag: uint):
    """Event 14003500"""
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 9621)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_3)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(PLAYER, 9621)
    Restart()


@RestartOnRest(14002590)
def Event_14002590():
    """Event 14002590"""
    EnableNetworkSync()
    GotoIfFlagRangeAllDisabled(Label.L0, flag_range=(14000276, 14000277))
    DisableAsset(Assets.AEG257_014_0500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG257_014_0500)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(FlagEnabled(14002595))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EndIfFlagRangeAllEnabled(flag_range=(14000276, 14000277))
    EnableAsset(Assets.AEG257_014_0500)
    ForceAnimation(Assets.AEG257_014_0500, 1)
    CreateTemporaryVFX(
        vfx_id=814630,
        anchor_entity=Assets.AEG003_316_9001,
        model_point=100,
        anchor_type=CoordEntityType.Asset,
    )
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500000,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500010,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500020,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500030,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500040,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500050,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500060,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500070,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    Wait(10.0)
    DisableAsset(Assets.AEG257_014_0500)
    Restart()


@RestartOnRest(14002592)
def Event_14002592():
    """Event 14002592"""
    DeleteAssetVFX(Assets.AEG003_316_9002)
    CreateAssetVFX(Assets.AEG003_316_9002, vfx_id=100, model_point=814631)


@RestartOnRest(14002594)
def Event_14002594():
    """Event 14002594"""
    EndIfFlagRangeAllEnabled(flag_range=(14000276, 14000277))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002590))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002595)
    Wait(10.0)
    DisableNetworkFlag(14002595)
    Restart()


@RestartOnRest(14002650)
def Event_14002650(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 14002650"""
    if Multiplayer():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(14002328)
def Event_14002328(_, character: uint):
    """Event 14002328"""
    Kill(character)


@RestartOnRest(14002360)
def Event_14002360(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    attacked_entity: uint,
    attacked_entity_1: uint,
    attacked_entity_2: uint,
):
    """Event 14002360"""
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
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=0))
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=0))
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=0))
    AND_1.Add(OR_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
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


@RestartOnRest(14002490)
def Event_14002490(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 14002490"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    DisableGravity(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)
    EnableGravity(character)
    Wait(2.799999952316284)

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(14002491)
def Event_14002491(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 14002491"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    DisableGravity(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)
    EnableGravity(character)
    Wait(2.799999952316284)

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(14002495)
def Event_14002495():
    """Event 14002495"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(14002140))
    OR_1.Add(FlagEnabled(14002150))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(Characters.TalkDummy7, 9531)
    AND_1.Add(FlagDisabled(14002140))
    AND_1.Add(FlagDisabled(14002150))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.TalkDummy7, 9532)
    Wait(1.0)
    Restart()


@NeverRestart(14002606)
def Event_14002606():
    """Event 14002606"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=14000676)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=14003606))
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    DisplayDialog(text=208199, anchor_entity=Assets.AEG099_630_9006)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(Assets.AEG099_630_9006, obj_act_id=199630)
    End()


@RestartOnRest(14002665)
def Event_14002665():
    """Event 14002665"""
    DisableAsset(14006600)


@RestartOnRest(14002689)
def Event_14002689():
    """Event 14002689"""
    GotoIfFlagEnabled(Label.L0, flag=14000801)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=14002689))
    
    ActivateGparamOverride(gparam_sub_id=500, change_duration=0.0)
    Wait(0.10000000149011612)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeactivateGparamOverride(change_duration=0.0)
    End()


@RestartOnRest(14002800)
def Event_14002800():
    """Event 14002800"""
    GotoIfFlagDisabled(Label.L1, flag=14000804)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    MoveRemains(source_region=14002840, destination_region=14002843)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L0, flag=14000800)
    
    MAIN.Await(HealthValue(Characters.RennalaPhaseTwo) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(14008000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.RennalaPhaseTwo))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(14000800))
    
    MAIN.Await(OR_2)
    
    Kill(14005810)
    KillBossAndDisplayBanner(character=Characters.RennalaPhaseTwo, banner_type=BannerType.LegendFelled)
    EnableNetworkFlag(14000800)
    EnableFlag(9118)
    if PlayerInOwnWorld():
        EnableFlag(61118)
    SetRespawnPoint(respawn_point=14003900)
    SaveRequest()
    Wait(8.0)
    if PlayerNotInOwnWorld():
        return

    # --- Label 0 --- #
    DefineLabel(0)
    WarpToMap(game_map=RAYA_LUCARIA, player_start=14003900)
    SetRespawnPoint(respawn_point=14003900)
    SaveRequest()
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    EnableAssetActivation(Assets.AEG099_630_9006, obj_act_id=199630)
    MoveRemains(source_region=14002840, destination_region=14002843)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    EnableFlag(14000804)
    SetBackreadStateAlternate(35000, False)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)


@RestartOnRest(14002810)
def Event_14002810():
    """Event 14002810"""
    GotoIfFlagDisabled(Label.L0, flag=14000800)
    DisableCharacter(14005800)
    DisableAnimations(14005800)
    Kill(14005800)
    EnableCharacter(Characters.RennalaPhaseOne1)
    EnableAnimations(Characters.RennalaPhaseOne1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(14005800)
    DisableCharacter(Characters.RennalaPhaseOne1)
    DisableAnimations(Characters.RennalaPhaseOne1)
    DisableCharacter(Characters.RennalaPhaseTwo)
    DisableAnimations(Characters.RennalaPhaseTwo)
    DisableAssetActivation(Assets.AEG099_630_9006, obj_act_id=199630)
    MoveRemains(source_region=14002840, destination_region=14002841)
    GotoIfFlagEnabled(Label.L1, flag=14000801)
    DisableCharacter(14005800)
    DisableAnimations(14005800)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=10)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=1)
    DeleteVFX(14002600, erase_root_only=False)
    DeleteVFX(14002601, erase_root_only=False)
    DeleteVFX(14002602, erase_root_only=False)
    DeleteVFX(14002603, erase_root_only=False)
    DeleteVFX(14002604, erase_root_only=False)
    DeleteVFX(14002605, erase_root_only=False)
    DeleteVFX(14002606, erase_root_only=False)
    DeleteVFX(14002607, erase_root_only=False)
    DeleteVFX(14002608, erase_root_only=False)
    DeleteVFX(14002609, erase_root_only=False)
    DeleteVFX(14002610, erase_root_only=False)
    DeleteVFX(14002611, erase_root_only=False)
    DeleteVFX(14002612, erase_root_only=False)
    DeleteVFX(14002613, erase_root_only=False)
    DeleteVFX(14002614, erase_root_only=False)
    DeleteVFX(14002615, erase_root_only=False)
    DeleteVFX(14002616, erase_root_only=False)
    DeleteVFX(14002617, erase_root_only=False)
    DeleteVFX(14002618, erase_root_only=False)
    DeleteVFX(14002619, erase_root_only=False)
    DeleteVFX(14002620, erase_root_only=False)
    DeleteVFX(14002621, erase_root_only=False)
    DeleteVFX(14002622, erase_root_only=False)
    DeleteVFX(14002623, erase_root_only=False)
    DeleteVFX(14002624, erase_root_only=False)
    DeleteVFX(14002625, erase_root_only=False)
    DeleteVFX(14002626, erase_root_only=False)
    DeleteVFX(14002627, erase_root_only=False)
    DeleteVFX(14002628, erase_root_only=False)
    DeleteVFX(14002629, erase_root_only=False)
    DeleteVFX(14002630, erase_root_only=False)
    DeleteVFX(14002631, erase_root_only=False)
    DeleteVFX(14002680, erase_root_only=False)
    DeleteVFX(14002681, erase_root_only=False)
    DeleteVFX(14002682, erase_root_only=False)
    DeleteVFX(14002683, erase_root_only=False)
    DeleteVFX(14002684, erase_root_only=False)
    DeleteVFX(14002685, erase_root_only=False)
    DeleteVFX(14002686, erase_root_only=False)
    DeleteVFX(14002687, erase_root_only=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent0, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent1, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent2, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent3, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent4, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent5, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent6, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent7, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent8, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent9, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent10, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent11, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent12, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent13, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent14, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent15, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent16, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent17, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent18, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent19, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent20, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent21, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent22, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent23, state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.RennalaPhaseOne0, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableFlag(9021)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=14000000,
            cutscene_flags=0,
            move_to_region=14002802,
            map_id=14000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(14000000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(14000801)
    EnableCharacter(Characters.RennalaPhaseOne0)
    EnableAnimations(Characters.RennalaPhaseOne0)
    EnableCharacter(14005810)
    EnableAnimations(14005810)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=0)
    ForceAnimation(Assets.AEG257_031_5000, 0, loop=True)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    AND_2.Add(FlagEnabled(14002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=14002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(14005800)
    SetNetworkUpdateRate(Characters.RennalaPhaseOne0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(14005810, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    EnableBossHealthBar(Characters.RennalaPhaseOne0, name=902030000)


@RestartOnRest(14002811)
def Event_14002811():
    """Event 14002811"""
    if FlagEnabled(14000800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterDead(Characters.RennalaPhaseOne0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002802)
    SetCharacterFadeOnEnable(character=Characters.RennalaPhaseTwo, state=False)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=10)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=1)
    DeleteVFX(14002600, erase_root_only=False)
    DeleteVFX(14002601, erase_root_only=False)
    DeleteVFX(14002602, erase_root_only=False)
    DeleteVFX(14002603, erase_root_only=False)
    DeleteVFX(14002604, erase_root_only=False)
    DeleteVFX(14002605, erase_root_only=False)
    DeleteVFX(14002606, erase_root_only=False)
    DeleteVFX(14002607, erase_root_only=False)
    DeleteVFX(14002608, erase_root_only=False)
    DeleteVFX(14002609, erase_root_only=False)
    DeleteVFX(14002610, erase_root_only=False)
    DeleteVFX(14002611, erase_root_only=False)
    DeleteVFX(14002612, erase_root_only=False)
    DeleteVFX(14002613, erase_root_only=False)
    DeleteVFX(14002614, erase_root_only=False)
    DeleteVFX(14002615, erase_root_only=False)
    DeleteVFX(14002616, erase_root_only=False)
    DeleteVFX(14002617, erase_root_only=False)
    DeleteVFX(14002618, erase_root_only=False)
    DeleteVFX(14002619, erase_root_only=False)
    DeleteVFX(14002620, erase_root_only=False)
    DeleteVFX(14002621, erase_root_only=False)
    DeleteVFX(14002622, erase_root_only=False)
    DeleteVFX(14002623, erase_root_only=False)
    DeleteVFX(14002624, erase_root_only=False)
    DeleteVFX(14002625, erase_root_only=False)
    DeleteVFX(14002626, erase_root_only=False)
    DeleteVFX(14002627, erase_root_only=False)
    DeleteVFX(14002628, erase_root_only=False)
    DeleteVFX(14002629, erase_root_only=False)
    DeleteVFX(14002630, erase_root_only=False)
    DeleteVFX(14002631, erase_root_only=False)
    DeleteVFX(14002680, erase_root_only=False)
    DeleteVFX(14002681, erase_root_only=False)
    DeleteVFX(14002682, erase_root_only=False)
    DeleteVFX(14002683, erase_root_only=False)
    DeleteVFX(14002684, erase_root_only=False)
    DeleteVFX(14002685, erase_root_only=False)
    DeleteVFX(14002686, erase_root_only=False)
    DeleteVFX(14002687, erase_root_only=False)
    SetPlayerPositionDisplay(
        state=False,
        aboveground=True,
        game_map=RAYA_LUCARIA,
        x=42.02000045776367,
        y=154.1999969482422,
        z=-23.889999389648438,
    )
    SetBackreadStateAlternate(Characters.RennalaPhaseTwo, True)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=14000010,
            cutscene_flags=0,
            move_to_region=14002803,
            map_id=14000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=14000010,
            cutscene_flags=0,
            move_to_region=14002806,
            map_id=14000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=4.960000038146973, y_angle=-117.80000305175781)
    EnableFlag(14002803)
    SetBackreadStateAlternate(35000, True)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    Move(
        35000,
        destination=14002806,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.RennalaPhaseTwo,
    )
    Move(
        Characters.TalkDummy7,
        destination=14002806,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.RennalaPhaseTwo,
    )
    SetCharacterTalkRange(character=Characters.TalkDummy7, distance=200.0)
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    EnableCharacter(Characters.RennalaPhaseTwo)
    EnableAnimations(Characters.RennalaPhaseTwo)
    ForceAnimation(Characters.RennalaPhaseTwo, 20005)
    EnableBossHealthBar(Characters.RennalaPhaseTwo, name=902030001)
    SetNetworkUpdateRate(Characters.RennalaPhaseTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFramesAfterCutscene(frames=1)
    AttachAssetToCharacter(character=Characters.TalkDummy7, model_point=10, asset=Assets.AEG099_052_9001)


@RestartOnRest(140028121)
def Event_140028121():
    """Event 140028121"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(14000800):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.RennalaPhaseOne0, 14350))
    
    MAIN.Await(OR_1)
    
    EnableFlag(14002707)
    AND_1.Add(FlagDisabled(14002707))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.RennalaPhaseOne0, 14350))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(140028122)
def Event_140028122(_, character: uint, special_effect: int, special_effect_1: int):
    """Event 140028122"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(character):
        return
    OR_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_1.Add(CharacterHasSpecialEffect(character, special_effect_1))
    
    MAIN.Await(OR_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(14002720)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(14002722)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_1.Add(FlagRangeAllDisabled(flag_range=(14002720, 14002723)))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, special_effect))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, special_effect_1))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(14002849)
def Event_14002849():
    """Event 14002849"""
    CommonFunc_9005800(
        0,
        flag=14000800,
        entity=Assets.AEG099_001_9000,
        region=14002800,
        flag_1=14002805,
        character=14005800,
        action_button_id=10000,
        left=14000801,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=14000800,
        entity=Assets.AEG099_001_9000,
        region=14002800,
        flag_1=14002805,
        flag_2=14002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=14000800, asset=Assets.AEG099_001_9000, model_point=3, right=14000801)
    CommonFunc_9005822(0, 14000800, 203000, 14002805, 14002806, 0, 14002803, 1, 0)


@RestartOnRest(14002850)
def Event_14002850():
    """Event 14002850"""
    if FlagEnabled(14000850):
        return
    
    MAIN.Await(HealthRatio(Characters.RedWolf) <= 0.0)
    
    Wait(2.0)
    PlaySoundEffect(Characters.RedWolf, 77777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.RedWolf))
    
    KillBossAndDisplayBanner(character=Characters.RedWolf, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(14000850)
    EnableFlag(9117)
    if PlayerInOwnWorld():
        EnableFlag(61117)


@RestartOnRest(14002860)
def Event_14002860():
    """Event 14002860"""
    GotoIfFlagDisabled(Label.L0, flag=14000850)
    DisableCharacter(Characters.RedWolf)
    DisableAnimations(Characters.RedWolf)
    Kill(Characters.RedWolf)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.RedWolf)
    GotoIfFlagEnabled(Label.L1, flag=14000851)
    ForceAnimation(Characters.RedWolf, 30002, loop=True)
    AND_2.Add(FlagEnabled(14002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=14002850))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(14000851)
    ForceAnimation(Characters.RedWolf, 20002)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(Characters.RedWolf, destination=14002856, destination_type=CoordEntityType.Region, short_move=True)
    AND_2.Add(FlagEnabled(14002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=14002850))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.RedWolf)
    SetNetworkUpdateRate(14005850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.RedWolf, name=903181000)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(14005850, authority_level=UpdateAuthority.Forced)


@RestartOnRest(14002889)
def Event_14002889():
    """Event 14002889"""
    CommonFunc_9005800(
        0,
        flag=14000850,
        entity=Assets.AEG099_003_9000,
        region=14002850,
        flag_1=14002855,
        character=14005850,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=14000850,
        entity=Assets.AEG099_003_9000,
        region=14002850,
        flag_1=14002855,
        flag_2=14002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=14000850, asset=Assets.AEG099_003_9000, model_point=3, right=0)
    CommonFunc_9005813(
        0,
        flag=14000850,
        asset=Assets.AEG099_003_9001,
        model_point=3,
        right=14000851,
        model_point_1=806760,
    )
    CommonFunc_9005822(0, 14000850, 921400, 14002855, 14002856, 0, 14000852, 0, 0)


@RestartOnRest(14002820)
def Event_14002820(_, character: uint):
    """Event 14002820"""
    DisableAI(character)
    AND_1.Add(CharacterInsideRegion(character=20000, region=14002812))
    AND_1.Add(HasAIStatus(Characters.RennalaStudent0, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    DisableAsset(Assets.AEG099_001_9000)
    DisableAsset(14006800)
    SetNetworkUpdateRate(Characters.RennalaPhaseOne0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(character)
    
    MAIN.Await(FlagEnabled(14002810))
    
    WaitFrames(frames=1)
    DisableBossHealthBar(Characters.RennalaPhaseOne0)
    EnableBossHealthBar(character)


@RestartOnRest(14002821)
def Event_14002821(_, character: uint):
    """Event 14002821"""
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=character, radius=30.0))
    OR_1.Add(HealthRatio(character, target_comparison_type=ComparisonType.NotEqual) == 1.0)
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(Characters.RennalaPhaseOne0, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableAI(character)
    EnableBossHealthBar(character)


@RestartOnRest(14002822)
def Event_14002822(_, character: uint):
    """Event 14002822"""
    MAIN.Await(CharacterDead(character))
    
    Wait(1.5)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DemigodFelled)
    EnableFlag(14000899)


@RestartOnRest(14003801)
def Event_14003801(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
    character_10: uint,
    character_11: uint,
    character_12: uint,
    character_13: uint,
    character_14: uint,
    character_15: uint,
    character_16: uint,
    character_17: uint,
    character_18: uint,
    character_19: uint,
    character_20: uint,
    character_21: uint,
    character_22: uint,
    character_23: uint,
    character_24: uint,
    character_25: uint,
):
    """Event 14003801"""
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(FlagEnabled(14002805))
    AwaitConditionTrue(AND_10)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasSpecialEffect(character_1, 14394, target_comparison_type=ComparisonType.LessThan))
    OR_1.Add(CharacterHasSpecialEffect(character, 14357))
    OR_1.Add(CharacterHasSpecialEffect(character, 14361))
    OR_1.Add(CharacterHasSpecialEffect(character, 14368))
    OR_1.Add(CharacterHasSpecialEffect(character, 14369))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlag(14003802)
    DisableFlag(14003803)
    DisableFlag(14003804)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(14003802, 14003804))
    if FlagDisabled(14003804):
        GotoIfFlagEnabled(Label.L0, flag=14003802)
        GotoIfFlagEnabled(Label.L1, flag=14003803)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_2, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_2, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_2, special_effect=14393)
    AddSpecialEffect(character_2, 14394)
    ReplanAI(character_2)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_3, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_3, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_3, special_effect=14393)
    AddSpecialEffect(character_3, 14394)
    ReplanAI(character_3)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_4, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_4, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_4, special_effect=14393)
    AddSpecialEffect(character_4, 14394)
    ReplanAI(character_4)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_5, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_5, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_5, special_effect=14393)
    AddSpecialEffect(character_5, 14394)
    ReplanAI(character_5)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_6, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_6, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_6, special_effect=14393)
    AddSpecialEffect(character_6, 14394)
    ReplanAI(character_6)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_7, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_7, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_7, special_effect=14393)
    AddSpecialEffect(character_7, 14394)
    ReplanAI(character_7)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_8, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_8, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_8, special_effect=14393)
    AddSpecialEffect(character_8, 14394)
    ReplanAI(character_8)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_9, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_9, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_9, special_effect=14393)
    AddSpecialEffect(character_9, 14394)
    ReplanAI(character_9)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_10, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_10, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_10, special_effect=14393)
    AddSpecialEffect(character_10, 14394)
    ReplanAI(character_10)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_11, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_11, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_11, special_effect=14393)
    AddSpecialEffect(character_11, 14394)
    ReplanAI(character_11)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_12, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_12, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_12, special_effect=14393)
    AddSpecialEffect(character_12, 14394)
    ReplanAI(character_12)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_13, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_13, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_13, special_effect=14393)
    AddSpecialEffect(character_13, 14394)
    ReplanAI(character_13)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_14, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_14, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_14, special_effect=14393)
    AddSpecialEffect(character_14, 14394)
    ReplanAI(character_14)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_15, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_15, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_15, special_effect=14393)
    AddSpecialEffect(character_15, 14394)
    ReplanAI(character_15)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_16, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_16, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_16, special_effect=14393)
    AddSpecialEffect(character_16, 14394)
    ReplanAI(character_16)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_17, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_17, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_17, special_effect=14393)
    AddSpecialEffect(character_17, 14394)
    ReplanAI(character_17)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_18, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_18, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_18, special_effect=14393)
    AddSpecialEffect(character_18, 14394)
    ReplanAI(character_18)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_19, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_19, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_19, special_effect=14393)
    AddSpecialEffect(character_19, 14394)
    ReplanAI(character_19)
    Restart()
    Goto(Label.L10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_20, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_20, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_20, special_effect=14393)
    AddSpecialEffect(character_20, 14394)
    ReplanAI(character_20)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_21, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_21, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_21, special_effect=14393)
    AddSpecialEffect(character_21, 14394)
    ReplanAI(character_21)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_22, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_22, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_22, special_effect=14393)
    AddSpecialEffect(character_22, 14394)
    ReplanAI(character_22)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_23, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_23, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_23, special_effect=14393)
    AddSpecialEffect(character_23, 14394)
    ReplanAI(character_23)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_24, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_24, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_24, special_effect=14393)
    AddSpecialEffect(character_24, 14394)
    ReplanAI(character_24)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_25, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_25, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_25, special_effect=14393)
    AddSpecialEffect(character_25, 14394)
    ReplanAI(character_25)
    Restart()


@RestartOnRest(14003805)
def Event_14003805(_, flag: uint, character: uint, character_1: uint, character_2: uint):
    """Event 14003805"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 14356))
    AND_1.Add(CharacterHasSpecialEffect(character_1, 14396, target_count=0.0))
    AND_1.Add(CharacterHasSpecialEffect(character_1, 14394, target_count=0.0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=14369)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=14368)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=14361):
        return RESTART
    AddSpecialEffect(character, 14368)
    OR_15.Add(CharacterHasSpecialEffect(character_1, 14394, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_15)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 14369)
    OR_15.Add(CharacterHasSpecialEffect(character_1, 14394, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_15)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 14357)
    AddSpecialEffect(character_1, 14384)
    AddSpecialEffect(character, 14578)
    ReplanAI(character)
    EnableFlag(14003816)
    DisableFlag(14003800)
    AddSpecialEffect(character_1, 14388)
    AddSpecialEffect(character_2, 14388)
    Restart()


@RestartOnRest(14003807)
def Event_14003807(_, character: uint, character_1: uint):
    """Event 14003807"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 14357))
    AND_1.Add(CharacterHasSpecialEffect(character, 14358))
    AND_1.Add(CharacterHasSpecialEffect(character_1, 14396, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 14356)
    AddSpecialEffect(character_1, 14589)
    DisableFlag(14003816)
    Restart()


@RestartOnRest(14003808)
def Event_14003808(_, flag: uint, character: uint):
    """Event 14003808"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 14358))
    AND_1.Add(CharacterHasSpecialEffect(character, 14357))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(10.0)
    EnableFlag(flag)
    OR_15.Add(CharacterHasSpecialEffect(character, 14356))
    AwaitConditionFalse(OR_15)
    Restart()


@RestartOnRest(14003809)
def Event_14003809(_, flag: uint, character: uint):
    """Event 14003809"""
    AND_1.Add(CharacterHasSpecialEffect(character, 14350))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(3.0)
    DisableFlag(flag)
    Restart()


@RestartOnRest(14003811)
def Event_14003811(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
    character_10: uint,
    character_11: uint,
    character_12: uint,
    character_13: uint,
    character_14: uint,
    character_15: uint,
    character_16: uint,
    character_17: uint,
    character_18: uint,
    character_19: uint,
    character_20: uint,
    character_21: uint,
    character_22: uint,
    character_23: uint,
    character_24: uint,
):
    """Event 14003811"""
    OR_1.Add(CharacterHasSpecialEffect(
        character,
        14351,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=5.0,
    ))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableFlag(flag)
    Restart()
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasSpecialEffect(character, 14351, target_comparison_type=ComparisonType.LessThan, target_count=5.0))
    
    MAIN.Await(AND_1)
    
    DisableFlag(14003802)
    DisableFlag(14003803)
    DisableFlag(14003804)
    EnableRandomFlagInRange(flag_range=(14003802, 14003804))
    if FlagDisabled(14003804):
        GotoIfFlagEnabled(Label.L0, flag=14003802)
        GotoIfFlagEnabled(Label.L1, flag=14003803)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_1, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_1, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_1, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_1, special_effect=14393)
    AddSpecialEffect(character_1, 14351)
    ReplanAI(character_1)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_2, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_2, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_2, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_2, special_effect=14393)
    AddSpecialEffect(character_2, 14351)
    ReplanAI(character_2)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_3, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_3, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_3, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_3, special_effect=14393)
    AddSpecialEffect(character_3, 14351)
    ReplanAI(character_3)
    SetNetworkUpdateRate(character_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_4, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_4, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_4, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_4, special_effect=14393)
    AddSpecialEffect(character_4, 14351)
    ReplanAI(character_4)
    SetNetworkUpdateRate(character_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_5, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_5, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_5, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_5, special_effect=14393)
    AddSpecialEffect(character_5, 14351)
    ReplanAI(character_5)
    SetNetworkUpdateRate(character_5, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_6, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_6, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_6, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_6, special_effect=14393)
    AddSpecialEffect(character_6, 14351)
    ReplanAI(character_6)
    SetNetworkUpdateRate(character_6, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_7, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_7, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_7, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_7, special_effect=14393)
    AddSpecialEffect(character_7, 14351)
    ReplanAI(character_7)
    SetNetworkUpdateRate(character_7, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_8, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_8, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_8, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_8, special_effect=14393)
    AddSpecialEffect(character_8, 14351)
    ReplanAI(character_8)
    SetNetworkUpdateRate(character_8, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_9, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_9, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_9, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_9, special_effect=14393)
    AddSpecialEffect(character_9, 14351)
    ReplanAI(character_9)
    SetNetworkUpdateRate(character_9, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_10, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_10, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_10, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_10, special_effect=14393)
    AddSpecialEffect(character_10, 14351)
    ReplanAI(character_10)
    SetNetworkUpdateRate(character_10, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_11, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_11, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_11, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_11, special_effect=14393)
    AddSpecialEffect(character_11, 14351)
    ReplanAI(character_11)
    SetNetworkUpdateRate(character_11, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_12, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_12, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_12, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_12, special_effect=14393)
    AddSpecialEffect(character_12, 14351)
    ReplanAI(character_12)
    SetNetworkUpdateRate(character_12, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_13, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_13, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_13, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_13, special_effect=14393)
    AddSpecialEffect(character_13, 14351)
    ReplanAI(character_13)
    SetNetworkUpdateRate(character_13, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_14, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_14, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_14, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_14, special_effect=14393)
    AddSpecialEffect(character_14, 14351)
    ReplanAI(character_14)
    SetNetworkUpdateRate(character_14, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_15, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_15, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_15, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_15, special_effect=14393)
    AddSpecialEffect(character_15, 14351)
    ReplanAI(character_15)
    SetNetworkUpdateRate(character_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_16, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_16, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_16, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_16, special_effect=14393)
    AddSpecialEffect(character_16, 14351)
    ReplanAI(character_16)
    SetNetworkUpdateRate(character_16, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_17, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_17, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_17, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_17, special_effect=14393)
    AddSpecialEffect(character_17, 14351)
    ReplanAI(character_17)
    SetNetworkUpdateRate(character_17, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_18, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_18, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_18, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_18, special_effect=14393)
    AddSpecialEffect(character_18, 14351)
    ReplanAI(character_18)
    SetNetworkUpdateRate(character_18, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    Goto(Label.L10)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_19, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_19, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_19, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_19, special_effect=14393)
    AddSpecialEffect(character_19, 14351)
    ReplanAI(character_19)
    SetNetworkUpdateRate(character_19, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_20, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_20, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_20, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_20, special_effect=14393)
    AddSpecialEffect(character_20, 14351)
    ReplanAI(character_20)
    SetNetworkUpdateRate(character_20, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_21, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_21, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_21, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_21, special_effect=14393)
    AddSpecialEffect(character_21, 14351)
    ReplanAI(character_21)
    SetNetworkUpdateRate(character_21, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_22, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_22, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_22, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_22, special_effect=14393)
    AddSpecialEffect(character_22, 14351)
    ReplanAI(character_22)
    SetNetworkUpdateRate(character_22, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_23, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_23, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_23, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_23, special_effect=14393)
    AddSpecialEffect(character_23, 14351)
    ReplanAI(character_23)
    SetNetworkUpdateRate(character_23, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=6, character=character_24, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_24, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_24, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_24, special_effect=14393)
    AddSpecialEffect(character_24, 14351)
    ReplanAI(character_24)
    SetNetworkUpdateRate(character_24, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(14003814)
def Event_14003814(_, destination: uint, character: uint):
    """Event 14003814"""
    if ThisEventSlotFlagDisabled():
        DisableGravity(character)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Character,
        model_point=20,
        short_move=True,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(14003815)
def Event_14003815(_, character: uint, anchor_entity: uint):
    """Event 14003815"""
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    TriggerAISound(ai_sound_param_id=203000, anchor_entity=anchor_entity, unk_8_12=2)
    Wait(5.0)
    Restart()


@RestartOnRest(14003817)
def Event_14003817(_, character__character_group: uint):
    """Event 14003817"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(14003816))
    AND_1.Add(CharacterProportionHasSpecialEffect(
        character_group=character__character_group,
        special_effect=14385,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    ))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character__character_group, 14384)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(14003820)
def Event_14003820(_, asset: uint):
    """Event 14003820"""
    if ThisEventSlotFlagDisabled():
        SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
        Restart()
    
    MAIN.Await(ThisEventSlotFlagDisabled())
    
    Wait(20.0)
    EnableAsset(asset)
    if AssetDestroyed(asset):
        RestoreAsset(asset)
    ForceAnimation(asset, 1, wait_for_completion=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()


@RestartOnRest(14003825)
def Event_14003825(_, flag: uint, character: uint, character_1: uint):
    """Event 14003825"""
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(CharacterBackreadEnabled(character))
    AND_10.Add(CharacterBackreadEnabled(Characters.RennalaStudent0))
    AND_10.Add(CharacterBackreadEnabled(Characters.RennalaStudent8))
    AND_10.Add(CharacterBackreadEnabled(Characters.RennalaStudent16))
    AND_10.Add(FlagEnabled(14002805))
    AwaitConditionTrue(AND_10)
    DisableFlag(14003802)
    DisableFlag(14003803)
    DisableFlag(14003804)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(14003802, 14003804))
    if FlagEnabled(14003802):
        AddSpecialEffect(Characters.RennalaStudent0, 14394)
    if FlagEnabled(14003803):
        AddSpecialEffect(Characters.RennalaStudent8, 14394)
    if FlagEnabled(14003804):
        AddSpecialEffect(Characters.RennalaStudent16, 14394)
    AddSpecialEffect(character, 14361)
    WaitFrames(frames=1)
    EnableFlag(flag)
    DisableThisSlotFlag()
    OR_1.Add(CharacterHasSpecialEffect(character_1, 14396, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_1)
    EnableFlag(14003806)
    End()


@RestartOnRest(14003950)
def Event_14003950(_, flag: uint, asset: uint):
    """Event 14003950"""
    AND_1.Add(AssetDestroyed(asset))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(14003834)
def Event_14003834(_, asset: uint):
    """Event 14003834"""
    if ThisEventSlotFlagDisabled():
        SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
        Restart()
    
    MAIN.Await(ThisEventSlotFlagDisabled())
    
    Wait(20.0)
    EnableAsset(asset)
    ForceAnimation(asset, 2, wait_for_completion=True)
    Wait(3.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()


@RestartOnRest(14003840)
def Event_14003840(_, character: uint, left: uint, left_1: uint, left_2: uint, flag: uint, flag_1: uint, flag_2: uint):
    """Event 14003840"""
    WaitFrames(frames=1)
    SkipLinesIfUnsignedEqual(2, left=left_2, right=0)
    SkipLinesIfFlagDisabled(1, flag_2)
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=left_2, radius=10.0))
    SkipLinesIfUnsignedEqual(2, left=left_1, right=0)
    SkipLinesIfFlagDisabled(1, flag_1)
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=left_1, radius=10.0))
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    SkipLinesIfFlagDisabled(1, flag)
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=left, radius=10.0))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14367))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 14367)
    ReplanAI(character)
    Wait(8.0)
    Restart()


@RestartOnRest(14003845)
def Event_14003845(
    _,
    character: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
    asset_4: uint,
    asset_5: uint,
):
    """Event 14003845"""
    MAIN.Await(CharacterHasSpecialEffect(character, 14362))
    
    if FlagEnabled(asset_5):
        CreateAssetVFX(asset_2, vfx_id=200, model_point=814625)
    if FlagEnabled(asset_4):
        CreateAssetVFX(asset_1, vfx_id=200, model_point=814625)
    if FlagEnabled(asset_3):
        CreateAssetVFX(asset, vfx_id=200, model_point=814625)
    Wait(1.5)
    if FlagEnabled(asset_5):
        OR_1.Add(EntityWithinDistance(entity=20000, other_entity=asset_2, radius=4.5))
    if FlagEnabled(asset_4):
        OR_1.Add(EntityWithinDistance(entity=20000, other_entity=asset_1, radius=4.5))
    if FlagEnabled(asset_3):
        OR_1.Add(EntityWithinDistance(entity=20000, other_entity=asset, radius=4.5))
    OR_1.Add(TimeElapsed(seconds=5.0))
    AwaitConditionTrue(OR_1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L10, character=character, special_effect=14363)
    ReplanAI(character)
    ForceAnimation(character, 3014)
    Wait(0.699999988079071)
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=asset_2, radius=4.5))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=asset_5)
    GotoIfAssetDestroyed(Label.L0, asset=asset_5)
    DisableNetworkFlag(asset_5)
    ShootProjectile(
        owner_entity=character,
        source_entity=asset_2,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableAsset(asset_2)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=asset_1, radius=4.5))
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    GotoIfFlagDisabled(Label.L1, flag=asset_4)
    GotoIfAssetDestroyed(Label.L1, asset=asset_4)
    DisableNetworkFlag(asset_4)
    ShootProjectile(
        owner_entity=character,
        source_entity=asset_1,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableAsset(asset_1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(EntityWithinDistance(entity=20000, other_entity=asset, radius=4.5))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    GotoIfFlagDisabled(Label.L2, flag=asset_3)
    GotoIfAssetDestroyed(Label.L2, asset=asset_3)
    DisableNetworkFlag(asset_3)
    ShootProjectile(
        owner_entity=character,
        source_entity=asset,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableAsset(asset)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 10 --- #
    DefineLabel(10)
    DeleteAssetVFX(asset_2)
    DeleteAssetVFX(asset_1)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(14003850)
def Event_14003850(
    _,
    character: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
    asset_4: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    flag_4: uint,
    asset__asset_flag: uint,
    asset__asset_flag_1: uint,
    asset__asset_flag_2: uint,
    asset__asset_flag_3: uint,
    asset__asset_flag_4: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
    region_4: uint,
):
    """Event 14003850"""
    MAIN.Await(CharacterHasSpecialEffect(character, 14363))
    
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region)
    if FlagEnabled(flag):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag)
        ForceAnimation(asset, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag,
            asset=asset__asset_flag,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_1)
    if FlagEnabled(flag_1):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_1)
        ForceAnimation(asset_1, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_1,
            asset=asset__asset_flag_1,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_1)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_2)
    if FlagEnabled(flag_2):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_2)
        ForceAnimation(asset_2, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_2,
            asset=asset__asset_flag_2,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_2)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_3)
    if FlagEnabled(flag_3):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_3)
        ForceAnimation(asset_3, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_3,
            asset=asset__asset_flag_3,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_3)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_4)
    if FlagEnabled(flag_4):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_4)
        ForceAnimation(asset_4, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_4,
            asset=asset__asset_flag_4,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_4)
        Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    Restart()


@NeverRestart(14003880)
def Event_14003880(
    _,
    character: uint,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
):
    """Event 14003880"""
    DisableNetworkSync()
    if FlagEnabled(14000899):
        return
    GotoIfThisEventSlotFlagDisabled(Label.L10)
    OR_14.Add(CharacterType(20000, character_type=CharacterType.WhitePhantom))
    if not OR_14:
        return
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(20000, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=0)
        End()
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(20000, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=0)
        End()
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(20000, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    OR_15.Add(CharacterType(20000, character_type=CharacterType.WhitePhantom))
    OR_15.Add(CharacterType(20000, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, OR_15)
    End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    WaitFrames(frames=1)
    DisableAI(Characters.RennalaPhaseTwo)
    SetNetworkUpdateRate(14005810, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    Wait(4.0)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    DisableBossHealthBar(character)
    Wait(3.0)
    AND_10.Add(CharacterType(ProtectedEntities.ClientPlayer1, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L0, input_condition=AND_10)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer1,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer1,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer1,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 0 --- #
    DefineLabel(0)
    AND_11.Add(CharacterType(ProtectedEntities.ClientPlayer2, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L1, input_condition=AND_11)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer2,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer2,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer2,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    AND_12.Add(CharacterType(ProtectedEntities.ClientPlayer3, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L2, input_condition=AND_12)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer3,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer3,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer3,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(flag_2):
        return
    AND_13.Add(CharacterType(ProtectedEntities.ClientPlayer4, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L3, input_condition=AND_13)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer4,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer4,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer4,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagEnabled(flag_2):
        return
    AND_14.Add(CharacterType(ProtectedEntities.ClientPlayer5, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L4, input_condition=AND_14)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer5,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer5,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer5,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)


@RestartOnRest(14003885)
def Event_14003885(
    _,
    character: uint,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    special_effect: int,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 14003885"""
    MAIN.Await(CharacterHasSpecialEffect(character, 14372))
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_1)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_2)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_3)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(14003886)
def Event_14003886(_, character: uint, region: uint, special_effect__special_effect_id: int):
    """Event 14003886"""
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect__special_effect_id, target_count=0.0))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect__special_effect_id)
    Restart()


@RestartOnRest(14003892)
def Event_14003892(_, character: uint, character_1: uint):
    """Event 14003892"""
    MAIN.Await(CharacterHasSpecialEffect(character, 14378))
    
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(1.0)
    Restart()


@RestartOnRest(14003893)
def Event_14003893(_, character: uint, character_1: uint):
    """Event 14003893"""
    MAIN.Await(CharacterHasSpecialEffect(character, 5028))
    
    AddSpecialEffect(character_1, 14353)
    Wait(1.0)
    Restart()


@RestartOnRest(14003894)
def Event_14003894(_, character: uint, character_1: uint):
    """Event 14003894"""
    MAIN.Await(CharacterHasSpecialEffect(character, 5029))
    
    AddSpecialEffect(character_1, 14355)
    Wait(1.0)
    Restart()


@RestartOnRest(14003898)
def Event_14003898(
    _,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
):
    """Event 14003898"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal, target_comparison_type=ComparisonType.NotEqual))
    Wait(40.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_1, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_1, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_1, special_effect=14393)
    AddSpecialEffect(character_1, 14367)
    ReplanAI(character_1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_2, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_2, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_2, special_effect=14393)
    AddSpecialEffect(character_2, 14367)
    ReplanAI(character_2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_3, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_3, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_3, special_effect=14393)
    AddSpecialEffect(character_3, 14367)
    ReplanAI(character_3)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_4, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_4, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_4, special_effect=14393)
    AddSpecialEffect(character_4, 14367)
    ReplanAI(character_4)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_5, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_5, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_5, special_effect=14393)
    AddSpecialEffect(character_5, 14367)
    ReplanAI(character_5)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_6, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_6, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_6, special_effect=14393)
    AddSpecialEffect(character_6, 14367)
    ReplanAI(character_6)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_7, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_7, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_7, special_effect=14393)
    AddSpecialEffect(character_7, 14367)
    ReplanAI(character_7)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_8, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_8, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_8, special_effect=14393)
    AddSpecialEffect(character_8, 14367)
    ReplanAI(character_8)
    DisableThisSlotFlag()
    Restart()


@RestartOnRest(14003900)
def Event_14003900(_, owner_entity: uint, source_entity: uint):
    """Event 14003900"""
    WaitRandomSeconds(min_seconds=3.0, max_seconds=10.0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=220400180,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@RestartOnRest(14003915)
def Event_14003915():
    """Event 14003915"""
    MAIN.Await(FlagEnabled(14000800))
    
    Kill(14005810)
    End()


@RestartOnRest(14003922)
def Event_14003922(_, flag: uint, character: uint, character_1: uint):
    """Event 14003922"""
    AND_1.Add(CharacterHasSpecialEffect(character, 14580))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=230,
        copy_draw_parent=character,
    )
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    ReplanAI(character_1)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 20010)
    Wait(0.800000011920929)
    EnableAnimations(character_1)
    Restart()


@RestartOnRest(14003923)
def Event_14003923(_, flag: uint, flag_1: uint, character: uint, character_1: uint):
    """Event 14003923"""
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterHasSpecialEffect(character, 14572))
    OR_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    RemoveSpecialEffect(character_1, 14590)
    ReplanAI(character_1)
    Wait(3.0)
    Restart()


@RestartOnRest(14003924)
def Event_14003924(_, flag: uint, flag_1: uint, character: uint):
    """Event 14003924"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    DisableFlag(flag_1)
    RemoveSpecialEffect(character, 14573)
    Restart()


@RestartOnRest(14003925)
def Event_14003925(_, flag: uint, character: uint):
    """Event 14003925"""
    AND_1.Add(HealthValue(character) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14573))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 20011)
    Wait(5.0)
    Restart()


@RestartOnRest(14003926)
def Event_14003926(_, character: uint):
    """Event 14003926"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(character)
        DisableAnimations(character)
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14574))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    RemoveSpecialEffect(character, 14572)
    RemoveSpecialEffect(character, 14573)
    RemoveSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003937)
def Event_14003937(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
):
    """Event 14003937"""
    AND_1.Add(CharacterHasSpecialEffect(character, 14595))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=71,
        copy_draw_parent=character,
    )
    ReplanAI(character_2)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_1, 20015)
    RemoveSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    Wait(0.10000000149011612)
    EnableCharacter(character_2)
    EnableAnimations(character_2)
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=72,
        copy_draw_parent=character,
    )
    ReplanAI(character_2)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_2, 20015)
    RemoveSpecialEffect(character_2, 14574)
    Wait(0.20000000298023224)
    EnableCharacter(character_3)
    EnableAnimations(character_3)
    Move(
        character_3,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=73,
        copy_draw_parent=character,
    )
    ReplanAI(character_3)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_3, 20015)
    RemoveSpecialEffect(character_3, 14574)
    Wait(0.10000000149011612)
    EnableCharacter(character_4)
    EnableAnimations(character_4)
    Move(
        character_4,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=70,
        copy_draw_parent=character,
    )
    ReplanAI(character_4)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_4, 20015)
    RemoveSpecialEffect(character_4, 14574)
    Restart()


@RestartOnRest(14003938)
def Event_14003938(
    _,
    flag: uint,
    flag_1: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
):
    """Event 14003938"""
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterHasSpecialEffect(character, 14572))
    OR_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterHasSpecialEffect(character_1, 14572))
    OR_2.Add(CharacterHasSpecialEffect(character_1, 14573))
    AND_1.Add(OR_2)
    OR_3.Add(CharacterHasSpecialEffect(character_2, 14572))
    OR_3.Add(CharacterHasSpecialEffect(character_2, 14573))
    AND_1.Add(OR_3)
    OR_4.Add(CharacterHasSpecialEffect(character_3, 14572))
    OR_4.Add(CharacterHasSpecialEffect(character_3, 14573))
    AND_1.Add(OR_4)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    RemoveSpecialEffect(character_4, 14590)
    ReplanAI(character_4)
    Restart()


@RestartOnRest(14003939)
def Event_14003939(
    _,
    flag: uint,
    flag_1: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
):
    """Event 14003939"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(CharacterHasSpecialEffect(character_1, 14573))
    AND_1.Add(CharacterHasSpecialEffect(character_2, 14573))
    AND_1.Add(CharacterHasSpecialEffect(character_3, 14573))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    DisableFlag(flag_1)
    RemoveSpecialEffect(character, 14573)
    RemoveSpecialEffect(character_1, 14573)
    RemoveSpecialEffect(character_2, 14573)
    RemoveSpecialEffect(character_3, 14573)
    Restart()


@RestartOnRest(14003940)
def Event_14003940(_, flag: uint, character: uint):
    """Event 14003940"""
    AND_1.Add(HealthValue(character) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14573))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DisableAnimations(character)
    ForceAnimation(character, 3035)
    Wait(5.0)
    Restart()


@RestartOnRest(14003945)
def Event_14003945(_, character: uint):
    """Event 14003945"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(character)
        DisableAnimations(character)
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14574))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    RemoveSpecialEffect(character, 14572)
    RemoveSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003962)
def Event_14003962(_, flag: uint, character: uint, character_1: uint):
    """Event 14003962"""
    AND_1.Add(CharacterHasSpecialEffect(character, 14585))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=243,
        copy_draw_parent=character,
    )
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    ReplanAI(character_1)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 20026)
    DisableAnimations(character_1)
    Wait(4.0)
    EnableAnimations(character_1)
    Restart()


@RestartOnRest(14003963)
def Event_14003963(_, flag: uint, flag_1: uint, character: uint, character_1: uint):
    """Event 14003963"""
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterHasSpecialEffect(character, 14572))
    OR_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    RemoveSpecialEffect(character_1, 14590)
    ReplanAI(character_1)
    Restart()


@RestartOnRest(14003964)
def Event_14003964(_, flag: uint, flag_1: uint, character: uint):
    """Event 14003964"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    DisableFlag(flag_1)
    RemoveSpecialEffect(character, 14573)
    Restart()


@RestartOnRest(14003965)
def Event_14003965(_, flag: uint, character: uint):
    """Event 14003965"""
    AND_1.Add(HealthValue(character) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14573))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 20025)
    Wait(5.0)
    Restart()


@RestartOnRest(14003966)
def Event_14003966(_, character: uint):
    """Event 14003966"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(character)
        DisableAnimations(character)
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14574))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    RemoveSpecialEffect(character, 14572)
    RemoveSpecialEffect(character, 14573)
    RemoveSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003972)
def Event_14003972(_, flag: uint, character: uint, character_1: uint):
    """Event 14003972"""
    AND_1.Add(CharacterHasSpecialEffect(character, 14575))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=65,
        copy_draw_parent=character,
    )
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    ReplanAI(character_1)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 20026)
    Wait(0.800000011920929)
    EnableAnimations(character_1)
    Restart()


@RestartOnRest(14003973)
def Event_14003973(_, flag: uint, flag_1: uint, character: uint, character_1: uint):
    """Event 14003973"""
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterHasSpecialEffect(character, 14572))
    OR_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    RemoveSpecialEffect(character_1, 14590)
    ReplanAI(character_1)
    Restart()


@RestartOnRest(14003974)
def Event_14003974(_, flag: uint, flag_1: uint, character: uint):
    """Event 14003974"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    DisableFlag(flag_1)
    RemoveSpecialEffect(character, 14573)
    Restart()


@RestartOnRest(14003975)
def Event_14003975(_, flag: uint, character: uint):
    """Event 14003975"""
    AND_1.Add(HealthValue(character) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14573))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 20027)
    Wait(5.0)
    Restart()


@RestartOnRest(14003976)
def Event_14003976(_, character: uint):
    """Event 14003976"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(character)
        DisableAnimations(character)
    AND_1.Add(CharacterHasSpecialEffect(character, 14573))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14574))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    RemoveSpecialEffect(character, 14572)
    RemoveSpecialEffect(character, 14573)
    RemoveSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003977)
def Event_14003977(_, character: uint, character_1: uint):
    """Event 14003977"""
    MAIN.Await(HealthValue(character) == 0)
    
    AddSpecialEffect(character_1, 14572)
    ReplanAI(character_1)


@RestartOnRest(14003978)
def Event_14003978():
    """Event 14003978"""
    MAIN.Await(FlagEnabled(14000800))
    
    DisableSpawner(entity=14003810)
    DisableSpawner(entity=14003811)
    DisableSpawner(entity=14003812)
    DisableSpawner(entity=14003813)
    DisableSpawner(entity=14003814)
    DisableSpawner(entity=14003815)
    DisableSpawner(entity=14003816)
    DisableSpawner(entity=14003817)
    DisableSpawner(entity=14003818)


@RestartOnRest(14000700)
def Event_14000700():
    """Event 14000700"""
    if FlagEnabled(14009205):
        return
    SetCharacterTalkRange(character=Characters.RennalaPhaseOne1, distance=30.0)
    AND_1.Add(FlagEnabled(14000800))
    AND_1.Add(FlagDisabled(3468))
    AND_1.Add(EntityWithinDistance(entity=Characters.RennalaPhaseOne1, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002705)
    End()


@RestartOnRest(14000701)
def Event_14000701():
    """Event 14000701"""
    if FlagEnabled(14009210):
        return
    SetCharacterTalkRange(character=Characters.RennalaPhaseOne1, distance=30.0)
    AND_1.Add(FlagEnabled(14000800))
    AND_1.Add(FlagEnabled(3468))
    AND_1.Add(EntityWithinDistance(entity=Characters.RennalaPhaseOne2, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002706)
    End()


@RestartOnRest(14000702)
def Event_14000702():
    """Event 14000702"""
    WaitFrames(frames=1)
    DisableCharacter(Characters.RennalaPhaseOne1)
    DisableBackread(Characters.RennalaPhaseOne1)
    DisableCharacter(Characters.RennalaPhaseOne2)
    DisableBackread(Characters.RennalaPhaseOne2)
    AwaitFlagEnabled(flag=9118)
    OR_1.Add(FlagEnabled(3468))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(Characters.RennalaPhaseOne1)
    EnableBackread(Characters.RennalaPhaseOne1)
    ForceAnimation(Characters.RennalaPhaseOne1, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(Characters.RennalaPhaseOne2)
    EnableBackread(Characters.RennalaPhaseOne2)
    ForceAnimation(Characters.RennalaPhaseOne2, 930010)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(14000703)
def Event_14000703():
    """Event 14000703"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9614))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9615))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60540)
    Wait(0.20000000298023224)
    Restart()


@RestartOnRest(14000710)
def Event_14000710(_, asset__character: uint, asset__character_1: uint):
    """Event 14000710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3460))
    AND_1.Add(FlagEnabled(14009253))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(14009253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableCharacter(asset__character_1)
    DisableBackread(asset__character_1)
    OR_1.Add(FlagEnabled(3468))
    OR_1.Add(FlagEnabled(3469))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3468))
    OR_2.Add(FlagEnabled(3469))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)
    GotoIfFlagEnabled(Label.L4, flag=3462)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(3468):
        EnableCharacter(asset__character)
        EnableBackread(asset__character)
        ForceAnimation(asset__character, 90100)
    if FlagEnabled(14002713):
        Move(asset__character, destination=14002701, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(3469):
        EnableCharacter(asset__character_1)
        EnableBackread(asset__character_1)
        SetTeamType(asset__character_1, TeamType.FriendlyNPC)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(3468):
        EnableCharacter(asset__character)
        EnableBackread(asset__character)
        SetTeamType(asset__character, TeamType.HostileNPC)
    if FlagEnabled(3469):
        EnableCharacter(asset__character_1)
        EnableBackread(asset__character_1)
        SetTeamType(asset__character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    if FlagEnabled(3468):
        DropMandatoryTreasure(asset__character)
        DisableCharacter(asset__character)
        DisableBackread(asset__character)
        DisableAsset(asset__character)
    if FlagEnabled(3469):
        DropMandatoryTreasure(asset__character_1)
        DisableCharacter(asset__character_1)
        DisableBackread(asset__character_1)
        DisableAsset(asset__character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3468))
    OR_15.Add(FlagEnabled(3469))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(14000711)
def Event_14000711():
    """Event 14000711"""
    if FlagEnabled(3463):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(Characters.SorceressSellen0) == 0)
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(Characters.SorceressSellen0, True)
    AND_2.Add(TimeElapsed(seconds=20.0))
    
    MAIN.Await(AND_2)
    
    SetBackreadStateAlternate(Characters.SorceressSellen0, False)
    End()


@RestartOnRest(14000712)
def Event_14000712():
    """Event 14000712"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400401):
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(7609))
    AwaitConditionTrue(AND_2)
    EnableFlag(14002713)
    AwardItemLot(104010, host_only=False)
    End()


@RestartOnRest(14000713)
def Event_14000713():
    """Event 14000713"""
    AwaitFlagEnabled(flag=7609)
    AwaitFlagEnabled(flag=14002713)
    Move(Characters.SorceressSellen0, destination=14002701, destination_type=CoordEntityType.Region, short_move=True)
    End()


@RestartOnRest(14000714)
def Event_14000714():
    """Event 14000714"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3461, 3463)))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1034509259)
    End()


@RestartOnRest(14000720)
def Event_14000720():
    """Event 14000720"""
    if FlagEnabled(14009300):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002080))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 14307))
    
    MAIN.Await(AND_1)
    
    EnableFlag(14009300)
    End()


@RestartOnRest(14000730)
def Event_14000730(_, character: uint):
    """Event 14000730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3360):
        DisableFlag(1041339253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3371)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3371))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
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
    
    MAIN.Await(FlagDisabled(3371))
    
    Restart()


@RestartOnRest(14000731)
def Event_14000731():
    """Event 14000731"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400106):
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(7608))
    AwaitConditionTrue(AND_2)
    AwardItemLot(101060, host_only=False)
    End()


@RestartOnRest(14000740)
def Event_14000740(_, character: uint):
    """Event 14000740"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3948)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3948))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L4, flag=3943)

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
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3948))
    
    Restart()


@RestartOnRest(14000741)
def Event_14000741(_, character: uint):
    """Event 14000741"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3949)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3949))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930025)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3949))
    
    Restart()


@RestartOnRest(14000742)
def Event_14000742():
    """Event 14000742"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3943):
        return
    AND_1.Add(FlagEnabled(3948))
    AND_1.Add(FlagDisabled(11109306))
    AND_1.Add(EntityWithinDistance(entity=Characters.BoctheSeamster, other_entity=20000, radius=4.0))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109306)
    End()


@RestartOnRest(14000750)
def Event_14000750(_, character: uint, asset: uint):
    """Event 14000750"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3806)
    DisableCharacter(character)
    DisableBackread(character)
    EnableAsset(asset)
    
    MAIN.Await(FlagEnabled(3806))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    DisableGravity(character)
    DisableAnimations(character)
    ResetCharacterPosition(character=character)
    EnableAsset(asset)
    EnableAssetInvulnerability(asset)
    ForceAnimation(character, 90103)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3806))
    
    Restart()

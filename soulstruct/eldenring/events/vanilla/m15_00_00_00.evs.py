"""
Miquella's Haligtree

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
from .enums.m15_00_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    DisableAsset(Assets.AEG099_332_9000)
    CommonFunc_9005810(
        0,
        flag=15000800,
        grace_flag=15000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=0.0,
    )
    CommonFunc_9005810(
        0,
        flag=15000850,
        grace_flag=15000005,
        character=Characters.TalkDummy5,
        asset=Assets.AEG099_060_9005,
        enemy_block_distance=0.0,
    )
    RegisterGrace(grace_flag=15000001, asset=Assets.AEG099_060_9001, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=15000002, asset=Assets.AEG099_060_9002, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=15000003, asset=Assets.AEG099_060_9003, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=15000004, asset=Assets.AEG099_060_9004, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=15000006, asset=Assets.AEG099_060_9006, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=15000007, asset=Assets.AEG099_060_9007, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=15000008, asset=Assets.AEG099_060_9008, enemy_block_distance=8.0)
    Event_15002800()
    Event_15002810()
    Event_15002811()
    Event_15002820(0, character=Characters.Malenia2, animation_id=3030, special_effect=18451)
    Event_15002820(1, character=Characters.Malenia3, animation_id=3031, special_effect=18452)
    Event_15002820(2, character=Characters.Malenia4, animation_id=3032, special_effect=18453)
    Event_15002820(3, character=Characters.Malenia5, animation_id=3033, special_effect=18454)
    Event_15002830(0, special_effect=18410, special_effect_1=18420)
    Event_15002830(1, special_effect=18411, special_effect_1=18421)
    Event_15002830(2, special_effect=18412, special_effect_1=18422)
    Event_15002830(3, special_effect=18413, special_effect_1=18423)
    Event_15002830(4, special_effect=18414, special_effect_1=18424)
    Event_15002830(5, special_effect=18415, special_effect_1=18425)
    Event_15002830(6, special_effect=18416, special_effect_1=18426)
    Event_15002830(7, special_effect=18417, special_effect_1=18427)
    Event_15002830(8, special_effect=18418, special_effect_1=18428)
    Event_15002830(9, special_effect=18419, special_effect_1=18429)
    Event_15002848(0, special_effect=18031, locked_camera_id__normal_camera_id=2122)
    Event_15002849()
    Event_15002850()
    Event_15002860()
    Event_15002861()
    Event_15002899()
    CommonFunc_90005795(
        0,
        flag=7610,
        flag_1=0,
        flag_2=15009208,
        left_flag=15002141,
        cancel_flag__right_flag=15002142,
        message=80610,
        action_button_id=9060,
        asset=Assets.AEG099_090_9002,
        model_point=30000,
    )
    if CeremonyActive(ceremony=20):
        CommonFunc_90005797(0, flag=7610, character=15005706, banner_type=7, region=15002142, special_effect=4823)
    Event_15002145()
    CommonFunc_90005795(
        0,
        flag=7611,
        flag_1=0,
        flag_2=15009209,
        left_flag=15002151,
        cancel_flag__right_flag=15002152,
        message=80611,
        action_button_id=9061,
        asset=Assets.AEG099_090_9003,
        model_point=30010,
    )
    if CeremonyActive(ceremony=30):
        CommonFunc_90005796(0, flag=7611, character=Characters.Millicent2, banner_type=5, region=15002151)
    Event_15002155()
    CommonFunc_90005300(0, flag=15000390, character=15000390, item_lot=15001250, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=15000391, character=15000391, item_lot=15001260, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=15000392, character=Characters.PutridAvatar0, item_lot=15001270, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=15000393, character=Characters.PutridAvatar1, item_lot=15001280, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=15000394, character=15000394, item_lot=15001290, seconds=0.0, left=0)
    CommonFunc_90005300(
        0,
        flag=15000398,
        character=Characters.UlceratedTreeSpirit,
        item_lot=15001200,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Scarab0,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=Characters.Scarab2, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=Characters.Scarab3, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy0,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy1,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy2,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy18,
        animation_id=30000,
        animation_id_1=20000,
        region=15002418,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy3,
        animation_id=30000,
        animation_id_1=20000,
        region=15002403,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy4,
        animation_id=30000,
        animation_id_1=20000,
        region=15002404,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy5,
        animation_id=30000,
        animation_id_1=20000,
        region=15002404,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy6,
        animation_id=30000,
        animation_id_1=20000,
        region=15002404,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy14,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy15,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=15000431,
        animation_id=30000,
        animation_id_1=20000,
        region=15002403,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Misbegotten0, region=15002360, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Misbegotten1,
        animation_id=30005,
        animation_id_1=20005,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Misbegotten2,
        animation_id=30005,
        animation_id_1=20005,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Misbegotten3,
        animation_id=30002,
        animation_id_1=20002,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Misbegotten4, region=15002364, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Misbegotten5,
        animation_id=30001,
        animation_id_1=20001,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Misbegotten6, region=15002387, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Misbegotten7, region=15002387, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Misbegotten8, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten9,
        region=15002369,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=3008,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten10,
        region=15002371,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Misbegotten11,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.399999976158142,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.ScalyMisbegotten0,
        region=15002380,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.ScalyMisbegotten1,
        region=15002381,
        radius=0.10000000149011612,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005201(
        0,
        character=Characters.ScalyMisbegotten2,
        animation_id=30005,
        animation_id_1=20005,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.ScalyMisbegotten3,
        region=15002383,
        radius=0.10000000149011612,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeonineMisbegotten1,
        animation_id=30001,
        animation_id_1=20001,
        region=15002387,
        radius=1.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.BattleMage0, region=15002340, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse0,
        region=15002450,
        radius=1.0,
        seconds=0.0,
        animation_id=3021,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse1,
        region=15002450,
        radius=1.0,
        seconds=0.20000000298023224,
        animation_id=3021,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse2,
        region=15002450,
        radius=1.0,
        seconds=0.20000000298023224,
        animation_id=3021,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse3,
        region=15002450,
        radius=1.0,
        seconds=0.10000000149011612,
        animation_id=3021,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse4,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse5,
        region=15002455,
        radius=1.0,
        seconds=0.0,
        animation_id=3037,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse6,
        region=15002456,
        radius=1.0,
        seconds=0.0,
        animation_id=3037,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse7,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse8,
        animation_id=30006,
        animation_id_1=20006,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse9,
        animation_id=30006,
        animation_id_1=20006,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse20,
        region=15002470,
        radius=1.0,
        seconds=0.0,
        animation_id=3037,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse21,
        region=15002470,
        radius=1.0,
        seconds=0.5,
        animation_id=3037,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Revenant0,
        animation_id=30000,
        animation_id_1=20000,
        region=15002330,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Revenant1,
        animation_id=30000,
        animation_id_1=20000,
        region=15002331,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Revenant2,
        animation_id=30000,
        animation_id_1=20000,
        region=15002332,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Revenant4,
        animation_id=30000,
        animation_id_1=20000,
        region=15002334,
        radius=1.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier1,
        animation_id=30005,
        animation_id_1=20005,
        region=15002202,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005213(
        0,
        character=Characters.HaligtreeSoldier2,
        animation_id=30002,
        animation_id_1=20002,
        region=15002203,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.HaligtreeSoldier3,
        seconds_1=0.5,
    )
    CommonFunc_90005213(
        0,
        character=Characters.HaligtreeSoldier3,
        animation_id=30001,
        animation_id_1=20001,
        region=15002203,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=1,
        left_2=1,
        left_3=0,
        character_1=Characters.HaligtreeSoldier2,
        seconds_1=1.0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier4,
        animation_id=30002,
        animation_id_1=20002,
        region=15002205,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier5,
        animation_id=30002,
        animation_id_1=20002,
        region=15002206,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier6,
        animation_id=30002,
        animation_id_1=20002,
        region=15002206,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier7,
        animation_id=30003,
        animation_id_1=20003,
        region=15002208,
        radius=0.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier8,
        animation_id=30001,
        animation_id_1=20001,
        region=15002208,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier9,
        animation_id=30005,
        animation_id_1=20005,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier10,
        animation_id=30005,
        animation_id_1=20005,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier12,
        animation_id=30002,
        animation_id_1=20002,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.HaligtreeSoldier13, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier14,
        animation_id=30004,
        animation_id_1=20004,
        region=15002218,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier15,
        animation_id=30003,
        animation_id_1=20003,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeSoldier17,
        region=15002221,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeSoldier18,
        region=15002221,
        radius=1.0,
        seconds=0.10000000149011612,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeSoldier19,
        region=15002226,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeSoldier20,
        region=15002227,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier21,
        animation_id=30002,
        animation_id_1=20002,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=15000229,
        animation_id=30002,
        animation_id_1=20002,
        region=0,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.HaligtreeSoldier25, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier26,
        animation_id=30003,
        animation_id_1=20003,
        region=15002234,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier27,
        animation_id=30005,
        animation_id_1=20005,
        region=15002235,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier28,
        animation_id=30003,
        animation_id_1=20003,
        region=15002236,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier29,
        animation_id=30005,
        animation_id_1=20005,
        region=15002238,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.HaligtreeSoldier35,
        animation_id=30003,
        animation_id_1=20003,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.HaligtreeSoldier36,
        animation_id=30002,
        animation_id_1=20002,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.HaligtreeSoldier37,
        animation_id=30002,
        animation_id_1=20002,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.HaligtreeSoldier40,
        animation_id=30003,
        animation_id_1=20003,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.HaligtreeSoldier41,
        animation_id=30004,
        animation_id_1=20004,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.HaligtreeSoldier42, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier43,
        animation_id=30002,
        animation_id_1=20002,
        region=15002258,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeSoldier44,
        animation_id=30002,
        animation_id_1=20002,
        region=15002258,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeFootSoldier0,
        region=15002260,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeFootSoldier1,
        region=15002260,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeFootSoldier2,
        region=15002260,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeFootSoldier3,
        region=15002260,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeFootSoldier6,
        animation_id=30010,
        animation_id_1=20010,
        region=15002266,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeKnight0,
        animation_id=30000,
        animation_id_1=20000,
        region=15002270,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeKnight2,
        animation_id=30000,
        animation_id_1=20000,
        region=15002272,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeKnight3,
        animation_id=30000,
        animation_id_1=20000,
        region=15002273,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.HaligtreeKnight4,
        animation_id=30000,
        animation_id_1=20000,
        region=15002274,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeKnight5,
        region=15002275,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.HaligtreeKnight6,
        region=15002275,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_15002310(0, character=Characters.Crystalian0, character_1=Characters.Snail0)
    Event_15002310(1, character=Characters.Crystalian1, character_1=Characters.Snail1)
    Event_15002310(2, character=Characters.Crystalian2, character_1=Characters.Snail2)
    CommonFunc_90005211(
        0,
        character=Characters.Crystalian3,
        animation_id=30000,
        animation_id_1=20000,
        region=15002322,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Crystalian4,
        animation_id=30000,
        animation_id_1=20000,
        region=15002323,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Crystalian5,
        animation_id=30000,
        animation_id_1=20000,
        region=15002324,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Crystalian6,
        animation_id=30001,
        animation_id_1=20001,
        region=15002326,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Crystalian7,
        animation_id=30001,
        animation_id_1=20001,
        region=15002327,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Crystalian8,
        animation_id=30001,
        animation_id_1=20001,
        region=15002327,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Crystalian9,
        animation_id=30001,
        animation_id_1=20001,
        region=15002327,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Snail0,
        region=15002344,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=30002,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Snail1,
        region=15002345,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=30002,
    )
    CommonFunc_90005261(0, character=Characters.Snail2, region=15002346, radius=1.0, seconds=0.0, animation_id=30002)
    Event_15002344(0, character=Characters.Snail0, entity=15003344)
    Event_15002344(1, character=Characters.Snail1, entity=15003345)
    Event_15002344(2, character=Characters.Snail2, entity=15003346)
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot0,
        region=15002280,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot1,
        region=15002281,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot2,
        region=15002282,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot14,
        animation_id=30000,
        animation_id_1=20001,
        region=0,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot15,
        region=15002296,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot16,
        animation_id=30000,
        animation_id_1=20001,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot17,
        animation_id=30000,
        animation_id_1=20001,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot18,
        animation_id=30000,
        animation_id_1=20001,
        region=0,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot3,
        region=15002283,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot4,
        region=15002284,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot5,
        region=15002285,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot7,
        region=15002280,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot8,
        animation_id=30002,
        animation_id_1=20005,
        region=15002288,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot9,
        animation_id=30000,
        animation_id_1=20001,
        region=15002288,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot10,
        animation_id=30000,
        animation_id_1=20001,
        region=15002288,
        radius=1.0,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRot11,
        animation_id=30002,
        animation_id_1=20005,
        region=15002281,
        radius=1.0,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot12,
        region=15002292,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.KindredofRot13,
        region=15002291,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005201(
        0,
        character=Characters.KindredofRotLarva9,
        animation_id=30001,
        animation_id_1=20001,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRotLarva10,
        animation_id=30001,
        animation_id_1=20001,
        region=15002275,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRotLarva11,
        animation_id=30001,
        animation_id_1=20001,
        region=15002275,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRotLarva12,
        animation_id=30000,
        animation_id_1=20000,
        region=15002278,
        radius=1.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRotLarva13,
        animation_id=30000,
        animation_id_1=20000,
        region=15002278,
        radius=1.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRotLarva14,
        animation_id=30000,
        animation_id_1=20000,
        region=15002278,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.KindredofRotLarva16,
        animation_id=30001,
        animation_id_1=20001,
        region=15002275,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.CleanrotKnight0,
        region=15002300,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GiantMirandaRotFlower6,
        region=15002356,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaRotFlower3,
        region=15002356,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaRotFlower4,
        region=15002356,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaRotFlower5,
        region=15002356,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridAvatar0,
        region=15002392,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.UlceratedTreeSpirit,
        animation_id=30002,
        animation_id_1=20002,
        region=15002398,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005501(
        0,
        flag=15000520,
        flag_1=15001520,
        left=0,
        asset=Assets.AEG267_024_0500,
        asset_1=Assets.AEG267_023_0504,
        asset_2=Assets.AEG267_023_0505,
        flag_2=15000521,
    )
    CommonFunc_90005501(
        0,
        flag=15000525,
        flag_1=15001525,
        left=0,
        asset=Assets.AEG267_027_0500,
        asset_1=Assets.AEG267_023_0507,
        asset_2=Assets.AEG267_023_0506,
        flag_2=15000526,
    )
    Event_15002520()
    CommonFunc_90005501(
        0,
        flag=15000620,
        flag_1=15001620,
        left=0,
        asset=Assets.AEG267_028_0500,
        asset_1=Assets.AEG267_023_0501,
        asset_2=Assets.AEG267_023_0500,
        flag_2=15000621,
    )
    CommonFunc_90005501(
        0,
        flag=15000625,
        flag_1=15001625,
        left=0,
        asset=Assets.AEG267_026_0500,
        asset_1=Assets.AEG267_038_0500,
        asset_2=Assets.AEG267_038_0501,
        flag_2=15000626,
    )
    Event_15002620()
    CommonFunc_90005620(
        0,
        flag=15000570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=15002570,
        cancel_flag__right_flag=15002571,
        right=15002572,
    )
    CommonFunc_90005621(0, flag=15000570, asset=Assets.AEG099_272_9000)
    CommonFunc_90005620(
        0,
        flag=15000575,
        asset=Assets.AEG027_079_9001,
        asset_1=Assets.AEG027_216_9001,
        asset_2=0,
        left_flag=15002575,
        cancel_flag__right_flag=15002576,
        right=15002577,
    )
    CommonFunc_90005621(0, flag=15000575, asset=Assets.AEG099_272_9001)
    Event_15002580()
    Event_15002680()
    Event_15000700()
    Event_15000701()
    Event_15000702(0, asset=Assets.AEG099_332_9000, asset_1=Assets.AEG099_090_9001)
    Event_15000710(0, character=Characters.Millicent0)
    CommonFunc_90005704(0, attacked_entity=Characters.Millicent0, flag=4181, flag_1=4180, flag_2=15002901, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Millicent0,
        flag=4181,
        flag_1=4182,
        flag_2=15002901,
        flag_3=1059481190,
        first_flag=4180,
        last_flag=4184,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Millicent0, flag=4183, first_flag=4180, last_flag=4184)
    Event_15000711(0, character=Characters.Millicent3)
    CommonFunc_90005708(0, character=Characters.Millicent3, flag=4180, left=0)
    CommonFunc_90005702(0, character=Characters.Millicent3, flag=4183, first_flag=4180, last_flag=4184)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9000,
        action_button_id=4350,
        item_lot=103210,
        first_flag=400321,
        last_flag=400321,
        flag=4192,
        model_point=0,
    )
    CommonFunc_90005752(0, asset=15001704, vfx_id=200, model_point=120, seconds=3.0)
    Event_15000712(0, asset=Assets.AEG267_063_3000)
    Event_15000713(0, entity=Assets.AEG099_090_9001)
    Event_15000715()
    Event_15000716()
    CommonFunc_90005774(0, flag=7611, item_lot=103220, flag_1=400323)
    CommonFunc_90005774(0, flag=7610, item_lot=104800, flag_1=400480)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Millicent0)
    DisableBackread(Characters.Millicent1)
    DisableBackread(Characters.Millicent2)
    DisableBackread(Characters.Millicent3)
    DisableBackread(Characters.MaryEldestSister0)
    DisableBackread(Characters.MaryEldestSister1)
    DisableBackread(15000707)
    DisableBackread(Characters.MaureenSecondSister)
    DisableBackread(15000709)
    DisableBackread(Characters.AmyThirdSister)
    DisableBackread(15000711)
    DisableBackread(Characters.PolyannaYoungestSister)
    Event_15000050()
    Event_15002200(4, character=Characters.HaligtreeSoldier3, asset=Assets.AEG260_697_2009)
    Event_15002200(9, character=Characters.HaligtreeSoldier8, asset=Assets.AEG260_697_2006)
    Event_15002550()


@ContinueOnRest(15000050)
def Event_15000050():
    """Event 15000050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(15000525)
    EnableFlag(15000625)


@RestartOnRest(15002145)
def Event_15002145():
    """Event 15002145"""
    if CeremonyInactive(ceremony=20):
        return
    EnableBackread(Characters.Millicent1)
    EnableBackread(Characters.MaryEldestSister1)
    EnableBackread(Characters.MaureenSecondSister)
    EnableBackread(Characters.AmyThirdSister)
    EnableBackread(Characters.PolyannaYoungestSister)
    SetTeamType(Characters.Millicent1, TeamType.Human)
    SetTeamType(Characters.MaryEldestSister1, TeamType.Enemy)
    SetTeamType(Characters.MaureenSecondSister, TeamType.Enemy)
    SetTeamType(Characters.AmyThirdSister, TeamType.Enemy)
    SetTeamType(Characters.PolyannaYoungestSister, TeamType.Enemy)
    CreateAssetVFX(Assets.AEG099_120_9000, vfx_id=200, model_point=806700)


@RestartOnRest(15002155)
def Event_15002155():
    """Event 15002155"""
    if CeremonyInactive(ceremony=30):
        return
    EnableBackread(Characters.Millicent2)
    EnableBackread(Characters.MaryEldestSister0)
    CreateAssetVFX(Assets.AEG099_120_9000, vfx_id=200, model_point=806700)


@RestartOnRest(15002200)
def Event_15002200(_, character: uint, asset: uint):
    """Event 15002200"""
    if ThisEventSlotFlagEnabled():
        return
    EnableAssetInvulnerability(asset)
    Wait(0.10000000149011612)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(asset)


@RestartOnRest(15002310)
def Event_15002310(_, character: uint, character_1: uint):
    """Event 15002310"""
    AND_1.Add(CharacterDead(character_1))
    
    MAIN.Await(AND_1)
    
    Kill(character)


@RestartOnRest(15002344)
def Event_15002344(_, character: uint, entity: uint):
    """Event 15002344"""
    DisableSpawner(entity=entity)
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 15007))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=entity)
    AND_2.Add(CharacterAlive(character))
    AND_2.Add(CharacterHasSpecialEffect(character, 15007))
    
    MAIN.Await(not AND_2)
    
    DisableSpawner(entity=entity)


@ContinueOnRest(15002520)
def Event_15002520():
    """Event 15002520"""
    CommonFunc_90005500(
        0,
        flag=15000520,
        flag_1=15001520,
        left=0,
        asset=Assets.AEG267_024_0500,
        asset_1=Assets.AEG267_023_0504,
        obj_act_id=15003521,
        asset_2=Assets.AEG267_023_0505,
        obj_act_id_1=15003522,
        region=15002521,
        region_1=15002522,
        flag_2=15000521,
        flag_3=15002522,
        left_1=15000523,
    )
    CommonFunc_90015502(0, flag=15000523, asset=Assets.AEG267_023_0504, region=15002522)
    CommonFunc_90005500(
        0,
        flag=15000525,
        flag_1=15001525,
        left=0,
        asset=Assets.AEG267_027_0500,
        asset_1=Assets.AEG267_023_0507,
        obj_act_id=15003526,
        asset_2=Assets.AEG267_023_0506,
        obj_act_id_1=15003527,
        region=15002526,
        region_1=15002527,
        flag_2=15000526,
        flag_3=15002527,
        left_1=0,
    )


@ContinueOnRest(15002620)
def Event_15002620():
    """Event 15002620"""
    CommonFunc_90005500(
        0,
        flag=15000620,
        flag_1=15001620,
        left=0,
        asset=Assets.AEG267_028_0500,
        asset_1=Assets.AEG267_023_0501,
        obj_act_id=15003621,
        asset_2=Assets.AEG267_023_0500,
        obj_act_id_1=15003622,
        region=15002621,
        region_1=15002622,
        flag_2=15000621,
        flag_3=15002622,
        left_1=15000623,
    )
    CommonFunc_90005502(0, flag=15000623, asset=Assets.AEG267_023_0501, region=15002622)
    CommonFunc_90005500(
        0,
        flag=15000625,
        flag_1=15001625,
        left=0,
        asset=Assets.AEG267_026_0500,
        asset_1=Assets.AEG267_038_0500,
        obj_act_id=15003626,
        asset_2=Assets.AEG267_038_0501,
        obj_act_id_1=15003627,
        region=15002626,
        region_1=15002627,
        flag_2=15000626,
        flag_3=15002627,
        left_1=0,
    )


@RestartOnRest(15002550)
def Event_15002550():
    """Event 15002550"""
    EnableAssetInvulnerability(Assets.AEG260_676_2011)
    EnableAssetInvulnerability(Assets.AEG260_676_2029)
    EnableAssetInvulnerability(Assets.AEG260_676_2030)


@RestartOnRest(15002580)
def Event_15002580():
    """Event 15002580"""
    RegisterLadder(start_climbing_flag=15000580, stop_climbing_flag=15000581, asset=Assets.AEG267_021_0500)
    RegisterLadder(start_climbing_flag=15000582, stop_climbing_flag=15000583, asset=Assets.AEG267_022_0500)
    RegisterLadder(start_climbing_flag=15000584, stop_climbing_flag=15000585, asset=Assets.AEG267_020_0500)
    RegisterLadder(start_climbing_flag=15000586, stop_climbing_flag=15000587, asset=Assets.AEG267_019_0500)
    RegisterLadder(start_climbing_flag=15000588, stop_climbing_flag=15000589, asset=Assets.AEG267_025_0500)
    RegisterLadder(start_climbing_flag=15000590, stop_climbing_flag=15000591, asset=Assets.AEG267_017_0500)


@RestartOnRest(15002680)
def Event_15002680():
    """Event 15002680"""
    RegisterLadder(start_climbing_flag=15000680, stop_climbing_flag=15000681, asset=Assets.AEG267_000_0501)
    RegisterLadder(start_climbing_flag=15000682, stop_climbing_flag=15000683, asset=Assets.AEG267_013_0500)
    RegisterLadder(start_climbing_flag=15000684, stop_climbing_flag=15000685, asset=Assets.AEG267_012_0500)
    RegisterLadder(start_climbing_flag=15000686, stop_climbing_flag=15000687, asset=Assets.AEG267_000_0500)
    RegisterLadder(start_climbing_flag=15000688, stop_climbing_flag=15000689, asset=Assets.AEG267_015_0500)
    RegisterLadder(start_climbing_flag=15000690, stop_climbing_flag=15000691, asset=15001690)
    RegisterLadder(start_climbing_flag=15000692, stop_climbing_flag=15000693, asset=Assets.AEG267_014_0500)
    RegisterLadder(start_climbing_flag=15000694, stop_climbing_flag=15000695, asset=Assets.AEG267_014_0501)
    RegisterLadder(start_climbing_flag=15000696, stop_climbing_flag=15000697, asset=Assets.AEG267_018_0500)
    RegisterLadder(start_climbing_flag=15000698, stop_climbing_flag=15000699, asset=Assets.AEG267_016_0500)


@RestartOnRest(15002800)
def Event_15002800():
    """Event 15002800"""
    if FlagEnabled(15000800):
        return
    
    MAIN.Await(HealthValue(Characters.Malenia0) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(15008000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.Malenia0))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(15000800))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=Characters.Malenia0, banner_type=BannerType.DemigodFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableNetworkFlag(15000800)
    EnableFlag(9120)
    if PlayerInOwnWorld():
        EnableFlag(61120)


@RestartOnRest(15002810)
def Event_15002810():
    """Event 15002810"""
    GotoIfFlagDisabled(Label.L0, flag=15000800)
    DisableCharacter(15005800)
    DisableAnimations(15005800)
    Kill(15005800)
    EnableTreasure(asset=15001810)
    DisableAsset(Assets.AEG260_526_3000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(15005800)
    EnableImmortality(Characters.Malenia0)
    DisableCharacter(Characters.Malenia1)
    DisableAnimations(Characters.Malenia1)
    SetLockOnPoint(character=0, lock_on_model_point=-1, state=True)
    DisableCharacter(Characters.Malenia2)
    DisableAnimations(Characters.Malenia2)
    SetLockOnPoint(character=Characters.Malenia2, lock_on_model_point=220, state=True)
    DisableCharacter(Characters.Malenia3)
    DisableAnimations(Characters.Malenia3)
    SetLockOnPoint(character=Characters.Malenia3, lock_on_model_point=220, state=True)
    DisableCharacter(Characters.Malenia4)
    DisableAnimations(Characters.Malenia4)
    SetLockOnPoint(character=Characters.Malenia4, lock_on_model_point=220, state=True)
    DisableCharacter(Characters.Malenia5)
    DisableAnimations(Characters.Malenia5)
    SetLockOnPoint(character=Characters.Malenia5, lock_on_model_point=220, state=True)
    DisableTreasure(asset=15001810)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=15000801)
    AddSpecialEffect(Characters.Malenia0, 5402)
    DisableAnimations(Characters.Malenia0)
    DisableGravity(Characters.Malenia0)
    SetDisplayMask(Characters.Malenia0, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.Malenia0, bit_index=12, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.Malenia0, bit_index=13, switch_type=OnOffChange.On)
    ForceAnimation(Characters.Malenia0, 30000)
    AND_1.Add(FlagEnabled(15002805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=15002800))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    EnableNetworkFlag(15000801)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=15000000,
            cutscene_flags=0,
            move_to_region=15002811,
            map_id=15000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(15000000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=13.069999694824219, y_angle=34.47999954223633)
    AddSpecialEffect(Characters.Malenia0, 5400)
    Move(Characters.Malenia0, destination=15002812, destination_type=CoordEntityType.Region, short_move=True)
    EnableGravity(Characters.Malenia0)
    EnableAnimations(Characters.Malenia0)
    SetDisplayMask(Characters.Malenia0, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.Malenia0, bit_index=12, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.Malenia0, bit_index=13, switch_type=OnOffChange.Off)
    DisableAsset(Assets.AEG260_526_3000)
    ForceAnimation(Characters.Malenia0, 3006)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(Characters.Malenia0, destination=15002814, destination_type=CoordEntityType.Region, short_move=True)
    DisableAsset(Assets.AEG260_526_3000)
    AND_2.Add(FlagEnabled(15002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=15002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(15005800)
    SetNetworkUpdateRate(15005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Malenia0, name=902120000)
    RemoveSpecialEffect(Characters.Malenia0, 16141)


@RestartOnRest(15002811)
def Event_15002811():
    """Event 15002811"""
    if FlagEnabled(15000800):
        return
    AND_1.Add(HealthValue(Characters.Malenia0) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.Malenia0, 18480))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Malenia0))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=15000010,
            cutscene_flags=0,
            move_to_region=15002815,
            map_id=15000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(15000010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(15002802)
    if PlayerInOwnWorld():
        ChangeCamera(normal_camera_id=2121, locked_camera_id=2121)
    Move(Characters.Malenia0, destination=15002816, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=-29.0, y_angle=68.80000305175781)
    EnableBossHealthBar(Characters.Malenia0, name=902120001)
    AddSpecialEffect(Characters.Malenia0, 18000)
    AddSpecialEffect(Characters.Malenia0, 18001)
    AddSpecialEffect(Characters.Malenia0, 18002)
    RemoveSpecialEffect(Characters.Malenia0, 18015)
    AddSpecialEffect(Characters.Malenia0, 18016)
    SetDisplayMask(Characters.Malenia0, bit_index=10, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.Malenia0, bit_index=11, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.Malenia0, bit_index=12, switch_type=OnOffChange.On)
    CreateNPCPart(Characters.Malenia0, npc_part_id=10, part_index=NPCPartType.Part1, part_health=99999)
    SetNPCPartEffects(
        Characters.Malenia0,
        npc_part_id=10,
        material_sfx_id=109,
        material_vfx_id=109,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    CreateNPCPart(Characters.Malenia0, npc_part_id=310, part_index=NPCPartType.WeakPoint, part_health=99999)
    SetNPCPartEffects(
        Characters.Malenia0,
        npc_part_id=310,
        material_sfx_id=110,
        material_vfx_id=110,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    AddSpecialEffect(Characters.Malenia0, 18400)
    AddSpecialEffect(Characters.Malenia1, 18400)
    DisableHealthBar(Characters.Malenia1)
    ForceAnimation(Characters.Malenia0, 20002)
    WaitFrames(frames=1)
    ReplanAI(Characters.Malenia0)
    Wait(3.200000047683716)
    DisableImmortality(Characters.Malenia0)
    if PlayerInOwnWorld():
        ChangeCamera(normal_camera_id=2120, locked_camera_id=2120)


@ContinueOnRest(15002820)
def Event_15002820(_, character: uint, animation_id: int, special_effect: int):
    """Event 15002820"""
    if FlagEnabled(15000800):
        return
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    AND_1.Add(FlagDisabled(15002803))
    AND_1.Add(CharacterHasSpecialEffect(Characters.Malenia0, special_effect))
    AND_2.Add(FlagEnabled(15002803))
    AND_2.Add(CharacterHasSpecialEffect(Characters.Malenia1, special_effect))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableCharacter(character)
    WaitFrames(frames=1)
    if FlagDisabled(15002803):
        Move(
            character,
            destination=Characters.Malenia0,
            destination_type=CoordEntityType.Character,
            model_point=228,
            copy_draw_parent=Characters.Malenia0,
        )
    else:
        Move(
            character,
            destination=Characters.Malenia1,
            destination_type=CoordEntityType.Character,
            model_point=228,
            copy_draw_parent=Characters.Malenia1,
        )
    ForceAnimation(character, animation_id)
    EnableAI(character)
    Wait(0.699999988079071)
    EnableAnimations(character)
    Wait(0.30000001192092896)
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5029))
    
    MAIN.Await(AND_5)
    
    Restart()


@ContinueOnRest(15002830)
def Event_15002830(_, special_effect: int, special_effect_1: int):
    """Event 15002830"""
    if FlagEnabled(15000800):
        return
    AND_1.Add(PlayerNotInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, special_effect_1))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        AddSpecialEffect(Characters.Malenia0, special_effect)
    Wait(0.20000000298023224)
    Restart()


@ContinueOnRest(15002840)
def Event_15002840(_, character: uint, character_1: uint, state: uchar):
    """Event 15002840"""
    if FlagEnabled(15000800):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 18037))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    AddSpecialEffect(character_1, 18401)
    WaitFrames(frames=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=228,
        copy_draw_parent=character_1,
    )
    ReplanAI(character)
    ReplanAI(character_1)
    Wait(0.699999988079071)
    EnableAnimations(character_1)
    RemoveSpecialEffect(character_1, 18401)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5029))
    
    MAIN.Await(AND_2)
    
    DisableCharacter(character)
    DisableAnimations(character)
    SetAbsoluteNetworkFlagState(15002803, state=state)
    Restart()


@ContinueOnRest(15002842)
def Event_15002842(_, character: uint, special_effect: int, special_effect_1: int):
    """Event 15002842"""
    if FlagEnabled(15000800):
        return
    AddSpecialEffect(character, special_effect)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_1.Add(FlagDisabled(15002803))
    AND_1.Add(CharacterHasSpecialEffect(Characters.Malenia0, special_effect_1))
    AND_2.Add(FlagEnabled(15002803))
    AND_2.Add(CharacterHasSpecialEffect(Characters.Malenia1, special_effect_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableCharacter(character)
    WaitFrames(frames=1)
    EnableAI(character)
    if FlagDisabled(15002803):
        Move(
            character,
            destination=Characters.Malenia0,
            destination_type=CoordEntityType.Character,
            model_point=228,
            copy_draw_parent=Characters.Malenia0,
        )
    else:
        Move(
            character,
            destination=Characters.Malenia1,
            destination_type=CoordEntityType.Character,
            model_point=228,
            copy_draw_parent=Characters.Malenia1,
        )
    ReplanAI(character)
    Wait(0.699999988079071)
    EnableAnimations(character)
    Wait(2.0)
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5029))
    
    MAIN.Await(AND_5)
    
    Restart()


@ContinueOnRest(15002848)
def Event_15002848(_, special_effect: int, locked_camera_id__normal_camera_id: int):
    """Event 15002848"""
    DisableNetworkSync()
    if FlagEnabled(15000800):
        return
    AND_2.Add(FlagEnabled(15002810))
    if PlayerInOwnWorld():
        AND_2.Add(FlagEnabled(15002805))
    else:
        AND_2.Add(FlagEnabled(15002806))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.Malenia0, special_effect))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.Malenia0, 18032))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(15000800))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(15000800):
        return
    ChangeCamera(normal_camera_id=2120, locked_camera_id=2120)
    AND_1.Add(FlagEnabled(15002810))
    AND_1.Add(CharacterHasSpecialEffect(Characters.Malenia0, special_effect))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.Malenia0, 18032))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(15000800))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(15000800):
        return
    ChangeCamera(
        normal_camera_id=locked_camera_id__normal_camera_id,
        locked_camera_id=locked_camera_id__normal_camera_id,
    )
    Restart()


@RestartOnRest(15002849)
def Event_15002849():
    """Event 15002849"""
    CommonFunc_9005800(
        0,
        flag=15000800,
        entity=Assets.AEG099_003_9000,
        region=15002800,
        flag_1=15002805,
        character=15005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=15000800,
        entity=Assets.AEG099_003_9000,
        region=15002800,
        flag_1=15002805,
        flag_2=15002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=15000800, asset=Assets.AEG099_003_9000, model_point=5, right=0)
    CommonFunc_9005822(
        0,
        flag=15002800,
        bgm_boss_conv_param_id=212000,
        flag_1=15002805,
        flag_2=15002806,
        right=0,
        flag_3=15002802,
        left=1,
        left_1=1,
    )


@RestartOnRest(15002850)
def Event_15002850():
    """Event 15002850"""
    if FlagEnabled(15000850):
        return
    
    MAIN.Await(HealthValue(Characters.Loretta) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Loretta, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Loretta))
    
    KillBossAndDisplayBanner(character=Characters.Loretta, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(15000850)
    EnableFlag(9119)
    if PlayerInOwnWorld():
        EnableFlag(61119)


@RestartOnRest(15002860)
def Event_15002860():
    """Event 15002860"""
    GotoIfFlagDisabled(Label.L0, flag=15000850)
    DisableCharacter(15005850)
    DisableAnimations(15005850)
    Kill(15005850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(15005850)
    ForceAnimation(Characters.Loretta, 30001)
    GotoIfFlagEnabled(Label.L1, flag=15000851)
    AddSpecialEffect(Characters.TalkDummy12, 9531)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=15002851))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Loretta, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(15000851)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(
        Characters.Loretta,
        destination=15002860,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.Loretta,
    )
    AND_2.Add(FlagEnabled(15002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=15002850))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(Characters.Loretta, 20011)
    ForceAnimation(Characters.Loretta, 3005)
    EnableAI(15005850)
    SetNetworkUpdateRate(15005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(Characters.TalkDummy12, 9532)
    Wait(2.0)
    EnableBossHealthBar(Characters.Loretta, name=903252000)


@RestartOnRest(15002861)
def Event_15002861():
    """Event 15002861"""
    if FlagEnabled(15000850):
        return
    AND_1.Add(HealthRatio(Characters.Loretta) <= 0.550000011920929)
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)


@RestartOnRest(15002899)
def Event_15002899():
    """Event 15002899"""
    CommonFunc_9005800(
        0,
        flag=15000850,
        entity=Assets.AEG099_003_9001,
        region=15002850,
        flag_1=15002855,
        character=15005850,
        action_button_id=10000,
        left=15000851,
        region_1=15002851,
    )
    CommonFunc_9005801(
        0,
        flag=15000850,
        entity=Assets.AEG099_003_9001,
        region=15002850,
        flag_1=15002855,
        flag_2=15002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=15000850, asset=Assets.AEG099_003_9001, model_point=3, right=15000851)
    CommonFunc_9005811(0, flag=15000850, asset=Assets.AEG099_003_9002, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=15000850,
        bgm_boss_conv_param_id=920200,
        flag_1=15002855,
        flag_2=15002856,
        right=0,
        flag_3=15002852,
        left=0,
        left_1=0,
    )


@ContinueOnRest(15000700)
def Event_15000700():
    """Event 15000700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(15000800):
        return
    if FlagEnabled(15002700):
        return
    
    MAIN.Await(FlagEnabled(15002805))
    
    SetCharacterTalkRange(character=Characters.Malenia0, distance=100.0)
    
    MAIN.Await(FlagEnabled(15002701))
    
    SetCharacterTalkRange(character=Characters.Malenia0, distance=17.0)


@ContinueOnRest(15000701)
def Event_15000701():
    """Event 15000701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(15000800):
        return
    if FlagEnabled(15002700):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(Characters.Malenia0) == 0)
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(Characters.Malenia0, True)
    OR_1.Add(TimeElapsed(seconds=100.0))
    OR_1.Add(FlagEnabled(15002701))
    
    MAIN.Await(OR_1)
    
    SetBackreadStateAlternate(Characters.Malenia0, False)


@RestartOnRest(15000702)
def Event_15000702(_, asset: uint, asset_1: uint):
    """Event 15000702"""
    DisableAsset(asset)
    DisableAsset(asset_1)
    GotoIfFlagEnabled(Label.L19, flag=9120)
    AND_1.Add(FlagEnabled(9120))
    AND_1.Add(FlagEnabled(9000))
    AwaitConditionTrue(AND_1)
    Wait(1.0)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableAsset(asset)
    EnableAsset(asset_1)
    EnableNetworkFlag(15009212)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(15000710)
def Event_15000710(_, character: uint):
    """Event 15000710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4180):
        DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4190)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4190))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

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
    
    MAIN.Await(FlagDisabled(4190))
    
    Restart()


@RestartOnRest(15000711)
def Event_15000711(_, character: uint):
    """Event 15000711"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4180):
        DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(4191))
    OR_1.Add(FlagEnabled(4192))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(Assets.AEG099_320_9000)
    OR_2.Add(FlagEnabled(4191))
    OR_2.Add(FlagEnabled(4192))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    EnableAsset(Assets.AEG099_320_9000)
    if FlagDisabled(4191):
        ForceAnimation(character, 90104)
        SetTeamType(character, TeamType.NoTeam)
        DisableAsset(Assets.AEG099_320_9000)
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
    AND_1.Add(FlagDisabled(4191))
    AND_1.Add(FlagDisabled(4192))
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(15000712)
def Event_15000712(_, asset: uint):
    """Event 15000712"""
    DisableAsset(asset)
    AwaitFlagEnabled(flag=4194)
    EnableAsset(asset)
    End()


@RestartOnRest(15000713)
def Event_15000713(_, entity: uint):
    """Event 15000713"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400324):
        return
    AND_2.Add(PlayerHasGood(8196))
    AND_2.Add(FlagDisabled(400324))
    AND_2.Add(FlagEnabled(15009212))
    AND_2.Add(ActionButtonParamActivated(action_button_id=6519, entity=entity))
    AwaitConditionTrue(AND_2)
    AwardItemLot(103240, host_only=False)
    RemoveGoodFromPlayer(item=8196, quantity=1)
    End()


@RestartOnRest(15000714)
def Event_15000714():
    """Event 15000714"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400323):
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(7611))
    AwaitConditionTrue(AND_2)
    AwardItemLot(103220, host_only=False)
    End()


@RestartOnRest(15000715)
def Event_15000715():
    """Event 15000715"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4190):
        return
    AND_1.Add(FlagEnabled(4190))
    AND_1.Add(FlagEnabled(15009206))
    OR_1.Add(EntityWithinDistance(entity=Assets.AEG099_060_9002, other_entity=20000, radius=5.0))
    OR_1.Add(EntityWithinDistance(entity=Assets.AEG099_060_9003, other_entity=20000, radius=12.0))
    AND_1.Add(OR_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(15009213)
    EnableNetworkFlag(4198)
    EnableNetworkFlag(4178)
    End()


@RestartOnRest(15000716)
def Event_15000716():
    """Event 15000716"""
    if FlagEnabled(15000398):
        return
    AwaitFlagEnabled(flag=15000398)
    EnableNetworkFlag(4198)
    End()

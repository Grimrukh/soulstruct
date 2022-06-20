"""
linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.emevd
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.darksouls3.events import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(13000009, obj=3001950, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13000003, obj=3001959, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13000005, obj=3001955, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13000008, obj=3001958, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RunCommonEvent(20005500, args=(13000800, 13000002, 3000952, 3001952))
    RunCommonEvent(20005500, args=(13000830, 13000001, 3000951, 3001951))
    RunCommonEvent(20005500, args=(13000890, 13000004, 3000954, 3001954))
    RunEvent(13000210)
    RunEvent(13000200)
    RunCommonEvent(20005780, args=(3001780, 2))
    RunEvent(13005350, slot=0, args=(3001890, 3))
    RunEvent(13005810)
    RunEvent(13005811)
    RunEvent(13005815)
    RunEvent(13005820)
    RunEvent(13005812)
    RunEvent(13005817)
    RunCommonEvent(20005840, args=(3001800,))
    RunCommonEvent(20005841, args=(3001800,))
    RunEvent(13005825, slot=0, args=(13000825, 13000800, 13000896, 13000890, 711))
    RunEvent(13005830)
    RunEvent(13005831)
    RunEvent(13005840)
    RunEvent(13005835)
    RunEvent(13005836)
    RunEvent(13005837)
    RunEvent(13005838)
    RunEvent(13005595)
    RunEvent(13005850)
    RunEvent(13005890)
    RunEvent(13005895)
    RunEvent(13005891)
    RunEvent(13005892)
    RunEvent(13005893)
    RunEvent(13005889)
    RunEvent(13005899)
    RunEvent(13005880)
    RunCommonEvent(20005840, args=(3001890,))
    RunCommonEvent(20005841, args=(3001890,))
    RunEvent(13005280, slot=0, args=(3001316, 830078))
    RunEvent(13005280, slot=1, args=(3001300, 830077))
    RunEvent(13005280, slot=2, args=(3001301, 830077))
    RunEvent(13005280, slot=3, args=(3001302, 830077))
    RunEvent(13005280, slot=4, args=(3001303, 830077))
    RunEvent(13005280, slot=5, args=(3001304, 830077))
    RunEvent(13005280, slot=6, args=(3001305, 830077))
    RunEvent(13005280, slot=7, args=(3001306, 830077))
    RunEvent(13005280, slot=8, args=(3001307, 830077))
    RunEvent(13005280, slot=9, args=(3001308, 830077))
    RunEvent(13005280, slot=10, args=(3001309, 830077))
    RunEvent(13005280, slot=11, args=(3001310, 830077))
    RunEvent(13005280, slot=12, args=(3001311, 830077))
    RunEvent(13005280, slot=13, args=(3001312, 830077))
    RunEvent(13005280, slot=14, args=(3001313, 830077))
    RunEvent(13005280, slot=15, args=(3001314, 830077))
    RunEvent(13005280, slot=16, args=(3001315, 830077))
    RunEvent(13005480)
    RunEvent(13005485)
    RunEvent(13005486)
    RunEvent(13005487)
    RunEvent(13005488)
    RunEvent(13005489)
    RunEvent(13005481)
    RunEvent(13005490)
    RunEvent(13005493)
    RunEvent(13005494)
    RunCommonEvent(20005415, args=(13001500, 3000610, 3000611, 702, 1702, 3002490, 13005501, 13005502))
    RunCommonEvent(20005417, args=(13001501, 3000612, 3000613, 702, 1702, 0, 13005503, 13005504, 3002365))
    RunEvent(13005510, slot=0, args=(3000610, 3000502, 20000, 0.20000000298023224), arg_types="iiif")
    RunEvent(13005510, slot=1, args=(3000610, 3000509, 20001, 0.0), arg_types="iiif")
    RunEvent(13005510, slot=2, args=(3000610, 3000505, 20002, 0.699999988079071), arg_types="iiif")
    RunEvent(13005510, slot=3, args=(3000610, 3000507, 20000, 1.0), arg_types="iiif")
    RunEvent(13005510, slot=4, args=(3000612, 3000423, 20000, 0.0), arg_types="iiif")
    RunEvent(13005510, slot=5, args=(3000612, 3000421, 20000, 0.20000000298023224), arg_types="iiif")
    RunEvent(13005510, slot=6, args=(3000612, 3000410, 20001, 0.4000000059604645), arg_types="iiif")
    RunEvent(13005510, slot=7, args=(3000612, 3000411, 20002, 0.6000000238418579), arg_types="iiif")
    RunEvent(
        13005200,
        slot=0,
        args=(3000451, 20001, 0.8999999761581421, 0, 3000450, 3000601, 3000607, 3000452),
        arg_types="iifiiiii",
    )
    RunEvent(
        13005200,
        slot=1,
        args=(3000450, 20000, 0.20000000298023224, 3000451, 0, 3000601, 3000607, 3000452),
        arg_types="iifiiiii",
    )
    RunEvent(
        13005200,
        slot=2,
        args=(3000601, 20001, 0.4000000059604645, 3000451, 3000450, 0, 3000607, 3000452),
        arg_types="iifiiiii",
    )
    RunEvent(13005200, slot=3, args=(3000607, 20001, 0.0, 3000451, 3000450, 3000601, 0, 3000452), arg_types="iifiiiii")
    RunEvent(
        13005200,
        slot=4,
        args=(3000452, 20002, 0.699999988079071, 3000451, 3000450, 3000601, 3000607, 0),
        arg_types="iifiiiii",
    )
    RunEvent(13005210, slot=0, args=(3000604, 20001, 0.5, 3000600, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005210, slot=1, args=(3000600, 20000, 0.699999988079071, 3000604, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005210, slot=2, args=(3000484, 20002, 0.5, 3000454, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005210, slot=3, args=(3000454, 20001, 0.699999988079071, 3000484, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005210, slot=4, args=(3000605, 20002, 0.699999988079071, 0, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005220, slot=1, args=(3000457, 20001, 0.30000001192092896, 3000456, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005220, slot=2, args=(3000456, 20000, 0.10000000149011612, 3000457, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005230, slot=0, args=(3000464, 20002, 0.800000011920929, 3000463, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005230, slot=1, args=(3000463, 20001, 0.30000001192092896, 3000464, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005240, slot=0, args=(3000592, 20000, 0.0, 3000596, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005240, slot=1, args=(3000596, 20002, 0.0, 3000592, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005240, slot=2, args=(3000533, 20001, 0.0, 0, 0, 0, 0, 0), arg_types="iifiiiii")
    RunEvent(13005025)
    RunEvent(13005530)
    RunEvent(13005535)
    RunCommonEvent(20005119, args=(3000230, 3002350, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3000237, 3002222, 3002225, 0, 0, 0, 0, 0))
    RunCommonEvent(20005350, args=(3000238, 12800420, 53010980))
    RunCommonEvent(20005119, args=(3000254, 3002226, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005110, args=(3000255, 3002360))
    RunCommonEvent(20005224, args=(3000280, 701, 1701))
    RunCommonEvent(20005224, args=(3000281, 701, 1701))
    RunCommonEvent(20005119, args=(3000300, 3002226, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005220, args=(3000350, 702, 1702))
    RunCommonEvent(20005224, args=(3000351, 702, 1702))
    RunCommonEvent(20005350, args=(3000352, 11901120, 53010955))
    RunCommonEvent(20005202, args=(3000360, 701, 1701, 3002655))
    RunCommonEvent(20005202, args=(3000361, 701, 1701, 3002655))
    RunCommonEvent(20005210, args=(3000409, 706, 1706, 1077936128))
    RunCommonEvent(20005290, args=(3000410, 701, 1701))
    RunCommonEvent(20005290, args=(3000411, 702, 1702))
    RunCommonEvent(20005200, args=(3000412, 705, 1705, 3002390))
    RunCommonEvent(20005110, args=(3000418, 3002431))
    RunCommonEvent(20005110, args=(3000419, 3002391))
    RunCommonEvent(20005110, args=(3000420, 3002223))
    RunCommonEvent(20005290, args=(3000421, 700, 1700))
    RunCommonEvent(20005290, args=(3000423, 700, 1700))
    RunCommonEvent(20005110, args=(3000424, 3002224))
    RunCommonEvent(20005110, args=(3000425, 3002224))
    RunCommonEvent(20005290, args=(3000426, 705, 1705))
    RunCommonEvent(20005110, args=(3000427, 3002341))
    RunCommonEvent(20005220, args=(3000430, 703, 1703))
    RunCommonEvent(20005122, args=(3000431, 3003, 1086324736))
    RunCommonEvent(20005220, args=(3000432, 706, 1706))
    RunCommonEvent(20005210, args=(3000432, 706, 1706, 1084227584))
    RunCommonEvent(20005213, args=(3000433, 703, 1703, 1077936128, 3002650))
    RunCommonEvent(20005111, args=(3000434, 3011, 3002380))
    RunCommonEvent(20005213, args=(3000435, 703, 1703, 1077936128, 3002425))
    RunCommonEvent(20005213, args=(3000436, 706, 1706, 1077936128, 3002425))
    RunCommonEvent(20005119, args=(3000440, 3002226, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005210, args=(3000441, 703, 1703, 1077936128))
    RunCommonEvent(20005119, args=(3000442, 3002226, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005290, args=(3000450, 700, 1700))
    RunCommonEvent(20005290, args=(3000451, 701, 1701))
    RunCommonEvent(20005290, args=(3000452, 702, 1702))
    RunCommonEvent(20005290, args=(3000454, 701, 1701))
    RunCommonEvent(20005290, args=(3000456, 700, 1700))
    RunCommonEvent(20005290, args=(3000457, 701, 1701))
    RunCommonEvent(20005110, args=(3000443, 3002340))
    RunCommonEvent(20005290, args=(3000463, 701, 1701))
    RunCommonEvent(20005290, args=(3000464, 702, 1702))
    RunCommonEvent(20005192, args=(3000471, 3002441))
    RunCommonEvent(20005290, args=(3000473, 700, 1700))
    RunCommonEvent(20005205, args=(3000477, 710, 1710, 3002361, 1066192077))
    RunCommonEvent(20005205, args=(3000478, 710, 1710, 3002361, 1065353216))
    RunCommonEvent(20005119, args=(3000482, 3002226, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005110, args=(3000483, 3002340))
    RunCommonEvent(20005290, args=(3000484, 702, 1702))
    RunCommonEvent(20005290, args=(3000486, 701, 1701))
    RunCommonEvent(20005290, args=(3000487, 702, 1702))
    RunCommonEvent(20005205, args=(3000490, 710, 1710, 3002361, 1061997773))
    RunCommonEvent(20005205, args=(3000492, 710, 1710, 3002361, 1053609165))
    RunCommonEvent(20005220, args=(3000494, 703, 1703))
    RunCommonEvent(20005220, args=(3000495, 703, 1703))
    RunCommonEvent(20005210, args=(3000496, 710, 1710, 1083179008))
    RunCommonEvent(20005290, args=(3000500, 703, 1703))
    RunCommonEvent(20005290, args=(3000502, 700, 1700))
    RunCommonEvent(20005290, args=(3000504, 702, 1702))
    RunCommonEvent(20005290, args=(3000505, 702, 1702))
    RunCommonEvent(20005290, args=(3000507, 700, 1700))
    RunCommonEvent(20005290, args=(3000509, 701, 1701))
    RunCommonEvent(20005122, args=(3000511, 3000, 1084227584))
    RunCommonEvent(20005210, args=(3000520, 706, 1706, 1085276160))
    RunCommonEvent(20005202, args=(3000522, 710, 1710, 3002430))
    RunCommonEvent(20005111, args=(3000523, 3003, 3002220))
    RunCommonEvent(20005210, args=(3000525, 706, 1706, 1084227584))
    RunCommonEvent(20005210, args=(3000526, 710, 1710, 1084227584))
    RunCommonEvent(20005290, args=(3000533, 701, 1701))
    RunCommonEvent(20005119, args=(3000537, 3002480, 3002350, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3000538, 3002480, 3002350, 0, 0, 0, 0, 0))
    RunCommonEvent(20005210, args=(3000539, 706, 1706, 1077936128))
    RunCommonEvent(20005210, args=(3000540, 706, 1706, 1077936128))
    RunCommonEvent(20005213, args=(3000545, 703, 1703, 1077936128, 3002362))
    RunCommonEvent(20005290, args=(3000551, 703, 1703))
    RunCommonEvent(20005290, args=(3000560, 703, 1703))
    RunCommonEvent(20005214, args=(3000568, 710, 1710, 1089470464))
    RunCommonEvent(20005221, args=(3000570, 703, 1703, 1084227584))
    RunCommonEvent(20005221, args=(3000571, 705, 1705, 1084227584))
    RunCommonEvent(20005221, args=(3000572, 706, 1706, 1084227584))
    RunCommonEvent(20005111, args=(3000579, 3000, 3002245))
    RunCommonEvent(20005202, args=(3000580, 710, 1710, 3002246))
    RunCommonEvent(20005290, args=(3000592, 700, 1700))
    RunCommonEvent(20005290, args=(3000596, 702, 1702))
    RunCommonEvent(20005290, args=(3000600, 700, 1700))
    RunCommonEvent(20005290, args=(3000601, 701, 1701))
    RunCommonEvent(20005290, args=(3000604, 701, 1701))
    RunCommonEvent(20005290, args=(3000605, 702, 1702))
    RunCommonEvent(20005290, args=(3000607, 701, 1701))
    RunCommonEvent(20005119, args=(3000615, 3002560, 3002561, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3000616, 3002560, 3002561, 0, 0, 0, 0, 0))
    RunCommonEvent(20005400, args=(3000620,))
    RunCommonEvent(20000343, args=(13000358, 3000620, 53000960))
    RunCommonEvent(20005341, args=(13000359, 3000630, 21500000))
    RunCommonEvent(20005110, args=(3000652, 3002290))
    RunCommonEvent(20005110, args=(3000660, 3002260))
    RunCommonEvent(20005110, args=(3000661, 3002260))
    RunCommonEvent(20005110, args=(3005450, 3002420))
    RunCommonEvent(20005192, args=(3005470, 3002621))
    RunCommonEvent(20005410, args=(3000561, 3005))
    RunCommonEvent(20005411, args=(3000561, 3000560, 703, 1703, 1056964608))
    RunCommonEvent(20005411, args=(3000561, 3000407, 706, 1706, 1067030938))
    RunCommonEvent(20005411, args=(3000561, 3000408, 703, 1703, 1053609165))
    RunCommonEvent(20005411, args=(3000561, 3000428, 706, 1706, 0))
    RunCommonEvent(20005410, args=(3000443, 3005))
    RunCommonEvent(20005411, args=(3000443, 3000444, 705, 1705, 0))
    RunCommonEvent(20005411, args=(3000443, 3000426, 705, 1705, 1053609165))
    RunCommonEvent(20005410, args=(3000400, 3005))
    RunCommonEvent(20005411, args=(3000400, 3000401, 703, 1703, 1076677837))
    RunCommonEvent(20005411, args=(3000400, 3000402, 705, 1705, 1069547520))
    RunCommonEvent(20005411, args=(3000400, 3000403, 706, 1706, 1065353216))
    RunCommonEvent(20005411, args=(3000400, 3000405, 703, 1703, 1074161254))
    RunCommonEvent(20005411, args=(3000400, 3000406, 703, 1703, 1075838976))
    RunEvent(13000380, slot=0, args=(3000660, 60940, 6780))
    RunCommonEvent(20005340, args=(13000381, 3000661))
    RunCommonEvent(20005701, args=(13000800, 13005700, 13005701, 3000190, 3002780, 13005392))
    RunEvent(
        13005826,
        slot=0,
        args=(13005700, 13005805, 13005885, 3000190, 3002800, 3002896, 3002820, 3002870, 13000801, 13000896),
    )
    RunCommonEvent(20005720, args=(13005700, 13005701, 13000800, 3000190))
    RunCommonEvent(20005714, args=(13005700, 13005805, 3000190, 3002829, 13000801))
    RunEvent(13005390)
    RunEvent(13005391)
    RunCommonEvent(20005701, args=(13000800, 13005705, 13005706, 3000191, 3002781, 9500))
    RunEvent(
        13005826,
        slot=1,
        args=(13005705, 13005805, 13005885, 3000191, 3002800, 3002896, 3002820, 3002870, 13000801, 13000896),
    )
    RunCommonEvent(20005720, args=(13005705, 13005706, 13000800, 3000191))
    RunCommonEvent(20005714, args=(13005705, 13005805, 3000191, 3002829, 13000801))
    RunCommonEvent(20005701, args=(13000830, 13005710, 13005711, 3000192, 3002783, 70000007))
    RunCommonEvent(20005710, args=(13005710, 13005855, 3000192, 3002831, 3002840))
    RunCommonEvent(20005720, args=(13005710, 13005711, 13000830, 3000192))
    RunCommonEvent(20005520, args=(13000350, 3001350, 3004350))
    RunCommonEvent(20005520, args=(13000351, 3001351, 3004351))
    RunCommonEvent(20005520, args=(13000352, 3001352, 3004352))
    RunCommonEvent(20005520, args=(13000353, 3001353, 3004353))
    RunCommonEvent(20005520, args=(13000354, 3001354, 3004354))
    RunCommonEvent(20005521, args=(13000420, 13005420, 3001250, 3001251, 3000170))
    RunCommonEvent(20005525, args=(53000650, 3000650, 3001260, 61))
    RunCommonEvent(20005526, args=(53000950, 3000950, 3001900, 61, 9480))
    RunCommonEvent(20005620, args=(13000300, 13000301, 3001200, 3001201, 3001202, 13001300))
    RunCommonEvent(20005624, args=(13000310, 13000311, 3001210, 3001211, 3001212, 13001310))
    RunCommonEvent(20005620, args=(13000320, 13000321, 3001220, 3001221, 3001222, 13001320))
    RunCommonEvent(20005622, args=(13000330, 13000331, 3001230, 3001231, 3001232, 13001330))
    RunCommonEvent(20005650, args=(13000990, 3001550))
    RunEvent(13005440)
    RunEvent(13005550)
    RunCommonEvent(20005610, args=(13000450, 3002460, 3002461))
    RunCommonEvent(20005611, args=(13000450, 3003253, 3001410, 300310))
    DisableObjectActivation(3001410, obj_act_id=-1, event_layers=[0])
    RunCommonEvent(20005610, args=(13000455, 3002460, 3002461))
    RunCommonEvent(20005611, args=(13000455, 3003254, 3001414, 300310))
    DisableObjectActivation(3001414, obj_act_id=-1, event_layers=[9])
    RunCommonEvent(20005610, args=(13000451, 3002450, 3002451))
    RunCommonEvent(20005611, args=(13000451, 3003302, 3001400, 300320))
    RunCommonEvent(20005610, args=(13000452, 3002471, 3002470))
    RunCommonEvent(20005611, args=(13000452, 3003304, 3001412, 300310))
    RunCommonEvent(20005611, args=(13000453, 3003303, 3001411, 300312))
    RunCommonEvent(20005613, args=(13000405, 3003309, 3001413, 4294967295, 10010861))
    RunCommonEvent(20005613, args=(13000406, 3003310, 3001415, 300313, 10010870))
    RunEvent(13005540)
    DeleteObjectVFX(3001885, erase_root=True)
    DeleteObjectVFX(3001886, erase_root=True)
    DeleteObjectVFX(3001887, erase_root=True)
    DeleteObjectVFX(3001888, erase_root=True)
    CreateObjectVFX(800023, obj=3001885, model_point=200)
    CreateObjectVFX(800023, obj=3001886, model_point=200)
    CreateObjectVFX(800023, obj=3001887, model_point=200)
    CreateObjectVFX(800023, obj=3001888, model_point=200)
    RunCommonEvent(20005530, args=(13005561, 3001619))
    RunCommonEvent(20005530, args=(13005562, 3001620))
    RunCommonEvent(20005530, args=(13005563, 3001621))
    RunCommonEvent(20005530, args=(13005564, 3001622))
    RunCommonEvent(20005530, args=(13005565, 3001623))
    RunCommonEvent(20005530, args=(13005566, 3001624))
    RunCommonEvent(20005530, args=(13005567, 3001625))
    RunCommonEvent(20005530, args=(13005568, 3001626))
    RunCommonEvent(20005530, args=(13005569, 3001627))
    RunCommonEvent(20005530, args=(13005570, 3001628))
    RunCommonEvent(20005530, args=(13005571, 3001629))
    RunCommonEvent(20005530, args=(13005572, 3001630))
    RunCommonEvent(20005530, args=(13005573, 3001631))
    RunCommonEvent(20005530, args=(13005574, 3001610))
    RunCommonEvent(20005530, args=(13005575, 3001611))
    RunCommonEvent(20005530, args=(13005576, 3001612))
    RunCommonEvent(20005530, args=(13005577, 3001613))
    RunCommonEvent(20005530, args=(13005578, 3001614))
    RunCommonEvent(20005530, args=(13005579, 3001632))
    RunCommonEvent(20005530, args=(13005580, 3001633))
    RunCommonEvent(20005530, args=(13005581, 3001634))
    RunCommonEvent(20005530, args=(13005582, 3001635))
    RunCommonEvent(20005530, args=(13005583, 3001636))
    RunCommonEvent(20005530, args=(13005584, 3001637))
    RunCommonEvent(20005530, args=(13005585, 3001638))
    RunCommonEvent(20005530, args=(13005586, 3001639))
    RunCommonEvent(20005530, args=(13005587, 3001640))
    RunCommonEvent(20005530, args=(13005588, 3001641))
    RunCommonEvent(20005530, args=(13005360, 3001600))
    RunCommonEvent(20005530, args=(13005361, 3001601))
    RunCommonEvent(20005530, args=(13005362, 3001602))
    RunCommonEvent(20005530, args=(13005363, 3001603))
    RunCommonEvent(20005530, args=(13005364, 3001604))
    RunCommonEvent(20005530, args=(13005365, 3001605))
    RunCommonEvent(20005530, args=(13005366, 3001606))
    RunCommonEvent(20005530, args=(13005367, 3001607))
    RunCommonEvent(20005540, args=(13005630, 3001510, 200, 5110, 1056964608, 0, 1065353216))
    RunCommonEvent(20005540, args=(13005631, 3001511, 200, 5110, 1056964608, 0, 1065353216))
    RunCommonEvent(20005540, args=(13005632, 3001512, 200, 5110, 1056964608, 0, 1065353216))
    RunCommonEvent(20005540, args=(13005633, 3001513, 200, 5110, 1056964608, 0, 1065353216))
    RegisterLadder(start_climbing_flag=13000250, stop_climbing_flag=13000251, obj=3001080)
    RegisterLadder(start_climbing_flag=13000252, stop_climbing_flag=13000253, obj=3001081)
    RegisterLadder(start_climbing_flag=13000254, stop_climbing_flag=13000255, obj=3001082)
    RegisterLadder(start_climbing_flag=13000256, stop_climbing_flag=13000257, obj=3001083)
    RegisterLadder(start_climbing_flag=13000258, stop_climbing_flag=13000259, obj=3001084)
    RegisterLadder(start_climbing_flag=13000260, stop_climbing_flag=13000261, obj=3001085)
    RegisterLadder(start_climbing_flag=13000262, stop_climbing_flag=13000263, obj=3001086)
    RunEvent(13000230)
    RunCommonEvent(20005523, args=(3001270, 1))
    RunCommonEvent(20005523, args=(3001271, 1))
    RunCommonEvent(20005523, args=(3001272, 2))
    RunCommonEvent(20005523, args=(3001273, 2))
    RunCommonEvent(20006003, args=(3000700, 73000132, 1215, 1200, 1201, 1200, 1214))
    RunCommonEvent(20006002, args=(3000700, 1218, 1215, 1219))
    RunCommonEvent(20006000, args=(3000700, 1216, 1217, 73000130, 1059481190, 1215, 1219, 0))
    RunCommonEvent(20006001, args=(3000700, 1216, 1217, 73000130, 3))
    RunEvent(13005601, slot=0, args=(73000181,))
    RunEvent(13005602, slot=0, args=(3000705, 73000180))
    RunEvent(13005603, slot=0, args=(3000705,))
    RunCommonEvent(20006002, args=(3000705, 1438, 1435, 1439))
    RunEvent(13005604)
    RunEvent(13005560)
    RunEvent(13000360)
    RunEvent(13000901, slot=0, args=(3001900,))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(13000410)
    RunEvent(13005861)
    RunEvent(13005590)
    SetMultiplayerBuffs_NonBoss(3000850, state=True)
    RunEvent(13005620, slot=0, args=(3000700,))
    RunEvent(13005600, slot=0, args=(3000705, 3001875, 3001876))
    RunEvent(13005640, slot=0, args=(3000830,))
    DisableSoundEvent(3002805)
    DisableSoundEvent(3002806)
    DisableSoundEvent(3002835)
    DisableSoundEvent(3002836)
    DisableSoundEvent(3002898)
    DisableSoundEvent(3002899)


def Event13000200():
    """ 13000200: Event 13000200 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterOutsideRegion(0, PLAYER, region=3002550)
    EnableFlag(13000201)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13000201)


def Event13000210():
    """ 13000210: Event 13000210 """
    EndIfFlagOn(13000009)
    IfFlagOn(0, 13000009)
    DisableFlag(13000000)


def Event13000230():
    """ 13000230: Event 13000230 """
    EndIfThisEventSlotOn()
    DisableSoapstoneMessage(3002280)
    IfPlayerHasGood(0, 2117, including_box=True)
    EnableSoapstoneMessage(3002280)


def Event13000360():
    """ 13000360: Event 13000360 """
    EndIfPlayerNotInOwnWorld()
    DisableNetworkSync()
    EndIfThisEventSlotOn()
    IfFlagOn(0, 711)
    ForceAnimation(PLAYER, 63010)
    CreateTemporaryVFX(30300, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=245)
    CreateObjectVFX(830095, obj=3001705, model_point=90)
    EnableFlag(13000360)
    Wait(10.0)
    DeleteObjectVFX(3001705, erase_root=True)


def Event13000380(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13000380: Event 13000380 """
    EndIfPlayerNotInOwnWorld()
    IfThisEventSlotOn(1)
    IfFlagOn(1, arg_8_11)
    EndIfConditionTrue(1)
    IfCharacterDead(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    End()


def Event13000410():
    """ 13000410: Event 13000410 """
    EndIfThisEventSlotOn()
    EnableFlag(13000300)
    EnableFlag(13000310)
    End()


@RestartOnRest
def Event13005025():
    """ 13005025: Event 13005025 """
    EndIfThisEventSlotOn()
    ForceAnimation(3000404, 703, loop=True)
    DisableAI(3000404)
    IfObjectDestroyed(-1, 3001250)
    IfAttacked(-2, 3000404, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    IfObjectDestroyed(-1, 3001250)
    IfAttacked(-2, 3000404, attacker=PLAYER)
    SkipLinesIfConditionTrue(2, -2)
    ForceAnimation(3000404, 1703, wait_for_completion=True)
    EnableAI(3000404)


@RestartOnRest
def Event13005200(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: float,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 13005200: Event 13005200 """
    EndIfThisEventSlotOn()
    Wait(1.0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_12_15, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_16_19, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_20_23, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_24_27, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_28_31, attacker=PLAYER)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=1.0)
    IfHasAIStatus(2, 3000427, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, 3000427, arg_0_3, radius=3.5)
    IfHasAIStatus(3, 3000443, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(3, 3000443, arg_0_3, radius=3.5)
    IfHasAIStatus(4, 3000426, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(4, 3000426, arg_0_3, radius=3.5)
    IfHasAIStatus(5, 3000483, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(5, 3000483, arg_0_3, radius=3.5)
    IfHasAIStatus(
        6,
        3005500,
        ai_status=AIStatusType.Battle,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=1.0,
    )
    IfEntityWithinDistance(6, PLAYER, arg_0_3, radius=3.5)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    Wait(arg_8_11)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=arg_0_3, special_effect=5450)
    ForceAnimation(arg_0_3, arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13005210(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: float,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 13005210: Event 13005210 """
    EndIfThisEventSlotOn()
    Wait(1.0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_12_15, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_16_19, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_20_23, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_24_27, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_28_31, attacker=PLAYER)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=1.0)
    IfHasAIStatus(2, 3000427, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, 3000427, arg_0_3, radius=3.5)
    IfHasAIStatus(3, 3000443, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(3, 3000443, arg_0_3, radius=3.5)
    IfHasAIStatus(4, 3000426, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(4, 3000426, arg_0_3, radius=3.5)
    IfHasAIStatus(5, 3000483, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(5, 3000483, arg_0_3, radius=3.5)
    IfHasAIStatus(6, 3005500, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(6, PLAYER, arg_0_3, radius=3.5)
    IfHasTAEEvent(7, 3000443, tae_event_id=20)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(0, input_condition=-2)
    Wait(arg_8_11)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=arg_0_3, special_effect=5450)
    ForceAnimation(arg_0_3, arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13005220(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: float,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 13005220: Event 13005220 """
    EndIfThisEventSlotOn()
    Wait(1.0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_12_15, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_16_19, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_20_23, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_24_27, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_28_31, attacker=PLAYER)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=1.0)
    IfHasAIStatus(2, 3000427, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, 3000427, arg_0_3, radius=3.5)
    IfHasAIStatus(3, 3000443, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(3, 3000443, arg_0_3, radius=3.5)
    IfHasAIStatus(4, 3000426, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(4, 3000426, arg_0_3, radius=3.5)
    IfHasAIStatus(5, 3000483, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(5, 3000483, arg_0_3, radius=3.5)
    IfHasAIStatus(6, 3000561, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(6, 3000561, arg_0_3, radius=3.5)
    IfHasAIStatus(7, 3000408, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(7, 3000408, arg_0_3, radius=3.5)
    IfHasAIStatus(8, 3000560, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(8, 3000560, arg_0_3, radius=3.5)
    IfHasAIStatus(9, 3000579, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(9, 3000579, arg_0_3, radius=3.5)
    IfHasAIStatus(10, 3000428, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(10, 3000428, arg_0_3, radius=3.5)
    IfHasAIStatus(
        11,
        3005501,
        ai_status=AIStatusType.Battle,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=1.0,
    )
    IfEntityWithinDistance(11, PLAYER, arg_0_3, radius=3.5)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(-2, input_condition=8)
    IfConditionTrue(-2, input_condition=9)
    IfConditionTrue(-2, input_condition=10)
    IfConditionTrue(-2, input_condition=11)
    IfConditionTrue(0, input_condition=-2)
    Wait(arg_8_11)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=arg_0_3, special_effect=5450)
    ForceAnimation(arg_0_3, arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13005230(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: float,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 13005230: Event 13005230 """
    EndIfThisEventSlotOn()
    Wait(1.0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_12_15, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_16_19, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_20_23, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_24_27, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_28_31, attacker=PLAYER)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=1.0)
    IfHasAIStatus(2, 3000418, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, 3000418, arg_0_3, radius=3.5)
    IfHasAIStatus(3, 3000522, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(3, 3000522, arg_0_3, radius=3.5)
    IfHasAIStatus(4, 3000471, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(4, 3000471, arg_0_3, radius=3.5)
    IfHasAIStatus(5, 3000494, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(5, 3000494, arg_0_3, radius=3.5)
    IfHasAIStatus(6, 3000488, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(6, 3000488, arg_0_3, radius=3.5)
    IfHasAIStatus(7, 3000230, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(7, 3000230, arg_0_3, radius=3.5)
    IfHasAIStatus(
        8,
        3005502,
        ai_status=AIStatusType.Battle,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=1.0,
    )
    IfEntityWithinDistance(8, PLAYER, arg_0_3, radius=3.5)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(-2, input_condition=8)
    IfConditionTrue(0, input_condition=-2)
    Wait(arg_8_11)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=arg_0_3, special_effect=5450)
    ForceAnimation(arg_0_3, arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13005240(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: float,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 13005240: Event 13005240 """
    EndIfThisEventSlotOn()
    Wait(1.0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_12_15, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_16_19, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_20_23, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_24_27, attacker=PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=arg_28_31, attacker=PLAYER)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=1.0)
    IfHasAIStatus(2, 3000255, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, 3000255, arg_0_3, radius=3.5)
    IfHasAIStatus(3, 3000520, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(3, 3000520, arg_0_3, radius=3.5)
    IfHasAIStatus(4, 3000253, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(4, 3000253, arg_0_3, radius=3.5)
    IfHasAIStatus(5, 3000242, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(5, 3000242, arg_0_3, radius=3.5)
    IfHasAIStatus(6, 3000245, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(6, 3000245, arg_0_3, radius=3.5)
    IfHasAIStatus(
        7,
        3005503,
        ai_status=AIStatusType.Battle,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=1.0,
    )
    IfEntityWithinDistance(7, PLAYER, arg_0_3, radius=3.5)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(0, input_condition=-2)
    Wait(arg_8_11)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=arg_0_3, special_effect=5450)
    ForceAnimation(arg_0_3, arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    ReplanAI(arg_0_3)


def Event13005280(_, arg_0_3: int, arg_4_7: int):
    """ 13005280: Event 13005280 """
    IfObjectBurnState(1, obj=arg_0_3, comparison_type=ComparisonType.GreaterThan, state=False)
    IfFlagOn(1, 13000890)
    IfConditionTrue(0, input_condition=1)
    CreateTemporaryVFX(arg_4_7, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object, model_point=200)


@RestartOnRest
def Event13005350(_, arg_0_3: int, arg_4_7: int):
    """ 13005350: Event 13005350 """
    DisableNetworkSync()
    IfFlagOn(0, 13000890)
    DisableObject(arg_0_3)
    DeleteObjectVFX(arg_0_3, erase_root=True)
    IfTryingToJoinSession(-1)
    IfTryingToCreateSession(-1)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(arg_0_3)
    CreateObjectVFX(arg_4_7, obj=arg_0_3, model_point=101)
    IfTryingToJoinSession(-2)
    IfTryingToCreateSession(-2)
    IfConditionFalse(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event13005390():
    """ 13005390: Event 13005390 """
    EndIfFlagOn(13000800)
    IfPlayerHasGood(1, 2117, including_box=True)
    EndIfConditionTrue(1)
    EnableFlag(13005392)
    IfPlayerHasGood(0, 2117, including_box=True)
    DisableFlag(13005392)


@RestartOnRest
def Event13005391():
    """ 13005391: Event 13005391 """
    EndIfFlagOn(13000800)
    IfPlayerHasGood(1, 2117, including_box=True)
    EndIfConditionTrue(1)
    IfPlayerHasGood(2, 2117, including_box=True)
    IfFlagOn(2, 13005700)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(3000190, 91030)
    Wait(2.0)
    SendNPCSummonHome(3000190)


@RestartOnRest
def Event13005480():
    """ 13005480: Event 13005480 """
    DisableCharacter(3000850)
    DisableGravity(3000850)
    DisableAI(3000850)
    SetLockOnPoint(3000850, lock_on_model_point=220, state=False)
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    GotoIfFlagOff(Label.L0, 13000480)
    EnableCharacter(3000850)
    Move(3000850, destination=3002600, destination_type=CoordEntityType.Region, short_move=True)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableImmortality(3000850)
    EndIfThisEventSlotOn()
    CancelSpecialEffect(3000850, 11000)
    AddSpecialEffect(3000850, 11004)
    ForceAnimation(3000850, 30002, skip_transition=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3002620)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfFlagOn(3, 13000480)
    IfFlagOn(4, 13000481)
    IfFlagOn(5, 9420)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=5)
    Move(3000850, destination=3002600, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3000850, 20003, skip_transition=True)
    EnableFlag(13000480)
    EnableImmortality(3000850)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(3000850)
    DisableGravity(3000850)
    DisableAI(3000850)
    SetLockOnPoint(3000850, lock_on_model_point=220, state=False)


@RestartOnRest
def Event13005481():
    """ 13005481: Event 13005481 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfHealthLessThanOrEqual(1, 3000850, 0.20000000298023224)
    IfFlagOn(2, 9420)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AwardItemLot(31410000, host_only=False)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3000850, 20007, wait_for_completion=True, skip_transition=True)
    DisableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    EnableFlag(13000481)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Never)


@RestartOnRest
def Event13005485():
    """ 13005485: Event 13005485 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    GotoIfFlagOn(Label.L0, 13000480)
    EndIfThisEventSlotOn()
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=3002621)
    IfCharacterHasSpecialEffect(2, 3000850, 11000)
    IfCharacterHasSpecialEffect(2, 3000850, 11001)
    IfConditionTrue(3, input_condition=-1)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    CancelSpecialEffect(3000850, 11000)
    ForceAnimation(3000850, 20001, skip_transition=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(3000850, 11000)
    ForceAnimation(3000850, 30002, skip_transition=True)
    End()


@RestartOnRest
def Event13005486():
    """ 13005486: Event 13005486 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=3002617)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(3000850, 11003)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event13005487():
    """ 13005487: Event 13005487 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=3002610)
    IfCharacterInsideRegion(-2, PLAYER, region=3002611)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(3000850, 11004)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event13005488():
    """ 13005488: Event 13005488 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=3002615)
    IfCharacterInsideRegion(-2, PLAYER, region=3002616)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(3000850, 11004)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event13005489():
    """ 13005489: Event 13005489 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=3002630)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(3000850, 11005)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event13005490():
    """ 13005490: Event 13005490 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=3002640)
    IfCharacterInsideRegion(-2, PLAYER, region=3002642)
    IfCharacterInsideRegion(-3, PLAYER, region=3002641)
    IfCharacterInsideRegion(-3, PLAYER, region=3002643)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(3000850, 11006)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event13005493():
    """ 13005493: Event 13005493 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfAttackedWithDamageType(1, attacked_entity=3000850, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=3002644)
    IfCharacterInsideRegion(-1, PLAYER, region=3002645)
    IfCharacterInsideRegion(-1, PLAYER, region=3002646)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(3000850, 11010)
    Restart()


@RestartOnRest
def Event13005494():
    """ 13005494: Event 13005494 """
    EndIfFlagOn(13000481)
    EndIfFlagOn(9420)
    IfAttackedWithDamageType(1, attacked_entity=3000850, attacker=PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3002647)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(3000850, 11011)
    Restart()


@RestartOnRest
def Event13005510(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 13005510: Event 13005510 """
    EndIfThisEventSlotOn()
    IfHasTAEEvent(0, arg_0_3, tae_event_id=100)
    Wait(arg_12_15)
    IfCharacterHasSpecialEffect(1, arg_4_7, 5450)
    IfCharacterAlive(1, arg_4_7)
    EndIfConditionFalse(1)
    ForceAnimation(arg_4_7, arg_8_11)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event13005530():
    """ 13005530: Event 13005530 """
    EndIfThisEventSlotOn()
    Wait(5.0)
    Move(3000496, destination=3002500, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000580, destination=3002501, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000526, destination=3002502, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000522, destination=3002503, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest
def Event13005535():
    """ 13005535: Event 13005535 """
    EndIfThisEventSlotOn()
    DisableAI(3000488)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=3002381)
    IfCharacterInsideRegion(-2, PLAYER, region=3002382)
    IfAttacked(-3, 3000488, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    IfCharacterInsideRegion(2, PLAYER, region=3002381)
    IfCharacterInsideRegion(-4, PLAYER, region=3002382)
    IfAttacked(-4, 3000488, attacker=PLAYER)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    GotoIfConditionTrue(Label.L1, input_condition=-4)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3000488, 3004, skip_transition=True)
    EnableAI(3000488)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableAI(3000488)
    End()


@RestartOnRest
def Event13005540():
    """ 13005540: Event 13005540 """
    IfCharacterInsideRegion(-1, PLAYER, region=3002510)
    IfCharacterInsideRegion(-1, PLAYER, region=3002511)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3002510)
    IfCharacterInsideRegion(2, PLAYER, region=3002511)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAreaWelcomeMessage()


@RestartOnRest
def Event13005550():
    """ 13005550: Event 13005550 """
    EndIfPlayerNotInOwnWorld()
    IfActionButtonParam(0, action_button_id=3001810, entity=3001650)
    IfPlayerHasGood(1, 2102, including_box=False)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisplayDialog(
        10012001,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfLeavingSession(2)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()
    SkipLinesIfFlagOn(2, 13100331)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(
        31000010,
        CutsceneFlags.Skippable,
        ceremony_id=0,
        unknown=1,
        move_to_region=3102515,
        move_to_map=UNDEAD_SETTLEMENT,
        player_id=PLAYER,
    )
    SkipLines(1)
    WarpToMap(game_map=UNDEAD_SETTLEMENT, player_start=3100974)
    EnableFlag(13100330)
    WaitFrames(1)
    SetRespawnPoint(3102515)
    SaveRequest()
    Restart()


@RestartOnRest
def Event13005560():
    """ 13005560: Event 13005560 """
    GotoIfFlagOn(Label.L0, 711)
    DisableObject(3001872)
    DisableObject(3001874)
    EnableObject(3001871)
    EnableObject(3001873)
    IfFlagOn(0, 711)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(3001872)
    EnableObject(3001874)
    DisableObject(3001871)
    DisableObject(3001873)


@RestartOnRest
def Event13005590():
    """ 13005590: Event 13005590 """
    EndIfThisEventSlotOn()
    RestoreObject(3006450)


@RestartOnRest
def Event13005595():
    """ 13005595: Event 13005595 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3002680)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    PlaySoundEffect(anchor_entity=3002681, sound_type=SoundType.a_Ambient, sound_id=300000010)


@RestartOnRest
def Event13005440():
    """ 13005440: Event 13005440 """
    RunCommonEvent(
        20005621,
        args=(13000300, 13000301, 3001200, 3001201, 3004201, 3001202, 3004202, 3002301, 3002302, 13001300, 13004300, 0),
    )
    RunCommonEvent(
        20005625,
        args=(13000310, 13000311, 3001210, 3001211, 3004211, 3001212, 3004212, 3002311, 3002312, 13001310, 13004310, 0),
    )
    RunCommonEvent(
        20005621,
        args=(13000320, 13000321, 3001220, 3001221, 3004221, 3001222, 3004222, 3002321, 3002322, 13001320, 13004320, 0),
    )
    RunCommonEvent(
        20005623,
        args=(13000330, 13000331, 3001230, 3001231, 3004231, 3001232, 3004232, 3002331, 3002332, 13001330, 13004330, 0),
    )


@RestartOnRest
def Event13005810():
    """ 13005810: Event 13005810 """
    DisableAI(3000800)
    DisableHealthBar(3000800)
    DisableCharacter(3000800)
    EndIfFlagOn(13000800)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.Equal, 0)
    GotoIfThisEventSlotOn(Label.L2)
    GotoIfFlagOn(Label.L1, 13000801)
    Move(3000800, destination=3002811, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterInsideRegion(1, PLAYER, region=3002815)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    BanishInvaders(unknown=0)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=4)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=7)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=21)
    IfCharacterType(-15, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(-15)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagOn(Label.L2, 13000801)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        30000030,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=3002810,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    PlayCutscene(
        30000030,
        skippable=False,
        fade_out=True,
        player_id=PLAYER,
        move_to_region=3002810,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000030, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    EnableCharacter(3000800)
    IfFlagOff(3, 13000800)
    IfCharacterInsideRegion(3, PLAYER, region=3002801)
    IfConditionTrue(0, input_condition=3)
    ForceAnimation(3000800, 3030)

    # --- 2 --- #
    DefineLabel(2)
    EnableCharacter(3000800)
    EnableAI(3000800)
    SetNetworkUpdateRate(3000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3000800, name=902240)
    SetNetworkConnectedFlagState(flag=13000801, state=FlagState.On)


def Event13005811():
    """ 13005811: Event 13005811 """
    EndIfFlagOn(13000800)
    IfHealthLessThanOrEqual(0, 3000800, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=3000800, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 3000800)
    Wait(3.5)
    KillBoss(3000800)
    DisableSoundEvent(3002805)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableFlag(13000800)
    EnableFlag(9301)
    EnableFlag(6301)


@RestartOnRest
def Event13005812():
    """ 13005812: Event 13005812 """
    GotoIfFlagOn(Label.L0, 13000800)
    IfFlagOn(0, 13000800)
    Wait(2.0)
    ForceAnimation(3001815, 1, skip_transition=True)
    Wait(7.5)
    CreateObjectVFX(830101, obj=3001815, model_point=100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3001815, 2, loop=True)
    CreateObjectVFX(830101, obj=3001815, model_point=100)


@RestartOnRest
def Event13005815():
    """ 13005815: Event 13005815 """
    EndIfFlagOn(13000800)
    IfHasTAEEvent(0, 3000800, tae_event_id=10)
    End()


@RestartOnRest
def Event13005817():
    """ 13005817: Event 13005817 """
    EndIfFlagOn(13000800)
    DisableNetworkSync()
    IfFlagOn(1, 13005805)
    IfCharacterInsideRegion(1, PLAYER, region=3002801)
    IfConditionTrue(0, input_condition=1)
    ChangeCamera(normal_camera_id=3300, locked_camera_id=3300)


@RestartOnRest
def Event13005820():
    """ 13005820: Event 13005820 """
    RunCommonEvent(20005800, args=(13000800, 3001800, 3002800, 13005805, 3001800, 3000800, 13000801, 0))
    RunCommonEvent(20005801, args=(13000800, 3001800, 3002800, 13005805, 3001800, 13005806))
    RunCommonEvent(20005820, args=(13000800, 3001800, 3, 13000801))
    SkipLinesIfFlagOn(2, 13000801)
    RunCommonEvent(20001836, args=(13000800, 13005805, 13005806, 13005810, 3002805, 3002806, 13005815))
    SkipLines(1)
    RunCommonEvent(20005831, args=(13000800, 13005805, 13005806, 3002800, 3002805, 3002806, 13005815))
    RunCommonEvent(20005810, args=(13000825, 3001800, 3002800, 10000))


@RestartOnRest
def Event13005825(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13005825: Event 13005825 """
    GotoIfThisEventSlotOff(Label.L0)
    IfFlagChange(-1, arg_4_7)
    IfFlagChange(-1, arg_8_11)
    IfFlagChange(-1, arg_12_15)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(1, arg_12_15)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    IfFlagOn(2, arg_4_7)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_16_19)
    GotoIfConditionTrue(Label.L2, input_condition=2)
    IfFlagOff(3, arg_4_7)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    IfFlagOn(4, arg_4_7)
    IfFlagOn(4, arg_8_11)
    GotoIfConditionTrue(Label.L1, input_condition=4)
    IfFlagOn(5, arg_4_7)
    IfFlagOn(5, arg_16_19)
    GotoIfConditionTrue(Label.L1, input_condition=4)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(arg_0_3)
    Wait(5.0)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(arg_0_3)
    Wait(5.0)
    Restart()


@RestartOnRest
def Event13005826(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
    arg_36_39: int,
):
    """ 13005826: Event 13005826 """
    EndIfPlayerNotInOwnWorld()
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(2, arg_0_3)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    AICommand(arg_12_15, command_id=10, slot=0)
    ReplanAI(arg_12_15)
    IfCharacterInsideRegion(2, arg_12_15, region=arg_24_27)
    IfFlagOn(2, arg_32_35)
    IfConditionTrue(0, input_condition=2)
    RotateToFaceEntity(arg_12_15, arg_16_19, animation=60060, wait_for_completion=True)
    IfCharacterInsideRegion(-10, arg_12_15, region=arg_16_19)
    IfTimeElapsed(-11, 3.0)
    IfConditionTrue(-10, input_condition=-11)
    IfConditionTrue(0, input_condition=-10)
    RestartIfFinishedConditionTrue(-11)
    AICommand(arg_12_15, command_id=-1, slot=0)
    AICommand(arg_12_15, command_id=50, slot=3)
    ReplanAI(arg_12_15)
    SetNetworkUpdateRate(arg_12_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_12_15, command_id=11, slot=0)
    ReplanAI(arg_12_15)
    IfCharacterInsideRegion(2, arg_12_15, region=arg_28_31)
    IfFlagOn(2, arg_36_39)
    IfConditionTrue(0, input_condition=2)
    RotateToFaceEntity(arg_12_15, arg_20_23, animation=60060, wait_for_completion=True)
    IfCharacterInsideRegion(-12, arg_12_15, region=arg_20_23)
    IfTimeElapsed(-13, 3.0)
    IfConditionTrue(-12, input_condition=-13)
    IfConditionTrue(0, input_condition=-12)
    RestartIfFinishedConditionTrue(-13)
    AICommand(arg_12_15, command_id=-1, slot=0)
    ReplanAI(arg_12_15)
    SetNetworkUpdateRate(arg_12_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()


@RestartOnRest
def Event13005830():
    """ 13005830: Event 13005830 """
    DisableAI(3000830)
    DisableHealthBar(3000830)
    DisableCharacter(3000830)
    DisableSoundEvent(3002835)
    EndIfFlagOn(13000830)
    GotoIfThisEventSlotOn(Label.L1)
    GotoIfFlagOn(Label.L0, 13000838)
    IfFlagOff(1, 13000830)
    IfCharacterInsideRegion(1, PLAYER, region=3002830)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    BanishInvaders(unknown=0)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=4)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=7)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=21)
    IfCharacterType(-15, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(-15)
    GotoIfFlagOn(Label.L1, 13000838)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(30000040, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    PlayCutscene(30000040, skippable=False, fade_out=True, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(30000040, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EnableCharacter(3000830)
    IfFlagOff(2, 13000830)
    IfCharacterInsideRegion(2, PLAYER, region=3002830)
    IfConditionTrue(0, input_condition=2)

    # --- 1 --- #
    DefineLabel(1)
    EnableCharacter(3000830)
    EnableAI(3000830)
    SetNetworkUpdateRate(3000830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3000830, name=902090)
    DisableObjectActivation(3001813, obj_act_id=300371)
    SetNetworkConnectedFlagState(flag=13000838, state=FlagState.On)


def Event13005831():
    """ 13005831: Event 13005831 """
    EndIfFlagOn(13000830)
    IfHealthLessThanOrEqual(0, 3000830, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=3000830, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 3000830)
    Wait(3.5)
    KillBoss(3000830)
    EnableFlag(13000830)
    EnableFlag(9302)
    EnableFlag(6302)
    WaitFrames(1)
    EnableObjectActivation(3001813, obj_act_id=300371)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest
def Event13005835():
    """ 13005835: Event 13005835 """
    EndIfFlagOn(13000830)
    IfHasTAEEvent(0, 3000830, tae_event_id=10)
    WaitFrames(1)
    End()


@RestartOnRest
def Event13005836():
    """ 13005836: Event 13005836 """
    EndIfFlagOn(13000830)
    IfHasTAEEvent(0, 3000830, tae_event_id=20)
    EnableFlag(73000202)
    WaitFrames(1)
    End()


@RestartOnRest
def Event13005837():
    """ 13005837: Event 13005837 """
    EndIfFlagOn(13000830)
    IfHasTAEEvent(0, 3000830, tae_event_id=20)
    CreateNPCPart(
        3000830,
        npc_part_id=10,
        part_index=NPCPartType.Part6,
        part_health=193,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )


@RestartOnRest
def Event13005838():
    """ 13005838: Event 13005838 """
    EndIfFlagOn(13000830)
    IfCharacterHasSpecialEffect(1, 3000830, 5404)
    IfCharacterPartHealthLessThanOrEqual(1, 3000830, npc_part_id=10, value=0)
    IfFlagOn(1, 13005837)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3000830, 20000, wait_for_completion=True, skip_transition=True)
    CreateNPCPart(
        3000830,
        npc_part_id=10,
        part_index=NPCPartType.Part6,
        part_health=193,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    Restart()


@RestartOnRest
def Event13005840():
    """ 13005840: Event 13005840 """
    RunCommonEvent(20005800, args=(13000830, 3001830, 3002831, 13005855, 3001830, 3000830, 0, 3002830))
    RunCommonEvent(20005801, args=(13000830, 3001830, 3002831, 13005855, 3001830, 13005856))
    RunCommonEvent(20005820, args=(13000830, 3001830, 3, 0))
    RunCommonEvent(20001836, args=(13000830, 13005855, 13005856, 13005830, 3002835, 3002836, 13005835))
    RunCommonEvent(20005837, args=(13000830, 3001830, 1148829696, 2090, 2090, 13005855, 13005856))
    RunCommonEvent(20005810, args=(13000830, 3001830, 3002831, 10000))
    RunCommonEvent(20005810, args=(13000825, 3001890, 3002896, 10000))


@RestartOnRest
def Event13005850():
    """ 13005850: Event 13005850 """
    EndIfFlagOn(13000830)
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=3002850)
    EndIfFlagOn(13000830)
    SetBackgroundMusic(state=True, slot=0, entity=3002850, sound_type=SoundType.a_Ambient, sound_id=300000020)
    IfCharacterOutsideRegion(0, PLAYER, region=3002850)
    SetBackgroundMusic(state=False, slot=0, entity=3002850, sound_type=SoundType.a_Ambient, sound_id=300000020)
    Restart()


@RestartOnRest
def Event13005861():
    """ 13005861: Event 13005861 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(13005862)
    IfFailedToCreateSession(0)
    EnableFlag(13005862)
    IfFailedToCreateSession(1)
    IfConditionFalse(0, input_condition=1)
    DisableFlag(13005862)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event13005880():
    """ 13005880: Event 13005880 """
    GotoIfFlagOn(Label.L0, 13000885)
    ForceAnimation(3001087, 0, loop=True)
    DisableObject(3001870)
    EndIfPlayerNotInOwnWorld()
    IfFlagOn(0, 13000890)
    IfActionButtonParam(0, action_button_id=3001895, entity=3001896)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        30000020,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=3002880,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    PlayCutscene(
        30000020,
        skippable=False,
        fade_out=True,
        player_id=PLAYER,
        move_to_region=3002880,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000020, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    RemoveGoodFromPlayer(2117, quantity=1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3001087, 10, loop=True)
    EnableObject(3001870)
    RegisterLadder(start_climbing_flag=13000264, stop_climbing_flag=13000265, obj=3001087)
    ForceAnimation(3001896, 2, loop=True)
    EnableFlag(13000885)


@RestartOnRest
def Event13005889():
    """ 13005889: Event 13005889 """
    EndIfFlagOn(13000890)
    IfCharacterType(1, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(1)
    WaitFrames(1)
    IfFlagOn(0, 13005885)
    EnableCharacter(3000899)
    EnableAnimations(3000899)
    EnableAI(3000899)
    ActivateMultiplayerBuffs(3000899)
    EnableFlag(13000896)


@RestartOnRest
def Event13005890():
    """ 13005890: Event 13005890 """
    DisableObject(3001890)
    DisableAI(3000899)
    DisableCharacter(3000899)
    DisableAnimations(3000899)
    DisableSoundEvent(3002899)
    DisableSoundEvent(3002898)
    ForceAnimation(3001895, 2, loop=True)
    DisableObjectActivation(3001895, obj_act_id=300370)
    CreateObjectVFX(800030, obj=3001360, model_point=210)
    CreateObjectVFX(800030, obj=3001360, model_point=212)
    CreateObjectVFX(800043, obj=3001360, model_point=214)
    CreateObjectVFX(800030, obj=3001361, model_point=210)
    CreateObjectVFX(800030, obj=3001361, model_point=212)
    CreateObjectVFX(800043, obj=3001361, model_point=214)
    CreateObjectVFX(800030, obj=3001362, model_point=210)
    CreateObjectVFX(800030, obj=3001362, model_point=212)
    CreateObjectVFX(800043, obj=3001362, model_point=214)
    CreateObjectVFX(800030, obj=3001363, model_point=210)
    CreateObjectVFX(800030, obj=3001363, model_point=212)
    CreateObjectVFX(800043, obj=3001363, model_point=214)
    DeleteObjectVFX(3001890, erase_root=True)
    DeleteObjectVFX(3001899, erase_root=True)
    EndIfFlagOn(13000890)
    GotoIfFlagOn(Label.L1, 13000896)
    Move(3000899, destination=3002893, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.Equal, 0)
    EnableObject(3001890)
    CreateObjectVFX(3, obj=3001890, model_point=101)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    SetNetworkConnectedFlagState(flag=13000881, state=FlagState.On)
    IfCharacterDead(1, 3000705)
    IfPlayerHasGood(1, 2117, including_box=False)
    IfCharacterInsideRegion(1, PLAYER, region=3002700)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    BanishInvaders(unknown=0)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    Wait(1.0)
    DeleteObjectVFX(3001890, erase_root=True)
    WaitFrames(1)
    EnableFlag(13004890)
    IfFlagOn(0, 13005894)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    NotifyBossBattleStart()
    SkipLinesIfLeavingSession(2)
    EnableObject(3001890)
    CreateObjectVFX(3, obj=3001890, model_point=101)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(3001890)
    CreateObjectVFX(3, obj=3001890, model_point=101)
    EnableCharacter(3000899)
    EnableAnimations(3000899)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    IfActionButtonParam(0, action_button_id=3001890, entity=3001890)
    RotateToFaceEntity(PLAYER, 3002896, animation=60060, wait_for_completion=True)

    # --- 2 --- #
    DefineLabel(2)
    IfCharacterInsideRegion(0, PLAYER, region=3002895)
    EnableFlag(13000880)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    NotifyBossBattleStart()
    BanishInvaders(unknown=0)
    IfCharacterType(3, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(3)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfPlayerNotInOwnWorld(Label.L4)
    EnableBossMusic(3002899)
    Unknown_2010_07(sound_id=3002898)
    EnableBossHealthBar(3000899, name=905270)
    SetNetworkUpdateRate(3000899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ChangeCamera(normal_camera_id=3000, locked_camera_id=3000)
    SetNetworkUpdateAuthority(3000899, UpdateAuthority.Forced)
    SetNetworkConnectedFlagState(flag=13005885, state=FlagState.On)

    # --- 4 --- #
    DefineLabel(4)


@RestartOnRest
def Event13005891():
    """ 13005891: Event 13005891 """
    EndIfFlagOn(13000890)
    IfHasTAEEvent(0, 3000899, tae_event_id=10)
    EnableBossMusic(3002898)


@RestartOnRest
def Event13005892():
    """ 13005892: Event 13005892 """
    EndIfFlagOn(13000890)
    CreateNPCPart(
        3000899,
        npc_part_id=10,
        part_index=NPCPartType.Part5,
        part_health=400,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(0, 3000899, npc_part_id=10, value=0)
    ForceAnimation(3000899, 20000, wait_for_completion=True, skip_transition=True)
    SetNPCPartHealth(3000899, npc_part_id=10, desired_health=400, overwrite_max=True)
    Restart()


def Event13005893():
    """ 13005893: Event 13005893 """
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    DisableFlag(13005885)
    EndIfPlayerInOwnWorld()
    DisableNetworkSync()
    IfFlagOn(0, 13000881)
    GotoIfFlagOn(Label.L0, 13005894)
    ForceAnimation(3001895, 2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3001895, 0)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(0, 13005885)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfFlagOff(1, 13000890)
    IfActionButtonParam(1, action_button_id=3001890, entity=3001890)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3002896, animation=60060, wait_for_completion=True)
    EnableBossMusic(3002899)
    EnableBossHealthBar(3000899, name=905270)
    SetNetworkUpdateRate(3000899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ChangeCamera(normal_camera_id=3000, locked_camera_id=3000)
    EnableFlag(13005886)
    EnableFlag(13000896)
    End()


@RestartOnRest
def Event13005895():
    """ 13005895: Event 13005895 """
    EndIfFlagOn(13000890)
    IfHealthLessThanOrEqual(0, 3000899, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=3000899, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 3000899)
    Wait(2.5)
    DisableBossMusic(3002899)
    DisableBossMusic(3002898)
    DisableBossMusic(-1)
    KillBoss(3000899)
    ExtinguishBurningObjects()
    DeleteObjectVFX(3001885, erase_root=True)
    DeleteObjectVFX(3001886, erase_root=True)
    DeleteObjectVFX(3001887, erase_root=True)
    DeleteObjectVFX(3001888, erase_root=True)
    EnableFlag(13000890)
    EnableFlag(9300)
    EnableFlag(6300)
    DisableObject(3001890)
    DeleteObjectVFX(3001890, erase_root=True)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(2.0)
    SkipLinesIfFlagOn(2, 13000880)
    ForceAnimation(3001895, 1, wait_for_completion=True)
    ForceAnimation(3001895, 2)


@RestartOnRest
def Event13005899():
    """ 13005899: Event 13005899 """
    EndIfFlagOn(13000890)
    GotoIfFlagOn(Label.L0, 13005894)
    IfPlayerInOwnWorld(1)
    IfFlagOn(1, 13004890)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=4)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=7)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=21)
    IfCharacterType(-15, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(-15)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        30000010,
        skippable=True,
        fade_out=True,
        player_id=PLAYER,
        move_to_region=3002897,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    PlayCutscene(
        30000010,
        skippable=False,
        fade_out=True,
        player_id=PLAYER,
        move_to_region=3002897,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000010, skippable=False, fade_out=False, player_id=PLAYER)
    DeleteObjectVFX(3001360, erase_root=True)
    DeleteObjectVFX(3001361, erase_root=True)
    DeleteObjectVFX(3001362, erase_root=True)
    DeleteObjectVFX(3001363, erase_root=True)
    WaitFrames(1)
    ForceAnimation(3001895, 0)
    EnableFlag(13005894)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(3001360, erase_root=True)
    DeleteObjectVFX(3001361, erase_root=True)
    DeleteObjectVFX(3001362, erase_root=True)
    DeleteObjectVFX(3001363, erase_root=True)
    ForceAnimation(3001895, 0)
    EnableFlag(13005894)
    End()


@RestartOnRest
def Event13000901(_, arg_0_3: int):
    """ 13000901: Event 13000901 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagOn(6079)
    DisableNetworkSync()
    CreateObjectVFX(62, obj=arg_0_3, model_point=90)
    IfActionButtonParam(0, action_button_id=4200, entity=arg_0_3)
    ForceAnimation(PLAYER, 60070)
    DeleteObjectVFX(arg_0_3, erase_root=True)
    EnableFlag(13000900)


def Event13005600(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13005600: Event 13005600 """
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyOn(2, (1435, 1439))
    SetNetworkConnectedFlagRangeState((1435, 1439), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1435, state=FlagState.On)
    IfFlagOn(2, 1435)
    IfFlagOn(2, 50006230)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1435, 1439), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1438, state=FlagState.On)
    SkipLinesIfFlagRangeAnyOn(2, (1420, 1434))
    SetNetworkConnectedFlagRangeState((1420, 1434), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1420, state=FlagState.On)
    IfFlagOn(1, 711)
    IfFlagOn(1, 1435)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1420, 1434), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1421, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    GotoIfFlagOn(Label.L0, 1420)
    GotoIfFlagOn(Label.L1, 1421)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableObject(arg_0_3)
    DisableObject(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(arg_8_11)
    GotoIfFlagOn(Label.L10, 1438)
    ForceAnimation(arg_0_3, 20)
    Move(arg_0_3, destination=3002705, destination_type=CoordEntityType.Region, short_move=True)
    EnableObjectInvulnerability(arg_4_7)
    End()

    # --- 10 --- #
    DefineLabel(10)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    Move(arg_0_3, destination=3002710, destination_type=CoordEntityType.Region, short_move=True)
    DisableObject(arg_4_7)
    GotoIfFlagOn(Label.L10, 1438)
    ForceAnimation(arg_0_3, 30000)
    DisableHealthBar(arg_0_3)
    EnableImmortality(arg_0_3)
    End()

    # --- 10 --- #
    DefineLabel(10)
    DisableObject(arg_8_11)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event13005601(_, arg_0_3: int):
    """ 13005601: Event 13005601 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagOn(0, arg_0_3)
    AwardItemLot(62320, host_only=False)


def Event13005602(_, arg_0_3: int, arg_4_7: int):
    """ 13005602: Event 13005602 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_4_7)
    IfFlagOn(0, arg_4_7)
    ForceAnimation(arg_0_3, 20001)


def Event13005603(_, arg_0_3: int):
    """ 13005603: Event 13005603 """
    EndIfPlayerNotInOwnWorld()
    IfFlagOn(1, 1421)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(73000182)
    ForceAnimation(arg_0_3, 20001)


def Event13005604():
    """ 13005604: Event 13005604 """
    IfFlagOn(0, 1438)
    DisableObjectInvulnerability(3001875)


def Event13005620(_, arg_0_3: int):
    """ 13005620: Event 13005620 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyOn(2, (1215, 1219))
    SetNetworkConnectedFlagRangeState((1215, 1219), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1215, state=FlagState.On)
    IfFlagOn(1, 1216)
    IfFlagOn(1, 70000062)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1215, 1219), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1215, state=FlagState.On)
    SkipLinesIfFlagRangeAnyOn(2, (1200, 1214))
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1200, state=FlagState.On)
    GotoIfFlagOff(Label.L9, 1215)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000062)
    SkipLinesIfFlagOff(1, 1215)
    DisableFlag(73000120)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagOn(Label.L0, 1200)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagOn(Label.L1, 1216)
    GotoIfFlagOn(Label.L2, 1218)
    ForceAnimation(arg_0_3, 90360, skip_transition=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(arg_0_3)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()


@RestartOnRest
def Event13005640(_, arg_0_3: int):
    """ 13005640: Event 13005640 """
    SkipLinesIfFlagOn(4, 13000830)
    SetCharacterTalkRange(arg_0_3, distance=80.0)
    DisableFlag(73000200)
    DisableFlag(73000201)
    DisableFlag(73000202)

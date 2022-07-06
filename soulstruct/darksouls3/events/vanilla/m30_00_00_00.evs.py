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
from soulstruct.darksouls3.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=13000009, obj=3001950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13000003, obj=3001959, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13000005, obj=3001955, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13000008, obj=3001958, reaction_distance=5.0)
    RunCommonEvent(20005500, args=(13000800, 13000002, 3000952, 3001952))
    RunCommonEvent(20005500, args=(13000830, 13000001, 3000951, 3001951))
    RunCommonEvent(20005500, args=(13000890, 13000004, 3000954, 3001954))
    Event_13000210()
    Event_13000200()
    RunCommonEvent(20005780, args=(3001780, 2))
    Event_13005350(0, obj=3001890, model_point=3)
    Event_13005810()
    Event_13005811()
    Event_13005815()
    Event_13005820()
    Event_13005812()
    Event_13005817()
    RunCommonEvent(20005840, args=(3001800,))
    RunCommonEvent(20005841, args=(3001800,))
    Event_13005825(0, flag=13000825, flag_1=13000800, flag_2=13000896, flag_3=13000890, flag_4=711)
    Event_13005830()
    Event_13005831()
    Event_13005840()
    Event_13005835()
    Event_13005836()
    Event_13005837()
    Event_13005838()
    Event_13005595()
    Event_13005850()
    Event_13005890()
    Event_13005895()
    Event_13005891()
    Event_13005892()
    Event_13005893()
    Event_13005889()
    Event_13005899()
    Event_13005880()
    RunCommonEvent(20005840, args=(3001890,))
    RunCommonEvent(20005841, args=(3001890,))
    Event_13005280(0, obj=3001316, vfx_id=830078)
    Event_13005280(1, obj=3001300, vfx_id=830077)
    Event_13005280(2, obj=3001301, vfx_id=830077)
    Event_13005280(3, obj=3001302, vfx_id=830077)
    Event_13005280(4, obj=3001303, vfx_id=830077)
    Event_13005280(5, obj=3001304, vfx_id=830077)
    Event_13005280(6, obj=3001305, vfx_id=830077)
    Event_13005280(7, obj=3001306, vfx_id=830077)
    Event_13005280(8, obj=3001307, vfx_id=830077)
    Event_13005280(9, obj=3001308, vfx_id=830077)
    Event_13005280(10, obj=3001309, vfx_id=830077)
    Event_13005280(11, obj=3001310, vfx_id=830077)
    Event_13005280(12, obj=3001311, vfx_id=830077)
    Event_13005280(13, obj=3001312, vfx_id=830077)
    Event_13005280(14, obj=3001313, vfx_id=830077)
    Event_13005280(15, obj=3001314, vfx_id=830077)
    Event_13005280(16, obj=3001315, vfx_id=830077)
    Event_13005480()
    Event_13005485()
    Event_13005486()
    Event_13005487()
    Event_13005488()
    Event_13005489()
    Event_13005481()
    Event_13005490()
    Event_13005493()
    Event_13005494()
    RunCommonEvent(20005415, args=(13001500, 3000610, 3000611, 702, 1702, 3002490, 13005501, 13005502))
    RunCommonEvent(20005417, args=(13001501, 3000612, 3000613, 702, 1702, 0, 13005503, 13005504, 3002365))
    Event_13005510(0, 3000610, 3000502, 20000, 0.20000000298023224)
    Event_13005510(1, 3000610, 3000509, 20001, 0.0)
    Event_13005510(2, 3000610, 3000505, 20002, 0.699999988079071)
    Event_13005510(3, 3000610, 3000507, 20000, 1.0)
    Event_13005510(4, 3000612, 3000423, 20000, 0.0)
    Event_13005510(5, 3000612, 3000421, 20000, 0.20000000298023224)
    Event_13005510(6, 3000612, 3000410, 20001, 0.4000000059604645)
    Event_13005510(7, 3000612, 3000411, 20002, 0.6000000238418579)
    Event_13005200(0, 3000451, 20001, 0.8999999761581421, 0, 3000450, 3000601, 3000607, 3000452)
    Event_13005200(1, 3000450, 20000, 0.20000000298023224, 3000451, 0, 3000601, 3000607, 3000452)
    Event_13005200(2, 3000601, 20001, 0.4000000059604645, 3000451, 3000450, 0, 3000607, 3000452)
    Event_13005200(3, 3000607, 20001, 0.0, 3000451, 3000450, 3000601, 0, 3000452)
    Event_13005200(4, 3000452, 20002, 0.699999988079071, 3000451, 3000450, 3000601, 3000607, 0)
    Event_13005210(0, 3000604, 20001, 0.5, 3000600, 0, 0, 0, 0)
    Event_13005210(1, 3000600, 20000, 0.699999988079071, 3000604, 0, 0, 0, 0)
    Event_13005210(2, 3000484, 20002, 0.5, 3000454, 0, 0, 0, 0)
    Event_13005210(3, 3000454, 20001, 0.699999988079071, 3000484, 0, 0, 0, 0)
    Event_13005210(4, 3000605, 20002, 0.699999988079071, 0, 0, 0, 0, 0)
    Event_13005220(1, 3000457, 20001, 0.30000001192092896, 3000456, 0, 0, 0, 0)
    Event_13005220(2, 3000456, 20000, 0.10000000149011612, 3000457, 0, 0, 0, 0)
    Event_13005230(0, 3000464, 20002, 0.800000011920929, 3000463, 0, 0, 0, 0)
    Event_13005230(1, 3000463, 20001, 0.30000001192092896, 3000464, 0, 0, 0, 0)
    Event_13005240(0, 3000592, 20000, 0.0, 3000596, 0, 0, 0, 0)
    Event_13005240(1, 3000596, 20002, 0.0, 3000592, 0, 0, 0, 0)
    Event_13005240(2, 3000533, 20001, 0.0, 0, 0, 0, 0, 0)
    Event_13005025()
    Event_13005530()
    Event_13005535()
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
    RunCommonEvent(20005210, args=(3000409, 706, 1706, 3.0), arg_types="iiif")
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
    RunCommonEvent(20005122, args=(3000431, 3003, 6.0), arg_types="iif")
    RunCommonEvent(20005220, args=(3000432, 706, 1706))
    RunCommonEvent(20005210, args=(3000432, 706, 1706, 5.0), arg_types="iiif")
    RunCommonEvent(20005213, args=(3000433, 703, 1703, 3.0, 3002650), arg_types="iiifi")
    RunCommonEvent(20005111, args=(3000434, 3011, 3002380))
    RunCommonEvent(20005213, args=(3000435, 703, 1703, 3.0, 3002425), arg_types="iiifi")
    RunCommonEvent(20005213, args=(3000436, 706, 1706, 3.0, 3002425), arg_types="iiifi")
    RunCommonEvent(20005119, args=(3000440, 3002226, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005210, args=(3000441, 703, 1703, 3.0), arg_types="iiif")
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
    RunCommonEvent(20005205, args=(3000477, 710, 1710, 3002361, 1.100000023841858), arg_types="iiiif")
    RunCommonEvent(20005205, args=(3000478, 710, 1710, 3002361, 1.0), arg_types="iiiif")
    RunCommonEvent(20005119, args=(3000482, 3002226, 3002221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005110, args=(3000483, 3002340))
    RunCommonEvent(20005290, args=(3000484, 702, 1702))
    RunCommonEvent(20005290, args=(3000486, 701, 1701))
    RunCommonEvent(20005290, args=(3000487, 702, 1702))
    RunCommonEvent(20005205, args=(3000490, 710, 1710, 3002361, 0.800000011920929), arg_types="iiiif")
    RunCommonEvent(20005205, args=(3000492, 710, 1710, 3002361, 0.4000000059604645), arg_types="iiiif")
    RunCommonEvent(20005220, args=(3000494, 703, 1703))
    RunCommonEvent(20005220, args=(3000495, 703, 1703))
    RunCommonEvent(20005210, args=(3000496, 710, 1710, 4.5), arg_types="iiif")
    RunCommonEvent(20005290, args=(3000500, 703, 1703))
    RunCommonEvent(20005290, args=(3000502, 700, 1700))
    RunCommonEvent(20005290, args=(3000504, 702, 1702))
    RunCommonEvent(20005290, args=(3000505, 702, 1702))
    RunCommonEvent(20005290, args=(3000507, 700, 1700))
    RunCommonEvent(20005290, args=(3000509, 701, 1701))
    RunCommonEvent(20005122, args=(3000511, 3000, 5.0), arg_types="iif")
    RunCommonEvent(20005210, args=(3000520, 706, 1706, 5.5), arg_types="iiif")
    RunCommonEvent(20005202, args=(3000522, 710, 1710, 3002430))
    RunCommonEvent(20005111, args=(3000523, 3003, 3002220))
    RunCommonEvent(20005210, args=(3000525, 706, 1706, 5.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(3000526, 710, 1710, 5.0), arg_types="iiif")
    RunCommonEvent(20005290, args=(3000533, 701, 1701))
    RunCommonEvent(20005119, args=(3000537, 3002480, 3002350, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3000538, 3002480, 3002350, 0, 0, 0, 0, 0))
    RunCommonEvent(20005210, args=(3000539, 706, 1706, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(3000540, 706, 1706, 3.0), arg_types="iiif")
    RunCommonEvent(20005213, args=(3000545, 703, 1703, 3.0, 3002362), arg_types="iiifi")
    RunCommonEvent(20005290, args=(3000551, 703, 1703))
    RunCommonEvent(20005290, args=(3000560, 703, 1703))
    RunCommonEvent(20005214, args=(3000568, 710, 1710, 7.5), arg_types="iiif")
    RunCommonEvent(20005221, args=(3000570, 703, 1703, 5.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(3000571, 705, 1705, 5.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(3000572, 706, 1706, 5.0), arg_types="iiif")
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
    RunCommonEvent(20005411, args=(3000561, 3000560, 703, 1703, 0.5), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000561, 3000407, 706, 1706, 1.2000000476837158), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000561, 3000408, 703, 1703, 0.4000000059604645), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000561, 3000428, 706, 1706, 0.0), arg_types="iiiif")
    RunCommonEvent(20005410, args=(3000443, 3005))
    RunCommonEvent(20005411, args=(3000443, 3000444, 705, 1705, 0.0), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000443, 3000426, 705, 1705, 0.4000000059604645), arg_types="iiiif")
    RunCommonEvent(20005410, args=(3000400, 3005))
    RunCommonEvent(20005411, args=(3000400, 3000401, 703, 1703, 2.700000047683716), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000400, 3000402, 705, 1705, 1.5), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000400, 3000403, 706, 1706, 1.0), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000400, 3000405, 703, 1703, 2.0999999046325684), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3000400, 3000406, 703, 1703, 2.5), arg_types="iiiif")
    Event_13000380(0, character=3000660, item_lot_param_id=60940, flag=6780)
    RunCommonEvent(20005340, args=(13000381, 3000661))
    RunCommonEvent(20005701, args=(13000800, 13005700, 13005701, 3000190, 3002780, 13005392))
    Event_13005826(
        0,
        flag=13005700,
        flag_1=13005805,
        flag_2=13005885,
        character=3000190,
        region=3002800,
        region_1=3002896,
        region_2=3002820,
        region_3=3002870,
        flag_3=13000801,
        flag_4=13000896
    )
    RunCommonEvent(20005720, args=(13005700, 13005701, 13000800, 3000190))
    RunCommonEvent(20005714, args=(13005700, 13005805, 3000190, 3002829, 13000801))
    Event_13005390()
    Event_13005391()
    RunCommonEvent(20005701, args=(13000800, 13005705, 13005706, 3000191, 3002781, 9500))
    Event_13005826(
        1,
        flag=13005705,
        flag_1=13005805,
        flag_2=13005885,
        character=3000191,
        region=3002800,
        region_1=3002896,
        region_2=3002820,
        region_3=3002870,
        flag_3=13000801,
        flag_4=13000896
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
    Event_13005440()
    Event_13005550()
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
    RunCommonEvent(20005613, args=(13000405, 3003309, 3001413, -1, 10010861))
    RunCommonEvent(20005613, args=(13000406, 3003310, 3001415, 300313, 10010870))
    Event_13005540()
    DeleteObjectVFX(3001885)
    DeleteObjectVFX(3001886)
    DeleteObjectVFX(3001887)
    DeleteObjectVFX(3001888)
    CreateObjectVFX(3001885, vfx_id=200, model_point=800023)
    CreateObjectVFX(3001886, vfx_id=200, model_point=800023)
    CreateObjectVFX(3001887, vfx_id=200, model_point=800023)
    CreateObjectVFX(3001888, vfx_id=200, model_point=800023)
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
    RunCommonEvent(20005540, args=(13005630, 3001510, 200, 5110, 0.5, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005540, args=(13005631, 3001511, 200, 5110, 0.5, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005540, args=(13005632, 3001512, 200, 5110, 0.5, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005540, args=(13005633, 3001513, 200, 5110, 0.5, 0.0, 1.0), arg_types="iiiifff")
    RegisterLadder(start_climbing_flag=13000250, stop_climbing_flag=13000251, obj=3001080)
    RegisterLadder(start_climbing_flag=13000252, stop_climbing_flag=13000253, obj=3001081)
    RegisterLadder(start_climbing_flag=13000254, stop_climbing_flag=13000255, obj=3001082)
    RegisterLadder(start_climbing_flag=13000256, stop_climbing_flag=13000257, obj=3001083)
    RegisterLadder(start_climbing_flag=13000258, stop_climbing_flag=13000259, obj=3001084)
    RegisterLadder(start_climbing_flag=13000260, stop_climbing_flag=13000261, obj=3001085)
    RegisterLadder(start_climbing_flag=13000262, stop_climbing_flag=13000263, obj=3001086)
    Event_13000230()
    RunCommonEvent(20005523, args=(3001270, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3001271, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3001272, 2), arg_types="iB")
    RunCommonEvent(20005523, args=(3001273, 2), arg_types="iB")
    RunCommonEvent(20006003, args=(3000700, 73000132, 1215, 1200, 1201, 1200, 1214))
    RunCommonEvent(20006002, args=(3000700, 1218, 1215, 1219))
    RunCommonEvent(
        20006000,
        args=(3000700, 1216, 1217, 73000130, 0.6499999761581421, 1215, 1219, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3000700, 1216, 1217, 73000130, 3))
    Event_13005601(0, flag=73000181)
    Event_13005602(0, entity=3000705, flag=73000180)
    Event_13005603(0, attacked_entity=3000705)
    RunCommonEvent(20006002, args=(3000705, 1438, 1435, 1439))
    Event_13005604()
    Event_13005560()
    Event_13000360()
    Event_13000901(0, 3001900)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13000410()
    Event_13005861()
    Event_13005590()
    SetMultiplayerBuffs_NonBoss(character=3000850, state=True)
    Event_13005620(0, character=3000700)
    Event_13005600(0, character__obj=3000705, obj=3001875, obj_1=3001876)
    Event_13005640(0, character=3000830)
    DisableSoundEvent(sound_id=3002805)
    DisableSoundEvent(sound_id=3002806)
    DisableSoundEvent(sound_id=3002835)
    DisableSoundEvent(sound_id=3002836)
    DisableSoundEvent(sound_id=3002898)
    DisableSoundEvent(sound_id=3002899)


@NeverRestart(13000200)
def Event_13000200():
    """Event 13000200"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3002550))
    
    EnableFlag(13000201)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13000201)


@NeverRestart(13000210)
def Event_13000210():
    """Event 13000210"""
    if FlagEnabled(13000009):
        return
    
    MAIN.Await(FlagEnabled(13000009))
    
    DisableFlag(13000000)


@NeverRestart(13000230)
def Event_13000230():
    """Event 13000230"""
    if ThisEventSlotFlagEnabled():
        return
    DisableSoapstoneMessage(3002280)
    
    MAIN.Await(PlayerHasGood(2117, including_storage=True))
    
    EnableSoapstoneMessage(3002280)


@NeverRestart(13000360)
def Event_13000360():
    """Event 13000360"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(711))
    
    ForceAnimation(PLAYER, 63010, unknown2=1.0)
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=PLAYER, model_point=245, anchor_type=CoordEntityType.Character)
    CreateObjectVFX(3001705, vfx_id=90, model_point=830095)
    EnableFlag(13000360)
    Wait(10.0)
    DeleteObjectVFX(3001705)


@NeverRestart(13000380)
def Event_13000380(_, character: int, item_lot_param_id: int, flag: int):
    """Event 13000380"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(FlagEnabled(flag))
    if AND_1:
        return
    
    MAIN.Await(CharacterDead(character))
    
    AwardItemLot(item_lot_param_id, host_only=True)
    End()


@NeverRestart(13000410)
def Event_13000410():
    """Event 13000410"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13000300)
    EnableFlag(13000310)
    End()


@RestartOnRest(13005025)
def Event_13005025():
    """Event 13005025"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(3000404, 703, loop=True, unknown2=1.0)
    DisableAI(3000404)
    OR_1.Add(ObjectDestroyed(3001250))
    OR_2.Add(Attacked(attacked_entity=3000404, attacker=PLAYER))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    OR_1.Add(ObjectDestroyed(3001250))
    OR_2.Add(Attacked(attacked_entity=3000404, attacker=PLAYER))
    SkipLinesIfConditionTrue(2, OR_2)
    ForceAnimation(3000404, 1703, wait_for_completion=True, unknown2=1.0)
    EnableAI(3000404)


@RestartOnRest(13005200)
def Event_13005200(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005200"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000427, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000427, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000443, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000443, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000426, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000426, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000483, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000483, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3005500, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005210)
def Event_13005210(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005210"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000427, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000427, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000443, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000443, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000426, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000426, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000483, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000483, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3005500, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    AND_7.Add(CharacterHasTAEEvent(3000443, tae_event_id=20))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005220)
def Event_13005220(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005220"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000427, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000427, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000443, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000443, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000426, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000426, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000483, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000483, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3000561, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=3000561, other_entity=character, radius=3.5))
    AND_7.Add(HasAIStatus(3000408, ai_status=AIStatusType.Battle))
    AND_7.Add(EntityWithinDistance(entity=3000408, other_entity=character, radius=3.5))
    AND_8.Add(HasAIStatus(3000560, ai_status=AIStatusType.Battle))
    AND_8.Add(EntityWithinDistance(entity=3000560, other_entity=character, radius=3.5))
    AND_9.Add(HasAIStatus(3000579, ai_status=AIStatusType.Battle))
    AND_9.Add(EntityWithinDistance(entity=3000579, other_entity=character, radius=3.5))
    AND_10.Add(HasAIStatus(3000428, ai_status=AIStatusType.Battle))
    AND_10.Add(EntityWithinDistance(entity=3000428, other_entity=character, radius=3.5))
    AND_11.Add(HasAIStatus(3005501, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_11.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_2.Add(AND_9)
    OR_2.Add(AND_10)
    OR_2.Add(AND_11)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005230)
def Event_13005230(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005230"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000418, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000418, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000522, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000522, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000471, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000471, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000494, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000494, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3000488, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=3000488, other_entity=character, radius=3.5))
    AND_7.Add(HasAIStatus(3000230, ai_status=AIStatusType.Battle))
    AND_7.Add(EntityWithinDistance(entity=3000230, other_entity=character, radius=3.5))
    AND_8.Add(HasAIStatus(3005502, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_8.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005240)
def Event_13005240(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005240"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000255, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000255, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000520, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000520, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000253, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000253, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000242, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000242, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3000245, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=3000245, other_entity=character, radius=3.5))
    AND_7.Add(HasAIStatus(3005503, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_7.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@NeverRestart(13005280)
def Event_13005280(_, obj: int, vfx_id: int):
    """Event 13005280"""
    AND_1.Add(ObjectBurnState(obj=obj, comparison_type=ComparisonType.GreaterThan, state=False))
    AND_1.Add(FlagEnabled(13000890))
    
    MAIN.Await(AND_1)
    
    CreateTemporaryVFX(vfx_id=vfx_id, anchor_entity=obj, model_point=200, anchor_type=CoordEntityType.Object)


@RestartOnRest(13005350)
def Event_13005350(_, obj: int, model_point: int):
    """Event 13005350"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(13000890))
    
    DisableObject(obj)
    DeleteObjectVFX(obj)
    OR_1.Add(TryingToJoinSession())
    OR_1.Add(TryingToCreateSession())
    
    MAIN.Await(OR_1)
    
    EnableObject(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    OR_2.Add(TryingToJoinSession())
    OR_2.Add(TryingToCreateSession())
    
    MAIN.Await(not OR_2)
    
    Restart()


@RestartOnRest(13005390)
def Event_13005390():
    """Event 13005390"""
    if FlagEnabled(13000800):
        return
    AND_1.Add(PlayerHasGood(2117, including_storage=True))
    if AND_1:
        return
    EnableFlag(13005392)
    
    MAIN.Await(PlayerHasGood(2117, including_storage=True))
    
    DisableFlag(13005392)


@RestartOnRest(13005391)
def Event_13005391():
    """Event 13005391"""
    if FlagEnabled(13000800):
        return
    AND_1.Add(PlayerHasGood(2117, including_storage=True))
    if AND_1:
        return
    AND_2.Add(PlayerHasGood(2117, including_storage=True))
    AND_2.Add(FlagEnabled(13005700))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(3000190, 91030, unknown2=1.0)
    Wait(2.0)
    SendNPCSummonHome(character=3000190)


@RestartOnRest(13005480)
def Event_13005480():
    """Event 13005480"""
    DisableCharacter(3000850)
    DisableGravity(3000850)
    DisableAI(3000850)
    SetLockOnPoint(character=3000850, lock_on_model_point=220, state=False)
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    GotoIfFlagDisabled(Label.L0, flag=13000480)
    EnableCharacter(3000850)
    Move(3000850, destination=3002600, destination_type=CoordEntityType.Region, short_move=True)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableImmortality(3000850)
    if ThisEventSlotFlagEnabled():
        return
    CancelSpecialEffect(3000850, 11000)
    AddSpecialEffect(3000850, 11004)
    ForceAnimation(3000850, 30002, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002620))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    AND_3.Add(FlagEnabled(13000480))
    AND_4.Add(FlagEnabled(13000481))
    AND_5.Add(FlagEnabled(9420))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_5)
    Move(3000850, destination=3002600, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3000850, 20003, skip_transition=True, unknown2=1.0)
    EnableFlag(13000480)
    EnableImmortality(3000850)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(3000850)
    DisableGravity(3000850)
    DisableAI(3000850)
    SetLockOnPoint(character=3000850, lock_on_model_point=220, state=False)


@RestartOnRest(13005481)
def Event_13005481():
    """Event 13005481"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_1.Add(HealthLessThanOrEqual(3000850, value=0.20000000298023224))
    AND_2.Add(FlagEnabled(9420))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AwardItemLot(31410000, host_only=False)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3000850, 20007, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    DisableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    EnableFlag(13000481)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Never)


@RestartOnRest(13005485)
def Event_13005485():
    """Event 13005485"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    GotoIfFlagEnabled(Label.L0, flag=13000480)
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002621))
    AND_2.Add(CharacterHasSpecialEffect(3000850, 11000))
    AND_2.Add(CharacterHasSpecialEffect(3000850, 11001))
    AND_3.Add(OR_1)
    AND_3.Add(AND_1)
    AND_3.Add(AND_2)
    
    MAIN.Await(AND_3)
    
    CancelSpecialEffect(3000850, 11000)
    ForceAnimation(3000850, 20001, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(3000850, 11000)
    ForceAnimation(3000850, 30002, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(13005486)
def Event_13005486():
    """Event 13005486"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002617))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11003)
    Wait(3.0)
    Restart()


@RestartOnRest(13005487)
def Event_13005487():
    """Event 13005487"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002610))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002611))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11004)
    Wait(3.0)
    Restart()


@RestartOnRest(13005488)
def Event_13005488():
    """Event 13005488"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002615))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002616))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    CancelSpecialEffect(3000850, 11004)
    Wait(3.0)
    Restart()


@RestartOnRest(13005489)
def Event_13005489():
    """Event 13005489"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002630))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3000850, 11005)
    Wait(3.0)
    Restart()


@RestartOnRest(13005490)
def Event_13005490():
    """Event 13005490"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002640))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002642))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=3002641))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=3002643))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11006)
    Wait(3.0)
    Restart()


@RestartOnRest(13005493)
def Event_13005493():
    """Event 13005493"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=3000850, attacker=PLAYER))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002644))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002645))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002646))
    AND_2.Add(AND_1)
    AND_2.Add(OR_1)
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3000850, 11010)
    Restart()


@RestartOnRest(13005494)
def Event_13005494():
    """Event 13005494"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=3000850, attacker=PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002647))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11011)
    Restart()


@RestartOnRest(13005510)
def Event_13005510(_, character: int, character_1: int, animation_id: int, seconds: float):
    """Event 13005510"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=100))
    
    Wait(seconds)
    AND_1.Add(CharacterHasSpecialEffect(character_1, 5450))
    AND_1.Add(CharacterAlive(character_1))
    if not AND_1:
        return
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    ReplanAI(character_1)


@RestartOnRest(13005530)
def Event_13005530():
    """Event 13005530"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(5.0)
    Move(3000496, destination=3002500, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000580, destination=3002501, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000526, destination=3002502, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000522, destination=3002503, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(13005535)
def Event_13005535():
    """Event 13005535"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3000488)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002381))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002382))
    OR_3.Add(Attacked(attacked_entity=3000488, attacker=PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(OR_3)
    
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3002381))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3002382))
    OR_4.Add(Attacked(attacked_entity=3000488, attacker=PLAYER))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    GotoIfConditionTrue(Label.L1, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3000488, 3004, skip_transition=True, unknown2=1.0)
    EnableAI(3000488)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(3000488)
    End()


@RestartOnRest(13005540)
def Event_13005540():
    """Event 13005540"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002510))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002511))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002510))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3002511))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetAreaWelcomeMessageState(state=False)


@RestartOnRest(13005550)
def Event_13005550():
    """Event 13005550"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3001810, entity=3001650))
    
    AND_1.Add(PlayerHasGood(2102))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisplayDialog(text=10012001)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfLeavingSession(2)
    DisplayDialog(text=10010170)
    Restart()
    if FlagDisabled(13100331):
        PlayCutsceneAndMovePlayerAndSetMapCeremony(
            cutscene=31000010,
            cutscene_flags=0,
            ceremony_id=0,
            unknown=1,
            move_to_region=3102515,
            game_map=UNDEAD_SETTLEMENT,
            player_id=10000,
        )
    else:
        WarpToMap(game_map=UNDEAD_SETTLEMENT, player_start=3100974)
    EnableFlag(13100330)
    WaitFrames(frames=1)
    SetRespawnPoint(respawn_point=3102515)
    SaveRequest()
    Restart()


@RestartOnRest(13005560)
def Event_13005560():
    """Event 13005560"""
    GotoIfFlagEnabled(Label.L0, flag=711)
    DisableObject(3001872)
    DisableObject(3001874)
    EnableObject(3001871)
    EnableObject(3001873)
    
    MAIN.Await(FlagEnabled(711))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(3001872)
    EnableObject(3001874)
    DisableObject(3001871)
    DisableObject(3001873)


@RestartOnRest(13005590)
def Event_13005590():
    """Event 13005590"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(3006450)


@RestartOnRest(13005595)
def Event_13005595():
    """Event 13005595"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002680))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    
    MAIN.Await(AND_2)
    
    PlaySoundEffect(3002681, 300000010, sound_type=SoundType.a_Ambient)


@RestartOnRest(13005440)
def Event_13005440():
    """Event 13005440"""
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


@RestartOnRest(13005810)
def Event_13005810():
    """Event 13005810"""
    DisableAI(3000800)
    DisableHealthBar(3000800)
    DisableCharacter(3000800)
    if FlagEnabled(13000800):
        return
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    GotoIfThisEventSlotFlagEnabled(Label.L2)
    GotoIfFlagEnabled(Label.L1, flag=13000801)
    Move(3000800, destination=3002811, destination_type=CoordEntityType.Region, short_move=True)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002815))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_15:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L2, flag=13000801)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(30000030, cutscene_flags=0, player_id=10000, move_to_region=3002810, game_map=HIGH_WALL_OF_LOTHRIC)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        30000030,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002810,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000030, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(3000800)
    AND_3.Add(FlagDisabled(13000800))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=3002801))
    
    MAIN.Await(AND_3)
    
    ForceAnimation(3000800, 3030, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(3000800)
    EnableAI(3000800)
    SetNetworkUpdateRate(3000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3000800, name=902240)
    SetNetworkConnectedFlagState(flag=13000801, state=FlagSetting.On)


@NeverRestart(13005811)
def Event_13005811():
    """Event 13005811"""
    if FlagEnabled(13000800):
        return
    
    MAIN.Await(HealthLessThanOrEqual(3000800, value=0.0))
    
    Wait(1.0)
    PlaySoundEffect(3000800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3000800))
    
    Wait(3.5)
    KillBoss(game_area_param_id=3000800)
    DisableSoundEvent(sound_id=3002805)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableFlag(13000800)
    EnableFlag(9301)
    EnableFlag(6301)


@RestartOnRest(13005812)
def Event_13005812():
    """Event 13005812"""
    GotoIfFlagEnabled(Label.L0, flag=13000800)
    
    MAIN.Await(FlagEnabled(13000800))
    
    Wait(2.0)
    ForceAnimation(3001815, 1, skip_transition=True, unknown2=1.0)
    Wait(7.5)
    CreateObjectVFX(3001815, vfx_id=100, model_point=830101)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3001815, 2, loop=True, unknown2=1.0)
    CreateObjectVFX(3001815, vfx_id=100, model_point=830101)


@RestartOnRest(13005815)
def Event_13005815():
    """Event 13005815"""
    if FlagEnabled(13000800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000800, tae_event_id=10))
    
    End()


@RestartOnRest(13005817)
def Event_13005817():
    """Event 13005817"""
    if FlagEnabled(13000800):
        return
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(13005805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002801))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=3300, locked_camera_id=3300)


@RestartOnRest(13005820)
def Event_13005820():
    """Event 13005820"""
    RunCommonEvent(20005800, args=(13000800, 3001800, 3002800, 13005805, 3001800, 3000800, 13000801, 0))
    RunCommonEvent(20005801, args=(13000800, 3001800, 3002800, 13005805, 3001800, 13005806))
    RunCommonEvent(20005820, args=(13000800, 3001800, 3, 13000801))
    if FlagDisabled(13000801):
        RunCommonEvent(20001836, args=(13000800, 13005805, 13005806, 13005810, 3002805, 3002806, 13005815))
    else:
        RunCommonEvent(20005831, args=(13000800, 13005805, 13005806, 3002800, 3002805, 3002806, 13005815))
    RunCommonEvent(20005810, args=(13000825, 3001800, 3002800, 10000))


@RestartOnRest(13005825)
def Event_13005825(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13005825"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_1))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_3))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_3))
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_4))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    AND_4.Add(FlagEnabled(flag_1))
    AND_4.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)
    AND_5.Add(FlagEnabled(flag_1))
    AND_5.Add(FlagEnabled(flag_4))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(flag)
    Wait(5.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag)
    Wait(5.0)
    Restart()


@RestartOnRest(13005826)
def Event_13005826(
    _,
    flag: int,
    flag_1: int,
    flag_2: int,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    flag_3: int,
    flag_4: int,
):
    """Event 13005826"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    AND_2.Add(CharacterInsideRegion(character=character, region=region_2))
    AND_2.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_2)
    
    RotateToFaceEntity(character, region, animation=60060, wait_for_completion=True)
    OR_10.Add(CharacterInsideRegion(character=character, region=region))
    OR_11.Add(TimeElapsed(seconds=3.0))
    OR_10.Add(OR_11)
    
    MAIN.Await(OR_10)
    
    RestartIfFinishedConditionTrue(input_condition=OR_11)
    AICommand(character, command_id=-1, command_slot=0)
    AICommand(character, command_id=50, command_slot=3)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=11, command_slot=0)
    ReplanAI(character)
    AND_2.Add(CharacterInsideRegion(character=character, region=region_3))
    AND_2.Add(FlagEnabled(flag_4))
    
    MAIN.Await(AND_2)
    
    RotateToFaceEntity(character, region_1, animation=60060, wait_for_completion=True)
    OR_12.Add(CharacterInsideRegion(character=character, region=region_1))
    OR_13.Add(TimeElapsed(seconds=3.0))
    OR_12.Add(OR_13)
    
    MAIN.Await(OR_12)
    
    RestartIfFinishedConditionTrue(input_condition=OR_13)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()


@RestartOnRest(13005830)
def Event_13005830():
    """Event 13005830"""
    DisableAI(3000830)
    DisableHealthBar(3000830)
    DisableCharacter(3000830)
    DisableSoundEvent(sound_id=3002835)
    if FlagEnabled(13000830):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=13000838)
    AND_1.Add(FlagDisabled(13000830))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002830))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=13000838)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(30000040, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(30000040, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(30000040, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(3000830)
    AND_2.Add(FlagDisabled(13000830))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3002830))
    
    MAIN.Await(AND_2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(3000830)
    EnableAI(3000830)
    SetNetworkUpdateRate(3000830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3000830, name=902090)
    DisableObjectActivation(3001813, obj_act_id=300371)
    SetNetworkConnectedFlagState(flag=13000838, state=FlagSetting.On)


@NeverRestart(13005831)
def Event_13005831():
    """Event 13005831"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(HealthLessThanOrEqual(3000830, value=0.0))
    
    Wait(1.0)
    PlaySoundEffect(3000830, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3000830))
    
    Wait(3.5)
    KillBoss(game_area_param_id=3000830)
    EnableFlag(13000830)
    EnableFlag(9302)
    EnableFlag(6302)
    WaitFrames(frames=1)
    EnableObjectActivation(3001813, obj_act_id=300371)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(13005835)
def Event_13005835():
    """Event 13005835"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000830, tae_event_id=10))
    
    WaitFrames(frames=1)
    End()


@RestartOnRest(13005836)
def Event_13005836():
    """Event 13005836"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000830, tae_event_id=20))
    
    EnableFlag(73000202)
    WaitFrames(frames=1)
    End()


@RestartOnRest(13005837)
def Event_13005837():
    """Event 13005837"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000830, tae_event_id=20))
    
    CreateNPCPart(3000830, npc_part_id=10, part_index=NPCPartType.Part6, part_health=193)


@RestartOnRest(13005838)
def Event_13005838():
    """Event 13005838"""
    if FlagEnabled(13000830):
        return
    AND_1.Add(CharacterHasSpecialEffect(3000830, 5404))
    AND_1.Add(CharacterPartHealthLessThanOrEqual(3000830, npc_part_id=10, value=0))
    AND_1.Add(FlagEnabled(13005837))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3000830, 20000, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    CreateNPCPart(3000830, npc_part_id=10, part_index=NPCPartType.Part6, part_health=193)
    Restart()


@RestartOnRest(13005840)
def Event_13005840():
    """Event 13005840"""
    RunCommonEvent(20005800, args=(13000830, 3001830, 3002831, 13005855, 3001830, 3000830, 0, 3002830))
    RunCommonEvent(20005801, args=(13000830, 3001830, 3002831, 13005855, 3001830, 13005856))
    RunCommonEvent(20005820, args=(13000830, 3001830, 3, 0))
    RunCommonEvent(20001836, args=(13000830, 13005855, 13005856, 13005830, 3002835, 3002836, 13005835))
    RunCommonEvent(20005837, args=(13000830, 3001830, 999.0, 2090, 2090, 13005855, 13005856), arg_types="iifiiii")
    RunCommonEvent(20005810, args=(13000830, 3001830, 3002831, 10000))
    RunCommonEvent(20005810, args=(13000825, 3001890, 3002896, 10000))


@RestartOnRest(13005850)
def Event_13005850():
    """Event 13005850"""
    if FlagEnabled(13000830):
        return
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3002850))
    
    if FlagEnabled(13000830):
        return
    SetBackgroundMusic(True, music_slot=0, entity=3002850, sound_type=SoundType.a_Ambient, sound_id=300000020)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3002850))
    
    SetBackgroundMusic(False, music_slot=0, entity=3002850, sound_type=SoundType.a_Ambient, sound_id=300000020)
    Restart()


@RestartOnRest(13005861)
def Event_13005861():
    """Event 13005861"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(13005862)
    
    MAIN.Await(FailedToCreateSession())
    
    EnableFlag(13005862)
    AND_1.Add(FailedToCreateSession())
    
    MAIN.Await(not AND_1)
    
    DisableFlag(13005862)
    Wait(1.0)
    Restart()


@RestartOnRest(13005880)
def Event_13005880():
    """Event 13005880"""
    GotoIfFlagEnabled(Label.L0, flag=13000885)
    ForceAnimation(3001087, 0, loop=True, unknown2=1.0)
    DisableObject(3001870)
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(13000890))
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3001895, entity=3001896))
    
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(30000020, cutscene_flags=0, player_id=10000, move_to_region=3002880, game_map=HIGH_WALL_OF_LOTHRIC)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        30000020,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002880,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000020, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    RemoveGoodFromPlayer(item=2117, quantity=1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3001087, 10, loop=True, unknown2=1.0)
    EnableObject(3001870)
    RegisterLadder(start_climbing_flag=13000264, stop_climbing_flag=13000265, obj=3001087)
    ForceAnimation(3001896, 2, loop=True, unknown2=1.0)
    EnableFlag(13000885)


@RestartOnRest(13005889)
def Event_13005889():
    """Event 13005889"""
    if FlagEnabled(13000890):
        return
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_1:
        return
    WaitFrames(frames=1)
    
    MAIN.Await(FlagEnabled(13005885))
    
    EnableCharacter(3000899)
    EnableAnimations(3000899)
    EnableAI(3000899)
    ActivateMultiplayerBuffs(3000899)
    EnableFlag(13000896)


@RestartOnRest(13005890)
def Event_13005890():
    """Event 13005890"""
    DisableObject(3001890)
    DisableAI(3000899)
    DisableCharacter(3000899)
    DisableAnimations(3000899)
    DisableSoundEvent(sound_id=3002899)
    DisableSoundEvent(sound_id=3002898)
    ForceAnimation(3001895, 2, loop=True, unknown2=1.0)
    DisableObjectActivation(3001895, obj_act_id=300370)
    CreateObjectVFX(3001360, vfx_id=210, model_point=800030)
    CreateObjectVFX(3001360, vfx_id=212, model_point=800030)
    CreateObjectVFX(3001360, vfx_id=214, model_point=800043)
    CreateObjectVFX(3001361, vfx_id=210, model_point=800030)
    CreateObjectVFX(3001361, vfx_id=212, model_point=800030)
    CreateObjectVFX(3001361, vfx_id=214, model_point=800043)
    CreateObjectVFX(3001362, vfx_id=210, model_point=800030)
    CreateObjectVFX(3001362, vfx_id=212, model_point=800030)
    CreateObjectVFX(3001362, vfx_id=214, model_point=800043)
    CreateObjectVFX(3001363, vfx_id=210, model_point=800030)
    CreateObjectVFX(3001363, vfx_id=212, model_point=800030)
    CreateObjectVFX(3001363, vfx_id=214, model_point=800043)
    DeleteObjectVFX(3001890)
    DeleteObjectVFX(3001899)
    if FlagEnabled(13000890):
        return
    GotoIfFlagEnabled(Label.L1, flag=13000896)
    Move(3000899, destination=3002893, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObject(3001890)
    CreateObjectVFX(3001890, vfx_id=101, model_point=3)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13000881, state=FlagSetting.On)
    AND_1.Add(CharacterDead(3000705))
    AND_1.Add(PlayerHasGood(2117))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002700))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    Wait(1.0)
    DeleteObjectVFX(3001890)
    WaitFrames(frames=1)
    EnableFlag(13004890)
    
    MAIN.Await(FlagEnabled(13005894))
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    NotifyBossBattleStart()
    SkipLinesIfLeavingSession(2)
    EnableObject(3001890)
    CreateObjectVFX(3001890, vfx_id=101, model_point=3)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableObject(3001890)
    CreateObjectVFX(3001890, vfx_id=101, model_point=3)
    EnableCharacter(3000899)
    EnableAnimations(3000899)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3001890, entity=3001890))
    
    RotateToFaceEntity(PLAYER, 3002896, animation=60060, wait_for_completion=True)

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3002895))
    
    EnableFlag(13000880)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    NotifyBossBattleStart()
    BanishInvaders(unknown=0)
    AND_3.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_3:
        return

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfPlayerNotInOwnWorld(Label.L4)
    EnableBossMusic(sound_id=3002899)
    Unknown_2010_07(sound_id=3002898)
    EnableBossHealthBar(3000899, name=905270)
    SetNetworkUpdateRate(3000899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ChangeCamera(normal_camera_id=3000, locked_camera_id=3000)
    SetNetworkUpdateAuthority(3000899, authority_level=UpdateAuthority.Forced)
    SetNetworkConnectedFlagState(flag=13005885, state=FlagSetting.On)

    # --- Label 4 --- #
    DefineLabel(4)


@RestartOnRest(13005891)
def Event_13005891():
    """Event 13005891"""
    if FlagEnabled(13000890):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000899, tae_event_id=10))
    
    EnableBossMusic(sound_id=3002898)


@RestartOnRest(13005892)
def Event_13005892():
    """Event 13005892"""
    if FlagEnabled(13000890):
        return
    CreateNPCPart(3000899, npc_part_id=10, part_index=NPCPartType.Part5, part_health=400)
    
    MAIN.Await(CharacterPartHealthLessThanOrEqual(3000899, npc_part_id=10, value=0))
    
    ForceAnimation(3000899, 20000, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SetNPCPartHealth(3000899, npc_part_id=10, desired_health=400, overwrite_max=True)
    Restart()


@NeverRestart(13005893)
def Event_13005893():
    """Event 13005893"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(13005885)
    if PlayerInOwnWorld():
        return
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(13000881))
    
    GotoIfFlagEnabled(Label.L0, flag=13005894)
    ForceAnimation(3001895, 2, unknown2=1.0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3001895, 0, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(13005885))
    
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(FlagDisabled(13000890))
    AND_1.Add(ActionButtonParamActivated(action_button_id=3001890, entity=3001890))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 3002896, animation=60060, wait_for_completion=True)
    EnableBossMusic(sound_id=3002899)
    EnableBossHealthBar(3000899, name=905270)
    SetNetworkUpdateRate(3000899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ChangeCamera(normal_camera_id=3000, locked_camera_id=3000)
    EnableFlag(13005886)
    EnableFlag(13000896)
    End()


@RestartOnRest(13005895)
def Event_13005895():
    """Event 13005895"""
    if FlagEnabled(13000890):
        return
    
    MAIN.Await(HealthLessThanOrEqual(3000899, value=0.0))
    
    Wait(1.0)
    PlaySoundEffect(3000899, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3000899))
    
    Wait(2.5)
    DisableBossMusic(sound_id=3002899)
    DisableBossMusic(sound_id=3002898)
    DisableBossMusic(sound_id=-1)
    KillBoss(game_area_param_id=3000899)
    ExtinguishBurningObjects()
    DeleteObjectVFX(3001885)
    DeleteObjectVFX(3001886)
    DeleteObjectVFX(3001887)
    DeleteObjectVFX(3001888)
    EnableFlag(13000890)
    EnableFlag(9300)
    EnableFlag(6300)
    DisableObject(3001890)
    DeleteObjectVFX(3001890)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(2.0)
    if FlagDisabled(13000880):
        ForceAnimation(3001895, 1, wait_for_completion=True, unknown2=1.0)
        ForceAnimation(3001895, 2, unknown2=1.0)


@RestartOnRest(13005899)
def Event_13005899():
    """Event 13005899"""
    if FlagEnabled(13000890):
        return
    GotoIfFlagEnabled(Label.L0, flag=13005894)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(13004890))
    
    MAIN.Await(AND_1)
    
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_15:
        return
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        30000010,
        cutscene_flags=CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002897,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        30000010,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002897,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    DeleteObjectVFX(3001360)
    DeleteObjectVFX(3001361)
    DeleteObjectVFX(3001362)
    DeleteObjectVFX(3001363)
    WaitFrames(frames=1)
    ForceAnimation(3001895, 0, unknown2=1.0)
    EnableFlag(13005894)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(3001360)
    DeleteObjectVFX(3001361)
    DeleteObjectVFX(3001362)
    DeleteObjectVFX(3001363)
    ForceAnimation(3001895, 0, unknown2=1.0)
    EnableFlag(13005894)
    End()


@RestartOnRest(13000901)
def Event_13000901(_, obj: int):
    """Event 13000901"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(6079):
        return
    DisableNetworkSync()
    CreateObjectVFX(obj, vfx_id=90, model_point=62)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=4200, entity=obj))
    
    ForceAnimation(PLAYER, 60070, unknown2=1.0)
    DeleteObjectVFX(obj)
    EnableFlag(13000900)


@NeverRestart(13005600)
def Event_13005600(_, character__obj: int, obj: int, obj_1: int):
    """Event 13005600"""
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1435, 1439))
    DisableNetworkConnectedFlagRange(flag_range=(1435, 1439))
    SetNetworkConnectedFlagState(flag=1435, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1435))
    AND_2.Add(FlagEnabled(50006230))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1435, 1439))
    SetNetworkConnectedFlagState(flag=1438, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1420, 1434))
    DisableNetworkConnectedFlagRange(flag_range=(1420, 1434))
    SetNetworkConnectedFlagState(flag=1420, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(711))
    AND_1.Add(FlagEnabled(1435))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1420, 1434))
    SetNetworkConnectedFlagState(flag=1421, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableGravity(character__obj)
    DisableCharacterCollision(character__obj)
    GotoIfFlagEnabled(Label.L0, flag=1420)
    GotoIfFlagEnabled(Label.L1, flag=1421)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj_1)
    GotoIfFlagEnabled(Label.L10, flag=1438)
    ForceAnimation(character__obj, 20, unknown2=1.0)
    Move(character__obj, destination=3002705, destination_type=CoordEntityType.Region, short_move=True)
    EnableObjectInvulnerability(obj)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DropMandatoryTreasure(character__obj)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableGravity(character__obj)
    DisableCharacterCollision(character__obj)
    Move(character__obj, destination=3002710, destination_type=CoordEntityType.Region, short_move=True)
    DisableObject(obj)
    GotoIfFlagEnabled(Label.L10, flag=1438)
    ForceAnimation(character__obj, 30000, unknown2=1.0)
    DisableHealthBar(character__obj)
    EnableImmortality(character__obj)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableObject(obj_1)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DropMandatoryTreasure(character__obj)
    End()


@NeverRestart(13005601)
def Event_13005601(_, flag: int):
    """Event 13005601"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    AwardItemLot(62320, host_only=False)


@NeverRestart(13005602)
def Event_13005602(_, entity: int, flag: int):
    """Event 13005602"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 20001, unknown2=1.0)


@NeverRestart(13005603)
def Event_13005603(_, attacked_entity: int):
    """Event 13005603"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1421))
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableFlag(73000182)
    ForceAnimation(attacked_entity, 20001, unknown2=1.0)


@NeverRestart(13005604)
def Event_13005604():
    """Event 13005604"""
    MAIN.Await(FlagEnabled(1438))
    
    DisableObjectInvulnerability(3001875)


@NeverRestart(13005620)
def Event_13005620(_, character: int):
    """Event 13005620"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1215, 1219))
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1215, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1216))
    AND_1.Add(FlagEnabled(70000062))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1215, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1200, 1214))
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1200, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1215)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000062)
    if FlagEnabled(1215):
        DisableFlag(73000120)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1200)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1216)
    GotoIfFlagEnabled(Label.L2, flag=1218)
    ForceAnimation(character, 90360, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(13005640)
def Event_13005640(_, character: int):
    """Event 13005640"""
    if FlagDisabled(13000830):
        SetCharacterTalkRange(character=character, distance=80.0)
        DisableFlag(73000200)
        DisableFlag(73000201)
        DisableFlag(73000202)

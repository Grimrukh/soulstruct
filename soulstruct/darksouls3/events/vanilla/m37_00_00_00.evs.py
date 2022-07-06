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
    RegisterBonfire(bonfire_flag=13700000, obj=3701950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13700003, obj=3701953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13700004, obj=3701954, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13700005, obj=3701955, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13700007, obj=3701957, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13700008, obj=3701958, reaction_distance=5.0)
    RunCommonEvent(20005500, args=(13700850, 13700001, 3700951, 3701951))
    RunCommonEvent(20005500, args=(13700800, 13700002, 3700952, 3701952))
    RunCommonEvent(20005500, args=(13700249, 13700006, 3700956, 3701956))
    RunCommonEvent(20005780, args=(3701780, 3))
    RunCommonEvent(20005780, args=(3701781, 2))
    RunCommonEvent(20005780, args=(3701783, 2))
    RunCommonEvent(20005780, args=(3701784, 2))
    Event_13705350(0, obj=3701785)
    Event_13705351(0, obj=3701785, model_point=3)
    Event_13700200()
    RunCommonEvent(20005342, args=(13700198, 3700170))
    RunCommonEvent(20005342, args=(13700199, 3700171))
    RunCommonEvent(20005701, args=(13700850, 13704190, 13705190, 3700190, 3702190, 70000022))
    RunCommonEvent(20005720, args=(13704190, 13705190, 13700850, 3700190))
    RunCommonEvent(20005710, args=(13704190, 13705855, 3700190, 3702850, 3702852))
    RunCommonEvent(20005701, args=(13700850, 13704195, 13705195, 3700195, 3702190, 70000023))
    RunCommonEvent(20005720, args=(13704195, 13705195, 13700850, 3700195))
    RunCommonEvent(20005710, args=(13704195, 13705855, 3700195, 3702850, 3702852))
    RunCommonEvent(20005701, args=(13700850, 13704191, 13705191, 3700191, 3702191, 0))
    RunCommonEvent(20005720, args=(13704191, 13705191, 13700850, 3700191))
    RunCommonEvent(20005710, args=(13704191, 13705855, 3700191, 3702850, 3702852))
    RunCommonEvent(20005701, args=(13700850, 13704192, 13705192, 3700192, 3702192, 70000002))
    RunCommonEvent(20005720, args=(13704192, 13705192, 13700800, 3700192))
    RunCommonEvent(20005710, args=(13704192, 13705855, 3700192, 3702850, 3702852))
    RunCommonEvent(
        20005750,
        args=(13700800, 13700193, 13704193, 13705193, 3700193, 3702193, 3702194, 0.0, 70000005),
        arg_types="iiiiiiifi",
    )
    RunCommonEvent(20005721, args=(13704193, 13705193, 13700193, 3700193))
    RunCommonEvent(20005760, args=(13700193, 13704193, 13705193, 3700193))
    RunCommonEvent(20005341, args=(13700193, 3700193, 58500))
    RunCommonEvent(
        20005750,
        args=(13700800, 13700194, 13704194, 13705194, 3700194, 3702195, 3702196, 0.0, 13705282),
        arg_types="iiiiiiifi",
    )
    RunCommonEvent(20005721, args=(13704194, 13705194, 13700194, 3700194))
    RunCommonEvent(20005760, args=(13700194, 13704194, 13705194, 3700194))
    RunCommonEvent(20005341, args=(13700194, 3700194, 57900))
    Event_13705280()
    Event_13705281()
    RunCommonEvent(20005110, args=(3700200, 3702203))
    RunCommonEvent(20005110, args=(3700201, 3702211))
    RunCommonEvent(20005110, args=(3700202, 3702211))
    RunCommonEvent(20005110, args=(3700206, 3702214))
    RunCommonEvent(20005110, args=(3700207, 3702214))
    RunCommonEvent(20005110, args=(3700211, 3702215))
    RunCommonEvent(20005110, args=(3700212, 3702215))
    RunCommonEvent(20005110, args=(3700213, 3702204))
    RunCommonEvent(20005140, args=(3700214, 3702205, 3700213))
    RunCommonEvent(20005120, args=(3700215, 15.0), arg_types="if")
    RunCommonEvent(20005119, args=(3705202, 3702200, 3702201, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3705203, 3702201, 3702202, 0, 0, 0, 0, 0))
    RunCommonEvent(20005110, args=(3700231, 3702215))
    RunCommonEvent(20005119, args=(3700232, 3702232, 3702233, 0, 0, 0, 0, 0))
    RunCommonEvent(20005320, args=(3700233, 3702353, 3704358))
    Event_13705240()
    Event_13705230(0, character=3700240)
    Event_13705230(1, character=3700241)
    Event_13705230(2, character=3700242)
    Event_13705235()
    Event_13705244()
    Event_13705245()
    Event_13705246()
    Event_13705260()
    RunCommonEvent(20005341, args=(13700250, 3700240, 22500000))
    RunCommonEvent(20005340, args=(13700251, 3700241))
    RunCommonEvent(20005340, args=(13700252, 3700242))
    RunCommonEvent(20005110, args=(3700241, 3702248))
    RunCommonEvent(20005110, args=(3700242, 3702248))
    RunCommonEvent(20005110, args=(3700250, 3702213))
    RunCommonEvent(20005110, args=(3700251, 3702213))
    RunCommonEvent(20005200, args=(3700252, 701, 1701, 3702273))
    RunCommonEvent(20005200, args=(3700253, 701, 1701, 3702273))
    RunCommonEvent(20005330, args=(3700250, 3702213, 13705210))
    RunCommonEvent(20005330, args=(3700251, 3702213, 13705211))
    RunCommonEvent(20005330, args=(3700252, 3702273, 13705212))
    RunCommonEvent(20005330, args=(3700253, 3702273, 13705213))
    RunCommonEvent(20005200, args=(3700254, 700, 1700, 3702222))
    RunCommonEvent(20005210, args=(3700255, 701, 1701, 6.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(3700255, 701, 1701, 3702222, 15.0), arg_types="iiiif")
    RunCommonEvent(20005200, args=(3700256, 700, 1700, 3702222))
    RunCommonEvent(20005119, args=(3705270, 3702270, 3702271, 0, 0, 0, 0, 0))
    RunCommonEvent(20005220, args=(3700257, 701, 1701))
    RunCommonEvent(20005220, args=(3700258, 701, 1701))
    RunCommonEvent(20005220, args=(3700259, 701, 1701))
    RunCommonEvent(20005120, args=(3700260, 4.0), arg_types="if")
    RunCommonEvent(20005120, args=(3700261, 7.0), arg_types="if")
    RunCommonEvent(20005220, args=(3700262, 700, 1700))
    RunCommonEvent(20005220, args=(3700263, 700, 1700))
    RunCommonEvent(20005220, args=(3700264, 700, 1700))
    RunCommonEvent(20005210, args=(3700265, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(3700266, 700, 1700, 2.5), arg_types="iiif")
    RunCommonEvent(20005119, args=(3700270, 3702216, 3702217, 0, 0, 0, 0, 0))
    RunCommonEvent(20005200, args=(3700271, 700, 20001, 3702230))
    RunCommonEvent(20005132, args=(3700273, 2.0, 3702320), arg_types="ifi")
    RunCommonEvent(20005213, args=(3700274, 700, 1700, 2.0, 3702320), arg_types="iiifi")
    RunCommonEvent(20005119, args=(3700275, 3702232, 3702233, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3700276, 3702232, 3702233, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3700277, 3702232, 3702233, 0, 0, 0, 0, 0))
    RunCommonEvent(20005200, args=(3700278, 700, 20001, 3702234))
    RunCommonEvent(20005132, args=(3700279, 3.0, 3702218), arg_types="ifi")
    RunCommonEvent(20005200, args=(3700280, 700, 20001, 3702235))
    RunCommonEvent(20005200, args=(3700281, 700, 20001, 3702237))
    RunCommonEvent(20005111, args=(3700282, 3000, 3702219))
    RunCommonEvent(20005120, args=(3700282, 7.0), arg_types="if")
    RunCommonEvent(20005411, args=(3700282, 3700283, 700, 1700, 0.0), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3700282, 3700284, 700, 1700, 0.5), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3700282, 3700285, 700, 1700, 0.0), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3700282, 3700286, 700, 1700, 0.0), arg_types="iiiif")
    RunCommonEvent(20005411, args=(3700282, 3700287, 700, 1700, 0.5), arg_types="iiiif")
    RunCommonEvent(20005120, args=(3700288, 7.0), arg_types="if")
    RunCommonEvent(20005120, args=(3700289, 7.0), arg_types="if")
    RunCommonEvent(20005120, args=(3700290, 7.0), arg_types="if")
    RunCommonEvent(20005120, args=(3700291, 7.0), arg_types="if")
    RunCommonEvent(20005260, args=(3700292, 700, 1700, 3700253))
    RunCommonEvent(20005132, args=(3700293, 2.0, 3702274), arg_types="ifi")
    RunCommonEvent(20005132, args=(3700294, 5.0, 3702275), arg_types="ifi")
    RunCommonEvent(20005213, args=(3700295, 700, 1700, 2.0, 3702357), arg_types="iiifi")
    RunCommonEvent(20005200, args=(3700296, 700, 20001, 3702236))
    RunCommonEvent(20005330, args=(3700297, 3702353, 13705290))
    RunCommonEvent(20005330, args=(3700298, 3702353, 13705291))
    RunCommonEvent(20005132, args=(3700299, 3.0, 3702239), arg_types="ifi")
    RunCommonEvent(20005110, args=(3700300, 3702310))
    RunCommonEvent(20005341, args=(13700310, 3700300, 21507000))
    RunCommonEvent(20005120, args=(3700301, 4.0), arg_types="if")
    RunCommonEvent(20005341, args=(13700311, 3700301, 21507010))
    RunCommonEvent(20005341, args=(13700312, 3700302, 21507020))
    RunCommonEvent(20005341, args=(13700313, 3700303, 21507030))
    RunCommonEvent(20005341, args=(13700314, 3700304, 21507040))
    RunCommonEvent(20005210, args=(3700325, 704, 1704, 8.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(3700326, 705, 1705, 6.0), arg_types="iiif")
    RunCommonEvent(20005430, args=(3700325,))
    RunCommonEvent(20005431, args=(3700325,))
    RunCommonEvent(20005430, args=(3700326,))
    RunCommonEvent(20005431, args=(3700326,))
    RunCommonEvent(20005211, args=(3700330, 700, 1700, 13.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700331, 700, 1700, 13.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700332, 700, 1700, 13.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700333, 700, 1700, 13.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700334, 700, 1700, 13.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700335, 700, 1700, 2.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700336, 700, 1700, 2.0, 0.5), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700337, 700, 1700, 2.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3700338, 700, 1700, 13.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005201, args=(3700339, 700, 1700, 3702315, 0.5), arg_types="iiiif")
    RunCommonEvent(20005201, args=(3700340, 700, 1700, 3702315, 0.0), arg_types="iiiif")
    RunCommonEvent(20005211, args=(3700341, 700, 1700, 4.5, 1.5), arg_types="iiiff")
    RunCommonEvent(20005220, args=(3700350, 701, 1701))
    RunCommonEvent(20005350, args=(3700350, 12303010, 53700975))
    RunCommonEvent(20005206, args=(3700355, 700, 1700, 3702370, 0, 0, 0, 0, 0))
    RunCommonEvent(20005340, args=(13700370, 3700355))
    RunCommonEvent(20005432, args=(3700355,))
    RunCommonEvent(20005119, args=(3700360, 3702360, 3702361, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3700361, 3702362, 3702363, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3700362, 3702361, 3702364, 0, 0, 0, 0, 0))
    RunCommonEvent(20005320, args=(3700363, 3702368, 3704368))
    RunCommonEvent(20005119, args=(3700365, 3702365, 3702366, 0, 0, 0, 0, 0))
    RunCommonEvent(20005132, args=(3700366, 5.0, 3702367), arg_types="ifi")
    RunCommonEvent(20005120, args=(3700368, 11.0), arg_types="if")
    RunCommonEvent(20005114, args=(3700369, 3702365, 2.0), arg_types="iif")
    RunCommonEvent(20005110, args=(3700369, 3702366))
    RunCommonEvent(20005340, args=(13700371, 3700366))
    RunCommonEvent(20005340, args=(13700372, 3700367))
    RunCommonEvent(20005340, args=(13700373, 3700368))
    RunCommonEvent(20005120, args=(3700380, 40.0), arg_types="if")
    RunCommonEvent(20005120, args=(3700381, 40.0), arg_types="if")
    RunCommonEvent(20005120, args=(3700382, 40.0), arg_types="if")
    Event_13705360(0, character=3700390, animation_id=700, animation_id_1=1700, region=3702390)
    Event_13705360(1, character=3700391, animation_id=700, animation_id_1=1700, region=3702391)
    Event_13705360(2, character=3700392, animation_id=700, animation_id_1=1700, region=3702392)
    Event_13705360(3, character=3700393, animation_id=700, animation_id_1=1700, region=3702393)
    Event_13705360(4, character=3700394, animation_id=700, animation_id_1=1700, region=3702394)
    Event_13705360(5, character=3700395, animation_id=700, animation_id_1=1700, region=3702395)
    Event_13705360(6, character=3700396, animation_id=700, animation_id_1=1700, region=3702396)
    Event_13705360(7, character=3700397, animation_id=700, animation_id_1=1700, region=3702397)
    Event_13705360(8, character=3700398, animation_id=700, animation_id_1=1700, region=3702398)
    Event_13705360(9, character=3700399, animation_id=700, animation_id_1=1700, region=3702399)
    RunCommonEvent(20005400, args=(3700400,))
    RunCommonEvent(20000343, args=(13700400, 3700400, 53700950))
    RunCommonEvent(20005211, args=(3700405, 700, 1700, 8.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005110, args=(3700410, 3702381))
    RunCommonEvent(20005110, args=(3700411, 3702355))
    RunCommonEvent(20005110, args=(3700412, 3702252))
    RunCommonEvent(20005119, args=(3700413, 3702232, 3702233, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3700414, 3702232, 3702233, 0, 0, 0, 0, 0))
    Event_13705300(0, 3700450, 3702250, 0.0)
    Event_13705300(1, 3700451, 3702250, 0.5)
    Event_13705300(2, 3700452, 3702250, 1.100000023841858)
    Event_13705330(0, character=3700450, region=3702260)
    Event_13705330(1, character=3700451, region=3702260)
    Event_13705330(2, character=3700452, region=3702260)
    Event_13705300(3, 3700454, 3702251, 0.0)
    Event_13705330(3, character=3700454, region=3702261)
    Event_13705300(4, 3700453, 3702252, 0.0)
    Event_13705300(5, 3700470, 3702252, 0.20000000298023224)
    Event_13705330(4, character=3700453, region=3702262)
    Event_13705330(5, character=3700470, region=3702262)
    Event_13705810()
    Event_13700800()
    Event_13705811()
    Event_13705815()
    Event_13705819()
    Event_13705820()
    Event_13705860()
    Event_13700861()
    Event_13705865()
    Event_13705870()
    Event_13705880()
    Event_13705881()
    Event_13705882()
    Event_13705883()
    Event_13705700(0, character=3700851, character_1=3700850, special_effect=10600, command_id=10)
    Event_13705700(1, character=3700851, character_1=3700850, special_effect=10601, command_id=20)
    Event_13705700(2, character=3700851, character_1=3700850, special_effect=10602, command_id=30)
    Event_13705700(3, character=3700851, character_1=3700850, special_effect=10603, command_id=40)
    Event_13705700(4, character=3700851, character_1=3700850, special_effect=10604, command_id=50)
    Event_13705700(5, character=3700851, character_1=3700850, special_effect=10605, command_id=60)
    Event_13705700(6, character=3700851, character_1=3700850, special_effect=10606, command_id=70)
    Event_13705700(7, character=3700851, character_1=3700850, special_effect=10607, command_id=80)
    Event_13705700(8, character=3700851, character_1=3700850, special_effect=10608, command_id=90)
    Event_13705700(9, character=3700851, character_1=3700850, special_effect=10609, command_id=100)
    Event_13705700(10, character=3700851, character_1=3700850, special_effect=10610, command_id=110)
    Event_13705700(11, character=3700851, character_1=3700850, special_effect=10611, command_id=120)
    Event_13705700(12, character=3700851, character_1=3700850, special_effect=10612, command_id=130)
    Event_13705700(13, character=3700851, character_1=3700850, special_effect=10613, command_id=140)
    Event_13705700(16, character=3700851, character_1=3700850, special_effect=10616, command_id=170)
    Event_13705700(17, character=3700851, character_1=3700850, special_effect=10617, command_id=180)
    Event_13705700(18, character=3700851, character_1=3700850, special_effect=10618, command_id=190)
    Event_13705700(19, character=3700851, character_1=3700850, special_effect=10619, command_id=200)
    Event_13705700(20, character=3700851, character_1=3700850, special_effect=10620, command_id=210)
    Event_13705700(21, character=3700851, character_1=3700850, special_effect=10621, command_id=220)
    Event_13705700(22, character=3700851, character_1=3700850, special_effect=10622, command_id=230)
    Event_13705700(23, character=3700851, character_1=3700850, special_effect=10623, command_id=240)
    Event_13705700(24, character=3700851, character_1=3700850, special_effect=10624, command_id=250)
    Event_13705700(25, character=3700851, character_1=3700850, special_effect=10625, command_id=260)
    Event_13705885()
    Event_13705886()
    Event_13705887()
    Event_13705889()
    RunCommonEvent(20005620, args=(13700410, 13700412, 3701410, 3701411, 3701412, 13701410))
    Event_13705400()
    RunCommonEvent(20005620, args=(13700420, 13700422, 3701420, 3701421, 3701422, 13701420))
    RunCommonEvent(20005628, args=(13700421, 3701422, 3702421))
    if FlagEnabled(13700800):
        ForceAnimation(3701805, 0, loop=True, unknown2=1.0)
        ForceAnimation(3701806, 0, loop=True, unknown2=1.0)
    EnableObjectInvulnerability(3701700)
    Event_13705430()
    Event_13705440()
    Event_13705450()
    Event_13705460()
    Event_13700470()
    Event_13700471()
    Event_13705480()
    Event_13705510(0, flag=13700500, flag_1=13700501, entity=3701500, obj=3701502, obj_1=3701501, flag_2=13701500)
    Event_13705512(0, flag=13700500, entity=3701500, action_button_id=9301, action_button_id_1=9300, flag_1=13701500)
    Event_13705513()
    Event_13705540()
    Event_13705541()
    Event_13705542()
    Event_13705543()
    Event_13705545(0, obj=3701541, region=3702541)
    RunCommonEvent(20005650, args=(13700530, 3701530))
    RunCommonEvent(20005650, args=(13700531, 3701531))
    Event_13705532()
    RunCommonEvent(20005650, args=(13700534, 3701534))
    Event_13705535()
    Event_13705520(0, obj=3701520, entity=3701521)
    Event_13705950(0, 13705900, 3701900, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(1, 13705901, 3701901, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(2, 13705902, 3701902, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(3, 13705903, 3701903, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(4, 13705904, 3701904, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(5, 13705905, 3701905, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(6, 13705906, 3701906, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(7, 13705907, 3701907, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(8, 13705908, 3701908, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(9, 13705909, 3701909, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(10, 13705910, 3701910, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(11, 13705911, 3701911, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(12, 13705912, 3701912, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(13, 13705913, 3701913, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(14, 13705914, 3701914, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(15, 13705915, 3701915, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(16, 13705916, 3701916, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(17, 13705917, 3701917, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(18, 13705918, 3701918, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(19, 13705919, 3701919, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(20, 13705920, 3701920, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(21, 13705921, 3701921, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(22, 13705922, 3701922, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(23, 13705923, 3701923, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(24, 13705924, 3701924, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(25, 13705925, 3701925, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(26, 13705926, 3701926, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(27, 13705927, 3701927, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(28, 13705928, 3701928, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(29, 13705929, 3701929, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    Event_13705950(30, 13705930, 3701930, 11, 11, 837070, 5200, 1.75, 0.0, 0.15000000596046448)
    RunCommonEvent(20005520, args=(13701510, 3701510, 3704510))
    RunCommonEvent(20005520, args=(13701511, 3701511, 3704511))
    RunCommonEvent(20005520, args=(13701512, 3701512, 3704512))
    RunCommonEvent(20005520, args=(13701513, 3701513, 3704513))
    RunCommonEvent(20005520, args=(13701514, 3701514, 3704514))
    RunCommonEvent(20005520, args=(13701515, 3701515, 3704515))
    RunCommonEvent(20005520, args=(13701516, 3701516, 3704516))
    RunCommonEvent(20005520, args=(13701517, 3701517, 3704517))
    RunCommonEvent(20005524, args=(3701565, 13700193))
    RunCommonEvent(20005523, args=(3701560, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3701561, 2), arg_types="iB")
    RunCommonEvent(20005523, args=(3701562, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3701563, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3701564, 2), arg_types="iB")
    RunCommonEvent(20005525, args=(53700840, 3700840, 3701590, 61))
    Event_13705110()
    Event_13700111()
    Event_13705155()
    Event_13700156()
    RunCommonEvent(20005061, args=(8240, 3700725), event_layers=[2])
    RunCommonEvent(20005062, args=(8241, 8242), event_layers=[2])
    Event_13705684(0, 3700725, 90720, event_layers=[2])
    Event_13705157(event_layers=[2])
    RunCommonEvent(
        20005060,
        args=(8200, 8201, 13701162, 13704161, 13705161, 10012030, 9360, 3701160, 30001),
        event_layers=[0, 1],
    )
    RunCommonEvent(20005061, args=(8200, 3700161), event_layers=[3])
    RunCommonEvent(20005062, args=(8201, 8202), event_layers=[3])
    Event_13700163()
    Event_13700165(event_layers=[3])
    RunCommonEvent(
        20005060,
        args=(8260, 8261, 13701172, 13704171, 13705171, 10012031, 9360, 3701170, 30001),
        event_layers=[0, 1],
    )
    Event_13705652(0, 3700707, event_layers=[4])
    RunCommonEvent(
        20005060,
        args=(8260, 8261, 13701173, 13704171, 13705171, 10012031, 9360, 3701175, 30001),
        event_layers=[0, 1],
    )
    Event_13705652(1, 3700712, event_layers=[4])
    Event_13700173()
    Event_13700172(event_layers=[4])
    Event_13700174(event_layers=[0, 1])
    Event_13700175(event_layers=[4])
    RunCommonEvent(20006002, args=(3700700, 1098, 1095, 1099))
    RunCommonEvent(20006005, args=(3700700, 73700115, 73700116, 3702710, 1.0, 91010, 91012, -1), arg_types="iiiifiii")
    RunCommonEvent(20006005, args=(3700700, 73700118, 73700121, 3702710, 1.0, 91010, 91012, -1), arg_types="iiiifiii")
    RunCommonEvent(20006010, args=(73700119, 91013))
    Event_13705624(1, entity=3700700)
    RunCommonEvent(20006030, args=(3701701, 4000, 1, 50610, 50006060, 50006060, 1098))
    RunCommonEvent(20006030, args=(3701701, 4000, 1, 50600, 6750, 6750, 50006060))
    Event_13705621(0, entity=3700700)
    Event_13705641(
        0,
        character=3700705,
        character_1=3700710,
        character_2=3700721,
        command_id=2160,
        obj=3701721,
        character_3=3700706,
        character_4=3700711,
        command_id_1=1901,
        obj_1=3701706,
        vfx_id=3704707,
        vfx_id_1=3704712
    )
    Event_13700642(
        0,
        character=3700705,
        character_1=3700710,
        animation_id=90780,
        character_2=3700720,
        obj=3701720,
        special_effect_id=12400
    )
    Event_13700643(
        0,
        3700705,
        3700710,
        3704707,
        3704712,
        3700720,
        3700721,
        2160,
        3701720,
        3701721,
        3700706,
        3700711,
        1901,
        3701706,
    )
    Event_13705644(
        0,
        entity=3700706,
        entity_1=3700711,
        move_to_region__region=3702706,
        obj=3701706,
        character=3700721,
        animation_id=30003
    )
    Event_13705651(0, character=3700705, character_1=3700710)
    RunCommonEvent(
        20006000,
        args=(3700705, 1356, 1357, 73700180, 0.6499999761581421, 1355, 1359, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3700705, 1356, 1357, 73700180, 3))
    RunCommonEvent(20006002, args=(3700705, 1358, 1355, 1359))
    RunCommonEvent(
        20006000,
        args=(3700710, 1356, 1357, 73700181, 0.6499999761581421, 1355, 1359, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3700710, 1356, 1357, 73700181, 3))
    RunCommonEvent(20006002, args=(3700710, 1358, 1355, 1359))
    RunCommonEvent(20006002, args=(3700720, 1578, 1575, 1579))
    RunCommonEvent(20006002, args=(3700721, 1578, 1575, 1579))
    Event_13705646(0, character=3700720, obj=3701720, special_effect_id=12400)
    Event_13705647(0, character=3700721, animation_id=20007, flag=73700330)
    RunCommonEvent(20006030, args=(3701722, 4000, 1, 53000, 50006300, 50006300, 1566))
    RunCommonEvent(
        20006000,
        args=(3700715, 1396, 1397, 73700240, 0.6499999761581421, 1395, 1399, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3700715, 1396, 1397, 73700240, 3))
    RunCommonEvent(20006002, args=(3700715, 1398, 1395, 1399))
    Event_13705661(0, character=3700715)
    Event_13705662(0, character=3700715)
    Event_13705663(0, character=3700715)
    Event_13700664()
    RunCommonEvent(20006010, args=(73700952, 69003))
    RunCommonEvent(20005780, args=(3701786, 2))
    RunCommonEvent(20005780, args=(3701787, 2))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13700220()
    Event_13705620(0, character=3700700)
    Event_13705640(0, character=3700705, character_1=3700710, animation_id=90780, vfx_id=3704707, vfx_id_1=3704712)
    Event_13705645(
        0,
        character=3700720,
        character_1=3700721,
        obj=3701720,
        special_effect_id=12400,
        command_id=2160,
        obj_1=3701721,
        character_2=3700706,
        character_3=3700711,
        command_id_1=1901,
        obj_2=3701706
    )
    Event_13705650()
    Event_13705660(0, character=3700715)
    Event_13705630(0, character=3700730, command_id=1200)
    DisableAnimations(3700790)
    DisableGravity(3700790)
    DisableCharacterCollision(3700790)
    DisableSoundEvent(sound_id=3704801)
    DisableSoundEvent(sound_id=3704802)
    DisableSoundEvent(sound_id=3704851)
    DisableSoundEvent(sound_id=3704852)
    Event_13705239()
    DisableFlag(13701162)


@RestartOnRest(13705110)
def Event_13705110():
    """Event 13705110"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3702980))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3702981))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3702982))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3702983))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 9010)
    Wait(0.800000011920929)
    Restart()


@RestartOnRest(13700111)
def Event_13700111():
    """Event 13700111"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(3700381))
    
    End()


@NeverRestart(13705155)
def Event_13705155():
    """Event 13705155"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(115))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3702151))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    DisplayStatus(10010690)


@NeverRestart(13700156)
def Event_13700156():
    """Event 13700156"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(8240))
    
    RemoveGoodFromPlayer(item=115, quantity=1)
    AwardItemLot(60930, host_only=False)
    EnableFlag(6312)
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1153, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1155, 1159))
    SetNetworkConnectedFlagState(flag=1158, state=FlagSetting.On)


@NeverRestart(13705157)
def Event_13705157():
    """Event 13705157"""
    CreateObjectVFX(3701156, vfx_id=101, model_point=3)
    CreateObjectVFX(3701157, vfx_id=101, model_point=2)


@RestartOnRest(13700162)
def Event_13700162():
    """Event 13700162"""
    EnableFlag(13700240)


@NeverRestart(13700163)
def Event_13700163():
    """Event 13700163"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13700240))
    AND_1.Add(FlagEnabled(1124))
    AND_1.Add(FlagDisabled(8220))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13701162)


@NeverRestart(13700165)
def Event_13700165():
    """Event 13700165"""
    CreateObjectVFX(3701540, vfx_id=101, model_point=837061)


@NeverRestart(13700172)
def Event_13700172():
    """Event 13700172"""
    EnableFlag(13705805)
    EnableFlag(13705806)


@NeverRestart(13700173)
def Event_13700173():
    """Event 13700173"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1350))
    AND_1.Add(FlagEnabled(1498))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(PlayerGender(gender=Gender.Female))
    SkipLinesIfConditionTrue(2, AND_2)
    EnableFlag(13701172)
    End()
    EnableFlag(13701173)
    End()


@NeverRestart(13700174)
def Event_13700174():
    """Event 13700174"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(8260))
    
    Wait(1.0)
    AddSpecialEffect(PLAYER, 3293)


@NeverRestart(13700175)
def Event_13700175():
    """Event 13700175"""
    MAIN.Await(FlagEnabled(9314))
    
    Wait(1.0)
    AwardItemLot(4550, host_only=True)


@NeverRestart(13700200)
def Event_13700200():
    """Event 13700200"""
    if FlagEnabled(13700201):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(PlayerHasGood(2005))
    
    EnableFlag(13700201)


@NeverRestart(13700220)
def Event_13700220():
    """Event 13700220"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13700410)
    End()


@RestartOnRest(13705230)
def Event_13705230(_, character: int):
    """Event 13705230"""
    CreateNPCPart(character, npc_part_id=10, part_index=NPCPartType.Part1, part_health=176)
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterPartHealthLessThanOrEqual(character, npc_part_id=10, value=0))
    
    MAIN.Await(AND_1)
    
    if CharacterHasSpecialEffect(character=3700240, special_effect=10652):
        return RESTART
    ForceAnimation(character, 20003, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Restart()


@RestartOnRest(13705235)
def Event_13705235():
    """Event 13705235"""
    DisableNetworkSync()
    if FlagEnabled(13700240):
        return
    AND_1.Add(CharacterAlive(3700240))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3704300))
    AND_1.Add(FlagDisabled(13700240))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=5280, locked_camera_id=5280)
    OR_1.Add(CharacterDead(3700240))
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=3704300))
    
    MAIN.Await(OR_1)
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Restart()


@RestartOnRest(13705239)
def Event_13705239():
    """Event 13705239"""
    EnableFlag(13700240, event_layers=[3])
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3700240, authority_level=UpdateAuthority.Forced)
    GotoIfFlagEnabled(Label.L0, flag=13700250)
    GotoIfFlagEnabled(Label.L1, flag=13700240)
    GotoIfFlagEnabled(Label.L2, flag=13705241)
    DisableCharacter(3700240)
    DisableAnimations(3700240)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(3700240)
    EnableAnimations(3700240)
    SetNetworkUpdateRate(3700240, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Move(3700240, destination=3702243, destination_type=CoordEntityType.Region, copy_draw_parent=3700240)
    SetNest(3700240, region=3702245)
    GotoIfFlagEnabled(Label.L3, flag=13705251)
    DisableCharacter(3700240)
    DisableAnimations(3700240)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(3700240)
    EnableAnimations(3700240)
    SetNetworkUpdateRate(3700240, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(3700240)
    DisableAnimations(3700240)
    End()


@RestartOnRest(13705240)
def Event_13705240():
    """Event 13705240"""
    if FlagEnabled(13700250):
        return
    GotoIfFlagEnabled(Label.L1, flag=13700240)
    GotoIfFlagEnabled(Label.L0, flag=13705241)
    OR_15.Add(CharacterHuman(PLAYER))
    OR_15.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_15)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3702240))
    
    MAIN.Await(AND_1)
    
    CancelSpecialEffect(3700240, 10652)
    EnableCharacter(3700240)
    EnableAnimations(3700240)
    Move(3700240, destination=3702246, destination_type=CoordEntityType.Region, copy_draw_parent=3702246)
    SetNetworkUpdateRate(3700240, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3700240)
    SetNest(3700240, region=3702244)
    ForceAnimation(3700240, 20006, wait_for_completion=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13705241, state=FlagSetting.On)
    Wait(3.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_14.Add(CharacterHuman(PLAYER))
    OR_14.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_14)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=3702249))
    OR_3.Add(FlagEnabled(13700240))
    AND_2.Add(OR_3)
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3700240, 10652)
    SetNetworkConnectedFlagState(flag=13705241, state=FlagSetting.Off)
    Wait(3.0)
    SetNetworkUpdateRate(3700240, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=13705251)
    OR_13.Add(CharacterHuman(PLAYER))
    OR_13.Add(CharacterHollow(PLAYER))
    AND_3.Add(OR_13)
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=3702242))
    
    MAIN.Await(AND_3)
    
    CancelSpecialEffect(3700240, 10652)
    EnableCharacter(3700240)
    EnableAnimations(3700240)
    Move(3700240, destination=3702243, destination_type=CoordEntityType.Region, copy_draw_parent=3700240)
    SetNetworkUpdateRate(3700240, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3700240, 20002, wait_for_completion=True, unknown2=1.0)
    EnableAI(3700240)
    ReplanAI(3700240)
    ChangePatrolBehavior(3700240, patrol_information_id=3704390)
    SetNest(3700240, region=3702245)
    SetNetworkConnectedFlagState(flag=13705251, state=FlagSetting.On)
    Wait(3.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    OR_12.Add(CharacterHuman(PLAYER))
    OR_12.Add(CharacterHollow(PLAYER))
    AND_4.Add(OR_12)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3704340))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3704350))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3704361))
    OR_1.Add(FlagEnabled(13700250))
    AND_4.Add(OR_1)
    
    MAIN.Await(AND_4)
    
    Wait(3.0)
    AddSpecialEffect(3700240, 10652)
    SetNetworkConnectedFlagState(flag=13705251, state=FlagSetting.Off)
    Wait(3.0)
    SetNetworkUpdateRate(3700240, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(13705244)
def Event_13705244():
    """Event 13705244"""
    if FlagEnabled(13700250):
        return
    if FlagEnabled(13700240):
        return
    CreateProjectileOwner(entity=3700249)
    AND_1.Add(CharacterAlive(3700240))
    AND_1.Add(FlagEnabled(13705241))
    AND_1.Add(CharacterInsideRegion(character=3700240, region=3704370))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L0, flag=13705247)
    GotoIfFlagDisabled(Label.L1, flag=13705248)
    GotoIfFlagEnabled(Label.L2, flag=13705248)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=3700240, special_effect=10652)
    ShootProjectile(
        owner_entity=3700249,
        source_entity=3704371,
        model_point=-1,
        behavior_id=6110,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    EnableFlag(13705247)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=3700240, special_effect=10652)
    ShootProjectile(
        owner_entity=3700249,
        source_entity=3704371,
        model_point=-1,
        behavior_id=6110,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    EnableFlag(13705248)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=3700240, special_effect=10652)
    ShootProjectile(
        owner_entity=3700249,
        source_entity=3704371,
        model_point=-1,
        behavior_id=6100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    Restart()


@RestartOnRest(13705245)
def Event_13705245():
    """Event 13705245"""
    if FlagEnabled(13700250):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3700240, tae_event_id=100))
    
    ReplanAI(3700240)
    CancelSpecialEffect(3700240, 10652)
    DisableCharacter(3700240)
    DisableAnimations(3700240)
    SetNetworkUpdateRate(3700240, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    DisableAI(3700240)
    Move(3700240, destination=3702246, destination_type=CoordEntityType.Region, copy_draw_parent=3702246)
    Wait(2.0)
    Restart()


@RestartOnRest(13705246)
def Event_13705246():
    """Event 13705246"""
    if FlagEnabled(13700240):
        return
    OR_1.Add(FlagEnabled(13700004))
    OR_15.Add(CharacterHuman(PLAYER))
    OR_15.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_15)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3704321))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableFlag(13700240)
    AddSpecialEffect(3700240, 10652)


@RestartOnRest(13705260)
def Event_13705260():
    """Event 13705260"""
    if FlagEnabled(53700990):
        return
    AND_1.Add(CharacterDead(3700241))
    AND_1.Add(CharacterDead(3700242))
    
    MAIN.Await(AND_1)
    
    if PlayerNotInOwnWorld():
        return
    EnableFlag(13700249)
    AwardItemLot(22501010, host_only=True)
    End()


@RestartOnRest(13705280)
def Event_13705280():
    """Event 13705280"""
    GotoIfFlagDisabled(Label.L1, flag=70000004)
    GotoIfFlagEnabled(Label.L0, flag=13700193)
    GotoIfFlagEnabled(Label.L1, flag=70000005)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13705282)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(13705282)
    End()


@RestartOnRest(13705281)
def Event_13705281():
    """Event 13705281"""
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 70000004))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 70000005))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 13700193))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagDisabled(Label.L1, flag=70000004)
    GotoIfFlagEnabled(Label.L0, flag=13700193)
    GotoIfFlagEnabled(Label.L1, flag=70000005)
    EnableFlag(13705282)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13705282)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(13705282)
    Restart()


@RestartOnRest(13705300)
def Event_13705300(_, character: int, region: int, seconds: float):
    """Event 13705300"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    Wait(seconds)
    EnableAI(character)


@RestartOnRest(13705330)
def Event_13705330(_, character: int, region: int):
    """Event 13705330"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)


@RestartOnRest(13705350)
def Event_13705350(_, obj: int):
    """Event 13705350"""
    DisableNetworkSync()
    DisableObject(obj)
    OR_1.Add(TryingToJoinSession())
    OR_1.Add(TryingToCreateSession())
    
    MAIN.Await(OR_1)
    
    EnableObject(obj)
    OR_2.Add(TryingToJoinSession())
    OR_2.Add(TryingToCreateSession())
    
    MAIN.Await(not OR_2)
    
    Restart()


@RestartOnRest(13705351)
def Event_13705351(_, obj: int, model_point: int):
    """Event 13705351"""
    DisableNetworkSync()
    DeleteObjectVFX(obj)
    OR_1.Add(TryingToJoinSession())
    OR_1.Add(TryingToCreateSession())
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj, radius=7.0))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    
    MAIN.Await(AND_2)
    
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    OR_3.Add(TryingToCreateSession())
    OR_3.Add(TryingToJoinSession())
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj, radius=7.0))
    AND_4.Add(OR_3)
    AND_4.Add(AND_3)
    
    MAIN.Await(not AND_4)
    
    Restart()


@RestartOnRest(13705360)
def Event_13705360(_, character: int, animation_id: int, animation_id_1: int, region: int):
    """Event 13705360"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableGravity(character)
    AddSpecialEffect(character, 4050)
    AddSpecialEffect(character, 4070)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(13705400)
def Event_13705400():
    """Event 13705400"""
    RunCommonEvent(
        20005621,
        args=(13700410, 13700412, 3701410, 3701411, 3704411, 3701412, 3704412, 3702411, 3702412, 13701410, 13704410, 0),
    )
    RunCommonEvent(
        20005621,
        args=(
            13700420,
            13700422,
            3701420,
            3701421,
            3704421,
            3701422,
            3704422,
            3702421,
            3702422,
            13701420,
            13704420,
            13700421,
        ),
    )


@NeverRestart(13705430)
def Event_13705430():
    """Event 13705430"""
    RunCommonEvent(20005610, args=(13700430, 3702431, 3702432))
    RunCommonEvent(20005611, args=(13700430, 3703430, 3701430, 370301))


@NeverRestart(13705440)
def Event_13705440():
    """Event 13705440"""
    RunCommonEvent(20005610, args=(13700440, 3702441, 3702442))
    RunCommonEvent(20005611, args=(13700440, 3703440, 3701440, 370301))


@NeverRestart(13705450)
def Event_13705450():
    """Event 13705450"""
    RunCommonEvent(20005610, args=(13700450, 3702451, 3702452))
    RunCommonEvent(20005611, args=(13700450, 3703450, 3701450, 370301))


@NeverRestart(13705460)
def Event_13705460():
    """Event 13705460"""
    RunCommonEvent(20005614, args=(3701460, 63700460))


@RestartOnRest(13700470)
def Event_13700470():
    """Event 13700470"""
    GotoIfFlagEnabled(Label.L0, flag=13700472)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=3701000, entity=3701471))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13700472)
    Move(PLAYER, destination=3701471, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 60231, unknown2=1.0)
    ForceAnimation(3701471, 0, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(3701470, 1, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(3701471, obj_act_id=-1)
    EndOfAnimation(obj=3701471, animation_id=0)
    EndOfAnimation(obj=3701470, animation_id=1)


@RestartOnRest(13700471)
def Event_13700471():
    """Event 13700471"""
    DisableNetworkSync()
    if FlagEnabled(13700472):
        return
    AND_1.Add(FlagDisabled(13700470))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=3701470))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010160)
    Restart()


@NeverRestart(13705480)
def Event_13705480():
    """Event 13705480"""
    RegisterLadder(start_climbing_flag=13700480, stop_climbing_flag=13700481, obj=3701480)
    RegisterLadder(start_climbing_flag=13700482, stop_climbing_flag=13700483, obj=3701482)
    RegisterLadder(start_climbing_flag=13701484, stop_climbing_flag=13701485, obj=3701484)
    RegisterLadder(start_climbing_flag=13701486, stop_climbing_flag=13701487, obj=3701486)


@NeverRestart(13705510)
def Event_13705510(_, flag: int, flag_1: int, entity: int, obj: int, obj_1: int, flag_2: int):
    """Event 13705510"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(flag_2)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    ForceAnimation(entity, 20, skip_transition=True, unknown2=1.0)
    DisableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity, 10, skip_transition=True, unknown2=1.0)
    EnableFlag(flag_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    End()


@NeverRestart(13705511)
def Event_13705511(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    obj_1: int,
    obj_act_id: int,
    obj_2: int,
    obj_act_id_1: int,
    flag_2: int,
    flag_3: int,
):
    """Event 13705511"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObjectActivation(obj_2, obj_act_id=-1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_2.Add(FlagEnabled(flag))
    OR_3.Add(ActionButtonParamActivated(action_button_id=9300, entity=obj))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(OR_3)
    
    MAIN.Await(OR_4)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    SkipLinesIfFinishedConditionTrue(3, input_condition=OR_2)
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 60231, unknown2=1.0)
    ForceAnimation(obj, 221, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.On)
    ForceAnimation(obj, 221, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.Off)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(ObjectBackreadEnabled(obj=obj))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.Off)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    OR_5.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_6.Add(FlagDisabled(flag))
    OR_7.Add(ActionButtonParamActivated(action_button_id=9301, entity=obj))
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    OR_8.Add(OR_7)
    
    MAIN.Await(OR_8)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L3, flag=flag_3)
    SkipLinesIfFinishedConditionTrue(3, input_condition=OR_6)
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 60230, unknown2=1.0)
    ForceAnimation(obj, 212, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.On)
    ForceAnimation(obj, 212, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.Off)

    # --- Label 4 --- #
    DefineLabel(4)
    AND_2.Add(ObjectBackreadEnabled(obj=obj))
    
    MAIN.Await(AND_2)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.Off)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@RestartOnRest(13705512)
def Event_13705512(_, flag: int, entity: int, action_button_id: int, action_button_id_1: int, flag_1: int):
    """Event 13705512"""
    DisableNetworkSync()
    
    MAIN.Await(FlagDisabled(flag_1))
    
    GotoIfFlagEnabled(Label.L0, flag=flag)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(flag):
        DisplayDialog(text=10010170, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(ActionButtonParamActivated(action_button_id=action_button_id_1, entity=entity))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag):
        DisplayDialog(text=10010170, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(13705513)
def Event_13705513():
    """Event 13705513"""
    Event_13705511(0, 13700500, 13700501, 3701500, 3701502, 3704502, 3701501, 3704501, 13701500, 13704500)


@NeverRestart(13705520)
def Event_13705520(_, obj: int, entity: int):
    """Event 13705520"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    CreateObjectVFX(obj, vfx_id=200, model_point=831023)
    CreateObjectVFX(obj, vfx_id=200, model_point=60)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9600, entity=entity))
    
    ForceAnimation(PLAYER, 60070, unknown2=1.0)
    Wait(0.20000000298023224)
    CreateTemporaryVFX(vfx_id=301002, anchor_entity=PLAYER, model_point=220, anchor_type=CoordEntityType.Character)
    PlaySoundEffect(PLAYER, 999999988, sound_type=SoundType.c_CharacterMotion)
    AddSpecialEffect(PLAYER, 2005)
    DeleteObjectVFX(obj)


@NeverRestart(13705532)
def Event_13705532():
    """Event 13705532"""
    GotoIfFlagEnabled(Label.L0, flag=13700532)
    ForceAnimation(3701533, 0, loop=True, unknown2=1.0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AttackedWithDamageType(attacked_entity=3701532, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13700532)
    ForceAnimation(3701532, 1, unknown2=1.0)
    ForceAnimation(3701533, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(3701532)
    EndOfAnimation(obj=3701533, animation_id=1)


@NeverRestart(13705535)
def Event_13705535():
    """Event 13705535"""
    GotoIfFlagEnabled(Label.L0, flag=13700535)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(AttackedWithDamageType(attacked_entity=3701535, attacker=PLAYER))
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(1564, 1565)))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(13700535)
    ForceAnimation(3701535, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(3701535)


@NeverRestart(13705540)
def Event_13705540():
    """Event 13705540"""
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=13700540)
    EnableObject(3701540)
    
    MAIN.Await(PlayerHasGood(2005))
    
    EnableFlag(13700540)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(3701540)


@NeverRestart(13705541)
def Event_13705541():
    """Event 13705541"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13700540):
        return
    AND_1.Add(ActionButtonParamActivated(action_button_id=9310, entity=3701540))
    IfPlayerDoesNotHaveGood(AND_1, 2005)
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10012005, anchor_entity=3701540, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13705542)
def Event_13705542():
    """Event 13705542"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3702540))
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    AND_1.Add(FlagEnabled(13700540))
    
    MAIN.Await(AND_1)
    
    CreateTemporaryVFX(vfx_id=837060, anchor_entity=3701540, model_point=101, anchor_type=CoordEntityType.Object)
    Wait(1.0)
    Restart()


@NeverRestart(13705543)
def Event_13705543():
    """Event 13705543"""
    DisableNetworkSync()
    DeleteObjectVFX(3701540)
    AND_1.Add(EntityWithinDistance(entity=3701540, other_entity=PLAYER, radius=15.0))
    CreateObjectVFX(3701540, vfx_id=101, model_point=837061)
    
    MAIN.Await(EntityBeyondDistance(entity=3701540, other_entity=PLAYER, radius=18.0))
    
    DeleteObjectVFX(3701540)
    Restart()


@RestartOnRest(13705545)
def Event_13705545(_, obj: int, region: int):
    """Event 13705545"""
    DisableNetworkSync()
    DisableObject(obj)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    EnableObject(obj)
    ForceAnimation(obj, 2, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(obj, 0, unknown2=1.0)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(13705700)
def Event_13705700(_, character: int, character_1: int, special_effect: int, command_id: int):
    """Event 13705700"""
    if FlagEnabled(13700850):
        return
    AND_1.Add(CharacterHasSpecialEffect(character_1, 10636))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    
    MAIN.Await(AND_1)
    
    AICommand(character_1, command_id=command_id, command_slot=0)
    
    MAIN.Await(CharacterHasSpecialEffect(character_1, 5027))
    
    AICommand(3700850, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(13700800)
def Event_13700800():
    """Event 13700800"""
    if FlagEnabled(13700800):
        return
    
    MAIN.Await(HealthLessThanOrEqual(3700800, value=0.0))
    
    Wait(1.0)
    PlaySoundEffect(3700800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3700800))
    
    Wait(3.5)
    HandleBossDefeatAndDisplayBanner(boss=3700800, banner=BannerType.UnknownBossDefeat)
    EnableFlag(13700800)
    EnableFlag(9314)
    EnableFlag(6314)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableFlag(8260, event_layers=[4])
    Wait(4.0)
    ForceAnimation(3701805, 0, loop=True, unknown2=1.0)
    ForceAnimation(3701806, 0, loop=True, unknown2=1.0)


@RestartOnRest(13705810)
def Event_13705810():
    """Event 13705810"""
    GotoIfFlagDisabled(Label.L0, flag=13700800)
    DisableCharacter(3700800)
    Kill(3700800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3700800)
    AND_1.Add(FlagEnabled(13705805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3702800, event_layers=[0, 1]))
    AND_1.Add(CharacterInsideRegion(character=3700707, region=3702800, event_layers=[4]))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=13700801)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(3700800)
    SetNetworkUpdateRate(3700800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3700800)
    DisableHealthBar(3700800, event_layers=[4])
    
    MAIN.Await(FlagEnabled(13705687, event_layers=[4]))
    
    EnableBossHealthBar(3700800, name=905150)
    EnableFlag(13700801)


@RestartOnRest(13705811)
def Event_13705811():
    """Event 13705811"""
    DisableNetworkSync()
    if FlagEnabled(13700800):
        return
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    
    MAIN.Await(FlagEnabled(13705805))
    
    SkipLines(1)
    
    MAIN.Await(FlagEnabled(13705806))
    
    ChangeCamera(normal_camera_id=5150, locked_camera_id=5150)
    OR_1.Add(EntityWithinDistance(entity=3700800, other_entity=PLAYER, radius=9.0))
    OR_1.Add(FlagEnabled(13700800))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L0, flag=13700800)
    ChangeCamera(normal_camera_id=5151, locked_camera_id=5151)
    Wait(0.5)
    OR_2.Add(EntityBeyondDistance(entity=3700800, other_entity=PLAYER, radius=16.0))
    OR_2.Add(FlagEnabled(13700800))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L0, flag=13700800)
    ChangeCamera(normal_camera_id=5150, locked_camera_id=5150)
    Wait(0.5)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(0.5)
    End()


@RestartOnRest(13705815)
def Event_13705815():
    """Event 13705815"""
    if FlagEnabled(13700800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3700800, tae_event_id=20))
    
    EnableFlag(13705815)
    Restart()


@RestartOnRest(13705819)
def Event_13705819():
    """Event 13705819"""
    if FlagEnabled(13700800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3700800, tae_event_id=10))
    
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=3702810)
    GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=3702811)
    GotoIfCharacterInsideRegion(Label.L3, character=PLAYER, region=3702812)
    GotoIfCharacterInsideRegion(Label.L4, character=PLAYER, region=3702813)

    # --- Label 0 --- #
    DefineLabel(0)
    Move(3700800, destination=3702824, destination_type=CoordEntityType.Region, copy_draw_parent=3700800)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(3700800, destination=3702820, destination_type=CoordEntityType.Region, copy_draw_parent=3700800)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(3700800, destination=3702821, destination_type=CoordEntityType.Region, copy_draw_parent=3700800)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(3700800, destination=3702822, destination_type=CoordEntityType.Region, copy_draw_parent=3700800)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    Move(3700800, destination=3702823, destination_type=CoordEntityType.Region, copy_draw_parent=3700800)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(13705820)
def Event_13705820():
    """Event 13705820"""
    RunCommonEvent(20005800, args=(13700800, 3701800, 3702800, 13705805, 3701800, 3700800, 0, 0))
    RunCommonEvent(20005801, args=(13700800, 3701800, 3702800, 13705805, 3701800, 13705806))
    RunCommonEvent(20005820, args=(13700800, 3701800, 3, 0))
    RunCommonEvent(20005820, args=(13700800, 3701801, 3, 0))
    RunCommonEvent(20005820, args=(13700800, 3701802, 2, 0))
    RunCommonEvent(
        20005831,
        args=(13700800, 13705805, 13705806, 3702801, 3704801, 3704802, 13705815),
        event_layers=[0, 1],
    )
    RunCommonEvent(
        20005831,
        args=(13700800, 13705687, 13705687, 3702801, 3704801, 3704802, 13705815),
        event_layers=[4],
    )
    RunCommonEvent(20005810, args=(13700800, 3701800, 3702800, 10000))


@RestartOnRest(13700861)
def Event_13700861():
    """Event 13700861"""
    if FlagEnabled(13700850):
        return
    
    MAIN.Await(HealthLessThanOrEqual(3700850, value=0.0))
    
    Kill(3700851)
    Wait(1.0)
    PlaySoundEffect(3700850, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3700850))
    
    Wait(3.5)
    KillBoss(game_area_param_id=3700850)
    EnableFlag(13700850)
    EnableFlag(9313)
    EnableFlag(6313)


@RestartOnRest(13705860)
def Event_13705860():
    """Event 13705860"""
    GotoIfFlagDisabled(Label.L0, flag=13700850)
    DisableCharacter(3700850)
    DisableCharacter(3700851)
    Kill(3700850)
    Kill(3700851)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3700850)
    AND_1.Add(FlagEnabled(13705855))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3702850))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=13700851)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(3700850)
    SetNetworkUpdateRate(3700850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3700851, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3700850)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3700850, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3700851, authority_level=UpdateAuthority.Forced)
    EnableBossHealthBar(3700850, name=905140)
    EnableFlag(13700851)


@RestartOnRest(13705865)
def Event_13705865():
    """Event 13705865"""
    if FlagEnabled(13700850):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3700850, tae_event_id=500))
    
    EnableFlag(13705865)
    End()


@RestartOnRest(13705870)
def Event_13705870():
    """Event 13705870"""
    RunCommonEvent(20005800, args=(13700850, 3701850, 3702850, 13705855, 3701850, 3705850, 0, 0))
    RunCommonEvent(20005801, args=(13700850, 3701850, 3702850, 13705855, 3701850, 13705856))
    RunCommonEvent(20005820, args=(13700850, 3701850, 4, 0))
    RunCommonEvent(20005820, args=(13700850, 3701851, 2, 0))
    RunCommonEvent(20005831, args=(13700850, 13705855, 13705856, 3702851, 3704851, 3704852, 13705865))
    RunCommonEvent(20005810, args=(13700850, 3701850, 3702850, 10000))


@NeverRestart(13705880)
def Event_13705880():
    """Event 13705880"""
    if FlagEnabled(13700850):
        return
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3700850, 10636))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3700850, 10637))
    AND_1.Add(CharacterHasTAEEvent(3700850, tae_event_id=10))
    AND_1.Add(CharacterDrawGroupDisabled(character=3700850))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableImmortality(3700851)
    EnableGravity(3700851)
    Move(
        3700851,
        destination=3700850,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=3700850,
    )
    WaitFrames(frames=5)
    AddSpecialEffect(3700850, 10636)
    EnableCharacter(3700851)
    ForceAnimation(3700851, 3039, unknown2=1.0)
    SetLockOnPoint(character=3700851, lock_on_model_point=220, state=True)
    EnableHealthBar(3700851)
    ReplanAI(3700851)
    AICommand(3700851, command_id=-1, command_slot=0)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(13705881)
def Event_13705881():
    """Event 13705881"""
    if FlagEnabled(13700850):
        return
    SetCharacterEventTarget(3700850, region=3700851)
    DisableCharacter(3700851)
    SetLockOnPoint(character=3700851, lock_on_model_point=220, state=False)
    SetNetworkUpdateRate(3700851, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    DisableHealthBar(3700851)
    EnableImmortality(3700851)


@NeverRestart(13705882)
def Event_13705882():
    """Event 13705882"""
    if FlagEnabled(13700850):
        return
    AND_1.Add(CharacterHasSpecialEffect(3700850, 10636))
    AND_1.Add(HealthValueEqual(3700851, value=1))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    CancelSpecialEffect(3700850, 10636)
    AddSpecialEffect(3700850, 10637)
    ReplanAI(3700850)
    ForceAnimation(3700851, 20000, wait_for_completion=True, unknown2=1.0)
    DisableCharacter(3700851)
    SetLockOnPoint(character=3700851, lock_on_model_point=220, state=False)
    DisableHealthBar(3700851)
    AddSpecialEffect(3700851, 10639)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(13705883)
def Event_13705883():
    """Event 13705883"""
    if FlagEnabled(13700850):
        return
    OR_1.Add(CharacterHasSpecialEffect(3700850, 10634))
    OR_1.Add(CharacterHasSpecialEffect(3700851, 5028))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(3700850, 10636))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3700851, 5029))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3700851, 10633)
    WaitFrames(frames=5)
    Restart()


@NeverRestart(13705885)
def Event_13705885():
    """Event 13705885"""
    if FlagEnabled(13700850):
        return
    
    MAIN.Await(HealthLessThanOrEqual(3700850, value=0.0))
    
    DisableImmortality(3700851)
    Kill(3700851)


@NeverRestart(13705886)
def Event_13705886():
    """Event 13705886"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagEnabled(13700850):
        return
    
    MAIN.Await(HasAIStatus(3700850, ai_status=AIStatusType.Battle))
    
    Wait(3.0)
    AddSpecialEffect(3700850, 10640)
    AddSpecialEffect(3700850, 10641)


@NeverRestart(13705887)
def Event_13705887():
    """Event 13705887"""
    if FlagEnabled(13700850):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterHasSpecialEffect(3700850, 10636))
    
    OR_1.Add(CharacterHasSpecialEffect(3700851, 5029))
    OR_1.Add(CharacterHasSpecialEffect(3700851, 5027))
    OR_1.Add(CharacterHasSpecialEffect(3700851, 5030))
    OR_1.Add(CharacterHasSpecialEffect(3700851, 5031))
    OR_1.Add(CharacterHasSpecialEffect(3700851, 5032))
    OR_1.Add(CharacterHasSpecialEffect(3700851, 5033))
    OR_2.Add(OR_1)
    OR_2.Add(TimeElapsed(seconds=5.0))
    OR_2.Add(CharacterHasTAEEvent(3700851, tae_event_id=300))
    AND_1.Add(OR_2)
    AND_1.Add(FlagDisabled(13705888))
    
    MAIN.Await(AND_1)
    
    GotoIfFinishedConditionTrue(Label.L20, input_condition=OR_1)
    SetNetworkConnectedFlagState(flag=13705888, state=FlagSetting.On)

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(3.0)
    Restart()


@NeverRestart(13705889)
def Event_13705889():
    """Event 13705889"""
    if FlagEnabled(13700850):
        return
    
    MAIN.Await(FlagEnabled(13705888))
    
    Move(
        3700851,
        destination=3700850,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=3700850,
    )
    ForceAnimation(3700851, 3038, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13705888, state=FlagSetting.Off)
    Wait(1.0)
    Restart()


@RestartOnRest(13705950)
def Event_13705950(
    _,
    obj_flag: int,
    obj: int,
    model_point: int,
    model_point_1: int,
    vfx_id: int,
    behavior_param_id: int,
    radius: float,
    life: float,
    repetition_time: float,
):
    """Event 13705950"""
    WaitFrames(frames=1)
    if ObjectDestroyed(obj):
        return
    
    MAIN.Await(ObjectDestroyed(obj))
    
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=vfx_id, anchor_entity=obj, model_point=model_point, anchor_type=CoordEntityType.Object)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=model_point_1,
        behavior_param_id=behavior_param_id,
        target_type=DamageTargetType.Character,
        radius=radius,
        life=life,
        repetition_time=repetition_time,
    )
    Wait(10.0)
    RemoveObjectFlag(obj_flag=obj_flag)


@NeverRestart(13705620)
def Event_13705620(_, character: int):
    """Event 13705620"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    DisableFlag(73700115)
    DisableFlag(73700118)
    SkipLinesIfFlagRangeAnyEnabled(2, (1080, 1099))
    SetNetworkConnectedFlagState(flag=1080, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=1095, state=FlagSetting.On)
    DisableFlagRange((73700115, 73700116))
    DisableFlag(73700118)
    DisableFlag(73700121)
    DisableFlagRange((73700122, 73700123))

    # --- Label 10 --- #
    DefineLabel(10)
    DisableGravity(character)
    DisableCharacterCollision(character)
    GotoIfFlagEnabled(Label.L0, flag=1080)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L10, flag=1098)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@RestartOnRest(13705621)
def Event_13705621(_, entity: int):
    """Event 13705621"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(73700110)
    
    MAIN.Await(FlagEnabled(73700110))
    
    ForceAnimation(entity, 20001, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    EnableFlag(73700111)
    
    MAIN.Await(FlagDisabled(73700110))
    
    ForceAnimation(entity, 20002, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    EnableFlag(73700112)
    Restart()


@RestartOnRest(13705622)
def Event_13705622(_, region: int, flag: int, flag_1: int, target_entity: int, animation: int, animation_id: int):
    """Event 13705622"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, region, animation=69070)
    WaitFrames(frames=1)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 150))
    OR_1.Add(AND_2)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FramesElapsed(frames=89))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_2)
    DisableFlag(flag)
    Restart()
    SkipLinesIfFinishedConditionFalse(3, input_condition=OR_2)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    DisableFlag(flag)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    RotateToFaceEntity(PLAYER, target_entity, animation=animation, wait_for_completion=True)
    EnableFlag(flag_1)
    OR_3.Add(FlagDisabled(flag))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 150))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_3)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(13705624)
def Event_13705624(_, entity: int):
    """Event 13705624"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(73700123)
    
    MAIN.Await(FlagEnabled(73700122))
    
    ForceAnimation(entity, 20003, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    EnableFlag(73700123)
    
    MAIN.Await(FlagDisabled(73700122))
    
    ForceAnimation(entity, 20004, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Restart()


@NeverRestart(13705630)
def Event_13705630(_, character: int, command_id: int):
    """Event 13705630"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1215, 1219))
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1215, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1200, 1214))
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1200, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1215)
    AND_4.Add(FlagEnabled(1203))
    AND_4.Add(FlagEnabled(74000306))
    SkipLinesIfConditionFalse(3, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1204, state=FlagSetting.On)
    EnableFlag(70000151)
    AND_5.Add(FlagEnabled(1204))
    AND_5.Add(FlagEnabled(74000318))
    AND_5.Add(FlagDisabled(1385))
    AND_5.Add(FlagDisabled(1366))
    SkipLinesIfConditionFalse(5, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1205, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1218, state=FlagSetting.On)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1205)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EzstateAIRequest(character, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(13705640)
def Event_13705640(_, character: int, character_1: int, animation_id: int, vfx_id: int, vfx_id_1: int):
    """Event 13705640"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1355, 1359))
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1355, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1356))
    AND_1.Add(FlagEnabled(70000069))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1355, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1340, 1354))
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1340, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1355)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000069)
    if FlagEnabled(1355):
        DisableFlag(73700170)
    AND_2.Add(FlagEnabled(1347))
    AND_2.Add(FlagEnabled(1355))
    AND_2.Add(FlagEnabled(73700150))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(13700651)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L6, flag=1347)
    GotoIfFlagEnabled(Label.L7, flag=1348)
    GotoIfFlagEnabled(Label.L8, flag=1349)
    GotoIfFlagRangeAnyEnabled(Label.L9, flag_range=(1350, 1353))
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DeleteVFX(vfx_id, erase_root_only=False)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DeleteVFX(vfx_id, erase_root_only=False)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    if FlagEnabled(13700651):
        DisableCharacter(character)
        DisableBackread(character)
        DisableCharacter(character_1)
        DisableBackread(character_1)
        End()
    GotoIfFlagEnabled(Label.L16, flag=1356)
    GotoIfFlagEnabled(Label.L18, flag=1358)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    ForceAnimation(character_1, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 7 --- #
    DefineLabel(7)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DeleteVFX(vfx_id, erase_root_only=False)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    End()

    # --- Label 8 --- #
    DefineLabel(8)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DeleteVFX(vfx_id, erase_root_only=False)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()


@NeverRestart(13705641)
def Event_13705641(
    _,
    character: int,
    character_1: int,
    character_2: int,
    command_id: int,
    obj: int,
    character_3: int,
    character_4: int,
    command_id_1: int,
    obj_1: int,
    vfx_id: int,
    vfx_id_1: int,
):
    """Event 13705641"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1347))
    AND_1.Add(FlagEnabled(1355))
    AND_1.Add(FlagEnabled(73700150))
    AND_1.Add(FlagEnabled(9313))
    if not AND_1:
        return
    AND_2.Add(FlagEnabled(1347))
    AND_2.Add(FlagEnabled(1562))
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(1041, 1043)))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1348, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1563, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1347))
    AND_3.Add(FlagEnabled(1562))
    AND_3.Add(FlagRangeAllDisabled(flag_range=(1041, 1043)))
    SkipLinesIfConditionFalse(8, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1348, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1358, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1566, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1575, 1579))
    SetNetworkConnectedFlagState(flag=1578, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1347))
    AND_4.Add(FlagEnabled(1561))
    AND_4.Add(FlagEnabled(1578))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1350, state=FlagSetting.On)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L0, flag=1348)
    GotoIfFlagEnabled(Label.L2, flag=1350)
    Goto(Label.L15)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    Goto(Label.L15)

    # --- Label 20 --- #
    DefineLabel(20)
    Goto(Label.L15)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    CreateVFX(vfx_id)
    Goto(Label.L15)

    # --- Label 20 --- #
    DefineLabel(20)
    CreateVFX(vfx_id_1)
    Goto(Label.L15)

    # --- Label 15 --- #
    DefineLabel(15)
    GotoIfFlagEnabled(Label.L4, flag=1563)
    GotoIfFlagEnabled(Label.L5, flag=1566)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    EzstateAIRequest(character_2, command_id=command_id, command_slot=1)
    EnableObject(obj)
    EnableObject(obj_1)
    GotoIfFlagDisabled(Label.L10, flag=9013)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    EzstateAIRequest(character_3, command_id=command_id_1, command_slot=1)
    DropMandatoryTreasure(character_3)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character_4)
    EnableBackread(character_4)
    EzstateAIRequest(character_4, command_id=command_id_1, command_slot=1)
    DropMandatoryTreasure(character_4)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@NeverRestart(13700642)
def Event_13700642(
    _,
    character: int,
    character_1: int,
    animation_id: int,
    character_2: int,
    obj: int,
    special_effect_id: int,
):
    """Event 13700642"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1347))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L10, flag=9013)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, animation_id, loop=True, skip_transition=True, unknown2=1.0)

    # --- Label 20 --- #
    DefineLabel(20)
    if FlagDisabled(1561):
        return
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableCharacter(character_2)
    EnableBackread(character_2)
    EnableImmortality(character_2)
    EnableObject(obj)
    AddSpecialEffect(character_2, special_effect_id)
    End()


@NeverRestart(13700643)
def Event_13700643(
    _,
    character: int,
    character_1: int,
    vfx_id: int,
    vfx_id_1: int,
    character_2: int,
    character_3: int,
    command_id: int,
    obj: int,
    obj_1: int,
    character_4: int,
    character_5: int,
    command_id_1: int,
    obj_2: int,
):
    """Event 13700643"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9313))
    AND_2.Add(FlagEnabled(1355))
    AND_2.Add(FlagEnabled(1347))
    AND_2.Add(FlagEnabled(73700150))
    AND_2.Add(CharacterBackreadDisabled(character))
    AND_2.Add(CharacterBackreadDisabled(character_1))
    OR_1.Add(AND_2)
    AND_3.Add(FlagEnabled(1561))
    AND_3.Add(FlagEnabled(1575))
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_3.Add(FlagEnabled(1561))
    AND_3.Add(FlagEnabled(1575))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1562, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1355))
    AND_4.Add(FlagEnabled(1347))
    AND_4.Add(FlagEnabled(73700150))
    AND_4.Add(FlagEnabled(1562))
    AND_4.Add(FlagEnabled(1575))
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(1041, 1043)))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1348, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1563, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1355))
    AND_5.Add(FlagEnabled(1347))
    AND_5.Add(FlagEnabled(73700150))
    AND_5.Add(FlagEnabled(1562))
    AND_5.Add(FlagEnabled(1575))
    AND_5.Add(FlagRangeAllDisabled(flag_range=(1041, 1043)))
    SkipLinesIfConditionFalse(8, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1348, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1358, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1566, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1575, 1579))
    SetNetworkConnectedFlagState(flag=1578, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1355))
    AND_6.Add(FlagEnabled(1347))
    AND_6.Add(FlagEnabled(73700150))
    AND_6.Add(FlagEnabled(1561))
    AND_6.Add(FlagEnabled(1578))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1350, state=FlagSetting.On)
    SaveRequest()

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1348)
    GotoIfFlagEnabled(Label.L2, flag=1350)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagDisabled(Label.L10, flag=9013)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagDisabled(Label.L10, flag=9013)
    CreateVFX(vfx_id)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    CreateVFX(vfx_id_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L4, flag=1562)
    GotoIfFlagEnabled(Label.L5, flag=1563)
    GotoIfFlagEnabled(Label.L6, flag=1566)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableObject(obj)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableObject(obj)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableObject(obj)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    EzstateAIRequest(character_3, command_id=command_id, command_slot=1)
    EnableObject(obj_1)
    EnableObject(obj_2)
    GotoIfFlagDisabled(Label.L10, flag=9013)
    EnableCharacter(character_4)
    EnableBackread(character_4)
    EzstateAIRequest(character_4, command_id=command_id_1, command_slot=1)
    DropMandatoryTreasure(character_4)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character_5)
    EnableBackread(character_5)
    EzstateAIRequest(character_5, command_id=command_id_1, command_slot=1)
    DropMandatoryTreasure(character_5)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@NeverRestart(13705644)
def Event_13705644(
    _,
    entity: int,
    entity_1: int,
    move_to_region__region: int,
    obj: int,
    character: int,
    animation_id: int,
):
    """Event 13705644"""
    if FlagEnabled(50006193):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1564))
    AND_1.Add(PlayerHasGood(2139))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=move_to_region__region))
    GotoIfFlagDisabled(Label.L0, flag=9013)
    AND_1.Add(ActionButtonParamActivated(action_button_id=6290, entity=entity))
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(ActionButtonParamActivated(action_button_id=6290, entity=entity_1))

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L15, flag=9013)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(37000020, cutscene_flags=0, player_id=10000, move_to_region=move_to_region__region, game_map=IRITHYLL)
    Goto(Label.L20)
    PlayCutscene(37000020, cutscene_flags=0, player_id=10000)
    Goto(Label.L20)

    # --- Label 15 --- #
    DefineLabel(15)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(37000021, cutscene_flags=0, player_id=10000, move_to_region=move_to_region__region, game_map=IRITHYLL)
    Goto(Label.L20)
    PlayCutscene(37000021, cutscene_flags=0, player_id=10000)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L5)
    RemoveGoodFromPlayer(item=2139, quantity=1)
    AwardItemLot(61930, host_only=True)
    EnableFlag(13700644)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1349, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1358, state=FlagSetting.On)
    if FlagDisabled(1578):
        DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
        SetNetworkConnectedFlagState(flag=1565, state=FlagSetting.On)
        DisableNetworkConnectedFlagRange(flag_range=(1575, 1579))
        SetNetworkConnectedFlagState(flag=1578, state=FlagSetting.On)
    SaveRequest()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableObject(obj)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFrames(frames=1)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@NeverRestart(13705645)
def Event_13705645(
    _,
    character: int,
    character_1: int,
    obj: int,
    special_effect_id: int,
    command_id: int,
    obj_1: int,
    character_2: int,
    character_3: int,
    command_id_1: int,
    obj_2: int,
):
    """Event 13705645"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1575, 1579))
    DisableNetworkConnectedFlagRange(flag_range=(1575, 1579))
    SetNetworkConnectedFlagState(flag=1575, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1560, 1574))
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1560, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1575)
    AND_2.Add(FlagEnabled(1563))
    AND_2.Add(FlagEnabled(74000605))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1564, state=FlagSetting.On)
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(1561, 1562)))
    AND_4.Add(FlagEnabled(1347))
    AND_4.Add(FlagEnabled(1358))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1567, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000080)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L1, flag=1561)
    GotoIfFlagEnabled(Label.L3, flag=1563)
    GotoIfFlagEnabled(Label.L4, flag=1564)
    GotoIfFlagEnabled(Label.L5, flag=1565)
    GotoIfFlagEnabled(Label.L6, flag=1566)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableObject(obj_2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableObject(obj_2)
    GotoIfFlagEnabled(Label.L18, flag=1578)
    EnableImmortality(character)
    AddSpecialEffect(character, special_effect_id)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableCharacter(character)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableObject(obj_2)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    DisableObject(obj_2)
    if FlagEnabled(13700644):
        DisableObject(obj_1)
        DisableCharacter(character_2)
        DisableBackread(character_2)
        DisableCharacter(character_3)
        DisableBackread(character_3)
        DropMandatoryTreasure(character_2)
        Goto(Label.L20)
    GotoIfFlagDisabled(Label.L10, flag=9013)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    EzstateAIRequest(character_2, command_id=command_id_1, command_slot=1)
    DisableHealthBar(character_2)
    Kill(character_2)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    EzstateAIRequest(character_3, command_id=command_id_1, command_slot=1)
    DisableHealthBar(character_3)
    Kill(character_3)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L18, flag=1578)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableObject(obj_2)
    EzstateAIRequest(character_1, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character_1)
    DropMandatoryTreasure(character_2)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    EzstateAIRequest(character_1, command_id=command_id, command_slot=1)
    GotoIfFlagDisabled(Label.L10, flag=9013)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    EzstateAIRequest(character_2, command_id=command_id_1, command_slot=1)
    DropMandatoryTreasure(character_2)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    EzstateAIRequest(character_3, command_id=command_id_1, command_slot=1)
    DropMandatoryTreasure(character_3)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@NeverRestart(13705646)
def Event_13705646(_, character: int, obj: int, special_effect_id: int):
    """Event 13705646"""
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_2.Add(FlagEnabled(1561))
    AND_2.Add(FlagEnabled(1575))
    GotoIfConditionTrue(Label.L20, input_condition=AND_2)
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(1561))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    CreateTemporaryVFX(vfx_id=435012, anchor_entity=character, model_point=220, anchor_type=CoordEntityType.Character)
    EnableCharacter(character)
    DisableImmortality(character)
    DisableObject(obj)
    SetNetworkConnectedFlagState(flag=13705646, state=FlagSetting.On)
    WaitFrames(frames=5)
    CancelSpecialEffect(character, special_effect_id)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableImmortality(character)
    DisableObject(obj)
    EnableCharacter(character)
    CancelSpecialEffect(character, special_effect_id)


@NeverRestart(13705647)
def Event_13705647(_, character: int, animation_id: int, flag: int):
    """Event 13705647"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(HealthNotEqual(character, value=0.0))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id, unknown2=1.0)
    WaitFrames(frames=1)
    OR_1.Add(CharacterHasTAEEvent(character, tae_event_id=20))
    OR_2.Add(CharacterDoesNotHaveSpecialEffect(character, 152))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=OR_2)
    AwardItemLot(63010, host_only=False)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 152))
    
    Restart()


@NeverRestart(13705650)
def Event_13705650():
    """Event 13705650"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (1075, 1079))
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1075, state=FlagSetting.On)
    AND_11.Add(FlagEnabled(1076))
    AND_11.Add(FlagEnabled(70000055))
    SkipLinesIfConditionFalse(2, AND_11)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1075, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1060, 1074))
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1060, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L20, flag=1075)
    AND_12.Add(FlagEnabled(1060))
    AND_12.Add(FlagEnabled(73100152))
    SkipLinesIfConditionFalse(2, AND_12)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1061, state=FlagSetting.On)
    AND_13.Add(FlagEnabled(1061))
    AND_13.Add(PlayerRemainingYoelLevelComparison(comparison_type=ComparisonType.LessThanOrEqual, value=0))
    SkipLinesIfConditionFalse(4, AND_13)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1062, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1078, state=FlagSetting.On)
    AND_14.Add(FlagEnabled(1061))
    AND_14.Add(FlagEnabled(136))
    SkipLinesIfConditionFalse(4, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1064, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1078, state=FlagSetting.On)
    AND_15.Add(FlagEnabled(1060))
    AND_15.Add(FlagEnabled(136))
    SkipLinesIfConditionFalse(4, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1063, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1078, state=FlagSetting.On)

    # --- Label 20 --- #
    DefineLabel(20)
    SkipLinesIfFlagRangeAnyEnabled(2, (1055, 1059))
    DisableNetworkConnectedFlagRange(flag_range=(1055, 1059))
    SetNetworkConnectedFlagState(flag=1055, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1056))
    AND_1.Add(FlagEnabled(70000054))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1055, 1059))
    SetNetworkConnectedFlagState(flag=1055, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1040, 1054))
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1040, state=FlagSetting.On)
    if FlagDisabled(1055):
        return
    AND_2.Add(FlagEnabled(700))
    AND_2.Add(FlagEnabled(1040))
    AND_2.Add(PlayerRemainingYoelLevelComparison(comparison_type=ComparisonType.LessThanOrEqual, value=0))
    AND_2.Add(FlagDisabled(74000124))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1041, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1041))
    AND_3.Add(FlagEnabled(50006193))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1042, state=FlagSetting.On)
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(1040, 1042)))
    AND_5.Add(PlayerRemainingYoelLevelComparison(comparison_type=ComparisonType.GreaterThan, value=0))
    AND_5.Add(FlagEnabled(1078))
    OR_4.Add(AND_5)
    OR_4.Add(FlagEnabled(74000124))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1044, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1041))
    AND_6.Add(FlagRangeAnyEnabled(flag_range=(1340, 1347)))
    AND_6.Add(FlagEnabled(1358))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1044, state=FlagSetting.On)
    AND_7.Add(FlagRangeAnyEnabled(flag_range=(1041, 1042)))
    AND_7.Add(FlagEnabled(1561))
    AND_7.Add(FlagEnabled(1578))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1043, state=FlagSetting.On)
    AND_8.Add(FlagEnabled(1043))
    OR_8.Add(FlagEnabled(74000619))
    OR_8.Add(FlagDisabled(74000600))
    AND_8.Add(OR_8)
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1044, state=FlagSetting.On)


@NeverRestart(13705651)
def Event_13705651(_, character: int, character_1: int):
    """Event 13705651"""
    if FlagEnabled(13700651):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(73700150))
    AND_1.Add(FlagEnabled(1347))
    AND_1.Add(FlagEnabled(1355))
    AND_1.Add(CharacterBackreadDisabled(character))
    AND_1.Add(CharacterBackreadDisabled(character_1))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=13700651, state=FlagSetting.On)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)


@NeverRestart(13705652)
def Event_13705652(_, character: int):
    """Event 13705652"""
    MAIN.Await(HealthEqual(3700800, value=0.0))
    
    SetAIParamID(character, ai_param_id=1)
    ReplanAI(character)


@NeverRestart(13705660)
def Event_13705660(_, character: int):
    """Event 13705660"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    SkipLinesIfFlagRangeAnyEnabled(2, (1395, 1399))
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    AND_15.Add(FlagEnabled(1396))
    AND_15.Add(FlagEnabled(70000071))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1380, 1394))
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1380, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L19, flag=1395)
    OR_1.Add(FlagEnabled(1380))
    OR_1.Add(FlagEnabled(1382))
    OR_1.Add(FlagEnabled(1394))
    AND_1.Add(OR_1)
    OR_2.Add(FlagEnabled(73100350))
    OR_2.Add(FlagEnabled(73100360))
    OR_2.Add(FlagEnabled(73100363))
    AND_1.Add(OR_2)
    AND_1.Add(FlagEnabled(1378))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1385, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1383))
    AND_2.Add(FlagEnabled(73500105))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1385, state=FlagSetting.On)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(70000071)
    if FlagEnabled(1395):
        DisableFlag(73700249)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L1, flag=1385)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagRangeAnyEnabled(Label.L18, flag_range=(1396, 1397))
    GotoIfFlagEnabled(Label.L17, flag=1398)
    AND_3.Add(FlagDisabled(73700201))
    AND_3.Add(FlagDisabled(73700206))
    SkipLinesIfConditionFalse(2, AND_3)
    ForceAnimation(character, 90860, loop=True, skip_transition=True, unknown2=1.0)
    End()
    ForceAnimation(character, 90850, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 17 --- #
    DefineLabel(17)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@RestartOnRest(13705661)
def Event_13705661(_, character: int):
    """Event 13705661"""
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(character, 150))
    OR_1.Add(FlagEnabled(1396))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1396):
        return
    EzstateAIRequest(character, command_id=2100, command_slot=1)
    OR_2.Add(FlagEnabled(1396))
    OR_2.Add(CharacterHasSpecialEffect(character, 150))
    OR_2.Add(TimeElapsed(seconds=0.5))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(1396):
        return
    Restart()


@RestartOnRest(13705662)
def Event_13705662(_, character: int):
    """Event 13705662"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1396):
        return
    
    MAIN.Await(FlagEnabled(73700206))
    
    ForceAnimation(character, 90860, loop=True, skip_transition=True, unknown2=1.0)
    WaitFrames(frames=1)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 152))
    
    DisableFlag(73700206)
    Restart()


@RestartOnRest(13705663)
def Event_13705663(_, character: int):
    """Event 13705663"""
    if PlayerNotInOwnWorld():
        return
    EnableFlag(73700211)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 153))
    
    DisableFlag(73700211)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 153))
    
    Restart()


@RestartOnRest(13700664)
def Event_13700664():
    """Event 13700664"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13700664):
        return
    
    MAIN.Await(FlagEnabled(73700204))
    
    ForceAnimation(PLAYER, 60070, unknown2=1.0)
    Wait(0.20000000298023224)
    CreateTemporaryVFX(vfx_id=301002, anchor_entity=PLAYER, model_point=220, anchor_type=CoordEntityType.Character)
    PlaySoundEffect(PLAYER, 999999988, sound_type=SoundType.c_CharacterMotion)
    AddSpecialEffect(PLAYER, 2005)


@NeverRestart(13705684)
def Event_13705684(_, character: int, animation_id: int):
    """Event 13705684"""
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    SetCharacterTalkRange(character=character, distance=100.0)
    EnableFlag(13705684)
    OR_1.Add(FlagEnabled(13705683))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=6.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(1, AND_1)
    ForceAnimation(character, 0, unknown2=1.0)

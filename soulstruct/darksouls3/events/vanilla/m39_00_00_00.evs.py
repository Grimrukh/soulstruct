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
    RegisterBonfire(bonfire_flag=13900000, obj=3901950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13900002, obj=3901952, reaction_distance=5.0)
    RunCommonEvent(20005500, args=(13900800, 13900001, 3900951, 3901951))
    RunCommonEvent(20005780, args=(3901780, 2))
    RunCommonEvent(
        20005750,
        args=(13900800, 13900192, 13904192, 13905192, 3900192, 3902192, 3902193, 0.0, 0),
        arg_types="iiiiiiifi",
    )
    RunCommonEvent(20005721, args=(13904192, 13905192, 13900192, 3900192))
    RunCommonEvent(20005760, args=(13900192, 13904192, 13905192, 3900192))
    RunCommonEvent(20005341, args=(13900192, 3900192, 58600))
    Event_13905900()
    RunCommonEvent(20005119, args=(3900200, 3902200, 3902201, 3902206, 0, 0, 0, 0))
    RunCommonEvent(20005110, args=(3900203, 3902202))
    RunCommonEvent(20005110, args=(3900206, 3902202))
    RunCommonEvent(20005110, args=(3900207, 3902202))
    RunCommonEvent(20005203, args=(3900220, 30000, 20000, 3902220, 3902221, 3902222, 0, 0, 0))
    RunCommonEvent(20005203, args=(3900221, 30000, 20000, 3902220, 3902221, 3902222, 0, 0, 0))
    RunCommonEvent(20005203, args=(3900222, 30000, 20000, 3902220, 3902221, 3902222, 0, 0, 0))
    RunCommonEvent(20005210, args=(3900223, 30000, 20000, 3.0), arg_types="iiif")
    RunCommonEvent(20005110, args=(3900225, 3902228))
    RunCommonEvent(20005110, args=(3900226, 3902228))
    Event_13905220(0, character=3900225, region=3902227, flag=13905225)
    Event_13905220(1, character=3900226, region=3902227, flag=13905226)
    Event_13905225(0, character=3900225, region=3902228, flag=13905220)
    Event_13905225(1, character=3900226, region=3902228, flag=13905221)
    Event_13905230(0, character=3900204, patrol_information_id=3904240, flag=53900510)
    Event_13905230(1, character=3900205, patrol_information_id=3904240, flag=53900510)
    Event_13905230(2, character=3900213, patrol_information_id=3904245, flag=53900460)
    Event_13905230(3, character=3900214, patrol_information_id=3904245, flag=53900460)
    Event_13905230(4, character=3900215, patrol_information_id=3904245, flag=53900460)
    Event_13905230(5, character=3900216, patrol_information_id=3904245, flag=53900460)
    Event_13905230(6, character=3900217, patrol_information_id=3904245, flag=53900460)
    Event_13905230(7, character=3900218, patrol_information_id=3904245, flag=53900460)
    Event_13905230(8, character=3900219, patrol_information_id=3904245, flag=53900460)
    RunCommonEvent(20005119, args=(3900390, 3902390, 3902391, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3900391, 3902390, 3902391, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3900392, 3902392, 3902391, 3902390, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3900393, 3902392, 3902391, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3900394, 3902392, 3902391, 0, 0, 0, 0, 0))
    RunCommonEvent(20005120, args=(3900395, 7.5), arg_types="if")
    RunCommonEvent(20005290, args=(3900230, 30001, -1))
    RunCommonEvent(20005212, args=(3900231, 30000, 20003, 5.0, 3902231), arg_types="iiifi")
    RunCommonEvent(20005111, args=(3900233, 3008, 3902233))
    RunCommonEvent(20005133, args=(3900234, 3001, 3.0, 3902234), arg_types="iifi")
    RunCommonEvent(20005220, args=(3900240, 30000, 20003))
    RunCommonEvent(20005220, args=(3900241, 702, 1702))
    RunCommonEvent(20005260, args=(3900242, 700, 1700, 3900241))
    RunCommonEvent(20005260, args=(3900243, 700, 1700, 3900241))
    RunCommonEvent(20005220, args=(3900244, 30000, 20003))
    RunCommonEvent(20005134, args=(3900250, 3006, 1.5, 3902253), arg_types="iifi")
    Event_13905251()
    Event_13905255(0, 3900257, 700, 1700, 1.5, 0.0, 3901200, 3901201, 3901205, 0, 0)
    Event_13905255(1, 3900267, 701, 3001, 1.5, 0.0, 3901202, 3901203, 3901204, 3901206, 0)
    Event_13905255(2, 3900268, 702, 1702, 1.5, 0.20000000298023224, 3901202, 3901203, 3901204, 3901206, 0)
    Event_13905255(3, 3900269, 700, 1700, 1.5, 0.0, 3901202, 3901203, 3901204, 3901206, 0)
    RunCommonEvent(20005210, args=(3900252, 702, 1702, 1.5), arg_types="iiif")
    RunCommonEvent(20005213, args=(3900253, 700, 1700, 1.5, 3902258), arg_types="iiifi")
    RunCommonEvent(20005213, args=(3900255, 702, 1702, 1.5, 3902258), arg_types="iiifi")
    RunCommonEvent(20005213, args=(3900256, 700, 1700, 1.5, 3902258), arg_types="iiifi")
    RunCommonEvent(20005114, args=(3900257, 3902256, 1.0), arg_types="iif")
    RunCommonEvent(20005121, args=(3900258, 5.0, 6.0), arg_types="iff")
    RunCommonEvent(20005119, args=(3900260, 3902252, 3902260, 0, 0, 0, 0, 0))
    RunCommonEvent(20005204, args=(3900261, 700, 1700, 3902250, 2.0, 1700, 3902252, 2.0), arg_types="iiiifiif")
    RunCommonEvent(20005132, args=(3900262, 5.0, 3902257), arg_types="ifi")
    RunCommonEvent(20005210, args=(3900263, 702, 1702, 3.0), arg_types="iiif")
    RunCommonEvent(20005114, args=(3900264, 3902257, 8.0), arg_types="iif")
    RunCommonEvent(20005120, args=(3900264, 3.0), arg_types="if")
    RunCommonEvent(20005210, args=(3900265, 702, 1702, 3.0), arg_types="iiif")
    RunCommonEvent(20005213, args=(3900266, 700, 1700, 4.0, 3902254), arg_types="iiifi")
    RunCommonEvent(20005110, args=(3900268, 3902255))
    Event_13900260(0, entity=3900254, animation_id=703, animation_id_1=1703)
    RunCommonEvent(20005350, args=(3900259, 20601010, 53900920))
    RunCommonEvent(20005122, args=(3900270, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3900271, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3900272, 3000, 1.5), arg_types="iif")
    RunCommonEvent(20005122, args=(3900273, 3000, 3.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3900274, 3000, 3.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3900275, 3000, 3.0), arg_types="iif")
    RunCommonEvent(20005131, args=(3900276, 3000, 2.5, 3902270), arg_types="iifi")
    RunCommonEvent(20005131, args=(3900277, 3000, 2.0, 3902270), arg_types="iifi")
    RunCommonEvent(20005114, args=(3900280, 3902291, 6.0), arg_types="iif")
    RunCommonEvent(20005190, args=(3900290, 21.0), arg_types="if")
    RunCommonEvent(20005220, args=(3900291, 706, 1706))
    RunCommonEvent(20005110, args=(3900292, 3902291))
    RunCommonEvent(20005110, args=(3900293, 3902291))
    RunCommonEvent(20005130, args=(3900294, 30.0, 3902291), arg_types="ifi")
    RunCommonEvent(20005110, args=(3900296, 3902291))
    RunCommonEvent(20005110, args=(3900297, 3902291))
    RunCommonEvent(20005114, args=(3900298, 3902291, 6.0), arg_types="iif")
    RunCommonEvent(20005110, args=(3900299, 3902290))
    EnableSpawner(entity=3904300)
    RunCommonEvent(20005320, args=(3900310, 3902310, 3904310))
    RunCommonEvent(20005330, args=(3900311, 3902311, 13905300))
    RunCommonEvent(20005330, args=(3900312, 3902311, 13905301))
    RunCommonEvent(20005330, args=(3900313, 3902311, 13905302))
    RunCommonEvent(20005330, args=(3900314, 3902311, 13905303))
    RunCommonEvent(20005110, args=(3900315, 3902312))
    RunCommonEvent(20005110, args=(3900316, 3902312))
    RunCommonEvent(20005192, args=(3900317, 3902310))
    RunCommonEvent(20005192, args=(3900318, 3902310))
    Event_13905320(0, character=3900321, flag=13905325)
    Event_13905320(1, character=3900322, flag=13905326)
    Event_13905320(2, character=3900323, flag=13905327)
    Event_13905320(3, character=3900324, flag=13905328)
    Event_13905320(4, character=3900325, flag=13905329)
    RunCommonEvent(20005111, args=(3900321, 20000, 3902321))
    RunCommonEvent(20005111, args=(3900322, 20000, 3902321))
    RunCommonEvent(20005111, args=(3900323, 20000, 3902321))
    RunCommonEvent(20005111, args=(3900324, 20000, 3902321))
    RunCommonEvent(20005111, args=(3900325, 20000, 3902321))
    RunCommonEvent(20005212, args=(3900330, 700, 1700, 8.0, 3902330), arg_types="iiifi")
    RunCommonEvent(20005212, args=(3900331, 700, 1700, 8.0, 3902330), arg_types="iiifi")
    RunCommonEvent(20005212, args=(3900332, 700, 1700, 5.5, 3902330), arg_types="iiifi")
    RunCommonEvent(20005211, args=(3900333, 700, 1700, 7.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3900334, 700, 1700, 5.5, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3900335, 700, 20000, 8.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3900336, 700, 1700, 6.5, 1.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3900337, 700, 20000, 4.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3900338, 700, 20000, 12.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005211, args=(3900339, 700, 1700, 8.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005341, args=(13900340, 3900340, 21508000))
    RunCommonEvent(20005341, args=(13900341, 3900341, 21508010))
    RunCommonEvent(20005341, args=(13900342, 3900342, 21508020))
    RunCommonEvent(20005341, args=(13900343, 3900343, 21508030))
    RunCommonEvent(20005400, args=(3900350,))
    RunCommonEvent(20005400, args=(3900351,))
    RunCommonEvent(20005400, args=(3900352,))
    RunCommonEvent(20005400, args=(3900353,))
    RunCommonEvent(20005400, args=(3900354,))
    RunCommonEvent(20005400, args=(3900355,))
    RunCommonEvent(20005400, args=(3900356,))
    RunCommonEvent(20000343, args=(13900350, 3900350, 53900940))
    RunCommonEvent(20000343, args=(13900351, 3900351, 53900990))
    RunCommonEvent(20000343, args=(13900352, 3900352, 53900970))
    RunCommonEvent(20000343, args=(13900353, 3900353, 53900950))
    RunCommonEvent(20000343, args=(13900354, 3900354, 53900960))
    RunCommonEvent(20000343, args=(13900355, 3900355, 53900980))
    RunCommonEvent(20000343, args=(13900356, 3900356, 53900995))
    Event_13905360()
    Event_13905361()
    Event_13905363()
    Event_13905364()
    RunCommonEvent(20005132, args=(3900362, 20.0, 3902362), arg_types="ifi")
    RunCommonEvent(20005220, args=(3900370, 700, 1700))
    RunCommonEvent(20005220, args=(3900371, 700, 1700))
    RunCommonEvent(20005220, args=(3900372, 700, 1700))
    RunCommonEvent(20005340, args=(13900370, 3900370))
    RunCommonEvent(20005340, args=(13900371, 3900371))
    RunCommonEvent(20005340, args=(13900372, 3900372))
    RunCommonEvent(20005341, args=(13900373, 3900373, 20400020))
    Event_13905380()
    Event_13905381()
    RunCommonEvent(20005340, args=(13900380, 3900380))
    RunCommonEvent(20005110, args=(3900399, 3902280))
    RunCommonEvent(20005342, args=(13900360, 3900399))
    Event_13905810()
    Event_13905811()
    Event_13905815()
    Event_13905816()
    Event_13905820()
    Event_13905840()
    Event_13905850()
    Event_13905860()
    Event_13905861()
    Event_13905830(0, npc_part_id=10, part_index=3, part_health=400, npc_part_id_1=10, animation_id=20000)
    Event_13905830(1, npc_part_id=20, part_index=6, part_health=400, npc_part_id_1=20, animation_id=20002)
    Event_13905835()
    Event_13905870(0, obj=3901651, obj_1=3901650)
    Event_13905500(0, flag=13900500, obj=3901500, obj_act_id=3903500, obj_act_id_1=3903600)
    Event_13905500(2, flag=13900502, obj=3901502, obj_act_id=3903502, obj_act_id_1=3903602)
    Event_13905500(3, flag=13900503, obj=3901503, obj_act_id=3903503, obj_act_id_1=3903603)
    Event_13905500(4, flag=13900504, obj=3901504, obj_act_id=3903504, obj_act_id_1=3903604)
    Event_13905500(5, flag=13900505, obj=3901505, obj_act_id=3903505, obj_act_id_1=3903605)
    Event_13905500(6, flag=13900510, obj=3901510, obj_act_id=3903510, obj_act_id_1=3903610)
    Event_13905500(7, flag=13900511, obj=3901511, obj_act_id=3903511, obj_act_id_1=3903611)
    Event_13905500(8, flag=13900512, obj=3901512, obj_act_id=3903512, obj_act_id_1=3903612)
    Event_13905500(9, flag=13900513, obj=3901513, obj_act_id=3903513, obj_act_id_1=3903613)
    Event_13905500(10, flag=13900514, obj=3901514, obj_act_id=3903514, obj_act_id_1=3903614)
    Event_13905500(11, flag=13900515, obj=3901515, obj_act_id=3903515, obj_act_id_1=3903615)
    Event_13905500(12, flag=13900516, obj=3901516, obj_act_id=3903516, obj_act_id_1=3903616)
    Event_13905500(13, flag=13900517, obj=3901517, obj_act_id=3903517, obj_act_id_1=3903617)
    Event_13905500(16, flag=13900520, obj=3901520, obj_act_id=3903520, obj_act_id_1=3903620)
    Event_13905500(17, flag=13900521, obj=3901521, obj_act_id=3903521, obj_act_id_1=3903621)
    Event_13905500(18, flag=13900522, obj=3901522, obj_act_id=3903522, obj_act_id_1=3903622)
    Event_13905500(21, flag=13900525, obj=3901525, obj_act_id=3903525, obj_act_id_1=3903625)
    Event_13905500(22, flag=13900526, obj=3901526, obj_act_id=3903526, obj_act_id_1=3903626)
    Event_13905500(24, flag=13900528, obj=3901528, obj_act_id=3903528, obj_act_id_1=3903628)
    Event_13905500(25, flag=13900530, obj=3901530, obj_act_id=3903530, obj_act_id_1=3903630)
    Event_13905500(27, flag=13900532, obj=3901532, obj_act_id=3903532, obj_act_id_1=3903632)
    Event_13905500(28, flag=13900533, obj=3901533, obj_act_id=3903533, obj_act_id_1=3903633)
    Event_13905500(29, flag=13900534, obj=3901534, obj_act_id=3903534, obj_act_id_1=3903634)
    Event_13905500(30, flag=13900535, obj=3901535, obj_act_id=3903535, obj_act_id_1=3903635)
    Event_13905420()
    Event_13905425()
    Event_13905430()
    Event_13905435()
    Event_13905440()
    Event_13905445()
    Event_13905450()
    Event_13905460()
    Event_13905480()
    RunCommonEvent(20005613, args=(13900550, 3903550, 3901550, 390350, 10010868))
    RunCommonEvent(20005613, args=(13900551, 3903551, 3901551, 390350, 10010868))
    Event_13905415(
        0,
        flag=13900552,
        obj_act_id=3903552,
        obj_act_id_1=3903557,
        obj=3901552,
        obj_act_id_2=390350,
        obj_act_id_3=390360,
        text=10010868
    )
    Event_13905415(
        1,
        flag=13900553,
        obj_act_id=3903553,
        obj_act_id_1=3903558,
        obj=3901553,
        obj_act_id_2=390350,
        obj_act_id_3=390360,
        text=10010868
    )
    Event_13905470()
    Event_13905471()
    Event_13905475()
    RunCommonEvent(20005620, args=(13900400, 13900402, 3901400, 3901401, 3901402, 13901400))
    RunCommonEvent(20005628, args=(13900401, 3901401, 3902402))
    Event_13900411()
    RunCommonEvent(20005622, args=(13900405, 13900407, 3901405, 3901406, 3901407, 13901405))
    RunCommonEvent(20005628, args=(13900406, 3901406, 3902407))
    Event_13900412()
    RunCommonEvent(20005520, args=(13900609, 3901609, 3904609))
    RunCommonEvent(20005520, args=(13900611, 3901611, 3904611))
    RunCommonEvent(20005520, args=(13900613, 3901613, 3904613))
    Event_13905620(0, entity=3901620, flag=53900450, flag_1=13905620)
    Event_13905620(1, entity=3901621, flag=53900460, flag_1=13905621)
    Event_13905620(2, entity=3901625, flag=53900510, flag_1=13905625)
    RunCommonEvent(20005524, args=(3901622, 13900192))
    RunCommonEvent(20005523, args=(3901624, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3901627, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3901628, 2), arg_types="iB")
    Event_13900900()
    RunCommonEvent(20006003, args=(3900700, 73900131, 1275, 1260, 1261, 1260, 1274))
    RunCommonEvent(20006002, args=(3900700, 1278, 1275, 1279))
    RunCommonEvent(20006002, args=(3900705, 1398, 1395, 1399))
    RunCommonEvent(20006002, args=(3900706, 1398, 1395, 1399))
    RunCommonEvent(
        20006000,
        args=(3900705, 1396, 1397, 73900190, 0.6499999761581421, 1395, 1399, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3900705, 1396, 1397, 73900190, 3))
    Event_13900721()
    Event_13900723(0, 3900706, 38.0)
    Event_13900726()
    Event_13905727()
    Event_13905728()
    Event_13900729(0, character=3900705)
    RunCommonEvent(20006030, args=(3901706, 4000, 1, 62140, 50006215, 50006216, 1390))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13900465()
    Event_13900410()
    Event_13905700(0, character=3900700, animation_id=90460)
    Event_13905720(0, character=3900705, character_1=3900706)
    DisableSoundEvent(sound_id=3904801)
    DisableSoundEvent(sound_id=3904802)


@RestartOnRest(13905220)
def Event_13905220(_, character: int, region: int, flag: int):
    """Event 13905220"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 11890)
    CancelSpecialEffect(character, 11900)
    CancelSpecialEffect(character, 11901)
    CancelSpecialEffect(character, 11902)
    CancelSpecialEffect(character, 11903)
    CancelSpecialEffect(character, 11899)


@RestartOnRest(13905225)
def Event_13905225(_, character: int, region: int, flag: int):
    """Event 13905225"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagEnabled(flag))
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    EnableAI(character)
    CancelSpecialEffect(character, 11890)
    AddSpecialEffect(character, 11899)


@RestartOnRest(13905230)
def Event_13905230(_, character: int, patrol_information_id: int, flag: int):
    """Event 13905230"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    ReplanAI(character)
    AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    OR_1.Add(ThisEventSlotFlagEnabled())
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    CancelSpecialEffect(character, 5000)


@RestartOnRest(13905251)
def Event_13905251():
    """Event 13905251"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(3900251, 702, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3902254, radius=1.5))
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 53900450))
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=3900251, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(3900251, 5450))
    if AND_2:
        return
    ForceAnimation(3900251, 1702, unknown2=1.0)
    ReplanAI(3900251)


@RestartOnRest(13905255)
def Event_13905255(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    obj: int,
    obj_1: int,
    obj_2: int,
    obj_3: int,
    obj_4: int,
):
    """Event 13905255"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(obj)
    RestoreObject(obj_1)
    RestoreObject(obj_2)
    RestoreObject(obj_3)
    RestoreObject(obj_4)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_1)
    OR_9.Add(ObjectDestroyed(obj))
    if ValueNotEqual(left=obj_1, right=0):
        OR_9.Add(ObjectDestroyed(obj_1))
    if ValueNotEqual(left=obj_2, right=0):
        OR_9.Add(ObjectDestroyed(obj_2))
    if ValueNotEqual(left=obj_3, right=0):
        OR_9.Add(ObjectDestroyed(obj_3))
    if ValueNotEqual(left=obj_4, right=0):
        OR_9.Add(ObjectDestroyed(obj_4))
    OR_2.Add(OR_9)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(13900260)
def Event_13900260(_, entity: int, animation_id: int, animation_id_1: int):
    """Event 13900260"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(entity, animation_id, unknown2=1.0)
    OR_1.Add(ObjectActivated(obj_act_id=3903515))
    OR_1.Add(ObjectActivated(obj_act_id=3903615))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, animation_id_1, unknown2=1.0)


@RestartOnRest(13905320)
def Event_13905320(_, character: int, flag: int):
    """Event 13905320"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3902320))
    AND_1.Add(FlagEnabled(53900610))
    OR_2.Add(AND_1)
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 53900610))
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)
    AddSpecialEffect(character, 5000)
    EnableFlag(flag)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    CancelSpecialEffect(character, 5000)


@RestartOnRest(13905360)
def Event_13905360():
    """Event 13905360"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3900360)
    DisableGravity(3900360)
    DisableCharacterCollision(3900360)
    ForceAnimation(3900360, 30001, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3902360))
    AND_1.Add(CharacterBackreadEnabled(3900360))
    AND_1.Add(CharacterHasSpecialEffect(3900360, 5450))
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=3900360, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(3900360, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(3900360, 640)
    EnableAI(3900360)
    SetNest(3900360, region=3902365)
    EnableGravity(3900360)
    EnableCharacterCollision(3900360)
    ForceAnimation(3900360, 20000, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(3900360, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13905361)
def Event_13905361():
    """Event 13905361"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3900361)
    DisableGravity(3900361)
    DisableCharacterCollision(3900361)
    ForceAnimation(3900361, 30001, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902361))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(3900361))
    AND_1.Add(CharacterHasSpecialEffect(3900361, 5450))
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=3900361, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(3900361, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(3900361, 640)
    EnableAI(3900361)
    SetNest(3900361, region=3902366)
    EnableGravity(3900361)
    EnableCharacterCollision(3900361)
    ForceAnimation(3900361, 20005, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(3900361, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13905363)
def Event_13905363():
    """Event 13905363"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3900363)
    DisableGravity(3900363)
    DisableCharacterCollision(3900363)
    ForceAnimation(3900363, 30001, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902363))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902364))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(3900363))
    AND_1.Add(CharacterHasSpecialEffect(3900363, 5450))
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=3900363, attacker=PLAYER))
    OR_2.Add(CharacterDead(3905390))
    OR_2.Add(HealthRatioLessThanOrEqual(3900364, value=0.5))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(3900363, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(3900363, 640)
    SetNest(3900363, region=3902368)
    EnableGravity(3900363)
    EnableCharacterCollision(3900363)
    ForceAnimation(3900363, 20007, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(3900363, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableAI(3900363)
    AND_5.Add(CharacterInsideRegion(character=PLAYER, region=3902364))
    GotoIfConditionFalse(Label.L0, input_condition=AND_5)
    AddSpecialEffect(3900363, 5000)
    ChangePatrolBehavior(3900363, patrol_information_id=3904360)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(3900363)


@RestartOnRest(13905364)
def Event_13905364():
    """Event 13905364"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3900364)
    DisableGravity(3900364)
    DisableCharacterCollision(3900364)
    ForceAnimation(3900364, 30001, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3902364))
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=3900364, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(3900363, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(3900364, 640)
    EnableAI(3900364)
    SetNest(3900364, region=3902369)
    EnableGravity(3900364)
    EnableCharacterCollision(3900364)
    ForceAnimation(3900364, 20006, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(3900363, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13905380)
def Event_13905380():
    """Event 13905380"""
    DisableAI(3900380)
    ForceAnimation(3900380, 30000, loop=True, unknown2=1.0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902380))
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=3900380, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    ForceAnimation(3900380, 20000, wait_for_completion=True, unknown2=1.0)
    EnableAI(3900380)


@RestartOnRest(13905381)
def Event_13905381():
    """Event 13905381"""
    DisableNetworkSync()
    SetNetworkUpdateRate(3900380, is_fixed=False, update_rate=CharacterUpdateRate.EveryFiveFrames)
    AND_1.Add(CharacterBackreadEnabled(3900380))
    AND_1.Add(CharacterAlive(3900380))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(3900380, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    OR_1.Add(CharacterBackreadDisabled(3900380))
    OR_1.Add(CharacterDead(3900380))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(13905415)
def Event_13905415(
    _,
    flag: int,
    obj_act_id: int,
    obj_act_id_1: int,
    obj: int,
    obj_act_id_2: int,
    obj_act_id_3: int,
    text: int,
):
    """Event 13905415"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=text, anchor_entity=obj)
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_3)


@NeverRestart(13900900)
def Event_13900900():
    """Event 13900900"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    CreateObjectVFX(3901250, vfx_id=90, model_point=61)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=4200, entity=3901250))
    
    ForceAnimation(PLAYER, 60070, skip_transition=True, unknown2=1.0)
    if FlagDisabled(6073):
        AwardGestureItem(gesture_id=23, item_type=ItemType.Good, item_id=9024)
    AwardItemLot(3900900, host_only=False)
    DeleteObjectVFX(3901250)
    EnableFlag(6073)


@NeverRestart(13900410)
def Event_13900410():
    """Event 13900410"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13900400)
    EnableFlag(13900405)
    EnableFlag(13900410)


@RestartOnRest(13900411)
def Event_13900411():
    """Event 13900411"""
    RunCommonEvent(
        20005621,
        args=(
            13900400,
            13900402,
            3901400,
            3901401,
            3904401,
            3901402,
            3904402,
            3902401,
            3902402,
            13901400,
            13904400,
            13900401,
        ),
    )


@RestartOnRest(13900412)
def Event_13900412():
    """Event 13900412"""
    RunCommonEvent(
        20005623,
        args=(
            13900405,
            13900407,
            3901405,
            3901406,
            3904406,
            3901407,
            3904407,
            3902406,
            3902407,
            13901405,
            13904405,
            13900406,
        ),
    )


@NeverRestart(13905420)
def Event_13905420():
    """Event 13905420"""
    RunCommonEvent(20005610, args=(13900420, 3902420, 3902421))
    RunCommonEvent(20005611, args=(13900420, 3903420, 3901420, 390305))


@NeverRestart(13905425)
def Event_13905425():
    """Event 13905425"""
    RunCommonEvent(20005613, args=(13900425, 3903425, 3901425, 390340, 10010872))


@NeverRestart(13905430)
def Event_13905430():
    """Event 13905430"""
    RunCommonEvent(20005610, args=(13900430, 3902430, 3902431))
    RunCommonEvent(20005611, args=(13900430, 3903430, 3901430, 390305))


@NeverRestart(13905435)
def Event_13905435():
    """Event 13905435"""
    RunCommonEvent(20005610, args=(13900435, 3902435, 3902436))
    RunCommonEvent(20005611, args=(13900435, 3903435, 3901435, 390300))


@NeverRestart(13905440)
def Event_13905440():
    """Event 13905440"""
    RunCommonEvent(20005610, args=(13900440, 3902440, 3902441))
    RunCommonEvent(20005611, args=(13900440, 3903440, 3901440, 390305))


@NeverRestart(13905445)
def Event_13905445():
    """Event 13905445"""
    EndOfAnimation(obj=3901445, animation_id=0)


@NeverRestart(13905450)
def Event_13905450():
    """Event 13905450"""
    RunCommonEvent(20005613, args=(13900450, 3903450, 3901450, 390320, 10010867))


@NeverRestart(13905460)
def Event_13905460():
    """Event 13905460"""
    RunCommonEvent(20005614, args=(3901460, 63900460))


@NeverRestart(13900465)
def Event_13900465():
    """Event 13900465"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13900500)
    EnableFlag(13900502)
    EnableFlag(13900504)
    EnableFlag(13900505)
    EnableFlag(13900511)
    EnableFlag(13900512)
    EnableFlag(13900514)
    EnableFlag(13900516)
    EnableFlag(13900517)
    EnableFlag(13900518)
    EnableFlag(13900521)
    EnableFlag(13900522)
    EnableFlag(13900526)
    EnableFlag(13900528)
    EnableFlag(13900535)


@RestartOnRest(13905470)
def Event_13905470():
    """Event 13905470"""
    DeleteObjectVFX(3901470, erase_root=False)
    CreateObjectVFX(3901470, vfx_id=200, model_point=839020)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3900470, authority_level=UpdateAuthority.Forced)


@RestartOnRest(13905471)
def Event_13905471():
    """Event 13905471"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13900471, state=FlagSetting.Off)
    GotoIfFlagEnabled(Label.L0, flag=13905479)
    SetNetworkUpdateRate(3900470, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902471))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902472))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902473))
    AND_1.Add(FlagDisabled(13900471))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    OR_3.Add(FlagEnabled(13900472))
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13900471, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=13900472, state=FlagSetting.On)
    DisableFlag(13900472)
    GotoIfFlagEnabled(Label.L0, flag=13905479)
    CreateTemporaryVFX(vfx_id=524112, anchor_entity=3902470, anchor_type=CoordEntityType.Region)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=3900470,
            source_entity=3902470,
            model_point=-1,
            behavior_id=5900,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=3900470,
            source_entity=3902470,
            model_point=-1,
            behavior_id=5901,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=3900470,
            source_entity=3902470,
            model_point=-1,
            behavior_id=5902,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=3900470,
            source_entity=3902470,
            model_point=-1,
            behavior_id=5903,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=3900470,
            source_entity=3902470,
            model_point=-1,
            behavior_id=5904,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=3900470,
            source_entity=3902470,
            model_point=-1,
            behavior_id=5905,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=3900470,
            source_entity=3902470,
            model_point=-1,
            behavior_id=5906,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(3900470, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    DisableAI(3900470)
    End()


@RestartOnRest(13905475)
def Event_13905475():
    """Event 13905475"""
    AND_1.Add(CharacterAlive(3900223))
    AND_1.Add(HasAIStatus(3900223, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.NotEqual))
    AND_1.Add(CharacterInsideRegion(character=3900223, region=3902475))
    
    MAIN.Await(not AND_1)
    
    EnableFlag(13905479)


@RestartOnRest(13905480)
def Event_13905480():
    """Event 13905480"""
    RegisterLadder(start_climbing_flag=13900480, stop_climbing_flag=13900481, obj=3901480)
    RegisterLadder(start_climbing_flag=13900482, stop_climbing_flag=13900483, obj=3901481)
    RegisterLadder(start_climbing_flag=13900484, stop_climbing_flag=13900485, obj=3901482)
    RegisterLadder(start_climbing_flag=13900486, stop_climbing_flag=13900487, obj=3901483)
    RegisterLadder(start_climbing_flag=13900488, stop_climbing_flag=13900489, obj=3901484)
    RegisterLadder(start_climbing_flag=13900490, stop_climbing_flag=13900491, obj=3901485)
    RegisterLadder(start_climbing_flag=13900492, stop_climbing_flag=13900493, obj=3901486)
    RegisterLadder(start_climbing_flag=13900494, stop_climbing_flag=13900495, obj=3901487)
    RegisterLadder(start_climbing_flag=13900496, stop_climbing_flag=13900497, obj=3901488)
    RegisterLadder(start_climbing_flag=13900498, stop_climbing_flag=13900499, obj=3901489)


@RestartOnRest(13905500)
def Event_13905500(_, flag: int, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 13905500"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EnableObjectActivation(obj, obj_act_id=390301)
    EnableObjectActivation(obj, obj_act_id=390302)
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    
    MAIN.Await(OR_1)
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    DisableObjectActivation(obj, obj_act_id=390301)
    DisableObjectActivation(obj, obj_act_id=390302)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=390301)
    DisableObjectActivation(obj, obj_act_id=390302)
    End()


@RestartOnRest(13905620)
def Event_13905620(_, entity: int, flag: int, flag_1: int):
    """Event 13905620"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    ForceAnimation(entity, 200, loop=True, skip_transition=True, unknown2=1.0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    ForceAnimation(entity, 201, wait_for_completion=True, unknown2=1.0)
    EnableFlag(flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity, 202, loop=True, unknown2=1.0)
    End()


@NeverRestart(13905700)
def Event_13905700(_, character: int, animation_id: int):
    """Event 13905700"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1275, 1279))
    DisableNetworkConnectedFlagRange(flag_range=(1275, 1279))
    SetNetworkConnectedFlagState(flag=1275, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1276))
    AND_1.Add(FlagEnabled(70000065))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1275, 1279))
    SetNetworkConnectedFlagState(flag=1275, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1260, 1274))
    DisableNetworkConnectedFlagRange(flag_range=(1260, 1274))
    SetNetworkConnectedFlagState(flag=1260, state=FlagSetting.On)
    GotoIfFlagEnabled(Label.L9, flag=1275)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000065)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1260)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1278)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(13905720)
def Event_13905720(_, character: int, character_1: int):
    """Event 13905720"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    SkipLinesIfFlagRangeAnyEnabled(2, (1395, 1399))
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    AND_15.Add(FlagEnabled(1396))
    AND_15.Add(FlagEnabled(70000071))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    AND_14.Add(FlagEnabled(1395))
    AND_14.Add(FlagEnabled(73900164))
    SkipLinesIfConditionFalse(2, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1398, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1380, 1394))
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1380, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L19, flag=1395)
    OR_1.Add(FlagEnabled(1384))
    OR_1.Add(FlagEnabled(1385))
    AND_2.Add(OR_1)
    AND_2.Add(FlagEnabled(140))
    AND_2.Add(FlagEnabled(73700201))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1386, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1386))
    AND_5.Add(FlagEnabled(73900152))
    OR_2.Add(AND_5)
    OR_2.Add(FlagEnabled(1387))
    AND_4.Add(OR_2)
    AND_4.Add(FlagEnabled(73100364))
    AND_4.Add(FlagEnabled(73700203))
    AND_4.Add(FlagEnabled(73500105))
    AND_4.Add(FlagDisabled(9318))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1388, state=FlagSetting.On)
    AND_7.Add(FlagEnabled(1386))
    AND_7.Add(FlagEnabled(9318))
    AND_7.Add(FlagEnabled(73900152))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1390, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1388))
    AND_6.Add(FlagEnabled(9318))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1389, state=FlagSetting.On)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(70000071)
    if FlagEnabled(1395):
        DisableFlag(73900199)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, flag=1386)
    GotoIfFlagEnabled(Label.L1, flag=1388)
    GotoIfFlagEnabled(Label.L2, flag=1389)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L16, flag=1396)
    GotoIfFlagEnabled(Label.L18, flag=1398)
    ForceAnimation(character, 90890, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L20, flag=13900722)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L18, flag=1398)
    SetTeamType(character_1, TeamType.WhitePhantom)
    DisableAI(character_1)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L18, flag=1398)
    SetTeamType(character_1, TeamType.WhitePhantom)
    ForceAnimation(character_1, 90850, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()


@RestartOnRest(13900721)
def Event_13900721():
    """Event 13900721"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAllDisabled(flag_range=(1396, 1398)))
    AND_1.Add(FlagEnabled(1386))
    AND_1.Add(FlagEnabled(73900152))
    AND_1.Add(FlagEnabled(73100364))
    AND_1.Add(FlagEnabled(73700203))
    AND_1.Add(FlagEnabled(73500105))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3902710))
    
    MAIN.Await(AND_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1388, state=FlagSetting.On)
    DisableCharacter(3900705)
    DisableBackread(3900705)


@RestartOnRest(13900723)
def Event_13900723(_, character: int, radius: float):
    """Event 13900723"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(73900164))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(HealthRatioNotEqual(character, value=0.0))
    AND_1.Add(FlagEnabled(1395))
    
    MAIN.Await(AND_1)
    
    Kill(character, award_souls=True)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1399))
    SetNetworkConnectedFlagState(flag=1389, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=1398, state=FlagSetting.On)


@RestartOnRest(13905725)
def Event_13905725():
    """Event 13905725"""
    MAIN.Await(FlagEnabled(9318))
    
    ClearTargetList(3900706)
    ReplanAI(3900706)
    DisableAI(3900706)


@RestartOnRest(13900726)
def Event_13900726():
    """Event 13900726"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(HealthRatioEqual(3900800, value=0.0))
    AND_1.Add(FlagEnabled(1388))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagDisabled():
        AICommand(3900706, command_id=20, command_slot=1)
        ReplanAI(3900706)
        Wait(2.0)
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(3900706, 150))
    OR_1.Add(FlagEnabled(1396))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1396):
        return
    EzstateAIRequest(3900706, command_id=2100, command_slot=1)
    OR_2.Add(FlagEnabled(1396))
    OR_2.Add(CharacterHasSpecialEffect(3900706, 150))
    OR_2.Add(TimeElapsed(seconds=0.5))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(1396):
        return
    Restart()


@RestartOnRest(13905727)
def Event_13905727():
    """Event 13905727"""
    if PlayerNotInOwnWorld():
        return
    EnableFlag(73900180)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(3900706, 153))
    
    DisableFlag(73900180)
    
    MAIN.Await(CharacterHasSpecialEffect(3900706, 153))
    
    Restart()


@RestartOnRest(13905728)
def Event_13905728():
    """Event 13905728"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(73900155)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3902712))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3902713))
    
    MAIN.Await(OR_1)
    
    EnableFlag(73900155)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902712))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3902713))
    
    MAIN.Await(not OR_2)
    
    DisableFlag(73900155)
    Restart()


@RestartOnRest(13900729)
def Event_13900729(_, character: int):
    """Event 13900729"""
    if ThisEventSlotFlagEnabled():
        return
    AND_2.Add(FlagEnabled(1383))
    AND_2.Add(FlagEnabled(73500105))
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(1385))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1395))
    AND_1.Add(FlagEnabled(140))
    AND_1.Add(FlagEnabled(73700201))
    AND_1.Add(CharacterBackreadDisabled(3700715))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1386, state=FlagSetting.On)
    DisableCharacter(3700715)
    DisableBackread(3700715)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90890, skip_transition=True, unknown2=1.0)


@RestartOnRest(13905810)
def Event_13905810():
    """Event 13905810"""
    GotoIfFlagDisabled(Label.L0, flag=13900800)
    DisableCharacter(3900800)
    Kill(3900800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3900800)
    DisableCharacterCollision(3900800)
    DisableGravity(3900800)
    DisableAnimations(3900706)
    AND_3.Add(FlagEnabled(1388))
    AND_3.Add(FlagEnabled(1395))
    AND_3.Add(FlagEnabled(13900722))
    SkipLinesIfConditionTrue(1, AND_3)
    ForceAnimation(3900800, 30000, unknown2=1.0)
    AND_1.Add(FlagEnabled(13905805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3902800))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13900801)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    OR_1.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_1.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_1.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_1:
        return
    AND_2.Add(FlagEnabled(1388))
    AND_2.Add(FlagEnabled(1395))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Wait(1.5)
    ForceAnimation(3900800, 20010, unknown2=1.0)
    EnableCharacterCollision(3900800)
    EnableGravity(3900800)
    EnableAI(3900800)
    SetNetworkUpdateRate(3900800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3900800, name=905260)
    EnableFlag(13905812)
    SetNetworkConnectedFlagState(flag=13905730, state=FlagSetting.On)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L1, flag=13900722)
    GotoIfFlagEnabled(Label.L1, flag=13905730)
    Wait(1.0)
    PlayCutscene(39000020, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableFlag(13900722)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(3900800, destination=3902711, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacterCollision(3900800)
    EnableGravity(3900800)
    ForceAnimation(3900800, 20, loop=True, unknown2=1.0)
    EnableAI(3900800)
    SetNetworkUpdateRate(3900800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3900800, name=905260)
    EnableFlag(13905812)
    SetNetworkConnectedFlagState(flag=13905730, state=FlagSetting.On)
    EnableCharacter(3900706)
    EnableBackread(3900706)
    SetTeamType(3900706, TeamType.WhitePhantom)
    SetCharacterTalkRange(character=3900706, distance=100.0)
    EnableAI(3900706)
    SetCharacterEventTarget(3900706, region=3900800)
    ReplanAI(3900706)
    EnableAnimations(3900706)
    if PlayerNotInOwnWorld():
        return
    SetNetworkUpdateRate(3900706, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateAuthority(3900706, authority_level=UpdateAuthority.Forced)


@RestartOnRest(13905811)
def Event_13905811():
    """Event 13905811"""
    if FlagEnabled(13900800):
        return
    
    MAIN.Await(HealthRatioLessThanOrEqual(3900800, value=0.0))
    
    Wait(1.0)
    PlaySoundEffect(3900800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3900800))
    
    Wait(4.5)
    HandleBossDefeatAndDisplayBanner(boss=3900800, banner=BannerType.UnknownBossDefeat)
    EnableFlag(13900800)
    EnableFlag(9318)
    EnableFlag(6318)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(13905815)
def Event_13905815():
    """Event 13905815"""
    if FlagEnabled(13900800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3900800, tae_event_id=500))
    
    EnableFlag(13905815)
    End()


@RestartOnRest(13905816)
def Event_13905816():
    """Event 13905816"""
    DeleteVFX(3904810, erase_root_only=False)
    if FlagEnabled(13900800):
        return
    
    MAIN.Await(FlagEnabled(13905815))
    
    CreateVFX(3904810)
    
    MAIN.Await(FlagEnabled(13900800))
    
    DeleteVFX(3904810)


@RestartOnRest(13905820)
def Event_13905820():
    """Event 13905820"""
    RunCommonEvent(20005800, args=(13900800, 3901800, 3902800, 13905805, 3901800, 3900800, 0, 0))
    RunCommonEvent(20005801, args=(13900800, 3901800, 3902800, 13905730, 3901800, 13905806))
    RunCommonEvent(20005820, args=(13900800, 3901800, 3, 0))
    RunCommonEvent(20001836, args=(13900800, 13905805, 13905806, 13905812, 3904801, 3904802, 13905815))
    RunCommonEvent(20005837, args=(13900800, 3900800, 7.0, 5260, 5260, 13905805, 13905806), arg_types="iifiiii")
    RunCommonEvent(20005810, args=(13900800, 3901800, 3902800, 10000))


@RestartOnRest(13905830)
def Event_13905830(_, npc_part_id: short, part_index: short, part_health: int, npc_part_id_1: int, animation_id: int):
    """Event 13905830"""
    if FlagEnabled(13900800):
        return
    CreateNPCPart(3900800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    
    MAIN.Await(CharacterPartHealthLessThanOrEqual(3900800, npc_part_id=npc_part_id_1, value=0))
    
    GotoIfCharacterHasSpecialEffect(Label.L0, character=3900800, special_effect=5034)
    ForceAnimation(3900800, animation_id, skip_transition=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(13905835)
def Event_13905835():
    """Event 13905835"""
    if FlagEnabled(13900800):
        return
    AND_1.Add(CharacterHasSpecialEffect(3900800, 6071))
    AND_1.Add(CharacterBackreadEnabled(3900800))
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L0, character=3900800, special_effect=5034)
    ForceAnimation(3900800, 20002, skip_transition=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(13905840)
def Event_13905840():
    """Event 13905840"""
    if FlagEnabled(13900800):
        return
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3902800))
    
    AddSpecialEffect(PLAYER, 4510)
    AddSpecialEffect(3900706, 4510)
    Wait(1.0)
    Restart()


@RestartOnRest(13905850)
def Event_13905850():
    """Event 13905850"""
    if FlagEnabled(13900800):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=3900800))
    AND_1.Add(HealthRatioLessThanOrEqual(3900800, value=0.6000000238418579))
    OR_1.Add(AND_1)
    AND_2.Add(HealthRatioLessThanOrEqual(3900800, value=0.7900000214576721))
    AND_2.Add(CharacterHasSpecialEffect(3900800, 11421))
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(3900800, 5404))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(3900800, 5034))
    
    MAIN.Await(AND_3)
    
    WaitFrames(frames=1)
    ForceAnimation(3900800, 20005, skip_transition=True, unknown2=1.0)


@RestartOnRest(13905860)
def Event_13905860():
    """Event 13905860"""
    if FlagEnabled(13900800):
        return
    AND_1.Add(CharacterHasSpecialEffect(3900800, 11421))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3900800, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=3900800, attacker=3900706))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    OR_4.Add(CharacterHuman(PLAYER))
    OR_4.Add(CharacterHollow(PLAYER))
    GotoIfConditionTrue(Label.L1, input_condition=OR_4)
    GotoIfFlagEnabled(Label.L2, flag=13905862)
    GotoIfFlagEnabled(Label.L3, flag=13905863)
    GotoIfFlagEnabled(Label.L4, flag=13905864)
    GotoIfFlagEnabled(Label.L4, flag=13905865)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11444)
    SkipLines(1)
    AddSpecialEffect(3900800, 11445)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11446)
    SkipLines(1)
    AddSpecialEffect(3900800, 11447)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11448)
    SkipLines(1)
    AddSpecialEffect(3900800, 11449)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L5, flag=13905862)
    GotoIfFlagEnabled(Label.L6, flag=13905863)
    GotoIfFlagEnabled(Label.L7, flag=13905864)
    GotoIfFlagEnabled(Label.L7, flag=13905865)
    Goto(Label.L7)

    # --- Label 5 --- #
    DefineLabel(5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11438)
    SkipLines(1)
    AddSpecialEffect(3900800, 11439)
    Goto(Label.L20)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11440)
    SkipLines(1)
    AddSpecialEffect(3900800, 11441)
    Goto(Label.L20)

    # --- Label 7 --- #
    DefineLabel(7)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11442)
    SkipLines(1)
    AddSpecialEffect(3900800, 11443)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L8, flag=13905862)
    GotoIfFlagEnabled(Label.L9, flag=13905863)
    GotoIfFlagEnabled(Label.L10, flag=13905864)
    GotoIfFlagEnabled(Label.L10, flag=13905865)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11430)
    SkipLines(1)
    AddSpecialEffect(3900800, 11431)
    Goto(Label.L20)

    # --- Label 8 --- #
    DefineLabel(8)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11432)
    SkipLines(1)
    AddSpecialEffect(3900800, 11433)
    Goto(Label.L20)

    # --- Label 9 --- #
    DefineLabel(9)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11434)
    SkipLines(1)
    AddSpecialEffect(3900800, 11435)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=3900800, special_effect=5032)
    AddSpecialEffect(3900800, 11436)
    SkipLines(1)
    AddSpecialEffect(3900800, 11437)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(13905861)
def Event_13905861():
    """Event 13905861"""
    if FlagEnabled(13900800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13905805))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    GotoIfCoopClientCountComparison(Label.L0, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=2)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=3)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(1388):
        SetNetworkConnectedFlagState(flag=13905862, state=FlagSetting.On)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1388):
        SetNetworkConnectedFlagState(flag=13905863, state=FlagSetting.On)
    else:
        SetNetworkConnectedFlagState(flag=13905862, state=FlagSetting.On)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(1388):
        SetNetworkConnectedFlagState(flag=13905864, state=FlagSetting.On)
    else:
        SetNetworkConnectedFlagState(flag=13905863, state=FlagSetting.On)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagEnabled(1388):
        SetNetworkConnectedFlagState(flag=13905865, state=FlagSetting.On)
    else:
        SetNetworkConnectedFlagState(flag=13905864, state=FlagSetting.On)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(13905870)
def Event_13905870(_, obj: int, obj_1: int):
    """Event 13905870"""
    DisableNetworkSync()
    DisableObject(obj)
    DisableTreasure(obj=obj)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13900800):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3902890))
    
    OR_1.Add(PlayerHasWeapon(6370000, including_storage=True))
    OR_1.Add(PlayerHasWeapon(6370001, including_storage=True))
    OR_1.Add(PlayerHasWeapon(6370002, including_storage=True))
    OR_1.Add(PlayerHasWeapon(6370003, including_storage=True))
    OR_1.Add(PlayerHasWeapon(6370004, including_storage=True))
    OR_1.Add(PlayerHasWeapon(6370005, including_storage=True))
    if OR_1:
        return
    if FlagDisabled(53900810):
        return
    DisableObject(obj_1)
    EnableObject(obj)
    EnableTreasure(obj=obj)


@RestartOnRest(13905900)
def Event_13905900():
    """Event 13905900"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    OR_15.Add(CharacterHuman(PLAYER))
    OR_15.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_15)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3902900))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4400))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(TimeElapsed(seconds=6.0))
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4400))
    
    MAIN.Await(OR_1)
    
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4400):
        return RESTART
    if TryingToCreateSession():
        return RESTART
    if TryingToJoinSession():
        return RESTART
    PlayCutscene(39000010, cutscene_flags=0, player_id=10000, move_to_region=3202900, game_map=ARCHDRAGON_PEAK)
    SetRespawnPoint(respawn_point=3202900)
    SaveRequest()
    WaitFrames(frames=1)
    Restart()

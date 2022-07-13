"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=16000002, obj=16001952, unknown=5.0)
    RegisterGrace(grace_flag=16000003, obj=16001953, unknown=5.0)
    RegisterGrace(grace_flag=16000004, obj=16001954, unknown=5.0)
    RegisterGrace(grace_flag=16000005, obj=16001960, unknown=5.0)
    RegisterGrace(grace_flag=16000007, obj=16001964, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(16000800, 16000000, 16000950, 16001950, 20.0), arg_types="IIIIf")
    RunCommonEvent(1, 9005810, args=(16000850, 16000001, 16000951, 16001951, 8.0), arg_types="IIIIf")
    RunCommonEvent(2, 9005810, args=(16000860, 16000006, 16000962, 16001962, 8.0), arg_types="IIIIf")
    Event_16002810()
    Event_16002800()
    Event_16002811()
    Event_16002812()
    Event_16002822()
    Event_16002824()
    Event_16002826()
    Event_16002830()
    Event_16002832()
    Event_16002836()
    Event_16002838()
    Event_16002840()
    Event_16002842(0, character=16000800)
    Event_16002842(1, character=16000801)
    Event_16002849()
    Event_16002855()
    Event_16002850()
    Event_16002899()
    Event_16002865()
    Event_16002860()
    Event_16002889()
    Event_16002695()
    Event_16002690(0, flag=16002696, obj=16001690, obj_1=16001692)
    Event_16002691(0, obj=16001690, obj_1=16001692, destination=16002690)
    Event_16002620(0, flag=16000622, obj=16001622)
    Event_16002620(1, flag=16000624, obj=16001624)
    Event_16002625()
    Event_16002500()
    Event_16002650()
    RunCommonEvent(0, 90005515, args=(16008544, 16001544), arg_types="II")
    RunCommonEvent(0, 90005515, args=(16008546, 16001546), arg_types="II")
    RunCommonEvent(0, 90005515, args=(16008548, 16001548), arg_types="II")
    RunCommonEvent(0, 90005515, args=(16008542, 16001542), arg_types="II")
    RunCommonEvent(0, 90005515, args=(16008552, 16001552), arg_types="II")
    RunCommonEvent(0, 90005515, args=(16008556, 16001556), arg_types="II")
    RunCommonEvent(0, 90005515, args=(16008554, 16001554), arg_types="II")
    RunCommonEvent(0, 90005510, args=(16000552, 16001552, 16003552, 1277018, 208134, 0), arg_types="IIIiiI")
    RunCommonEvent(0, 90005510, args=(16000564, 16001564, 16003564, 1277018, 208134, 0), arg_types="IIIiiI")
    RunCommonEvent(0, 90005510, args=(16000560, 16001560, 16003560, 1277018, 208134, 0), arg_types="IIIiiI")
    RunCommonEvent(0, 90005510, args=(16000562, 16001562, 16003562, 1277018, 208134, 0), arg_types="IIIiiI")
    Event_16002580()
    Event_16002510()
    RunCommonEvent(
        0,
        90005501,
        args=(16000510, 16001510, 0, 16001510, 16001511, 16001512, 16000511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(16000520, 16001520, 0, 16001520, 16001521, 16001522, 16000521),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005504, args=(16000525, 16001525, 0, 16001525, 16000526), arg_types="IIIII")
    RunCommonEvent(0, 90005504, args=(16000530, 16001530, 1, 16001530, 16000531), arg_types="IIIII")
    Event_16002640()
    Event_16002570(
        0,
        obj=16001570,
        area_id=16,
        block_id=0,
        cc_id=0,
        dd_id=0,
        player_start__region=16002570,
        unknown1=0,
        flag=16002574,
        left_flag=16002572,
        cancel_flag__right_flag=16002573
    )
    Event_16002579()
    Event_16002689()
    Event_16002670()
    RunCommonEvent(0, 900005610, args=(16001670, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(16001671, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005502, args=(16000514, 16001512, 16002511), arg_types="III")
    Event_16002590()
    RunCommonEvent(0, 90005694, args=(16001651, 16001650, 201, 0, 200400, 0.75, 0.0, 1.0), arg_types="IIiiifff")
    Event_16002505()
    RunCommonEvent(
        0,
        90005620,
        args=(16000575, 16001575, 16001576, 0, 16002575, 16002576, 16002577),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(16000575, 16001578), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(16000565, 16001565, 16001566, 16001567, 16002565, 16002566, 16002567),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(16000565, 16001568), arg_types="II")
    RunCommonEvent(
        0,
        90005790,
        args=(0, 16000180, 16002181, 16002182, 16000180, 23, 16002180, 16002181, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(16000180, 16002181, 16002182, 16000180), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(16000180, 16002181, 16002182, 16000180, 16000940, 0.0), arg_types="IIIIif")
    Event_16002185(
        0,
        unk_0_4=16000180,
        flag=16002181,
        flag_1=16002182,
        flag_2=16000180,
        flag_3=16002180,
        region=16002182
    )
    RunCommonEvent(0, 90005702, args=(16000701, 3103, 3100, 3104), arg_types="IIII")
    Event_16003700(0, character=16000700, destination=16002700, character_1=16000740)
    Event_16003701(0, character=16000701, character_1=16000760, obj=16001709)
    Event_16003702(0, flag=400073)
    Event_16003703(0, obj=16001701, obj_1=16001706, obj_2=16001700)
    Event_16003704(0, flag=7602, flag_1=7603, flag_2=7604)
    Event_16003707(0, character=16000700, flag=16009270)
    Event_16003705(0, character=16000741, character_1=16000701)
    Event_16003706(0, character=16000741, character_1=16000701)
    Event_16003708()
    Event_16003709()
    RunCommonEvent(0, 90005750, args=(16001702, 4350, 100730, 400073, 400073, 16009208, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001703, 4350, 100740, 400074, 400074, 16009216, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001704, 4350, 100750, 400075, 400075, 16009217, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001708, 4350, 100725, 400070, 400072, 16009270, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001709, 4350, 100710, 400071, 400071, 16009266, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001702, 4350, 100760, 400076, 400076, 16009267, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001703, 4350, 100770, 400077, 400077, 16009268, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001704, 4350, 100780, 400078, 400078, 16009269, 6101), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005775, args=(80110000, 400290, -1.0), arg_types="iIf")
    RunCommonEvent(0, 90005775, args=(80392000, 400180, -1.0), arg_types="iIf")
    RunCommonEvent(0, 90005775, args=(81423900, 400073, -1.0), arg_types="iIf")
    RunCommonEvent(0, 90005775, args=(83395300, 400074, -1.0), arg_types="iIf")
    RunCommonEvent(0, 90005775, args=(85505600, 400075, -1.0), arg_types="iIf")
    Event_16003710(0, character=16000710)
    Event_16003712()
    RunCommonEvent(0, 90005702, args=(16000722, 3423, 3420, 3424), arg_types="IIII")
    Event_16003720(0, character=16000720, character_1=16000721)
    Event_16003722(0, character=16000722, character_1=16000723)
    Event_16003721(0, flag=16009208)
    Event_16003723(0, character=16000722, character_1=16000723)
    Event_16003724()
    Event_16003725()
    Event_16003726()
    Event_16003727()
    RunCommonEvent(0, 90005750, args=(16001720, 4350, 100910, 400091, 400091, 16009337, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(16001721, 4350, 100911, 400091, 400091, 16009338, 0), arg_types="IiiIIIi")
    Event_16003730(0, character=16000730)
    Event_16003731(0, flag=16009417, flag_1=16002731, flag_2=16009400)
    Event_16003740(0, character=16000750, obj=16001705, destination=16002710)
    Event_16003742(0, character=16000751, obj=16001711, obj_1=16001705)
    Event_16003741(0, flag=16009450)
    Event_16003743()
    RunCommonEvent(0, 90005750, args=(16001712, 4350, 102910, 400291, 400291, 16009463, 0), arg_types="IiiIIIi")
    Event_16003750(0, 16000801, 16000800, 9122, 16002805, 195.0)
    Event_16003760(0, character__obj=16000770)
    Event_16003761(0, character=16000770)
    Event_16003762(
        0,
        obj=16001707,
        action_button_id=4110,
        unk_0_4=2,
        first_flag=60802,
        last_flag=60802,
        flag=9122,
        model_point=0
    )
    Event_16003763()
    Event_16003764()
    Event_16003765()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(16000700)
    DisableBackread(16000701)
    DisableBackread(16000710)
    DisableBackread(16000720)
    DisableBackread(16000721)
    DisableBackread(16000722)
    DisableBackread(16000723)
    DisableBackread(16000730)
    DisableBackread(16000740)
    DisableBackread(16000741)
    DisableBackread(16000750)
    DisableBackread(16000751)
    DisableBackread(16000760)
    DisableBackread(16000770)
    EnableObjectInvulnerability(16001700)
    EnableObjectInvulnerability(16001701)
    EnableObjectInvulnerability(16001705)
    EnableObjectInvulnerability(16001706)
    Event_16000519()
    RunCommonEvent(0, 90005250, args=(16000345, 16002345, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000346, 16002345, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000348, 16002345, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000355, 16002355, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000344, 16002344, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000343, 16002343, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000349, 16002343, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000350, 16002343, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000354, 16002343, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(16000520, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 16002310, args=(16000316, 18.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000311, 25.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000224, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(16000225, 16002225, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000226, 16002225, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000212, 16002225, 8.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000227, 16002227, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(16000216, 13.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000210, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000219, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000220, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(16000410, 16002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000411, 16002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000460, 16002460, 0.0, 3012), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000500, 16002500, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000462, 16002462, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000203, 16002203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000204, 16002203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000205, 16002203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000206, 16002203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(16000207, 16002203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(16000322, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(16000314, 16002314, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(16000270, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000271, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000272, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000273, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000274, 3.0, 0.0, 3015), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000275, 6.0, 1.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000276, 3.0, 0.0, 3015), arg_types="Iffi")
    RunCommonEvent(0, 90005211, args=(16000277, 30001, 20020, 16002277, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(16000278, 16002278, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000279, 16002278, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000280, 16002278, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000281, 16002278, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000282, 16002278, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000283, 16002278, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(16000235, 14.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000238, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000236, 12.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000237, 5.0, 0.0, 3002), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000240, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005211, args=(16000510, 30001, 20001, 16002510, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005300, args=(16000512, 16000510, 16002000, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005261, args=(16000461, 16002461, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000338, 16002338, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000328, 16002339, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(16000339, 16002339, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(16000440, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(16000441, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(16000443, 30011, 20, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(16000445, 30011, 20, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005211, args=(16000446, 30011, 20, 16002446, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(16000327, 16002327, 3.0, 0.0, 3007), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(16000450, 30011, 20, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(16000451, 30011, 20, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_16009000()
    RunCommonEvent(0, 90005300, args=(16000420, 16000420, 40590, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(16000421, 16000421, 40592, 0.0, 0), arg_types="IIifi")


@RestartOnRest(16002185)
def Event_16002185(_, unk_0_4: uint, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, region: uint):
    """Event 16002185"""
    EndIfFlagEnabled(unk_0_4)
    IfFlagEnabled(AND_1, unk_0_4)
    IfFlagEnabled(AND_2, flag)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=region)
    IfConditionTrue(OR_10, input_condition=AND_1)
    IfConditionTrue(OR_10, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_10)
    EndIfFlagEnabled(unk_0_4)
    Unknown_2003_79(unk_0_4=unk_0_4)
    End()
    IfFlagDisabled(OR_11, flag_1)
    IfFlagDisabled(OR_11, flag_2)
    IfFlagDisabled(OR_11, flag_3)


@RestartOnRest(16002310)
def Event_16002310(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 16002310"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(character, 16002310, wait_for_completion=True)
    EnableAI(character)


@NeverRestart(16002500)
def Event_16002500():
    """Event 16002500"""
    GotoIfFlagDisabled(Label.L0, flag=16000500)
    EndOfAnimation(obj=16001500, animation_id=20)
    EndOfAnimation(obj=16001501, animation_id=1)
    DisableObjectActivation(16001501, obj_act_id=-1)
    DisableObject(16001660)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfTryingToJoinSession(AND_8)
    IfTryingToCreateSession(AND_7)
    IfConditionFalse(AND_8, input_condition=AND_7)
    GotoIfConditionTrue(Label.L1, input_condition=AND_8)
    EnableObjectActivation(16001501, obj_act_id=277081)
    IfPlayerInOwnWorld(AND_1)
    IfObjectActivated(OR_1, obj_act_id=16003501)
    IfTryingToJoinSession(AND_2)
    IfTryingToCreateSession(AND_3)
    IfConditionFalse(AND_2, input_condition=AND_3)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfTryingToJoinSession(AND_6)
    IfTryingToCreateSession(AND_5)
    IfConditionFalse(AND_6, input_condition=AND_5)
    GotoIfConditionTrue(Label.L1, input_condition=AND_6)
    EnableNetworkFlag(16000500)
    EnableNetworkFlag(9021)
    PlayCutscene(16000000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EndOfAnimation(obj=16001500, animation_id=20)
    DisableObject(16001660)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObjectActivation(16001501, obj_act_id=277081)
    Wait(1.0)
    Restart()


@NeverRestart(16002505)
def Event_16002505():
    """Event 16002505"""
    DisableObject(16001505)


@NeverRestart(16002510)
def Event_16002510():
    """Event 16002510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            16000510,
            16001510,
            0,
            16001510,
            16001511,
            16003511,
            16001512,
            16003512,
            16002511,
            16002512,
            16000511,
            16002512,
            16000514,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            16000520,
            16001520,
            0,
            16001520,
            16001521,
            16003521,
            16001522,
            16003522,
            16002521,
            16002522,
            16000521,
            16002522,
            16000850,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005503,
        args=(16000525, 16001525, 0, 16001525, 16002526, 16002527, 16002528, 16002529, 16000526, 16002527, 0),
        arg_types="IIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005503,
        args=(16000530, 16001530, 1, 16001530, 16002531, 16002532, 16002533, 16002534, 16000531, 16002532, 0),
        arg_types="IIIIIIIIIII",
    )


@NeverRestart(16000519)
def Event_16000519():
    """Event 16000519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(16000510)
    EnableFlag(16000515)
    DisableFlag(16000520)
    EnableFlag(16000525)


@RestartOnRest(16002650)
def Event_16002650():
    """Event 16002650"""
    EndIfFlagDisabled(16000540)
    EndIfPlayerNotInOwnWorld()
    EnableFlag(9080)
    DisableFlag(16000540)


@RestartOnRest(16002570)
def Event_16002570(
    _,
    obj: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start__region: uint,
    unknown1: int,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 16002570"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=806870)
    IfPlayerInOwnWorld(AND_1)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=obj)
    IfTryingToJoinSession(AND_4)
    IfTryingToCreateSession(AND_5)
    IfConditionFalse(AND_4, input_condition=AND_5)
    IfPlayerInOwnWorld(AND_7)
    IfTryingToJoinSession(AND_7)
    IfTryingToCreateSession(AND_7)
    IfActionButtonParamActivated(AND_7, action_button_id=9140, entity=obj)
    IfMultiplayerState(OR_2, state=MultiplayerState.Unknown6)
    IfFailedToCreateSession(OR_2)
    IfConditionTrue(AND_8, input_condition=OR_2)
    IfConditionTrue(OR_14, input_condition=AND_1)
    IfConditionTrue(OR_14, input_condition=AND_4)
    IfConditionTrue(OR_14, input_condition=AND_7)
    IfConditionTrue(OR_14, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_14)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_7)
    DeleteObjectVFX(obj)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L6, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    IfTryingToJoinSession(AND_10)
    IfTryingToCreateSession(AND_10)
    IfConditionTrue(OR_15, input_condition=AND_10)
    IfTryingToJoinSession(AND_11)
    IfConditionFalse(AND_12, input_condition=AND_11)
    IfTryingToCreateSession(AND_13)
    IfConditionFalse(AND_12, input_condition=AND_13)
    IfConditionTrue(OR_15, input_condition=AND_12)
    SkipLinesIfConditionTrue(1, OR_15)
    Restart()
    IfMultiplayerState(OR_4, state=MultiplayerState.Unknown6)
    IfFailedToCreateSession(OR_4)
    RestartIfConditionTrue(input_condition=OR_4)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    Wait(3.0)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=player_start__region,
        unknown2=10,
        character_2=PLAYER,
        unknown3=0,
        unknown4=1,
    )
    EnableNetworkFlag(16002578)
    Restart()
    SkipLines(1)
    DisableFlag(flag)
    SkipLines(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start__region, unknown1=unknown1)


@RestartOnRest(16002579)
def Event_16002579():
    """Event 16002579"""
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    IfFlagEnabled(MAIN, 16002578)
    Unknown_2004_74(
        character=20000,
        unknown1=1,
        region=16002575,
        unknown2=10,
        character_2=20000,
        unknown3=0,
        unknown4=1,
    )
    End()


@RestartOnRest(16002580)
def Event_16002580():
    """Event 16002580"""
    RegisterLadder(start_climbing_flag=16000580, stop_climbing_flag=16000581, obj=16001580)
    RegisterLadder(start_climbing_flag=16000582, stop_climbing_flag=16000583, obj=16001582)
    RegisterLadder(start_climbing_flag=16000590, stop_climbing_flag=16000591, obj=16001590)
    RegisterLadder(start_climbing_flag=16000592, stop_climbing_flag=16000593, obj=16001592)
    RegisterLadder(start_climbing_flag=16000594, stop_climbing_flag=16000595, obj=16001594)


@RestartOnRest(16002590)
def Event_16002590():
    """Event 16002590"""
    SkipLinesIfFlagDisabled(1, 16000520)
    EnableObjectActivation(16001522, obj_act_id=277021)
    EndIfFlagEnabled(16000850)
    ForceAnimation(16001520, 20, loop=True, unknown2=1.0)
    EnableFlag(16000520)
    EnableFlag(16001520)
    Wait(2.5)
    DisableObjectActivation(16001522, obj_act_id=277021)
    IfFlagEnabled(MAIN, 16000850)
    Wait(4.0)
    DisableFlag(16001520)
    DisableFlag(16000520)


@RestartOnRest(16002620)
def Event_16002620(_, flag: uint, obj: uint):
    """Event 16002620"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=obj, attacker=20000)
    IfEntityWithinDistance(OR_1, entity=obj, other_entity=PLAYER, radius=1.0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)


@RestartOnRest(16002625)
def Event_16002625():
    """Event 16002625"""
    EnableObjectInvulnerability(16001625)
    EnableObjectInvulnerability(16001626)


@RestartOnRest(16002640)
def Event_16002640():
    """Event 16002640"""
    GotoIfFlagDisabled(Label.L0, flag=16000640)
    DisableObject(16001640)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=16002640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(16001640)
    EnableFlag(16000640)


@RestartOnRest(16002670)
def Event_16002670():
    """Event 16002670"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_2, character=20000, region=16002670)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_3, character=20000, region=16002670)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Wait(0.10000000149011612)
    CancelSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(16002689)
def Event_16002689():
    """Event 16002689"""
    DisableNetworkSync()
    SkipLinesIfThisEventSlotFlagEnabled(1)
    DeleteVFX(16003680, erase_root_only=False)
    IfInsideMap(AND_1, game_map=VOLCANO_MANOR)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=16002680)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=16002681)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=16002682)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateVFX(16003680)
    Wait(1.0)
    IfOutsideMap(OR_1, game_map=VOLCANO_MANOR)
    IfCharacterOutsideRegion(OR_1, character=PLAYER, region=16002680)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=16002681)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=16002682)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DeleteVFX(16003680)
    Wait(1.0)
    Restart()


@RestartOnRest(16002690)
def Event_16002690(_, flag: uint, obj: uint, obj_1: uint):
    """Event 16002690"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16000800)
    EnableObject(obj)
    ForceAnimation(obj, 0, unknown2=1.0)
    IfFlagEnabled(MAIN, 16002695)
    IfFlagEnabled(AND_1, flag)
    SkipLinesIfConditionTrue(3, AND_1)
    DisableObject(obj)
    DeleteObjectVFX(obj_1)
    End()
    CreateObjectVFX(obj_1, vfx_id=90, model_point=6102)
    ForceAnimation(obj, 0, unknown2=1.0)
    EnableObjectActivation(obj, obj_act_id=99340)
    DisableFlag(16007690)


@RestartOnRest(16002691)
def Event_16002691(_, obj: uint, obj_1: uint, destination: uint):
    """Event 16002691"""
    IfFlagEnabled(OR_15, 16000800)
    IfPlayerNotInOwnWorld(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfActionButtonParamActivated(AND_2, action_button_id=9532, entity=obj_1)
    IfFlagEnabled(AND_2, 16002696)
    AwaitConditionTrue(AND_2)
    DeleteObjectVFX(obj_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 60530, unknown2=1.0)
    ForceAnimation(obj, 1, unknown2=1.0)
    Wait(2.799999952316284)
    DisableObject(obj)
    Wait(0.10000000149011612)
    AwardItemLot(16000690, host_only=False)


@RestartOnRest(16002695)
def Event_16002695():
    """Event 16002695"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16000800)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=16002165)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfPlayerHasWeapon(OR_4, 17030000, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030001, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030002, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030003, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030004, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030005, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030006, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030007, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030008, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030009, including_storage=True)
    IfPlayerHasWeapon(OR_4, 17030010, including_storage=True)
    SkipLinesIfConditionTrue(1, OR_4)
    EnableFlag(16002696)


@RestartOnRest(16002800)
def Event_16002800():
    """Event 16002800"""
    EndIfFlagEnabled(16000800)
    IfHealthValueLessThanOrEqual(MAIN, 16000800, value=0)
    Wait(4.0)
    PlaySoundEffect(16008000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 16000800)
    KillBossAndDisplayBanner(character=16000800, banner_type=BannerType.HollowArenaLoss)
    SkipLinesIfPlayerNotInOwnWorld(1)
    TriggerMultiplayerEvent(event_id=0)
    EnableFlag(16000800)
    EnableFlag(9122)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61122)
    CancelSpecialEffect(PLAYER, 1908)
    DeleteVFX(16002810)
    DeleteVFX(16002811)
    DeleteVFX(16002812)
    DeleteVFX(16002813)
    DeleteVFX(16002814)
    ChangeCamera(normal_camera_id=0, locked_camera_id=0)


@RestartOnRest(16002810)
def Event_16002810():
    """Event 16002810"""
    GotoIfFlagDisabled(Label.L0, flag=16000800)
    DisableCharacter(16005800)
    DisableAnimations(16005800)
    Kill(16005800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(16005800)
    DisableCharacter(16000800)
    DisableAnimations(16000800)
    Unknown_2004_73(entity=16000800, unk_4_8=0)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=16000801, radius=40.0)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=16000800, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_1, character=16000800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000800, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(16000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 16002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=16002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 1908)
    EnableAI(16000801)
    SetNetworkUpdateRate(16000801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(16000801, name=904710000)
    EnableFlag(16002803)
    SetLockOnPoint(character=16000801, lock_on_model_point=220, state=True)
    SetLockOnPoint(character=16000801, lock_on_model_point=221, state=False)
    EnableFlag(16002801)
    ForceAnimation(16000801, 20002, unknown2=1.0)


@RestartOnRest(16002811)
def Event_16002811():
    """Event 16002811"""
    EndIfFlagEnabled(16000800)
    IfPlayerInOwnWorld(AND_1)
    IfHealthRatioLessThanOrEqual(AND_1, 16000801, value=0.009999999776482582)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000801, 11955)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(0.10000000149011612)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=16000801, special_effect=11955)
    Restart()
    ForceAnimation(16000801, 20001, unknown2=1.0)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterAlive(AND_2, PLAYER)
    IfCharacterHasSpecialEffect(AND_2, 16000801, 11920)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(16000801, 30001, loop=True, unknown2=1.0)
    CancelSpecialEffect(16000801, 11943)
    CancelSpecialEffect(16000801, 11948)
    IfHealthRatioEqual(OR_9, PLAYER, value=0.0)
    IfCharacterDead(OR_9, PLAYER)
    EndIfConditionTrue(input_condition=OR_9)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=16000020,
        cutscene_flags=0,
        move_to_region=16002830,
        map_base_id=16,
        player_id=10000,
        unknown2=16,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(16000020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=-4.0, unknown2=0.0)
    EnableFlag(16002802)
    AddSpecialEffect(16000800, 11901)
    DisableCharacter(16000801)
    DisableAnimations(16000801)
    EnableCharacter(16000800)
    SetNetworkUpdateRate(16000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreateVFX(16002814)
    Move(
        16000800,
        destination=16002831,
        destination_type=CoordEntityType.Region,
        model_point=0,
        copy_draw_parent=16000801,
    )
    WaitFrames(frames=1)
    EnableAnimations(16000800)
    EnableAI(16000800)
    EnableBossHealthBar(16000800, name=904710001)
    SetLockOnPoint(character=16000800, lock_on_model_point=220, state=False)
    SetLockOnPoint(character=16000800, lock_on_model_point=221, state=True)
    ForceAnimation(16000800, 20002, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(16002812)
def Event_16002812():
    """Event 16002812"""
    EndIfFlagEnabled(16000800)
    IfHealthRatioLessThanOrEqual(AND_1, 16000800, value=0.5)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(16000800, 11902)


@RestartOnRest(16002822)
def Event_16002822():
    """Event 16002822"""
    IfCharacterBackreadEnabled(AND_1, 16000800)
    IfCharacterHasSpecialEffect(OR_1, 16000800, 11901)
    IfCharacterHasSpecialEffect(OR_1, 16000800, 11902)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterHasSpecialEffect(AND_1, 16000800, 11940)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11930)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11931)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11941)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11946)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11947)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    CreateVFX(16002810)
    AddSpecialEffect(16000800, 11930)
    Wait(1.0)
    Restart()


@RestartOnRest(16002824)
def Event_16002824():
    """Event 16002824"""
    IfCharacterBackreadEnabled(AND_1, 16000800)
    IfCharacterHasSpecialEffect(OR_1, 16000800, 11901)
    IfCharacterHasSpecialEffect(OR_1, 16000800, 11902)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterHasSpecialEffect(AND_1, 16000800, 11940)
    IfCharacterHasSpecialEffect(AND_1, 16000800, 11930)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11931)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11941)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11946)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11947)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    CreateVFX(16002811)
    DeleteVFX(16002810)
    AddSpecialEffect(16000800, 11931)
    CancelSpecialEffect(16000800, 11930)
    Wait(1.0)
    Restart()


@RestartOnRest(16002826)
def Event_16002826():
    """Event 16002826"""
    IfCharacterBackreadEnabled(AND_1, 16000800)
    IfCharacterHasSpecialEffect(OR_1, 16000800, 11901)
    IfCharacterHasSpecialEffect(OR_1, 16000800, 11902)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterHasSpecialEffect(AND_1, 16000800, 11940)
    IfCharacterHasSpecialEffect(AND_1, 16000800, 11931)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11930)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11941)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11946)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 16000800, 11947)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    CreateVFX(16002812)
    DeleteVFX(16002811)
    AddSpecialEffect(16000800, 11941)
    CancelSpecialEffect(16000800, 11931)
    Wait(1.0)
    Restart()


@RestartOnRest(16002830)
def Event_16002830():
    """Event 16002830"""
    EndIfFlagEnabled(16000800)
    IfCharacterHasSpecialEffect(MAIN, 16000800, 11942)
    CreateVFX(16002813)
    CancelSpecialEffect(16000800, 11941)
    AddSpecialEffect(16000800, 11947)
    ShootProjectile(
        owner_entity=16000800,
        source_entity=16001800,
        model_point=100,
        behavior_id=247100510,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=16000800,
        source_entity=16001800,
        model_point=100,
        behavior_id=247100810,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=16000800,
        source_entity=16001800,
        model_point=100,
        behavior_id=247100820,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=16000800,
        source_entity=16001800,
        model_point=100,
        behavior_id=247100830,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(25.0)
    AddSpecialEffect(16000800, 11945)
    Wait(1.0)
    Restart()


@RestartOnRest(16002832)
def Event_16002832():
    """Event 16002832"""
    IfCharacterHasSpecialEffect(MAIN, 16000800, 11946)
    DeleteVFX(16002810)
    DeleteVFX(16002811)
    DeleteVFX(16002812)
    DeleteVFX(16002813)
    CancelSpecialEffect(16000800, 11941)
    CancelSpecialEffect(16000800, 11945)
    CancelSpecialEffect(16000800, 11947)
    CancelSpecialEffect(16000800, 11946)
    Wait(1.0)
    Restart()


@RestartOnRest(16002836)
def Event_16002836():
    """Event 16002836"""
    DisableNetworkSync()
    EndIfFlagEnabled(16000800)
    EndIfFlagEnabled(16002802)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagDisabled(AND_1, 16002802)
    IfFlagEnabled(AND_1, 16002801)
    IfFlagEnabled(AND_1, 16002805)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangeCamera(normal_camera_id=4710, locked_camera_id=4712)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagDisabled(AND_2, 16002802)
    IfFlagEnabled(AND_2, 16002806)
    IfFlagEnabled(AND_2, 16002801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ChangeCamera(normal_camera_id=4710, locked_camera_id=4712)


@RestartOnRest(16002838)
def Event_16002838():
    """Event 16002838"""
    DisableNetworkSync()
    EndIfFlagEnabled(16000800)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(AND_1, 16002802)
    IfFlagEnabled(AND_1, 16002805)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangeCamera(normal_camera_id=4710, locked_camera_id=4711)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(AND_2, 16002802)
    IfFlagEnabled(AND_2, 16002806)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ChangeCamera(normal_camera_id=4710, locked_camera_id=4711)


@RestartOnRest(16002840)
def Event_16002840():
    """Event 16002840"""
    DisableNetworkSync()
    EndIfFlagEnabled(16000800)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=16002164)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 1908)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@RestartOnRest(16002842)
def Event_16002842(_, character: uint):
    """Event 16002842"""
    EndIfFlagEnabled(16000800)
    IfCharacterHasSpecialEffect(OR_10, character, 1929)
    IfCharacterHasSpecialEffect(OR_10, character, 1930)
    IfCharacterHasSpecialEffect(OR_10, character, 1931)
    IfCharacterHasSpecialEffect(OR_10, character, 1932)
    IfConditionTrue(MAIN, input_condition=OR_10)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=1929)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=1930)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=1931)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=1932)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(character, 19450)
    Goto(Label.L10)
    AddSpecialEffect(character, 19451)
    Goto(Label.L10)
    AddSpecialEffect(character, 19452)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(character, 19455)
    Goto(Label.L10)
    AddSpecialEffect(character, 19456)
    Goto(Label.L10)
    AddSpecialEffect(character, 19457)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(character, 19460)
    Goto(Label.L10)
    AddSpecialEffect(character, 19461)
    Goto(Label.L10)
    AddSpecialEffect(character, 19462)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(character, 19465)
    Goto(Label.L10)
    AddSpecialEffect(character, 19466)
    Goto(Label.L10)
    AddSpecialEffect(character, 19467)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(16002846)
def Event_16002846(
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
    """Event 16002846"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    SkipLinesIfUnsignedEqual(1, left=region_1, right=0)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region_1)
    IfFlagEnabled(OR_1, left)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    RestartIfFlagEnabled(flag)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    IfPlayerInOwnWorld(AND_3)
    IfFlagDisabled(AND_3, flag)
    IfActionButtonParamActivated(AND_3, action_button_id=action_button_id, entity=entity)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    RestartIfFlagEnabled(flag)
    UnknownSound_2010_11(unk_0_4=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(AND_4, input_condition=OR_5)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, flag)
    IfConditionTrue(OR_6, input_condition=AND_4)
    IfFlagEnabled(OR_6, flag)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFlagEnabled(flag)
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    IfPlayerInOwnWorld(AND_8)
    IfEntityWithinDistance(AND_8, entity=16000801, other_entity=PLAYER, radius=40.0)
    IfConditionTrue(MAIN, input_condition=AND_8)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    EndIfPlayerNotInOwnWorld()
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, flag)
    IfFailedToCreateSession(OR_10)
    IfMultiplayerState(OR_10, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=entity)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(16002849)
def Event_16002849():
    """Event 16002849"""
    Event_16002846(
        0,
        flag=16000800,
        entity=16001801,
        region=16002801,
        flag_1=16002805,
        character=16005800,
        action_button_id=10000,
        left=0,
        region_1=0
    )
    RunCommonEvent(0, 9005801, args=(16000800, 16001801, 16002801, 16002805, 16002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(16000800, 16001801, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(16000800, 471000, 16002805, 16002806, 16002803, 16002802, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(16002850)
def Event_16002850():
    """Event 16002850"""
    EndIfFlagEnabled(16000850)
    IfHealthValueLessThanOrEqual(MAIN, 16000850, value=0)
    Wait(4.0)
    PlaySoundEffect(16008000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 16000850)
    KillBossAndDisplayBanner(character=16000850, banner_type=BannerType.Unknown)
    EnableFlag(16000850)
    EnableFlag(9121)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61121)
    EnableTreasure(obj=16001681)
    DeleteObjectVFX(16001682)


@RestartOnRest(16002855)
def Event_16002855():
    """Event 16002855"""
    GotoIfFlagDisabled(Label.L0, flag=16000850)
    DisableCharacter(16000850)
    DisableAnimations(16000850)
    Kill(16000850)
    DeleteObjectVFX(16001682)
    SkipLinesIfFlagEnabled(1, 16007710)
    EnableTreasure(obj=16001681)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableTreasure(obj=16001681)
    CreateObjectVFX(16001682, vfx_id=90, model_point=6101)
    DisableAI(16000850)
    GotoIfFlagEnabled(Label.L1, flag=16000851)
    DisableCharacter(16000850)
    DisableAnimations(16000850)
    ForceAnimation(16000850, 30001, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=16000850, radius=26.0)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=16000850, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_1, character=16000850, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000850, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000850, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000850, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=16000850, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(16000851)
    EnableCharacter(16000850)
    EnableAnimations(16000850)
    EnableAI(16000850)
    ForceAnimation(16000850, 20001, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 16002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=16002850)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(16000850)
    SetNetworkUpdateRate(16000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(16000850, name=903570000)


@RestartOnRest(16002860)
def Event_16002860():
    """Event 16002860"""
    EndIfFlagEnabled(16000860)
    IfCharacterDead(AND_1, 16000860)
    IfCharacterDead(AND_1, 16000861)
    IfConditionTrue(MAIN, input_condition=AND_1)
    KillBossAndDisplayBanner(character=16000860, banner_type=BannerType.DutyFulfilled)
    EnableFlag(16000860)
    EnableFlag(9129)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61129)


@RestartOnRest(16002865)
def Event_16002865():
    """Event 16002865"""
    GotoIfFlagDisabled(Label.L0, flag=16000860)
    DisableCharacter(16000860)
    DisableAnimations(16000860)
    Kill(16000860)
    DisableCharacter(16000861)
    DisableAnimations(16000861)
    Kill(16000861)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(16000860)
    DisableAI(16000861)
    IfFlagEnabled(AND_2, 16002865)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=16002860)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(16000860)
    EnableAI(16000861)
    SetNetworkUpdateRate(16000860, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(16000861, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(16000860, name=904470000)
    EnableBossHealthBar(16000861, name=904470001, bar_slot=1)


@NeverRestart(16002889)
def Event_16002889():
    """Event 16002889"""
    RunCommonEvent(
        0,
        9005800,
        args=(16000860, 16001860, 16002860, 16002865, 16005860, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(16000860, 16001860, 16002860, 16002865, 16002866, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(16000860, 16001860, 4, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(16000860, 16001861, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(16000860, 931000, 16002865, 16002866, 0, 16002862, 0, 0), arg_types="IiIIIIii")


@NeverRestart(16002899)
def Event_16002899():
    """Event 16002899"""
    RunCommonEvent(
        0,
        9005800,
        args=(16000850, 16001850, 16002850, 16002855, 16005850, 10000, 16000851, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(16000850, 16001850, 16002850, 16002855, 16002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(16000850, 16001850, 4, 16000851), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(16000850, 16001851, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(16000850, 356000, 16002855, 16002856, 0, 16002852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(16009000)
def Event_16009000():
    """Event 16009000"""
    AwaitFlagEnabled(flag=16009213)
    IfCharacterBackreadEnabled(MAIN, PLAYER)
    UnknownCutscene_11(
        cutscene_id=16000010,
        cutscene_flags=0,
        move_to_region=16002840,
        map_base_id=16000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(16009213)
    ForceAnimation(20000, 60451, unknown2=1.0)


@RestartOnRest(16002900)
def Event_16002900():
    """Event 16002900"""
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=16000801, radius=30.0)
    SetLockedCameraSlot(area_id=16, block_id=0, camera_slot=1)
    IfEntityBeyondDistance(MAIN, entity=PLAYER, other_entity=16000801, radius=30.0)
    SetLockedCameraSlot(area_id=16, block_id=0, camera_slot=0)
    Restart()


@RestartOnRest(16003700)
def Event_16003700(_, character: uint, destination: uint, character_1: uint):
    """Event 16003700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3100)
    DisableFlag(16009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3105)
    GotoIfFlagEnabled(Label.L5, flag=3106)
    GotoIfFlagEnabled(Label.L5, flag=3107)
    GotoIfFlagEnabled(Label.L5, flag=3108)
    DisableCharacter(character)
    DisableBackread(character)
    EnableGravity(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(OR_3, 3105)
    IfFlagEnabled(OR_3, 3106)
    IfFlagEnabled(OR_3, 3107)
    IfFlagEnabled(OR_3, 3108)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3100)
    GotoIfFlagEnabled(Label.L2, flag=3101)
    GotoIfFlagEnabled(Label.L3, flag=3102)
    GotoIfFlagEnabled(Label.L4, flag=3103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    DisableGravity(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100, unknown2=1.0)
    ForceAnimation(character_1, 930010, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3105)
    IfFlagEnabled(OR_4, 3106)
    IfFlagEnabled(OR_4, 3107)
    IfFlagEnabled(OR_4, 3108)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(16003701)
def Event_16003701(_, character: uint, character_1: uint, obj: uint):
    """Event 16003701"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3100)
    DisableFlag(16009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3109)
    GotoIfFlagEnabled(Label.L5, flag=3110)
    GotoIfFlagEnabled(Label.L5, flag=3111)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(OR_3, 3109)
    IfFlagEnabled(OR_3, 3110)
    IfFlagEnabled(OR_3, 3111)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    MoveObjectToCharacter(obj, character=character)
    GotoIfFlagEnabled(Label.L1, flag=3100)
    GotoIfFlagEnabled(Label.L2, flag=3101)
    GotoIfFlagEnabled(Label.L3, flag=3102)
    GotoIfFlagEnabled(Label.L4, flag=3103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101, unknown2=1.0)
    SkipLinesIfFlagDisabled(2, 3110)
    ForceAnimation(character, 90102, unknown2=1.0)
    DisableAnimations(character)
    SkipLinesIfFlagDisabled(2, 3111)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    SkipLinesIfFlagDisabled(2, 3111)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    SkipLinesIfFlagDisabled(2, 3111)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    SkipLinesIfFlagDisabled(2, 3111)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3109)
    IfFlagEnabled(OR_4, 3110)
    IfFlagEnabled(OR_4, 3111)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(16003702)
def Event_16003702(_, flag: uint):
    """Event 16003702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3105)
    IfFlagEnabled(MAIN, flag)
    EnableFlag(3118)
    End()


@RestartOnRest(16003703)
def Event_16003703(_, obj: uint, obj_1: uint, obj_2: uint):
    """Event 16003703"""
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    RestoreObject(obj_1)
    EnableObjectInvulnerability(obj_1)
    RestoreObject(obj_2)
    EnableObjectInvulnerability(obj_2)
    End()


@RestartOnRest(16003704)
def Event_16003704(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 16003704"""
    IfEventValueGreaterThanOrEqual(AND_1, flag=16009260, bit_count=3, value=3)
    EndIfConditionTrue(input_condition=AND_1)
    EndIfFlagEnabled(3109)
    EndIfFlagEnabled(3110)
    EndIfFlagEnabled(3111)
    ClearEventValue(16009260, bit_count=3)
    EndIfFlagDisabled(flag)
    IncrementEventValue(16009260, bit_count=3, max_value=3)
    EndIfFlagDisabled(flag_1)
    IncrementEventValue(16009260, bit_count=3, max_value=3)
    EnableFlag(3438)
    EndIfFlagDisabled(flag_2)
    IncrementEventValue(16009260, bit_count=3, max_value=3)
    EnableFlag(3118)
    End()


@RestartOnRest(16003705)
def Event_16003705(_, character: uint, character_1: uint):
    """Event 16003705"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    DisableCharacter(character)
    DisableBackread(character)
    DisableImmortality(character_1)
    IfFlagEnabled(AND_1, 16009265)
    IfFlagDisabled(AND_1, 16009264)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    EndIfFlagEnabled(16009264)
    EndIfFlagDisabled(3109)
    DisableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character_1)
    SetCharacterTalkRange(character=character_1, distance=50.0)
    IfAttackedWithDamageType(AND_2, attacked_entity=character_1, attacker=PLAYER)
    IfFlagDisabled(AND_2, 9000)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(16009265)
    ForceAnimation(character_1, 90201, unknown2=1.0)
    SetCharacterTalkRange(character=character_1, distance=17.0)
    Wait(7.0)
    EnableCharacter(character)
    ForceAnimation(character, 20021, unknown2=1.0)
    DisplayUnknownMessage_12(text=80020, unknown1=0)
    Wait(1.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    EnableBackread(character)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=character_1, radius=10.0)
    IfFlagDisabled(AND_3, 9000)
    IfConditionTrue(MAIN, input_condition=AND_3)
    DisableBackread(character_1)
    Wait(2.0)
    EnableCharacter(character)
    ForceAnimation(character, 20021, unknown2=1.0)
    DisplayUnknownMessage_12(text=80020, unknown1=0)
    Wait(1.0)
    Wait(4.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()


@RestartOnRest(16003706)
def Event_16003706(_, character: uint, character_1: uint):
    """Event 16003706"""
    EndIfFlagEnabled(16009264)
    IfCharacterDead(MAIN, character)
    DisplayUnknownMessage_12(text=80021, unknown1=0)
    EnableFlag(16009264)
    AwardItemLot(16000950, host_only=False)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    DisableAnimations(character_1)
    ForceAnimation(character_1, 90007, unknown2=1.0)
    Wait(2.0)
    ForceAnimation(character_1, 90202, unknown2=1.0)
    End()


@RestartOnRest(16003707)
def Event_16003707(_, character: uint, flag: uint):
    """Event 16003707"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_5, 400070)
    IfFlagEnabled(AND_5, 400072)
    SkipLinesIfConditionFalse(2, AND_5)
    DisableFlag(flag)
    End()
    GotoIfFlagEnabled(Label.L1, flag=flag)
    IfFlagDisabled(AND_1, 16009208)
    IfFlagEnabled(AND_1, 16000800)
    IfCharacterBackreadDisabled(AND_1, character)
    IfFlagDisabled(AND_2, 400070)
    IfFlagEnabled(AND_2, 16000800)
    IfFlagRangeAnyEnabled(AND_2, flag_range=(3109, 3111))
    IfCharacterBackreadDisabled(AND_2, character)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_6, 400070)
    IfFlagEnabled(AND_6, 400072)
    IfConditionTrue(MAIN, input_condition=AND_6)
    DisableFlag(flag)
    End()


@RestartOnRest(16003708)
def Event_16003708():
    """Event 16003708"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16009266)
    GotoIfFlagEnabled(Label.L1, flag=16009264)
    IfFlagEnabled(MAIN, 16009264)
    Wait(3.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(16009266)
    End()


@RestartOnRest(16003709)
def Event_16003709():
    """Event 16003709"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(16009267)
    DisableFlag(16009268)
    DisableFlag(16009269)
    EndIfFlagEnabled(400078)
    EndIfFlagDisabled(16000800)
    EndIfFlagDisabled(16009208)
    IfFlagEnabled(AND_3, 400075)
    IfFlagEnabled(AND_3, 7604)
    IfFlagDisabled(AND_3, 400078)
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    IfFlagEnabled(AND_2, 400074)
    IfFlagEnabled(AND_2, 7603)
    IfFlagDisabled(AND_2, 400077)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    IfFlagEnabled(AND_1, 400073)
    IfFlagEnabled(AND_1, 7602)
    IfFlagDisabled(AND_1, 400076)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(16009267)
    DisableFlag(16009268)
    DisableFlag(16009269)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(16009267)
    EnableFlag(16009268)
    DisableFlag(16009269)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(16009267)
    DisableFlag(16009268)
    EnableFlag(16009269)
    End()


@RestartOnRest(16003710)
def Event_16003710(_, character: uint):
    """Event 16003710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3689)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3689)
    IfConditionTrue(MAIN, input_condition=OR_3)
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
    ForceAnimation(character, 90100, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3689)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(16003711)
def Event_16003711(_, character: uint, flag: uint):
    """Event 16003711"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3681)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    DisableFlag(flag)
    SetTeamType(character, TeamType.NoTeam)
    EnableNetworkFlag(3698)
    End()


@RestartOnRest(16003712)
def Event_16003712():
    """Event 16003712"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16000800)
    IfFlagEnabled(MAIN, 16000800)
    EndIfFlagEnabled(3689)
    EndIfFlagEnabled(3690)
    EndIfFlagEnabled(3691)
    EndIfFlagEnabled(3692)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3683)
    SaveRequest()
    End()


@RestartOnRest(16003720)
def Event_16003720(_, character: uint, character_1: uint):
    """Event 16003720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3420)
    DisableFlag(1038519203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3427)
    GotoIfFlagEnabled(Label.L5, flag=3428)
    GotoIfFlagEnabled(Label.L5, flag=3430)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(OR_3, 3427)
    IfFlagEnabled(OR_3, 3428)
    IfFlagEnabled(OR_3, 3430)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    DisableBackread(character_1)
    DisableCharacter(character_1)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfFlagEnabled(Label.L20, flag=3430)
    IfFlagEnabled(AND_1, 16009308)
    IfFlagDisabled(AND_1, 16002710)
    SkipLinesIfConditionFalse(2, AND_1)
    Move(character, destination=16002730, destination_type=CoordEntityType.Region, short_move=True)
    Move(character_1, destination=16002730, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L20, flag=3428)
    IfFlagEnabled(AND_2, 16009308)
    IfFlagDisabled(AND_2, 16002710)
    IfFlagDisabled(AND_2, 16009306)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 16002711)
    SkipLinesIfConditionFalse(5, OR_2)
    DisableBackread(character)
    DisableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 930000, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3427)
    IfFlagEnabled(OR_4, 3428)
    IfFlagEnabled(OR_4, 3430)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(16003721)
def Event_16003721(_, flag: uint):
    """Event 16003721"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3420)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(16000800)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(3438)
    End()


@RestartOnRest(16003722)
def Event_16003722(_, character: uint, character_1: uint):
    """Event 16003722"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3420)
    DisableFlag(1038519203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3429)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(OR_3, 3429)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(1, 16009327)
    EnableFlag(16009329)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    DisableCharacter(character_1)
    ForceAnimation(character, 90101, unknown2=1.0)
    ForceAnimation(character_1, 930020, unknown2=1.0)
    GotoIfFlagDisabled(Label.L20, flag=16009329)
    ForceAnimation(character, 90102, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3429)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(16003723)
def Event_16003723(_, character: uint, character_1: uint):
    """Event 16003723"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(3429)
    EndIfFlagEnabled(3423)
    IfFlagEnabled(MAIN, 3423)
    Wait(3.5)
    EnableCharacter(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    DisableAnimations(character_1)
    Wait(5.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(16003724)
def Event_16003724():
    """Event 16003724"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16009316)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=16002731)
    EnableFlag(16009316)
    End()


@RestartOnRest(16003725)
def Event_16003725():
    """Event 16003725"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3431)
    EndIfFlagDisabled(16009319)
    GotoIfFlagEnabled(Label.L1, flag=16009327)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(16009338)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(16009337)
    End()


@RestartOnRest(16003726)
def Event_16003726():
    """Event 16003726"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16000800)
    EndIfFlagEnabled(16009208)
    EndIfFlagEnabled(16009309)
    EndIfFlagDisabled(1038519205)
    WaitFrames(frames=1)
    ForceAnimation(20000, 60451, unknown2=1.0)
    EnableFlag(16009309)
    End()


@RestartOnRest(16003727)
def Event_16003727():
    """Event 16003727"""
    WaitFramesAfterCutscene(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3429)
    WaitFramesAfterCutscene(frames=1)
    IfFlagDisabled(AND_1, 3105)
    IfFlagDisabled(AND_1, 3106)
    IfFlagDisabled(AND_1, 3107)
    IfFlagDisabled(AND_1, 3108)
    IfFlagDisabled(AND_1, 3689)
    IfFlagDisabled(AND_1, 3448)
    IfFlagDisabled(AND_1, 3449)
    IfFlagDisabled(AND_1, 3886)
    EndIfConditionFalse(input_condition=AND_1)
    EnableFlag(3438)
    End()


@RestartOnRest(16003730)
def Event_16003730(_, character: uint):
    """Event 16003730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    DisableFlag(16009400)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3440)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3448)
    IfFlagDisabled(AND_1, 16002731)
    IfFlagEnabled(AND_1, 3449)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    IfFlagDisabled(AND_2, 16009405)
    IfFlagEnabled(AND_2, 3449)
    GotoIfConditionTrue(Label.L5, input_condition=AND_2)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3448)
    IfFlagDisabled(AND_3, 16002731)
    IfFlagEnabled(AND_3, 3449)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfFlagDisabled(AND_4, 16009405)
    IfFlagEnabled(AND_4, 3449)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 3449)
    ForceAnimation(character, 90105, unknown2=1.0)
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
    IfFlagEnabled(OR_15, 3448)
    IfFlagDisabled(AND_10, 16002731)
    IfFlagEnabled(AND_10, 3449)
    IfConditionTrue(OR_15, input_condition=AND_10)
    IfFlagDisabled(AND_11, 16009405)
    IfFlagEnabled(AND_11, 3449)
    IfConditionTrue(OR_15, input_condition=AND_11)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(16003731)
def Event_16003731(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 16003731"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3449)
    EndIfFlagEnabled(flag)
    EnableFlag(flag)
    EnableFlag(flag_1)
    WaitFrames(frames=1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(16003740)
def Event_16003740(_, character: uint, obj: uint, destination: uint):
    """Event 16003740"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3880)
    DisableFlag(1042389253)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3886)
    DisableCharacter(character)
    DisableBackread(character)
    EnableGravity(character)
    DisableObjectInvulnerability(obj)
    IfFlagEnabled(OR_3, 3886)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3880)
    GotoIfFlagEnabled(Label.L2, flag=3881)
    GotoIfFlagEnabled(Label.L3, flag=3882)
    GotoIfFlagEnabled(Label.L4, flag=3883)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    DisableGravity(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3886)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(16003741)
def Event_16003741(_, flag: uint):
    """Event 16003741"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3880)
    EndIfFlagEnabled(16009208)
    IfFlagEnabled(AND_1, 16009208)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(3898)
    WaitFrames(frames=1)
    EnableFlag(flag)
    End()


@RestartOnRest(16003742)
def Event_16003742(_, character: uint, obj: uint, obj_1: uint):
    """Event 16003742"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3887)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    EnableObject(obj_1)
    IfFlagEnabled(OR_3, 3887)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3880)
    GotoIfFlagEnabled(Label.L2, flag=3881)
    GotoIfFlagEnabled(Label.L3, flag=3882)
    GotoIfFlagEnabled(Label.L4, flag=3883)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(obj)
    DisableObject(obj_1)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(obj)
    DisableObject(obj_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(obj)
    DisableObject(obj_1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(obj)
    DisableObject(obj_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3887)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(16003743)
def Event_16003743():
    """Event 16003743"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 3887)
    IfFlagEnabled(AND_1, 7605)
    IfFlagDisabled(AND_1, 400291)
    EndIfConditionFalse(input_condition=AND_1)
    EnableFlag(16009463)
    End()


@RestartOnRest(16003750)
def Event_16003750(_, character: uint, character_1: uint, flag: uint, flag_1: uint, distance: float):
    """Event 16003750"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=character, distance=17.0)
    SkipLinesIfUnsignedEqual(1, left=0, right=character_1)
    SetCharacterTalkRange(character=character_1, distance=17.0)
    EndIfFlagEnabled(flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, flag_1)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetCharacterTalkRange(character=character, distance=distance)
    SkipLinesIfUnsignedEqual(1, left=0, right=character_1)
    SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(16003760)
def Event_16003760(_, character__obj: uint):
    """Event 16003760"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3780)
    IfFlagEnabled(AND_1, 16009503)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(16009503)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    IfFlagEnabled(AND_5, 3785)
    IfFlagEnabled(AND_5, 16002756)
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
    IfFlagEnabled(AND_6, 3785)
    IfFlagEnabled(AND_6, 16002756)
    IfConditionTrue(MAIN, input_condition=AND_6)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=character__obj, distance=80.0)
    GotoIfFlagEnabled(Label.L1, flag=3780)
    GotoIfFlagEnabled(Label.L2, flag=3781)
    GotoIfFlagEnabled(Label.L4, flag=3783)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    SetTeamType(character__obj, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character__obj)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(AND_15, 3785)
    IfFlagEnabled(AND_15, 16002756)
    IfConditionFalse(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(16003761)
def Event_16003761(_, character: uint):
    """Event 16003761"""
    EndIfPlayerNotInOwnWorld()
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=character, radius=59.0)
    IfFlagEnabled(AND_1, 16002751)
    IfFlagDisabled(AND_1, 16009505)
    IfFlagEnabled(AND_1, 16002756)
    AwaitConditionTrue(AND_1)
    Move(character, destination=16002720, destination_type=CoordEntityType.Region, short_move=True)
    EnableFlag(16009508)
    End()


@RestartOnRest(16003762)
def Event_16003762(
    _,
    obj: uint,
    action_button_id: int,
    unk_0_4: int,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    model_point: int,
):
    """Event 16003762"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagRangeAnyDisabled(AND_1, flag_range=(first_flag, last_flag))
    AwaitConditionTrue(AND_1)
    SkipLinesIfValueEqual(2, left=model_point, right=0)
    CreateObjectVFX(obj, vfx_id=90, model_point=model_point)
    SkipLines(1)
    CreateObjectVFX(obj, vfx_id=90, model_point=6101)
    IfFlagDisabled(OR_2, flag)
    IfFlagRangeAllEnabled(OR_2, flag_range=(first_flag, last_flag))
    IfActionButtonParamActivated(OR_1, action_button_id=action_button_id, entity=obj)
    IfConditionTrue(OR_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    DeleteObjectVFX(obj)
    Unknown_2003_71(unk_0_4=unk_0_4)
    EnableNetworkFlag(first_flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(obj)
    Restart()


@RestartOnRest(16003763)
def Event_16003763():
    """Event 16003763"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L0, flag=16009509)
    GotoIfFlagDisabled(Label.L1, flag=16009510)
    GotoIfFlagDisabled(Label.L2, flag=16009511)
    Goto(Label.L3)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(16009509)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(16009510)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(16009511)
    EnableNetworkFlag(16002756)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableRandomFlagInRange(flag_range=(16002752, 16002756))
    End()


@RestartOnRest(16003764)
def Event_16003764():
    """Event 16003764"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16009505)
    IfFlagDisabled(AND_1, 16009505)
    IfFlagDisabled(AND_1, 16009508)
    IfFlagDisabled(AND_1, 16002751)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=16002721)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(16002750)
    End()


@RestartOnRest(16003765)
def Event_16003765():
    """Event 16003765"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(16009505)
    IfFlagDisabled(AND_1, 16009505)
    IfFlagEnabled(AND_1, 16009508)
    IfFlagDisabled(AND_1, 16002758)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=16002722)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(16002757)
    End()

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
    RegisterGrace(grace_flag=71223, obj=12021953, unknown=5.0)
    RegisterGrace(grace_flag=71224, obj=12021954, unknown=5.0)
    RegisterGrace(grace_flag=71226, obj=12021956, unknown=5.0)
    RegisterGrace(grace_flag=71227, obj=12021957, unknown=5.0)
    RegisterGrace(grace_flag=71228, obj=12021958, unknown=5.0)
    RegisterGrace(grace_flag=71229, obj=12021959, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(12020850, 71221, 12020951, 12021951, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 9005810, args=(12020800, 71220, 12020950, 12021950, 5.0), arg_types="IIIIf")
    Event_12022503()
    Event_12022580()
    RunCommonEvent(0, 90005920, args=(12020900, 12021900, 12023900), arg_types="III")
    RunCommonEvent(0, 900005610, args=(12021682, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(12021683, 100, 800, 0), arg_types="IiiI")
    Event_12022800()
    Event_12022810()
    Event_12022849()
    Event_12022820()
    Event_12022821()
    Event_12022850()
    Event_12022860()
    Event_12022865(0, character=12020860, character_1=12020850, region=63010)
    Event_12022899()
    RunCommonEvent(
        0,
        90005501,
        args=(12020520, 12021520, 5, 12021520, 1049401521, 12021522, 12020522),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005620,
        args=(12020570, 12021570, 12021571, 12021572, 12022570, 12022571, 12022572),
        arg_types="IIIIIIi",
    )
    Event_12022567(0, flag=12020570, region=12022570)
    Event_12022569(0, flag=12020524, flag_1=12020570)
    Event_12020500()
    RunCommonEvent(
        0,
        90005620,
        args=(12020575, 12021575, 12021576, 0, 12022575, 12022576, 12022577),
        arg_types="IIIIIIi",
    )
    Event_12022568(0, flag=12020575, obj=12021578)
    Event_12020510()
    Event_12022670()
    RunCommonEvent(
        0,
        90005605,
        args=(12021203, 12, 2, 0, 0, 12022203, 12020000, 12022203, 12022210, 12022211, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(
        0,
        90005605,
        args=(12021204, 12, 2, 0, 0, 12022204, 12020000, 12022204, 12022212, 12022213, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(
        0,
        90005605,
        args=(12021205, 12, 2, 0, 0, 12022205, 12020000, 12022205, 12022215, 12022206, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_12022600()
    Event_12022609()
    Event_12022620()
    Event_12022629()
    Event_12022601(0, flag=12020600, obj=12021600, obj_1=12021610)
    Event_12022601(1, flag=12020601, obj=12021601, obj_1=12021611)
    Event_12022601(2, flag=12020602, obj=12021602, obj_1=12021612)
    Event_12022601(3, flag=12020603, obj=12021603, obj_1=12021613)
    Event_12022601(4, flag=12020604, obj=12021604, obj_1=12021614)
    Event_12022601(5, flag=12020605, obj=12021605, obj_1=12021615)
    Event_12022601(6, flag=12020606, obj=12021606, obj_1=12021616)
    Event_12022601(7, flag=12020607, obj=12021607, obj_1=12021617)
    Event_12022621(0, flag=12020620, obj=12021620, obj_1=12021630)
    Event_12022621(1, flag=12020621, obj=12021621, obj_1=12021631)
    Event_12022621(2, flag=12020622, obj=12021622, obj_1=12021632)
    Event_12022621(3, flag=12020623, obj=12021623, obj_1=12021633)
    Event_12022621(4, flag=12020624, obj=12021624, obj_1=12021634)
    Event_12022621(5, flag=12020625, obj=12021625, obj_1=12021635)
    Event_12022621(6, flag=12020626, obj=12021626, obj_1=12021636)
    Event_12022621(7, flag=12020627, obj=12021627, obj_1=12021637)
    RunCommonEvent(0, 90005250, args=(12020211, 12022211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(12020220, 12022220, 70.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12020221, 12022220, 70.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005300, args=(12020221, 12020221, 0, 0.0, -1), arg_types="IIifi")
    Event_12022300(0, 12020300, 12022300, 0.0)
    Event_12022300(1, 12020301, 12022300, 0.0)
    Event_12022300(2, 12020303, 12022302, 0.0)
    RunCommonEvent(0, 90005250, args=(12020303, 12022302, 0.0, 3006), arg_types="IIfi")
    Event_12022300(3, 12025303, 12022303, 0.0)
    Event_12022300(4, 12025304, 12022304, 0.0)
    RunCommonEvent(0, 90005250, args=(12020304, 12022304, 0.0, -1), arg_types="IIfi")
    Event_12022300(5, 12025305, 12022305, 0.0)
    RunCommonEvent(0, 90005250, args=(12020310, 12022305, 2.0, 3011), arg_types="IIfi")
    Event_12022300(6, 12025306, 12022306, 0.0)
    Event_12022300(7, 12025307, 12022307, 0.0)
    Event_12022300(8, 12025308, 12022308, 0.0)
    Event_12022300(9, 12025309, 12022309, 0.0)
    RunCommonEvent(0, 90005251, args=(12020340, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12020341, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12020342, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12020343, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12020344, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(0, 0, 0.0, 0.0, 0), arg_types="IIffi")
    Event_12022300(10, 12025310, 12022310, 0.0)
    Event_12022300(11, 12025311, 12022311, 0.0)
    Event_12022300(12, 12025312, 12022312, 0.0)
    Event_12022300(13, 12020313, 12022313, 0.0)
    Event_12022300(15, 12025315, 12022315, 0.0)
    Event_12022300(16, 12020316, 12022316, 0.0)
    RunCommonEvent(0, 90005250, args=(12020316, 12022316, 0.0, 3006), arg_types="IIfi")
    Event_12022300(17, 12020317, 12022317, 0.0)
    Event_12022300(18, 12025318, 12022318, 0.0)
    Event_12022300(19, 12020319, 12022319, 0.0)
    RunCommonEvent(0, 90005250, args=(12020319, 12022319, 0.0, -1), arg_types="IIfi")
    Event_12022300(20, 12020331, 12022331, 0.0)
    Event_12022300(21, 12020334, 12022334, 0.0)
    Event_12022300(22, 12020335, 12022334, 0.0)
    Event_12022300(23, 12020336, 12022336, 3.0)
    Event_12022300(24, 12020337, 12022336, 0.0)
    RunCommonEvent(0, 90005250, args=(12020336, 12022336, 0.0, 3006), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020337, 12022336, 0.0, 3006), arg_types="IIfi")
    Event_12022300(25, 12025324, 12022314, 0.0)
    Event_12022300(26, 12025325, 12022314, 0.0)
    Event_12022300(29, 12025329, 12022329, 0.0)
    RunCommonEvent(0, 90005201, args=(12020376, 30011, 20011, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(12020377, 30011, 20011, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(12020378, 30011, 20011, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(12020379, 30011, 20011, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(12020348, 100.0, 0.0, -1), arg_types="Iffi")
    Event_12022350(0, character=12020390, character_1=12025350)
    Event_12022360(0, character=12020390, character_1=12025350)
    Event_12022370()
    Event_12022371()
    RunCommonEvent(0, 90005250, args=(12020390, 12022350, 3.0, -1), arg_types="IIfi")
    Event_12022372()
    Event_12022373()
    Event_12022350(1, character=12020391, character_1=12025351)
    Event_12022360(1, character=12020391, character_1=12025351)
    Event_12022350(2, character=12020392, character_1=12025352)
    Event_12022360(2, character=12020392, character_1=12025352)
    RunCommonEvent(0, 90005250, args=(12020350, 12022350, 3.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020351, 12022350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020368, 12022366, 0.0, 3006), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020368, 12022368, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005860, args=(12020830, 0, 12020830, 1, 30620, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(12020830, 904650600, 25), arg_types="IiI")
    RunCommonEvent(0, 90005251, args=(12020471, 30.0, 0.0, 3009), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(12020470, 12020470, 40648, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12020472, 12020472, 40630, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12020474, 12020474, 40610, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12020477, 12020477, 40642, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12020479, 12020479, 40646, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005250, args=(12020420, 12022420, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(12020421, 60.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12020424, 100.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(12020422, 12022422, 45.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(12020424, 60.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12020431, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(12020430, 12020430, 12020435, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12020431, 12020431, 12020445, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12020434, 12020434, 0, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005261, args=(12020440, 12022440, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12020442, 12022442, 15.0, 0.0, -1), arg_types="IIffi")
    Event_12022440(0, character=12020431, character_1=12020440, patrol_information_id=12023440)
    Event_12022440(1, character=12020431, character_1=12020441, patrol_information_id=12023440)
    Event_12022440(2, character=12020431, character_1=12020442, patrol_information_id=12023440)
    Event_12022440(3, character=12020447, character_1=12020444, patrol_information_id=12023444)
    Event_12022440(4, character=12020447, character_1=12020445, patrol_information_id=12023444)
    Event_12022440(5, character=12020447, character_1=12020446, patrol_information_id=12023444)
    Event_12022440(6, character=12020447, character_1=12020448, patrol_information_id=12023444)
    Event_12022440(7, character=12020447, character_1=12020449, patrol_information_id=12023444)
    RunCommonEvent(0, 90005250, args=(12020450, 12022450, 1.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020451, 12022450, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020452, 12022450, 3.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020453, 12022450, 2.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020454, 12022450, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12020455, 12022450, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(12025461, 20.0, 0.0, -1), arg_types="Iffi")
    Event_12022419(0, character=12020400, character_1=12020490, region=12022400)
    Event_12022400(1, character=12020380, character_1=12020491, region=12022401)
    RunCommonEvent(0, 90005261, args=(12020380, 12022411, 20.0, 0.0, -1), arg_types="IIffi")
    Event_12022400(2, character=12020402, character_1=12020492, region=12022402)
    RunCommonEvent(0, 90005261, args=(12020402, 12022412, 20.0, 0.0, -1), arg_types="IIffi")
    Event_12022400(3, character=12020403, character_1=12020493, region=12022403)
    Event_12022400(4, character=12020404, character_1=12020494, region=12022404)
    Event_12022400(5, character=12020405, character_1=12020495, region=12022405)
    Event_12022400(6, character=12020406, character_1=12020496, region=12022406)
    Event_12022400(7, character=12020407, character_1=12020497, region=12022407)
    Event_12022400(10, character=12020410, character_1=12020480, region=12022410)
    RunCommonEvent(0, 90005702, args=(12020710, 4063, 4060, 4063), arg_types="IIII")
    Event_12020700(0, character=12020710, obj=12021711, obj_1=12021710)
    Event_12020701(0, entity=12022716)
    RunCommonEvent(0, 90005752, args=(12021710, 200, 120, 3.0), arg_types="Iiif")
    Event_12023720(0, character=12020720)
    RunCommonEvent(0, 90005703, args=(12020720, 3601, 3602, 12029151, 3603, 3600, 3603, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(12020720, 3601, 3600, 12029151, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(12020720, 3603, 3600, 3603), arg_types="IIII")
    Event_12023721(0, 12021701, 3.0, 9710, 1034509410)
    Event_12023710(0, character=12020700, character_1=12020701)
    RunCommonEvent(0, 90005725, args=(4800, 4801, 4803, 12029105, 12020705, 1035450701, 12026700), arg_types="IIIIIII")
    RunCommonEvent(0, 90005703, args=(12020705, 4801, 4802, 12029106, 4801, 4800, 4804, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(12020705, 4801, 4800, 12029106, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(12020705, 4803, 4800, 4804), arg_types="IIII")
    RunCommonEvent(0, 90005706, args=(12020730, 930023, 0), arg_types="IiI")
    RunCommonEvent(
        0,
        90005780,
        args=(12020800, 12022160, 12022161, 12020715, 20, 12022716, 12029019, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(12020800, 12022160, 12022161, 12020715), arg_types="IIII")
    Event_12022699()
    Event_12022698()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(12020700)
    DisableBackread(12020720)
    DisableBackread(12020730)
    DisableObject(12021710)
    Event_12020519()
    RunEvent(12020050, slot=0, args=(0,))


@RestartOnRest(12022699)
def Event_12022699():
    """Event 12022699"""
    IfFlagEnabled(MAIN, 12022805)
    IfCharacterInsideRegion(AND_1, character=12020715, region=12022717)
    GotoIfConditionTrue(Label.L10, input_condition=AND_1)
    RunCommonEvent(0, 90005784, args=(12022160, 12022805, 12020715, 12022800, 12022809, 0), arg_types="IIIIIi")
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    End()


@RestartOnRest(12022698)
def Event_12022698():
    """Event 12022698"""
    EndIfFlagEnabled(12020800)
    IfFlagEnabled(OR_1, 12022160)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableMapCollision(collision=12021698)


@RestartOnRest(12022569)
def Event_12022569(_, flag: uint, flag_1: uint):
    """Event 12022569"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag)
    Restart()


@NeverRestart(12022568)
def Event_12022568(_, flag: uint, obj: uint):
    """Event 12022568"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=101, model_point=806043)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableObject(obj)


@NeverRestart(12022567)
def Event_12022567(_, flag: uint, region: uint):
    """Event 12022567"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@RestartOnRest(12022600)
def Event_12022600():
    """Event 12022600"""
    GotoIfFlagDisabled(Label.L0, flag=12020609)
    DeleteObjectVFX(12021609)
    CreateObjectVFX(12021609, vfx_id=200, model_point=812600)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(AND_15, 12020600)
    IfFlagEnabled(AND_15, 12020601)
    IfFlagEnabled(AND_15, 12020602)
    IfFlagEnabled(AND_15, 12020603)
    IfFlagEnabled(AND_15, 12020604)
    IfFlagEnabled(AND_15, 12020605)
    IfFlagEnabled(AND_15, 12020606)
    IfFlagEnabled(AND_15, 12020607)
    IfConditionTrue(MAIN, input_condition=AND_15)
    EnableNetworkFlag(12020609)
    DeleteObjectVFX(12021609)
    CreateObjectVFX(12021609, vfx_id=200, model_point=812600)
    Wait(3.0)
    DisplayDialog(text=30010, anchor_entity=0, display_distance=5.0)


@RestartOnRest(12022601)
def Event_12022601(_, flag: uint, obj: uint, obj_1: uint):
    """Event 12022601"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1)
    CreateObjectVFX(obj, vfx_id=200, model_point=812070)
    CreateObjectVFX(obj, vfx_id=201, model_point=812070)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=812070)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAnimations(PLAYER)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfActionButtonParamActivated(AND_2, action_button_id=9524, entity=obj)
    IfPlayerInOwnWorld(AND_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableAnimations(PLAYER)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(1.2999999523162842)
    EnableNetworkFlag(flag)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1)
    CreateObjectVFX(obj, vfx_id=200, model_point=812070)
    CreateObjectVFX(obj, vfx_id=201, model_point=812070)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=812070)
    Wait(2.0)
    EnableAnimations(PLAYER)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagEnabled(MAIN, flag)
    Wait(1.2999999523162842)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1)
    CreateObjectVFX(obj, vfx_id=200, model_point=812070)
    CreateObjectVFX(obj, vfx_id=201, model_point=812070)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=812070)
    End()


@NeverRestart(12022609)
def Event_12022609():
    """Event 12022609"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    GotoIfFlagDisabled(Label.L1, flag=12020609)
    DisableNetworkFlag(12022610)
    IfPlayerInOwnWorld(AND_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9525, entity=12021609)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableNetworkFlag(12022610)
    RotateToFaceEntity(PLAYER, 12021609, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(0.4000000059604645)
    BanishInvaders(unknown=0)
    Wait(1.0)
    Unknown_2004_74(character=PLAYER, unknown1=1, region=12082400, unknown2=-1, character_2=0, unknown3=0, unknown4=1)
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 12020609)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(input_condition=AND_15)
    IfFlagEnabled(MAIN, 12022610)
    Unknown_2004_74(character=PLAYER, unknown1=1, region=12022202, unknown2=-1, character_2=0, unknown3=0, unknown4=1)
    Wait(5.0)
    Unknown_2004_74(character=PLAYER, unknown1=1, region=12082401, unknown2=-1, character_2=0, unknown3=0, unknown4=1)
    Restart()


@RestartOnRest(12022620)
def Event_12022620():
    """Event 12022620"""
    GotoIfFlagDisabled(Label.L0, flag=12020629)
    DeleteObjectVFX(12021629)
    CreateObjectVFX(12021629, vfx_id=200, model_point=812600)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(AND_15, 12020620)
    IfFlagEnabled(AND_15, 12020621)
    IfFlagEnabled(AND_15, 12020622)
    IfFlagEnabled(AND_15, 12020623)
    IfFlagEnabled(AND_15, 12020624)
    IfFlagEnabled(AND_15, 12020625)
    IfConditionTrue(MAIN, input_condition=AND_15)
    EnableNetworkFlag(12020629)
    DeleteObjectVFX(12021629)
    CreateObjectVFX(12021629, vfx_id=200, model_point=812600)
    Wait(3.0)
    DisplayDialog(text=30010, anchor_entity=0, display_distance=5.0)


@RestartOnRest(12022621)
def Event_12022621(_, flag: uint, obj: uint, obj_1: uint):
    """Event 12022621"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1)
    CreateObjectVFX(obj, vfx_id=200, model_point=812070)
    CreateObjectVFX(obj, vfx_id=201, model_point=812070)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=812070)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    EnableAnimations(PLAYER)
    IfActionButtonParamActivated(AND_2, action_button_id=9524, entity=obj)
    IfPlayerInOwnWorld(AND_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    DisableAnimations(PLAYER)
    Wait(1.2999999523162842)
    EnableNetworkFlag(flag)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1)
    CreateObjectVFX(obj, vfx_id=200, model_point=812070)
    CreateObjectVFX(obj, vfx_id=201, model_point=812070)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=812070)
    Wait(2.0)
    EnableAnimations(PLAYER)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagEnabled(MAIN, flag)
    Wait(1.2999999523162842)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1)
    CreateObjectVFX(obj, vfx_id=200, model_point=812070)
    CreateObjectVFX(obj, vfx_id=201, model_point=812070)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=812070)
    End()


@NeverRestart(12022629)
def Event_12022629():
    """Event 12022629"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    GotoIfFlagDisabled(Label.L1, flag=12020629)
    DisableNetworkFlag(12022630)
    IfPlayerInOwnWorld(AND_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9525, entity=12021629)
    IfConditionTrue(MAIN, input_condition=AND_2)
    RotateToFaceEntity(PLAYER, 12021629, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    EnableNetworkFlag(12022630)
    Wait(0.4000000059604645)
    SkipLinesIfLeavingSession(4)
    SkipLinesIfFlagDisabled(2, 12090800)
    BanishPhantoms(unknown=0)
    SkipLines(1)
    BanishInvaders(unknown=0)
    Wait(2.0)
    Unknown_2004_74(character=PLAYER, unknown1=1, region=12092400, unknown2=-1, character_2=0, unknown3=0, unknown4=1)
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 12020629)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(input_condition=AND_15)
    IfFlagEnabled(MAIN, 12022630)
    Unknown_2004_74(character=PLAYER, unknown1=1, region=12022209, unknown2=-1, character_2=0, unknown3=0, unknown4=1)
    Wait(5.0)
    Unknown_2004_74(character=PLAYER, unknown1=1, region=12092401, unknown2=-1, character_2=0, unknown3=0, unknown4=1)
    Restart()


@NeverRestart(12022670)
def Event_12022670():
    """Event 12022670"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    DeleteObjectVFX(12021670)
    CreateObjectVFX(12021670, vfx_id=200, model_point=806870)
    DisableFlag(12022670)
    DisableFlag(12022671)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=12021670)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=12021670,
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
    RotateToFaceEntity(PLAYER, 12021670, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    Wait(3.0)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=12022670,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=0,
        unknown4=1,
    )
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagEnabled(MAIN, 12022670)
    Wait(3.0)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=12022671,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=0,
        unknown4=0,
    )
    Restart()


@RestartOnRest(12022580)
def Event_12022580():
    """Event 12022580"""
    RegisterLadder(start_climbing_flag=12020580, stop_climbing_flag=12020581, obj=12021580)
    RegisterLadder(start_climbing_flag=12020582, stop_climbing_flag=12020583, obj=12021582)
    RegisterLadder(start_climbing_flag=12020584, stop_climbing_flag=12020585, obj=12021584)


@RestartOnRest(12022680)
def Event_12022680():
    """Event 12022680"""
    CreateObjectVFX(12021682, vfx_id=100, model_point=800)
    CreateObjectVFX(12021683, vfx_id=100, model_point=800)


@RestartOnRest(12022200)
def Event_12022200(_, region: uint, character: uint, special_effect_id: int):
    """Event 12022200"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_4, input_condition=OR_1)
    IfCharacterInsideRegion(AND_4, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_4)
    CancelSpecialEffect(character, special_effect_id)


@RestartOnRest(12022404)
def Event_12022404():
    """Event 12022404"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(OR_15, 12020404, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_15, 12020494, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=OR_15)
    ChangePatrolBehavior(12020405, patrol_information_id=12023405)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(12022300)
def Event_12022300(_, character: uint, region: uint, seconds: float):
    """Event 12022300"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EnableCharacter(character)
    End()
    DisableCharacter(character)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_4, input_condition=OR_1)
    IfCharacterInsideRegion(AND_4, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_4)
    Wait(seconds)
    EnableCharacter(character)
    End()


@RestartOnRest(12022350)
def Event_12022350(_, character: uint, character_1: uint):
    """Event 12022350"""
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=60.0)
    IfCharacterHasSpecialEffect(AND_1, character, 5080)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=30)
    AddSpecialEffect(character_1, 13190)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12022360)
def Event_12022360(_, character: uint, character_1: uint):
    """Event 12022360"""
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=60.0)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 5080)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CancelSpecialEffect(character_1, 13190)
    WaitFrames(frames=30)
    Restart()


@RestartOnRest(12022370)
def Event_12022370():
    """Event 12022370"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(OR_15, 12020350, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_15, 12020351, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_15, 12020390, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=OR_15)
    ForceAnimation(12020390, 30003, loop=True, unknown2=1.0)
    End()


@RestartOnRest(12022371)
def Event_12022371():
    """Event 12022371"""
    GotoIfUnknown_1004_05(Label.L0, character=12020390, unk_8_12=True)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=12020390, radius=6.0)
    IfCharacterBackreadEnabled(AND_1, 12020390)
    IfCharacterHasSpecialEffect(OR_11, 12020390, 5080)
    IfCharacterHasSpecialEffect(OR_11, 12020390, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfCharacterHasSpecialEffect(AND_4, 12020390, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020390, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020390, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020390, 90160)
    IfCharacterHasSpecialEffect(AND_5, 12020390, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020390, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020390, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020390, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020390, 90162)
    IfCharacterHasSpecialEffect(AND_6, 12020390, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020390, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020390, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020390, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020390, 90161)
    IfCharacterHasSpecialEffect(AND_7, 12020390, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020390, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020390, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020390, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020390, 90162)
    IfCharacterHasSpecialEffect(AND_8, 12020390, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020390, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020390, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020390, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=12020390, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=12020390, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020390, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020390, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020390, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020390, unk_8_12=260, unk_12_16=1)
    IfCharacterDead(OR_2, 12020351)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    Unknown_2004_83(character=12020390, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 12020390, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 12020390, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(0.0)
    ForceAnimation(12020390, 20003, loop=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(12022372)
def Event_12022372():
    """Event 12022372"""
    GotoIfUnknown_1004_05(Label.L0, character=12020391, unk_8_12=True)
    ForceAnimation(12020391, 30003, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=12020391, radius=6.0)
    IfCharacterBackreadEnabled(AND_1, 12020391)
    IfCharacterHasSpecialEffect(OR_11, 12020391, 5080)
    IfCharacterHasSpecialEffect(OR_11, 12020391, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfCharacterHasSpecialEffect(AND_4, 12020391, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020391, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020391, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020391, 90160)
    IfCharacterHasSpecialEffect(AND_5, 12020391, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020391, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020391, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020391, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020391, 90162)
    IfCharacterHasSpecialEffect(AND_6, 12020391, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020391, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020391, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020391, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020391, 90161)
    IfCharacterHasSpecialEffect(AND_7, 12020391, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020391, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020391, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020391, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020391, 90162)
    IfCharacterHasSpecialEffect(AND_8, 12020391, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020391, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020391, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020391, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=12020391, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=12020391, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020391, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020391, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020391, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020391, unk_8_12=260, unk_12_16=1)
    IfCharacterDead(AND_13, 12020360)
    IfCharacterDead(AND_13, 12020353)
    IfCharacterDead(AND_13, 12020354)
    IfConditionTrue(OR_2, input_condition=AND_13)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=12020391, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 12020391, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 12020391, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(0.0)
    ForceAnimation(12020391, 20003, loop=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(12022373)
def Event_12022373():
    """Event 12022373"""
    GotoIfUnknown_1004_05(Label.L0, character=12020392, unk_8_12=True)
    ForceAnimation(12020392, 30003, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=12020392, radius=6.0)
    IfCharacterBackreadEnabled(AND_1, 12020392)
    IfCharacterHasSpecialEffect(OR_11, 12020392, 5080)
    IfCharacterHasSpecialEffect(OR_11, 12020392, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfCharacterHasSpecialEffect(AND_4, 12020392, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020392, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020392, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12020392, 90160)
    IfCharacterHasSpecialEffect(AND_5, 12020392, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020392, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020392, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020392, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12020392, 90162)
    IfCharacterHasSpecialEffect(AND_6, 12020392, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020392, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020392, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020392, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12020392, 90161)
    IfCharacterHasSpecialEffect(AND_7, 12020392, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020392, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020392, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020392, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12020392, 90162)
    IfCharacterHasSpecialEffect(AND_8, 12020392, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020392, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020392, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12020392, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=12020392, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=12020392, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020392, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020392, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020392, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12020392, unk_8_12=260, unk_12_16=1)
    IfCharacterDead(AND_13, 12020370)
    IfCharacterDead(AND_13, 12020371)
    IfCharacterDead(AND_13, 12020372)
    IfConditionTrue(OR_2, input_condition=AND_13)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=12020392, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 12020392, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 12020392, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(0.0)
    ForceAnimation(12020392, 20003, loop=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(12022400)
def Event_12022400(_, character: uint, character_1: uint, region: uint):
    """Event 12022400"""
    IfCharacterAlive(AND_15, character_1)
    SkipLinesIfConditionTrue(1, AND_15)
    DisableCharacter(character)
    IfThisEventSlotFlagEnabled(AND_1)
    IfPlayerNotInOwnWorld(AND_1)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    IfCharacterHasSpecialEffect(MAIN, character, 16307)
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
    ForceAnimation(character_1, 63010, skip_transition=True, unknown2=1.0)
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
    IfCharacterAlive(AND_15, character_1)
    SkipLinesIfConditionTrue(1, AND_15)
    DisableCharacter(character)
    IfThisEventSlotFlagEnabled(AND_1)
    IfPlayerNotInOwnWorld(AND_1)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    IfCharacterHasSpecialEffect(MAIN, character, 16309)
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
    ForceAnimation(character_1, 20015, skip_transition=True, unknown2=1.0)
    AddSpecialEffect(character_1, 16316)
    Wait(5.199999809265137)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    SetNest(character_1, region=region)


@RestartOnRest(12022440)
def Event_12022440(_, character: uint, character_1: uint, patrol_information_id: uint):
    """Event 12022440"""
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    ReplanAI(character_1)
    AddSpecialEffect(character_1, 5000)
    ChangePatrolBehavior(character_1, patrol_information_id=patrol_information_id)


@NeverRestart(12022502)
def Event_12022502():
    """Event 12022502"""
    DisableNetworkSync()
    IfFlagEnabled(AND_2, 12020800)
    IfPlayerInOwnWorld(AND_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9710, entity=12021502)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(12020502)
    Wait(0.10000000149011612)
    EnableFlag(9021)
    SetRespawnPoint(respawn_point=12032502)
    SaveRequest()
    UnknownCutscene_11(
        cutscene_id=12020000,
        cutscene_flags=0,
        move_to_region=12032502,
        map_base_id=12030000,
        player_id=10000,
        unknown2=12020000,
        unknown3=0,
    )
    PlayCutscene(12020001, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFrames(frames=1)
    Wait(1.0)
    DisplayUnknownMessage_14(text=12030)


@NeverRestart(12022503)
def Event_12022503():
    """Event 12022503"""
    SkipLinesIfFlagDisabled(2, 12020502)
    DeleteObjectVFX(12021950, erase_root=False)
    End()
    IfFlagEnabled(MAIN, 71220)
    DeleteObjectVFX(12021950)
    CreateObjectVFX(12021950, vfx_id=100, model_point=6400)


@NeverRestart(12020510)
def Event_12020510():
    """Event 12020510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            12020520,
            12020521,
            5,
            12021520,
            1049401521,
            1049403521,
            12021522,
            12023522,
            12022521,
            12022522,
            12020522,
            12022523,
            12020524,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
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
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(12020519)
def Event_12020519():
    """Event 12020519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(12020510)
    DisableFlag(12020520)
    EnableFlag(12020525)
    EnableFlag(12020530)


@NeverRestart(12020500)
def Event_12020500():
    """Event 12020500"""
    EndIfFlagEnabled(12020570)
    Wait(0.5)
    DisableObjectActivation(1049401521, obj_act_id=239020)
    IfFlagEnabled(MAIN, 12020570)
    EnableObjectActivation(1049401521, obj_act_id=239020)


@RestartOnRest(12022850)
def Event_12022850():
    """Event 12022850"""
    EndIfFlagEnabled(12020850)
    IfHealthValueLessThanOrEqual(OR_1, 12020850, value=0)
    IfHealthValueLessThanOrEqual(OR_1, 12020860, value=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(4.0)
    PlaySoundEffect(12020850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(OR_5, 12020850)
    IfCharacterDead(OR_5, 12020860)
    IfConditionTrue(MAIN, input_condition=OR_5)
    Kill(12020850, award_souls=True)
    WaitFrames(frames=1)
    KillBossAndDisplayBanner(character=12020850, banner_type=BannerType.Unknown)
    EnableFlag(12020850)
    EnableFlag(9134)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(91134)


@RestartOnRest(12022860)
def Event_12022860():
    """Event 12022860"""
    GotoIfFlagDisabled(Label.L0, flag=12020850)
    DisableCharacter(12020850)
    DisableAnimations(12020850)
    Kill(12020850)
    DisableCharacter(12020860)
    DisableAnimations(12020860)
    Kill(12020860)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfThisEventSlotFlagEnabled(AND_10)
    IfPlayerNotInOwnWorld(AND_10)
    EndIfConditionTrue(input_condition=AND_10)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableThisSlotFlag()
    DisableAI(12020850)
    DisableAI(12020860)
    GotoIfFlagEnabled(Label.L1, flag=12020851)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12022851)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=12020860, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=12020860, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020860, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020860, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020860, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020860, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(12020851)
    GotoIfPlayerNotInOwnWorld(Label.L15)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(12025850, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 15 --- #
    DefineLabel(15)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 12022855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=12022850)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfPlayerNotInOwnWorld(Label.L16)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(12025850, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 16 --- #
    DefineLabel(16)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    SetAIParamID(12020850, ai_param_id=90603100)
    EnableAI(12020860)
    ForceAnimation(12020860, 20010, unknown2=1.0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    Unknown_2004_67(character=PLAYER, entity=12020850)
    SetNetworkUpdateRate(12020850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNest(12020850, region=12022852)
    Wait(8.0)
    DisableCharacter(12020860)
    DisableAI(12020860)
    EnableAI(12020850)
    IfCharacterDead(AND_8, 12020850)
    SkipLinesIfConditionTrue(1, AND_8)
    EnableBossHealthBar(12020850, name=903320000)
    EnableNetworkFlag(12022858)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(12022865)
def Event_12022865(_, character: uint, character_1: uint, region: uint):
    """Event 12022865"""
    IfThisEventSlotFlagEnabled(AND_1)
    IfPlayerNotInOwnWorld(AND_1)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    IfCharacterHasSpecialEffect(MAIN, character, 16307)
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
    ForceAnimation(character_1, 63010, skip_transition=True, unknown2=1.0)
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

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    BanishInvaders(unknown=0)

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


@RestartOnRest(12022899)
def Event_12022899():
    """Event 12022899"""
    Event_12022869(
        0,
        flag=12020850,
        entity=12021850,
        region=12022850,
        flag_1=12022855,
        character=12025850,
        action_button_id=10000,
        left=0,
        region_1=12022851
    )
    RunCommonEvent(0, 9005801, args=(12020850, 12021850, 12022850, 12022855, 12022856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(12020850, 12021850, 8, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005812, args=(12020850, 12021851, 8, 0, 0), arg_types="IIiIi")
    RunCommonEvent(
        0,
        9005822,
        args=(12020850, 921100, 12022855, 12022856, 12022858, 12022852, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(12022800)
def Event_12022800():
    """Event 12022800"""
    EndIfFlagEnabled(12020800)
    IfHealthValueLessThanOrEqual(AND_1, 12020800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 12020801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(12020800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 12020800)
    IfCharacterDead(AND_2, 12020801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=12020800, banner_type=BannerType.Unknown)
    EnableFlag(12020800)
    EnableFlag(9110)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61110)


@RestartOnRest(12022810)
def Event_12022810():
    """Event 12022810"""
    GotoIfFlagDisabled(Label.L0, flag=12020800)
    DisableCharacter(12020800)
    DisableAnimations(12020800)
    Kill(12020800)
    DisableCharacter(12020801)
    DisableAnimations(12020801)
    Kill(12020801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12020800)
    DisableAI(12020801)
    SetNetworkUpdateRate(12020800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(12020800, 30002, unknown2=1.0)
    GotoIfFlagEnabled(Label.L1, flag=12020801)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12022801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=12020800, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=12020800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=12020800, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(12020801)
    ForceAnimation(12020800, 20002, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 12022805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=12022800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(12020800, 20002, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(12020800)
    EnableBossHealthBar(12020800, name=904770000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(12022820)
def Event_12022820():
    """Event 12022820"""
    EndIfFlagEnabled(12020800)
    ForceAnimation(12020801, 30003, loop=True, unknown2=1.0)
    DisableFlag(12022820)
    IfHealthRatioLessThanOrEqual(AND_1, 12020800, value=0.550000011920929)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(12020801, 20003, loop=True, unknown2=1.0)
    WaitFrames(frames=1)
    EnableAI(12020801)
    SetNetworkUpdateRate(12020801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(5.0)
    EnableBossHealthBar(12020801, name=904770001, bar_slot=1)
    AddSpecialEffect(12020800, 17648)
    AddSpecialEffect(12020801, 17648)
    EnableFlag(12022820)


@RestartOnRest(12022821)
def Event_12022821():
    """Event 12022821"""
    EndIfFlagEnabled(12020800)
    IfFlagEnabled(AND_1, 12022820)
    IfCharacterDead(OR_1, 12020800)
    IfCharacterDead(OR_1, 12020801)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CancelSpecialEffect(12020800, 17648)
    CancelSpecialEffect(12020801, 17648)


@RestartOnRest(12022849)
def Event_12022849():
    """Event 12022849"""
    RunCommonEvent(0, 9005811, args=(12020800, 12021801, 5, 12020801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(12020800, 931000, 12022805, 12022806, 0, 12022820, 0, 0), arg_types="IiIIIIii")
    RunCommonEvent(
        0,
        9005800,
        args=(12020800, 12021800, 12022800, 12022805, 12025800, 10000, 12020801, 12022801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(12020800, 12021800, 12022800, 12022805, 12022806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(12020800, 12021800, 3, 12020801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(12020800, 931000, 12022805, 12022806, 0, 12022802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(12020700)
def Event_12020700(_, character: uint, obj: uint, obj_1: uint):
    """Event 12020700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4060)
    DisableFlag(12029002)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4065)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    DisableObject(obj_1)
    IfFlagEnabled(MAIN, 4065)
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
    ForceAnimation(character, 90107, unknown2=1.0)
    EnableObject(obj)
    EnableObject(obj_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableObject(obj)
    DisableObject(obj_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    DisableObject(obj_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4065)
    Restart()


@RestartOnRest(12020701)
def Event_12020701(_, entity: uint):
    """Event 12020701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAnyEnabled(flag_range=(4066, 4077))
    IfFlagEnabled(AND_1, 4065)
    IfFlagEnabled(AND_1, 12029016)
    IfFlagEnabled(AND_1, 4048)
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
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
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3503)
    EndIfFlagEnabled(12029060)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=other_entity, radius=5.0)
    EnableFlag(flag)
    IfEntityBeyondDistance(MAIN, entity=PLAYER, other_entity=other_entity, radius=5.0)
    DisableFlag(flag)
    Restart()


@RestartOnRest(12023720)
def Event_12023720(_, character: uint):
    """Event 12023720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3600)
    DisableFlag(12029152)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L10, flag=3610)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3610)
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
    ForceAnimation(character, 930010, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 3610)
    Restart()


@RestartOnRest(12023721)
def Event_12023721(_, other_entity: uint, radius: float, special_effect_id: int, flag: uint):
    """Event 12023721"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=other_entity, radius=radius)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, special_effect_id)
    Wait(3.0)
    Restart()

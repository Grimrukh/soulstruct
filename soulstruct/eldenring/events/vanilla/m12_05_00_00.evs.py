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
    RegisterGrace(grace_flag=71251, obj=12051951, unknown=5.0)
    RegisterGrace(grace_flag=71252, obj=12051952, unknown=5.0)
    RegisterGrace(grace_flag=71253, obj=12051953, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(12050800, 12050000, 12050950, 12051950, 5.0), arg_types="IIIIf")
    Event_12052800()
    Event_12052810()
    Event_12052811()
    Event_12052849()
    Event_12052847()
    Event_12052848()
    Event_12052820()
    Event_12052821()
    Event_12052822()
    Event_12052823()
    Event_12052824()
    Event_12052825()
    Event_12052826()
    RunCommonEvent(0, 90005221, args=(12050200, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050202, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050203, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050204, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050205, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050206, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050207, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005251, args=(12050208, 40.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005221, args=(12050209, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050211, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050212, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005251, args=(12050213, 50.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005221, args=(12050214, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050215, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050216, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050217, 30003, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050218, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050219, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005271, args=(12050200, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050202, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050203, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050204, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050205, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050206, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050207, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050209, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050211, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050212, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050214, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050215, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050216, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050217, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050218, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(12050219, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005211, args=(12050224, 30002, 20002, 12052224, 1.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12050225, 30002, 20002, 12052224, 1.0, 4.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12050226, 30002, 20002, 12052224, 1.0, 4.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12050227, 30002, 20002, 12052224, 1.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12050229, 30002, 20002, 12052224, 1.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(12055220, 12052220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(12050232, 30001, 20001, 12052232, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12050233, 30001, 20001, 12052232, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(12050240, 12052240, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12050241, 12052240, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005271, args=(12055240, 0.0, -1), arg_types="Ifi")
    Event_12052250(0, character=12050250, frames=0, entity=12050360, animation_id=30010, animation_id_1=20010)
    Event_12052251(1, character=12050251, frames=1, entity=12050361, animation_id=30012, animation_id_1=20012)
    Event_12052251(2, character=12050252, frames=1, entity=12050362, animation_id=30011, animation_id_1=20011)
    Event_12052251(3, character=12050253, frames=1, entity=12050363, animation_id=30010, animation_id_1=20010)
    RunCommonEvent(0, 90005251, args=(12055260, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12055268, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12055270, 40.0, 1.5, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12055261, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12050261, 25.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005221, args=(12050263, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050264, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005201, args=(12050267, 30006, 20006, 20.0, 7.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005221, args=(12050266, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050265, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050277, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050278, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050279, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050280, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050281, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050282, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050283, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050284, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050285, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050286, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050287, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050288, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050289, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050290, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050291, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050292, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050293, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(12050297, 30006, 20006, 12052297, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005221, args=(12050298, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050299, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050300, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050301, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050302, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050303, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050304, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050305, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(12050306, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005261, args=(12050310, 12052311, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050311, 12052314, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050312, 12052314, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050313, 12052311, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050314, 12052311, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050315, 12052311, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050316, 12052311, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050317, 12052312, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050318, 12052312, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050319, 12052312, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050320, 12052313, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050321, 12052313, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050322, 12052313, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050323, 12052313, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050324, 12052313, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12050342, 12052342, 20.0, 0.0, 20000), arg_types="IIffi")
    Event_12052200()
    RunCommonEvent(0, 90005250, args=(12050346, 12052346, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(12050350, 30000, 20000, 12052350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(12050351, 12052351, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(12050352, 30000, 20000, 12052352, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12050353, 30000, 20000, 12052353, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_12052360(0, character=12050360, character_1=12050250)
    Event_12052360(1, character=12050361, character_1=12050251)
    Event_12052360(2, character=12050362, character_1=12050252)
    Event_12052360(3, character=12050363, character_1=12050253)
    RunCommonEvent(0, 90005251, args=(12050370, 60.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(12050400, 12050400, 40680, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12050401, 12050401, 40682, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12050402, 12050402, 40684, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12050403, 12050403, 40686, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005790,
        args=(12050800, 12050410, 12052410, 12052411, 12050410, 21, 12052410, 12052411, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(12050410, 12052410, 12052411, 12050410), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(12050410, 12052410, 12052411, 12050410, 0, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005790,
        args=(12050800, 12050412, 12052412, 12052413, 12050412, 22, 12052412, 12052413, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(12050412, 12052412, 12052413, 12050412), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(12050412, 12052412, 12052413, 12050412, 12050950, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005790,
        args=(12050800, 12050414, 12052414, 12052415, 12050414, 23, 12052414, 12052415, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(12050414, 12052414, 12052415, 12050414), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(12050414, 12052414, 12052415, 12050414, 0, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005501,
        args=(12050510, 12050511, 0, 12051510, 12051511, 12051512, 12050512),
        arg_types="IIIIIII",
    )
    Event_12052510()
    Event_12052680()
    RunCommonEvent(0, 900005610, args=(12051630, 100, 800, 0), arg_types="IiiI")
    Event_12052601(0, 12051600, 0.0)
    Event_12052601(1, 12051601, 1.0)
    Event_12052601(5, 12051605, 4.0)
    Event_12052601(6, 12051606, 3.0)
    Event_12052601(7, 12051607, 2.0)
    Event_12052601(8, 12051608, 1.5)
    Event_12052601(9, 12051609, 0.5)
    Event_12052601(11, 12051611, 3.0)
    Event_12052620(0, obj=12051620, flag=12050410, flag_1=12052410, region=12052411)
    Event_12052620(1, obj=12051621, flag=12050412, flag_1=12052412, region=12052413)
    Event_12052620(2, obj=12051622, flag=12050414, flag_1=12052414, region=12052415)
    Event_12052201()
    RunCommonEvent(
        0,
        90005795,
        args=(7601, 0, 1042369259, 12052141, 12052142, 80601, 9000, 12051700, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=20)
    RunCommonEvent(0, 90005796, args=(7601, 12050705, 5, 12052141), arg_types="IIBI")
    Event_1039532145()
    Event_12052690()
    Event_12053700(0, 12050800, 0, 9112, 12052805, 145.0)
    Event_12053701(0, character=12050800)
    RunCommonEvent(0, 90005703, args=(12050710, 4811, 4812, 12059106, 4811, 4810, 4814, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(12050710, 4811, 4810, 12059106, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(12050710, 4813, 4810, 4814), arg_types="IIII")
    RunCommonEvent(0, 90005725, args=(4810, 4811, 4813, 12059105, 12050710, 1035450701, 12056700), arg_types="IIIIIII")
    Event_12053710(0, character=12050702)
    Event_12053711(0, character=12050702)
    Event_12053712()
    RunCommonEvent(0, 90005750, args=(12051700, 4350, 100360, 400036, 400037, 12059166, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005702, args=(12050702, 3183, 3180, 3184), arg_types="IIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(12050700)
    DisableBackread(12050701)
    DisableBackread(12050702)
    DisableBackread(12050705)
    DisableBackread(12050710)
    DisableBackread(12050715)


@RestartOnRest(1039532145)
def Event_1039532145():
    """Event 1039532145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(12050705)
    SetTeamType(12050705, TeamType.Human)
    DeleteObjectVFX(12056710)
    CreateObjectVFX(12056710, vfx_id=200, model_point=806700)


@RestartOnRest(12052600)
def Event_12052600():
    """Event 12052600"""
    SetTeamType(12050600, TeamType.Boss)
    CreateProjectileOwner(entity=12050600)


@RestartOnRest(12052601)
def Event_12052601(_, source_entity: uint, seconds: float):
    """Event 12052601"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    Wait(seconds)
    DisableThisSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagDisabled(2, 50)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)
    SkipLinesIfFlagDisabled(2, 51)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)
    SkipLinesIfFlagDisabled(2, 52)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)
    SkipLinesIfFlagDisabled(2, 53)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)
    SkipLinesIfFlagDisabled(2, 54)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)
    SkipLinesIfFlagDisabled(2, 55)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)
    SkipLinesIfFlagDisabled(2, 56)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)
    ShootProjectile(
        owner_entity=12050600,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 10 --- #
    DefineLabel(10)
    WaitRandomSeconds(min_seconds=6.0, max_seconds=10.0)
    RestartIfConditionTrue(input_condition=MAIN)


@RestartOnRest(12052620)
def Event_12052620(_, obj: uint, flag: uint, flag_1: uint, region: uint):
    """Event 12052620"""
    EndIfFlagEnabled(flag)
    CreateObjectVFX(obj, vfx_id=100, model_point=812610)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_14, input_condition=OR_1)
    IfCharacterInsideRegion(AND_14, character=PLAYER, region=region)
    IfFlagEnabled(AND_14, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_14)
    DeleteObjectVFX(obj)
    WaitFrames(frames=1)
    CreateObjectVFX(obj, vfx_id=100, model_point=812611)
    Wait(4.0)
    DeleteObjectVFX(obj)


@RestartOnRest(12052200)
def Event_12052200():
    """Event 12052200"""
    GotoIfUnknown_1004_05(Label.L0, character=12050343, unk_8_12=True)
    ForceAnimation(12050343, 30013, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=12052343)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=12050343, radius=20.0)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfCharacterBackreadEnabled(AND_1, 12050343)
    IfCharacterHasSpecialEffect(OR_11, 12050343, 5080)
    IfCharacterHasSpecialEffect(OR_11, 12050343, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfCharacterHasSpecialEffect(AND_4, 12050343, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12050343, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12050343, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12050343, 90160)
    IfCharacterHasSpecialEffect(AND_5, 12050343, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12050343, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12050343, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12050343, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12050343, 90162)
    IfCharacterHasSpecialEffect(AND_6, 12050343, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12050343, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12050343, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12050343, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12050343, 90161)
    IfCharacterHasSpecialEffect(AND_7, 12050343, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12050343, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12050343, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12050343, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12050343, 90162)
    IfCharacterHasSpecialEffect(AND_8, 12050343, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12050343, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12050343, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12050343, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=12050343, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=12050343, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12050343, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12050343, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12050343, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12050343, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkUpdateRate(12050343, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=12050343, unk_4_8=1)
    ForceAnimation(12050343, 20000, loop=True, unknown2=1.0)
    Wait(3.0)
    SetNetworkUpdateRate(12050343, is_fixed=False, update_rate=CharacterUpdateRate.Never)


@RestartOnRest(12052201)
def Event_12052201():
    """Event 12052201"""
    EndIfThisEventSlotFlagEnabled()
    CreateTemporaryVFX(vfx_id=30010, anchor_entity=12052700, anchor_type=CoordEntityType.Region)


@RestartOnRest(12052250)
def Event_12052250(_, character: uint, frames: int, entity: uint, animation_id: int, animation_id_1: int):
    """Event 12052250"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(entity, animation_id, loop=True, wait_for_completion=True, unknown2=1.0)
    IfHasAIStatus(AND_14, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=AND_14)
    ForceAnimation(character, 3007, loop=True, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(entity, animation_id_1, loop=True, wait_for_completion=True, unknown2=1.0)
    End()
    WaitFrames(frames=frames)


@RestartOnRest(12052251)
def Event_12052251(_, character: uint, frames: int, entity: uint, animation_id: int, animation_id_1: int):
    """Event 12052251"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(entity, animation_id, loop=True, wait_for_completion=True, unknown2=1.0)
    IfHasAIStatus(AND_14, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=AND_14)
    ForceAnimation(character, 3007, loop=True, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(entity, animation_id_1, loop=True, wait_for_completion=True, unknown2=1.0)
    End()
    WaitFrames(frames=frames)


@RestartOnRest(12052360)
def Event_12052360(_, character: uint, character_1: uint):
    """Event 12052360"""
    IfCharacterDead(OR_15, character_1)
    IfHealthLessThanOrEqual(MAIN, character_1, value=0.699999988079071)
    SkipLinesIfConditionFalse(2, OR_15)
    Kill(character)
    End()
    SetTeamType(character, TeamType.Enemy)
    SetTeamType(character_1, TeamType.Enemy)
    IfCharacterDead(OR_12, character_1)
    IfHealthLessThanOrEqual(OR_12, character_1, value=0.699999988079071)
    IfConditionTrue(MAIN, input_condition=OR_12)
    Kill(character)
    End()


@RestartOnRest(12052680)
def Event_12052680():
    """Event 12052680"""
    DisableNetworkSync()
    SkipLinesIfThisEventSlotFlagEnabled(1)
    DeleteVFX(12053680, erase_root_only=False)
    IfPlayerStandingOnCollision(OR_1, 12054681)
    IfPlayerStandingOnCollision(OR_1, 12054682)
    IfPlayerStandingOnCollision(OR_1, 12054683)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12052680)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateVFX(12053680)
    Wait(1.0)
    IfCharacterOutsideRegion(OR_2, character=PLAYER, region=12052680)
    IfPlayerStandingOnCollision(OR_2, 12054681)
    IfPlayerStandingOnCollision(OR_2, 12054682)
    IfPlayerStandingOnCollision(OR_2, 12054683)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DeleteVFX(12053680)
    Wait(1.0)
    Restart()
    SetTeamType(0, TeamType.Enemy2)


@RestartOnRest(12052690)
def Event_12052690():
    """Event 12052690"""
    DisableNetworkSync()
    AwaitFlagEnabled(flag=12052140)
    AddSpecialEffect(12050102, 9531)
    AwaitFlagDisabled(flag=12052140)
    AddSpecialEffect(12050102, 9532)
    Wait(1.0)
    Restart()


@RestartOnRest(12052800)
def Event_12052800():
    """Event 12052800"""
    EndIfFlagEnabled(12050800)
    IfHealthValueLessThanOrEqual(MAIN, 12050800, value=0)
    Wait(4.0)
    PlaySoundEffect(12050800, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 12050800)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 12050800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    KillBossAndDisplayBanner(character=12050800, banner_type=BannerType.HollowArenaLoss)
    SkipLinesIfPlayerNotInOwnWorld(1)
    TriggerMultiplayerEvent(event_id=0)
    EnableFlag(12050800)
    EnableFlag(9112)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61112)


@RestartOnRest(12052810)
def Event_12052810():
    """Event 12052810"""
    GotoIfFlagDisabled(Label.L0, flag=12050800)
    DisableCharacter(12050800)
    DisableAnimations(12050800)
    Kill(12050800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12050800)
    GotoIfFlagEnabled(Label.L1, flag=12050801)
    DisableCharacter(12050800)
    DisableAnimations(12050800)
    Unknown_2004_73(entity=12050800, unk_4_8=0)
    EnableObject(12051820)
    DisableObject(12051821)
    DisableObject(12051822)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12052801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=12050800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(12050801)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=12050020,
        cutscene_flags=0,
        move_to_region=12052805,
        map_base_id=12050000,
        player_id=10000,
        unknown2=12050000,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(12050020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(12050802)
    EnableCharacter(12050800)
    EnableAnimations(12050800)
    ForceAnimation(12050800, 20020, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 12052805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=12052800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableObject(12051821)
    DisableObject(12051822)
    EnableAI(12050800)
    SetNetworkUpdateRate(12050800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(12050800, name=904800000)


@RestartOnRest(12052811)
def Event_12052811():
    """Event 12052811"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(MAIN, 12050800, 10630)
    EnableFlag(12052802)


@RestartOnRest(12052820)
def Event_12052820():
    """Event 12052820"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(MAIN, 12050800, 10641)
    AddSpecialEffect(PLAYER, 10650)


@RestartOnRest(12052821)
def Event_12052821():
    """Event 12052821"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(MAIN, 12050800, 10642)
    AddSpecialEffect(PLAYER, 10651)


@RestartOnRest(12052822)
def Event_12052822():
    """Event 12052822"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(MAIN, 12050800, 10643)
    AddSpecialEffect(PLAYER, 10652)


@RestartOnRest(12052823)
def Event_12052823():
    """Event 12052823"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(MAIN, 12050800, 10645)
    AddSpecialEffect(PLAYER, 10660)
    AddSpecialEffect(PLAYER, 10665)


@RestartOnRest(12052824)
def Event_12052824():
    """Event 12052824"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(MAIN, 12050800, 10646)
    AddSpecialEffect(PLAYER, 10661)
    AddSpecialEffect(PLAYER, 10666)


@RestartOnRest(12052825)
def Event_12052825():
    """Event 12052825"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(MAIN, 12050800, 10647)
    AddSpecialEffect(PLAYER, 10662)
    AddSpecialEffect(PLAYER, 10667)


@RestartOnRest(12052826)
def Event_12052826():
    """Event 12052826"""
    EndIfFlagEnabled(12050800)
    IfCharacterHasSpecialEffect(OR_1, 12050800, 10648)
    IfCharacterDead(OR_1, 12050800)
    IfConditionTrue(MAIN, input_condition=OR_1)
    AddSpecialEffect(PLAYER, 10653)


@RestartOnRest(12052847)
def Event_12052847():
    """Event 12052847"""
    EndIfFlagEnabled(12050801)
    IfFlagEnabled(MAIN, 12050801)
    DisableObject(12051820)
    DisableObject(12051821)
    EnableObject(12051822)
    End()


@RestartOnRest(12052848)
def Event_12052848():
    """Event 12052848"""
    GotoIfFlagDisabled(Label.L0, flag=12050803)
    DisableObject(12051820)
    EnableObject(12051821)
    DisableObject(12051822)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, 12050802)
    DisableObject(12051820)
    EnableObject(12051821)
    DisableObject(12051822)
    EnableNetworkFlag(12050803)
    End()


@RestartOnRest(12052849)
def Event_12052849():
    """Event 12052849"""
    RunCommonEvent(0, 9005811, args=(12050800, 12051801, 12, 12050801), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(12050800, 12051802, 12, 12050801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(12050800, 90003101, 12052805, 12052806, 0, 12052802, 0, 0), arg_types="IiIIIIii")
    RunCommonEvent(
        0,
        9005800,
        args=(12050800, 12051800, 12052800, 12052805, 12055800, 10000, 12050801, 12052801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(12050800, 12051800, 12052800, 12052805, 12052806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(12050800, 12051800, 4, 12050801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(12050800, 480000, 12052805, 12052806, 0, 12052802, 0, 0), arg_types="IiIIIIii")


@NeverRestart(12052510)
def Event_12052510():
    """Event 12052510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            12050510,
            12050511,
            0,
            12051510,
            12051511,
            12053511,
            12051512,
            12053512,
            12052511,
            12052512,
            12050512,
            12050513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(12053700)
def Event_12053700(_, character: uint, character_1: uint, flag: uint, flag_1: uint, distance: float):
    """Event 12053700"""
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


@RestartOnRest(12053701)
def Event_12053701(_, character: uint):
    """Event 12053701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(12050800)
    IfCharacterDead(MAIN, character)
    SetBackreadStateAlternate(character, True)
    IfFlagEnabled(OR_1, 12059205)
    IfTimeElapsed(OR_1, seconds=30.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetBackreadStateAlternate(character, False)
    End()


@RestartOnRest(12053710)
def Event_12053710(_, character: uint):
    """Event 12053710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3180)
    DisableFlag(1042369205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3193)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3193)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3180)
    GotoIfFlagEnabled(Label.L2, flag=3181)
    GotoIfFlagEnabled(Label.L3, flag=3182)
    GotoIfFlagEnabled(Label.L4, flag=3183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
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
    IfFlagEnabled(OR_4, 3193)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(12053711)
def Event_12053711(_, character: uint):
    """Event 12053711"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3183)
    EndIfFlagDisabled(3193)
    MoveObjectToCharacter(12051700, character=character)
    IfFlagEnabled(MAIN, 12059166)
    DisableAnimations(character)
    End()


@RestartOnRest(12053712)
def Event_12053712():
    """Event 12053712"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3192)
    EnableFlag(1042369259)
    End()

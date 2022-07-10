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
    RegisterGrace(grace_flag=34110000, obj=34111950, unknown=5.0)
    RegisterGrace(grace_flag=34110001, obj=34111951, unknown=5.0)
    RegisterGrace(grace_flag=34110002, obj=34111952, unknown=5.0)
    RunCommonEvent(
        0,
        90005501,
        args=(34110510, 34111510, 1, 34111510, 34111511, 34111512, 34110511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(34110515, 34111515, 0, 34111515, 34111516, 34111517, 34110516),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(34110520, 34111520, 0, 34111520, 34111521, 34111522, 34110521),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005508,
        args=(34110525, 34111525, 0, 34111525, 34111526, 34111527, 34110526),
        arg_types="IIIIIII",
    )
    Event_34112510()
    Event_34112580()
    RunCommonEvent(0, 900005610, args=(34111680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(34111681, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005300, args=(34110280, 34110280, 34110400, 0.0, 0), arg_types="IIifi")
    Event_34112400()
    Event_34112410()
    Event_34112420()
    Event_34112430()
    Event_34112440(0, region=34112440, region_1=34112450)
    Event_34112440(1, region=34112441, region_1=34112451)
    Event_34112440(2, region=34112442, region_1=34112452)
    Event_34112440(3, region=34112443, region_1=34112453)
    Event_34112440(4, region=34112444, region_1=34112454)
    Event_34112440(5, region=34112445, region_1=34112455)
    Event_34112440(6, region=34112446, region_1=34112456)
    Event_34112440(7, region=34112447, region_1=34112457)
    Event_34112448()
    Event_34112449()
    Event_34112459()
    RunCommonEvent(0, 90005300, args=(34110710, 34110710, 34110700, 0.0, 0), arg_types="IIifi")
    Event_34112460()
    Event_34112465()
    RunCommonEvent(0, 90005300, args=(34110711, 34110711, 34110710, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005706, args=(34110700, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_34112150()
    Event_34112151()
    DisableBackread(34110700)
    Event_34112519()
    RunCommonEvent(0, 90005271, args=(34110200, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110201, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110202, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110205, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110206, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110207, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110210, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110211, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110215, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110216, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(34110217, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005250, args=(34110230, 34112230, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110231, 34112230, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110232, 34112230, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110235, 34112235, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110236, 34112235, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110237, 34112235, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110240, 34112465, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110241, 34112465, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110245, 34112245, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110246, 34112245, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34110247, 34112245, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005210, args=(34110400, 30004, 20004, 34112200, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110401, 30004, 20004, 34112200, 5.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110402, 30004, 20004, 34112400, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110403, 30004, 20004, 34112400, 15.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110405, 30004, 20004, 34112405, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110406, 30004, 20004, 34112405, 20.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110407, 30004, 20004, 34112405, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110408, 30004, 20004, 34112405, 20.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110409, 30004, 20004, 34112405, 30.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110410, 30004, 20004, 34112409, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(34110411, 30004, 20004, 34112410, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110412, 30004, 20004, 34112410, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110413, 30004, 20004, 34112410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005210, args=(34110415, 30004, 20004, 34112441, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110416, 30004, 20004, 34112441, 15.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110417, 30004, 20004, 34112441, 15.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110418, 30004, 20004, 34112442, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110419, 30004, 20004, 34112443, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(34110420, 30004, 20004, 34112443, 20.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(34110421, 30004, 20004, 34112445, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110422, 30004, 20004, 34112445, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110423, 30004, 20004, 34112445, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110424, 30004, 20004, 34112445, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110425, 30004, 20004, 34112445, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110450, 30006, 20006, 34112465, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110451, 30006, 20006, 34112475, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(34110452, 30006, 20006, 34112475, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(34112150)
def Event_34112150():
    """Event 34112150"""
    GotoIfFlagEnabled(Label.L0, flag=370)
    EnableCharacter(34115150)
    EnableAnimations(34115150)
    DisableCharacter(34115160)
    DisableAnimations(34115160)
    EnableObject(34116150)
    DisableObject(34116160)
    EnableMapCollision(collision=34114150)
    EnableMapCollision(collision=34114151)
    EnableMapCollision(collision=34114152)
    EnableMapCollision(collision=34114153)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9720, entity=34111150)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfPlayerInOwnWorld(AND_9)
    IfPlayerHasGood(AND_9, 8111)
    GotoIfConditionTrue(Label.L1, input_condition=AND_9)
    Wait(0.10000000149011612)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisplayDialog(text=20040, anchor_entity=34111150, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(370)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(2)
    PlayCutscene(34110000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    UnknownCutscene_11(
        cutscene_id=34110000,
        cutscene_flags=0,
        move_to_region=34112505,
        map_base_id=34110000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    EndOfAnimation(obj=34111505, animation_id=1)
    RemoveGoodFromPlayer(item=8111, quantity=1)
    DisableCharacter(34115150)
    DisableAnimations(34115150)
    EnableCharacter(34115160)
    EnableAnimations(34115160)
    DisableObject(34116150)
    EnableObject(34116160)
    DisableMapCollision(collision=34114150)
    DisableMapCollision(collision=34114151)
    DisableMapCollision(collision=34114152)
    DisableMapCollision(collision=34114153)
    SkipLinesIfFlagDisabled(1, 34110510)
    DisableObjectActivation(34111512, obj_act_id=27002)
    SkipLinesIfFlagDisabled(1, 34110510)
    ForceAnimation(34111610, 10, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 34110515)
    ForceAnimation(34111615, 10, unknown2=1.0)
    WaitFrames(frames=1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(34115150)
    DisableAnimations(34115150)
    EnableCharacter(34115160)
    EnableAnimations(34115160)
    DisableObject(34116150)
    EnableObject(34116160)
    DisableMapCollision(collision=34114150)
    DisableMapCollision(collision=34114151)
    DisableMapCollision(collision=34114152)
    DisableMapCollision(collision=34114153)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9721, entity=34111150)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableNetworkFlag(370)
    EnableObject(34116150)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(2)
    PlayCutscene(34110001, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    UnknownCutscene_11(
        cutscene_id=34110001,
        cutscene_flags=0,
        move_to_region=34112505,
        map_base_id=34110000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    EndOfAnimation(obj=34111505, animation_id=0)
    EnableFlag(34112155)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8111, flag=34112155, bit_count=1)
    EnableCharacter(34115150)
    EnableAnimations(34115150)
    DisableCharacter(34115160)
    DisableAnimations(34115160)
    EnableObject(34116150)
    DisableObject(34116160)
    EnableMapCollision(collision=34114150)
    EnableMapCollision(collision=34114151)
    EnableMapCollision(collision=34114152)
    EnableMapCollision(collision=34114153)
    SkipLinesIfFlagDisabled(1, 34110510)
    EnableObjectActivation(34111512, obj_act_id=27002)
    WaitFrames(frames=1)
    Restart()


@NeverRestart(34112151)
def Event_34112151():
    """Event 34112151"""
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9730, entity=34111160)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=34110010,
        cutscene_flags=0,
        move_to_region=34112160,
        map_base_id=34110000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    UnknownCutscene_11(
        cutscene_id=34110010,
        cutscene_flags=0,
        move_to_region=34112160,
        map_base_id=34110000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    UnknownCamera_4(unknown1=-0.23999999463558197, unknown2=-104.94999694824219)
    EnableFlag(34110520)
    Restart()


@RestartOnRest(34112152)
def Event_34112152():
    """Event 34112152"""
    IfFlagDisabled(MAIN, 34110520)
    EndOfAnimation(obj=34111520, animation_id=10)


@NeverRestart(34112510)
def Event_34112510():
    """Event 34112510"""
    Event_34112900(
        0,
        34110510,
        34111510,
        1,
        34111510,
        34111511,
        34113511,
        34111512,
        34113512,
        34112511,
        34112512,
        34110511,
        34112512,
        0,
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            34110515,
            34111515,
            0,
            34111515,
            34111516,
            34113516,
            34111517,
            34113517,
            34112516,
            34112517,
            34110516,
            34112517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    Event_34112910(
        0,
        flag=34110520,
        flag_1=34111520,
        left=0,
        obj=34111520,
        obj_1=0,
        obj_act_id=0,
        obj_2=0,
        obj_act_id_1=0,
        region=34112521,
        region_1=34112522,
        flag_2=34110521,
        flag_3=0,
        left_1=0
    )
    RunCommonEvent(
        0,
        90005507,
        args=(
            34110525,
            34111525,
            0,
            34111525,
            34111526,
            34112528,
            34111527,
            34112529,
            34112526,
            34112527,
            34110526,
            34112527,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(34112519)
def Event_34112519():
    """Event 34112519"""
    EndIfThisEventSlotFlagEnabled()
    EndIfCharacterInsideRegion(character=PLAYER, region=34112152)
    EnableFlag(34110520)
    DisableThisSlotFlag()


@RestartOnRest(34112580)
def Event_34112580():
    """Event 34112580"""
    RegisterLadder(start_climbing_flag=34110530, stop_climbing_flag=34110531, obj=34111530)
    RegisterLadder(start_climbing_flag=34110532, stop_climbing_flag=34110533, obj=34111532)


@NeverRestart(34112900)
def Event_34112900(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_2: uint,
    obj_act_id_1: uint,
    region: uint,
    region_1: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 34112900"""
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_2)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableObjectActivation(obj_2, obj_act_id=-1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    IfObjectActivated(OR_1, obj_act_id=obj_act_id_1)
    IfFlagDisabled(OR_2, flag)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_3, left_1)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(AND_11, input_condition=OR_4)
    IfFlagDisabled(AND_11, 370)
    IfConditionTrue(MAIN, input_condition=AND_11)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAllPlayersOutsideRegion(OR_10, region=region_1)
    IfFlagEnabled(OR_10, flag)
    IfObjectBackreadEnabled(AND_10, obj=obj)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfConditionTrue(MAIN, input_condition=AND_10)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, skip_transition=True, unknown2=1.0)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    IfObjectActivated(OR_5, obj_act_id=obj_act_id)
    IfFlagEnabled(OR_6, flag)
    IfCharacterInsideRegion(AND_7, character=PLAYER, region=region_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_7, left_1)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(OR_8, input_condition=AND_7)
    IfConditionTrue(AND_12, input_condition=OR_8)
    IfFlagDisabled(AND_12, 370)
    IfConditionTrue(MAIN, input_condition=AND_12)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    IfAllPlayersOutsideRegion(OR_11, region=region)
    IfFlagDisabled(OR_11, flag)
    IfObjectBackreadEnabled(AND_2, obj=obj)
    IfConditionTrue(AND_2, input_condition=OR_11)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfPlayerNotInOwnWorld(Label.L6)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_2)
    Restart()


@NeverRestart(34112910)
def Event_34112910(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_2: uint,
    obj_act_id_1: uint,
    region: uint,
    region_1: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 34112910"""
    EndIfCharacterInsideRegion(character=PLAYER, region=34112152)
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_2)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableObjectActivation(obj_2, obj_act_id=-1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    IfObjectActivated(OR_1, obj_act_id=obj_act_id_1)
    IfFlagDisabled(OR_2, flag)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_3, left_1)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAllPlayersOutsideRegion(OR_10, region=region_1)
    IfFlagEnabled(OR_10, flag)
    IfObjectBackreadEnabled(AND_1, obj=obj)
    IfConditionTrue(AND_1, input_condition=OR_10)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfUnknown_204(Label.L3, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 12 --- #
    DefineLabel(12)
    SaveRequest()
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    IfObjectActivated(OR_5, obj_act_id=obj_act_id)
    IfFlagEnabled(OR_6, flag)
    IfCharacterInsideRegion(AND_7, character=PLAYER, region=region_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_7, left_1)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(OR_8, input_condition=AND_7)
    IfConditionTrue(MAIN, input_condition=OR_8)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    IfAllPlayersOutsideRegion(OR_11, region=region)
    IfFlagDisabled(OR_11, flag)
    IfObjectBackreadEnabled(AND_2, obj=obj)
    IfConditionTrue(AND_2, input_condition=OR_11)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfUnknown_204(Label.L6, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    SaveRequest()
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_2)
    Restart()


@RestartOnRest(34112400)
def Event_34112400():
    """Event 34112400"""
    EndIfFlagEnabled(34110710)
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(34110710)
    DisableAnimations(34110710)
    Unknown_2004_73(entity=34110710, unk_4_8=1)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34112400)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    EnableCharacter(34110710)
    EnableAnimations(34110710)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(34112410)
def Event_34112410():
    """Event 34112410"""
    EndIfFlagEnabled(34110710)
    EndIfThisEventSlotFlagEnabled()
    Unknown_2004_73(entity=34110710, unk_4_8=1)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfHealthLessThanOrEqual(AND_1, 34110710, value=0.800000011920929)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 34110710, 90)
    IfHealthValueGreaterThan(AND_1, 34110710, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetLockOnPoint(character=34110710, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    Move(34110710, destination=34112411, destination_type=CoordEntityType.Region, copy_draw_parent=34110710)
    SetNest(34110710, region=34112411)
    SetLockOnPoint(character=34110710, lock_on_model_point=220, state=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(34112420)
def Event_34112420():
    """Event 34112420"""
    EndIfFlagEnabled(34110710)
    EndIfThisEventSlotFlagEnabled()
    Unknown_2004_73(entity=34110710, unk_4_8=1)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfHealthLessThanOrEqual(AND_1, 34110710, value=0.6000000238418579)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 34110710, 90)
    IfHealthValueGreaterThan(AND_1, 34110710, value=0)
    IfFlagEnabled(AND_1, 34112410)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetLockOnPoint(character=34110710, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    Move(34110710, destination=34112421, destination_type=CoordEntityType.Region, copy_draw_parent=34110710)
    SetNest(34110710, region=34112421)
    SetLockOnPoint(character=34110710, lock_on_model_point=220, state=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(34112430)
def Event_34112430():
    """Event 34112430"""
    EndIfFlagEnabled(34110710)
    EndIfThisEventSlotFlagEnabled()
    Unknown_2004_73(entity=34110710, unk_4_8=1)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfHealthLessThanOrEqual(AND_1, 34110710, value=0.4000000059604645)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 34110710, 90)
    IfHealthValueGreaterThan(AND_1, 34110710, value=0)
    IfFlagEnabled(AND_1, 34112420)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetLockOnPoint(character=34110710, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    Move(34110710, destination=34112431, destination_type=CoordEntityType.Region, copy_draw_parent=34110710)
    SetNest(34110710, region=34112431)
    Wait(1.0)
    ReplanAI(34110710)
    Wait(0.10000000149011612)
    DisableAI(34110710)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(34112439)
def Event_34112439():
    """Event 34112439"""
    EndIfFlagEnabled(34110710)
    IfFlagRangeAllEnabled(MAIN, flag_range=(34112440, 34112447))
    DisableCharacter(34110710)


@RestartOnRest(34112440)
def Event_34112440(_, region: uint, region_1: uint):
    """Event 34112440"""
    EndIfFlagEnabled(34110710)
    EndIfFlagEnabled(34112448)
    EndIfFlagEnabled(34112459)
    Unknown_2004_73(entity=34110710, unk_4_8=1)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfFlagEnabled(AND_1, 34112410)
    IfFlagEnabled(AND_1, 34112420)
    IfFlagEnabled(AND_1, 34112430)
    IfFlagDisabled(AND_1, 34112448)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    EndIfFlagEnabled(34112459)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110710, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=34110710, model_point=151, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    Move(34110710, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=34110710)
    SetNest(34110710, region=region_1)
    Wait(4.0)
    Restart()


@RestartOnRest(34112448)
def Event_34112448():
    """Event 34112448"""
    EndIfFlagEnabled(34110710)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34112448)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ClearTargetList(34110710)
    AddSpecialEffect(34110710, 8082)
    DisableThisSlotFlag()


@RestartOnRest(34112449)
def Event_34112449():
    """Event 34112449"""
    EndIfFlagEnabled(34110710)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34112449)
    IfFlagEnabled(AND_1, 34112410)
    IfFlagEnabled(AND_1, 34112420)
    IfFlagEnabled(AND_1, 34112430)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetLockOnPoint(character=34110710, lock_on_model_point=220, state=True)
    EnableAI(34110710)
    SetAIParamID(34110710, ai_param_id=523520200)
    DisableThisSlotFlag()


@RestartOnRest(34112459)
def Event_34112459():
    """Event 34112459"""
    EndIfFlagEnabled(34110710)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=34110710, attacker=PLAYER)
    IfFlagEnabled(AND_1, 34112410)
    IfFlagEnabled(AND_1, 34112420)
    IfFlagEnabled(AND_1, 34112430)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableThisSlotFlag()


@RestartOnRest(34112460)
def Event_34112460():
    """Event 34112460"""
    EndIfFlagEnabled(34110711)
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(34110711)
    DisableAnimations(34110711)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34112460)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=34110711, model_point=151, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    EnableCharacter(34110711)
    EnableAnimations(34110711)
    DisableThisSlotFlag()


@RestartOnRest(34112465)
def Event_34112465():
    """Event 34112465"""
    EndIfFlagEnabled(34110711)
    EndIfFlagEnabled(34112496)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfHealthLessThanOrEqual(AND_1, 34110711, value=0.30000001192092896)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 34110711, 90)
    IfHealthValueGreaterThan(AND_1, 34110711, value=0)
    IfFlagDisabled(AND_1, 34112496)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfHealthValueEqual(OR_15, 34110711, value=0)
    EndIfConditionTrue(input_condition=OR_15)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=34110711, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=34110711, model_point=151, anchor_type=CoordEntityType.Character)
    Move(34110711, destination=34112466, destination_type=CoordEntityType.Region, copy_draw_parent=34110711)
    SetNest(34110711, region=34112466)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112475)
def Event_34112475():
    """Event 34112475"""
    EndIfFlagEnabled(34110711)
    EndIfFlagEnabled(34112496)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfHealthLessThanOrEqual(AND_1, 34110711, value=0.800000011920929)
    IfFlagEnabled(AND_1, 34112465)
    IfFlagDisabled(AND_1, 34112496)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=806910, anchor_entity=34110711, model_point=220, anchor_type=CoordEntityType.Character)
    Move(34110711, destination=34112476, destination_type=CoordEntityType.Region, copy_draw_parent=34110711)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112485)
def Event_34112485():
    """Event 34112485"""
    EndIfFlagEnabled(34110711)
    EndIfFlagEnabled(34112496)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34112480)
    IfFlagEnabled(AND_1, 34112465)
    IfFlagEnabled(AND_1, 34112475)
    IfFlagDisabled(AND_1, 34112496)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=806910, anchor_entity=34110711, model_point=220, anchor_type=CoordEntityType.Character)
    Move(34110711, destination=34112485, destination_type=CoordEntityType.Region, copy_draw_parent=34110711)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112492)
def Event_34112492():
    """Event 34112492"""
    IfFlagEnabled(OR_1, 34110711)
    IfThisEventSlotFlagEnabled(OR_1)
    EndIfConditionTrue(input_condition=OR_1)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=34112482)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=34112483)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=806910, anchor_entity=34110711, model_point=220, anchor_type=CoordEntityType.Character)
    Move(34110711, destination=34112492, destination_type=CoordEntityType.Region, copy_draw_parent=34110711)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112493)
def Event_34112493():
    """Event 34112493"""
    IfFlagEnabled(OR_1, 34110711)
    IfThisEventSlotFlagEnabled(OR_1)
    EndIfConditionTrue(input_condition=OR_1)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=34112490)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=806910, anchor_entity=34110711, model_point=220, anchor_type=CoordEntityType.Character)
    Move(34110711, destination=34112493, destination_type=CoordEntityType.Region, copy_draw_parent=34110711)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112496)
def Event_34112496():
    """Event 34112496"""
    EndIfFlagEnabled(34110711)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=34112482)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=34112483)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=806910, anchor_entity=34110711, model_point=220, anchor_type=CoordEntityType.Character)
    Move(34110711, destination=34112496, destination_type=CoordEntityType.Region, copy_draw_parent=34110711)
    SetLockOnPoint(character=34110711, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112499)
def Event_34112499():
    """Event 34112499"""
    AddSpecialEffect(34110710, 8090)
    AddSpecialEffect(34110711, 8090)
    AddSpecialEffect(34110712, 8090)


@RestartOnRest(34112690)
def Event_34112690():
    """Event 34112690"""
    DisableNetworkSync()
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=34112690)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=34112691)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfUnknownCondition_31(OR_1, hours=8, unknown1=0.0, unknown2=0)
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    Unknown_2003_68(unknown1=8, unknown2=-1.0, unknown3=0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfUnknownCondition_31(OR_1, hours=11, unknown1=0.0, unknown2=0)
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    Unknown_2003_68(unknown1=11, unknown2=-1.0, unknown3=0)

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(34112800)
def Event_34112800():
    """Event 34112800"""
    EndIfFlagEnabled(34110800)
    IfHealthValueLessThanOrEqual(MAIN, 34110800, value=0)
    Wait(4.0)
    PlaySoundEffect(34110800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 34110800)
    KillBossAndDisplayBanner(character=34110800, banner_type=BannerType.Unknown)
    EnableFlag(34110800)


@RestartOnRest(34112810)
def Event_34112810():
    """Event 34112810"""
    GotoIfFlagDisabled(Label.L0, flag=34110800)
    DisableCharacter(34110800)
    DisableAnimations(34110800)
    Kill(34110800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34110800)
    DisableAnimations(34110800)
    IfFlagEnabled(AND_1, 34112805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34112800)
    IfAttackedWithDamageType(OR_1, attacked_entity=34110800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(34110800)
    EnableAnimations(34110800)
    SetNetworkUpdateRate(34110800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34110800)


@RestartOnRest(34112849)
def Event_34112849():
    """Event 34112849"""
    RunCommonEvent(
        0,
        9005800,
        args=(34110800, 34111800, 34112800, 34112805, 34115800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(34110800, 34111800, 34112800, 34112805, 34112806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(34110800, 34111800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(34110800, 930000, 34112805, 34112806, 0, 34112802, 0, 0), arg_types="IiIIIIii")

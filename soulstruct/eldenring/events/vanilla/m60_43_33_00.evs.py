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
    RunCommonEvent(0, 90005600, args=(1043330000, 1043331950, 5.0, 1043330480), arg_types="IIfI")
    RunCommonEvent(0, 90005870, args=(1043330800, 904810600, 18), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1043330800, 0, 1043330800, 0, 30185, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005251, args=(1043330800, 20.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005872, args=(1043330800, 18, 0), arg_types="III")
    RunCommonEvent(0, 900005610, args=(1043331680, 100, 800, 1043338600), arg_types="IiiI")
    RunCommonEvent(0, 90005550, args=(1043330530, 1043331530, 1043333530), arg_types="III")
    Event_1043332270()
    Event_1043332270(slot=1)
    RunCommonEvent(0, 90005724, args=(1043330290, 1043330290, 70500, 0.0, 1, 1043335291), arg_types="IIifiI")
    RunCommonEvent(0, 90005722, args=(1043330290, 1043330291), arg_types="II")
    RunCommonEvent(0, 90005720, args=(1043330290, 1043330292, 10961, 181), arg_types="IIii")
    RunCommonEvent(0, 90005720, args=(1043330290, 1043330293, 10961, 182), arg_types="IIii")
    RunCommonEvent(0, 90005721, args=(1043330290, 1043330292), arg_types="II")
    RunCommonEvent(0, 90005721, args=(1043330290, 1043330293), arg_types="II")
    RunCommonEvent(0, 90005723, args=(1043330290,))
    Event_1043332230(0, character=1043330230, region=1043332230)
    Event_1043332230(1, character=1043330231, region=1043332230)
    Event_1043332230(2, character=1043330232, region=1043332230)
    Event_1043332230(3, character=1043330233, region=1043332233)
    Event_1043332230(4, character=1043330234, region=1043332233)
    Event_1043332230(5, character=1043330235, region=1043332233)
    Event_1043332230(6, character=1043330236, region=1043332233)
    Event_1043332230(7, character=1043330237, region=1043332233)
    Event_1043332230(8, character=1043330238, region=1043332233)
    Event_1043332230(9, character=1043330239, region=1043332233)
    Event_1043332230(10, character=1043330240, region=1043332233)
    Event_1043332230(11, character=1043330241, region=1043332233)
    RunCommonEvent(0, 90005300, args=(1043330221, 1043330221, 40136, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1043330050()
    RunCommonEvent(0, 90005261, args=(1043330210, 1043332210, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1043330211, 1043332211, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1043330200, 5.0, 0.0, 3005), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1043330201, 1043332200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1043330202, 1043332200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1043330203, 1043332200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1043330204, 1043332200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(1043330250, 30000, 20000, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")


@NeverRestart(1043330050)
def Event_1043330050():
    """Event 1043330050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(1043330610)


@RestartOnRest(1043332230)
def Event_1043332230(_, character: uint, region: uint):
    """Event 1043332230"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    AddSpecialEffect(character, 8080)


@RestartOnRest(1043332270)
def Event_1043332270():
    """Event 1043332270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1043330270)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1043332270)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101240,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101250,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101260,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1043330270,
        source_entity=1043332271,
        model_point=900,
        behavior_id=802101270,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@NeverRestart(1043332650)
def Event_1043332650():
    """Event 1043332650"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1043330650,
            1043330651,
            0,
            1043331650,
            1043331651,
            1043332651,
            1043331652,
            1043332652,
            1043332651,
            1043332652,
            1043330652,
            1043332653,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1043330510)
def Event_1043330510():
    """Event 1043330510"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(1043330650)


@RestartOnRest(1043332520)
def Event_1043332520():
    """Event 1043332520"""
    RegisterLadder(start_climbing_flag=1043330530, stop_climbing_flag=1043330531, obj=1043331653)


@RestartOnRest(1043332680)
def Event_1043332680():
    """Event 1043332680"""
    IfFlagEnabled(MAIN, 1043338600)
    CreateObjectVFX(1043331680, vfx_id=100, model_point=800)

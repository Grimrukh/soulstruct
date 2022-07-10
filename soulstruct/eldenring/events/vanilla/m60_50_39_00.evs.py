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
    Event_1050392210(0, character=1050390290, obj=1050391290, region=1050392290)
    Event_1050392210(1, character=1050390291, obj=1050391291, region=1050392291)
    Event_1050392580(0, start_climbing_flag=50390580, stop_climbing_flag=50390851, obj=1050391580)
    RunCommonEvent(0, 90005525, args=(1050390620, 1050391620), arg_types="II")
    RunCommonEvent(0, 90005632, args=(580060, 1050391550, 80060), arg_types="IIi")
    Event_1050392300(0, obj=1050391650, flag=1050390200)
    Event_1050392300(1, obj=1050391651, flag=1050390200)
    Event_1050392301(2, obj=1050391652, flag=1050390201)
    Event_1050392303(0, obj=1050391600, flag=1050390201)
    RunCommonEvent(0, 90005251, args=(1050390200, 11.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1050390205, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1050390206, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1050390208, 1050392208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1050390209, 8.0, 0.0, -1), arg_types="Iffi")
    Event_1050392200(0, character=1050390200, special_effect_id=14807)
    Event_1050392200(1, character=1050390201, special_effect_id=14808)
    Event_1050392200(4, character=1050390204, special_effect_id=14808)
    Event_1050392200(5, character=1050390205, special_effect_id=14807)
    Event_1050392200(6, character=1050390206, special_effect_id=14807)
    Event_1050392200(7, character=1050390207, special_effect_id=14807)
    Event_1050392200(8, character=1050390208, special_effect_id=14807)
    Event_1050392200(9, character=1050390209, special_effect_id=14807)
    Event_1050392200(10, character=1050390210, special_effect_id=14807)
    RunCommonEvent(0, 90005200, args=(1050390258, 30014, 20014, 1050392350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1050390259, 30014, 20014, 1050392350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1050392200(11, character=1050390300, special_effect_id=10113)
    Event_1050392200(12, character=1050390304, special_effect_id=14807)
    Event_1050392200(13, character=1050390309, special_effect_id=14807)
    Event_1050392200(14, character=1050390310, special_effect_id=14807)
    Event_1050392201(0, 1050390301, 10113, 4.0, 3.0)
    Event_1050392201(1, 1050390302, 10113, 5.0, 4.0)
    Event_1050392201(2, 1050390303, 10113, 6.0, 2.0)
    Event_1050392201(3, 1050390305, 10113, 4.0, 4.0)
    Event_1050392201(4, 1050390306, 10113, 6.0, 3.0)
    Event_1050392201(5, 1050390307, 10113, 5.0, 3.0)
    Event_1050392201(6, 1050390308, 10113, 6.0, 4.0)
    RunCommonEvent(0, 90005200, args=(1050390351, 30016, 20016, 1050392350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1050390400, 1050392400, 0.0, -1), arg_types="IIfi")


@RestartOnRest(1050392200)
def Event_1050392200(_, character: uint, special_effect_id: int):
    """Event 1050392200"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1050392201)
def Event_1050392201(_, character: uint, special_effect_id: int, seconds: float, seconds_1: float):
    """Event 1050392201"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect_id)
    Wait(seconds)
    CancelSpecialEffect(character, special_effect_id)
    Wait(seconds_1)
    Restart()


@RestartOnRest(1050392210)
def Event_1050392210(_, character: uint, obj: uint, region: uint):
    """Event 1050392210"""
    DisableCharacter(character)
    EndIfFlagEnabled(region)
    IfCharacterDead(AND_3, character)
    EndIfConditionTrue(input_condition=AND_3)
    DisableHealthBar(character)
    IfCharacterType(AND_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_2)
    CreateObjectVFX(obj, vfx_id=100, model_point=620383)
    EnableCharacter(character)
    EnableNetworkFlag(region)
    Wait(2.0)
    DeleteObjectVFX(obj)
    ForceAnimation(character, 20001, unknown2=1.0)
    Wait(1.899999976158142)
    ForceAnimation(character, 20004, unknown2=1.0)
    Wait(2.0)
    ForceAnimation(character, 20004, unknown2=1.0)
    Wait(1.0)
    DisableCharacter(character)
    Kill(character)
    End()


@NeverRestart(1050392300)
def Event_1050392300(_, obj: uint, flag: uint):
    """Event 1050392300"""
    EnableNetworkSync()
    CreateObjectVFX(obj, vfx_id=200, model_point=1502)
    IfFlagEnabled(MAIN, flag)
    PlaySoundEffect(obj, 1500, sound_type=SoundType.s_SFX)
    DisableObject(obj)
    DeleteObjectVFX(obj)


@NeverRestart(1050392301)
def Event_1050392301(_, obj: uint, flag: uint):
    """Event 1050392301"""
    EnableNetworkSync()
    CreateObjectVFX(obj, vfx_id=200, model_point=1501)
    IfFlagEnabled(MAIN, flag)
    PlaySoundEffect(obj, 1500, sound_type=SoundType.s_SFX)
    DisableObject(obj)
    DeleteObjectVFX(obj)


@NeverRestart(1050392303)
def Event_1050392303(_, obj: uint, flag: uint):
    """Event 1050392303"""
    EnableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9520, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(1.2999999523162842)
    EnableFlag(flag)
    DisplayDialog(text=30000, anchor_entity=obj)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=100, model_point=806031)
    End()


@NeverRestart(1050392580)
def Event_1050392580(_, start_climbing_flag: uint, stop_climbing_flag: uint, obj: uint):
    """Event 1050392580"""
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)

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
    RunCommonEvent(0, 90005870, args=(1050560800, 904911600, 5), arg_types="IiI")
    RunCommonEvent(0, 90005861, args=(1050560800, 0, 1050560800, 1, 30550, 30065, 0.0), arg_types="IIIIiif")
    Event_1050562200(0, attacker__character=1050565200, region=1050562200)
    Event_1050562580()
    RunCommonEvent(
        0,
        90005620,
        args=(1050560570, 1050561570, 1050561571, 1050561572, 1050562570, 1050562571, 1050562572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1050560570, 1050561573), arg_types="II")
    RunCommonEvent(
        0,
        90005605,
        args=(1050561510, 60, 50, 56, 0, 1050562510, 0, 1050562511, 1050562512, 1050562513, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(
        0,
        90005633,
        args=(580330, 580030, 1050560550, 30016, 20016, 1050561550, 1050561551),
        arg_types="IIIiiII",
    )
    Event_1050562555(0, character=1050560550)
    Event_1050562250(
        0,
        flag=1050560250,
        obj=1050566250,
        character=1050560250,
        character_1=1050560251,
        character_2=35000,
        special_effect=17170,
        special_effect_1=17171
    )
    Event_1050562260(0, anchor_entity=1050561250)
    Event_1050562260(1, anchor_entity=1050561251)
    Event_1050562260(2, anchor_entity=1050561252)
    RunCommonEvent(0, 90005300, args=(1050560300, 1050560300, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005560, args=(1050560500, 1050561500, 0), arg_types="IIi")
    RunCommonEvent(
        0,
        90005795,
        args=(7604, 0, 1050569000, 1050562141, 1050562142, 80604, 9000, 1050561700, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=20)
    RunCommonEvent(0, 90005796, args=(7604, 1050560700, 5, 1050562141), arg_types="IIBI")
    Event_1050562145()
    Event_1050562400()
    Event_1050563700()
    RunCommonEvent(0, 90005774, args=(7604, 1050560700, 1050567700), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1050560700)


@RestartOnRest(1050562145)
def Event_1050562145():
    """Event 1050562145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(1050560700)
    SetTeamType(1050560700, TeamType.Human)
    DisableCharacter(1050570320)
    DisableAnimations(1050570320)
    DeleteObjectVFX(1050566700)
    CreateObjectVFX(1050566700, vfx_id=200, model_point=806700)


@RestartOnRest(1050562200)
def Event_1050562200(_, attacker__character: uint, region: uint):
    """Event 1050562200"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1050562200)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5650)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000, attacker=attacker__character)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=attacker__character, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=attacker__character, radius=10.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=35000, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1050562200)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5650)


@RestartOnRest(1050562555)
def Event_1050562555(_, character: uint):
    """Event 1050562555"""
    DisableGravity(character)


@RestartOnRest(1050562580)
def Event_1050562580():
    """Event 1050562580"""
    RegisterLadder(start_climbing_flag=1050560580, stop_climbing_flag=1050560581, obj=1050561580)


@RestartOnRest(1050562250)
def Event_1050562250(
    _,
    flag: uint,
    obj: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    special_effect: int,
    special_effect_1: int,
):
    """Event 1050562250"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EnableSpawner(entity=1050563250)
    EnableSpawner(entity=1050563251)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=1500)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect_1)
    IfHealthLessThanOrEqual(AND_1, character, value=0.0)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterHasSpecialEffect(AND_2, character_1, special_effect)
    IfCharacterHasSpecialEffect(AND_2, character_1, special_effect_1)
    IfHealthLessThanOrEqual(AND_2, character_1, value=0.0)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfCharacterHasSpecialEffect(AND_3, character_2, special_effect)
    IfCharacterHasSpecialEffect(AND_3, character_2, special_effect_1)
    IfHealthLessThanOrEqual(AND_3, character_2, value=0.0)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(flag)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=1050563250)
    DisableSpawner(entity=1050563251)
    DisableObject(obj)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 1500, sound_type=SoundType.s_SFX)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, flag)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)
    DisableSpawner(entity=1050563250)
    DisableSpawner(entity=1050563251)
    DisableObject(obj)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1050562260)
def Event_1050562260(_, anchor_entity: uint):
    """Event 1050562260"""
    DisableNetworkSync()
    EndIfFlagEnabled(1050560250)
    IfActionButtonParamActivated(OR_1, action_button_id=9320, entity=anchor_entity)
    IfFlagEnabled(OR_1, 1050560250)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1050560250)
    DisplayDialog(text=20200, anchor_entity=anchor_entity)
    Wait(1.0)
    Restart()


@RestartOnRest(1050562400)
def Event_1050562400():
    """Event 1050562400"""
    DisableNetworkSync()
    AwaitFlagEnabled(flag=1050562140)
    AddSpecialEffect(1050560100, 9531)
    AwaitFlagDisabled(flag=1050562140)
    AddSpecialEffect(1050560100, 9532)
    Wait(1.0)
    Restart()


@RestartOnRest(1050563700)
def Event_1050563700():
    """Event 1050563700"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(400075)
    EnableFlag(1050569000)
    End()

"""
linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005460, args=(1042320200,))
    RunCommonEvent(0, 90005461, args=(1042320200,))
    RunCommonEvent(0, 90005462, args=(1042320200,))
    Event_1042322220()
    Event_1042322230()
    Event_1042322580()
    Event_1042322510(0, 1042321510, 1042322510, 1042322500, 1042323900)


@RestartOnRest(1042322220)
def Event_1042322220():
    """Event 1042322220"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=1042322220)
    IfConditionTrue(AND_1, input_condition=AND_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ForceAnimation(1042320220, 3011, unknown2=1.0)
    Wait(5.0)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1042322220, unk_8_12=1)
    End()


@RestartOnRest(1042322230)
def Event_1042322230():
    """Event 1042322230"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=1042322230)
    IfConditionTrue(AND_1, input_condition=AND_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ForceAnimation(1042320230, 3031, unknown2=1.0)
    End()


@RestartOnRest(1042322500)
def Event_1042322500(_, character: uint):
    """Event 1042322500"""
    AddSpecialEffect(character, 5000)
    IfCharacterHasSpecialEffect(MAIN, character, 5411)
    CancelSpecialEffect(character, 5000)


@RestartOnRest(1042322510)
def Event_1042322510(_, obj: uint, region: uint, flag: uint, obj_act_id: uint):
    """Event 1042322510"""
    DisableNetworkSync()
    GotoIfTryingToJoinSession(Label.L1)
    GotoIfTryingToCreateSession(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfObjectActivated(OR_1, obj_act_id=obj_act_id)
    IfTryingToJoinSession(OR_1)
    IfTryingToCreateSession(OR_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfTryingToJoinSession(Label.L1)
    GotoIfTryingToCreateSession(Label.L1)
    EnableFlag(flag)
    Wait(1.2999999523162842)
    Wait(0.8999999761581421)
    GotoIfTryingToJoinSession(Label.L2)
    GotoIfTryingToCreateSession(Label.L2)
    IfHealthValueEqual(AND_1, PLAYER, value=0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    GotoIfCharacterOutsideRegion(Label.L20, character=PLAYER, region=region)
    GotoIfTryingToJoinSession(Label.L2)
    GotoIfTryingToCreateSession(Label.L2)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=1, unknown4=-1.0)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(0.699999988079071)
    AddSpecialEffect(PLAYER, 4090)
    PlaySoundEffect(PLAYER, 8700, sound_type=SoundType.c_CharacterMotion)
    Wait(2.700000047683716)
    DisableCharacter(PLAYER)
    IfHealthValueEqual(AND_3, PLAYER, value=0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_3)
    GotoIfTryingToJoinSession(Label.L3)
    GotoIfTryingToCreateSession(Label.L3)
    AddSpecialEffect(PLAYER, 4091)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=-1.0)
    EnableFlag(11000601)
    GotoIfFlagEnabled(Label.L10, flag=300)
    WarpToMap(game_map=LEYNDELL_ROYAL_CAPITAL, player_start=11002697, unknown1=60)
    SaveRequest()
    SetRespawnPoint(respawn_point=11002697)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    WarpToMap(game_map=LEYNDELL_ASHEN_CAPITAL, player_start=11052680, unknown1=60)
    SaveRequest()
    SetRespawnPoint(respawn_point=11052680)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=-1.0)
    Wait(4.400000095367432)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(obj, 2, wait_for_completion=True, unknown2=1.0)
    DisableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=2)
    DisableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableObjectActivation(obj, obj_act_id=-1)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    ForceAnimation(PLAYER, 60131, unknown2=1.0)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=-1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableObjectActivation(obj, obj_act_id=-1)
    ForceAnimation(obj, 2, wait_for_completion=True, unknown2=1.0)
    DisableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObjectActivation(obj, obj_act_id=-1)
    IfTryingToJoinSession(OR_2)
    IfConditionFalse(AND_2, input_condition=OR_2)
    IfTryingToCreateSession(OR_3)
    IfConditionFalse(AND_2, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableObjectActivation(obj, obj_act_id=-1)
    Restart()


@RestartOnRest(1042322400)
def Event_1042322400():
    """Event 1042322400"""
    GotoIfFlagDisabled(Label.L0, flag=1042320400)
    DisableObject(1042321400)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(1042321400, erase_root=False)
    CreateObjectVFX(1042321400, vfx_id=101, model_point=6)
    IfFlagEnabled(AND_1, 1042320401)
    IfFlagEnabled(AND_1, 1042320402)
    IfFlagEnabled(AND_1, 1042320403)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042320400)
    DeleteObjectVFX(1042321400)
    DisableObject(1042321400)


@RestartOnRest(1042322401)
def Event_1042322401(_, flag: uint, obj: uint, obj_1: uint):
    """Event 1042322401"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DestroyObject(obj)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=800056)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfObjectDestroyed(AND_1, obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=800056)


@RestartOnRest(1042322402)
def Event_1042322402():
    """Event 1042322402"""
    DisableObject(1042321400)
    DisableObject(1042321401)
    DisableObject(1042321402)
    DisableObject(1042321403)
    DisableObject(1042321404)
    DisableObject(1042321405)
    DisableObject(1042321406)


@RestartOnRest(1042322403)
def Event_1042322403(
    _,
    character: uint,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect: int,
):
    """Event 1042322403"""
    AddSpecialEffect(character_1, 10196)
    ForceAnimation(character_1, animation_id, loop=True, unknown2=1.0)
    IfCharacterHasSpecialEffect(AND_1, character_1, 5080)
    IfCharacterHasSpecialEffect(
        OR_1,
        character,
        special_effect,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    IfAttackedWithDamageType(OR_1, attacked_entity=character_1, attacker=0)
    IfHasAIStatus(OR_1, character_1, ai_status=AIStatusType.Search)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=special_effect, target_count=0)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(character_1, 10196)
    ForceAnimation(character_1, animation_id_1, wait_for_completion=True, unknown2=1.0)
    ReplanAI(character_1)


@RestartOnRest(1042322404)
def Event_1042322404(_, flag: uint, character: uint):
    """Event 1042322404"""
    EnableCharacter(character)
    EnableAnimations(character)
    IfFlagEnabled(MAIN, flag)
    DisableCharacter(character)
    DisableAnimations(character)


@NeverRestart(1042322580)
def Event_1042322580():
    """Event 1042322580"""
    RegisterLadder(start_climbing_flag=1042320580, stop_climbing_flag=1042320851, obj=1042321580)
    RegisterLadder(start_climbing_flag=1042320582, stop_climbing_flag=1042320853, obj=1042321582)
    RegisterLadder(start_climbing_flag=1042320584, stop_climbing_flag=1042320855, obj=1042321584)

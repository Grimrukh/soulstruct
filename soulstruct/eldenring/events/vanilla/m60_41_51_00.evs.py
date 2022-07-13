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
    RunCommonEvent(0, 90005870, args=(1041510800, 903251600, 12), arg_types="IiI")
    RunCommonEvent(0, 90005870, args=(1041510801, 903251600, 12), arg_types="IiI")
    Event_1041512800(
        0,
        flag=1041510800,
        left=0,
        character=1041510800,
        left_1=0,
        item_lot__item_lot_param_id=30335,
        character_1=1041510801
    )
    RunCommonEvent(0, 90005261, args=(1041510800, 1041512500, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041510801, 1041512500, 10.0, 0.0, 0), arg_types="IIffi")
    Event_1041512310(0, character__region=1041510800, character__region_1=1041510801)
    Event_1041512321(0, character=1041510800, character_1=1041510801, entity_id__unk_4_8=12, flag=1041512815)
    Event_1041512320(0, character=1041510800, character_1=1041510801)
    RunCommonEvent(0, 90005261, args=(1041510202, 1041512202, 10.0, 0.0, 0), arg_types="IIffi")
    Event_1041512200(0, character=1041510200)
    Event_1041512200(1, character=1041510201)
    RunCommonEvent(0, 90005300, args=(1041510410, 1041510410, 0, 0.0, 0), arg_types="IIifi")
    Event_1041512270()
    Event_1041512270(slot=1)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005250, args=(1041510410, 1041512410, 0.0, 700), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(1041510452, 30016, 20016, 100.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1041510450, 30017, 20017, 1041512450, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1041510451, 30017, 20017, 1041512450, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005200, args=(1041510453, 30016, 20016, 1041512453, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1041512200)
def Event_1041512200(_, character: uint):
    """Event 1041512200"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8092)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(1041512270)
def Event_1041512270():
    """Event 1041512270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1041510270)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1041512270)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1041510270,
        source_entity=1041512271,
        model_point=900,
        behavior_id=802103070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1041512310)
def Event_1041512310(_, character__region: uint, character__region_1: uint):
    """Event 1041512310"""
    EndIfFlagEnabled(1041510800)
    IfHasAIStatus(OR_1, character__region, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_1, character__region_1, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(30.0)
    EnableAI(character__region)
    EnableAI(character__region_1)
    SetCharacterEventTarget(character__region, region=character__region_1)
    SetCharacterEventTarget(character__region_1, region=character__region)
    Restart()


@RestartOnRest(1041512320)
def Event_1041512320(_, character: uint, character_1: uint):
    """Event 1041512320"""
    EndIfFlagEnabled(1041510800)
    IfCharacterDead(OR_1, character)
    IfCharacterDead(OR_1, character_1)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfHealthRatioLessThanOrEqual(AND_1, character, value=0.5)
    IfHealthRatioLessThanOrEqual(AND_1, character_1, value=0.5)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableNetworkFlag(1041512815)


@NeverRestart(1041512321)
def Event_1041512321(_, character: uint, character_1: uint, entity_id__unk_4_8: uint, flag: uint):
    """Event 1041512321"""
    DisableNetworkSync()
    IfFlagEnabled(AND_1, flag)
    IfUnknownCondition_33(AND_1, unk_4_8=entity_id__unk_4_8, unk_8_9=True)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownSound_2010_12(entity_id=entity_id__unk_4_8, unk_4_8=1)
    IfCharacterDead(AND_2, character)
    IfCharacterDead(AND_2, character_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfUnknownCondition_33(OR_2, unk_4_8=entity_id__unk_4_8, unk_8_9=False)
    IfConditionTrue(MAIN, input_condition=OR_2)
    UnknownSound_2010_12(entity_id=entity_id__unk_4_8, unk_4_8=0)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(1041512800)
def Event_1041512800(
    _,
    flag: uint,
    left: uint,
    character: uint,
    left_1: uint,
    item_lot__item_lot_param_id: int,
    character_1: uint,
):
    """Event 1041512800"""
    SkipLinesIfValueEqual(1, left=item_lot__item_lot_param_id, right=0)
    Unknown_2004_76(flag=flag, item_lot=item_lot__item_lot_param_id)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableAnimations(character)
    DisableAnimations(character_1)
    Kill(character)
    Kill(character_1)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(1.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableAnimations(character)
    EnableAnimations(character_1)
    IfHealthValueLessThanOrEqual(AND_15, character, value=0)
    IfHealthValueLessThanOrEqual(AND_15, character_1, value=0)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_14, character)
    IfCharacterDead(AND_14, character_1)
    IfConditionTrue(MAIN, input_condition=AND_14)
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DutyFulfilled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.Unknown)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaLoss)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaWin)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(5.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()

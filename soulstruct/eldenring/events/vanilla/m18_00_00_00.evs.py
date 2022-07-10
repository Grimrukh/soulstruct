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
    GotoIfPlayerNotInOwnWorld(Label.L0)
    Event_18000020()
    Event_18000021()
    Event_18000022()
    Event_18002023()

    # --- Label 0 --- #
    DefineLabel(0)
    Event_18000050()
    RegisterGrace(grace_flag=18000000, obj=18001950, unknown=5.0)
    RegisterGrace(grace_flag=18000001, obj=18001951, unknown=5.0)
    Event_18002800()
    Event_18002810()
    Event_18000820()
    RunCommonEvent(
        0,
        90005646,
        args=(18000800, 18002190, 18002191, 18001190, 18002190, 18, 0, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_18002850()
    Event_18002860()
    Event_18000870()
    Event_18002400()
    Event_18002440(0, 18000600, 18001600, 18001601, 18002600, 2.3299999237060547)
    Event_18002440(1, 18000601, 18001602, 18001603, 18002601, 2.2799999713897705)
    Event_18002440(2, 18000602, 18001604, 18001605, 18002602, 2.2799999713897705)
    Event_18002450(0, obj_flag=18000600, obj=18001600, flag=18002600)
    Event_18002450(1, obj_flag=18000601, obj=18001602, flag=18002601)
    Event_18002450(2, obj_flag=18000602, obj=18001604, flag=18002602)
    Event_18002410()
    Event_18002411(
        0,
        region=18002431,
        patrol_information_id=18003420,
        region_1=18002421,
        patrol_information_id_1=18003421,
        region_2=0,
        patrol_information_id_2=0
    )
    Event_18002411(
        1,
        region=18002432,
        patrol_information_id=18003421,
        region_1=18002422,
        patrol_information_id_1=18003422,
        region_2=0,
        patrol_information_id_2=0
    )
    Event_18002411(
        2,
        region=18002433,
        patrol_information_id=18003422,
        region_1=18002423,
        patrol_information_id_1=18003423,
        region_2=0,
        patrol_information_id_2=0
    )
    Event_18002411(
        3,
        region=18002434,
        patrol_information_id=18003423,
        region_1=18002424,
        patrol_information_id_1=18003424,
        region_2=0,
        patrol_information_id_2=0
    )
    Event_18002411(
        4,
        region=18002435,
        patrol_information_id=18003424,
        region_1=18002425,
        patrol_information_id_1=18003425,
        region_2=18002426,
        patrol_information_id_2=18003426
    )
    RunCommonEvent(0, 90005680, args=(18000530, 18000531, 18000532, 18000533, 18001530), arg_types="IIIII")
    RunCommonEvent(0, 900005610, args=(18001650, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(18001651, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005501,
        args=(18000510, 18001510, 0, 18001510, 18001511, 18001512, 18000511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(18000515, 18001515, 1, 18001515, 18001516, 18001517, 18000516),
        arg_types="IIIIIII",
    )
    Event_18002510()
    RunCommonEvent(0, 90005511, args=(18000542, 18001542, 18003542, 227010, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(18000542, 18002542, 18002543), arg_types="III")
    Event_18002580()
    RunCommonEvent(
        0,
        90005646,
        args=(18000800, 18002840, 18002841, 18001840, 18002840, 18, 0, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(
        0,
        90005620,
        args=(18000570, 18001570, 18001571, 18001572, 18002570, 18002571, 18002572),
        arg_types="IIIIIIi",
    )
    Event_18002569(0, flag=18000570, obj=18001573)
    RunCommonEvent(0, 90005570, args=(60809, 9, 18001640, 0, 1, 0), arg_types="IiIiii")
    Event_18002270(0, entity=18000270)
    Event_18002650(0, region=18002650, tutorial_param_id=1010, flag=710010)
    Event_18002640(0, region=18002651, tutorial_param_id=1020, flag=710020, item=9100, flag_1=69000)
    Event_18002640(1, region=18002656, tutorial_param_id=1070, flag=710070, item=9112, flag_1=69120)
    Event_18002640(2, region=18002663, tutorial_param_id=1140, flag=710140, item=9103, flag_1=69030)
    RunCommonEvent(0, 90005261, args=(18000202, 18002202, 10.0, 0.0, 0), arg_types="IIffi")
    Event_18002640(3, region=18002665, tutorial_param_id=1160, flag=710160, item=9104, flag_1=69040)
    Event_18002640(4, region=18002667, tutorial_param_id=1190, flag=710190, item=9105, flag_1=69050)
    Event_18002640(5, region=18002670, tutorial_param_id=1200, flag=710200, item=9129, flag_1=69290)
    Event_18002640(6, region=18002668, tutorial_param_id=1210, flag=710210, item=9138, flag_1=69380)
    Event_18002640(7, region=18002659, tutorial_param_id=1100, flag=710100, item=9140, flag_1=69400)
    Event_18002651(0, region=18002652, tutorial_param_id=1030, flag=710030)
    Event_18002651(1, region=18002653, tutorial_param_id=1040, flag=710040)
    Event_18002651(2, region=18002657, tutorial_param_id=1080, flag=710080)
    Event_18002651(3, region=18002658, tutorial_param_id=1090, flag=710090)
    Event_18002651(5, region=18002660, tutorial_param_id=1110, flag=710110)
    Event_18002651(7, region=18002664, tutorial_param_id=1150, flag=710150)
    Event_18002651(8, region=18002666, tutorial_param_id=1170, flag=710170)
    Event_18002654(0, region=18002654, tutorial_param_id=1050, flag=710050)
    Event_18002655(0, region=18002655, tutorial_param_id=1060, flag=18000655, flag_1=710060)
    Event_18002662(0, region=18002662, tutorial_param_id=1130, flag=18000662, flag_1=710130)
    Event_18002663(0, tutorial_param_id=1180, flag=710180, item=9106, flag_1=69060, entity=18000850)
    Event_18002665(0, flag=710660, tutorial_param_id=1660, item=9122, flag_1=69220)
    Event_18002200(0, character=18000200, region=18002201, patrol_information_id=18003200, flag=18002200)
    Event_18002211(0, other_entity=18000211, flag=18002211)
    Event_18002211(1, other_entity=18000220, flag=18000220)
    Event_18002671(0, flag=710010)
    Event_18002671(1, flag=710020)
    Event_18002671(2, flag=710030)
    Event_18002671(3, flag=710040)
    Event_18002671(4, flag=710050)
    Event_18002671(5, flag=18000655)
    Event_18002671(6, flag=18000662)
    Event_18002671(7, flag=710070)
    Event_18002671(8, flag=710080)
    Event_18002671(9, flag=710090)
    Event_18002671(10, flag=710100)
    Event_18002671(11, flag=710110)
    Event_18002671(12, flag=710120)
    Event_18002671(13, flag=710140)
    Event_18002671(14, flag=710150)
    Event_18002671(15, flag=710160)
    Event_18002671(16, flag=710170)
    Event_18002671(17, flag=710000)
    Event_18002671(18, flag=710110)
    Event_18002671(19, flag=710110)
    Event_18002671(20, flag=710210)
    Event_18002671(21, flag=710200)
    Event_18002671(22, flag=710190)
    Event_18002250(0, character=18000850, special_effect_id=8041)
    Event_18002250(1, character=18000256, special_effect_id=8040)
    Event_18002690()
    RunCommonEvent(0, 90005706, args=(18000701, 30025, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(18000701)
    RunCommonEvent(0, 90005251, args=(18000201, 2.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(18000300, 18002300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(18000313, 4.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(18000330, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(18000342, 4.0, 0.0, 3000), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(18000343, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(18000344, 5.0, 2.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005200, args=(18000350, 30002, 20002, 18002350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(18000351, 30002, 20002, 18002350, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005300, args=(18000350, 18000350, 18002000, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(18000351, 18000351, 18002010, 0.0, 0), arg_types="IIifi")
    Event_18002520()


@RestartOnRest(18000020)
def Event_18000020():
    """Event 18000020"""
    EndIfPlayerNotInOwnWorld()
    IfThisEventSlotFlagEnabled(AND_15)
    IfFlagDisabled(AND_15, 60000)
    GotoIfConditionTrue(Label.L0, input_condition=AND_15)
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(AND_1, 10010020)
    IfInsideMap(AND_1, game_map=STRANDED_GRAVEYARD)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(101)
    SetRespawnPoint(respawn_point=18002020)
    SaveRequest()
    DisableImmortality(PLAYER)
    EqualRecovery()
    Unknown_2004_61(unk_0_4=9999)
    AddSpecialEffect(PLAYER, 4291)
    AddSpecialEffect(PLAYER, 4790)
    EndIfFlagDisabled(2000)
    EnableFlag(9021)
    PlayCutscene(60430000, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    UnknownCamera_4(unknown1=6.980000019073486, unknown2=106.95999908447266)

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerHasGood(OR_10, 201)
    IfPlayerHasGood(OR_10, 203)
    IfPlayerHasGood(OR_10, 205)
    IfPlayerHasGood(OR_10, 207)
    IfPlayerHasGood(OR_10, 209)
    IfPlayerHasGood(OR_10, 211)
    IfPlayerHasGood(OR_10, 213)
    IfPlayerHasGood(OR_10, 215)
    IfPlayerHasGood(OR_10, 217)
    IfPlayerHasGood(OR_10, 219)
    IfPlayerHasGood(OR_11, 221)
    IfPlayerHasGood(OR_11, 223)
    IfPlayerHasGood(OR_11, 225)
    IfPlayerHasGood(OR_11, 227)
    IfPlayerHasGood(OR_11, 229)
    IfPlayerHasGood(OR_11, 221)
    IfPlayerHasGood(OR_11, 223)
    IfPlayerHasGood(OR_11, 225)
    IfPlayerHasGood(OR_11, 227)
    IfPlayerHasGood(OR_11, 229)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfConditionTrue(AND_11, input_condition=OR_11)
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    AwardItemLot(2000, host_only=True)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(60000)


@RestartOnRest(18000021)
def Event_18000021():
    """Event 18000021"""
    DisableNetworkSync()
    EndIfFlagEnabled(102)
    EndIfFlagEnabled(2002)
    UnknownTimer_04(
        hours=10,
        minutes=30,
        seconds=0,
        unknown1=0,
        unknown2=0,
        unknown3=0,
        unknown4=0,
        unknown5=0,
        unknown6=0,
    )
    UnknownTimer_05(unknown1=1)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1042368540)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownTimer_05(unknown1=0)
    EnableFlag(71801)
    DisableThisSlotFlag()
    EnableFlag(102)
    Unknown_2003_68(unknown1=0, unknown2=3600.0, unknown3=0)


@RestartOnRest(18000022)
def Event_18000022():
    """Event 18000022"""
    EndIfFlagEnabled(18000021)
    EndIfFlagEnabled(102)
    EndIfFlagEnabled(2002)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=18002022)
    UnknownTimer_04(
        hours=10,
        minutes=30,
        seconds=0,
        unknown1=0,
        unknown2=0,
        unknown3=0,
        unknown4=0,
        unknown5=0,
        unknown6=0,
    )


@RestartOnRest(18002023)
def Event_18002023():
    """Event 18002023"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(710820)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=18002680)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(710820)


@RestartOnRest(18000050)
def Event_18000050():
    """Event 18000050"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(2030)
    DisableObjectActivation(18001542, obj_act_id=-1)
    IfFlagEnabled(OR_1, 2030)
    IfActionButtonParamActivated(OR_2, action_button_id=7200, entity=18001542)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=OR_2)
    UnknownText_2007_9(text=2000)
    Wait(1.0)
    RestartIfFlagDisabled(2030)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObjectActivation(18001542, obj_act_id=-1)


@RestartOnRest(18002200)
def Event_18002200(_, character: uint, region: uint, patrol_information_id: uint, flag: uint):
    """Event 18002200"""
    EndIfFlagEnabled(flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ClearTargetList(character)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableFlag(flag)


@RestartOnRest(18002211)
def Event_18002211(_, other_entity: uint, flag: uint):
    """Event 18002211"""
    EndIfFlagEnabled(flag)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=other_entity, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(other_entity, 3001, wait_for_completion=True, unknown2=1.0)
    EnableFlag(flag)


@RestartOnRest(18002250)
def Event_18002250(_, character: uint, special_effect_id: int):
    """Event 18002250"""
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(18002270)
def Event_18002270(_, entity: uint):
    """Event 18002270"""
    ForceAnimation(entity, 930025, unknown2=1.0)
    End()


@RestartOnRest(18002400)
def Event_18002400():
    """Event 18002400"""
    SkipLinesIfFlagDisabled(4, 18000400)
    DisableCharacter(18000400)
    DisableAnimations(18000400)
    DisableAI(18000400)
    End()
    IfInsideMap(MAIN, game_map=STRANDED_GRAVEYARD)
    DisableInvincibility(18000400)
    EnableImmortality(18000400)
    SetLockOnPoint(character=18000400, lock_on_model_point=220, state=False)
    DisableHealthBar(18000400)
    AddSpecialEffect(18000400, 5000)
    SetNetworkUpdateRate(18000400, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(18000400, True)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(18000400, authority_level=UpdateAuthority.Unknown8192)


@RestartOnRest(18002410)
def Event_18002410():
    """Event 18002410"""
    EndIfFlagEnabled(18000400)
    EndIfPlayerNotInOwnWorld()
    IfTrueFlagCountGreaterThanOrEqual(AND_1, FlagType.Absolute, flag_range=(18002411, 18002411), value=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=18002400)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangePatrolBehavior(18000400, patrol_information_id=18003420)
    WaitFrames(frames=1)


@RestartOnRest(18002411)
def Event_18002411(
    _,
    region: uint,
    patrol_information_id: uint,
    region_1: uint,
    patrol_information_id_1: uint,
    region_2: uint,
    patrol_information_id_2: uint,
):
    """Event 18002411"""
    EndIfFlagEnabled(18000400)
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(MAIN, character=18000400, region=region)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region_1)
    SkipLinesIfUnsignedEqual(1, left=0, right=region_2)
    GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=region_2)
    ChangePatrolBehavior(18000400, patrol_information_id=patrol_information_id)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangePatrolBehavior(18000400, patrol_information_id=patrol_information_id_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangePatrolBehavior(18000400, patrol_information_id=patrol_information_id_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfCharacterOutsideRegion(MAIN, character=18000400, region=region)
    Restart()


@RestartOnRest(18002440)
def Event_18002440(_, obj_flag: uint, obj: uint, obj_1: uint, flag: uint, seconds: float):
    """Event 18002440"""
    SkipLinesIfFlagDisabled(4, flag)
    DisableObject(obj)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableObject(obj_1)
    End()
    EnableObject(obj)
    IfObjectDestroyed(MAIN, obj_1)
    DestroyObject(obj, request_slot=0)
    RemoveObjectFlag(obj_flag=obj_flag)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=200,
        behavior_param_id=200500,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=0.10000000149011612,
    )
    EnableFlag(flag)
    Wait(seconds)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=18000400, special_effect=19300)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301800,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301810,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301820,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301830,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301840,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301850,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301860,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301870,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableObject(obj)
    RemoveObjectFlag(obj_flag=obj_flag)

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(18002450)
def Event_18002450(_, obj_flag: uint, obj: uint, flag: uint):
    """Event 18002450"""
    EndIfFlagEnabled(18000400)
    IfCharacterHasSpecialEffect(AND_1, 18000400, 19300)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301800,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301810,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301820,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301830,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301840,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301850,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301860,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=18000600,
        source_entity=obj,
        model_point=200,
        behavior_id=803301870,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableObject(obj)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableImmortality(18000400)
    Kill(18000400, award_souls=True)
    CancelSpecialEffect(18000400, 19300)
    Wait(3.0)
    EndIfFlagEnabled(18000400)
    SkipLinesIfPlayerNotInOwnWorld(1)
    AwardItemLot(18000900, host_only=True)
    EnableFlag(18000400)


@NeverRestart(18002510)
def Event_18002510():
    """Event 18002510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            18000510,
            18001510,
            0,
            18001510,
            18001511,
            18003511,
            18001512,
            18003512,
            18002511,
            18002512,
            18000511,
            18002512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            18000515,
            18001515,
            1,
            18001515,
            18001516,
            18003516,
            18001517,
            18003517,
            18002516,
            18002517,
            18000516,
            18002517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005681, args=(18000530, 18000531, 18000532, 18000533, 18001530), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100770, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100760, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100750, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100740, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100730, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100720, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100710, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(18000532, 18001530, 18002530, 18000530, 801100700, 801100705, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )


@NeverRestart(18002520)
def Event_18002520():
    """Event 18002520"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(18000530)


@NeverRestart(18002569)
def Event_18002569(_, flag: uint, obj: uint):
    """Event 18002569"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=101, model_point=806043)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableObject(obj)


@RestartOnRest(18002580)
def Event_18002580():
    """Event 18002580"""
    RegisterLadder(start_climbing_flag=18000580, stop_climbing_flag=18000581, obj=18001580)


@RestartOnRest(18002640)
def Event_18002640(_, region: uint, tutorial_param_id: int, flag: uint, item: int, flag_1: uint):
    """Event 18002640"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(18002650)
def Event_18002650(_, region: uint, tutorial_param_id: int, flag: uint):
    """Event 18002650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfHealthLessThan(AND_1, PLAYER, value=100.0)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(2.0)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)


@RestartOnRest(18002651)
def Event_18002651(_, region: uint, tutorial_param_id: int, flag: uint):
    """Event 18002651"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)


@RestartOnRest(18002654)
def Event_18002654(_, region: uint, tutorial_param_id: int, flag: uint):
    """Event 18002654"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerDoesNotHaveWeapon(AND_1, 33000000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33040000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33050000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33060000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33090000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33120000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33130000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33170000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33180000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33190000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33200000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33210000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33230000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33240000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33250000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33260000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33270000)
    IfPlayerDoesNotHaveWeapon(AND_1, 33280000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34000000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34010000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34020000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34030000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34040000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34060000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34070000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34080000)
    IfPlayerDoesNotHaveWeapon(AND_1, 34090000)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)


@RestartOnRest(18002655)
def Event_18002655(_, region: uint, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 18002655"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerHasWeapon(OR_1, 33000000)
    IfPlayerHasWeapon(OR_1, 33040000)
    IfPlayerHasWeapon(OR_1, 33050000)
    IfPlayerHasWeapon(OR_1, 33060000)
    IfPlayerHasWeapon(OR_1, 33090000)
    IfPlayerHasWeapon(OR_1, 33120000)
    IfPlayerHasWeapon(OR_1, 33130000)
    IfPlayerHasWeapon(OR_1, 33170000)
    IfPlayerHasWeapon(OR_1, 33180000)
    IfPlayerHasWeapon(OR_1, 33190000)
    IfPlayerHasWeapon(OR_1, 33200000)
    IfPlayerHasWeapon(OR_1, 33210000)
    IfPlayerHasWeapon(OR_1, 33230000)
    IfPlayerHasWeapon(OR_1, 33240000)
    IfPlayerHasWeapon(OR_1, 33250000)
    IfPlayerHasWeapon(OR_1, 33260000)
    IfPlayerHasWeapon(OR_1, 33270000)
    IfPlayerHasWeapon(OR_1, 33280000)
    IfPlayerHasWeapon(OR_1, 34000000)
    IfPlayerHasWeapon(OR_1, 34010000)
    IfPlayerHasWeapon(OR_1, 34020000)
    IfPlayerHasWeapon(OR_1, 34030000)
    IfPlayerHasWeapon(OR_1, 34040000)
    IfPlayerHasWeapon(OR_1, 34060000)
    IfPlayerHasWeapon(OR_1, 34070000)
    IfPlayerHasWeapon(OR_1, 34080000)
    IfPlayerHasWeapon(OR_1, 34090000)
    IfFlagDisabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EnableFlag(flag_1)


@RestartOnRest(18002662)
def Event_18002662(_, region: uint, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 18002662"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerHasWeapon(OR_1, 40000000)
    IfPlayerHasWeapon(OR_1, 40010000)
    IfPlayerHasWeapon(OR_1, 40020000)
    IfPlayerHasWeapon(OR_1, 40030000)
    IfPlayerHasWeapon(OR_1, 40050000)
    IfPlayerHasWeapon(OR_1, 41000000)
    IfPlayerHasWeapon(OR_1, 41010000)
    IfPlayerHasWeapon(OR_1, 41020000)
    IfPlayerHasWeapon(OR_1, 41030000)
    IfPlayerHasWeapon(OR_1, 41040000)
    IfPlayerHasWeapon(OR_1, 41060000)
    IfPlayerHasWeapon(OR_1, 41070000)
    IfPlayerHasWeapon(OR_1, 42000000)
    IfPlayerHasWeapon(OR_1, 42000000)
    IfPlayerHasWeapon(OR_1, 42030000)
    IfPlayerHasWeapon(OR_1, 42040000)
    IfPlayerHasWeapon(OR_1, 43000000)
    IfPlayerHasWeapon(OR_1, 43020000)
    IfPlayerHasWeapon(OR_1, 43030000)
    IfPlayerHasWeapon(OR_1, 43050000)
    IfPlayerHasWeapon(OR_1, 43060000)
    IfPlayerHasWeapon(OR_1, 43080000)
    IfPlayerHasWeapon(OR_1, 43100000)
    IfPlayerHasWeapon(OR_1, 43110000)
    IfFlagDisabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EnableFlag(flag_1)


@RestartOnRest(18002663)
def Event_18002663(_, tutorial_param_id: int, flag: uint, item: int, flag_1: uint, entity: uint):
    """Event 18002663"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=PLAYER, radius=10.0)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(18002665)
def Event_18002665(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 18002665"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(18002671)
def Event_18002671(_, flag: uint):
    """Event 18002671"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=18002671)
    IfOutsideMap(OR_1, game_map=STRANDED_GRAVEYARD)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(flag)


@RestartOnRest(18002690)
def Event_18002690():
    """Event 18002690"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(18007090)
    IfFlagEnabled(MAIN, 18007090)
    Unknown_2003_71(unk_0_4=9)


@RestartOnRest(18002800)
def Event_18002800():
    """Event 18002800"""
    EndIfFlagEnabled(18000800)
    IfHealthValueLessThanOrEqual(MAIN, 18000800, value=0)
    Wait(4.0)
    PlaySoundEffect(18000800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 18000800)
    KillBossAndDisplayBanner(character=18000800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(18000800)
    EnableFlag(9128)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61128)


@RestartOnRest(18002810)
def Event_18002810():
    """Event 18002810"""
    GotoIfFlagDisabled(Label.L0, flag=18000800)
    DisableCharacter(18000800)
    DisableAnimations(18000800)
    Kill(18000800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(18000800)
    IfFlagEnabled(AND_2, 18002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=18002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(18000800)
    SetNetworkUpdateRate(18000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(18000800, name=904640000)


@RestartOnRest(18000820)
def Event_18000820():
    """Event 18000820"""
    RunCommonEvent(
        0,
        9005800,
        args=(18000800, 18001800, 18002800, 18002805, 18005800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(18000800, 18001800, 18002800, 18002805, 18002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(18000800, 18001800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(18000800, 920600, 18002805, 18002806, 0, 18002802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(18002850)
def Event_18002850():
    """Event 18002850"""
    EndIfFlagEnabled(18000850)
    IfHealthValueLessThanOrEqual(MAIN, 18000850, value=0)
    Wait(4.0)
    PlaySoundEffect(18000850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 18000850)
    KillBossAndDisplayBanner(character=18000850, banner_type=BannerType.DutyFulfilled)
    EnableFlag(18000850)


@RestartOnRest(18002860)
def Event_18002860():
    """Event 18002860"""
    GotoIfFlagDisabled(Label.L0, flag=18000850)
    DisableCharacter(18000850)
    DisableAnimations(18000850)
    Kill(18000850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(18000850)
    IfFlagEnabled(AND_2, 18002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=18002850)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(18000850)
    SetNetworkUpdateRate(18000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(18000850, name=904311000)


@RestartOnRest(18000870)
def Event_18000870():
    """Event 18000870"""
    RunCommonEvent(
        0,
        9005800,
        args=(18000850, 18001850, 18002850, 18002855, 18005850, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(18000850, 18001850, 18002850, 18002855, 18002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(18000850, 18001850, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(18000850, 18001851, 4, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(18000850, 931000, 18002855, 18002856, 0, 18002852, 0, 0), arg_types="IiIIIIii")

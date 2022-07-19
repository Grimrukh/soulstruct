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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_42_36_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1042360000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1042360001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=71001,
        flag_1=76100,
        asset=Assets.AEG099_090_9010,
        source_flag=77100,
        value=1,
        flag_2=78100,
        flag_3=78101,
        flag_4=78102,
        flag_5=78103,
        flag_6=78104,
        flag_7=78105,
        flag_8=78106,
        flag_9=78107,
        flag_10=78108,
        flag_11=78109,
    )
    CommonFunc_90005100(
        0,
        flag=71001,
        flag_1=76101,
        asset=Assets.AEG099_090_9011,
        source_flag=77100,
        value=0,
        flag_2=78100,
        flag_3=78101,
        flag_4=78102,
        flag_5=78103,
        flag_6=78104,
        flag_7=78105,
        flag_8=78106,
        flag_9=78107,
        flag_10=78108,
        flag_11=78109,
    )
    CommonFunc_90005870(0, character=Characters.TreeSentinel, name=903251600, npc_threat_level=12)
    CommonFunc_90005860(
        0,
        flag=1042360800,
        left=0,
        character=Characters.TreeSentinel,
        left_1=0,
        item_lot__item_lot_param_id=30100,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.TreeSentinel, npc_threat_level=12, right=0)
    CommonFunc_90005683(0, flag=62103, asset=Assets.AEG099_055_1500, vfx_id=210, flag_1=78190, flag_2=78190)
    Event_1042363700(0, character=Characters.WhiteMaskVarre, asset=Assets.AEG007_360_1000)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.WhiteMaskVarre,
        flag=3181,
        flag_1=3180,
        flag_2=1042369201,
        right=3,
    )
    CommonFunc_90005703(0, 1042360700, 3181, 3182, 1042369201, 3181, 3180, 3183, -1)
    CommonFunc_90005702(0, character=Characters.WhiteMaskVarre, flag=3183, first_flag=3180, last_flag=3183)
    RunCommonEvent(1042363701, slot=0)
    RunCommonEvent(1042363702, slot=0)
    RunCommonEvent(1042363703, slot=0)
    Event_1042360710(0, character=Characters.Ranni, asset=Assets.AEG099_090_9018)
    CommonFunc_90005704(0, attacked_entity=Characters.Ranni, flag=1042369401, flag_1=3746, flag_2=1042369401, right=3)
    CommonFunc_90005709(0, attacked_entity=Characters.Ranni, model_point=905, vfx_id=603000)
    CommonFunc_90005709(0, attacked_entity=Characters.Ranni, model_point=960, vfx_id=603050)
    Event_1042360711(0, character=Characters.TalkDummy3)
    Event_1042360712(0, entity=Characters.Ranni, asset=Assets.AEG099_090_9018)
    Event_1042360713(0, entity=Characters.Ranni, asset=Assets.AEG099_090_9018, character=Characters.TalkDummy3)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9017,
        action_button_id=4350,
        item_lot_param_id=103900,
        first_flag=400390,
        last_flag=400390,
        flag=1042369413,
        model_point=0,
    )
    CommonFunc_90005708(0, character=Characters.Ranni, flag=3746, left=0)
    Event_1042363720(0, character=Characters.Merchant, character_1=Characters.NomadMule)
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4701, flag_1=4700, flag_2=1042369301, right=3)
    CommonFunc_90005703(0, 1042360710, 4701, 4702, 1042369301, 4701, 4700, 4704, -1)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4703, first_flag=4700, last_flag=4704)
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4701, flag_1=4700, flag_2=1042369327, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4701,
        flag_1=4702,
        flag_2=1042369327,
        flag_3=4701,
        first_flag=4700,
        last_flag=4704,
        right=0,
    )
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1042362715, flag_1=1042362716)
    CommonFunc_90005727(
        0,
        flag=4701,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4700,
        last_flag=4703,
    )
    Event_1042360724(0, character=Characters.Merchant, character_1=Characters.NomadMule)
    Event_1042363730(0, character=1042360720)
    Event_1042363740(0, flag=78100, other_entity=Characters.TalkDummy1, flag_1=1042369450)
    Event_1042363741(0, flag=78101, other_entity=Characters.TalkDummy0, flag_1=1042369452)
    Event_1042363742(0, other_entity=Characters.TalkDummy1, flag=1042369450)
    Event_1042363743(0, other_entity=Characters.TalkDummy1, flag=1042369451)
    Event_1042363744(0, other_entity=Characters.TalkDummy0, flag=1042369452)
    Event_1042363745(0, other_entity=Characters.TalkDummy0, flag=1042369453)
    Event_1042363746(0, other_entity=Characters.TalkDummy1, flag=1042369451)
    Event_1042363747(0, other_entity=Characters.TalkDummy0, flag=1042369453)
    Event_1042360750(0, character=Characters.Dummy)
    Event_1042362215(0, character=Characters.Bat0, region=1042362215)
    Event_1042362215(1, character=1042360216, region=1042362215)
    Event_1042362215(2, character=Characters.Bat1, region=1042362217)
    Event_1042362650(0, tutorial_param_id=1500, flag=710500, flag_1=69070)
    Event_1042362652(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370,
    )
    Event_1042362656(0, tutorial_param_id=1740, flag=710740, flag_1=69310)
    Event_1042362660(0, 1730, 710730, 69300)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WhiteMaskVarre)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)
    DisableBackread(Characters.Ranni)
    CommonFunc_90005300(0, 1042360200, 1042365200, 0, 0.0, 0)


@RestartOnRest(1042362200)
def Event_1042362200(_, character: uint):
    """Event 1042362200"""
    if FlagDisabled(1042360000):
        return
    DisableCharacter(character)
    DisableAnimations(character)


@RestartOnRest(1042362215)
def Event_1042362215(_, character: uint, region: uint):
    """Event 1042362215"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    AND_5.Add(CharacterDead(character))
    if AND_5:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_10.Add(CharacterHasSpecialEffect(character, 482))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_3.Add(AND_4)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    OR_3.Add(AND_10)
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AddSpecialEffect(character, 8080)
    Wait(5.0)
    RemoveSpecialEffect(character, 8080)


@RestartOnRest(1042362650)
def Event_1042362650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1042362650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1042362657))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9107, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1042362652)
def Event_1042362652(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1042362652"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_SE_SW))
    AND_1.Add(PlayerDoesNotHaveGood(9109))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100690))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_2):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1042362656)
def Event_1042362656(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1042362656"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1042362656))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9131, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1042362660)
def Event_1042362660(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1042362660"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(76100))
    AND_1.Add(FlagDisabled(flag))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(3.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9130, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@NeverRestart(1042360684)
def Event_1042360684(_, anchor_entity: uint, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1042360684"""
    DisableNetworkSync()
    AND_1.Add(ActionButtonParamActivated(action_button_id=9260, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=4210, anchor_entity=anchor_entity)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    EnableFlag(flag)
    EnableFlag(flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    End()


@RestartOnRest(1042360690)
def Event_1042360690(_, asset: uint, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 1042360690"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag_2)
    DeleteAssetVFX(asset)
    DisableFlag(flag)
    DisableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateAssetVFX(asset, vfx_id=210, model_point=800530)
    EnableFlag(flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()


@RestartOnRest(1042363700)
def Event_1042363700(_, character: uint, asset: uint):
    """Event 1042363700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3180):
        DisableFlag(1042369205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3185)
    GotoIfFlagEnabled(Label.L5, flag=3187)
    GotoIfFlagEnabled(Label.L5, flag=3191)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(3185))
    OR_3.Add(FlagEnabled(3187))
    OR_3.Add(FlagEnabled(3191))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableAsset(asset)
    GotoIfFlagEnabled(Label.L1, flag=3180)
    GotoIfFlagEnabled(Label.L2, flag=3181)
    GotoIfFlagEnabled(Label.L3, flag=3182)
    GotoIfFlagEnabled(Label.L4, flag=3183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
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
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3185))
    OR_4.Add(FlagEnabled(3187))
    OR_4.Add(FlagEnabled(3191))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1042363701)
def Event_1042363701():
    """Event 1042363701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(1042369249)
    OR_1.Add(FlagEnabled(3188))
    OR_1.Add(FlagEnabled(3189))
    OR_1.Add(FlagEnabled(3190))
    if not OR_1:
        return
    if FlagDisabled(3180):
        return
    EnableFlag(1042369249)
    End()


@RestartOnRest(1042363702)
def Event_1042363702():
    """Event 1042363702"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(3185))
    AND_1.Add(FlagDisabled(3187))
    if AND_1:
        return
    if FlagDisabled(181):
        return
    EnableFlag(3198)
    End()


@RestartOnRest(1042363703)
def Event_1042363703():
    """Event 1042363703"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(60826):
        return
    
    MAIN.Await(FlagEnabled(400035))
    
    EnableFlag(60826)
    AwardGesture(gesture_param_id=60)
    End()


@RestartOnRest(1042360710)
def Event_1042360710(_, character: uint, asset: uint):
    """Event 1042360710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3746)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3746))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SetCurrentTime(
        time=(22, 30, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )
    CreateAssetVFX(asset, vfx_id=100, model_point=800227)
    SetCameraAngle(x_angle=0.0, y_angle=-115.86000061035156)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableBackread(character)
    EnableCharacter(character)
    SetCharacterTalkRange(character=character, distance=30.0)
    EnableImmortality(character)
    ForceAnimation(character, 930000)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3746))
    
    Restart()


@RestartOnRest(1042360711)
def Event_1042360711(_, character: uint):
    """Event 1042360711"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(4680))
    AND_1.Add(FlagDisabled(9000))
    AND_1.Add(EntityWithinDistance(entity=Assets.AEG099_060_9000, other_entity=20000, radius=5.0))
    AND_1.Add(HealthValue(character) > 0)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    EnableFlag(1042369411)
    EnableFlag(3758)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character)
    End()


@RestartOnRest(1042360712)
def Event_1042360712(_, entity: uint, asset: uint):
    """Event 1042360712"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042369410):
        return
    AND_1.Add(FlagEnabled(1042369401))
    OR_1.Add(FlagEnabled(1042362732))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    DisableFlag(1042369415)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_1)
    EnableFlag(1042369410)

    # --- Label 0 --- #
    DefineLabel(0)
    WaitFrames(frames=1)
    
    MAIN.Await(FlagDisabled(1042362733))
    
    EnableFlag(1042362734)
    ForceAnimation(entity, 20013)
    EnableFlag(4718)
    DeleteAssetVFX(asset)
    Wait(6.0)
    EnableFlag(1042369413)
    EnableFlag(3758)


@RestartOnRest(1042360713)
def Event_1042360713(_, entity: uint, asset: uint, character: uint):
    """Event 1042360713"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042369410):
        return
    AND_1.Add(FlagEnabled(3746))
    AND_1.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 30, 0)))
    
    MAIN.Await(AND_1)
    
    OR_2.Add(CharacterOutsideRegion(character=20000, region=1042362710))
    OR_2.Add(TimeOfDayInRange(earliest=(5, 30, 0), latest=(20, 0, 0)))
    OR_2.Add(PlayerTargeted(min_npc_threat_level=1, max_npc_threat_level=31, ai_status=AIStatusType.Battle))
    AND_2.Add(FlagDisabled(1042362733))
    AND_2.Add(OR_2)
    AND_3.Add(FlagEnabled(1042369410))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    DisableFlag(1042369415)
    ForceAnimation(entity, 20013)
    DeleteAssetVFX(asset)
    EnableFlag(4718)
    Kill(character)
    Wait(6.0)
    EnableFlag(3758)


@RestartOnRest(1042363720)
def Event_1042363720(_, character: uint, character_1: uint):
    """Event 1042363720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4700):
        DisableFlag(1042369303)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4705)
    GotoIfFlagEnabled(Label.L17, flag=4717)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    OR_3.Add(FlagEnabled(4705))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4700)
    GotoIfFlagEnabled(Label.L2, flag=4701)
    GotoIfFlagEnabled(Label.L3, flag=4702)
    GotoIfFlagEnabled(Label.L4, flag=4703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character, 930003)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(4705))
    
    MAIN.Await(not OR_4)
    
    Restart()

    # --- Label 17 --- #
    DefineLabel(17)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.NoTeam)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character, 930011)
    ForceAnimation(character_1, 930017)
    OR_5.Add(FlagEnabled(4705))
    OR_5.Add(FlagEnabled(4717))
    
    MAIN.Await(not OR_5)
    
    Restart()


@RestartOnRest(1042363723)
def Event_1042363723(_, character: uint):
    """Event 1042363723"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4700):
        return
    OR_1.Add(CharacterHasSpecialEffect(character, 9603))
    OR_1.Add(CharacterHasSpecialEffect(character, 9604))
    AND_1.Add(FlagEnabled(4701))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=9603)
    GotoIfCharacterHasSpecialEffect(Label.L4, character=character, special_effect=9604)

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20009)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    ForceAnimation(character, 20014)
    End()


@NeverRestart(1042360724)
def Event_1042360724(_, character: uint, character_1: uint):
    """Event 1042360724"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042369410):
        return
    AND_1.Add(FlagEnabled(4700))
    AND_1.Add(FlagEnabled(4717))
    
    MAIN.Await(AND_1)
    
    MAIN.Await(FlagEnabled(4705))
    
    ForceAnimation(character, 20019)
    ForceAnimation(character_1, 20017)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)


@RestartOnRest(1042363730)
def Event_1042363730(_, character: uint):
    """Event 1042363730"""
    WaitFrames(frames=1)
    EnableBackread(character)
    EnableCharacter(character)
    WaitFrames(frames=1)
    ForceAnimation(character, 30021)
    WaitFrames(frames=30)
    ForceAnimation(character, 30021)


@RestartOnRest(1042363740)
def Event_1042363740(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 1042363740"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372701)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1042363741)
def Event_1042363741(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 1042363741"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372701)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1042363742)
def Event_1042363742(_, other_entity: uint, flag: uint):
    """Event 1042363742"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4680):
        return
    
    MAIN.Await(FlagEnabled(4680))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363743)
def Event_1042363743(_, other_entity: uint, flag: uint):
    """Event 1042363743"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    
    MAIN.Await(FlagEnabled(1042379203))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363744)
def Event_1042363744(_, other_entity: uint, flag: uint):
    """Event 1042363744"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4680):
        return
    
    MAIN.Await(FlagEnabled(4680))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363745)
def Event_1042363745(_, other_entity: uint, flag: uint):
    """Event 1042363745"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    
    MAIN.Await(FlagEnabled(1042379203))
    
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363746)
def Event_1042363746(_, other_entity: uint, flag: uint):
    """Event 1042363746"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379207):
        return
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372702)
    
    MAIN.Await(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    
    DisableFlag(1042372702)
    Restart()


@RestartOnRest(1042363747)
def Event_1042363747(_, other_entity: uint, flag: uint):
    """Event 1042363747"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379207):
        return
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372702)
    
    MAIN.Await(EntityBeyondDistance(entity=20000, other_entity=other_entity, radius=5.0))
    
    DisableFlag(1042372702)
    Restart()


@RestartOnRest(1042360750)
def Event_1042360750(_, character: uint):
    """Event 1042360750"""
    DisableGravity(character)
    DisableAnimations(character)

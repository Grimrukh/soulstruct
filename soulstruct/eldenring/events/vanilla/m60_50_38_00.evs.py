"""
South Caelid (NE) (SW)

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
from .entities.m60_50_38_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1050380000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005200(
        0,
        character=Characters.Bat,
        animation_id=30000,
        animation_id_1=20000,
        region=1050382200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1050383700(0, character=Characters.SageGowry0, character_1=Characters.SageGowry1)
    CommonFunc_90005702(0, character=Characters.SageGowry0, flag=4163, first_flag=4160, last_flag=4163)
    CommonFunc_90005702(0, character=Characters.SageGowry1, flag=4163, first_flag=4160, last_flag=4163)
    Event_1050383701()
    Event_1050383702()
    Event_1050383703(0, character=Characters.KindredofRot)
    Event_1050383704(
        0,
        character=Characters.SageGowry0,
        asset=Assets.AEG007_506_2000,
        character_1=Characters.SageGowry1,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9001,
        action_button_id=4110,
        item_lot=103120,
        first_flag=400312,
        last_flag=400312,
        flag=7611,
        model_point=0,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9001,
        action_button_id=4110,
        item_lot=103120,
        first_flag=400312,
        last_flag=400312,
        flag=1050389238,
        model_point=0,
    )
    Event_1050383710(0, character=Characters.Millicent0)
    CommonFunc_90005704(0, attacked_entity=Characters.Millicent0, flag=4181, flag_1=4180, flag_2=1050389251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Millicent0,
        flag=4181,
        flag_1=4182,
        flag_2=1050389251,
        flag_3=1059481190,
        first_flag=4180,
        last_flag=4184,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Millicent0, flag=4183, first_flag=4180, last_flag=4184)
    Event_1050383711(0, character=Characters.Millicent2)
    CommonFunc_90005704(0, attacked_entity=Characters.Millicent2, flag=4181, flag_1=4180, flag_2=1050389251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Millicent2,
        flag=4181,
        flag_1=4182,
        flag_2=1050389251,
        flag_3=1059481190,
        first_flag=4180,
        last_flag=4184,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Millicent2, flag=4183, first_flag=4180, last_flag=4184)
    Event_1050383712(0, character=Characters.Millicent1)
    CommonFunc_90005704(0, attacked_entity=Characters.Millicent1, flag=4181, flag_1=4180, flag_2=1050389261, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Millicent1,
        flag=4181,
        flag_1=4182,
        flag_2=1050389261,
        flag_3=1059481190,
        first_flag=4180,
        last_flag=4184,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Millicent1, flag=4183, first_flag=4180, last_flag=4184)
    Event_1050383713()
    Event_1050383714()
    CommonFunc_90005752(0, asset=1050381700, vfx_id=200, model_point=120, seconds=3.0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.SageGowry0)
    DisableBackread(Characters.KindredofRot)
    DisableBackread(Characters.SageGowry1)
    DisableBackread(Characters.Millicent0)
    DisableBackread(Characters.Millicent1)
    DisableAsset(Assets.AEG099_320_9000)


@RestartOnRest(1050383700)
def Event_1050383700(_, character: uint, character_1: uint):
    """Event 1050383700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(4165))
    OR_1.Add(FlagEnabled(4166))
    OR_1.Add(FlagEnabled(4167))
    OR_1.Add(FlagEnabled(4168))
    OR_1.Add(FlagEnabled(4169))
    OR_1.Add(FlagEnabled(4170))
    OR_1.Add(FlagEnabled(4171))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(Assets.AEG007_506_2000)
    OR_1.Add(FlagEnabled(4165))
    OR_1.Add(FlagEnabled(4166))
    OR_1.Add(FlagEnabled(4167))
    OR_1.Add(FlagEnabled(4168))
    OR_1.Add(FlagEnabled(4169))
    OR_1.Add(FlagEnabled(4170))
    OR_1.Add(FlagEnabled(4171))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L3, flag=4171)
    GotoIfFlagEnabled(Label.L1, flag=4160)
    GotoIfFlagEnabled(Label.L2, flag=4161)
    GotoIfFlagEnabled(Label.L4, flag=4163)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableAsset(Assets.AEG007_506_2000)
    RestoreAsset(Assets.AEG007_506_2000)
    EnableAssetInvulnerability(Assets.AEG007_506_2000)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 90102)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(Assets.AEG007_506_2000)
    AND_1.Add(FlagDisabled(1050389266))
    AND_1.Add(FlagDisabled(4183))
    AND_1.Add(FlagEnabled(4187))
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    EnableAsset(Assets.AEG007_506_2000)
    RestoreAsset(Assets.AEG007_506_2000)
    EnableAssetInvulnerability(Assets.AEG007_506_2000)
    SkipLinesIfFlagRangeAllDisabled(4, (4165, 4168))
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    SkipLines(4)
    SkipLinesIfFlagRangeAllDisabled(3, (4169, 4170))
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 90100)
    AND_3.Add(FlagEnabled(4168))
    AND_3.Add(FlagDisabled(1050389230))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character, 90101)
    SkipLinesIfFlagRangeAllDisabled(1, (4169, 4170))
    ForceAnimation(character_1, 90101)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    DisableAsset(Assets.AEG007_506_2000)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(4165))
    OR_15.Add(FlagEnabled(4166))
    OR_15.Add(FlagEnabled(4167))
    OR_15.Add(FlagEnabled(4168))
    OR_15.Add(FlagEnabled(4169))
    OR_15.Add(FlagEnabled(4170))
    OR_15.Add(FlagEnabled(4171))
    AwaitConditionFalse(OR_15)
    Restart()


@RestartOnRest(1050383701)
def Event_1050383701():
    """Event 1050383701"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(4166))
    AND_1.Add(FlagEnabled(1050389255))
    AwaitConditionTrue(AND_1)
    EnableFlag(4178)
    End()


@RestartOnRest(1050383702)
def Event_1050383702():
    """Event 1050383702"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1050389228))
    AND_1.Add(FlagEnabled(1050389217))
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    AwaitFlagEnabled(flag=110850)
    EnableNetworkFlag(1050389228)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1050383703)
def Event_1050383703(_, character: uint):
    """Event 1050383703"""
    DisableCharacter(character)
    DisableBackread(character)
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(HealthValue(Characters.SageGowry0) == 0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.SageGowry0))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterBackreadEnabled(Characters.SageGowry0))
    OR_2.Add(HealthValue(Characters.SageGowry1) == 0)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.SageGowry1))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterBackreadEnabled(Characters.SageGowry1))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    AwaitConditionTrue(OR_3)
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_1)
    Kill(Characters.SageGowry0, award_runes=True)
    SkipLines(1)
    Kill(Characters.SageGowry1, award_runes=True)
    Wait(5.0)
    OR_4.Add(FlagEnabled(4169))
    OR_4.Add(FlagEnabled(4170))
    GotoIfConditionTrue(Label.L2, input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    Move(
        character,
        destination=Characters.SageGowry0,
        destination_type=CoordEntityType.Character,
        model_point=900,
        short_move=True,
    )
    EnableAnimations(character)
    ForceAnimation(character, 930010)
    DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
    EnableNetworkFlag(4163)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
    EnableNetworkFlag(4163)
    EnableNetworkFlag(1050389238)
    End()


@RestartOnRest(1050383704)
def Event_1050383704(_, character: uint, asset: uint, character_1: uint):
    """Event 1050383704"""
    EnableAssetInvulnerability(asset)
    OR_1.Add(HealthValue(character) == 0)
    OR_1.Add(HealthValue(character_1) == 0)
    
    MAIN.Await(OR_1)
    
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset, request_slot=0)
    End()


@RestartOnRest(1050383710)
def Event_1050383710(_, character: uint):
    """Event 1050383710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(4185))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(Assets.AEG099_320_9000)
    OR_2.Add(FlagEnabled(4185))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableAsset(Assets.AEG099_320_9000)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAsset(Assets.AEG099_320_9000)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(Assets.AEG099_320_9000)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_1.Add(FlagDisabled(4185))
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(1050383711)
def Event_1050383711(_, character: uint):
    """Event 1050383711"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4180):
        DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(4186))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_2.Add(FlagEnabled(4186))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    DisableAsset(Assets.AEG099_320_9000)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    AND_1.Add(FlagDisabled(4186))
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(1050383712)
def Event_1050383712(_, character: uint):
    """Event 1050383712"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4180):
        DisableFlag(1050389253)
    DisableNetworkFlag(1050389265)
    DisableNetworkFlag(1038519255)
    DisableNetworkFlag(4197)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(4187))
    AND_1.Add(FlagDisabled(1050389266))
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    if PlayerNotInOwnWorld():
        AND_3.Add(FlagEnabled(4187))
        AND_3.Add(FlagDisabled(4197))
        GotoIfConditionTrue(Label.L6, input_condition=AND_3)
    DisableCharacter(character)
    DisableBackread(character)
    AND_2.Add(FlagEnabled(4187))
    AND_2.Add(FlagDisabled(1050389266))
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableNetworkFlag(1050389265)
    DisableNetworkFlag(1038519255)
    DisableNetworkFlag(4197)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(4187))
    
    Restart()


@RestartOnRest(1050383713)
def Event_1050383713():
    """Event 1050383713"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4185):
        return
    
    MAIN.Await(FlagDisabled(1050389255))
    
    MAIN.Await(FlagEnabled(1050382716))
    
    WaitFrames(frames=2)
    PlayCutscene(60500000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(1050382717)
    ForceAnimation(Characters.Millicent0, 90102)
    WaitFramesAfterCutscene(frames=1)
    End()


@RestartOnRest(1050383714)
def Event_1050383714():
    """Event 1050383714"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=Characters.Millicent0, distance=17.0)
    if FlagEnabled(1050389255):
        return
    SetCharacterTalkRange(character=Characters.Millicent0, distance=50.0)
    AND_1.Add(FlagDisabled(1050389255))
    AND_1.Add(FlagDisabled(1050382713))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1050382710))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1050382713)
    End()

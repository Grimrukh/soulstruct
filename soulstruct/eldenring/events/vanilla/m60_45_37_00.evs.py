"""
East Limgrave (SW) (NE)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_45_37_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, vfx_id=100, dummy_id=800, right=0)
    CommonFunc_90005251(0, character=1045370201, radius=80.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1045370207, radius=50.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1045370214, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1045370216, radius=50.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005511(
        0,
        flag=1045370560,
        asset=Assets.AEG239_001_2000,
        obj_act_id=1045373560,
        obj_act_id_1=257018,
        left=0,
    )
    CommonFunc_90005512(0, flag=1045370560, region=1045372550, region_1=1045372551)
    CommonFunc_90005640(0, flag=1045370560, asset=Assets.AEG239_001_2000)
    Event_1045372230()
    CommonFunc_90005261(
        0,
        character=Characters.LargeDemiHuman,
        region=1045372240,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=Characters.DemiHuman0, region=1045372240, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.DemiHuman1, region=1045372240, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.DemiHuman2, region=1045372240, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.DemiHuman3, region=1045372240, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Runebear2, radius=4.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.Runebear1,
        animation_id=30002,
        animation_id_1=20002,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1045372344()
    CommonFunc_90005300(0, flag=1045370200, character=Characters.Scarab, item_lot=40116, seconds=0.0, item_is_dropped=0)
    CommonFunc_90005400(0, character=Characters.Runebear3, special_effect=0, seconds=0.0, seconds_1=0.0, left=0)
    CommonFunc_90005401(0, flag=98101, character=Characters.Runebear3)
    CommonFunc_90005637(0, flag=1045378601, character=Characters.WanderingNoble, region=1045371620)
    CommonFunc_90005636(
        0,
        flag=1045378601,
        character=Characters.WanderingNoble,
        entity=Assets.AEG099_374_9000,
        special_effect=4470,
        destination=1045372620,
        region=1045372621,
        flag_1=1045372620,
        patrol_information_id=1045373620,
        right=-1,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Blaidd, flag=3601, flag_1=3600, flag_2=1045379201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Blaidd,
        flag=3601,
        flag_1=3602,
        flag_2=1045379201,
        flag_3=3603,
        first_flag=3600,
        last_flag=3603,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Blaidd, flag=3603, first_flag=3600, last_flag=3604)
    Event_1045370710(0, character=Characters.Blaidd)
    Event_1045370711(0, character=Characters.Blaidd, destination=1045372700)
    Event_1045370714(0, character=Characters.Blaidd)
    Event_1045370713()
    CommonFunc_90005731(0, flag=1045379221, other_entity=Characters.Blaidd, radius=70.0, radius_1=90.0)
    CommonFunc_90005730(
        0,
        flag=1045379220,
        seconds=60.0,
        flag_1=1045379221,
        flag_2=3605,
        flag_3=1045370711,
        flag_4=1045379223,
    )
    CommonFunc_90005732(0, flag=1045379223, region=1045372701, region_1=1045372701)
    CommonFunc_90005730(
        0,
        flag=1045379222,
        seconds=15.0,
        flag_1=1045379223,
        flag_2=3605,
        flag_3=1045370711,
        flag_4=1045372706,
    )
    Event_1045370720()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Blaidd)
    DisableBackread(1045370701)
    EnableAssetInvulnerability(Assets.AEG700_045_1000)


@RestartOnRest(1045372200)
def Event_1045372200(_, asset: uint, entity: uint, flag: uint):
    """Event 1045372200"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateAssetVFX(asset, vfx_id=200, dummy_id=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1045372230)
def Event_1045372230():
    """Event 1045372230"""
    DropMandatoryTreasure(1045370234)
    DropMandatoryTreasure(1045370235)
    End()


@RestartOnRest(1045372344)
def Event_1045372344():
    """Event 1045372344"""
    RestoreAsset(Assets.AEG801_256_7007)


@RestartOnRest(1045370650)
def Event_1045370650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1045370650"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=EAST_LIMGRAVE_SW_NE))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9120, flag=flag_1, bit_count=1)


@RestartOnRest(1045370710)
def Event_1045370710(_, character: uint):
    """Event 1045370710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3600):
        DisableFlag(1045379202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=3605)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3605))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3601)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    if FlagDisabled(1045370711):
        ForceAnimation(character, 930012)
        Goto(Label.L20)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3605))
    
    Restart()


@RestartOnRest(1045370711)
def Event_1045370711(_, character: uint, destination: uint):
    """Event 1045370711"""
    if ThisEventSlotFlagEnabled():
        return
    DisableNetworkSync()
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    AND_2.Add(FlagEnabled(3600))
    AND_2.Add(FlagEnabled(3605))
    OR_2.Add(ThisEventSlotFlagEnabled())
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    SetTeamType(character, TeamType.NoTeam)
    DisableAI(character)
    EnableInvincibility(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    WaitFrames(frames=1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    if PlayerNotInOwnWorld():
        return
    EnableNetworkSync()
    AND_1.Add(FlagEnabled(3600))
    AND_1.Add(FlagEnabled(3605))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9672))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1045372701))
    OR_1.Add(ThisEventSlotFlagEnabled())
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableThisNetworkSlotFlag()
    Wait(0.30000001192092896)
    ForceAnimation(character, 20055)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    WaitFrames(frames=1)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9671))
    
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableAI(character)
    EnableFlag(1045372707)
    DisableInvincibility(character)


@RestartOnRest(1045370712)
def Event_1045370712():
    """Event 1045370712"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045370711):
        return
    DisableNetworkSync()
    
    MAIN.Await(FlagDisabled(1045379221))
    
    AND_1.Add(FlagEnabled(3600))
    AND_1.Add(FlagEnabled(3605))
    AND_1.Add(FlagDisabled(1045372705))
    AND_1.Add(FlagEnabled(1045379221))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1045379220)


@RestartOnRest(1045370713)
def Event_1045370713():
    """Event 1045370713"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045370711):
        return
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(1045372706))
    
    Wait(15.0)
    DisableFlag(1045372706)
    Restart()


@RestartOnRest(1045370714)
def Event_1045370714(_, character: uint):
    """Event 1045370714"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045370711):
        return
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=1045372705)
    SetCharacterTalkRange(character=character, distance=160.0)
    AND_1.Add(FlagEnabled(3600))
    AND_1.Add(FlagEnabled(3605))
    AND_1.Add(FlagEnabled(1045372705))
    AND_2.Add(FlagEnabled(3600))
    AND_2.Add(FlagEnabled(3605))
    AND_2.Add(FlagEnabled(1045370711))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=character, distance=160.0)
    AND_3.Add(FlagEnabled(3600))
    AND_3.Add(FlagEnabled(3605))
    AND_3.Add(FlagEnabled(1045370711))
    
    MAIN.Await(AND_3)
    
    SetCharacterTalkRange(character=character, distance=17.0)
    End()


@RestartOnRest(1045370720)
def Event_1045370720():
    """Event 1045370720"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045379250):
        return
    if FlagDisabled(31008522):
        return
    EnableFlag(1045379250)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1045372710, radius=1.0))
    if not AND_1:
        return
    EnableFlag(9080)
    ForceAnimation(PLAYER, 60131)
    SetRespawnPoint(respawn_point=1045372710)
    SaveRequest()
    End()

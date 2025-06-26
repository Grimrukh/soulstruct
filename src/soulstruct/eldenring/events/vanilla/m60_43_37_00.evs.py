"""
West Limgrave (SE) (NE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_43_37_00_enums import *
from .enums.m60_43_39_00_enums import Characters as m60_43_39_00_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043370000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005300(0, flag=1043370210, character=Characters.Scarab, item_lot=40108, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1043370800, character=Characters.NightsCavalryHorse, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005476(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    RunCommonEvent(90005477)
    Event_1043372340(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    CommonFunc_90005860(
        0,
        flag=1043370800,
        left=0,
        character=Characters.NightsCavalry,
        left_1=0,
        item_lot=1043370400,
        seconds=0.0,
    )
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry,
        name=903150600,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse,
    )
    CommonFunc_90005872(0, character=Characters.NightsCavalry, npc_threat_level=10, right=0)
    Event_1043373700(0, character=1043370700, character_1=1043370701, character_2=1043370702, asset=1043376700)
    Event_1043373703(0, character=1043370700)
    Event_1043373705(0, character=1043370700)
    CommonFunc_90005703(
        0,
        character=1043370700,
        flag=4701,
        flag_1=4702,
        flag_2=1043379249,
        flag_3=4701,
        first_flag=4700,
        last_flag=4703,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=1043370700, flag=4701, flag_1=4700, flag_2=1043379249, right=3)
    CommonFunc_90005702(0, character=1043370700, flag=4703, first_flag=4700, last_flag=4703)
    CommonFunc_90005703(
        0,
        character=1043370701,
        flag=1043379246,
        flag_1=1043379246,
        flag_2=1043379247,
        flag_3=1043379246,
        first_flag=1043379246,
        last_flag=1043379246,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=1043370701, flag=1043379246, flag_1=1043379246, flag_2=1043379247, right=3)
    RunCommonEvent(1043373706, slot=0, args=(1043370700, 1043370701), arg_types="II")
    Event_1043373707(
        0,
        character=1043370700,
        first_flag=4700,
        flag=4701,
        flag_1=4702,
        last_flag=4703,
        character_1=1043370701,
        flag_2=1043379246,
    )
    Event_1043373701()
    Event_1043373710(0, character=1043370730)
    Event_1043373711()
    Event_1043373722(
        0,
        character=Characters.BloodyFingerNerijus,
        region=1043372709,
        region_1=1043372711,
        region_2=1043372701,
        region_3=1043382700,
    )
    Event_1043373726(0, character=Characters.BloodyFingerNerijus)
    CommonFunc_90005791(
        0,
        flag=1043379262,
        flag_1=1043372715,
        flag_2=1043372716,
        character=Characters.BloodyFingerNerijus,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=1043379262,
        summon_flag=1043372715,
        dismissal_flag=1043372716,
        character=Characters.BloodyFingerNerijus,
        sign_type=21,
        region=1043382710,
        region_1=1043372709,
        seconds=0.0,
        right_1=1043372740,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=1043379262,
        summon_flag=1043372715,
        dismissal_flag=1043372716,
        character=Characters.BloodyFingerNerijus,
        sign_type=21,
        region=1043372712,
        region_1=1043372711,
        seconds=0.0,
        right_1=1043372741,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005774(0, flag=1043379262, item_lot=1042370700, flag_1=1042377700)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3940,
        flag_2=1043379351,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3942,
        flag_2=1043379351,
        flag_3=3941,
        first_flag=3940,
        last_flag=3944,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.DemiHumanShaman, flag=3943, first_flag=3940, last_flag=3944)
    Event_1043373730(0, character=Characters.DemiHumanShaman, asset=Assets.AEG801_480_9000)
    Event_1043373731(0, seconds=13.0, seconds_1=13.0, seconds_2=25.0)
    Event_1043373732(0, character=Characters.DemiHumanShaman, asset=Assets.AEG801_480_9000)
    Event_1043373733(0, character=Characters.DemiHumanShaman)
    Event_1043373734(0, entity=Characters.DemiHumanShaman)
    CommonFunc_90005630(0, far_view_id=61433700, asset=Assets.AEG099_130_9000, dummy_id=127)
    CommonFunc_90005460(0, character=1043370200)
    CommonFunc_90005461(0, character=1043370200)
    CommonFunc_90005462(0, character=1043370200)
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61010)
    Event_1043372650(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043370711)
    DisableBackread(m60_43_39_00_Characters.WanderingNoble)
    DisableBackread(Characters.BloodyFingerNerijus)
    DisableBackread(Characters.DemiHumanShaman)
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton0,
        animation_id=30019,
        animation_id_1=20019,
        region=1043372240,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton1,
        animation_id=30019,
        animation_id_1=20019,
        region=1043372240,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton2,
        animation_id=30019,
        animation_id_1=20019,
        region=1043372240,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton3,
        animation_id=30019,
        animation_id_1=20019,
        region=1043372240,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton4,
        animation_id=30019,
        animation_id_1=20019,
        region=1043372240,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Scarab, region=1043372210, radius=3.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1043372250)
def Event_1043372250(_, character: uint, region: uint, owner_entity: uint):
    """Event 1043372250"""
    if FlagEnabled(1041382200):
        return
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableFlag(1041382200)
    AND_5.Add(CharacterDead(character))
    if AND_5:
        return
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    AND_7.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    if AND_7:
        return
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    EnableCharacter(character)
    ForceAnimation(character, 20011)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        dummy_id=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    RemoveSpecialEffect(character, 8090)


@RestartOnRest(1043372340)
def Event_1043372340(_, character: Character | int, character_1: Character | int):
    """Event 1043372340"""
    AND_1.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    AND_2.Add(CharacterHasSpecialEffect(character, 11825))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_3)
    
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_4.Add(CharacterBackreadDisabled(character_1))
    
    MAIN.Await(AND_4)
    
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@RestartOnRest(1043372650)
def Event_1043372650(
    _,
    tutorial_param_id: int,
    flag: Flag | int,
    tutorial_param_id_1: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 1043372650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_SE_NE))
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


@RestartOnRest(1043373700)
def Event_1043373700(
    _,
    character: uint,
    character_1: Character | int,
    character_2: Character | int,
    asset: Asset | int,
):
    """Event 1043373700"""
    WaitFrames(frames=1)
    DisableFlag(1043379200)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(FlagEnabled(4700))
    AND_1.Add(FlagEnabled(1043379248))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379248)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    OR_1.Add(FlagEnabled(4705))
    OR_1.Add(FlagEnabled(4706))
    OR_1.Add(FlagEnabled(4707))
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=4700)
    GotoIfFlagEnabled(Label.L2, flag=4701)
    GotoIfFlagEnabled(Label.L4, flag=4703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    if FlagEnabled(4980):
        ForceAnimation(character, 30001)
    if FlagRangeAnyEnabled((4982, 4983)):
        ForceAnimation(character, 30002)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    if FlagEnabled(4980):
        ForceAnimation(character, 30001)
    if FlagRangeAnyEnabled((4982, 4983)):
        ForceAnimation(character, 30002)
        DisableAI(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(1043379200))
    
    Restart()


@RestartOnRest(1043373701)
def Event_1043373701():
    """Event 1043373701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043379229):
        return
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=1043370700, radius=7.5))
    
    EnableNetworkFlag(1043379229)
    End()


@ContinueOnRest(1043373703)
def Event_1043373703(_, character: uint):
    """Event 1043373703"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(4705))
    OR_1.Add(FlagEnabled(4706))
    OR_1.Add(FlagEnabled(4707))
    OR_2.Add(FlagEnabled(4700))
    OR_2.Add(FlagEnabled(4701))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    if not AND_1:
        return
    GotoIfFlagEnabled(Label.L0, flag=4980)
    GotoIfFlagRangeAnyEnabled(Label.L10, flag_range=(4982, 4983))

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(CharacterHasSpecialEffect(character, 9601))
    OR_5.Add(CharacterHasSpecialEffect(character, 9603))
    
    MAIN.Await(OR_5)
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=9601)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=9603)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_6.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=character, radius=4.0))
    OR_6.Add(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    MAIN.Await(OR_6)
    
    if CharacterHasSpecialEffect(character=character, special_effect=9601):
        ForceAnimation(character, 20004)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_7.Add(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=character, radius=6.0))
    OR_7.Add(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    MAIN.Await(OR_7)
    
    if CharacterHasSpecialEffect(character=character, special_effect=9603):
        ForceAnimation(character, 20010)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_10.Add(CharacterHasSpecialEffect(character, 9603))
    
    MAIN.Await(OR_10)
    
    GotoIfCharacterHasSpecialEffect(Label.L11, character=character, special_effect=9603)

    # --- Label 11 --- #
    DefineLabel(11)
    OR_11.Add(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=character, radius=6.0))
    OR_11.Add(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    MAIN.Await(OR_11)
    
    if CharacterHasSpecialEffect(character=character, special_effect=9603):
        ForceAnimation(character, 20011)
        DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1043373705)
def Event_1043373705(_, character: Character | int):
    """Event 1043373705"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(4705))
    OR_1.Add(FlagEnabled(4706))
    OR_1.Add(FlagEnabled(4707))
    OR_2.Add(FlagEnabled(4700))
    OR_2.Add(FlagEnabled(4701))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    if not AND_1:
        return
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=9602)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9602))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(character)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9602))
    
    Restart()


@RestartOnRest(1043373706)
def Event_1043373706(_, character: uint, attacked_entity: Character | int):
    """Event 1043373706"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1043372709))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1043372708)
    if FlagEnabled(4701):
        return
    if CharacterHasSpecialEffect(character=character, special_effect=9601):
        ForceAnimation(character, 20004)
    if CharacterHasSpecialEffect(character=character, special_effect=9602):
        ForceAnimation(character, 20006)


@ContinueOnRest(1043373707)
def Event_1043373707(
    _,
    character: Character | int,
    first_flag: Flag | int,
    flag: Flag | int,
    flag_1: Flag | int,
    last_flag: Flag | int,
    character_1: Character | int,
    flag_2: Flag | int,
):
    """Event 1043373707"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagDisabled(3000))
    
    if FlagDisabled(first_flag):
        return
    DisableNetworkFlag(flag_2)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    AND_1.Add(HealthValue(character) < 1)
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_3.Add(FlagEnabled(flag_2))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=ALL_PLAYERS))
    AND_3.Add(HealthValue(character_1) < 1)
    OR_4.Add(OR_3)
    OR_4.Add(AND_3)
    OR_5.Add(OR_2)
    OR_5.Add(OR_4)
    
    MAIN.Await(OR_5)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_2)
    GotoIfLastConditionResultTrue(Label.L5, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(flag_2)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1043373710)
def Event_1043373710(_, character: uint):
    """Event 1043373710"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023)


@RestartOnRest(1043373711)
def Event_1043373711():
    """Event 1043373711"""
    AND_1.Add(FlagDisabled(1043379305))
    AND_1.Add(FlagDisabled(1043379306))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1043370730, radius=8.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1043372722)


@RestartOnRest(1043373721)
def Event_1043373721(_, character: Character | int, flag: Flag | int, distance: float):
    """Event 1043373721"""
    if PlayerNotInOwnWorld():
        return
    DisableBackread(character)
    if FlagDisabled(3620):
        return
    AND_1.Add(FlagDisabled(3625))
    AND_1.Add(FlagDisabled(3626))
    if AND_1:
        return
    if FlagEnabled(1043379262):
        return
    if FlagEnabled(1043372716):
        return
    AND_2.Add(FlagDisabled(1043372713))
    AND_2.Add(FlagEnabled(1043372717))
    
    MAIN.Await(AND_2)
    
    EnableBackread(character)
    SetCharacterTalkRange(character=character, distance=distance)
    EnableNetworkFlag(flag)
    End()


@RestartOnRest(1043373722)
def Event_1043373722(
    _,
    character: Character | int,
    region: Region | int,
    region_1: Region | int,
    region_2: Region | int,
    region_3: Region | int,
):
    """Event 1043373722"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043379262):
        return
    if FlagEnabled(1043372716):
        return
    GotoIfFlagDisabled(Label.L1, flag=1043372714)
    GotoIfFlagEnabled(Label.L2, flag=1043372714)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    
    MAIN.Await(OR_3)
    
    GotoIfCharacterInsideRegion(Label.L5, character=PLAYER, region=region)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableFlag(1043372740)
    DisableFlag(1043372741)
    Goto(Label.L7)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(1043372741)
    DisableFlag(1043372740)
    Goto(Label.L7)

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(1043372714)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    OR_2.Add(CharacterDead(character))
    
    MAIN.Await(OR_2)
    
    DisableFlag(1043372714)
    DisableFlag(1043372740)
    DisableFlag(1043372741)
    EnableFlag(1043379263)
    AND_2.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(1043379262)
    WaitFrames(frames=1)
    EnableFlag(3638)
    DisableFlag(1043369200)
    if FlagEnabled(1043379262):
        return
    SendNPCSummonHome(character=character)
    End()


@RestartOnRest(1043373726)
def Event_1043373726(_, character: Character | int):
    """Event 1043373726"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043379262):
        return
    if FlagEnabled(1043372716):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9760))
    
    Wait(5.0)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    End()


@RestartOnRest(1043373730)
def Event_1043373730(_, character: uint, asset: Asset | int):
    """Event 1043373730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3940))
    AND_1.Add(FlagEnabled(1043379353))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379353)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_1.Add(FlagEnabled(3945))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3945))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L5, flag=1043379357)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    SetCharacterTalkRange(character=character, distance=70.0)
    EnableBackread(character)
    DisableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableAsset(asset)
    DisableAnimations(character)
    ForceAnimation(character, 930010)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930010)
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
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3945))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1043373731)
def Event_1043373731(_, seconds: float, seconds_1: float, seconds_2: float):
    """Event 1043373731"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3945):
        return
    if FlagEnabled(1043379357):
        return
    EnableFlag(1043372732)
    
    MAIN.Await(FlagEnabled(1043372733))
    
    Wait(seconds)
    EnableFlag(1043372734)
    
    MAIN.Await(FlagEnabled(1043372735))
    
    Wait(seconds_1)
    EnableFlag(1043372736)
    
    MAIN.Await(FlagEnabled(1043372737))
    
    Wait(seconds_2)
    DisableFlag(1043372732)
    DisableFlag(1043372733)
    DisableFlag(1043372734)
    DisableFlag(1043372735)
    DisableFlag(1043372736)
    DisableFlag(1043372737)
    Restart()


@RestartOnRest(1043373732)
def Event_1043373732(_, character: uint, asset: uint):
    """Event 1043373732"""
    GotoIfPlayerNotInOwnWorld(Label.L0)
    if FlagEnabled(1044342300):
        return
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=ALL_PLAYERS))
    AND_1.Add(OR_2)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(1043379357)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagEnabled(flag=1043379357)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableAsset(asset)
    Wait(0.30000001192092896)
    EnableCharacter(character)
    EnableAnimations(character)
    End()


@RestartOnRest(1043373733)
def Event_1043373733(_, character: uint):
    """Event 1043373733"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    SetBackreadStateAlternate(character, False)
    if FlagDisabled(3945):
        return
    if FlagEnabled(1043379357):
        return
    AND_1.Add(FlagDisabled(1043379357))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=15.0))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character, True)
    AND_2.Add(FlagDisabled(1043379357))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=15.0))
    
    MAIN.Await(not AND_2)
    
    SetBackreadStateAlternate(character, False)
    Restart()


@RestartOnRest(1043373734)
def Event_1043373734(_, entity: uint):
    """Event 1043373734"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3945):
        return
    if FlagDisabled(3940):
        return
    
    MAIN.Await(FlagEnabled(3941))
    
    ForceAnimation(entity, 20043)
    Restart()

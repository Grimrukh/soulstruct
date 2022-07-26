"""
East Weeping Peninsula (NW) (NW)

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
from .entities.m60_44_35_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044350000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76161,
        flag_1=76106,
        asset=Assets.AEG099_090_9003,
        source_flag=77110,
        value=0,
        flag_2=78110,
        flag_3=78111,
        flag_4=78112,
        flag_5=78113,
        flag_6=78114,
        flag_7=78115,
        flag_8=78116,
        flag_9=78117,
        flag_10=78118,
        flag_11=78119,
    )
    CommonFunc_90005880(
        0,
        flag=1044350800,
        flag_1=1044350805,
        flag_2=1044352800,
        character=Characters.BloodhoundKnight,
        item_lot=30130,
        area_id=60,
        block_id=44,
        cc_id=35,
        dd_id=0,
        player_start=1044352805,
    )
    CommonFunc_90005881(
        0,
        flag=1044350800,
        flag_1=1044350805,
        left_flag=1044352801,
        cancel_flag__right_flag=1044352802,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=44,
        cc_id=35,
        dd_id=0,
        player_start=1044352805,
    )
    CommonFunc_90005882(
        0,
        flag=1044350800,
        flag_1=1044350805,
        flag_2=1044352800,
        character=Characters.BloodhoundKnight,
        flag_3=1044352806,
        character_1=1044355810,
        asset=Assets.AEG099_120_9000,
        owner_entity=Characters.Dummy,
        source_entity=1044352810,
        name=904290520,
        animation_id=-1,
        animation_id_1=20021,
    )
    CommonFunc_90005883(0, flag=1044350800, flag_1=1044350805, entity=Assets.AEG099_170_1000)
    CommonFunc_90005885(
        0,
        flag=1044350800,
        bgm_boss_conv_param_id=0,
        flag_1=1044352806,
        flag_2=1044352807,
        left=0,
        left_1=1,
    )
    CommonFunc_90005390(
        0,
        flag=1035430270,
        flag_1=1035432270,
        anchor_entity=Characters.WanderingNoble2,
        character=Characters.Runebear,
        left=1,
        item_lot=1044350100,
    )
    CommonFunc_90005391(
        0,
        flag=1035430270,
        flag_1=1035432270,
        character=Characters.WanderingNoble2,
        character_1=Characters.Runebear,
        left=1,
    )
    CommonFunc_90005701(0, attacked_entity=1044350720, flag=3981, flag_1=3982, flag_2=1044359301, right=3)
    CommonFunc_90005700(
        0,
        character=1044350720,
        flag=3981,
        flag_1=3982,
        flag_2=1044359301,
        value=0.6499999761581421,
        first_flag=3980,
        last_flag=3983,
        right=-1,
    )
    CommonFunc_90005702(0, character=1044350720, flag=3983, first_flag=3980, last_flag=3983)
    Event_1044353720(0, asset__character=1044350720)
    Event_1044352740(0, character=1044350710, character_1=1044350705)
    CommonFunc_90005780(
        0,
        flag=1044350800,
        summon_flag=1044352160,
        dismissal_flag=1044352161,
        character=Characters.Blaidd1,
        sign_type=20,
        region=1044352720,
        right=1044349257,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=1044350800, flag_1=1044352160, flag_2=1044352161, character=Characters.Blaidd1)
    CommonFunc_90005783(
        0,
        flag=1044350800,
        flag_1=1044352160,
        flag_2=1044352161,
        character=Characters.Blaidd1,
        other_entity=1044352720,
        region=0,
        left=0,
    )
    Event_1044352600(0, attacked_entity=Assets.AEG099_280_9000, region=1044352600)
    Event_1044352650(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370,
    )
    Event_1044350710(0, character=Characters.Blaidd0, character_1=Characters.TalkDummy3)
    CommonFunc_90005704(0, attacked_entity=Characters.Blaidd0, flag=3601, flag_1=3600, flag_2=1044359251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Blaidd0,
        flag=3601,
        flag_1=3602,
        flag_2=1044359251,
        flag_3=3603,
        first_flag=3600,
        last_flag=3603,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Blaidd0, flag=3603, first_flag=3600, last_flag=3604)
    Event_1044350715(0, character=Characters.Blaidd0, character_1=Characters.TalkDummy3)
    CommonFunc_90005730(
        0,
        flag=1044359257,
        seconds=20.0,
        flag_1=1044359265,
        flag_2=3615,
        flag_3=1044359255,
        flag_4=1044359256,
    )
    CommonFunc_90005731(0, flag=1044359265, other_entity=Characters.TalkDummy3, radius=30.0, radius_1=50.0)
    Event_1044350711()
    Event_1044350713()
    Event_1044350712(0, character=Characters.TalkDummy2)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Blaidd0)
    DisableBackread(Characters.TalkDummy3)
    Event_1044352250()
    CommonFunc_90005251(0, character=Characters.SmallCrab0, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.SmallCrab1, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.SmallCrab2, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.SmallCrab3, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.WildMouflon0, radius=15.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.WildMouflon1, radius=15.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble0,
        region=1044352220,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005251(0, character=Characters.WanderingNoble1, radius=55.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1044352250)
def Event_1044352250():
    """Event 1044352250"""
    Kill(1044350250)
    Kill(1044350251)


@RestartOnRest(1044352600)
def Event_1044352600(_, attacked_entity: uint, region: uint):
    """Event 1044352600"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 810000099, sound_type=SoundType.Unknown14)
    ForceAnimation(attacked_entity, 1)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(2.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()


@RestartOnRest(1044352650)
def Event_1044352650(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044352650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(InsideMap(game_map=EAST_WEEPING_PENINSULA_NW_NW))
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


@RestartOnRest(1044352740)
def Event_1044352740(_, character: uint, character_1: uint):
    """Event 1044352740"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)


@RestartOnRest(1044350710)
def Event_1044350710(_, character: uint, character_1: uint):
    """Event 1044350710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3600):
        DisableFlag(1044359252)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L15, flag=3615)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    
    MAIN.Await(FlagEnabled(3615))
    
    Restart()

    # --- Label 15 --- #
    DefineLabel(15)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L5, flag=1044350715)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetCharacterTalkRange(character=character_1, distance=100.0)
    Goto(Label.L20)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character)
    EnableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L5, flag=1044350715)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character)
    EnableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3615))
    
    Restart()


@RestartOnRest(1044350711)
def Event_1044350711():
    """Event 1044350711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1044350800):
        return
    AND_1.Add(FlagEnabled(3605))
    AND_1.Add(FlagEnabled(1044352800))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1044352717)
    EnableFlag(3618)


@RestartOnRest(1044350712)
def Event_1044350712(_, character: uint):
    """Event 1044350712"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(1044352160))
    
    SetCharacterTalkRange(character=character, distance=100.0)
    EnableFlag(1044352715)


@RestartOnRest(1044350713)
def Event_1044350713():
    """Event 1044350713"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1044350800):
        return
    
    MAIN.Await(FlagEnabled(1044350800))
    
    if FlagDisabled(1044352160):
        return
    EnableFlag(1044349258)


@RestartOnRest(1044350714)
def Event_1044350714(_, character: uint):
    """Event 1044350714"""
    DisableCharacter(character)
    AND_1.Add(FlagDisabled(1044350800))
    AND_1.Add(FlagEnabled(3605))
    AND_1.Add(FlagEnabled(3600))
    if AND_1:
        return
    DisableBackread(character)
    End()


@RestartOnRest(1044350715)
def Event_1044350715(_, character: uint, character_1: uint):
    """Event 1044350715"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1044359260)
    AND_1.Add(FlagEnabled(3615))
    AND_1.Add(FlagEnabled(1044359260))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableThisSlotFlag()
    WaitFrames(frames=1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    SetCharacterTalkRange(character=character_1, distance=17.0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 20039)
    End()


@ContinueOnRest(1044353720)
def Event_1044353720(_, asset__character: uint):
    """Event 1044353720"""
    WaitFrames(frames=1)
    DisableFlag(1044359300)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3980))
    AND_1.Add(FlagEnabled(1044352720))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1044352720)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3980)
    GotoIfFlagEnabled(Label.L2, flag=3981)
    GotoIfFlagEnabled(Label.L4, flag=3983)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    ForceAnimation(asset__character, 30003)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    SetTeamType(asset__character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(asset__character)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableAsset(asset__character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(1044359300))
    
    Restart()

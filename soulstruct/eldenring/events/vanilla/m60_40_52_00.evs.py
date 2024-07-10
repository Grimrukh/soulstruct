"""
North Altus Plateau (SW) (SW)

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
from .enums.m60_40_52_00_enums import *
from .enums.m60_35_45_00_enums import Characters as m60_35_45_00_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76304, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76314,
        flag_1=76304,
        asset=Assets.AEG099_060_9001,
        source_flag=77310,
        value=0,
        flag_2=78310,
        flag_3=78311,
        flag_4=78312,
        flag_5=78313,
        flag_6=78314,
        flag_7=78315,
        flag_8=78316,
        flag_9=78317,
        flag_10=78318,
        flag_11=78319,
    )
    CommonFunc_90005870(0, character=Characters.BlackKnifeAssassin, name=902100600, npc_threat_level=14)
    CommonFunc_90005860(
        0,
        flag=1040520800,
        left=0,
        character=Characters.BlackKnifeAssassin,
        left_1=0,
        item_lot=30350,
        seconds=0.0,
    )
    Event_1040522240(0, asset=Assets.AEG099_070_9000, entity=Assets.AEG099_071_9000, flag=62030)
    AttachAssetToAsset(child_asset=1040521201, parent_asset=1040521200, parent_dummy_id=151)
    AttachAssetToAsset(child_asset=1040521211, parent_asset=1040521210, parent_dummy_id=151)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9006, dummy_id=100, vfx_id=800, right=1040528620)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=40,
        cc_id=55,
        dd_id=0,
        player_start=1040552650,
        unk_8_12=0,
        flag=1040552651,
        left_flag=1040552652,
        cancel_flag__right_flag=1040552653,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_1040523700(0, character=1040520700)
    Event_1040523701(0, attacked_entity=1040520700, flag=1040529205, flag_1=1040529206)
    Event_1040523702(0, entity=1040520700, attacked_entity=1040520710, flag=1040529206)
    Event_1040523703(0, character=1040520710)
    Event_1040523705(0, character=Characters.BrotherCorhyn)
    CommonFunc_90005704(0, attacked_entity=Characters.BrotherCorhyn, flag=4201, flag_1=4200, flag_2=1040529251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.BrotherCorhyn,
        flag=4201,
        flag_1=4202,
        flag_2=1040529251,
        flag_3=4201,
        first_flag=4200,
        last_flag=4203,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.BrotherCorhyn, flag=4203, first_flag=4200, last_flag=4204)
    CommonFunc_90005725(
        0,
        flag=4765,
        flag_1=4766,
        flag_2=4768,
        flag_3=1040529305,
        character=Characters.Merchant,
        character_1=m60_35_45_00_Characters.NomadMule,
        asset=1040526700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4766,
        flag_1=4767,
        flag_2=1035469206,
        flag_3=4766,
        first_flag=4765,
        last_flag=4769,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4766, flag_1=4765, flag_2=1035469206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4768, first_flag=4765, last_flag=4769)
    CommonFunc_90005705(0, character=Characters.FingerReader)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.BrotherCorhyn)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.FingerReader)
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier0,
        animation_id=30001,
        animation_id_1=20001,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellSoldier1,
        animation_id=30002,
        animation_id_1=20002,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.BlackKnifeAssassin,
        animation_id=30000,
        animation_id_1=20000,
        region=1040522800,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(1040522240)
def Event_1040522240(_, asset: Asset | int, entity: uint, flag: Flag | int):
    """Event 1040522240"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=803220)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1040523700)
def Event_1040523700(_, character: uint):
    """Event 1040523700"""
    WaitFrames(frames=1)
    DisableFlag(1040529200)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3620))
    AND_1.Add(FlagEnabled(1043379255))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(3630))
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    OR_2.Add(FlagEnabled(1040529205))
    OR_2.Add(FlagEnabled(1040529206))
    OR_2.Add(FlagEnabled(1040529207))
    SkipLinesIfConditionFalse(5, OR_2)
    EnableCharacter(character)
    EnableBackread(character)
    DisableAnimations(character)
    ForceAnimation(character, 90102)
    Goto(Label.L20)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101)
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
    
    MAIN.Await(FlagEnabled(1040529200))
    
    Restart()


@RestartOnRest(1040523701)
def Event_1040523701(_, attacked_entity: uint, flag: Flag | int, flag_1: Flag | int):
    """Event 1040523701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3620):
        return
    if FlagDisabled(3630):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    if OR_1:
        return
    
    MAIN.Await(OR_1)
    
    DisableAnimations(attacked_entity)
    if FlagEnabled(flag):
        return
    ForceAnimation(attacked_entity, 90201)
    if FlagEnabled(flag_1):
        return
    EnableFlag(1040529207)
    End()


@RestartOnRest(1040523702)
def Event_1040523702(_, entity: uint, attacked_entity: Character | int, flag: Flag | int):
    """Event 1040523702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3630):
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    EnableFlag(flag)
    DisableAnimations(entity)
    End()


@RestartOnRest(1040523703)
def Event_1040523703(_, character: uint):
    """Event 1040523703"""
    WaitFrames(frames=1)
    GotoIfFlagRangeAllDisabled(Label.L1, flag_range=(3620, 3624))
    GotoIfFlagRangeAnyEnabled(Label.L1, flag_range=(3625, 3629))
    GotoIfFlagEnabled(Label.L1, flag=3632)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    End()


@RestartOnRest(1040523705)
def Event_1040523705(_, character: uint):
    """Event 1040523705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4200):
        DisableFlag(1040529253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4206)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4206))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

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
    
    MAIN.Await(FlagDisabled(4206))
    
    Restart()

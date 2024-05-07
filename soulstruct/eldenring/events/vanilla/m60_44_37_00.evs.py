"""
East Limgrave (SW) (NW)

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
from .enums.m60_44_37_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044370000, asset=Assets.AEG099_060_9000)
    Event_1044372210(0, character=Characters.DemiHuman0, asset=1044371211, region=1044372210)
    Event_1044372210(1, character=Characters.DemiHuman1, asset=1044371212, region=1044372210)
    Event_1044372210(2, character=Characters.DemiHuman2, asset=1044371213, region=1044372210)
    Event_1044372210(3, character=Characters.DemiHuman3, asset=1044371214, region=1044372210)
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930023, left=0)
    Event_1044373715(0, character=1044370705)
    Event_1044373716()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble)
    DisableBackread(1044370705)
    Event_1044375220()
    CommonFunc_90005251(0, character=1044370203, radius=106.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.GodrickFootSoldier2,
        animation_id=30001,
        animation_id_1=20001,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Skeleton0, region=1044372200, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton0,
        animation_id=30014,
        animation_id_1=20014,
        region=1044372200,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005261(0, character=Characters.Skeleton1, region=1044372200, radius=10.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton1,
        animation_id=30014,
        animation_id_1=20014,
        region=1044372200,
        radius=10.0,
        seconds=1.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005261(0, character=Characters.Runebear, region=1044372350, radius=15.0, seconds=0.0, animation_id=0)


@RestartOnRest(1044372210)
def Event_1044372210(_, character: uint, asset: uint, region: uint):
    """Event 1044372210"""
    EnableAsset(asset)
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    AND_10.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableAsset(asset)
    End()
    EnableAsset(asset)
    DisableCharacter(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
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
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableAsset(asset)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1044375220)
def Event_1044375220():
    """Event 1044375220"""
    DropMandatoryTreasure(1044375220)


@RestartOnRest(1044372650)
def Event_1044372650(_, tutorial_param_id: int, flag: uint):
    """Event 1044372650"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)


@RestartOnRest(1044373700)
def Event_1044373700(
    _,
    asset__character: uint,
    asset__character_1: uint,
    asset__character_2: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044373700"""
    WaitFrames(frames=1)
    DisableFlag(flag)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(asset__character)
    EnableCharacter(asset__character_1)
    EnableAsset(asset__character_2)
    EnableBackread(asset__character)
    EnableBackread(asset__character_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DisableCharacter(asset__character)
    DisableCharacter(asset__character_1)
    DisableAsset(asset__character_2)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L2, flag=flag_2)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(asset__character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(asset__character)
    DropMandatoryTreasure(asset__character_1)
    DisableCharacter(asset__character)
    DisableCharacter(asset__character_1)
    DisableAsset(asset__character)
    DisableAsset(asset__character_1)
    DisableAsset(asset__character_2)
    DisableBackread(asset__character)
    DisableBackread(asset__character_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(flag))
    
    Restart()


@RestartOnRest(1044373701)
def Event_1044373701(_, flag: uint, flag_1: uint, flag_2: uint, first_flag: uint, last_flag: uint):
    """Event 1044373701"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagDisabled(flag_1):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
        EnableNetworkFlag(flag_2)
        EnableNetworkFlag(first_flag)
        End()
    if FlagEnabled(flag_2):
        return
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_2)


@RestartOnRest(1044373702)
def Event_1044373702(_, character: uint, flag: uint, first_flag: uint, flag_1: uint, last_flag: uint, flag_2: uint):
    """Event 1044373702"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(first_flag))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)


@RestartOnRest(1044373710)
def Event_1044373710(_, character: uint):
    """Event 1044373710"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30021)
    DisableGravity(character)


@RestartOnRest(1044373715)
def Event_1044373715(_, character: uint):
    """Event 1044373715"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(1044373716)
def Event_1044373716():
    """Event 1044373716"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3503):
        return
    AND_1.Add(FlagEnabled(3506))
    AND_1.Add(FlagDisabled(1044379256))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1044372700))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1044379255)
    End()

"""
Southeast Liurnia (NE) (NW)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_38_43_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038430000, asset=Assets.AEG099_060_9000)
    Event_1038432260(
        0,
        flag=1038430250,
        destination=Assets.AEG099_160_9000,
        character=Characters.Balloon,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1038432261(
        0,
        flag=1038430250,
        asset=Assets.AEG099_160_9000,
        character=Characters.Balloon,
        character_1=1038435260,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot_param_id=1038430100,
        flag_1=1038432250,
    )
    Event_1038432262(
        0,
        character=Characters.Balloon,
        seconds=0.0,
        attacked_entity=Characters.Balloon,
        seconds_1=0.0,
        character_1=Characters.Marionette0,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1038432250,
    )
    Event_1038432262(
        1,
        character=Characters.Balloon,
        seconds=0.0,
        attacked_entity=Characters.Balloon,
        seconds_1=0.0,
        character_1=Characters.Marionette1,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1038432250,
    )
    Event_1038432262(
        3,
        character=Characters.Balloon,
        seconds=0.0,
        attacked_entity=Characters.Balloon,
        seconds_1=0.0,
        character_1=Characters.Marionette2,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1038432250,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Hyetta, flag=3381, flag_1=3380, flag_2=1038439201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Hyetta,
        flag=3381,
        flag_1=3382,
        flag_2=1038439201,
        flag_3=3381,
        first_flag=3380,
        last_flag=3384,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Hyetta, flag=3383, first_flag=3380, last_flag=3384)
    Event_1038430700(0, character=Characters.Hyetta)
    Event_1038430701(0, 1038430700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Hyetta)
    CommonFunc_90005201(
        0,
        character=Characters.RayaLucariaFootSoldier,
        animation_id=30001,
        animation_id_1=20001,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038430702()


@RestartOnRest(1038432260)
def Event_1038432260(
    _,
    flag: uint,
    destination: uint,
    character: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    seconds_5: float,
    seconds_6: float,
):
    """Event 1038432260"""
    if FlagEnabled(flag):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    if AND_1:
        return
    ForceAnimation(destination, 0)
    Move(character, destination=destination, destination_type=CoordEntityType.Asset, model_point=220, short_move=True)
    Wait(5.400000095367432)
    Restart()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)
    Wait(seconds_5)
    Wait(seconds_6)


@RestartOnRest(1038432261)
def Event_1038432261(
    _,
    flag: uint,
    asset: uint,
    character: uint,
    character_1: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    item_lot_param_id: int,
    flag_1: uint,
):
    """Event 1038432261"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=200, model_point=803160)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    ForceAnimation(asset, 1)
    DeleteAssetVFX(asset)
    Wait(1.0)
    DisableAsset(asset)
    if PlayerInOwnWorld():
        Wait(0.30000001192092896)
        AwardItemLot(item_lot_param_id, host_only=True)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)


@RestartOnRest(1038432262)
def Event_1038432262(
    _,
    character: uint,
    seconds: float,
    attacked_entity: uint,
    seconds_1: float,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds_2: float,
    seconds_3: float,
    flag: uint,
):
    """Event 1038432262"""
    if FlagEnabled(character):
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character_1)
    ForceAnimation(character_1, animation_id)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=260))
    OR_2.Add(EntityWithinDistance(entity=character_1, other_entity=20000, radius=radius))
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
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character_1, state=True)
    Wait(seconds_2)
    ForceAnimation(character_1, animation_id_1)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_3)


@RestartOnRest(1038430700)
def Event_1038430700(_, character: uint):
    """Event 1038430700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3380):
        DisableFlag(1038439202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3389)
    GotoIfFlagEnabled(Label.L10, flag=3390)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3389, 3390)))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(3389, 3390)))
    
    Restart()


@RestartOnRest(1038430701)
def Event_1038430701(_, character: uint):
    """Event 1038430701"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(HealthRatio(character) <= 0.0)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1041389320, 1041389322)))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(1041389334)


@RestartOnRest(1038430702)
def Event_1038430702():
    """Event 1038430702"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1041389320, 1041389322)))
    AND_1.Add(FlagDisabled(1041382729))
    AND_1.Add(FlagDisabled(1038412709))
    
    MAIN.Await(AND_1)
    
    EnableFlag(3398)
    EnableFlag(1038432709)

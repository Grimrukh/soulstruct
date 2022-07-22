"""
East Limgrave (NW) (NE)

linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_45_39_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005616(0, flag=530170, region=1045392700)
    Event_1045392281(0, character=Characters.Wolf0, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(1, character=Characters.Wolf1, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(2, character=Characters.Wolf2, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(3, character=Characters.Wolf3, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(4, character=Characters.Wolf4, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(5, character=Characters.Wolf5, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(6, character=Characters.Wolf6, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(7, character=Characters.Wolf7, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392281(8, character=Characters.Wolf8, region=1045392280, owner_entity=Characters.Dummy)
    Event_1045392280(0, attacker__character=1045395280, region=1045392280)
    CommonFunc_90005620(
        0,
        flag=1045390570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=1045392570,
        cancel_flag__right_flag=1045392571,
        right=1045392572,
    )
    CommonFunc_90005621(0, flag=1045390570, asset=Assets.AEG099_272_9000)
    Event_1045392341(
        0,
        character=Characters.TibiaMariner,
        entity=1045393240,
        entity_1=1045393241,
        entity_2=1045393242,
        entity_3=1045393230,
        entity_4=1045393231,
        entity_5=1045393232,
        special_effect=15300,
        special_effect_1=15310,
        special_effect_2=15311,
        special_effect_3=15312,
    )
    Event_1045392342(
        0,
        character=Characters.TibiaMariner,
        flag=1045390800,
        special_effect=15302,
        destination=1045392343,
        first_flag=1045390350,
        special_effect_1=15310,
        special_effect_2=15311,
        special_effect_3=15312,
        destination_1=1045392343,
        destination_2=1045392344,
        destination_3=1045392345,
        last_flag=1045390351,
    )
    Event_1045392343(
        0,
        character=Characters.TibiaMariner,
        region=1045392340,
        region_1=1045392341,
        region_2=1045392342,
        special_effect_id=15310,
        special_effect_id_1=15311,
        special_effect_id_2=15312,
    )
    Event_1045392345(0, flag=1045390800, character=Characters.TibiaMariner, character_1=1045395230)
    Event_1045392346(0, character__targeting_character=Characters.TibiaMariner, region=1045392810)
    CommonFunc_90005870(0, character=Characters.TibiaMariner, name=904950600, npc_threat_level=24)
    CommonFunc_90005860(
        0,
        flag=1045390800,
        left=0,
        character=Characters.TibiaMariner,
        left_1=0,
        item_lot__item_lot_param_id=30170,
        seconds=0.0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.DHunteroftheDead,
        flag=4041,
        flag_1=4040,
        flag_2=1044399201,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.DHunteroftheDead,
        flag=4041,
        flag_1=4042,
        flag_2=1044399201,
        flag_3=4041,
        first_flag=4040,
        last_flag=4043,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.DHunteroftheDead, flag=4043, first_flag=4040, last_flag=4043)
    Event_1045390700(0, character=Characters.DHunteroftheDead)
    Event_1045390701()
    CommonFunc_90005775(0, 81463900, 1045399206, -1.0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.DHunteroftheDead)
    Event_1045392282()


@RestartOnRest(1045392280)
def Event_1045392280(_, attacker__character: uint, region: uint):
    """Event 1045392280"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5654)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1045392280):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5654)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=35000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=35000, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=35000, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1045392280)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5654)


@RestartOnRest(1045392281)
def Event_1045392281(_, character: uint, region: uint, owner_entity: uint):
    """Event 1045392281"""
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_11.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_11.Add(OR_7)
    GotoIfConditionTrue(Label.L0, input_condition=AND_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        model_point=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    ForceAnimation(character, 20011)
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    RemoveSpecialEffect(character, 8090)


@RestartOnRest(1045392282)
def Event_1045392282():
    """Event 1045392282"""
    DropMandatoryTreasure(1045395282)


@RestartOnRest(1045392341)
def Event_1045392341(
    _,
    character: uint,
    entity: uint,
    entity_1: uint,
    entity_2: uint,
    entity_3: uint,
    entity_4: uint,
    entity_5: uint,
    special_effect: int,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 1045392341"""
    GotoIfFlagDisabled(Label.L0, flag=1045390800)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(character))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=special_effect_1)
    EnableSpawner(entity=entity)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=special_effect_2)
    EnableSpawner(entity=entity_1)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=special_effect_3)
    EnableSpawner(entity=entity_2)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)
    Wait(1.0)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    Wait(1.0)
    Restart()


@RestartOnRest(1045392342)
def Event_1045392342(
    _,
    character: uint,
    flag: uint,
    special_effect: int,
    destination: uint,
    first_flag: uint,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    last_flag: uint,
):
    """Event 1045392342"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))
    
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect_1)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_2)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=special_effect_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(first_flag):
        Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
        Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagDisabled(first_flag):
        Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
        Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagDisabled(first_flag):
        Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
        Goto(Label.L0)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3022, loop=True)
    ReplanAI(character)
    Wait(5.0)
    Restart()


@RestartOnRest(1045392343)
def Event_1045392343(
    _,
    character: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    special_effect_id: int,
    special_effect_id_1: int,
    special_effect_id_2: int,
):
    """Event 1045392343"""
    if FlagEnabled(1045390800):
        return
    AND_2.Add(CharacterInsideRegion(character=character, region=region))
    OR_5.Add(AND_2)
    AND_3.Add(CharacterInsideRegion(character=character, region=region_1))
    OR_5.Add(AND_3)
    AND_4.Add(CharacterInsideRegion(character=character, region=region_2))
    OR_5.Add(AND_4)
    
    MAIN.Await(OR_5)
    
    GotoIfFinishedConditionFalse(Label.L2, input_condition=AND_2)
    AddSpecialEffect(character, special_effect_id)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFinishedConditionFalse(Label.L3, input_condition=AND_3)
    AddSpecialEffect(character, special_effect_id_1)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFinishedConditionFalse(Label.L4, input_condition=AND_4)
    AddSpecialEffect(character, special_effect_id_2)

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(1.0)
    Restart()


@RestartOnRest(1045392345)
def Event_1045392345(_, flag: uint, character: uint, character_1: uint):
    """Event 1045392345"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    MAIN.Await(MAIN)
    
    Kill(character_1)
    DisableSpawner(entity=1045393230)
    DisableSpawner(entity=1045393231)
    DisableSpawner(entity=1045393232)
    DisableSpawner(entity=1045393240)
    DisableSpawner(entity=1045393241)
    DisableSpawner(entity=1045393242)
    Wait(2.0)
    Kill(character_1)
    Wait(7.0)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()


@RestartOnRest(1045392346)
def Event_1045392346(_, character__targeting_character: uint, region: uint):
    """Event 1045392346"""
    DisableNetworkSync()
    if FlagEnabled(1045390800):
        return
    AND_1.Add(CharacterTargeting(targeting_character=character__targeting_character, targeted_character=20000))
    AND_1.Add(CharacterOutsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(character__targeting_character)
    Wait(5.0)
    Restart()


@RestartOnRest(1045390700)
def Event_1045390700(_, character: uint):
    """Event 1045390700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4040):
        DisableFlag(1044399202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4046)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4046))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L0, flag=4040)
    GotoIfFlagEnabled(Label.L1, flag=4041)
    GotoIfFlagEnabled(Label.L3, flag=4043)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90105)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4046))
    
    Restart()


@RestartOnRest(1045390701)
def Event_1045390701():
    """Event 1045390701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045390800):
        return
    
    MAIN.Await(FlagEnabled(1045390800))
    
    if FlagDisabled(4045):
        return
    EnableFlag(4058)

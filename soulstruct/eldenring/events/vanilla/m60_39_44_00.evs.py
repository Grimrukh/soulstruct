"""
East Liurnia (SE) (SE)

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
from .entities.m60_39_44_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1039440000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005261(0, character=Characters.Skeleton0, region=1039442200, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Skeleton1, region=1039442200, radius=5.0, seconds=1.5, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Skeleton2, region=1039442200, radius=5.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Skeleton3, region=1039442200, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005616(0, flag=530240, region=1039442710)
    CommonFunc_90005780(
        0,
        flag=1039440800,
        summon_flag=1039442160,
        dismissal_flag=1039442161,
        character=Characters.DHunteroftheDead,
        sign_type=20,
        region=1039442720,
        right=11109648,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=1039440800, flag_1=1039442160, flag_2=1039442161, character=Characters.DHunteroftheDead)
    CommonFunc_90005783(
        0,
        flag=1039440800,
        flag_1=1039442160,
        flag_2=1039442161,
        character=Characters.DHunteroftheDead,
        other_entity=1039442720,
        region=1039442160,
        left=0,
    )
    CommonFunc_90005703(
        0,
        character=Characters.LivingPot0,
        flag=3661,
        flag_1=3662,
        flag_2=1043399301,
        flag_3=1043399314,
        first_flag=3660,
        last_flag=3663,
        right=-1,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.LivingPot0,
        flag=1043399314,
        flag_1=3660,
        flag_2=1043399301,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.LivingPot0, flag=3663, first_flag=3660, last_flag=3663)
    Event_1039443700(0, character=Characters.LivingPot0)
    Event_1039443701()
    Event_1039443702()
    Event_1039443705()
    Event_1039443706()
    Event_1039443707()
    Event_1039443720(0, character=Characters.SmallLivingPot0, character_1=Characters.SmallLivingPot8)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot0,
        flag=3821,
        flag_1=3820,
        flag_2=1039449251,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot0,
        flag=3821,
        flag_1=3822,
        flag_2=1039449251,
        flag_3=3821,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot8,
        flag=3821,
        flag_1=3820,
        flag_2=1039449251,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot8,
        flag=3821,
        flag_1=3822,
        flag_2=1039449251,
        flag_3=3821,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443721(0, character=Characters.SmallLivingPot1)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot1,
        flag=3821,
        flag_1=3820,
        flag_2=1039449251,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot1,
        flag=3821,
        flag_1=3822,
        flag_2=1039449251,
        flag_3=3821,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443722(0, character=Characters.SmallLivingPot7)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot7,
        flag=3821,
        flag_1=3820,
        flag_2=1039449251,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot7,
        flag=3821,
        flag_1=3822,
        flag_2=1039449251,
        flag_3=3821,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443724(0, character=Characters.SmallLivingPot0)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot0, model_point=905, vfx_id=603000)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot0, model_point=200, vfx_id=603051)
    Event_1039443725(0, character=Characters.SmallLivingPot1)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot1, model_point=905, vfx_id=603000)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot1, model_point=200, vfx_id=603051)
    Event_1039443726(0, character=Characters.SmallLivingPot7)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot7, model_point=905, vfx_id=603000)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot7, model_point=200, vfx_id=603051)
    Event_1039443732(0, character=Characters.SmallLivingPot8)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot8, model_point=905, vfx_id=603000)
    CommonFunc_90005709(0, attacked_entity=Characters.SmallLivingPot8, model_point=200, vfx_id=603051)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9005,
        action_button_id=4110,
        item_lot_param_id=104600,
        first_flag=400460,
        last_flag=400460,
        flag=3829,
        model_point=0,
    )
    Event_1039443727()
    Event_1039443728(
        0,
        asset=Assets.AEG110_450_1000,
        asset_1=Assets.AEG110_451_1000,
        asset_2=Assets.AEG110_452_1000,
        asset_3=Assets.AEG110_453_1000,
    )
    Event_1039443740(0, character=Characters.LivingPot1)
    CommonFunc_90005702(
        0,
        character=Characters.LivingPot1,
        flag=1039440736,
        first_flag=1039440735,
        last_flag=1039440736,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.LivingPot1,
        flag=1039449284,
        flag_1=3820,
        flag_2=1039449294,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.LivingPot1,
        flag=3821,
        flag_1=3822,
        flag_2=1039449294,
        flag_3=1039449284,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443741(0, character=Characters.LivingPot2)
    CommonFunc_90005702(
        0,
        character=Characters.LivingPot2,
        flag=1039440738,
        first_flag=1039440737,
        last_flag=1039440738,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.LivingPot2,
        flag=1039449284,
        flag_1=3820,
        flag_2=1039449294,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.LivingPot2,
        flag=3821,
        flag_1=3822,
        flag_2=1039449294,
        flag_3=1039449284,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443742(0, character=Characters.SmallLivingPot2)
    CommonFunc_90005702(
        0,
        character=Characters.SmallLivingPot2,
        flag=1039440746,
        first_flag=1039440745,
        last_flag=1039440746,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot2,
        flag=1039449284,
        flag_1=3820,
        flag_2=1039449294,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot2,
        flag=3821,
        flag_1=3822,
        flag_2=1039449294,
        flag_3=1039449284,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443743(0, character=Characters.SmallLivingPot3)
    CommonFunc_90005702(
        0,
        character=Characters.SmallLivingPot3,
        flag=1039440748,
        first_flag=1039440747,
        last_flag=1039440748,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot3,
        flag=1039449284,
        flag_1=3820,
        flag_2=1039449294,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot3,
        flag=3821,
        flag_1=3822,
        flag_2=1039449294,
        flag_3=1039449284,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443744(0, character=Characters.SmallLivingPot4)
    CommonFunc_90005702(
        0,
        character=Characters.SmallLivingPot4,
        flag=1039440750,
        first_flag=1039440749,
        last_flag=1039440750,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot4,
        flag=1039449284,
        flag_1=3820,
        flag_2=1039449294,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot4,
        flag=3821,
        flag_1=3822,
        flag_2=1039449294,
        flag_3=1039449284,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443745(0, character=Characters.SmallLivingPot5)
    CommonFunc_90005702(
        0,
        character=Characters.SmallLivingPot5,
        flag=1039440752,
        first_flag=1039440751,
        last_flag=1039440752,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot5,
        flag=1039449284,
        flag_1=3820,
        flag_2=1039449294,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot5,
        flag=3821,
        flag_1=3822,
        flag_2=1039449294,
        flag_3=1039449284,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443746(0, character=Characters.SmallLivingPot6)
    CommonFunc_90005702(
        0,
        character=Characters.SmallLivingPot6,
        flag=1039440754,
        first_flag=1039440753,
        last_flag=1039440754,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SmallLivingPot6,
        flag=1039449284,
        flag_1=3820,
        flag_2=1039449294,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SmallLivingPot6,
        flag=3821,
        flag_1=3822,
        flag_2=1039449294,
        flag_3=1039449284,
        first_flag=3820,
        last_flag=3823,
        right=-1,
    )
    Event_1039443729()
    Event_1039443730()
    Event_1039443731()
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.KnightDiallos0,
        flag=3441,
        flag_1=3440,
        flag_2=1039449301,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.KnightDiallos0,
        flag=3441,
        flag_1=3442,
        flag_2=1039449301,
        flag_3=3441,
        first_flag=3440,
        last_flag=3444,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.KnightDiallos0, flag=3443, first_flag=3440, last_flag=3444)
    CommonFunc_90005702(0, character=Characters.KnightDiallos1, flag=3443, first_flag=3440, last_flag=3444)
    Event_1039443710(0, character=Characters.KnightDiallos0)
    Event_1039443711(0, character=Characters.KnightDiallos1)
    Event_1039443712(0, attacked_entity=Characters.KnightDiallos1, flag=1039449315)
    Event_1039443713()
    Event_1039442341(
        0,
        character=Characters.TibiaMariner,
        entity=1039443240,
        entity_1=1039443241,
        entity_2=1039443242,
        entity_3=1039443230,
        entity_4=1039443231,
        entity_5=1039443232,
        special_effect=15300,
        special_effect_1=15310,
        special_effect_2=15311,
        special_effect_3=15312,
    )
    Event_1039442342(
        0,
        character=Characters.TibiaMariner,
        flag=1039440800,
        special_effect=15302,
        destination=1039442803,
        first_flag=1039440350,
        special_effect_1=15310,
        special_effect_2=15311,
        special_effect_3=15312,
        destination_1=1039442803,
        destination_2=1039442804,
        destination_3=1039442805,
        last_flag=1039440351,
    )
    Event_1039442343(
        0,
        character=Characters.TibiaMariner,
        region=1039442800,
        region_1=1039442801,
        region_2=1039442802,
        special_effect_id=15310,
        special_effect_id_1=15311,
        special_effect_id_2=15312,
    )
    Event_1039442344(0, flag=1039440800, character=Characters.TibiaMariner, character_1=1039445250)
    Event_1039442345(0, character__targeting_character=Characters.TibiaMariner, region=1039442810)
    CommonFunc_90005870(0, character=Characters.TibiaMariner, name=904950601, npc_threat_level=24)
    CommonFunc_90005860(0, 1039440800, 0, 1039440800, 0, 30240, 0.0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.SmallLivingPot0)
    DisableBackread(Characters.SmallLivingPot1)
    DisableBackread(Characters.KnightDiallos0)
    DisableBackread(Characters.KnightDiallos1)
    DisableBackread(1039440720)


@RestartOnRest(1039442341)
def Event_1039442341(
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
    """Event 1039442341"""
    GotoIfFlagDisabled(Label.L0, flag=1039440800)
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


@RestartOnRest(1039442342)
def Event_1039442342(
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
    """Event 1039442342"""
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


@RestartOnRest(1039442343)
def Event_1039442343(
    _,
    character: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    special_effect_id: int,
    special_effect_id_1: int,
    special_effect_id_2: int,
):
    """Event 1039442343"""
    if FlagEnabled(1039440800):
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


@RestartOnRest(1039442344)
def Event_1039442344(_, flag: uint, character: uint, character_1: uint):
    """Event 1039442344"""
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
    DisableSpawner(entity=1039443240)
    DisableSpawner(entity=1039443241)
    DisableSpawner(entity=1039443242)
    DisableSpawner(entity=1039443230)
    DisableSpawner(entity=1039443231)
    DisableSpawner(entity=1039443232)
    Wait(2.0)
    Kill(character_1)
    Wait(7.0)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()


@RestartOnRest(1039442345)
def Event_1039442345(_, character__targeting_character: uint, region: uint):
    """Event 1039442345"""
    DisableNetworkSync()
    if FlagEnabled(character__targeting_character):
        return
    AND_1.Add(CharacterTargeting(targeting_character=character__targeting_character, targeted_character=20000))
    AND_1.Add(CharacterOutsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(character__targeting_character)
    Wait(5.0)
    Restart()


@RestartOnRest(1039443700)
def Event_1039443700(_, character: uint):
    """Event 1039443700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3669)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3669))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    if FlagEnabled(1039449214):
        Move(character, destination=1039442705, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
    if FlagDisabled(1039449214):
        ForceAnimation(character, 930018)
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
    
    MAIN.Await(FlagDisabled(3669))
    
    Restart()


@RestartOnRest(1039443701)
def Event_1039443701():
    """Event 1039443701"""
    WaitFrames(frames=1)
    if FlagDisabled(3660):
        return
    EnableImmortality(Characters.LivingPot0)
    DisableHealthBar(Characters.LivingPot0)
    AwaitFlagEnabled(flag=1039449214)
    DisableImmortality(Characters.LivingPot0)
    EnableHealthBar(Characters.LivingPot0)
    End()


@RestartOnRest(1039443702)
def Event_1039443702():
    """Event 1039443702"""
    if PlayerNotInOwnWorld():
        return
    AwaitFlagEnabled(flag=3669)
    DisableNetworkFlag(1039442702)
    DisableNetworkFlag(1039442703)
    AND_1.Add(FlagEnabled(3669))
    AND_1.Add(FlagDisabled(1039449206))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.LivingPot0, radius=70.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1039442702)
    Wait(20.0)
    Restart()


@RestartOnRest(1039443705)
def Event_1039443705():
    """Event 1039443705"""
    if FlagEnabled(1039449214):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.LivingPot0, 420))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039449207)
    End()


@RestartOnRest(1039443706)
def Event_1039443706():
    """Event 1039443706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1039449214):
        return
    EnableFlag(1043399314)
    
    MAIN.Await(FlagEnabled(1039449214))
    
    DisableFlag(1043399314)
    End()


@RestartOnRest(1039443707)
def Event_1039443707():
    """Event 1039443707"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3669):
        return
    AwaitFlagEnabled(flag=1035539204)
    EnableNetworkFlag(3678)
    End()


@RestartOnRest(1039443710)
def Event_1039443710(_, character: uint):
    """Event 1039443710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3440))
    AND_1.Add(FlagEnabled(11109405))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(3450))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3450))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90102)
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
    OR_15.Add(FlagEnabled(3450))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1039443711)
def Event_1039443711(_, character: uint):
    """Event 1039443711"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3440))
    AND_1.Add(FlagEnabled(11109405))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(Assets.AEG099_403_9000)
    OR_1.Add(FlagEnabled(3451))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3451))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    EnableAsset(Assets.AEG099_403_9000)
    DisableHealthBar(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90103)
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
    if FlagDisabled(1039449316):
        EnableCharacter(character)
        EnableBackread(character)
        EnableAsset(Assets.AEG099_403_9000)
        ForceAnimation(character, 90104)
        DisableAnimations(character)
        Goto(Label.L20)
    DisableCharacter(character)
    DisableBackread(character)
    EnableAsset(Assets.AEG099_403_9000)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3451))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1039443712)
def Event_1039443712(_, attacked_entity: uint, flag: uint):
    """Event 1039443712"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3451):
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    AwaitConditionTrue(OR_1)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3443)
    SaveRequest()
    DisableAnimations(attacked_entity)
    ForceAnimation(attacked_entity, 90200)
    End()


@RestartOnRest(1039443713)
def Event_1039443713():
    """Event 1039443713"""
    if FlagEnabled(3443):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(Characters.KnightDiallos0) == 0)
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(Characters.KnightDiallos0, True)
    AND_2.Add(TimeElapsed(seconds=10.0))
    
    MAIN.Await(AND_2)
    
    SetBackreadStateAlternate(Characters.KnightDiallos0, False)
    End()


@RestartOnRest(1039443720)
def Event_1039443720(_, character: uint, character_1: uint):
    """Event 1039443720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_10.Add(FlagEnabled(3820))
    AND_10.Add(FlagEnabled(1039449253))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1039449253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    OR_1.Add(FlagEnabled(3825))
    OR_1.Add(FlagEnabled(3826))
    AND_1.Add(FlagEnabled(3828))
    AND_1.Add(FlagEnabled(1039449296))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3825))
    OR_2.Add(FlagEnabled(3826))
    AND_2.Add(FlagEnabled(3828))
    AND_2.Add(FlagEnabled(1039449296))
    OR_2.Add(AND_2)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3820)
    GotoIfFlagEnabled(Label.L2, flag=3821)
    GotoIfFlagEnabled(Label.L3, flag=3822)
    GotoIfFlagEnabled(Label.L4, flag=3823)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(1039442715):
        EnableCharacter(character)
        EnableBackread(character)
        ForceAnimation(character, 930011)
        Move(character, destination=1039442700, destination_type=CoordEntityType.Region, short_move=True)
        EnableImmortality(character)
    if FlagEnabled(1039442715):
        EnableCharacter(character_1)
        EnableBackread(character_1)
        ForceAnimation(character_1, 930024)
        EnableImmortality(character_1)
        EnableNetworkFlag(1039442716)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagDisabled(3825))
    AND_15.Add(FlagDisabled(3826))
    AND_15.Add(FlagDisabled(3828))
    OR_15.Add(AND_15)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039442715))
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(1039443721)
def Event_1039443721(_, character: uint):
    """Event 1039443721"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_10.Add(FlagEnabled(3820))
    AND_10.Add(FlagEnabled(1039449253))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1039449253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(3827))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3827))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3820)
    GotoIfFlagEnabled(Label.L2, flag=3821)
    GotoIfFlagEnabled(Label.L3, flag=3822)
    GotoIfFlagEnabled(Label.L4, flag=3823)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930012)
    EnableImmortality(character)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagDisabled(3827))
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1039443722)
def Event_1039443722(_, character: uint):
    """Event 1039443722"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_10.Add(FlagEnabled(3820))
    AND_10.Add(FlagEnabled(1039449253))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1039449253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(3828))
    AND_1.Add(FlagDisabled(1039449296))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    AND_2.Add(FlagEnabled(3828))
    AND_2.Add(FlagDisabled(1039449296))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3820)
    GotoIfFlagEnabled(Label.L2, flag=3821)
    GotoIfFlagEnabled(Label.L3, flag=3822)
    GotoIfFlagEnabled(Label.L4, flag=3823)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930014)
    EnableImmortality(character)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagDisabled(3828))
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1039443724)
def Event_1039443724(_, character: uint):
    """Event 1039443724"""
    if FlagEnabled(3821):
        return
    if FlagEnabled(3822):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3821, 3822)))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20027)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443725)
def Event_1039443725(_, character: uint):
    """Event 1039443725"""
    if FlagEnabled(3821):
        return
    if FlagEnabled(3822):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3821, 3822)))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20030)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443726)
def Event_1039443726(_, character: uint):
    """Event 1039443726"""
    if FlagEnabled(3821):
        return
    if FlagEnabled(3822):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3821, 3822)))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20033)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443727)
def Event_1039443727():
    """Event 1039443727"""
    WaitFrames(frames=1)
    if FlagDisabled(3450):
        return
    if FlagDisabled(3440):
        return
    if FlagDisabled(3820):
        return
    if FlagEnabled(1039449278):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(1039449274):
        EnableNetworkFlag(1039449274)
        End()
    if FlagDisabled(1039449275):
        EnableNetworkFlag(1039449275)
        End()
    if FlagDisabled(1039449276):
        EnableNetworkFlag(1039449276)
        End()
    if FlagDisabled(1039449277):
        EnableNetworkFlag(1039449277)
        End()
    if FlagDisabled(1039449278):
        EnableNetworkFlag(1039449278)
        End()
    End()


@RestartOnRest(1039443728)
def Event_1039443728(_, asset: uint, asset_1: uint, asset_2: uint, asset_3: uint):
    """Event 1039443728"""
    WaitFrames(frames=1)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableAsset(asset_2)
    DisableAsset(asset_3)
    OR_1.Add(FlagEnabled(3827))
    OR_1.Add(FlagEnabled(3828))
    AND_1.Add(FlagEnabled(3829))
    AND_1.Add(FlagEnabled(1039449270))
    OR_1.Add(AND_1)
    if not OR_1:
        return
    EnableAsset(asset)
    EnableAsset(asset_1)
    EnableAsset(asset_2)
    EnableAsset(asset_3)
    AND_5.Add(FlagEnabled(1039440736))
    SkipLinesIfConditionFalse(1, AND_5)
    DisableAsset(asset)
    AND_5.Add(FlagEnabled(1039440746))
    SkipLinesIfConditionFalse(1, AND_5)
    DisableAsset(asset_2)
    AND_6.Add(FlagEnabled(1039440738))
    SkipLinesIfConditionFalse(1, AND_6)
    DisableAsset(asset_1)
    AND_7.Add(FlagEnabled(1039440748))
    AND_7.Add(FlagEnabled(1039440750))
    AND_7.Add(FlagEnabled(1039440752))
    SkipLinesIfConditionFalse(1, AND_7)
    DisableAsset(asset_3)
    DisableCharacter(Characters.LivingPot1)
    DisableBackread(Characters.LivingPot1)
    DisableCharacter(Characters.LivingPot2)
    DisableBackread(Characters.LivingPot2)
    DisableCharacter(Characters.SmallLivingPot2)
    DisableBackread(Characters.SmallLivingPot2)
    DisableCharacter(Characters.SmallLivingPot3)
    DisableBackread(Characters.SmallLivingPot3)
    DisableCharacter(Characters.SmallLivingPot4)
    DisableBackread(Characters.SmallLivingPot4)
    DisableCharacter(Characters.SmallLivingPot5)
    DisableBackread(Characters.SmallLivingPot5)
    DisableCharacter(Characters.SmallLivingPot6)
    DisableBackread(Characters.SmallLivingPot6)
    End()


@RestartOnRest(1039443729)
def Event_1039443729():
    """Event 1039443729"""
    if PlayerNotInOwnWorld():
        return
    WaitFramesAfterCutscene(frames=1)
    OR_1.Add(FlagEnabled(3822))
    OR_1.Add(FlagEnabled(3442))
    if OR_1:
        return
    OR_15.Add(FlagEnabled(3821))
    AND_1.Add(FlagEnabled(3441))
    AND_1.Add(FlagEnabled(3450))
    OR_15.Add(AND_1)
    if FlagDisabled(1039440736):
        OR_2.Add(FlagEnabled(1039440736))
    if FlagDisabled(1039440738):
        OR_2.Add(FlagEnabled(1039440738))
    if FlagDisabled(1039440746):
        OR_2.Add(FlagEnabled(1039440746))
    if FlagDisabled(1039440748):
        OR_2.Add(FlagEnabled(1039440748))
    if FlagDisabled(1039440750):
        OR_2.Add(FlagEnabled(1039440750))
    if FlagDisabled(1039440752):
        OR_2.Add(FlagEnabled(1039440752))
    if FlagDisabled(1039440754):
        OR_2.Add(FlagEnabled(1039440754))
    OR_15.Add(OR_2)
    AwaitConditionTrue(OR_15)
    EnableNetworkFlag(1039449251)
    if FlagEnabled(3450):
        EnableNetworkFlag(1039449301)
    AddSpecialEffect(Characters.LivingPot1, 15220)
    AddSpecialEffect(Characters.LivingPot2, 15220)
    AddSpecialEffect(Characters.SmallLivingPot2, 15220)
    AddSpecialEffect(Characters.SmallLivingPot3, 15220)
    AddSpecialEffect(Characters.SmallLivingPot4, 15220)
    AddSpecialEffect(Characters.SmallLivingPot5, 15220)
    AddSpecialEffect(Characters.SmallLivingPot6, 15220)
    End()


@RestartOnRest(1039443730)
def Event_1039443730():
    """Event 1039443730"""
    if PlayerNotInOwnWorld():
        return
    WaitFramesAfterCutscene(frames=1)
    AND_15.Add(FlagEnabled(3822))
    AND_15.Add(FlagEnabled(3442))
    if AND_15:
        return
    AND_1.Add(FlagEnabled(3443))
    AND_1.Add(FlagEnabled(3450))
    OR_15.Add(AND_1)
    AND_2.Add(FlagEnabled(1039440736))
    AND_2.Add(FlagEnabled(1039440738))
    AND_2.Add(FlagEnabled(1039440746))
    AND_2.Add(FlagEnabled(1039440748))
    AND_2.Add(FlagEnabled(1039440750))
    AND_2.Add(FlagEnabled(1039440752))
    AND_2.Add(FlagEnabled(1039440754))
    OR_15.Add(AND_2)
    AwaitConditionTrue(OR_15)
    DisableNetworkConnectedFlagRange(flag_range=(3820, 3823))
    EnableNetworkFlag(3822)
    AND_5.Add(FlagEnabled(3450))
    AND_5.Add(FlagDisabled(3443))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3443))
    EnableNetworkFlag(3442)
    AddSpecialEffect(Characters.LivingPot1, 15220)
    AddSpecialEffect(Characters.LivingPot2, 15220)
    AddSpecialEffect(Characters.SmallLivingPot2, 15220)
    AddSpecialEffect(Characters.SmallLivingPot3, 15220)
    AddSpecialEffect(Characters.SmallLivingPot4, 15220)
    AddSpecialEffect(Characters.SmallLivingPot5, 15220)
    AddSpecialEffect(Characters.SmallLivingPot6, 15220)
    End()


@RestartOnRest(1039443731)
def Event_1039443731():
    """Event 1039443731"""
    WaitFramesAfterCutscene(frames=1)
    if PlayerNotInOwnWorld():
        return
    OR_14.Add(FlagEnabled(3825))
    OR_14.Add(FlagEnabled(3826))
    OR_14.Add(FlagEnabled(3828))
    AwaitConditionTrue(OR_14)
    if FlagEnabled(1039449289):
        return
    DisableNetworkConnectedFlagRange(flag_range=(1039442730, 1039442739))
    DisableNetworkFlag(1039442715)
    GotoIfFlagEnabled(Label.L1, flag=3825)
    GotoIfFlagEnabled(Label.L2, flag=3826)
    GotoIfFlagEnabled(Label.L3, flag=3828)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L20, flag=1039449258)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(FlagEnabled(1039449261))
    AND_2.Add(FlagDisabled(11109430))
    OR_2.Add(AND_2)
    AND_3.Add(FlagEnabled(1039449261))
    AND_3.Add(FlagDisabled(3443))
    AND_3.Add(FlagDisabled(3063))
    AND_3.Add(FlagDisabled(11109430))
    OR_2.Add(AND_3)
    AND_4.Add(FlagEnabled(1039449263))
    AND_4.Add(FlagEnabled(11109430))
    AND_4.Add(FlagDisabled(3450))
    OR_2.Add(AND_4)
    AND_5.Add(FlagEnabled(1039449263))
    AND_5.Add(FlagEnabled(3443))
    AND_5.Add(FlagEnabled(3063))
    AND_5.Add(FlagDisabled(3450))
    OR_2.Add(AND_5)
    AND_6.Add(FlagEnabled(1039449266))
    AND_6.Add(FlagEnabled(3450))
    OR_2.Add(AND_6)
    GotoIfConditionTrue(Label.L20, input_condition=OR_2)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L20, flag=1039449282)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    EnableRandomFlagInRange(flag_range=(1039442730, 1039442739))
    SkipLinesIfFlagRangeAllDisabled(1, (1039442730, 1039442732))
    EnableNetworkFlag(1039442715)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3825))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3826))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3828))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3450))
    if OR_15:
        return RESTART


@RestartOnRest(1039443732)
def Event_1039443732(_, character: uint):
    """Event 1039443732"""
    if FlagEnabled(3821):
        return
    if FlagEnabled(3822):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3821, 3822)))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20030)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443740)
def Event_1039443740(_, character: uint):
    """Event 1039443740"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440735, 1039440736))
    DisableNetworkConnectedFlagRange(flag_range=(1039440735, 1039440736))
    EnableNetworkFlag(1039440735)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440735)
    GotoIfFlagEnabled(Label.L4, flag=1039440736)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443741)
def Event_1039443741(_, character: uint):
    """Event 1039443741"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440737, 1039440738))
    DisableNetworkConnectedFlagRange(flag_range=(1039440737, 1039440738))
    EnableNetworkFlag(1039440737)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440737)
    GotoIfFlagEnabled(Label.L4, flag=1039440738)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443742)
def Event_1039443742(_, character: uint):
    """Event 1039443742"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440745, 1039440746))
    DisableNetworkConnectedFlagRange(flag_range=(1039440745, 1039440746))
    EnableNetworkFlag(1039440745)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440745)
    GotoIfFlagEnabled(Label.L4, flag=1039440746)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30022)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443743)
def Event_1039443743(_, character: uint):
    """Event 1039443743"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440747, 1039440748))
    DisableNetworkConnectedFlagRange(flag_range=(1039440747, 1039440748))
    EnableNetworkFlag(1039440747)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440747)
    GotoIfFlagEnabled(Label.L4, flag=1039440748)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30024)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443744)
def Event_1039443744(_, character: uint):
    """Event 1039443744"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440749, 1039440750))
    DisableNetworkConnectedFlagRange(flag_range=(1039440749, 1039440750))
    EnableNetworkFlag(1039440749)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440749)
    GotoIfFlagEnabled(Label.L4, flag=1039440750)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30022)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443745)
def Event_1039443745(_, character: uint):
    """Event 1039443745"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440751, 1039440752))
    DisableNetworkConnectedFlagRange(flag_range=(1039440751, 1039440752))
    EnableNetworkFlag(1039440751)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440751)
    GotoIfFlagEnabled(Label.L4, flag=1039440752)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30022)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443746)
def Event_1039443746(_, character: uint):
    """Event 1039443746"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440753, 1039440754))
    DisableNetworkConnectedFlagRange(flag_range=(1039440753, 1039440754))
    EnableNetworkFlag(1039440753)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440753)
    GotoIfFlagEnabled(Label.L4, flag=1039440754)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30025)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()

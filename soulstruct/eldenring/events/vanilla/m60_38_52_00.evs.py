"""
West Altus Plateau (SE) (SW)

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
from .enums.m60_38_52_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005620(
        0,
        flag=1038520570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=1038522570,
        cancel_flag__right_flag=1038522571,
        right=1038522572,
    )
    CommonFunc_90005621(0, flag=1038520570, asset=Assets.AEG099_272_9000)
    CommonFunc_90005261(
        0,
        character=Characters.TibiaMariner,
        region=1038522300,
        radius=30.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        1,
        character=Characters.GiantSkeletonTorso,
        region=1038522300,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_1038522350()
    Event_1038522347(
        0,
        character__targeting_character=Characters.TibiaMariner,
        region=1038522400,
        flag=1038520800,
        character=Characters.GiantSkeletonTorso,
    )
    Event_1038522347(
        1,
        character__targeting_character=Characters.GiantSkeletonTorso,
        region=1038522400,
        flag=1038520800,
        character=Characters.TibiaMariner,
    )
    CommonFunc_90005870(0, character=Characters.TibiaMariner, name=904950602, npc_threat_level=24)
    CommonFunc_90005860(
        0,
        flag=1038520800,
        left=0,
        character=Characters.TibiaMariner,
        left_1=0,
        item_lot=30385,
        seconds=0.0,
    )
    Event_1038522339(0, character=Characters.TibiaMariner, character_1=Characters.GiantSkeletonTorso)
    Event_1038522349()
    CommonFunc_90005616(0, flag=530385, region=1038522700)
    Event_1038522346(
        0,
        character=Characters.TibiaMariner,
        flag=1038520800,
        special_effect=15302,
        destination=1038522320,
        flag_1=1038522340,
        special_effect_1=15310,
        special_effect_2=15311,
        special_effect_3=15312,
        destination_1=1038522343,
        destination_2=1038522344,
        destination_3=1038522345,
    )
    Event_1038522343(0, character=Characters.TibiaMariner, region=1038522340, special_effect=15310)
    Event_1038522343(1, character=Characters.TibiaMariner, region=1038522341, special_effect=15311)
    Event_1038522343(2, character=Characters.TibiaMariner, region=1038522342, special_effect=15312)
    Event_1038522344(
        0,
        flag=1038520800,
        character=Characters.TibiaMariner,
        character_1=1038525230,
        character_2=Characters.GiantSkeletonTorso,
    )
    Event_1038522345(
        0,
        character=Characters.TibiaMariner,
        character_1=Characters.GiantSkeletonTorso,
        special_effect=15335,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton0,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522200,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton1,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522200,
        radius=10.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton2,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522205,
        radius=10.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton3,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522205,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton4,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522210,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton5,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522215,
        radius=10.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton6,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522215,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton7,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522220,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton8,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522221,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton9,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522221,
        radius=10.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton10,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522225,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton11,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522225,
        radius=10.0,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton12,
        region=1038522250,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton13,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522250,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton14,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522255,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton15,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522255,
        radius=10.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        2,
        character=Characters.Skeleton16,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522255,
        radius=10.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton17,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522260,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton18,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522265,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        3,
        character=Characters.Skeleton19,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522265,
        radius=5.0,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        4,
        character=Characters.Skeleton20,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522265,
        radius=5.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton21,
        animation_id=30016,
        animation_id_1=20016,
        region=1038522270,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton22,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522280,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton23,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522280,
        radius=10.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        2,
        character=Characters.Skeleton24,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522280,
        radius=10.0,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton25,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522285,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton26,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522285,
        radius=10.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        2,
        character=Characters.Skeleton27,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522285,
        radius=10.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton28,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522290,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton29,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522295,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        1,
        character=Characters.Skeleton30,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522295,
        radius=10.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        2,
        character=Characters.Skeleton31,
        animation_id=30014,
        animation_id_1=20014,
        region=1038522295,
        radius=10.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=1038528600)
    CommonFunc_90005683(0, flag=62314, asset=Assets.AEG099_055_1001, vfx_id=211, flag_1=78392, flag_2=78392)


@RestartOnRest(1038522339)
def Event_1038522339(_, character: uint, character_1: uint):
    """Event 1038522339"""
    if FlagEnabled(1038520800):
        return
    SetCharacterEventTarget(character, entity=character_1)
    SetCharacterEventTarget(character_1, entity=character)
    AND_1.Add(CharacterDead(character_1))
    AwaitConditionTrue(AND_1)
    Wait(5.0)
    AND_2.Add(CharacterAlive(character_1))
    AwaitConditionTrue(AND_2)
    Restart()


@RestartOnRest(1038522341)
def Event_1038522341(
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
    """Event 1038522341"""
    AND_15.Add(CharacterDead(Characters.TibiaMariner))
    if AND_15:
        return
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    Kill(1038525230)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1038522230)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    Kill(1038525230)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L1, character=character, special_effect=special_effect_1)
    EnableSpawner(entity=entity)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L2, character=character, special_effect=special_effect_2)
    EnableSpawner(entity=entity_1)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L3, character=character, special_effect=special_effect_3)
    EnableSpawner(entity=entity_2)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(5.0)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    EnableFlag(1038522230)
    Restart()


@RestartOnRest(1038522342)
def Event_1038522342(
    _,
    character: uint,
    special_effect: int,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 1038522342"""
    if FlagEnabled(1038520800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))
    
    DisableCharacter(character)
    DisableAnimations(character)
    DisableFlag(1038520340)
    EnableRandomFlagInRange(flag_range=(1038520340, 1038520341))
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(10, character=character, special_effect=special_effect_1)
    SkipLinesIfFlagEnabled(4, 1038520340)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLines(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 3022, loop=True)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(10, character=character, special_effect=special_effect_2)
    SkipLinesIfFlagEnabled(4, 1038520341)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLines(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 3022, loop=True)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(10, character=character, special_effect=special_effect_3)
    SkipLinesIfFlagEnabled(4, 1038520340)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLines(3)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 3022, loop=True)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(1038522343)
def Event_1038522343(_, character: uint, region: uint, special_effect: int):
    """Event 1038522343"""
    if FlagEnabled(1038520800):
        return
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect, target_count=0.0))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect)
    Restart()


@RestartOnRest(1038522344)
def Event_1038522344(_, flag: uint, character: uint, character_1: uint, character_2: uint):
    """Event 1038522344"""
    if FlagEnabled(flag):
        DisableSpawner(entity=1038523350)
        DisableCharacter(character_1)
        DisableAnimations(character_1)
        Kill(character_1)
        DisableCharacter(character_2)
        DisableAnimations(character_2)
        Kill(character_2)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    MAIN.Await(MAIN)
    
    EnableNetworkFlag(flag)
    DisableSpawner(entity=1038522230)
    DisableSpawner(entity=1038522231)
    DisableSpawner(entity=1038522232)
    DisableSpawner(entity=1038522240)
    DisableSpawner(entity=1038522241)
    DisableSpawner(entity=1038522242)
    DisableSpawner(entity=1038523350)
    Kill(character_1)
    Wait(15.0)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    Kill(character_2)
    End()


@RestartOnRest(1038522345)
def Event_1038522345(_, character: uint, character_1: uint, special_effect: int):
    """Event 1038522345"""
    MAIN.Await(HealthValue(character) == 0)
    
    AND_1.Add(CharacterHasSpecialEffect(character_1, special_effect))
    
    MAIN.Await(AND_1)
    
    Kill(character_1, award_runes=True)
    End()


@RestartOnRest(1038522346)
def Event_1038522346(
    _,
    character: uint,
    flag: uint,
    special_effect: int,
    destination: uint,
    flag_1: uint,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
):
    """Event 1038522346"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))
    
    AND_1.Add(HealthRatio(character) <= 0.5)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableNetworkFlag(flag_1)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect_1)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_2)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=special_effect_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(flag_1):
        Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
        Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagDisabled(flag_1):
        Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
        Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3022, loop=True)
    ReplanAI(character)
    Wait(5.0)
    Restart()


@RestartOnRest(1038522347)
def Event_1038522347(_, character__targeting_character: uint, region: uint, flag: uint, character: uint):
    """Event 1038522347"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterTargeting(targeting_character=character__targeting_character, targeted_character=20000))
    AND_1.Add(CharacterOutsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(character__targeting_character)
    Wait(1.0)
    SetCharacterEventTarget(character__targeting_character, entity=character)
    SetCharacterEventTarget(character, entity=character__targeting_character)
    Wait(5.0)
    Restart()


@EndOnRest(1038522349)
def Event_1038522349():
    """Event 1038522349"""
    DisableFlag(1038520340)
    DisableFlag(1038520341)
    DisableFlag(1038520343)
    End()


@RestartOnRest(1038522350)
def Event_1038522350():
    """Event 1038522350"""
    AddSpecialEffect(Characters.TibiaMariner, 8092)
    End()

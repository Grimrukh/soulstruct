"""
Southwest Mountaintops (SE) (NE)

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
from .entities.m60_51_53_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1051530000, asset=Assets.AEG099_060_9000)
    Event_1051532200(0, character=1051535200)
    Event_1051532390()
    CommonFunc_90005200(
        0,
        character=1051530321,
        animation_id=30005,
        animation_id_1=20005,
        region=1051532321,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MassiveFingercreeper0,
        animation_id=30006,
        animation_id_1=20006,
        region=1051532322,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MassiveFingercreeper1,
        animation_id=30006,
        animation_id_1=20006,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MassiveFingercreeper2,
        animation_id=30006,
        animation_id_1=20006,
        region=0,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(
        0,
        flag=1051530210,
        character=Characters.ExtraLargeScarab,
        item_lot=1051530700,
        seconds=0.0,
        left=0,
    )
    Event_1051532220(
        0,
        character=Characters.ExtraLargeScarab,
        special_effect=12603,
        region=1051532210,
        region_1=1051532211,
        region_2=1051532212,
    )
    CommonFunc_90005201(
        0,
        character=Characters.ExtraLargeScarab,
        animation_id=30000,
        animation_id_1=20000,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(
        0,
        flag=1051530380,
        character=Characters.BloodyFingerOkina,
        item_lot=0,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=1051530180,
        summon_flag=1051532181,
        dismissal_flag=1051532182,
        character=Characters.BloodyFingerOkina,
        sign_type=21,
        region=1051532180,
        region_1=1051532181,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(
        0,
        flag=1051530180,
        flag_1=1051532181,
        flag_2=1051532182,
        character=Characters.BloodyFingerOkina,
    )
    CommonFunc_90005792(
        0,
        flag=1051530180,
        flag_1=1051532181,
        flag_2=1051532182,
        character=Characters.BloodyFingerOkina,
        item_lot=1051530500,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1051530180,
        flag_1=1051532181,
        flag_2=1051532182,
        character=Characters.BloodyFingerOkina,
        other_entity=1051532180,
        region=1051532182,
        left=0,
    )
    Event_1051532330(0, attacker__character=1051535330, region=1051532330)
    Event_1051532330(1, attacker__character=1051535331, region=1051532331)
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper1,
        animation_id=30000,
        animation_id_1=20000,
        region=1051532284,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Fingercreeper0,
        region=1051532283,
        radius=0.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005771(0, 1051530950, 1051532700)


@RestartOnRest(1051532200)
def Event_1051532200(_, character: uint):
    """Event 1051532200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@ContinueOnRest(1051532220)
def Event_1051532220(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1051532220"""
    if FlagEnabled(1051530210):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(1051530210))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlag(1051532221)
    DisableFlag(1051532222)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1051532221, 1051532222))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1051532221)
    SkipLines(4)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    SetNest(character, region=region_1)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    SetNest(character, region=region_2)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1051532221)
    SkipLines(4)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    SetNest(character, region=region)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    SetNest(character, region=region_2)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1051532221)
    SkipLines(4)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    SetNest(character, region=region)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    SetNest(character, region=region_1)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(1051532330)
def Event_1051532330(_, attacker__character: uint, region: uint):
    """Event 1051532330"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5651)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1051532330):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5651)
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
    
    EnableNetworkFlag(1050562200)
    RemoveSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 4802)
    RemoveSpecialEffect(attacker__character, 5651)


@RestartOnRest(1051532390)
def Event_1051532390():
    """Event 1051532390"""
    AddSpecialEffect(Characters.MonstrousCrow, 12019)
    AND_1.Add(CharacterHasSpecialEffect(Characters.MonstrousCrow, 12019))
    AND_1.Add(CharacterHasSpecialEffect(Characters.MonstrousCrow, 12018))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Characters.MonstrousCrow, 20020)
    End()

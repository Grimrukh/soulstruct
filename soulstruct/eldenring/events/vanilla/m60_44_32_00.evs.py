"""
East Weeping Peninsula (SW) (SW)

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
from .enums.m60_44_32_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1044322200(
        0,
        character=Characters.Scarab,
        special_effect=12603,
        region=1044322200,
        region_1=1044322201,
        region_2=1044322202,
    )
    CommonFunc_90005300(0, flag=1044320200, character=Characters.Scarab, item_lot=40138, seconds=0.0, left=0)
    CommonFunc_90005860(
        0,
        flag=1044320800,
        left=0,
        character=Characters.DeathRiteBird,
        left_1=0,
        item_lot=1044320400,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.DeathRiteBird, name=904980602, npc_threat_level=24)
    CommonFunc_90005300(0, flag=1044320850, character=Characters.NightsCavalryHorse, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005476(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    RunCommonEvent(90005477)
    Event_1044322340(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    CommonFunc_90005860(
        0,
        flag=1044320850,
        left=0,
        character=Characters.NightsCavalry,
        left_1=0,
        item_lot=1044320410,
        seconds=0.0,
    )
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry,
        name=903150601,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse,
    )
    CommonFunc_90005872(0, character=Characters.NightsCavalry, npc_threat_level=10, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005211(
        0,
        character=Characters.DeathRiteBird,
        animation_id=30000,
        animation_id_1=20000,
        region=1044322340,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@ContinueOnRest(1044322200)
def Event_1044322200(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1044322200"""
    if FlagEnabled(1044320200):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(1044320200))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlag(1044322201)
    DisableFlag(1044322202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1044322201, 1044322202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1044322201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1044322201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1044322201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(1044322210)
def Event_1044322210(_, asset: Asset | int, entity: uint, flag: Flag | int):
    """Event 1044322210"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1044322340)
def Event_1044322340(_, character: Character | int, character_1: Character | int):
    """Event 1044322340"""
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


@RestartOnRest(1044322600)
def Event_1044322600():
    """Event 1044322600"""
    DisableAsset(1044321600)
    DisableAsset(1044321601)
    DisableAsset(1044321602)
    DisableAsset(1044321603)
    DisableAsset(1044321604)

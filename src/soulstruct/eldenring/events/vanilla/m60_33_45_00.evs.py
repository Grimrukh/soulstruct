"""
West Liurnia (SW) (NE)

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
from .enums.m60_33_45_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005880(
        0,
        flag=1033450800,
        flag_1=1033450805,
        flag_2=1033452800,
        character=Characters.LiurniaTroll,
        item_lot=30250,
        area_id=60,
        block_id=33,
        cc_id=45,
        dd_id=0,
        player_start=1033452805,
    )
    CommonFunc_90005881(
        0,
        flag=1033450800,
        flag_1=1033450805,
        left_flag=1033452801,
        cancel_flag__right_flag=1033452802,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=33,
        cc_id=45,
        dd_id=0,
        player_start=1033452805,
    )
    CommonFunc_90005882(
        0,
        flag=1033450800,
        flag_1=1033450805,
        flag_2=1033452800,
        character=Characters.LiurniaTroll,
        flag_3=1033452806,
        character_1=1033455810,
        asset=Assets.AEG099_120_1000,
        owner_entity=Characters.TalkDummy,
        source_entity=1033452810,
        name=904600520,
        animation_id=-1,
        animation_id_1=20005,
    )
    CommonFunc_90005883(0, flag=1033450800, flag_1=1033450805, entity=Assets.AEG099_170_1000)
    CommonFunc_90005885(
        0,
        flag=1033450800,
        bgm_boss_conv_param_id=0,
        flag_1=1033452806,
        flag_2=1033452807,
        left=0,
        left_1=1,
    )
    Event_1033452200(
        0,
        character=Characters.Scarab,
        special_effect=12603,
        region=1033452200,
        region_1=1033452201,
        region_2=1033452202,
    )
    CommonFunc_90005300(0, flag=1033450200, character=Characters.Scarab, item_lot=40264, seconds=0.0, left=0)


@RestartOnRest(1033452360)
def Event_1033452360():
    """Event 1033452360"""
    AND_1.Add(FlagEnabled(1033452800))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    DisableCharacter(1033455800)
    DisableAnimations(1033455800)
    AND_1.Add(FlagEnabled(1033450800))
    
    MAIN.Await(AND_1)
    
    Wait(7.0)
    EnableCharacter(1033455800)
    EnableAnimations(1033455800)


@ContinueOnRest(1033452200)
def Event_1033452200(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1033452200"""
    if FlagEnabled(1233450200):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(1233450200))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlag(1033452201)
    DisableFlag(1033452202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1033452201, 1033452202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1033452201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1033452201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1033452201)
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

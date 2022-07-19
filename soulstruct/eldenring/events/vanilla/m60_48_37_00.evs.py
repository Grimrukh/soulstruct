"""
South Caelid (SW) (NW)

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
from .entities.m60_48_37_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1048370000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76458,
        flag_1=76405,
        asset=Assets.AEG099_090_9000,
        source_flag=77410,
        value=0,
        flag_2=78410,
        flag_3=78411,
        flag_4=78412,
        flag_5=78413,
        flag_6=78414,
        flag_7=78415,
        flag_8=78416,
        flag_9=78417,
        flag_10=78418,
        flag_11=78419,
    )
    CommonFunc_90005201(
        0,
        character=Characters.DecayingEkzykes,
        animation_id=30000,
        animation_id_1=20000,
        radius=50.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=Characters.DecayingEkzykes, name=904501600, npc_threat_level=25)
    CommonFunc_90005861(
        0,
        flag=1048370800,
        left=0,
        character=Characters.DecayingEkzykes,
        left_1=1,
        item_lot__item_lot_param_id=30400,
        text=30064,
        seconds=0.0,
    )
    Event_1048372200(
        0,
        character=Characters.Scarab,
        special_effect=12603,
        region=1048372299,
        region_1=1048372298,
        region_2=1048372297,
    )
    CommonFunc_90005300(0, 1048370299, 1048370299, 40406, 0.0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048370700)


@NeverRestart(1048372200)
def Event_1048372200(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1048372200"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    AND_2.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    DisableFlag(1048372201)
    DisableFlag(1048372202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1048372201, 1048372202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1048372201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1048372201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1048372201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()

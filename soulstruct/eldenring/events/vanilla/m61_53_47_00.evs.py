"""
Land of Shadow 13-11 NW NE

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_2053472400()
    Event_2053472403()
    CommonFunc_90005200(
        0,
        character=2053470210,
        animation_id=30002,
        animation_id_1=20002,
        region=2053472210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2053470211,
        animation_id=30002,
        animation_id_1=20002,
        region=2053472210,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2053470212,
        animation_id=30002,
        animation_id_1=20002,
        region=2053472210,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2053470213,
        animation_id=30002,
        animation_id_1=20002,
        region=2053472210,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2053470214,
        animation_id=30002,
        animation_id_1=20002,
        region=2053472210,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2053470215,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2053470216,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2053470217,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=2053470204, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2053470207, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2053470218, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)


@RestartOnRest(2053472400)
def Event_2053472400():
    """Event 2053472400"""
    if CharacterDoesNotHaveSpecialEffect(character=2053475200, special_effect=20011076):
        return
    AND_1.Add(FlagEnabled(2053472301))
    
    MAIN.Await(AND_1)
    
    AND_4.Add(CharacterBackreadEnabled(2053470200))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(2053470200, 20011075))
    AND_4.Add(CharacterAlive(2053470200))
    SkipLinesIfConditionTrue(1, AND_4)
    SkipLines(3)
    EnableFlag(2053472200)
    DisableFlag(2053472301)
    Goto(Label.L0)
    AND_2.Add(CharacterBackreadEnabled(2053470201))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(2053470201, 20011075))
    AND_2.Add(CharacterAlive(2053470201))
    SkipLinesIfConditionTrue(1, AND_2)
    SkipLines(3)
    EnableFlag(2053472201)
    DisableFlag(2053472301)
    Goto(Label.L0)
    AND_3.Add(CharacterBackreadEnabled(2053470202))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(2053470202, 20011075))
    AND_3.Add(CharacterAlive(2053470202))
    SkipLinesIfConditionTrue(1, AND_3)
    SkipLines(3)
    EnableFlag(2053472202)
    DisableFlag(2053472301)
    Goto(Label.L0)
    AND_6.Add(CharacterBackreadEnabled(2053470205))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(2053470205, 20011075))
    AND_6.Add(CharacterAlive(2053470205))
    SkipLinesIfConditionTrue(1, AND_6)
    SkipLines(3)
    EnableFlag(2053472205)
    DisableFlag(2053472301)
    Goto(Label.L0)
    AND_7.Add(CharacterBackreadEnabled(2053470206))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(2053470206, 20011075))
    AND_7.Add(CharacterAlive(2053470206))
    SkipLinesIfConditionTrue(1, AND_7)
    SkipLines(3)
    EnableFlag(2053472206)
    DisableFlag(2053472301)
    Goto(Label.L0)
    AND_9.Add(CharacterBackreadEnabled(2053470208))
    AND_9.Add(CharacterDoesNotHaveSpecialEffect(2053470208, 20011075))
    AND_9.Add(CharacterAlive(2053470208))
    SkipLinesIfConditionTrue(1, AND_9)
    SkipLines(3)
    EnableFlag(2053472208)
    DisableFlag(2053472301)
    Goto(Label.L0)
    WaitRealFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(2053472403)
def Event_2053472403():
    """Event 2053472403"""
    AND_13.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053470200, radius=25.0))
    AND_13.Add(CharacterAlive(2053470200))
    AND_13.Add(HasAIStatus(2053470200, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_13)
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053470201, radius=25.0))
    AND_15.Add(CharacterAlive(2053470201))
    AND_15.Add(HasAIStatus(2053470201, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_15)
    AND_14.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053470202, radius=25.0))
    AND_14.Add(CharacterAlive(2053470202))
    AND_14.Add(HasAIStatus(2053470202, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_14)
    AND_11.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053470205, radius=25.0))
    AND_11.Add(CharacterAlive(2053470205))
    AND_11.Add(HasAIStatus(2053470205, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_11)
    AND_10.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053470206, radius=25.0))
    AND_10.Add(CharacterAlive(2053470206))
    AND_10.Add(HasAIStatus(2053470206, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_10)
    AND_8.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053470208, radius=25.0))
    AND_8.Add(CharacterAlive(2053470208))
    AND_8.Add(HasAIStatus(2053470208, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_8)
    SkipLinesIfConditionTrue(1, OR_1)
    EnableFlag(2053472303)
    SkipLinesIfConditionFalse(1, OR_1)
    DisableFlag(2053472303)
    Wait(1.0)
    Restart()

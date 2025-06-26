"""
Land of Shadow 12-09 NE NW

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
    CommonFunc_90005261(0, character=2050390200, region=2050392200, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2050390205, region=2050392200, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2050390206, region=2050392200, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2050390207, region=2050392200, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2050390208, region=2050392200, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2050390209, region=2050392200, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2050390210, region=2050392200, radius=1.0, seconds=0.0, animation_id=0)
    Event_2050392400()
    Event_2050392401()
    Event_2050392405()
    Event_2050392404()


@RestartOnRest(2050392400)
def Event_2050392400():
    """Event 2050392400"""
    if CharacterDoesNotHaveSpecialEffect(character=2050395200, special_effect=20011076):
        return
    AND_1.Add(FlagEnabled(2050392301))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterBackreadEnabled(2050390205))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(2050390205, 20011075))
    AND_2.Add(CharacterAlive(2050390205))
    SkipLinesIfConditionTrue(1, AND_2)
    SkipLines(3)
    EnableFlag(2050392205)
    DisableFlag(2050392301)
    Goto(Label.L0)
    AND_3.Add(CharacterBackreadEnabled(2050390206))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(2050390206, 20011075))
    AND_3.Add(CharacterAlive(2050390206))
    SkipLinesIfConditionTrue(1, AND_3)
    SkipLines(3)
    EnableFlag(2050392206)
    DisableFlag(2050392301)
    Goto(Label.L0)
    AND_4.Add(CharacterBackreadEnabled(2050390207))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(2050390207, 20011075))
    AND_4.Add(CharacterAlive(2050390207))
    SkipLinesIfConditionTrue(1, AND_4)
    SkipLines(3)
    EnableFlag(2050392207)
    DisableFlag(2050392301)
    Goto(Label.L0)
    AND_5.Add(CharacterBackreadEnabled(2050390208))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(2050390208, 20011075))
    AND_5.Add(CharacterAlive(2050390208))
    SkipLinesIfConditionTrue(1, AND_5)
    SkipLines(3)
    EnableFlag(2050392208)
    DisableFlag(2050392301)
    Goto(Label.L0)
    EnableFlag(2050392301)
    DisableFlag(2050392301)
    WaitRealFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(2050392401)
def Event_2050392401():
    """Event 2050392401"""
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 20011090))
    OR_1.Add(FlagDisabled(2050392303))
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(2050392301)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 20011090))
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(2050392404)
def Event_2050392404():
    """Event 2050392404"""
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=2050390205, radius=25.0))
    AND_15.Add(CharacterAlive(2050390205))
    AND_15.Add(HasAIStatus(2050390205, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_15)
    AND_14.Add(EntityWithinDistance(entity=PLAYER, other_entity=2050390206, radius=25.0))
    AND_14.Add(CharacterAlive(2050390206))
    AND_14.Add(HasAIStatus(2050390206, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_14)
    AND_13.Add(EntityWithinDistance(entity=PLAYER, other_entity=2050390207, radius=25.0))
    AND_13.Add(CharacterAlive(2050390207))
    AND_13.Add(HasAIStatus(2050390207, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_13)
    AND_12.Add(EntityWithinDistance(entity=PLAYER, other_entity=2050390208, radius=25.0))
    AND_12.Add(CharacterAlive(2050390208))
    AND_12.Add(HasAIStatus(2050390208, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_12)
    SkipLinesIfConditionTrue(1, OR_1)
    EnableFlag(2050392303)
    SkipLinesIfConditionFalse(1, OR_1)
    DisableFlag(2050392303)
    Wait(0.5)
    Restart()


@RestartOnRest(2050392405)
def Event_2050392405():
    """Event 2050392405"""
    OR_1.Add(FlagEnabled(2050392205))
    OR_1.Add(FlagEnabled(2050392206))
    OR_1.Add(FlagEnabled(2050392207))
    OR_1.Add(FlagEnabled(2050392208))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(2050392205):
        SetNetworkUpdateAuthority(2050390205, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2050390205, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2050390205, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2050392206):
        SetNetworkUpdateAuthority(2050390206, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2050390206, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2050390206, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2050392207):
        SetNetworkUpdateAuthority(2050390207, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2050390207, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2050390207, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2050392208):
        SetNetworkUpdateAuthority(2050390208, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2050390208, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2050390208, 20011073)
        Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.20000000298023224)
    SetNetworkUpdateRate(2050390205, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2050390206, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2050390207, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2050390208, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateAuthority(2050390205, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2050390206, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2050390207, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2050390208, authority_level=UpdateAuthority.Normal)
    DisableFlag(2050392205)
    DisableFlag(2050392206)
    DisableFlag(2050392207)
    DisableFlag(2050392208)
    Restart()

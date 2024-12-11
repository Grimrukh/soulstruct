"""
Land of Shadow 13-11 NW SE

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
    Event_2053462400()
    Event_2053462401()
    Event_2053462405()
    Event_2053462404()
    CommonFunc_90005201(
        0,
        character=2053460209,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_2053462600()


@RestartOnRest(2053462400)
def Event_2053462400():
    """Event 2053462400"""
    if CharacterDoesNotHaveSpecialEffect(character=2053465200, special_effect=20011076):
        return
    AND_1.Add(FlagEnabled(2053462301))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterBackreadEnabled(2053460201))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(2053460201, 20011075))
    AND_2.Add(CharacterAlive(2053460201))
    SkipLinesIfConditionTrue(1, AND_2)
    SkipLines(3)
    EnableFlag(2053462201)
    DisableFlag(2053462301)
    Goto(Label.L0)
    AND_3.Add(CharacterBackreadEnabled(2053460202))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(2053460202, 20011075))
    AND_3.Add(CharacterAlive(2053460202))
    SkipLinesIfConditionTrue(1, AND_3)
    SkipLines(3)
    EnableFlag(2053462202)
    DisableFlag(2053462301)
    Goto(Label.L0)
    AND_4.Add(CharacterBackreadEnabled(2053460203))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(2053460203, 20011075))
    AND_4.Add(CharacterAlive(2053460203))
    SkipLinesIfConditionTrue(1, AND_4)
    SkipLines(3)
    EnableFlag(2053462203)
    DisableFlag(2053462301)
    Goto(Label.L0)
    AND_5.Add(CharacterBackreadEnabled(2053460204))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(2053460204, 20011075))
    AND_5.Add(CharacterAlive(2053460204))
    SkipLinesIfConditionTrue(1, AND_5)
    SkipLines(3)
    EnableFlag(2053462204)
    DisableFlag(2053462301)
    Goto(Label.L0)
    AND_6.Add(CharacterBackreadEnabled(2053460205))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(2053460205, 20011075))
    AND_6.Add(CharacterAlive(2053460205))
    SkipLinesIfConditionTrue(1, AND_6)
    SkipLines(3)
    EnableFlag(2053462205)
    DisableFlag(2053462301)
    Goto(Label.L0)
    AND_7.Add(CharacterBackreadEnabled(2053460206))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(2053460206, 20011075))
    AND_7.Add(CharacterAlive(2053460206))
    SkipLinesIfConditionTrue(1, AND_7)
    SkipLines(3)
    EnableFlag(2053462206)
    DisableFlag(2053462301)
    Goto(Label.L0)
    AND_8.Add(CharacterBackreadEnabled(2053460207))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(2053460207, 20011075))
    AND_8.Add(CharacterAlive(2053460207))
    SkipLinesIfConditionTrue(1, AND_8)
    SkipLines(3)
    EnableFlag(2053462207)
    DisableFlag(2053462301)
    Goto(Label.L0)
    AND_9.Add(CharacterBackreadEnabled(2053460208))
    AND_9.Add(CharacterDoesNotHaveSpecialEffect(2053460208, 20011075))
    AND_9.Add(CharacterAlive(2053460208))
    SkipLinesIfConditionTrue(1, AND_9)
    SkipLines(3)
    EnableFlag(2053462208)
    DisableFlag(2053462301)
    Goto(Label.L0)
    EnableFlag(2053472301)
    DisableFlag(2053462301)
    WaitRealFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(2053462401)
def Event_2053462401():
    """Event 2053462401"""
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 20011090))
    OR_1.Add(FlagDisabled(2053462303))
    OR_1.Add(FlagDisabled(2053472303))
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(2053462301)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 20011090))
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(2053462404)
def Event_2053462404():
    """Event 2053462404"""
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460201, radius=25.0))
    AND_15.Add(CharacterAlive(2053460201))
    AND_15.Add(HasAIStatus(2053460201, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_15)
    AND_14.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460202, radius=25.0))
    AND_14.Add(CharacterAlive(2053460202))
    AND_14.Add(HasAIStatus(2053460202, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_14)
    AND_13.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460203, radius=25.0))
    AND_13.Add(CharacterAlive(2053460203))
    AND_13.Add(HasAIStatus(2053460203, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_13)
    AND_12.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460204, radius=25.0))
    AND_12.Add(CharacterAlive(2053460204))
    AND_12.Add(HasAIStatus(2053460204, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_12)
    AND_11.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460205, radius=25.0))
    AND_11.Add(CharacterAlive(2053460205))
    AND_11.Add(HasAIStatus(2053460205, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_11)
    AND_10.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460206, radius=25.0))
    AND_10.Add(CharacterAlive(2053460206))
    AND_10.Add(HasAIStatus(2053460206, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_10)
    AND_9.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460207, radius=25.0))
    AND_9.Add(CharacterAlive(2053460207))
    AND_9.Add(HasAIStatus(2053460207, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_9)
    AND_8.Add(EntityWithinDistance(entity=PLAYER, other_entity=2053460208, radius=25.0))
    AND_8.Add(CharacterAlive(2053460208))
    AND_8.Add(HasAIStatus(2053460208, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_8)
    SkipLinesIfConditionTrue(1, OR_1)
    EnableFlag(2053462303)
    SkipLinesIfConditionFalse(1, OR_1)
    DisableFlag(2053462303)
    Wait(1.0)
    Restart()


@RestartOnRest(2053462405)
def Event_2053462405():
    """Event 2053462405"""
    OR_1.Add(FlagEnabled(2053472200))
    OR_1.Add(FlagEnabled(2053472201))
    OR_1.Add(FlagEnabled(2053472202))
    OR_1.Add(FlagEnabled(2053472205))
    OR_1.Add(FlagEnabled(2053472206))
    OR_1.Add(FlagEnabled(2053472208))
    OR_1.Add(FlagEnabled(2053462201))
    OR_1.Add(FlagEnabled(2053462202))
    OR_1.Add(FlagEnabled(2053462203))
    OR_1.Add(FlagEnabled(2053462204))
    OR_1.Add(FlagEnabled(2053462205))
    OR_1.Add(FlagEnabled(2053462206))
    OR_1.Add(FlagEnabled(2053462207))
    OR_1.Add(FlagEnabled(2053462208))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(2053472200):
        SetNetworkUpdateAuthority(2053470200, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053470200, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053470200, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053472201):
        SetNetworkUpdateAuthority(2053470201, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053470201, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053470201, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053472202):
        SetNetworkUpdateAuthority(2053470202, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053470202, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053470202, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053472205):
        SetNetworkUpdateAuthority(2053470205, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053470205, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053470205, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053472206):
        SetNetworkUpdateAuthority(2053470206, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053470206, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053470206, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053472208):
        SetNetworkUpdateAuthority(2053470208, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053470208, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053470208, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462201):
        SetNetworkUpdateAuthority(2053460201, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460201, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460201, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462202):
        SetNetworkUpdateAuthority(2053460202, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460202, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460202, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462203):
        SetNetworkUpdateAuthority(2053460203, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460203, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460203, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462204):
        SetNetworkUpdateAuthority(2053460204, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460204, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460204, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462205):
        SetNetworkUpdateAuthority(2053460205, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460205, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460205, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462206):
        SetNetworkUpdateAuthority(2053460206, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460206, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460206, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462207):
        SetNetworkUpdateAuthority(2053460207, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460207, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460207, 20011073)
        Goto(Label.L0)
    if FlagEnabled(2053462208):
        SetNetworkUpdateAuthority(2053460208, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(2053460208, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        AddSpecialEffect(2053460208, 20011073)
        Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.20000000298023224)
    SetNetworkUpdateRate(2053470200, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053470201, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053470202, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053470205, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053470206, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053470208, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460201, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460202, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460203, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460204, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460205, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460206, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460207, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2053460208, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateAuthority(2053470200, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053470201, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053470202, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053470205, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053470206, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053470208, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460201, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460202, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460203, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460204, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460205, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460206, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460207, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateAuthority(2053460208, authority_level=UpdateAuthority.Normal)
    DisableFlag(2053472200)
    DisableFlag(2053472201)
    DisableFlag(2053472202)
    DisableFlag(2053472205)
    DisableFlag(2053472206)
    DisableFlag(2053472208)
    DisableFlag(2053462201)
    DisableFlag(2053462202)
    DisableFlag(2053462203)
    DisableFlag(2053462204)
    DisableFlag(2053462205)
    DisableFlag(2053462206)
    DisableFlag(2053462207)
    DisableFlag(2053462208)
    Restart()


@ContinueOnRest(2053462600)
def Event_2053462600():
    """Event 2053462600"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2053460600):
        DisableAssetActivation(2053461600, obj_act_id=52407)
        Wait(1.0)
        AwardItemLot(2053460600, host_only=True)
        End()
    AND_10.Add(PlayerDoesNotHaveGood(2008008))
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(2008008))
    AND_1.Add(AssetActivated(obj_act_id=2053463600))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(2053460600)
    Wait(10.0)
    AwardItemLot(2053460600, host_only=True)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableAssetActivation(2053461600, obj_act_id=52407)
    
    MAIN.Await(PlayerHasGood(2008008))
    
    EnableAssetActivation(2053461600, obj_act_id=52407)
    Wait(0.10000000149011612)
    Restart()

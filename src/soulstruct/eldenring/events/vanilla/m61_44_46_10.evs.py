"""
Land of Shadow 11-11 (Alternate) NW SW

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
    RegisterGrace(grace_flag=76943, asset=2044461950)
    CommonFunc_90005102(
        0,
        flag=76945,
        flag_1=76943,
        asset=2044461980,
        source_flag=77900,
        value=5,
        flag_2=78900,
        flag_3=78901,
        flag_4=78902,
        flag_5=78903,
        flag_6=78904,
        flag_7=78905,
        flag_8=78906,
        flag_9=78907,
        flag_10=78908,
        flag_11=78909,
        flag_12=9146,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=2044460180,
        summon_flag=2044462181,
        dismissal_flag=2044462182,
        character=2044460700,
        sign_type=23,
        region=2044462700,
        region_1=2044462701,
        seconds=0.0,
        right_1=21019216,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2044460180, flag_1=2044462181, flag_2=2044462182, character=2044460700)
    CommonFunc_90005792(
        0,
        flag=2044460180,
        flag_1=2044462181,
        flag_2=2044462182,
        character=2044460700,
        item_lot=0,
        seconds=0.0,
    )
    Event_2044462550(
        0,
        flag=2044460180,
        flag_1=2044462181,
        flag_2=2044462182,
        character=2044460700,
        other_entity=2044462700,
        region=2044462182,
        left=0,
        region_1=2044462400,
    )
    CommonFunc_90005780(
        0,
        flag=2044450800,
        summon_flag=2044462164,
        dismissal_flag=2044462165,
        character=2044460730,
        sign_type=0,
        region=2044462731,
        right=2049449213,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=2044450800, flag_1=2044462164, flag_2=2044462165, character=2044460730)
    CommonFunc_90005784(
        0,
        flag=2044462164,
        flag_1=2044452805,
        character=2044460730,
        region=2044452800,
        region_1=2044462809,
        animation=0,
    )
    CommonFunc_90005785(
        0,
        flag=2044450800,
        flag_1=2044462164,
        flag_2=2044462165,
        character=2044460730,
        other_entity=2044462730,
        region=2044462300,
        radius=0.0,
    )
    CommonFunc_90005250(0, character=2044460200, region=2044462200, seconds=0.0, animation_id=3005)
    CommonFunc_90005501(
        0,
        flag=2044460510,
        flag_1=2044460511,
        left=0,
        asset=2044461510,
        asset_1=2044461511,
        asset_2=2044461512,
        flag_2=2044460512,
    )
    Event_2044462510()
    CommonFunc_90005638(0, flag=2044460500, asset=2044461500, asset_1=2044461501)
    CommonFunc_90005774(0, flag=2044460180, item_lot=116100, flag_1=400614)
    CommonFunc_90005706(0, character=2044460710, animation_id=30011, left=0)
    Event_2044460706(0, flag=2049449213, flag_1=2044450800)


@ContinueOnRest(2044460050)
def Event_2044460050():
    """Event 2044460050"""
    if ThisEventSlotFlagEnabled():
        return


@ContinueOnRest(2044462510)
def Event_2044462510():
    """Event 2044462510"""
    CommonFunc_90005500(
        0,
        flag=2044460510,
        flag_1=2044460511,
        left=0,
        asset=2044461510,
        asset_1=2044461511,
        obj_act_id=2044463511,
        asset_2=2044461512,
        obj_act_id_1=2044463512,
        region=2044462511,
        region_1=2044462512,
        flag_2=2044460512,
        flag_3=2044460513,
        left_1=0,
    )


@RestartOnRest(2044462500)
def Event_2044462500():
    """Event 2044462500"""
    GotoIfFlagDisabled(Label.L0, flag=2044460500)
    DisableAsset(2044461500)
    DisableAsset(2044461501)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetInvulnerability(2044461501)
    
    MAIN.Await(AssetDestroyed(2044461500))
    
    DisableAssetInvulnerability(2044461501)
    WaitRealFrames(frames=1)
    DestroyAsset(2044461501, request_slot=0)
    EnableFlag(2044460500)


@RestartOnRest(2044462550)
def Event_2044462550(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: Character | int,
    other_entity: uint,
    region: Region | int,
    left: int,
    region_1: Region | int,
):
    """Event 2044462550"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.NotEqual))
    if UnsignedEqual(left=region, right=0):
        AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=110.0))
    else:
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(flag_1))
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=180.0))
    SkipLines(3)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=360.0))
    SkipLines(1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=720.0))
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagEnabled(flag_1))
    AND_4.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)
    OR_10.Add(AND_3)
    OR_10.Add(AND_4)
    
    MAIN.Await(OR_10)
    
    if FlagEnabled(flag):
        return
    SendNPCSummonHome(character=character)
    End()
    OR_11.Add(FlagDisabled(flag_2))


@RestartOnRest(2044460705)
def Event_2044460705(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 2044460705"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    if FlagEnabled(flag_1):
        return
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_3))
    if OR_1:
        return
    EnableFlag(flag)
    OR_10.Add(FlagEnabled(flag_1))
    OR_10.Add(FlagEnabled(flag_2))
    OR_10.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_10)
    
    DisableFlag(flag)


@RestartOnRest(2044460706)
def Event_2044460706(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2044460706"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    if FlagEnabled(flag_1):
        return
    EnableFlag(flag)
    OR_10.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_10)
    
    DisableFlag(flag)

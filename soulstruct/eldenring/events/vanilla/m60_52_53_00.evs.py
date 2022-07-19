"""
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
from .entities.m60_52_53_00_entities import *
from .entities.m60_52_52_00_entities import Characters as m60_52_Characters


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052530000, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76508,
        asset=Assets.AEG099_090_9001,
        source_flag=77500,
        value=7,
        flag_2=78500,
        flag_3=78501,
        flag_4=78502,
        flag_5=78503,
        flag_6=78504,
        flag_7=78505,
        flag_8=78506,
        flag_9=78507,
        flag_10=78508,
        flag_11=78509,
    )
    Event_1052532500()
    Event_1052532510()
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy0, flag=1052532710)
    Event_1052533700()
    Event_1052533701()


@RestartOnRest(1052532500)
def Event_1052532500():
    """Event 1052532500"""
    GotoIfFlagDisabled(Label.L0, flag=1252520800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(Characters.Dummy, 9531)
    GotoIfFlagEnabled(Label.L1, flag=1252520801)
    
    MAIN.Await(FlagEnabled(1252520801))
    
    GotoIfConditionTrue(Label.L2, input_condition=MAIN)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=m60_52_Characters.FireGiant0, attacker=0))
    OR_1.Add(CharacterHasStateInfo(character=m60_52_Characters.FireGiant0, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=m60_52_Characters.FireGiant0, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=m60_52_Characters.FireGiant0, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=m60_52_Characters.FireGiant0, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=m60_52_Characters.FireGiant0, state_info=260))
    OR_1.Add(EntityWithinDistance(entity=m60_52_Characters.FireGiant0, other_entity=PLAYER, radius=120.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1052532800))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1052532801))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1252522805))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.Dummy, 9532)
    End()


@RestartOnRest(1052532510)
def Event_1052532510():
    """Event 1052532510"""
    if FlagEnabled(1254560800):
        return
    SetCharacterTalkRange(character=Characters.Dummy, distance=300.0)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005781(0, flag=1252520800, flag_1=1252532160, flag_2=1252532161, character=Characters.LivingPot0)
    CommonFunc_90005783(
        0,
        flag=1252520800,
        flag_1=1252532160,
        flag_2=1252532161,
        character=Characters.LivingPot0,
        other_entity=1052532700,
        region=1052532162,
        left=2,
    )
    CommonFunc_90005781(0, flag=1252520800, flag_1=1252532164, flag_2=1252532165, character=Characters.LivingPot1)
    CommonFunc_90005783(
        0,
        flag=1252520800,
        flag_1=1252532164,
        flag_2=1252532165,
        character=Characters.LivingPot1,
        other_entity=1052532701,
        region=1052532162,
        left=2,
    )
    Event_1052532400(
        0,
        flag=1252520800,
        summon_flag=1252532160,
        dismissal_flag=1252532161,
        character=Characters.LivingPot0,
        region=1052532700,
        right=1035539209,
        unknown=0,
        flag_1=1252532400,
        flag_2=1252532401,
    )
    Event_1052532400(
        1,
        1252520800,
        1252532164,
        1252532165,
        1052530701,
        1052532701,
        1035539209,
        0,
        1252532401,
        1252532400,
    )


@NeverRestart(1052532400)
def Event_1052532400(
    _,
    flag: uint,
    summon_flag: uint,
    dismissal_flag: uint,
    character: uint,
    region: uint,
    right: uint,
    unknown: uchar,
    flag_1: uint,
    flag_2: uint,
):
    """Event 1052532400"""
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(flag):
        return
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=10.0))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag_2):
        return
    EnableFlag(flag_1)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    EnableNetworkFlag(1252520804)

    # --- Label 1 --- #
    DefineLabel(1)
    PlaceSummonSign(
        sign_type=SummonSignType.NPCWhiteSign,
        character=character,
        region=region,
        summon_flag=summon_flag,
        dismissal_flag=dismissal_flag,
        unknown=unknown,
    )


@RestartOnRest(1052533700)
def Event_1052533700():
    """Event 1052533700"""
    if FlagEnabled(1052520800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1052520800))
    OR_1.Add(FlagEnabled(1252532160))
    OR_1.Add(FlagEnabled(1252532164))
    AND_1.Add(OR_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(13009259)
    End()


@RestartOnRest(1052533701)
def Event_1052533701():
    """Event 1052533701"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3661, 3663)))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1035539209)
    End()

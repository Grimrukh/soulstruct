"""
Southwest Liurnia (NW) (SE)

linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_33_42_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1033422211()
    Event_1033422611()
    CommonFunc_90005300(0, flag=1033420610, character=Characters.GiantTurtle, item_lot=0, seconds=0.0, item_is_dropped=0)
    CommonFunc_90005880(
        0,
        flag=1033420800,
        flag_1=1033420805,
        flag_2=1033422800,
        character=Characters.BlackKnifeAssassin,
        item_lot=30265,
        area_id=60,
        block_id=33,
        cc_id=42,
        dd_id=0,
        player_start=1033422805,
    )
    CommonFunc_90005881(
        0,
        flag=1033420800,
        flag_1=1033420805,
        left_flag=1033422801,
        cancel_flag__right_flag=1033422802,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=33,
        cc_id=42,
        dd_id=0,
        player_start=1033422805,
    )
    CommonFunc_90005882(
        0,
        flag=1033420800,
        flag_1=1033420805,
        flag_2=1033422800,
        character=Characters.BlackKnifeAssassin,
        flag_3=1033422806,
        character_1=1033425810,
        asset=Assets.AEG099_120_1000,
        owner_entity=Characters.TalkDummy,
        source_entity=1033422810,
        name=902100521,
        animation_id=-1,
        animation_id_1=20020,
    )
    CommonFunc_90005883(0, flag=1033420800, flag_1=1033420805, entity=Assets.AEG099_170_1000)
    CommonFunc_90005885(
        0,
        flag=1033420800,
        bgm_boss_conv_param_id=0,
        flag_1=1033422806,
        flag_2=1033422807,
        left=0,
        left_1=1,
    )


@RestartOnRest(1033422211)
def Event_1033422211():
    """Event 1033422211"""
    if FlagEnabled(1033420610):
        return
    DisableAI(Characters.GiantTurtle)
    ForceAnimation(Characters.GiantTurtle, 30008)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.GiantTurtle, attacker=PLAYER))
    OR_2.Add(EntityWithinDistance(entity=Characters.GiantTurtle, other_entity=40000, radius=7.0))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(1033420610)
    ForceAnimation(Characters.GiantTurtle, 20016, wait_for_completion=True)


@RestartOnRest(1033422611)
def Event_1033422611():
    """Event 1033422611"""
    if FlagEnabled(1033420610):
        return
    DisableCharacter(Characters.GiantTurtle)
    DisableAnimations(Characters.GiantTurtle)
    if PlayerNotInOwnWorld():
        EnableInvincibility(Characters.GiantTurtle)
    AND_1.Add(FlagEnabled(1034432616))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(Characters.GiantTurtle)
    EnableAnimations(Characters.GiantTurtle)
    EnableImmortality(Characters.GiantTurtle)
    DisableHealthBar(Characters.GiantTurtle)

"""
Northwest Caelid (NE) (SE)

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
    Event_1047422600()
    Event_1047422602()
    Event_1047422601()
    CommonFunc_900005610(0, asset=1047421690, dummy_id=100, vfx_id=800, right=1047428560)


@RestartOnRest(1047422600)
def Event_1047422600():
    """Event 1047422600"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(710870))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1047422600))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(710870)
    EnableFlag(60370)
    if FlagDisabled(6080):
        EnableFlag(6080)
        StartPS5Activity(activity_id=7)
    WaitFrames(frames=1)
    DisplayTutorialMessage(tutorial_param_id=1870, unk_4_5=True, unk_5_6=True)
    if FlagDisabled(69470):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9152, flag=710870, bit_count=1)
    WaitFrames(frames=1)
    EnableFlag(69470)


@RestartOnRest(1047422602)
def Event_1047422602():
    """Event 1047422602"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(710880))
    AND_1.Add(FlagDisabled(69480))
    AND_1.Add(FlagDisabled(2051))
    AND_1.Add(FlagDisabled(2052))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=1880, unk_4_5=True, unk_5_6=True)
    if FlagDisabled(69480):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9153, flag=710880, bit_count=1)
    EnableFlag(69480)


@RestartOnRest(1047422601)
def Event_1047422601():
    """Event 1047422601"""
    if FlagEnabled(1047428560):
        return
    GotoIfMultiplayer(Label.L0)
    GotoIfMultiplayerPending(Label.L0)
    EnableAssetActivation(1047421601, obj_act_id=400655)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(OR_2)
    
    DisableAssetActivation(1047421601, obj_act_id=400655)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(1047421601, obj_act_id=400655)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(not OR_2)
    
    EnableAssetActivation(1047421601, obj_act_id=400655)
    Restart()

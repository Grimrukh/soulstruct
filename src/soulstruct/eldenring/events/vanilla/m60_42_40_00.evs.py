"""
Northwest Limgrave Coast (SE) (SW)

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
from .enums.m60_42_40_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1042402650(0, flag=710670, tutorial_param_id=1670, item=9123, flag_1=69230)
    Event_1042402655()
    Event_1042402657()
    Event_1042402656()
    Event_1042402390()
    CommonFunc_90005706(0, character=Characters.StormhillColosseumSilentSpirit, animation_id=90101, left=0)
    Event_1042402659()
    CommonFunc_900005610(0, asset=1042401690, dummy_id=100, vfx_id=800, right=1042408560)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.StormhillColosseumSilentSpirit)


@RestartOnRest(1042402650)
def Event_1042402650(_, flag: Flag | int, tutorial_param_id: int, item: BaseItemParam | int, flag_1: Flag | int):
    """Event 1042402650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1042402655)
def Event_1042402655():
    """Event 1042402655"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(710860))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1042402655))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(710860)
    EnableFlag(60360)
    if FlagDisabled(6080):
        EnableFlag(6080)
        StartPS5Activity(activity_id=7)
    WaitFrames(frames=1)
    DisplayTutorialMessage(tutorial_param_id=1860, unk_4_5=True, unk_5_6=True)
    if FlagDisabled(69460):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9151, flag=710860, bit_count=1)
    WaitFrames(frames=1)
    EnableFlag(69460)


@RestartOnRest(1042402657)
def Event_1042402657():
    """Event 1042402657"""
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
    
    WaitFrames(frames=1)
    DisplayTutorialMessage(tutorial_param_id=1880, unk_4_5=True, unk_5_6=True)
    if FlagDisabled(69480):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9153, flag=710880, bit_count=1)
    EnableFlag(69480)


@RestartOnRest(1042402656)
def Event_1042402656():
    """Event 1042402656"""
    if FlagEnabled(1042408560):
        return
    GotoIfMultiplayer(Label.L0)
    GotoIfMultiplayerPending(Label.L0)
    EnableAssetActivation(1042401656, obj_act_id=400655)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(OR_2)
    
    DisableAssetActivation(1042401656, obj_act_id=400655)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(1042401656, obj_act_id=400655)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(not OR_2)
    
    EnableAssetActivation(1042401656, obj_act_id=400655)
    Restart()


@RestartOnRest(1042402658)
def Event_1042402658():
    """Event 1042402658"""
    if FlagEnabled(1042408560):
        return
    GotoIfMultiplayer(Label.L0)
    GotoIfMultiplayerPending(Label.L0)
    EnableAssetActivation(1042401656, obj_act_id=400655)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(OR_2)
    
    DisableAssetActivation(1042401656, obj_act_id=400655)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(1042401656, obj_act_id=400655)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(not OR_2)
    
    EnableAssetActivation(1042401656, obj_act_id=400655)
    Restart()


@RestartOnRest(1042402659)
def Event_1042402659():
    """Event 1042402659"""
    WaitFrames(frames=1)
    DisableCharacter(Characters.StormhillColosseumSilentSpirit)


@RestartOnRest(1042403700)
def Event_1042403700(_, character: uint):
    """Event 1042403700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30025)


@RestartOnRest(1042402390)
def Event_1042402390():
    """Event 1042402390"""
    DisableNetworkSync()
    
    MAIN.Await(InsideMap(game_map=NORTHWEST_LIMGRAVE_COAST_SE_SW))
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1042402390))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()

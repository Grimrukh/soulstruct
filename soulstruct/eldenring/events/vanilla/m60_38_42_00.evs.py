"""
Southeast Liurnia (NE) (SW)

linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_38_42_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1038422200(0, character=Characters.RayaLucariaSoldier0)
    Event_1038422200(1, character=Characters.RayaLucariaSoldier1)
    Event_1038422200(2, character=Characters.RayaLucariaSoldier2)
    Event_1038422200(3, character=Characters.RayaLucariaFootSoldier0)
    Event_1038422200(4, character=Characters.RayaLucariaFootSoldier1)
    Event_1038422200(5, character=Characters.RayaLucariaFootSoldier2)
    Event_1038422230(0, character=Characters.WanderingNoble0, region=1038422230, flag=1038422220)
    Event_1038422230(1, character=Characters.WanderingNoble1, region=1038422230, flag=1038422221)
    Event_1038422230(2, character=Characters.WanderingNoble2, region=1038422230, flag=1038422222)
    Event_1038422230(3, character=Characters.WanderingNoble3, region=1038422230, flag=1038422223)
    Event_1038422230(4, character=Characters.WanderingNoble4, region=1038422230, flag=1038422224)
    Event_1038422230(5, character=Characters.WanderingNoble5, region=1038422230, flag=1038422225)
    Event_1038422230(6, character=Characters.WanderingNoble6, region=1038422231, flag=1038422226)
    Event_1038422230(7, character=Characters.WanderingNoble7, region=1038422231, flag=1038422227)
    Event_1038422230(8, character=Characters.WanderingNoble8, region=1038422231, flag=1038422228)
    Event_1038422230(9, character=Characters.WanderingNoble9, region=1038422231, flag=1038422229)
    Event_1038422230(10, character=Characters.WanderingNoble10, region=1038422231, flag=1038422230)
    Event_1038422240()
    Event_1038422580()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, 1038420240, 1038422240, 30.0, 0.0, 0)


@RestartOnRest(1038422200)
def Event_1038422200(_, character: uint):
    """Event 1038422200"""
    Kill(character)
    End()


@RestartOnRest(1038422230)
def Event_1038422230(_, character: uint, region: uint, flag: uint):
    """Event 1038422230"""
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    AND_1.Add(OR_2)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    ForceAnimation(character, 30004)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20004)
    End()


@RestartOnRest(1038422240)
def Event_1038422240():
    """Event 1038422240"""
    OR_15.Add(CharacterDead(Characters.RayaLucariaScholar))
    if OR_15:
        return
    AddSpecialEffect(Characters.RayaLucariaScholar, 8089)
    End()


@ContinueOnRest(1038422580)
def Event_1038422580():
    """Event 1038422580"""
    RegisterLadder(start_climbing_flag=1038420580, stop_climbing_flag=1038420581, asset=Assets.AEG110_012_2000)
    RegisterLadder(start_climbing_flag=1038420582, stop_climbing_flag=1038420583, asset=Assets.AEG110_012_2001)
    RegisterLadder(start_climbing_flag=1038420584, stop_climbing_flag=1038420585, asset=Assets.AEG110_012_2002)

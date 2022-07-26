"""
West Limgrave (NE) (SW)

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
from .entities.m60_42_38_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1042380000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005860(
        0,
        flag=1042380800,
        left=0,
        character=Characters.DeathRiteBird,
        left_1=0,
        item_lot=1042380400,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.DeathRiteBird, name=904980601, npc_threat_level=24)
    Event_1042382350()
    CommonFunc_90005460(0, character=Characters.GiantOctopus)
    CommonFunc_90005461(0, character=Characters.GiantOctopus)
    CommonFunc_90005462(0, character=Characters.GiantOctopus)
    CommonFunc_90005760(
        0,
        flag=1042380850,
        character=Characters.BellBearingHunter,
        region=1042382360,
        flag_1=1042382718,
    )
    CommonFunc_90005770(0, flag=1042380701)
    CommonFunc_90005860(
        0,
        flag=1042380850,
        left=0,
        character=Characters.BellBearingHunter,
        left_1=0,
        item_lot=1042380410,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.BellBearingHunter, name=903100600, npc_threat_level=10)
    CommonFunc_90005872(0, character=Characters.BellBearingHunter, npc_threat_level=10, right=0)
    Event_1042383700(0, character=Characters.KnightBernahl)
    CommonFunc_90005704(0, attacked_entity=Characters.KnightBernahl, flag=3881, flag_1=3880, flag_2=1042389251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.KnightBernahl,
        flag=3881,
        flag_1=3882,
        flag_2=1042389251,
        flag_3=3881,
        first_flag=3880,
        last_flag=3884,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.KnightBernahl, flag=3883, first_flag=3880, last_flag=3884)
    CommonFunc_90005630(0, far_view_id=61423800, asset=1042381500, model_point=127)
    CommonFunc_90005560(0, flag=1042380600, asset=Assets.AEG099_635_9000, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.KnightBernahl)
    CommonFunc_90005251(0, character=Characters.WolfPackLeader, radius=40.0, seconds=0.0, animation_id=3011)
    CommonFunc_90005261(
        0,
        character=Characters.GodrickSoldier0,
        region=1042382240,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GodrickSoldier1,
        region=1042382240,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GodrickSoldier2,
        region=1042382240,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GodrickSoldier3,
        region=1042382240,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=1042380254, region=1042382254, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1042380255, region=1042382254, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1042380256, region=1042382254, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1042380262, region=1042382254, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1042380263, region=1042382254, radius=1.0, seconds=0.0, animation_id=-1)
    Event_1042382300()
    CommonFunc_90005211(
        0,
        character=Characters.DeathRiteBird,
        animation_id=30000,
        animation_id_1=20000,
        region=1042382340,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    Event_1042382290()


@RestartOnRest(1042382290)
def Event_1042382290():
    """Event 1042382290"""
    DisableNetworkSync()
    if CharacterInsideRegion(character=PLAYER, region=1043392396):
        return
    GotoIfFlagEnabled(Label.L0, flag=1042372800)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382290))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382291))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382292))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382293))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382294))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382295))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382296))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382297))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1042382298))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4211)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(1.0)
    Restart()


@RestartOnRest(1042382300)
def Event_1042382300():
    """Event 1042382300"""
    DropMandatoryTreasure(1042385200)


@RestartOnRest(1042382340)
def Event_1042382340(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 1042382340"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_3.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 0, 0)))
    AND_1.Add(AND_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1042382350)
def Event_1042382350():
    """Event 1042382350"""
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.Troll1)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1042382350))
    OR_3.Add(AttackedWithDamageType(attacked_entity=Characters.Troll1))
    OR_3.Add(CharacterHasStateInfo(character=Characters.Troll1, state_info=436))
    OR_3.Add(CharacterHasStateInfo(character=Characters.Troll1, state_info=2))
    OR_3.Add(CharacterHasStateInfo(character=Characters.Troll1, state_info=5))
    OR_3.Add(CharacterHasStateInfo(character=Characters.Troll1, state_info=6))
    OR_3.Add(CharacterHasStateInfo(character=Characters.Troll1, state_info=260))
    OR_3.Add(HasAIStatus(Characters.Troll1, ai_status=AIStatusType.Battle))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1042382351))
    AND_2.Add(OR_3)
    OR_2.Add(AND_2)
    AND_1.Add(OR_2)
    AND_4.Add(CharacterHasSpecialEffect(Characters.Troll1, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.Troll1, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.Troll1, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.Troll1, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.Troll1, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.Troll1, 90160))
    OR_4.Add(AND_4)
    OR_4.Add(AND_5)
    OR_4.Add(AND_6)
    OR_4.Add(AND_7)
    OR_4.Add(AND_8)
    OR_4.Add(AND_1)
    
    MAIN.Await(OR_4)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=Characters.Troll1, state=True)
    ForceAnimation(Characters.Troll1, 20016, wait_for_completion=True)
    ChangePatrolBehavior(Characters.Troll1, patrol_information_id=1042383350)


@RestartOnRest(1042382600)
def Event_1042382600(_, flag: uint, asset: uint):
    """Event 1042382600"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    PostDestruction(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(AssetDestroyed(asset))
    
    EnableNetworkFlag(flag)


@RestartOnRest(1042382650)
def Event_1042382650(_, tutorial_param_id: int, flag: uint):
    """Event 1042382650"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9530))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(6580))
    AND_1.Add(FlagEnabled(710550))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_NE_SW))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag, bit_count=1)


@RestartOnRest(1042382651)
def Event_1042382651(_, tutorial_param_id: int, flag: uint):
    """Event 1042382651"""
    if Multiplayer():
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    OR_1.Add(PlayerHasGood(203000, including_storage=True))
    AND_1.Add(Singleplayer())
    AND_1.Add(PlayerDoesNotHaveGood(9111, including_storage=True))
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_NE_SW))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(1042383700)
def Event_1042383700(_, character: uint):
    """Event 1042383700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3880):
        DisableFlag(1042389253)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L19, flag=1042382719)
    DisableNetworkFlag(1042382718)
    OR_15.Add(FlagEnabled(1042380701))
    OR_15.Add(FlagEnabled(3881))
    OR_15.Add(FlagEnabled(3882))
    OR_15.Add(FlagEnabled(3883))
    OR_15.Add(FlagDisabled(3885))
    AND_15.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 30, 0)))
    AND_15.Add(FlagDisabled(1042380850))
    AND_15.Add(OR_15)
    GotoIfConditionFalse(Label.L19, input_condition=AND_15)
    EnableNetworkFlag(1042382718)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableNetworkFlag(1042382719)
    GotoIfFlagEnabled(Label.L5, flag=3885)
    GotoIfFlagEnabled(Label.L4, flag=3888)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3885))
    OR_3.Add(FlagEnabled(3888))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3880)
    GotoIfFlagEnabled(Label.L2, flag=3881)
    GotoIfFlagEnabled(Label.L3, flag=3882)
    GotoIfFlagEnabled(Label.L4, flag=3883)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1042382718):
        DisableCharacter(character)
        DisableBackread(character)
        Goto(Label.L20)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(1042382718):
        DisableCharacter(character)
        DisableBackread(character)
        Goto(Label.L20)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagEnabled(1042382718):
        DisableCharacter(character)
        DisableBackread(character)
        Goto(Label.L20)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3885))
    OR_4.Add(FlagEnabled(3888))
    
    MAIN.Await(not OR_4)
    
    Restart()

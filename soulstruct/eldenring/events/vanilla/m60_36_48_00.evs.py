"""
Liurnia to Altus Plateau (SW) (SW)

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
from .enums.m60_36_48_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036480000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76209,
        flag_1=76207,
        asset=Assets.AEG099_090_9001,
        source_flag=77210,
        value=0,
        flag_2=78210,
        flag_3=78211,
        flag_4=78212,
        flag_5=78213,
        flag_6=78214,
        flag_7=78215,
        flag_8=78216,
        flag_9=78217,
        flag_10=78218,
        flag_11=78219,
    )
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble,
        region=1036482200,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005300(0, flag=1036480800, character=Characters.NightsCavalryHorse, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005476(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    RunCommonEvent(90005477)
    Event_1036482340(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    CommonFunc_90005860(
        0,
        flag=1036480800,
        left=0,
        character=Characters.NightsCavalry,
        left_1=0,
        item_lot=1036480400,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.NightsCavalry, npc_threat_level=10, right=0)
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry,
        name=903150603,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse,
    )
    CommonFunc_90005703(
        0,
        character=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3942,
        flag_2=1039409251,
        flag_3=3941,
        first_flag=3940,
        last_flag=3943,
        right=0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3940,
        flag_2=1039409251,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.DemiHumanShaman, flag=3943, first_flag=3940, last_flag=3944)
    Event_1036483700(0, character=Characters.DemiHumanShaman)
    Event_1036483701(0, entity=Characters.DemiHumanShaman)
    CommonFunc_90005705(0, character=Characters.FingerReader)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy0, flag=1036482710)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.DemiHumanShaman)
    DisableBackread(Characters.FingerReader)


@RestartOnRest(1036482340)
def Event_1036482340(_, character: Character | int, character_1: Character | int):
    """Event 1036482340"""
    AND_1.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    AND_2.Add(CharacterHasSpecialEffect(character, 11825))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_3)
    
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_4.Add(CharacterBackreadDisabled(character_1))
    
    MAIN.Await(AND_4)
    
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@RestartOnRest(1036483700)
def Event_1036483700(_, character: uint):
    """Event 1036483700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(FlagEnabled(3940))
    AND_1.Add(FlagEnabled(1043379353))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379353)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    AND_5.Add(FlagEnabled(3947))
    AND_5.Add(FlagDisabled(1039519209))
    AND_5.Add(FlagDisabled(11109819))
    AND_5.Add(FlagDisabled(3956))
    AND_5.Add(FlagDisabled(3957))
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    AND_6.Add(FlagEnabled(3947))
    AND_6.Add(FlagDisabled(1039519209))
    AND_6.Add(FlagDisabled(11109819))
    AND_6.Add(FlagDisabled(3956))
    AND_6.Add(FlagDisabled(3957))
    
    MAIN.Await(AND_6)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(4, 3955)
    SkipLinesIfFlagEnabled(3, 1036489213)
    AND_6.Add(FlagEnabled(76207))
    AND_6.Add(FlagEnabled(9000))
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    EnableNetworkFlag(1036489213)
    EnableNetworkFlag(3955)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
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
    AND_15.Add(FlagEnabled(3947))
    AND_15.Add(FlagDisabled(1039519209))
    AND_15.Add(FlagDisabled(11109819))
    AND_15.Add(FlagDisabled(3956))
    AND_15.Add(FlagDisabled(3957))
    
    MAIN.Await(not AND_15)
    
    Restart()


@RestartOnRest(1036483701)
def Event_1036483701(_, entity: uint):
    """Event 1036483701"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(3943))
    OR_1.Add(FlagDisabled(3947))
    OR_1.Add(FlagEnabled(1039409259))
    if OR_1:
        return
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=ALL_PLAYERS, radius=4.0))
    AND_1.Add(CharacterHasSpecialEffect(ALL_PLAYERS, 9690))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()

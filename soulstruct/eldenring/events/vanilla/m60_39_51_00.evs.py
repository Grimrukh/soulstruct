"""
Liurnia to Altus Plateau (NE) (NE)

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
from .entities.m60_39_51_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76303, asset=Assets.AEG099_060_9000, enemy_block_distance=3.0)
    CommonFunc_90005100(
        0,
        flag=76314,
        flag_1=76303,
        asset=Assets.AEG099_060_9001,
        source_flag=77300,
        value=2,
        flag_2=78300,
        flag_3=78301,
        flag_4=78302,
        flag_5=78303,
        flag_6=78304,
        flag_7=78305,
        flag_8=78306,
        flag_9=78307,
        flag_10=78308,
        flag_11=78309,
    )
    CommonFunc_90005476(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    Event_1039512451(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry,
        name=903150604,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse,
    )
    CommonFunc_90005860(
        0,
        flag=1039510800,
        left=0,
        character=Characters.NightsCavalry,
        left_1=0,
        item_lot=1039510200,
        seconds=0.0,
    )
    CommonFunc_90005300(
        0,
        flag=1039510800,
        character=Characters.NightsCavalryHorse,
        item_lot=0,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005872(0, character=Characters.NightsCavalry, npc_threat_level=10, right=0)
    CommonFunc_90005300(0, flag=1039510500, character=Characters.Scarab, item_lot=40304, seconds=0.0, left=0)
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
    Event_1039513700(0, character=Characters.DemiHumanShaman)
    Event_1039513701(0, entity=Characters.DemiHumanShaman)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy, flag=1039512710)
    CommonFunc_90005771(0, 1039510950, 1039512711)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.DemiHumanShaman)
    CommonFunc_90005201(
        0,
        character=1039510201,
        animation_id=30000,
        animation_id_1=20000,
        radius=12.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1039510202,
        animation_id=30001,
        animation_id_1=20001,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellSoldier,
        region=1039512300,
        radius=5.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier0,
        animation_id=30001,
        animation_id_1=20001,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier1,
        animation_id=30010,
        animation_id_1=20010,
        radius=18.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier2,
        animation_id=30010,
        animation_id_1=20010,
        radius=18.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.MadPumpkinHead, region=1039512350, seconds=0.0, animation_id=3003)
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellKnight1,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 1039510361, 1039512361, 0.0, -1)


@RestartOnRest(1039512451)
def Event_1039512451(_, character: uint, character_1: uint):
    """Event 1039512451"""
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


@RestartOnRest(1039513700)
def Event_1039513700(_, character: uint):
    """Event 1039513700"""
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
    AND_5.Add(FlagDisabled(11109819))
    AND_5.Add(FlagDisabled(3957))
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    AND_6.Add(FlagEnabled(3947))
    AND_6.Add(FlagDisabled(11109819))
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
    SkipLinesIfFlagEnabled(4, 3956)
    SkipLinesIfFlagEnabled(3, 1039519209)
    AND_6.Add(FlagEnabled(76303))
    AND_6.Add(FlagEnabled(9000))
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    EnableNetworkFlag(1039519209)
    EnableNetworkFlag(3956)
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
    AND_15.Add(FlagDisabled(11109819))
    AND_15.Add(FlagDisabled(3957))
    
    MAIN.Await(not AND_15)
    
    Restart()


@RestartOnRest(1039513701)
def Event_1039513701(_, entity: uint):
    """Event 1039513701"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(3943))
    OR_1.Add(FlagDisabled(3947))
    OR_1.Add(FlagEnabled(1039409259))
    if OR_1:
        return
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=20000, radius=4.0))
    AND_1.Add(CharacterHasSpecialEffect(20000, 9690))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()

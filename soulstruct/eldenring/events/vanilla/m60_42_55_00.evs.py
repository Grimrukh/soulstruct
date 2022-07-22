"""
North Altus Plateau (NE) (NW)

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
from .entities.m60_42_55_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005810(
        0,
        flag=1042550800,
        grace_flag=1042550000,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005870(0, character=Characters.GodskinApostle, name=903560600, npc_threat_level=27)
    CommonFunc_90005860(
        0,
        flag=1042550800,
        left=0,
        character=Characters.GodskinApostle,
        left_1=0,
        item_lot__item_lot_param_id=30325,
        seconds=0.0,
    )
    CommonFunc_90005780(
        0,
        flag=1042550800,
        summon_flag=1042552160,
        dismissal_flag=1042552161,
        character=Characters.Millicent1,
        sign_type=20,
        region=1042552700,
        right=1042559207,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=1042550800, flag_1=1042552160, flag_2=1042552161, character=Characters.Millicent1)
    CommonFunc_90005783(
        0,
        flag=1042550800,
        flag_1=1042552160,
        flag_2=1042552161,
        character=Characters.Millicent1,
        other_entity=1042552700,
        region=1041542701,
        left=1,
    )
    Event_1042553710(0, character=Characters.Millicent0)
    CommonFunc_90005704(0, attacked_entity=Characters.Millicent0, flag=4181, flag_1=4180, flag_2=1042559201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Millicent0,
        flag=4181,
        flag_1=4182,
        flag_2=1042559201,
        flag_3=1059481190,
        first_flag=4180,
        last_flag=4184,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Millicent0, flag=4183, first_flag=4180, last_flag=4184)
    Event_1042553711()
    Event_1042553712()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Millicent0)
    CommonFunc_90005251(0, 1042550800, 50.0, 0.0, 0)


@RestartOnRest(1042553710)
def Event_1042553710(_, character: uint):
    """Event 1042553710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4180):
        DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4188)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4188))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(4188))
    
    Restart()


@RestartOnRest(1042553711)
def Event_1042553711():
    """Event 1042553711"""
    if FlagEnabled(1042550800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1042552160))
    AND_1.Add(FlagEnabled(1042550800))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1042559204)
    End()


@RestartOnRest(1042553712)
def Event_1042553712():
    """Event 1042553712"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAllDisabled(flag_range=(1042559207, 1042559209))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(4181, 4183)))
    AwaitConditionTrue(AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1042559207, 1042559209))
    End()

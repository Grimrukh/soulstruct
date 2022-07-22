"""
North Caelid (SW) (NW)

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
from .entities.m60_48_41_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1048410000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005300(0, flag=1048410290, character=Characters.Scarab, item_lot=40412, seconds=0.0, left=0)
    CommonFunc_90005760(
        0,
        flag=1048410800,
        character=Characters.BellBearingHunter,
        region=1048412300,
        flag_1=1048412708,
    )
    CommonFunc_90005870(0, character=Characters.BellBearingHunter, name=903100603, npc_threat_level=10)
    CommonFunc_90005860(
        0,
        flag=1048410800,
        left=0,
        character=Characters.BellBearingHunter,
        left_1=0,
        item_lot=1048410800,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.BellBearingHunter, npc_threat_level=10, right=0)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4793, first_flag=4790, last_flag=4793)
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4791,
        flag_1=4792,
        flag_2=1048410702,
        flag_3=4791,
        first_flag=4790,
        last_flag=4793,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4791, flag_1=4790, flag_2=1048410702, right=3)
    Event_1048410700(0, character=Characters.Merchant, character_1=Characters.NomadMule, asset=1048416700)
    CommonFunc_90005770(0, flag=1048410701)
    CommonFunc_90005727(
        0,
        flag=4791,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4790,
        last_flag=4793,
    )
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1048412706, flag_1=1048412707)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4791,
        flag_1=4792,
        flag_2=1048410702,
        flag_3=4791,
        first_flag=4790,
        last_flag=4793,
        right=0,
    )
    CommonFunc_90005704(0, 1048410701, 4791, 4790, 1048410702, 3)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)


@RestartOnRest(1048410700)
def Event_1048410700(_, character: uint, character_1: uint, asset: uint):
    """Event 1048410700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4790):
        DisableFlag(1048419205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L4, flag=1048412709)
    DisableNetworkFlag(1048412708)
    OR_1.Add(FlagEnabled(1048410701))
    OR_1.Add(FlagEnabled(4791))
    OR_1.Add(FlagEnabled(4793))
    AND_1.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 30, 0)))
    AND_1.Add(FlagDisabled(1048410800))
    AND_1.Add(OR_1)
    GotoIfConditionFalse(Label.L4, input_condition=AND_1)
    EnableNetworkFlag(1048412708)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(1048412709)
    GotoIfFlagEnabled(Label.L0, flag=4790)
    GotoIfFlagEnabled(Label.L1, flag=4791)
    GotoIfFlagEnabled(Label.L3, flag=4793)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(1048412708):
        DisableCharacter(character)
        DisableBackread(character)
        DisableCharacter(character_1)
        DisableBackread(character_1)
        DisableAsset(asset)
        Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930003)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1048412708):
        DisableCharacter(character)
        DisableBackread(character)
        DisableCharacter(character_1)
        DisableBackread(character_1)
        DisableAsset(asset)
        Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()

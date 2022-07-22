"""
Liurnia to Altus Plateau (SW) (NW)

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
from .entities.m60_36_49_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036490000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76209,
        flag_1=76208,
        asset=Assets.AEG099_090_9001,
        source_flag=77210,
        value=1,
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
    RegisterGrace(grace_flag=1036490001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005300(
        0,
        flag=1036490200,
        character=Characters.ExtraLargeScarab,
        item_lot=40204,
        seconds=0.0,
        left=0,
    )
    Event_1036492610()
    CommonFunc_90005704(0, attacked_entity=Characters.Hyetta, flag=3381, flag_1=3380, flag_2=1036499201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Hyetta,
        flag=3381,
        flag_1=3382,
        flag_2=1036499201,
        flag_3=3381,
        first_flag=3380,
        last_flag=3384,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Hyetta, flag=3383, first_flag=3380, last_flag=3384)
    Event_1036493700(0, character=Characters.Hyetta)
    CommonFunc_90005725(
        0,
        flag=4755,
        flag_1=4756,
        flag_2=4758,
        flag_3=1036499255,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1036496700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4756,
        flag_1=4757,
        flag_2=1036499256,
        flag_3=4756,
        first_flag=4755,
        last_flag=4759,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4756, flag_1=4755, flag_2=1036499256, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4758, first_flag=4755, last_flag=4759)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4756,
        flag_1=4757,
        flag_2=1036499257,
        flag_3=4756,
        first_flag=4755,
        last_flag=4759,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4756, flag_1=4755, flag_2=1036499257, right=3)
    CommonFunc_90005727(0, 4756, 1036490705, 1036490706, 4755, 4758)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Hyetta)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)


@RestartOnRest(1036492610)
def Event_1036492610():
    """Event 1036492610"""
    OR_1.Add(AssetDestroyed(Assets.AEG003_089_9000))
    OR_2.Add(AssetNotDestroyed(Assets.AEG217_064_9000))
    OR_2.Add(AssetNotDestroyed(Assets.AEG217_064_9000))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DestroyAsset(Assets.AEG217_064_9000, request_slot=0)
    DestroyAsset(Assets.AEG217_064_9001, request_slot=0)


@RestartOnRest(1036493700)
def Event_1036493700(_, character: uint):
    """Event 1036493700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3380):
        DisableFlag(1036499202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L11, flag=3391)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3391))
    
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3391))
    
    Restart()

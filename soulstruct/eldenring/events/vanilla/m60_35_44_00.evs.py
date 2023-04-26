"""
West Liurnia (SE) (SE)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_35_44_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1035442650(0, flag=710680, tutorial_param_id=1680, item=9124, flag_1=69240)
    Event_1035443700(0, character=Characters.WhiteMaskVarre, asset=Assets.AEG007_360_1000)
    Event_1035443701(0, character=Characters.WhiteMaskVarre)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.WhiteMaskVarre,
        flag=3181,
        flag_1=3180,
        flag_2=1035449201,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.WhiteMaskVarre,
        flag=3181,
        flag_1=3182,
        flag_2=1035449201,
        flag_3=3181,
        first_flag=3180,
        last_flag=3184,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.WhiteMaskVarre, flag=3183, first_flag=3180, last_flag=3184)
    CommonFunc_90005740(
        0,
        flag=1035442705,
        flag_1=1035442706,
        left=1035442707,
        character=Characters.WhiteMaskVarre,
        model_point=700,
        asset=Assets.AEG099_090_9002,
        model_point_1=700,
        radius=0.20000000298023224,
        animation=90201,
        animation_id=-1,
        special_effect=-1,
        radius_1=1.100000023841858,
    )
    CommonFunc_90005741(
        0,
        flag=1035442708,
        flag_1=1035442709,
        left=1035442707,
        character=Characters.WhiteMaskVarre,
        animation__animation_id=90203,
        left_1=0,
        animation_id=-1,
        special_effect=-1,
        seconds=0.5,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WhiteMaskVarre)
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaSoldier0,
        region=1035442210,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaSoldier1,
        region=1035442210,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=1035440202, region=1035442210, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=1035440203, region=1035442210, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=1035440204, region=1035442210, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.ManeuverableFlamethrower,
        region=1035442210,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SanguineNoble,
        animation_id=30000,
        animation_id_1=20000,
        region=1035442220,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(1035442650)
def Event_1035442650(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 1035442650"""
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


@RestartOnRest(1035443700)
def Event_1035443700(_, character: uint, asset: uint):
    """Event 1035443700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3180):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3188)
    GotoIfFlagEnabled(Label.L5, flag=3189)
    GotoIfFlagEnabled(Label.L5, flag=3190)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(3188))
    OR_3.Add(FlagEnabled(3189))
    OR_3.Add(FlagEnabled(3190))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableAsset(asset)
    GotoIfFlagEnabled(Label.L1, flag=3180)
    GotoIfFlagEnabled(Label.L2, flag=3181)
    GotoIfFlagEnabled(Label.L3, flag=3182)
    GotoIfFlagEnabled(Label.L4, flag=3183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

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
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3188))
    OR_4.Add(FlagEnabled(3189))
    OR_4.Add(FlagEnabled(3190))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1035443701)
def Event_1035443701(_, character: uint):
    """Event 1035443701"""
    if FlagEnabled(3181):
        return
    if FlagEnabled(3183):
        return
    OR_1.Add(CharacterHasSpecialEffect(character, 90))
    OR_1.Add(FlagEnabled(3181))
    
    MAIN.Await(OR_1)
    
    if CharacterHasSpecialEffect(character=character, special_effect=90):
        return
    ForceAnimation(character, 90205)
    End()

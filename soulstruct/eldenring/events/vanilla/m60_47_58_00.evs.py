"""
West Consecrated Snowfield (NE) (SE)

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
from .entities.m60_47_58_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1047580000, asset=Assets.AEG099_060_9000)
    Event_1047583500(0, region=1047582710)
    Event_1047583700(
        0,
        character=Characters.AlbinauricArcher,
        character_1=Characters.ApostateAlbinauricArcher,
        asset=Assets.AEG099_990_9001,
    )
    Event_1047583701(0, character=Characters.AlbinauricArcher, entity=Assets.AEG099_090_9001)
    Event_1047583702(0, character=Characters.AlbinauricArcher)
    Event_1047583703(0, character=Characters.AlbinauricArcher)
    Event_1047583704(0, entity=Characters.AlbinauricArcher)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9001,
        action_button_id=4350,
        item_lot_param_id=104110,
        first_flag=400411,
        last_flag=400411,
        flag=1047589210,
        model_point=0,
    )
    CommonFunc_90005708(0, 1047580710, 6001, 0)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005451(0, character=Characters.WalkingMausoleum, asset_group=1247586420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=1247580400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=1247582400, flag_1=1247580400)
    CommonFunc_90005458(0, character=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9000, model_point=101, seconds=0.0)
    CommonFunc_90005453(
        1,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9001,
        model_point=102,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9002,
        model_point=103,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(
        0,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9003,
        model_point=104,
        seconds=0.30000001192092896,
    )
    CommonFunc_90005453(
        0,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9004,
        model_point=105,
        seconds=0.4000000059604645,
    )
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9005, model_point=106, seconds=0.5)
    CommonFunc_90005453(
        0,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9006,
        model_point=107,
        seconds=0.6000000238418579,
    )
    CommonFunc_90005453(
        0,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9007,
        model_point=108,
        seconds=0.699999988079071,
    )
    CommonFunc_90005453(
        0,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9008,
        model_point=109,
        seconds=0.800000011920929,
    )
    CommonFunc_90005453(
        0,
        asset__character=1247580400,
        asset=Assets.AEG300_006_9009,
        model_point=110,
        seconds=0.8999999761581421,
    )
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9010, model_point=111, seconds=1.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9016, model_point=117, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9017, model_point=118, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9018, model_point=119, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9019, model_point=120, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9020, model_point=121, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9021, model_point=122, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9022, model_point=123, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9023, model_point=124, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9024, model_point=125, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9025, model_point=126, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9026, model_point=127, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9027, model_point=128, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9032, model_point=133, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9033, model_point=134, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9034, model_point=135, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9035, model_point=136, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9036, model_point=137, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9037, model_point=138, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9038, model_point=139, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9039, model_point=140, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9040, model_point=141, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9041, model_point=142, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9048, model_point=149, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9049, model_point=150, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9050, model_point=151, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9051, model_point=152, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9052, model_point=153, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9053, model_point=154, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9054, model_point=155, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9055, model_point=156, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9056, model_point=157, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9057, model_point=158, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1247580400, asset=Assets.AEG300_006_9058, model_point=159, seconds=0.0)
    CommonFunc_90005456(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_004_9000,
        asset_1=Assets.AEG300_005_9000,
        flag=1247580400,
    )
    Event_1247582350(0, 1247580400, 1247582400)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1047580700)
    DisableBackread(Characters.AlbinauricArcher)


@RestartOnRest(1047583500)
def Event_1047583500(_, region: uint):
    """Event 1047583500"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(character=20000, region=region))
    OR_1.Add(Invasion())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    OR_2.Add(CharacterOutsideRegion(character=20000, region=region))
    OR_2.Add(Invasion())
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(1047583700)
def Event_1047583700(_, character: uint, character_1: uint, asset: uint):
    """Event 1047583700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    EnableBackread(character_1)
    EnableCharacter(character_1)
    EnableCharacterCollision(character_1)
    DisableGravity(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 930009)
    MoveAssetToCharacter(asset, character=character)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4100):
        DisableFlag(1036419203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4106)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(4106))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4100)
    GotoIfFlagEnabled(Label.L2, flag=4101)
    GotoIfFlagEnabled(Label.L3, flag=4102)
    GotoIfFlagEnabled(Label.L4, flag=4103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    DisableCharacter(character)
    SetTeamType(character, TeamType.NoTeam)
    ForceAnimation(character, 930011)
    if FlagEnabled(1047582700):
        EnableCharacter(character)
    if FlagEnabled(1047582701):
        ForceAnimation(character, 930013)
    if FlagEnabled(1047589205):
        DisableBackread(character)
        DisableCharacter(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(4106))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1047583701)
def Event_1047583701(_, character: uint, entity: uint):
    """Event 1047583701"""
    WaitFrames(frames=1)
    if FlagDisabled(4100):
        return
    if FlagDisabled(4106):
        return
    if FlagEnabled(1047589205):
        return
    if FlagEnabled(1047582700):
        return
    if PlayerNotInOwnWorld():
        MAIN.Await(FlagEnabled(1047582700))
    
        Goto(Label.L1)
    AND_1.Add(ActionButtonParamActivated(action_button_id=6340, entity=entity))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 90008)
    EnableNetworkFlag(1047582700)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.5)
    EnableCharacter(character)
    ForceAnimation(character, 20025)
    End()


@RestartOnRest(1047583702)
def Event_1047583702(_, character: uint):
    """Event 1047583702"""
    WaitFrames(frames=1)
    if FlagDisabled(4100):
        return
    if FlagDisabled(4106):
        return
    if FlagEnabled(1047589205):
        return
    
    MAIN.Await(FlagEnabled(1047589205))
    
    Wait(30.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1047583703)
def Event_1047583703(_, character: uint):
    """Event 1047583703"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(4100):
        return
    if FlagDisabled(4106):
        return
    if FlagEnabled(1047589210):
        return
    if FlagDisabled(1047589205):
        MAIN.Await(CharacterHasSpecialEffect(character, 9600))
    EnableFlag(1047589210)
    End()


@RestartOnRest(1047583704)
def Event_1047583704(_, entity: uint):
    """Event 1047583704"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4100):
        return
    if FlagDisabled(4106):
        return
    if FlagEnabled(1047589205):
        return
    if FlagEnabled(1047582700):
        return
    
    MAIN.Await(FlagEnabled(1047582701))
    
    Wait(3.5)
    ForceAnimation(entity, 20019)
    End()


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005450(0, 1247580400, 1247581400, 1247581410, 1247581418)


@RestartOnRest(1247582350)
def Event_1247582350(_, character: uint, region: uint):
    """Event 1247582350"""
    if FlagEnabled(1247580400):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=10.0))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(1247580400):
        return
    AICommand(character, command_id=10, command_slot=0)
    EnableFlag(1247582350)
    Wait(9.0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Wait(1.0)
    Restart()

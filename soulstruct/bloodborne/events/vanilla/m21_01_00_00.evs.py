"""
linked:
26

strings:
0: PC情報_現実拠点到達時
26: N:\\SPRJ\\data\\Param\\event\\common.emevd
102: 
104: 
106: 
108: 
110: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_12110200(0, obj=2111000, obj_act_id=12110000)
    Event_12110990()
    Event_12110400()
    Event_12110100()
    Event_12110300()
    Event_12110301()
    Event_12110302()
    RunEvent(7000, slot=52, args=(2110950, 2111950, 999, 12117800))
    RunEvent(7100, slot=52, args=(72110200, 2111950))
    RunEvent(7200, slot=52, args=(72110100, 2111950, 2102952))
    RunEvent(7300, slot=52, args=(72102110, 2111950))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableHealthBar(2110700)
    DisableGravity(2110700)
    DisableCharacterCollision(2110700)


@NeverRestart(12110100)
def Event_12110100():
    """Event 12110100"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2110000, entity=2110700))
    
    DisplayDialog(text=10010190, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12110200)
def Event_12110200(_, obj: int, obj_act_id: int):
    """Event 12110200"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(12110300)
def Event_12110300():
    """Event 12110300"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    CreateObjectVFX(2111100, vfx_id=200, model_point=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2110010, entity=2111100))
    
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110800, host_only=False)
    DeleteObjectVFX(2111100)


@NeverRestart(12110301)
def Event_12110301():
    """Event 12110301"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    CreateObjectVFX(2111101, vfx_id=200, model_point=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2110011, entity=2111101))
    
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110810, host_only=False)
    DeleteObjectVFX(2111101)


@NeverRestart(12110302)
def Event_12110302():
    """Event 12110302"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    CreateObjectVFX(2111102, vfx_id=200, model_point=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2110012, entity=2111102))
    
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110000, host_only=False)
    DeleteObjectVFX(2111102)


@NeverRestart(12110400)
def Event_12110400():
    """Event 12110400"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    GotoIfFlagEnabled(Label.L1, flag=9801)
    GotoIfFlagEnabled(Label.L2, flag=9800)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableMapPiece(map_piece_id=2114002)
    DisableMapPiece(map_piece_id=2114000)
    DisableMapPiece(map_piece_id=2114001)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableMapPiece(map_piece_id=2114002)
    EnableMapPiece(map_piece_id=2114000)
    DisableMapPiece(map_piece_id=2114001)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=2114002)
    DisableMapPiece(map_piece_id=2114000)
    EnableMapPiece(map_piece_id=2114001)
    End()


@NeverRestart(12110990)
def Event_12110990():
    """Event 12110990"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    
    MAIN.Await(PlayerStandingOnCollision(2113500))
    
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(achievement_id=12)

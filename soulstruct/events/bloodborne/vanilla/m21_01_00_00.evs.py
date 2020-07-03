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
from soulstruct.events.bloodborne import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(12110200, slot=0, args=(2111000, 12110000))
    RunEvent(12110990)
    RunEvent(12110400)
    RunEvent(12110100)
    RunEvent(12110300)
    RunEvent(12110301)
    RunEvent(12110302)
    RunEvent(7000, slot=52, args=(2110950, 2111950, 999, 12117800))
    RunEvent(7100, slot=52, args=(72110200, 2111950))
    RunEvent(7200, slot=52, args=(72110100, 2111950, 2102952))
    RunEvent(7300, slot=52, args=(72102110, 2111950))


def Preconstructor():
    """ 50: Event 50 """
    DisableHealthBar(2110700)
    DisableGravity(2110700)
    DisableCharacterCollision(2110700)


def Event12110100():
    """ 12110100: Event 12110100 """
    DisableNetworkSync()
    IfBossFogActivated(0, boss_entity_id=2110000, fog_object_id=2110700)
    DisplayDialog(10010190, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


def Event12110200(arg_0_3: int, arg_4_7: int):
    """ 12110200: Event 12110200 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event12110300():
    """ 12110300: Event 12110300 """
    EndIfThisEventOn()
    EndIfClient()
    CreateObjectFX(900201, obj=2111100, model_point=200)
    IfBossFogActivated(0, boss_entity_id=2110010, fog_object_id=2111100)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110800, host_only=False)
    DeleteObjectFX(2111100, erase_root=True)


def Event12110301():
    """ 12110301: Event 12110301 """
    EndIfThisEventOn()
    EndIfClient()
    CreateObjectFX(900201, obj=2111101, model_point=200)
    IfBossFogActivated(0, boss_entity_id=2110011, fog_object_id=2111101)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110810, host_only=False)
    DeleteObjectFX(2111101, erase_root=True)


def Event12110302():
    """ 12110302: Event 12110302 """
    EndIfThisEventOn()
    EndIfClient()
    CreateObjectFX(900201, obj=2111102, model_point=200)
    IfBossFogActivated(0, boss_entity_id=2110012, fog_object_id=2111102)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110000, host_only=False)
    DeleteObjectFX(2111102, erase_root=True)


def Event12110400():
    """ 12110400: Event 12110400 """
    GotoIfFlagOn(Label.L0, 9802)
    GotoIfFlagOn(Label.L1, 9801)
    GotoIfFlagOn(Label.L2, 9800)

    # --- 2 --- #
    DefineLabel(2)
    EnableMapPiece(2114002)
    DisableMapPiece(2114000)
    DisableMapPiece(2114001)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableMapPiece(2114002)
    EnableMapPiece(2114000)
    DisableMapPiece(2114001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(2114002)
    DisableMapPiece(2114000)
    EnableMapPiece(2114001)
    End()


def Event12110990():
    """ 12110990: Event 12110990 """
    EndIfThisEventOn()
    EndIfClient()
    IfStandingOnCollision(0, 2113500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 0, PlayLogMultiplayerType.HostOnly)
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(12)

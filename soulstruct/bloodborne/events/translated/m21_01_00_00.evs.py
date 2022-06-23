"""ABANDONED OLD WORKSHOP

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
from .common_entities import *
from .m21_01_entities import *
# from .common import GainInsight


def Constructor():
    """ 0: Event 0 """
    OpenChest(0, 2111000, 12110000)
    AwardAbandonedOldWorkshopAchievement()
    InitializeMoonPhase()
    InspectDoll()
    GetItemFromStorage()  # Small Hair Ornament
    GetItemFromMemoryAltar()  # Third Umbilical Cord
    GetItemFromOldHunterHeadstone()  # Old Hunter Bone
    RunEvent(7000, slot=52, args=(2110950, 2111950, 999, 12117800))
    RunEvent(7100, slot=52, args=(72110200, 2111950))
    RunEvent(7200, slot=52, args=(72110100, 2111950, 2102952))
    RunEvent(7300, slot=52, args=(72102110, 2111950))


def Preconstructor():
    """ 50: Event 50 """
    DisableHealthBar(Characters.InanimateDoll)
    DisableGravity(Characters.InanimateDoll)
    DisableCharacterCollision(Characters.InanimateDoll)


def InspectDoll():
    """ 12110100: Event 12110100 """
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=2110000, entity=Characters.InanimateDoll)
    DisplayDialog(
        10010190,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 12110200: Event 12110200 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def GetItemFromStorage():
    """ 12110300: Event 12110300 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    CreateObjectVFX(900201, obj=2111100, model_point=200)
    IfActionButtonParam(0, action_button_id=2110010, entity=2111100)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110800, host_only=False)
    DeleteObjectVFX(2111100, erase_root=True)


def GetItemFromMemoryAltar():
    """ 12110301: Event 12110301 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    CreateObjectVFX(900201, obj=2111101, model_point=200)
    IfActionButtonParam(0, action_button_id=2110011, entity=2111101)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110810, host_only=False)
    DeleteObjectVFX(2111101, erase_root=True)


def GetItemFromOldHunterHeadstone():
    """ 12110302: Event 12110302 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    CreateObjectVFX(900201, obj=2111102, model_point=200)
    IfActionButtonParam(0, action_button_id=2110012, entity=2111102)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2110000, host_only=False)
    DeleteObjectVFX(2111102, erase_root=True)


def InitializeMoonPhase():
    """ 12110400: Event 12110400 """
    GotoIfFlagEnabled(Label.L0, CommonFlags.BloodMoonPhase)
    GotoIfFlagEnabled(Label.L1, CommonFlags.NightPhase)
    GotoIfFlagEnabled(Label.L2, CommonFlags.EveningPhase)

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


def AwardAbandonedOldWorkshopAchievement():
    """ 12110990: Event 12110990 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfStandingOnCollision(0, Collisions.CollisionForAchievement)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 0, PlayLogMultiplayerType.HostOnly)
    RunEvent(9350, 0, args=(2,))
    AwardAchievement(Achievements.DiscoveredAbandonedOldWorkshop)

"""
West Altus Plateau (SE) (NE)

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
from .enums.m60_39_53_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=76350, asset=Assets.AEG099_060_9000, enemy_block_distance=5.0, character=0)
    CommonFunc_90005100(
        0,
        flag=71602,
        flag_1=76350,
        asset=Assets.AEG099_060_9001,
        source_flag=77350,
        value=1,
        flag_2=78350,
        flag_3=78351,
        flag_4=78352,
        flag_5=78353,
        flag_6=78354,
        flag_7=78355,
        flag_8=78356,
        flag_9=78357,
        flag_10=78358,
        flag_11=78359,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellSoldier1,
        region=1039532350,
        radius=60.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MadPumpkinHead,
        animation_id=30005,
        animation_id_1=20005,
        region=1039532360,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1039532400()
    Event_1039532650()
    Event_1039532660()
    Event_1039532600()
    Event_1039532610()
    Event_1039532300()
    Event_1039532670()
    RegisterLadder(start_climbing_flag=1039530580, stop_climbing_flag=1039530581, asset=Assets.AEG110_119_2000)
    CommonFunc_90005795(
        0,
        flag=7603,
        flag_1=0,
        flag_2=1039539200,
        left_flag=1039532141,
        cancel_flag__right_flag=1039532142,
        message=80603,
        action_button_id=9000,
        asset=Assets.AEG099_090_9002,
        vfx_id=30010,
    )
    if CeremonyActive(ceremony=20):
        CommonFunc_90005796(0, flag=7603, character=Characters.RileightheIdle, banner_type=5, region=1039532141)
        Event_1039532145()
    Event_1039533700()
    CommonFunc_90005774(0, flag=7603, item_lot=1039530700, flag_1=1039537700)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.RileightheIdle)


@ContinueOnRest(100)
def Event_100():
    """Event 100"""
    Event_1039532500()


@RestartOnRest(1039532145)
def Event_1039532145():
    """Event 1039532145"""
    if CeremonyInactive(ceremony=20):
        return
    EnableBackread(Characters.RileightheIdle)
    SetTeamType(Characters.RileightheIdle, TeamType.Human)
    DeleteAssetVFX(1039536700)
    CreateAssetVFX(1039536700, dummy_id=200, vfx_id=806700)


@RestartOnRest(1039532300)
def Event_1039532300():
    """Event 1039532300"""
    if ThisEventSlotFlagEnabled():
        return
    EnableAssetInvulnerability(Assets.AEG110_302_2002)
    EnableThisNetworkSlotFlag()


@RestartOnRest(1039532400)
def Event_1039532400():
    """Event 1039532400"""
    GotoIfFlagEnabled(Label.L0, flag=1039530510)
    DisableAsset(1039536400)
    DisableAsset(Assets.AEG099_630_9000)
    DisableTreasure(asset=1039533501)
    DisableAsset(Assets.AEG099_620_9000)
    DisableTreasure(asset=1039533502)
    AND_1.Add(FlagEnabled(1039530655))
    AND_1.Add(FlagEnabled(1039520655))
    AND_1.Add(FlagEnabled(1040530655))
    AND_1.Add(AllPlayersOutsideRegion(region=1039532260))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1039530510)
    Wait(2.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(1039536400)
    EnableAsset(Assets.AEG099_630_9000)
    EnableTreasure(asset=1039533501)
    EnableAsset(Assets.AEG099_620_9000)
    EnableTreasure(asset=1039533502)
    End()


@RestartOnRest(1039532500)
def Event_1039532500():
    """Event 1039532500"""
    GotoIfFlagEnabled(Label.L0, flag=1039530505)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=Assets.AEG008_263_2000, radius=100.0))
    
    EnableNetworkFlag(1039530505)
    CreateTemporaryVFX(vfx_id=806850, anchor_entity=Assets.AEG008_263_2000, anchor_type=CoordEntityType.Asset)
    ForceAnimation(Assets.AEG008_263_2000, 1, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG008_263_2000)
    Wait(1.0)
    Restart()


@RestartOnRest(1039532600)
def Event_1039532600():
    """Event 1039532600"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9210, entity=Assets.AEG099_004_9001))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=60031, anchor_entity=Assets.AEG099_004_9001, number_buttons=NumberButtons.OneButton)
    if FlagDisabled(1039537080):
        AwardItemLot(1039530080, host_only=True)
    Wait(1.0)
    Restart()


@RestartOnRest(1039532610)
def Event_1039532610():
    """Event 1039532610"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1039537080):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1039537080))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    DisplayDialog(text=30101, display_distance=5.0, button_type=ButtonType.Yes_or_No)


@RestartOnRest(1039532650)
def Event_1039532650():
    """Event 1039532650"""
    GotoIfFlagEnabled(Label.L0, flag=1039530655)
    DisableAsset(Assets.AEG003_316_9001)
    DeleteVFX(1039532650, erase_root_only=False)
    
    MAIN.Await(FlagEnabled(1039530505))
    
    EnableAsset(Assets.AEG003_316_9001)
    CreateVFX(1039532650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG003_316_9001)
    DeleteVFX(1039532650, erase_root_only=False)
    End()


@RestartOnRest(1039532660)
def Event_1039532660():
    """Event 1039532660"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1039530655):
        return
    AND_1.Add(FlagEnabled(1039530505))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1039532651))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9521, entity=Assets.AEG003_316_9001))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1039530655)
    DisableAsset(Assets.AEG003_316_9001)
    FaceEntityAndForceAnimation(PLAYER, Assets.AEG003_316_9001, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.0)
    PlaySoundEffect(1039532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1039532650)
    End()


@RestartOnRest(1039532670)
def Event_1039532670():
    """Event 1039532670"""
    AwaitFlagEnabled(flag=1039530510)
    MoveRemains(source_region=1039532270, destination_region=1039532272)
    MoveRemains(source_region=1039532271, destination_region=1039532272)


@RestartOnRest(1039533700)
def Event_1039533700():
    """Event 1039533700"""
    WaitFrames(frames=1)
    if FlagDisabled(400074):
        return
    EnableFlag(1039539200)
    End()

"""
Liurnia to Altus Plateau (SE) (SE)

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
from .enums.m60_39_48_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""

    # --- Label 0 --- #
    DefineLabel(0)
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, dummy_id=100, vfx_id=800, right=1039488600)
    Event_1039482510()
    CommonFunc_90005501(
        0,
        flag=1039480510,
        flag_1=1039480511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        asset_2=Assets.AEG099_182_2000,
        flag_2=1039480512,
    )
    Event_1039482610()
    Event_1039482611()
    CommonFunc_90005300(0, flag=1039480340, character=Characters.LiurniaTroll, item_lot=0, seconds=0.0, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1039480519()
    CommonFunc_90005251(0, character=Characters.GravenSchool, radius=10.0, seconds=0.0, animation_id=1700)


@RestartOnRest(1039482510)
def Event_1039482510():
    """Event 1039482510"""
    CommonFunc_90005500(
        0,
        flag=1039480510,
        flag_1=1039480511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        obj_act_id=1039483511,
        asset_2=Assets.AEG099_182_2000,
        obj_act_id_1=1039483512,
        region=1039482511,
        region_1=1039482512,
        flag_2=1039480512,
        flag_3=1039480513,
        left_1=0,
    )


@ContinueOnRest(1039480519)
def Event_1039480519():
    """Event 1039480519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1039480510)
    EnableThisSlotFlag()


@RestartOnRest(1039482610)
def Event_1039482610():
    """Event 1039482610"""
    GotoIfFlagDisabled(Label.L0, flag=1039480610)
    DisableAsset(Assets.AEG099_251_2000)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    CreateAssetVFX(Assets.AEG099_251_2000, dummy_id=200, vfx_id=1502)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1039480610))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 485))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 486))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1039480610)
    DisplayDialog(text=20210, display_distance=5.0)
    PlaySoundEffect(Assets.AEG099_251_2000, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(Assets.AEG099_251_2000)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    End()


@RestartOnRest(1039482611)
def Event_1039482611():
    """Event 1039482611"""
    DisableNetworkSync()
    if FlagEnabled(1039480610):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=Assets.AEG099_251_2000))
    OR_1.Add(FlagEnabled(1039480610))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1039480610):
        return
    DisplayDialog(text=20200, anchor_entity=Assets.AEG099_251_2000)
    Wait(1.0)
    Restart()

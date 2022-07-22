"""
Regal Ancestor (Lower)

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
from .entities.m12_08_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_12082849()
    Event_12082800()
    Event_12082810()
    Event_12082848()


@ContinueOnRest(12082848)
def Event_12082848():
    """Event 12082848"""
    GotoIfFlagEnabled(Label.L0, flag=12080800)
    DeleteAssetVFX(Assets.AEG099_065_9000, erase_root=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(12080800))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(Assets.AEG099_065_9000)
    CreateAssetVFX(Assets.AEG099_065_9000, vfx_id=190, model_point=1300)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9526, entity=Assets.AEG099_065_9000))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(PLAYER, 60460)
    Wait(2.5)
    SetRespawnPoint(respawn_point=12022200)
    SaveRequest()
    WarpToMap(game_map=SIOFRA_RIVER, player_start=12022200)


@ContinueOnRest(12082800)
def Event_12082800():
    """Event 12082800"""
    if FlagEnabled(12080800):
        return
    
    MAIN.Await(HealthRatio(Characters.AncestorSpirit) <= 0.0)
    
    Wait(2.0)
    PlaySoundEffect(Characters.AncestorSpirit, 77777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.AncestorSpirit))
    
    KillBossAndDisplayBanner(character=Characters.AncestorSpirit, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(12080800)
    EnableFlag(9132)
    if PlayerInOwnWorld():
        EnableFlag(61132)


@RestartOnRest(12082810)
def Event_12082810():
    """Event 12082810"""
    GotoIfFlagDisabled(Label.L0, flag=12080800)
    DisableCharacter(Characters.AncestorSpirit)
    DisableAnimations(Characters.AncestorSpirit)
    Kill(Characters.AncestorSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.AncestorSpirit)
    AND_2.Add(FlagEnabled(12082805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12082800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.AncestorSpirit)
    SetNetworkUpdateRate(Characters.AncestorSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.AncestorSpirit, name=904670000)


@ContinueOnRest(12082849)
def Event_12082849():
    """Event 12082849"""
    CommonFunc_9005800(
        0,
        flag=12080800,
        entity=Assets.AEG099_002_9000,
        region=12082800,
        flag_1=12082805,
        character=12085800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=12080800,
        entity=Assets.AEG099_002_9000,
        region=12082800,
        flag_1=12082805,
        flag_2=12082806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=12080800, asset=Assets.AEG099_002_9000, model_point=8, right=0)
    CommonFunc_9005822(0, 12080800, 467000, 12082805, 12082806, 0, 12082802, 0, 0)

"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_12082849()
    Event_12082800()
    Event_12082810()
    Event_12082848()


@NeverRestart(12082848)
def Event_12082848():
    """Event 12082848"""
    GotoIfFlagEnabled(Label.L0, flag=12080800)
    DeleteObjectVFX(12081848, erase_root=False)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 12080800)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(12081848)
    CreateObjectVFX(12081848, vfx_id=190, model_point=1300)
    IfTryingToJoinSession(OR_2)
    IfTryingToCreateSession(OR_2)
    IfConditionFalse(AND_2, input_condition=OR_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9526, entity=12081848)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(PLAYER, 60460, unknown2=1.0)
    Wait(2.5)
    SetRespawnPoint(respawn_point=12022200)
    SaveRequest()
    WarpToMap(game_map=SIOFRA_RIVER, player_start=12022200)


@NeverRestart(12082800)
def Event_12082800():
    """Event 12082800"""
    EndIfFlagEnabled(12080800)
    IfHealthRatioLessThanOrEqual(MAIN, 12080800, value=0.0)
    Wait(2.0)
    PlaySoundEffect(12080800, 77777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 12080800)
    KillBossAndDisplayBanner(character=12080800, banner_type=BannerType.Unknown)
    EnableFlag(12080800)
    EnableFlag(9132)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61132)


@RestartOnRest(12082810)
def Event_12082810():
    """Event 12082810"""
    GotoIfFlagDisabled(Label.L0, flag=12080800)
    DisableCharacter(12080800)
    DisableAnimations(12080800)
    Kill(12080800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12080800)
    IfFlagEnabled(AND_2, 12082805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=12082800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(12080800)
    SetNetworkUpdateRate(12080800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(12080800, name=904670000)


@NeverRestart(12082849)
def Event_12082849():
    """Event 12082849"""
    RunCommonEvent(
        0,
        9005800,
        args=(12080800, 12081800, 12082800, 12082805, 12085800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(12080800, 12081800, 12082800, 12082805, 12082806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(12080800, 12081800, 8, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(12080800, 467000, 12082805, 12082806, 0, 12082802, 0, 0), arg_types="IiIIIIii")

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
    RunCommonEvent(0, 90005211, args=(1048510202, 30001, 20001, 0, 0.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005476, args=(1048510800, 1048510810), arg_types="II")
    Event_1048512820(0, character=1048510800, character_1=1048510810)
    RunCommonEvent(0, 90005871, args=(1048510800, 903150607, 10, 1048510810), arg_types="IiII")
    RunCommonEvent(0, 1048512800, args=(1048510800, 0, 1048510800, 0, 1048510700, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1048510800, 10, 0), arg_types="III")


@RestartOnRest(1048512800)
def Event_1048512800(
    _,
    flag: uint,
    left: uint,
    character: uint,
    left_1: uint,
    item_lot__item_lot_param_id: int,
    seconds: float,
):
    """Event 1048512800"""
    SkipLinesIfValueEqual(1, left=item_lot__item_lot_param_id, right=0)
    Unknown_2004_76(flag=flag, item_lot=item_lot__item_lot_param_id)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(1048510810)
    DisableAnimations(1048510810)
    Kill(1048510810)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(1.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthValueLessThanOrEqual(MAIN, character, value=0)
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, character)
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DutyFulfilled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.Unknown)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaLoss)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaWin)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(5.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()
    Wait(seconds)


@RestartOnRest(1048512820)
def Event_1048512820(_, character: uint, character_1: uint):
    """Event 1048512820"""
    IfCharacterAlive(AND_1, character)
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    IfCharacterHasSpecialEffect(AND_2, character, 11825)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfCharacterBackreadEnabled(AND_3, character_1)
    IfConditionTrue(MAIN, input_condition=AND_3)
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterBackreadDisabled(AND_4, character_1)
    IfConditionTrue(MAIN, input_condition=AND_4)
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()

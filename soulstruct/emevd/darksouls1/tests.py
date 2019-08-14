from soulstruct.emevd.shared.tests import *
import soulstruct.emevd.darksouls1.instructions as instr
import soulstruct.game_types as gt


HOST = ConstantCondition(
    if_true_func=instr.IfHost,
    skip_if_true_func=instr.SkipLinesIfHost,
    end_if_true_func=instr.EndIfHost,
    restart_if_true_func=instr.RestartIfHost,
)

CLIENT = ConstantCondition(
    if_true_func=instr.IfClient,
    skip_if_true_func=instr.SkipLinesIfClient,
    end_if_true_func=instr.EndIfClient,
    restart_if_true_func=instr.RestartIfClient,
)

SINGLEPLAYER = ConstantCondition(
    if_true_func=instr.IfSingleplayer,
    skip_if_true_func=instr.SkipLinesIfSingleplayer,
    end_if_true_func=instr.EndIfSingleplayer,
    restart_if_true_func=instr.RestartIfSingleplayer,
)

MULTIPLAYER = ConstantCondition(
    if_true_func=instr.IfMultiplayer,
    skip_if_true_func=instr.SkipLinesIfMultiplayer,
    end_if_true_func=instr.EndIfMultiplayer,
    restart_if_true_func=instr.RestartIfMultiplayer,
)

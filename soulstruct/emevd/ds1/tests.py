from soulstruct.emevd.shared.tests import *
from soulstruct.emevd.ds1.instructions import *


_HOST = ConstantCondition(
    if_true_func=IfHost,
    skip_if_true_func=SkipLinesIfHost,
    end_if_true_func=EndIfHost,
    restart_if_true_func=RestartIfHost,
)

_CLIENT = ConstantCondition(
    if_true_func=IfClient,
    skip_if_true_func=SkipLinesIfClient,
    end_if_true_func=EndIfClient,
    restart_if_true_func=RestartIfClient,
)

_SINGLEPLAYER = ConstantCondition(
    if_true_func=IfSingleplayer,
    skip_if_true_func=SkipLinesIfSingleplayer,
    end_if_true_func=EndIfSingleplayer,
    restart_if_true_func=RestartIfSingleplayer,
)

_MULTIPLAYER = ConstantCondition(
    if_true_func=IfMultiplayer,
    skip_if_true_func=SkipLinesIfMultiplayer,
    end_if_true_func=EndIfMultiplayer,
    restart_if_true_func=RestartIfMultiplayer,
)


# TODO
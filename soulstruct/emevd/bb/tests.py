from soulstruct.emevd.shared.tests import *
from soulstruct.emevd.bb.instructions import *


def __no_skip_or_negate_or_terminate(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if negate:
            raise NoNegateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, **kwargs)

    return decorated


def __negate_only(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, negate=negate, **kwargs)

    return decorated


def __skip_and_negate_and_terminate(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, skip_lines=skip_lines, negate=negate, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if condition not in range(-7, 8):
                raise ValueError("Condition register index must be in range [-7, 7], inclusive.")
            return func(*args, condition=condition, negate=negate, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, end_event=True, negate=negate, **kwargs)

        if restart_event:
            return func(*args, restart_event=True, negate=negate, **kwargs)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    return decorated


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


@__no_skip_or_negate_or_terminate
def _IsAttackedWithDamageType(attacked_entity, attacking_character, damage_type, condition):
    return IfDamageType(condition, attacked_entity, attacking_character, damage_type)


@__no_skip_or_negate_or_terminate
def _WearingArmorTypeInRange(armor_type, required_armor_range_first, required_armor_range_last, condition):
    return IfPlayerArmorType(condition, armor_type, required_armor_range_first, required_armor_range_last)


@__no_skip_or_negate_or_terminate
def _CharacterDrawGroupActive(character, condition):
    return IfCharacterDrawGroupActive(condition, character)


@__no_skip_or_negate_or_terminate
def _CharacterDrawGroupInactive(character, condition):
    return IfCharacterDrawGroupInactive(condition, character)


@__negate_only
def _INSIGHT(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfPlayerInsightAmountComparison(condition, comparison_value, comparison_type)

from soulstruct.emevd.shared.tests import *
from soulstruct.emevd.ds3.instructions import *


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

_IN_OWN_WORLD = ConstantCondition(
    if_true_func=IfPlayerInOwnWorld,
    if_false_func=IfPlayerNotInOwnWorld,
    end_if_true_func=EndIfPlayerInOwnWorld,
    end_if_false_func=EndIfPlayerNotInOwnWorld,
    restart_if_true_func=RestartIfPlayerInOwnWorld,
    restart_if_false_func=RestartIfPlayerNotInOwnWorld,
)


@__no_skip_or_negate_or_terminate
def _ActionButtonInRegion(action_button_id, region, condition):
    return IfActionButtonInRegion(condition, action_button_id, region)


@__no_skip_or_negate_or_terminate
def _IsAttackedWithDamageType(attacked_entity, attacking_character, damage_type, condition):
    return IfDamageType(condition, attacked_entity, attacking_character, damage_type)


@__no_skip_or_negate_or_terminate
def _CharacterDrawGroupActive(character, condition):
    return IfCharacterDrawGroupActive(condition, character)


@__no_skip_or_negate_or_terminate
def _CharacterDrawGroupInactive(character, condition):
    return IfCharacterDrawGroupInactive(condition, character)

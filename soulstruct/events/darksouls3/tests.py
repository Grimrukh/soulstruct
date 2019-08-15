from soulstruct.events.core import no_skip_or_negate_or_terminate, ConstantCondition
from soulstruct.events.shared.tests import *
import soulstruct.events.darksouls3.instructions as instr
from soulstruct.enums.darksouls3 import *


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

IN_OWN_WORLD = ConstantCondition(
    if_true_func=instr.IfPlayerInOwnWorld,
    if_false_func=instr.IfPlayerNotInOwnWorld,
    end_if_true_func=instr.EndIfPlayerInOwnWorld,
    end_if_false_func=instr.EndIfPlayerNotInOwnWorld,
    restart_if_true_func=instr.RestartIfPlayerInOwnWorld,
    restart_if_false_func=instr.RestartIfPlayerNotInOwnWorld,
)


@no_skip_or_negate_or_terminate
def ActionButtonInRegion(action_button_id: int, region: gt.RegionInt, condition: int):
    return instr.IfActionButtonInRegion(condition, action_button_id, region)


@no_skip_or_negate_or_terminate
def IsAttackedWithDamageType(attacked_entity: gt.AnimatedInt, attacking_character: gt.CharacterInt,
                             damage_type: DamageType, condition: int):
    return instr.IfDamageType(condition, attacked_entity, attacking_character, damage_type)


@no_skip_or_negate_or_terminate
def CharacterDrawGroupActive(character: gt.CharacterInt, condition: int):
    return instr.IfCharacterDrawGroupActive(condition, character)


@no_skip_or_negate_or_terminate
def CharacterDrawGroupInactive(character: gt.CharacterInt, condition: int):
    return instr.IfCharacterDrawGroupInactive(condition, character)

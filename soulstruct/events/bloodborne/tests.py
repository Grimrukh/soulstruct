from soulstruct.events.core import no_skip_or_negate_or_terminate, negate_only, \
    ConstantCondition, COMPARISON_NODES, NEG_COMPARISON_NODES
from soulstruct.events.shared.tests import *
import soulstruct.events.bloodborne.instructions as instr
from soulstruct.enums.bloodborne import *


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


@no_skip_or_negate_or_terminate
def IsAttackedWithDamageType(attacked_entity: gt.AnimatedInt, attacking_character: gt.CharacterInt,
                             damage_type: DamageType, condition: int):
    return instr.IfDamageType(condition, attacked_entity, attacking_character, damage_type)


@no_skip_or_negate_or_terminate
def WearingArmorTypeInRange(armor_type: ArmorType, required_armor_range_first: int, required_armor_range_last: int,
                            condition: int):
    return instr.IfPlayerArmorType(condition, armor_type, required_armor_range_first, required_armor_range_last)


@no_skip_or_negate_or_terminate
def CharacterDrawGroupActive(character: gt.CharacterInt, condition: int):
    return instr.IfCharacterDrawGroupActive(condition, character)


@no_skip_or_negate_or_terminate
def CharacterDrawGroupInactive(character: gt.CharacterInt, condition: int):
    return instr.IfCharacterDrawGroupInactive(condition, character)


@negate_only
def INSIGHT(op_node, comparison_value, condition: int, negate: bool = False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfPlayerInsightAmountComparison(condition, comparison_value, comparison_type)

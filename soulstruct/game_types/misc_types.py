from enum import IntEnum
from .basic_types import GameObject


class BaseAIScript(GameObject, IntEnum):
    """Base type for Logic and Battle scripts."""


class LogicAIScript(BaseAIScript):
    """Script that governs a character outside of battle."""


class BattleAIScript(BaseAIScript):
    """Script that governs a character in battle."""

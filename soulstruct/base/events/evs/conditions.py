from __future__ import annotations

__all__ = [
    "ConditionGroupState",
    "EVSConditionManager",
]

import ast
from dataclasses import dataclass, field

from .exceptions import ConditionNameError, ConditionLimitError


@dataclass(slots=True)
class ConditionGroupState:
    """Stores the state of a condition group, including its name and whether it is held or not."""

    # True internal index of condition. Matches indexing into `EVSConditionManager.conditions`.
    index: int

    # Variable name assigned to condition; non-empty implies condition has been used. Underscore '_' indicates condition
    # has been checked out automatically, i.e. the caller will not see it.
    name: str = ""

    # Enabled by the EVS `COMPILE` function whenever a test of any kind (including another condition group) is added to
    # this condition group. This informs us that 'old' will be enabled later and a valid 'Last Result' available.
    # Disabled across ALL conditions whenever a 'frame-ending' instruction like `MAIN.Await()` or `Wait()` is called.
    _active: bool = False

    # Condition group has been evaluated due to a previous Wait/Await instruction (or a few others that I'm still
    # tracking down). Its 'Last Result' will be available and it will only be used again automatically if not `held`.
    _stale: bool = False  # condition group has been evaluated due to a previous Wait/Await instruction

    # If enabled, caller has requested that condition NOT be automatically re-used in compilation, even when stale.
    # Used to guarantee post-evaluation access with '...IfLastConditionResult...' instructions.
    held: bool = False

    # Condition groups that have been loaded into this one. EVS users are free to repeatedly load the same condition
    # group into multiple other condition groups, but this is not tracked here (we just use a set).
    children: set[ConditionGroupState] = field(default_factory=set)

    @property
    def active(self):
        return self._active

    @property
    def stale(self):
        return self._stale

    def reset(self):
        """Called ONLY at the start of compiling a new `Event`, which wants fresh condition groups."""
        self.name = ""
        self._active = False
        self._stale = False
        self.held = False
        self.children = set()

    def activate(self):
        self._stale = False
        self._active = True

    def activate_with_child(self, condition: ConditionGroupState):
        self.children.add(condition)
        self.activate()

    def deactivate(self):
        """Called when a 'frame-ending' instruction like `MAIN.Await()` or `Wait()` is called.

        Does not touch `held`, which cannot be disabled (per event) once enabled. That will simply prevent the stale
        condition from being checked out automatically while compiling high-level syntax like `if/else`.
        """
        if self._active:
            self._active = False
            self._stale = True  # 'Last Result' will be available for appropriate SkipLines/Goto/Return instructions
        self.children.clear()

    def __hash__(self):
        return hash(self.index)

    def __eq__(self, other: ConditionGroupState):
        return self.index == other.index

    def __repr__(self):
        """For appearance in numeric EMEVD."""
        return f"{self.index}"


class EVSConditionManager:

    # Current event ID.
    event_id: int

    # Managed condition slots.
    conditions: list[ConditionGroupState]
    # Sub-lists of conditions for quick access.
    or_conditions: list[ConditionGroupState]  # negative indices
    and_conditions: list[ConditionGroupState]  # positive indices
    
    # Enabled when the very last instruction was `MAIN.Await()`, so back-to-back Awaits() can be used without warning
    # about stale conditions (rarely useful).
    just_awaited_main: bool

    def __init__(self, or_slots: list[int], and_slots: list[int]):
        self.event_id = -1
        self.conditions = [
            ConditionGroupState(index=0)  # dummy MAIN condition (0) for indexing consistency
        ] + [
            ConditionGroupState(index=and_slot) for and_slot in sorted(and_slots)  # least to most position
        ] + [
            ConditionGroupState(index=or_slot) for or_slot in sorted(or_slots)  # most to least negative
        ]
        self.just_awaited_main = False

        self.or_conditions = [c for c in self.conditions if c.index < 0]
        self.and_conditions = [c for c in self.conditions if c.index > 0]

    @property
    def MAIN(self):
        return self.conditions[0]

    def __getitem__(self, name_or_index: str | int | ConditionGroupState) -> ConditionGroupState:
        if isinstance(name_or_index, ConditionGroupState):
            # May already have been resolved before passing to internal compiler.
            return name_or_index

        if isinstance(name_or_index, int):
            return self.conditions[name_or_index]

        if isinstance(name_or_index, str):
            for condition in self.conditions:
                if condition.name == name_or_index:
                    return condition
            raise KeyError(f"No condition named '{name_or_index}'.")

        raise TypeError(f"Condition name or index must be an integer or string, not {type(name_or_index).__name__}.")

    @property
    def names(self) -> set[str]:
        return {c.name for c in self.conditions}

    def deactivate_all(self):
        """Called when a 'frame-ending' instruction like `MAIN.Await()` or `Wait()` is called.

        Note that these 'frame-ending' instructions nuke all condition groups equally -- not just ones that have been
        added to other conditions, or to MAIN. So we don't need to check or use `children`.
        """
        for condition in self.conditions:
            condition.deactivate()

    def reset(self, event_id: int):
        """Reset for every new event."""
        self.event_id = event_id
        for condition in self.conditions:
            condition.reset()

    def check_out_OR(self, node: ast.AST, event_id: int, name="_", hold=False) -> ConditionGroupState:
        """Automatically check out the next available OR condition group index (closest to 0)."""
        return self._check_out(node, event_id, name, hold, "OR", self.or_conditions)

    def check_out_AND(self, node: ast.AST, event_id: int, name="_", hold=False) -> ConditionGroupState:
        """Automatically check out the next available AND condition group index (closest to 0)."""
        return self._check_out(node, event_id, name, hold, "AND", self.and_conditions)

    def _check_out(
        self, node, event_id: int, name: str, hold: bool, bool_type: str, conditions: list[ConditionGroupState]
    ) -> ConditionGroupState:
        if name != "_" and name in self.names:
            raise ConditionNameError(node, f"A condition named '{name}' already exists in this event.")

        for cond in conditions:
            if cond.name == "":
                # This OR slot is free.
                cond.name = name
                cond.held = hold
                return cond

        # Failed to find a completely unused (unnamed) condition, so get a non-held 'stale' one.
        # Its usage as an output condition (by the caller) will clear the 'stale' flag.
        for cond in conditions:
            if cond.stale and not cond.held:
                # Condition is stale and NOT held, and so is available for re-use.
                # TODO: Clear stale flag here? Is this condition always going to be an output?
                cond.name = name
                cond.held = hold
                return cond

        raise ConditionLimitError(
            node,
            f"No available or stale {bool_type} conditions left in event {event_id}.\n"
            "You may need to manage conditions manually or change your logic."
        )

    def check_out_TEMP(self, lineno: int, event_id: int) -> ConditionGroupState:
        """Check out highest-magnitude condition of either OR type (preferred) or AND type for temporary use (e.g when
        a simple skip cannot be used in a one-line IF statement, like 'if HealthRatio(PLAYER) <= 0: ...').

        This serves no purpose other than a convention (started by FromSoft themselves) to distinguish temporary
        one-test conditions from meaningful conditions containing multiple tests.
        """
        highest_mag_condition = max(abs(cond.index) for cond in self.conditions)
        if highest_mag_condition == 0:
            raise ConditionLimitError(
                lineno,
                f"No conditions available in event {event_id} to check out a temporary condition.",
            )

        cond = self.conditions[highest_mag_condition]
        cond.name = "_"
        return cond

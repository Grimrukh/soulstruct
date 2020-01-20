from functools import wraps

from soulstruct.core import SoulstructError
from soulstruct.utilities import word_wrap

__all__ = ["SoulstructProjectError", "error_as_dialog", "ActionHistory", "bind_events"]


class SoulstructProjectError(SoulstructError):
    pass


def bind_events(widget, bindings: dict):
    for event, func in bindings.items():
        widget.bind(event, func)


def error_as_dialog(window, func):
    @wraps(func)
    def window_method(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except SoulstructProjectError as e:
            window.CustomDialog(
                title="Runtime Manager Error",
                message=word_wrap(str(e), 50),
            )
        except Exception as e:
            window.CustomDialog(
                title="Unknown Internal Error",
                message="Internal Error:\n\n" + word_wrap(str(e), 50) + "\n\nPlease report this error.",
            )

    return window_method


class ActionHistory(object):
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def record_action(self, undo, redo):
        """Record the undo and redo callbacks (no arguments) for an action."""
        if not callable(undo) or not callable(redo):
            raise TypeError("Action and inverse action functions must be callable, with no arguments.")
        self._undo_stack.append((undo, redo))
        self._redo_stack = []  # old timeline dies

    def undo(self, _=None):
        if self._undo_stack:
            undo, redo = self._undo_stack.pop()
            undo(from_history=True)
            self._redo_stack.append((undo, redo))
            return True
        else:
            return False

    def redo(self, _=None):
        if self._redo_stack:
            undo, redo = self._redo_stack.pop()
            redo(from_history=True)
            self._undo_stack.append((undo, redo))
            return True
        else:
            return False

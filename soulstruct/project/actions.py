
__all__ = ['ActionHistory']


class ActionHistory(object):
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def record_action(self, undo, redo):
        """Record the undo and redo callbacks (no arguments) for an action."""
        if not callable(undo) or not callable(redo):
            raise TypeError("Action and inverse action functions must be callable, with no arguments.")
        self._undo_stack.append((undo, redo))

    def undo(self, _=None):
        if self._undo_stack:
            undo, redo = self._undo_stack.pop()
            undo(record_action=False)
            self._redo_stack.append((undo, redo))
            return True
        else:
            return False

    def redo(self, _=None):
        if self._redo_stack:
            undo, redo = self._redo_stack.pop()
            redo(record_action=False)
            self._undo_stack.append((undo, redo))
            return True
        else:
            return False

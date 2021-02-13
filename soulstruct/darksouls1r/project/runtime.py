__all__ = ["RuntimeManager"]

from soulstruct.base.project.runtime import RuntimeManager as _BaseRuntimeManager
from soulstruct.utilities.memory import DSRMemoryHook


class RuntimeManager(_BaseRuntimeManager):
    HOOK_CLASS = DSRMemoryHook

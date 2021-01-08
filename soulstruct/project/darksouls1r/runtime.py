__all__ = ["RuntimeManager"]

from soulstruct.project.base.runtime import RuntimeManager as _BaseRuntimeManager
from soulstruct.utilities.memory import DSRMemoryHook


class RuntimeManager(_BaseRuntimeManager):
    HOOK_CLASS = DSRMemoryHook

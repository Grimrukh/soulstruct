__all__ = ["RuntimeManager"]

from soulstruct.project.base.runtime import RuntimeManager as _BaseRuntimeManager


class RuntimeManager(_BaseRuntimeManager):
    HOOK_CLASS = None  # no hook for PTDE

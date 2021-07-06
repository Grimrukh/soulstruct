__all__ = ["RuntimeManager"]

from soulstruct.base.project.runtime import RuntimeManager as _BaseRuntimeManager
from soulstruct.utilities.memory import DSRMemoryHook


class RuntimeManager(_BaseRuntimeManager):
    HOOK_CLASS = DSRMemoryHook

    _hook: DSRMemoryHook

    def inject_draw_param(self, draw_param, area_id: int, slot=0):
        if self._hook is None:
            raise ConnectionError("Memory hook has not been created.")
        return self._hook.write_draw_param_to_memory(draw_param, area_id, slot)

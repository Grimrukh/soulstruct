__all__ = ["RuntimeManager"]

import typing as tp

from soulstruct.base.project.runtime import RuntimeManager as _BaseRuntimeManager
from soulstruct.utilities.memory import DSRMemoryHook


class RuntimeManager(_BaseRuntimeManager):
    HOOK_CLASS = DSRMemoryHook

    _hook: DSRMemoryHook

    def inject_draw_param(self, draw_param, area_id: int, slot=0):
        if self._hook is None:
            raise ConnectionError("Memory hook has not been created.")
        return self._hook.write_draw_param_to_memory(draw_param, area_id, slot)

    def get_current_map_id(self) -> tp.Optional[tp.Tuple[int, int, int, int]]:
        if self._hook is None:
            raise ConnectionError("Memory hook has not been created.")
        current_map = self._hook.get("current_map")
        if current_map == (255, 255, 255, 255):
            return None
        return tuple(current_map[::-1])

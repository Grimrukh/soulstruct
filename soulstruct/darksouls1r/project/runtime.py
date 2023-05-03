from __future__ import annotations

__all__ = ["RuntimeManager"]

import logging
import typing as tp

from soulstruct.base.project.runtime import RuntimeManager as _BaseRuntimeManager
from soulstruct.darksouls1r.utilities.memory import DSRMemoryHook, MemoryDrawParam

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.params.draw_param import DrawParam
    from .core import GameDirectoryProject

_LOGGER = logging.getLogger(__name__)


class RuntimeManager(_BaseRuntimeManager):
    HOOK_CLASS = DSRMemoryHook

    _hook: DSRMemoryHook

    memory_draw_params: dict[tuple[str, int, bool], MemoryDrawParam]

    def __init__(self, project: GameDirectoryProject, master=None, toplevel=False):
        super().__init__(project, master=master, toplevel=toplevel)
        self.memory_draw_params = {}

    def inject_draw_param(self, draw_param: DrawParam, draw_param_stem: str, area_id: int, is_extra_slot=False):
        if self._hook is None:
            raise ConnectionError("Memory hook has not been created.")

        if (draw_param_stem, area_id, is_extra_slot) not in self.memory_draw_params:
            _LOGGER.info(
                f"Creating new `MemoryDrawParam` for: ({draw_param_stem}, {area_id}, isextra_slots={is_extra_slot})")
            self.memory_draw_params[draw_param_stem, area_id, is_extra_slot] = self._hook.get_memory_draw_param(
                draw_param.ROW_TYPE, draw_param_stem, area_id, is_extra_slot
            )
            self.memory_draw_params[draw_param_stem, area_id, is_extra_slot].read_from_memory()

        self.memory_draw_params[draw_param_stem, area_id, is_extra_slot].set_from_draw_param(draw_param)
        self.memory_draw_params[draw_param_stem, area_id, is_extra_slot].write_to_memory()

    def get_current_map_id(self) -> tuple[int, int, int, int] | None:
        if self._hook is None:
            raise ConnectionError("Memory hook has not been created.")
        current_map = self._hook.get("current_map")
        if current_map == (255, 255, 255, 255):
            return None
        return tuple(current_map[::-1])

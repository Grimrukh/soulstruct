from __future__ import annotations

import typing as tp
from soulstruct.base.project.links import WindowLinker as _BaseWindowLinker

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.params.draw_param import DrawParam
    from .window import ProjectWindow


class WindowLinker(_BaseWindowLinker):

    window: ProjectWindow

    def inject_draw_param(self, draw_param: DrawParam, area_id: int, slot=0):
        return self.window.runtime_tab.inject_draw_param(draw_param, area_id, slot)

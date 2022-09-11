from __future__ import annotations

__all__ = ["WindowLinker"]

import typing as tp

from soulstruct.base.project.links import WindowLinker as _BaseWindowLinker

if tp.TYPE_CHECKING:
    from .window import ProjectWindow


class WindowLinker(_BaseWindowLinker):

    window: ProjectWindow

    # TODO: Currently nothing.

    def validate_model_subtype(self, model_subtype, name: str, map_id: str):
        """Check appropriate game model files to confirm the given model name is valid."""
        raise NotImplementedError("Elden Ring cannot validate MSB model subtype yet.")

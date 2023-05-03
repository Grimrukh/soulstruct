from __future__ import annotations

__all__ = ["WindowLinker"]

import typing as tp
from soulstruct.containers import Binder
from soulstruct.darksouls1ptde.project.links import WindowLinker as _BaseWindowLinker
from soulstruct.darksouls1r.game_types.map_types import *

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.params.draw_param import DrawParam
    from .window import ProjectWindow


class WindowLinker(_BaseWindowLinker):

    window: ProjectWindow

    def inject_draw_param(self, draw_param: DrawParam, draw_param_stem: str, area_id: int, is_extra_slot=False):
        return self.window.runtime_tab.inject_draw_param(draw_param, draw_param_stem, area_id, is_extra_slot)

    def get_current_map_id(self) -> tp.Optional[tp.Tuple[int, int, int, int]]:
        return self.window.runtime_tab.get_current_map_id()

    def enable_flag(self, flag_id: int):
        self.window.runtime_tab.enable_flag(flag_id)

    def disable_flag(self, flag_id: int):
        self.window.runtime_tab.disable_flag(flag_id)

    def validate_model_subtype(self, model_game_type: tp.Type[MapModel], model_name: str, map_stem: str):
        """Check appropriate game model files to confirm the given model name is valid.

        Note that Character and Object models don't actually need `map_id` to validate them.
        """
        if model_game_type == CharacterModel:
            if (self.project.game_root / f"chr/{model_name}.chrbnd.dcx").is_file():
                return True
        elif model_game_type == ObjectModel:
            if (self.project.game_root / f"obj/{model_name}.objbnd.dcx").is_file():
                return True
        elif model_game_type == MapPieceModel:
            if (self.project.game_root / f"map/{map_stem}/{model_name}A{map_stem[1:3]}.flver.dcx").is_file():
                return True
        elif model_game_type == CollisionModel:
            hkxbhd_path = self.project.game_root / f"map/{map_stem}/h{map_stem}.hkxbhd"
            if hkxbhd_path.is_file():
                # NOTE: Brute-force check for name string in header file (for speed).
                with hkxbhd_path.open("r") as f:
                    if model_name + "A10.hkx.dcx" in f.read():
                        return True
        elif model_game_type == NavmeshModel:
            nvmbnd_path = self.project.game_root / f"map/{map_stem}/{map_stem}.nvmbnd.dcx"
            if nvmbnd_path.is_file():
                navmesh_bnd = Binder(nvmbnd_path)
                if model_name + "A10.nvm" in navmesh_bnd.entries_by_name.keys():
                    return True

        return False

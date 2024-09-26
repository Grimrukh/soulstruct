from __future__ import annotations

__all__ = [
    "ExistingConnectionError",
    "MissingConnectionError",
    "backup_all_mcp_msg",
    "draw_multiple_maps",
    "import_matplotlib_plt",
]

import shutil
import types
import typing as tp
from pathlib import Path

from soulstruct.exceptions import SoulstructError


class ExistingConnectionError(SoulstructError):
    """Tried to connect two MCG nodes or two MCP AABBs that are already connected."""


class MissingConnectionError(SoulstructError):
    """Tried to disconnect or otherwise falsely assumed two MCG nodes or two MCP AABBs are connected."""


def backup_all_mcp_msg(source_map, dest_map):
    """Arguments should be 'map' directory (e.g. in game root)."""
    for mcg_path in Path(source_map).glob("*/*.mcg"):
        dest_path = Path(dest_map, mcg_path.parent.relative_to(source_map))
        dest_path.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(mcg_path), str(dest_path))
    for mcp_path in Path(source_map).glob("*/*.mcp"):
        dest_path = Path(dest_map, mcp_path.parent.relative_to(source_map))
        dest_path.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(mcp_path), str(dest_path))


def draw_multiple_maps(map_ids):
    plt = import_matplotlib_plt(raise_if_missing=True)
    from soulstruct import DSR_PATH
    from .core import NavmeshGraph

    fig = plt.figure(figsize=(8, 8))
    axes = fig.add_subplot(111, projection="3d")
    colors = ("cyan", "blue", "green", "pink")
    for i, map_id in enumerate(map_ids):
        graph = NavmeshGraph(DSR_PATH + f"/map/{map_id}")
        graph.draw(axes=axes, auto_show=False, aabb_color=colors[i])
    plt.show()


def import_matplotlib_plt(raise_if_missing=False) -> tp.Optional[types.ModuleType]:
    try:
        # noinspection PyPackageRequirements
        import matplotlib.pyplot as plt
    except ImportError:
        if raise_if_missing:
            raise
        return None
    return plt

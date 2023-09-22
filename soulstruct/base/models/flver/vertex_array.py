__all__ = [
    "get_vertex_positions",
    "get_vertex_bone_weights",
    "get_vertex_bone_indices",
    "get_vertex_normals",
    "get_vertex_tangents",
    "get_vertex_bitangents",
    "get_vertex_colors",
    "get_vertex_uvs",
    "get_vertex_all_uvs",
]

import numpy as np


# region Vertex Array Operations

def get_vertex_positions(array) -> np.ndarray:
    """Get a view into the 'position_{c}' columns of the given vertex array.

    The returned view is a convenient way to get the vertex positions as 'vectors' and can be used to modify the
    vertex positions in-place.
    """
    fields = [f"position_{c}" for c in "xyz"]
    return array[fields]


def get_vertex_bone_weights(array) -> np.ndarray:
    """Get a view into the 'bone_weight_{c}' columns of the given vertex array."""
    fields = [f"bone_weight_{c}" for c in "abcd"]
    return array[fields]


def get_vertex_bone_indices(array) -> np.ndarray:
    """Get a view into the 'bone_index_{c}' columns of the given vertex array."""
    fields = [f"bone_index_{c}" for c in "abcd"]
    return array[fields]


def get_vertex_normals(array) -> np.ndarray:
    """Get a view into the 'normal_{c}' columns of the given vertex array."""
    fields = [f"normal_{c}" for c in "xyz"]
    return array[fields]


def get_vertex_tangents(array) -> np.ndarray:
    """Get a view into the 'tangent_{c}' columns of the given vertex array."""
    fields = [f"tangent_{c}" for c in "xyz"]
    return array[fields]


def get_vertex_bitangents(array) -> np.ndarray:
    """Get a view into the 'bitangent_{c}' columns of the given vertex array."""
    fields = [f"bitangent_{c}" for c in "xyz"]
    return array[fields]


def get_vertex_colors(array, color_index=0) -> np.ndarray:
    """Get a view into the 'color_{c}_{color_index}' columns of the given vertex array."""
    fields = [f"color_{c}_{color_index}" for c in "rgba"]
    try:
        return array[fields]
    except KeyError:
        raise KeyError(f"Vertex array does not have color index {color_index}.")


def get_vertex_uvs(array, uv_index: int, include_w=False) -> np.ndarray:
    """Get a view into the 'uv_{c}_{uv_index}' columns of the given vertex array."""
    fields = [f"uv_u_{uv_index}", f"uv_v_{uv_index}"]
    if include_w:  # assumes you know it's valid!
        fields.append(f"uv_w_{uv_index}")
    try:
        return array[fields]
    except KeyError:
        raise KeyError(f"Vertex array does not have UV index {uv_index}.")


def get_vertex_all_uvs(array, include_w=False) -> list[np.ndarray]:
    """Get a view into ALL 'uv_{c}_{i}' columns of the given vertex array.

    Returns a list of such views, one per UV index.
    """
    uv_views = []
    uv_u_names = [name for name in array.dtype.names if name.startswith("uv_u_")]
    for name in uv_u_names:
        fields = [name, name.replace("uv_u_", "uv_v_")]
        if include_w:
            fields.append(name.replace("uv_u_", "uv_w_"))
        uv_views.append(array[fields])
    return uv_views

# endregion

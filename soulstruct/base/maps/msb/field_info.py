
__all__ = ["FIELD_INFO"]

# Maps assorted MSB field names (across all types) to their display names and descriptions for the GUI.
# Used as default info if field metadata is unspecified.
FIELD_INFO = {
    "sib_path": (
        "Placeholder Path",
        "Internal path to model placeholder SIB file. The path's base name should match the model name.",
    ),

    "parts[translate]": (
        "Translate", "3D coordinates of the part's position. Note that the anchor of the part is usually at its base.",
    ),
    "parts[rotate]": (
        "Rotate", "Euler angles for part rotation around its local X, Y, and Z axes.",
    ),

    "regions[translate]": (
        "Translate",
        "3D coordinates of the region's position. Note that this is the middle of the bottom face for box regions.",
    ),
}

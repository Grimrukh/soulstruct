from pathlib import Path

EVENT_EXTENSIONS = {
    "evs": {".evs", ".evs.py", ".py", ".emevd.py"},
    "emevd": {".emevd"},
    "emevd.dcx": {".emevd.dcx"},
    "numeric": {".numeric", ".txt", ".numeric.txt"},
}


def convert_events(output_type, output_directory, input_directory, maps, emevd_class, input_type=None):
    """Convert all events from one format to another.

    The possible formats are 'evs' (or 'py'), 'emevd', 'emevd.dcx', and 'numeric' (or 'txt'). By default, the input
    type is auto-detected from the name of each EMEVD file with the appropriate map formatting (e.g.
    'm10_00_00_00.emevd.py', 'm10_01_00_00.numeric.txt') in the input directory (which defaults to the packaged vanilla
    'evs.py' scripts).

    A subset of EMEVD map constants to convert can be passed to `maps`, or it can be left to default to looking for all
    EMEVD files used in this game (in which case an error will be raised if any are not found).
    """
    output_ext = "." + output_type.lower().lstrip(".")
    output_type = None
    for ext_type, exts in EVENT_EXTENSIONS.items():
        if output_ext in exts:
            output_type = ext_type
    if output_type is None:
        raise ValueError(f"Invalid EMEVD output extension: {repr(output_ext)}.")
    output_directory = Path(output_directory)
    input_ext = "." + input_type.lower().lstrip(".") if input_type is not None else None
    input_directory = Path(input_directory)
    emevd_sources = {m.emevd_file_stem: None for m in maps}
    all_exts = EVENT_EXTENSIONS["evs"].union(
        EVENT_EXTENSIONS["emevd"].union(EVENT_EXTENSIONS["emevd.dcx"].union(EVENT_EXTENSIONS["numeric"]))
    )
    for available in input_directory.glob("*"):
        parts = available.name.split(".")
        name, ext = parts[0], "." + ".".join(parts[1:])
        if name in emevd_sources and (ext == input_ext or (input_ext is None and ext in all_exts)):
            if emevd_sources[name] is not None:
                raise FileExistsError(f"Found multiple files named {repr(name)} with different extensions.")
            emevd_sources[name] = available
    missing = [name for name, source in emevd_sources.items() if source is None]
    if missing:
        raise FileNotFoundError(f"Could not find EMEVD sources for: {missing}.")
    for name, source in emevd_sources.items():
        try:
            emevd = emevd_class(source, script_path=input_directory)
            output_path = output_directory / (name + output_ext)
            if output_type == "evs":
                print(Path(output_path).absolute())
                emevd.write_evs(output_path)
            elif output_type == "emevd":
                emevd.write_emevd(output_path, dcx=False)
            elif output_type == "emevd.dcx":
                emevd.write_emevd(output_path, dcx=True)
            elif output_type == "numeric":
                emevd.write_numeric(output_path)
        except Exception as e:
            raise ValueError(f"Encountered an error while attempting to compile {name + output_ext}: {str(e)}")

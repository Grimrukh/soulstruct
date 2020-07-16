__all__ = ["get_ds1_executable_and_version"]

from pathlib import Path


def get_ds1_executable_and_version(executable_path, dsr, debug=False):
    executable_path = Path(executable_path)
    if executable_path.is_dir():
        executables = [exe.name for exe in executable_path.glob("*.exe")]
        if "DARKSOULS.exe" in executables and "DarkSoulsRemastered.exe" in executables:
            raise FileExistsError(f"Both PTDE and DSR were executables found in directory {str(executable_path)}.")
        elif "DARKSOULS.exe" in executables:
            executable_path = executable_path / "DARKSOULS.exe"
        elif "DarkSoulsRemastered.exe" in executables:
            executable_path = executable_path / "DarkSoulsRemastered.exe"
        else:
            raise FileNotFoundError(f"Neither the PTDE or DSR Dark Souls 1 executable were found in directory "
                                    f"{str(executable_path)}.")

    if executable_path.is_file():
        if executable_path.name == "DARKSOULS.exe":
            if dsr is None:
                dsr = False
        elif executable_path == "DarkSoulsRemastered.exe":
            if dsr is None:
                dsr = True
        else:
            if dsr is None:
                raise ValueError("Could not guess if this executable is Dark Souls Remastered from its name. You must "
                                 "specify `dsr=True` or `dsr=False`.")
    else:
        raise FileNotFoundError(f"Dark Souls 1 executable not found: {str(executable_path)}")

    if dsr and debug:
        raise ValueError("`debug` cannot be True for Dark Souls Remastered.")

    return executable_path, dsr, debug

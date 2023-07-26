"""SOULSTRUCT

Command Line Usage:

python -m soulstruct [source]
    [-c / --console]
    [-t / --text]
    [-p / --params]
    [-l / --lighting]
    [-m / --modmanager]
    [--binderpack]
    [--binderunpack]
    [--tpfpack]
    [--tpfunpack]
    [--ai]
    [--consoleLogLevel]
    [--fileLogLevel]
"""
import argparse
import logging
from pathlib import Path

try:
    from colorama import init as colorama_init, Fore
except ImportError:
    colorama_init = None
    Fore = None
    MAGENTA = ""
    GREEN = ""
    RED = ""
    RESET = ""
else:
    MAGENTA = Fore.MAGENTA
    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Fore.RESET

from soulstruct._logging import CONSOLE_HANDLER, FILE_HANDLER
from soulstruct.config import DEFAULT_PROJECT_PATH
from soulstruct.games import get_game
from soulstruct.utilities.files import read_json
from soulstruct.utilities.game_selector import GameSelector
from soulstruct.utilities.text import word_wrap

LOG_LEVELS = {"debug", "info", "warning", "error", "fatal", "critical"}
_LOGGER = logging.getLogger("soulstruct")


parser = argparse.ArgumentParser(prog="soulstruct", description="Launch Soulstruct programs or adjust settings.")
parser.add_argument(
    "source",
    nargs="?",
    default=DEFAULT_PROJECT_PATH,
    help=word_wrap(
        "Source file or project directory to read from. Defaults to `DEFAULT_PROJECT_PATH` from `config.py`, which "
        "will be auto-generated the first time you run Soulstruct. If your project path is relative, it will be "
        "resolved relative to the executable directory (if running the frozen Soulstruct exe) or otherwise the working "
        "directory. If no additional arguments are given, the main Soulstruct GUI will launch. Alternatively, if "
        "`--console` is used, the `DarkSoulsProject` instance will be loaded into an interactive session (iPython "
        "package required)."
    ),
)
parser.add_argument(
    "-c",
    "--console",
    action="store_true",
    default=False,
    help=word_wrap(
        "Open an interactive IPython console rather than using the Soulstruct GUI. IPython must be installed to use "
        "this option, but you can always import and use Soulstruct from directly within an existing Python session."
    ),
)
parser.add_argument(
    "--show_console_startup",
    action="store_true",
    default=True,
    help=word_wrap("Show information message at console startup."),
)
parser.add_argument(
    "--maps", action="store_true", help=word_wrap("Open Soulstruct Maps Editor with given source.")
)
parser.add_argument(
    "--params", action="store_true", help=word_wrap("Open Soulstruct Param Editor with given source.")
)
parser.add_argument(
    "--lighting", action="store_true", help=word_wrap("Open Soulstruct Lighting Editor with given source.")
)
parser.add_argument(
    "--text", action="store_true", help=word_wrap("Open Soulstruct Text Editor with given source.")
)
parser.add_argument(
    "-m",
    "--modmanager",
    action="store_true",
    help=word_wrap("Open Soulstruct Mod Manager for given installation path. Defaults to `DSR_PATH` variable."),
)
parser.add_argument("--binderpack", action="store", help=word_wrap("Repack a BND/BXF from the given source directory."))
parser.add_argument("--binderunpack", action="store", help=word_wrap("Unpack a BND/BXF from the given source file."))
parser.add_argument("--tpfpack", action="store", help=word_wrap("Repack a TPF from the given source directory."))
parser.add_argument("--tpfunpack", action="store", help=word_wrap("Unpack a TPF from the given source file."))
parser.add_argument(
    "--consoleLogLevel",
    action="store",
    default="INFO",
    help=word_wrap(
        "Set the console log level to 'DEBUG', 'INFO', 'WARNING', 'ERROR', or 'CRITICAL'. Note that the console is "
        "disabled for frozen executable releases."
    ),
)
parser.add_argument(
    "--fileLogLevel",
    action="store",
    default="DEBUG",
    help=word_wrap("Set the file log level to 'DEBUG', 'INFO', 'WARNING', 'ERROR', or 'CRITICAL'."),
)


Project = None
Maps = None
Text = None
Params = None
Lighting = None


def get_existing_project_game(project_path: str):
    project_path = Path(project_path)
    if project_path.is_dir() and (project_path / "project_config.json").is_file():
        project_config = read_json(project_path / "project_config.json")
        if game_name := project_config.get("GameName", ""):
            return get_game(game_name)
    return None


def soulstruct_main(ss_args) -> bool:

    try:
        console_log_level = int(ss_args.consoleLogLevel)
    except ValueError:
        if ss_args.consoleLogLevel.lower() not in LOG_LEVELS:
            raise argparse.ArgumentError(ss_args.consoleLogLevel, f"Log level must be one of: {LOG_LEVELS}")
        console_log_level = getattr(logging, ss_args.consoleLogLevel.upper())
    CONSOLE_HANDLER.setLevel(console_log_level)

    try:
        file_log_level = int(ss_args.fileLogLevel)
    except ValueError:
        if ss_args.fileLogLevel.lower() not in LOG_LEVELS:
            raise argparse.ArgumentError(ss_args.fileLogLevel, f"Log level must be one of: {LOG_LEVELS}")
        file_log_level = getattr(logging, ss_args.fileLogLevel.upper())
    FILE_HANDLER.setLevel(file_log_level)

    source = None if not ss_args.source else ss_args.source

    if ss_args.modmanager:
        from soulstruct.utilities.mod_manager import ModManagerWindow
        ModManagerWindow(source).wait_window()
        return ss_args.console

    if ss_args.maps:
        game = GameSelector("darksouls1ptde", "darksouls1r", "bloodborne").go()
        global Maps
        Maps = game.import_game_submodule("maps").MapStudioDirectory(source)
        return ss_args.console

    if ss_args.params:
        game = GameSelector("darksouls1ptde", "darksouls1r", "bloodborne").go()
        global Params
        Params = game.import_game_submodule("params").GameParamBND(source)
        return ss_args.console

    if ss_args.lighting:
        game = GameSelector("darksouls1ptde", "darksouls1r").go()
        global Lighting
        Lighting = game.import_game_submodule("lighting").DrawParamDirectory(source)
        return ss_args.console

    if ss_args.text:
        game = GameSelector("darksouls1ptde", "darksouls1r", "bloodborne", "darksouls3", "eldenring").go()
        global Text
        Text = game.import_game_submodule("text").MSGDirectory(source)
        return ss_args.console

    if ss_args.binderpack is not None:
        from soulstruct.containers import Binder
        binder = Binder.from_unpacked_path(ss_args.binderpack)
        binder.write()
        return False

    if ss_args.binderunpack is not None:
        from soulstruct.containers import Binder
        binder = Binder.from_path(ss_args.binderunpack)
        binder.write_unpacked_directory()
        return False

    if ss_args.tpfunpack is not None:
        from soulstruct.containers.tpf import TPF
        tpf = TPF.from_path(ss_args.tpfunpack)
        tpf.write_unpacked_directory()
        return False

    if ss_args.tpfpack is not None:
        from soulstruct.containers.tpf import TPF
        tpf = TPF.from_unpacked_path(ss_args.tpfpack)
        tpf.write()
        return False

    # No specific type. Open entire Soulstruct Project.
    game = get_existing_project_game(source) if source else None
    if game is None:
        game = GameSelector("darksouls1ptde", "darksouls1r", "bloodborne", "eldenring").go()
    if ss_args.console:
        # Console only.
        global Project
        Project = game.import_game_submodule("project").GameDirectoryProject(source)
        if ss_args.show_console_startup:
            if colorama_init:
                colorama_init()
            print(
                "\n"
                f"Starting interactive console. You can modify your project data directly here through the\n"
                f"{GREEN}Project{RESET} attributes {GREEN}maps{RESET}, {GREEN}params{RESET}, "
                f"{GREEN}lighting{RESET}, and {GREEN}text{RESET}. For example:\n\n"
                f"    {GREEN}Project.maps.parts.new_character(name=\"Pet Gaping Dragon\", model_name=\"c5260\")"
                f"{RESET}\n\n"
                "You can also access other common operations, such as:\n\n"
                f"    {GREEN}Project.save(\"maps\"){RESET}  # save current Maps data to project\n"
                f"    {GREEN}Project.export_data(\"params\"){RESET}  # export current Params data to game\n"
                f"    {GREEN}Project.import_data(){RESET}  # import ALL data types from game into project\n\n"
                f"See the Soulstruct Python package for other functions: "
                f"{MAGENTA}https://github.com/grimrukh/soulstruct{RESET}\n\n"
                f"Type {RED}exit{RESET} or close the window to terminate the console. Make sure to use "
                f"{GREEN}Project.save(){RESET}\n"
                f"to save your changes first, if desired!\n",
            )
        return True
    # Window.
    window = game.import_game_submodule("project").ProjectWindow(source)
    window.wait_window()  # MAIN LOOP
    return False


try:
    launch_interactive = soulstruct_main(parser.parse_args())
except Exception as ex:
    _LOGGER.exception(f"Error occurred in soulstruct.__main__: {ex}")
    launch_interactive = False
    input("Press any key to exit.")


if launch_interactive:
    try:
        from IPython import embed
    except ImportError:
        _LOGGER.error(
            "IPython must be installed to open an interactive console from a script.\n"
            "You can install it with `python -m pip install ipython` and run `python -m soulstruct` again, or directly "
            "`import soulstruct` within an existing Python session to use the default Python console."
        )
    else:
        embed(colors="neutral")

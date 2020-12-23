"""SOULSTRUCT

Command Line Usage:

python -m soulstruct [source]
    [-c / --console]
    [-t / --text]
    [-p / --params]
    [-l / --lighting]
    [-m / --modmanager]
    [--bndpack]
    [--bndunpack]
    [--ai]
    [--consoleLogLevel]
    [--fileLogLevel]
"""
import argparse
import logging

from soulstruct.config import DEFAULT_PROJECT_PATH
from soulstruct._logging import CONSOLE_HANDLER, FILE_HANDLER
from soulstruct.utilities import word_wrap

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
    "-t", "--text", action="store_true", help=word_wrap("Open Soulstruct Text Editor with given source.")
)
parser.add_argument(
    "-p", "--params", action="store_true", help=word_wrap("Open Soulstruct Param Editor with given source.")
)
parser.add_argument(
    "-l", "--lighting", action="store_true", help=word_wrap("Open Soulstruct Lighting Editor with given source.")
)
parser.add_argument(
    "-m",
    "--modmanager",
    action="store_true",
    help=word_wrap("Open Soulstruct Mod Manager. No sources should be given."),
)
parser.add_argument("--bndpack", action="store", help=word_wrap("Repack a BND from the given source path."))
parser.add_argument("--bndunpack", action="store", help=word_wrap("Unpack a BND from the given source path."))
parser.add_argument("--ai", action="store_true", help=word_wrap("Open Soulstruct AI Script Editor with given source."))
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
AI = None


def soulstruct_main(ss_args):

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

        ModManagerWindow().wait_window()
        return ss_args.console

    if ss_args.text:
        # TODO: Support other games (Bloodborne).
        from soulstruct.maps.darksouls1 import MapStudioDirectory

        global Maps
        Maps = MapStudioDirectory(source)
        return ss_args.console

    if ss_args.text:
        from soulstruct.text.darksouls1 import MSGDirectory

        global Text
        Text = MSGDirectory(source)
        return ss_args.console

    if ss_args.params:
        from soulstruct.params.darksouls1r import GameParamBND

        global Params
        Params = GameParamBND(source)
        return ss_args.console

    if ss_args.lighting:
        from soulstruct.params.darksouls1r import DrawParamDirectory

        global Lighting
        Lighting = DrawParamDirectory(source)
        return ss_args.console

    if ss_args.bndpack is not None:
        from soulstruct.bnd import BND

        bnd = BND(ss_args.bndpack)
        bnd.write()
        return

    if ss_args.bndunpack is not None:
        from soulstruct.bnd import BND

        bnd = BND(ss_args.bndunpack)
        bnd.write_unpacked_dir()
        return

    if ss_args.ai:
        from soulstruct.ai.darksouls1 import AIDirectory

        global AI
        AI = AIDirectory(source)
        return ss_args.console

    # No specific type. Open entire Soulstruct Project.
    if ss_args.console:
        from soulstruct.project.darksouls1r import GameDirectoryProject

        global Project
        Project = GameDirectoryProject(source)
    else:
        from soulstruct.project.darksouls1r import ProjectWindow

        window = ProjectWindow(source)
        window.wait_window()  # MAIN LOOP
    return ss_args.console


try:
    launch_interactive = soulstruct_main(parser.parse_args())
except Exception as e:
    _LOGGER.exception(f"Error occurred in soulstruct.__main__: {e}")
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
        embed()

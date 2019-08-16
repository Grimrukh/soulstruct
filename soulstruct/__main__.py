"""SOULSTRUCT

Command Line Usage:

python -m soulstruct [source]
    [-c / --console]
    [-t / --text]
    [-p / --params]
    [-l / --lighting]
    [--config] live_game_path temp_game_path default_game_path
    TODO: Event and ESD editors.
    TODO: fileLogLevel and consoleLogLevel.


"""
import argparse
import logging

from soulstruct.utilities import word_wrap

LOG_LEVELS = {'debug', 'info', 'result', 'warning', 'error', 'fatal', 'critical'}


parser = argparse.ArgumentParser(prog='soulstruct', description="Launch Soulstruct programs or adjust settings.")
parser.add_argument(
    "source", nargs='?', default=None,
    help=word_wrap(
        "Source file or directory to read from. Use 'live' to use the LIVE_GAME_PATH, 'temp' to use the "
        "TEMP_GAME_PATH, or 'default' (or no source) to use the DEFAULT_GAME_PATH. If no additional arguments are "
        "given, the main Soulstruct GUI will launch (in which case, 'source' must be either the game executable or its "
        "containing directory), or if '--console' is True, all possible structures will be loaded into an interactive "
        "console."
    )
)
parser.add_argument(
    # TODO: Defaults to True until GUI is ready, and will then default to False.
    "-c", "--console", action='store_true', default=True,
    help=word_wrap(
        "Open an interactive IPython console rather than using the Soulstruct GUI. IPython must be installed to use "
        "this option, but you can always import and use Soulstruct from directly within an existing Python session."
    )
)
parser.add_argument(
    "-t", "--text", action='store_true',
    help=word_wrap(
        "Open Soulstruct Text Editor with given source."
    )
)
parser.add_argument(
    "-p", "--params", action='store_true',
    help=word_wrap(
        "Open Soulstruct Param Editor with given source."
    )
)
parser.add_argument(
    "-l", "--lighting", action='store_true',
    help=word_wrap(
        "Open Soulstruct Lighting Editor with given source."
    )
)
parser.add_argument(
    "--config", nargs=3,
    help=word_wrap(
        "Pass three strings for LIVE, TEMP, and DEFAULT game paths to be written to 'config.py'. Dark Souls files in "
        "these directories can then be accessed using simply 'live', 'temp', or 'default' (which is usually the "
        "default) for the different Soulstruct structures and editors."
    )
)
parser.add_argument(
    "--consoleLogLevel", action='store', default='WARNING',
    help=word_wrap(
        "Set the console log level to 'DEBUG', 'INFO', 'WARNING', 'ERROR', or 'CRITICAL'."
    )
)
parser.add_argument(
    "--fileLogLevel", action='store', default='INFO',
    help=word_wrap(
        "Set the file log level to 'DEBUG', 'INFO', 'WARNING', 'ERROR', or 'CRITICAL'."
    )
)


Project = None
Text = None
Params = None
Lighting = None


def soulstruct_main(ss_args):

    # try:
    #     console_log_level = int(ss_args.consoleLogLevel)
    # except ValueError:
    #     if ss_args.consoleLogLevel.lower() not in LOG_LEVELS:
    #         raise argparse.ArgumentError(ss_args.consoleLogLevel, f"Log level must be one of: {LOG_LEVELS}")
    #     console_log_level = getattr(logging, ss_args.consoleLogLevel.upper())
    # TODO: CONSOLE_HANDLER.setLevel(console_log_level)

    # try:
    #     file_log_level = int(ss_args.fileLogLevel)
    # except ValueError:
    #     if ss_args.fileLogLevel.lower() not in LOG_LEVELS:
    #         raise argparse.ArgumentError(ss_args.fileLogLevel, f"Log level must be one of: {LOG_LEVELS}")
    #     file_log_level = getattr(logging, ss_args.fileLogLevel.upper())
    # TODO: FILE_HANDLER.setLevel(file_log_level)

    if ss_args.text:
        from soulstruct.text import DarkSoulsText
        global Text
        Text = DarkSoulsText(ss_args.source)
        return ss_args.console

    if ss_args.params:
        from soulstruct.params import DarkSoulsGameParameters
        global Params
        Params = DarkSoulsGameParameters(ss_args.source)
        return ss_args.console

    if ss_args.lighting:
        from soulstruct.params import DarkSoulsLightingParameters
        global Lighting
        Lighting = DarkSoulsLightingParameters(ss_args.source)
        return ss_args.console

    # No specific type. Open entire project.
    from soulstruct.core import SoulstructProject
    global Project
    Project = SoulstructProject(ss_args.source)
    return ss_args.console


if soulstruct_main(parser.parse_args()):
    try:
        from IPython import embed
    except ImportError:
        print("# ERROR: IPython must be installed to open an interactive console from a script.\n"
              "# You can install it, or directly import Soulstruct within an existing Python session.")
    else:
        embed()

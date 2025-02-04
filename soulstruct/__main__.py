"""SOULSTRUCT

Command Line Usage:

python -m soulstruct
    [--binderpack]
    [--binderunpack]
    [--tpfpack]
    [--tpfunpack]
    [--restorebak]
    [--consoleLogLevel]
    [--fileLogLevel]
"""
import argparse
import logging
from pathlib import Path

from soulstruct._logging import CONSOLE_HANDLER, FILE_HANDLER
from soulstruct.utilities.files import create_bak
from soulstruct.utilities.text import word_wrap

LOG_LEVELS = {"debug", "info", "warning", "error", "fatal", "critical"}
_LOGGER = logging.getLogger("soulstruct")


parser = argparse.ArgumentParser(prog="soulstruct", description="Launch Soulstruct programs or adjust settings.")

parser.add_argument("--undcx", action="store", help=word_wrap("Remove DCX compression and extension from file."))
parser.add_argument("--binderpack", action="store", help=word_wrap("Repack a BND/BXF from the given source directory."))
parser.add_argument("--binderunpack", action="store", help=word_wrap("Unpack a BND/BXF from the given source file."))
parser.add_argument("--tpfpack", action="store", help=word_wrap("Repack a TPF from the given source directory."))
parser.add_argument("--tpfunpack", action="store", help=word_wrap("Unpack a TPF from the given source file."))
parser.add_argument("--msbtojson", action="store", help=word_wrap("Convert an MSB file to JSON (DS1R only)."))
parser.add_argument("--jsontomsb", action="store", help=word_wrap("Convert a JSON file to MSB (DS1R only)."))
parser.add_argument("--restorebak", action="store", help=word_wrap("Restore a BAK file, overwriting any non-BAK file."))
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

    if ss_args.undcx is not None:
        from soulstruct.dcx import decompress
        dcx_path = Path(ss_args.undcx)
        uncompressed, dcx_type = decompress(dcx_path)
        undcx_path = dcx_path.with_suffix("") if dcx_path.suffix == ".dcx" else dcx_path.with_suffix(".undcx")
        if undcx_path.is_file():
            create_bak(undcx_path)
        with undcx_path.open("wb") as f:
            f.write(uncompressed)
        return

    # TODO: `dcx` command to compress a file. (Requires user to specify DCX type, or assert a metafile saying such.)

    if ss_args.binderpack is not None:
        from soulstruct.containers import Binder
        binder = Binder.from_unpacked_path(ss_args.binderpack)
        binder.write()
        return

    if ss_args.binderunpack is not None:
        from soulstruct.containers import Binder
        binder = Binder.from_path(ss_args.binderunpack)
        binder.write_unpacked_directory()
        return

    if ss_args.tpfunpack is not None:
        from soulstruct.containers.tpf import TPF
        tpf = TPF.from_path(ss_args.tpfunpack)
        tpf.write_unpacked_directory()
        return

    if ss_args.tpfpack is not None:
        from soulstruct.containers.tpf import TPF
        tpf = TPF.from_unpacked_path(ss_args.tpfpack)
        tpf.write()
        return

    if ss_args.msbtojson is not None:
        from soulstruct.darksouls1r.maps import MSB
        try:
            msb = MSB.from_path(ss_args.msbtojson)
        except ValueError as ex:
            _LOGGER.error(f"Could not load MSB file: {ex}")
            raise
        msb.write_json(msb.path.with_suffix(f"{msb.path.suffix}.json"))
        return

    if ss_args.jsontomsb is not None:
        from soulstruct.darksouls1r.maps import MSB
        try:
            msb = MSB.from_json(ss_args.jsontomsb)
        except ValueError as ex:
            _LOGGER.error(f"Could not load JSON file as MSB: {ex}")
            raise
        msb.write(msb.path.with_name(f"{msb.path_minimal_stem}.msb"))
        return

    if ss_args.restorebak is not None:
        from soulstruct.utilities.files import restore_bak
        # NOTE: Dangerous enough that I require user confirmation if the non-BAK file exists.
        target = Path(ss_args.restorebak)
        if target.is_file():
            replaced_path = Path(target.with_name(target.name.removesuffix(".bak")))
            if replaced_path.is_file() and input(
                f"Are you sure you want to overwrite file {replaced_path} with restored BAK file? "
                f"Type 'y' to confirm: "
            ).lower() != "y":
                return
        elif target.is_dir():
            if input(
                f"Are you sure you want to restore all BAK files in {ss_args.restorebak} (overwriting non-BAK files)? "
                f"Type 'y' to confirm: "
            ).lower() != "y":
                return
        else:
            _LOGGER.warning(f"Could not find file or directory {ss_args.restorebak} to restore.")
            return
        count = restore_bak(ss_args.restorebak, delete_baks=False)
        _LOGGER.info(f"{count} bak files restored (bak files not deleted).")
        return

    return


try:
    soulstruct_main(parser.parse_args())
except Exception as main_ex:
    _LOGGER.exception(f"Error occurred in soulstruct.__main__: {main_ex}")
    input("Press any key to exit.")

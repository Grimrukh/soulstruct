"""
Soulstruct command-line interface (and `python -m soulstruct` main script).

Runs as either

    python -m soulstruct ...

or the console script installed from pyproject.toml:

    soulstruct ...

Global logging options come first, followed by sub-commands.
"""
from __future__ import annotations

__all__ = [
    "app",
]

import logging
from pathlib import Path

import typer

from soulstruct.logging_utils import setup
from soulstruct.utilities.files import create_bak

LOG_LEVELS = {"debug", "info", "warning", "error", "fatal", "critical"}
_LOGGER = logging.getLogger(__name__)


def _parse_level(value: str) -> int:
    """Convert a level name (info) or int string (20) ➜ logging level."""
    if value.isdigit():
        return int(value)
    if value.lower() in LOG_LEVELS:
        return getattr(logging, value.upper())
    raise typer.BadParameter(f"Log level must be int or one of {LOG_LEVELS}")


# Typer application.
app = typer.Typer(
    add_completion=False,
    help="Launch Soulstruct utilities (packing/unpacking, conversion, etc.).",
)

# Global options executed before any sub-command.
@app.callback()
def main(
    console_log_level: str = typer.Option(
        "INFO", "--console-log-level", "-cl", help="Console log level (DEBUG/INFO/…)."
    ),
    file_log_level: str = typer.Option(
        "DEBUG", "--file-log-level", "-fl", help="Log-file level (DEBUG/INFO/…)."
    ),
    file_log_path: Path = typer.Option(
        None,
        "--file-log-path",
        "-fp",
        help="Path to log file (default: `soulstruct.log` in current directory).",
    ),
):
    """Global logging controls (executed before sub-commands)."""
    setup(
        console_level=console_log_level,
        file_level=file_log_level,
        log_path=file_log_path,
        rich_tracebacks=True,
        clear_old_handlers=True,
    )


# region Commands

@app.command()
def undcx(path: Path):
    """Remove DCX compression (writes *.undcx or suffix-free file)."""
    from soulstruct.dcx import decompress

    uncompressed, _dcx_type = decompress(path)
    out = path.with_suffix("") if path.suffix == ".dcx" else path.with_suffix(".undcx")
    if out.exists():
        create_bak(out)
    out.write_bytes(uncompressed)
    _LOGGER.info("Wrote %s", out)


@app.command()
def binderpack(source_dir: Path):
    """Re-pack a BND/BXF from directory *SOURCE_DIR*."""
    from soulstruct.containers import Binder

    Binder.from_unpacked_path(source_dir).write()


@app.command()
def binderunpack(binder_file: Path):
    """Unpack a BND/BXF file."""
    from soulstruct.containers import Binder

    Binder.from_path(binder_file).write_unpacked_directory()


@app.command()
def tpfpack(source_dir: Path):
    """Re-pack a TPF from directory *SOURCE_DIR*."""
    from soulstruct.containers.tpf import TPF

    TPF.from_unpacked_path(source_dir).write()


@app.command()
def tpfunpack(tpf_file: Path):
    """Unpack a TPF file."""
    from soulstruct.containers.tpf import TPF

    TPF.from_path(tpf_file).write_unpacked_directory()


@app.command()
def msbtojson(msb_path: Path):
    """Convert an MSB file to JSON (DS1R only)."""
    from soulstruct.darksouls1r.maps import MSB

    msb = MSB.from_path(msb_path)
    out = msb.path.with_suffix(f"{msb.path.suffix}.json")
    msb.write_json(out)
    _LOGGER.info("Wrote %s", out)


@app.command()
def jsontomsb(json_path: Path):
    """Convert a JSON file back to MSB (DS1R only)."""
    from soulstruct.darksouls1r.maps import MSB

    msb = MSB.from_json(json_path)
    out = msb.path.with_name(f"{msb.path_minimal_stem}.msb")
    msb.write(out)
    _LOGGER.info("Wrote %s", out)


@app.command()
def restorebak(
    target: Path,
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompts."),
):
    """Restore *.bak files, overwriting originals."""
    from soulstruct.utilities.files import restore_bak

    def _confirm(msg: str) -> bool:
        return yes or typer.confirm(msg)

    if target.is_file():
        repl = target.with_name(target.name.removesuffix(".bak"))
        if repl.exists() and not _confirm(f"Overwrite {repl} with {target}?"):
            raise typer.Abort()
    elif target.is_dir():
        if not _confirm(f"Restore all .bak files in {target}?"):
            raise typer.Abort()
    else:
        _LOGGER.warning("No such file or directory: %s", target)
        raise typer.Exit(1)

    count = restore_bak(target, delete_baks=False)
    _LOGGER.info("Restored %s bak files (bak files kept).", count)

# endregion


if __name__ == "__main__":
    try:
        app()
    except Exception as ex:
        _LOGGER.exception("Unhandled exception: %s", ex)
        input("Press any key to exit.")

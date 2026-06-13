__all__ = [
    "SoulstructConfig",
    "Config",

    # Backward-compat module-level aliases (read once at import; use `Config.<FIELD>` for live values).
    "DES_PATH",
    "DESR_PATH",
    "PTDE_PATH",
    "DSR_PATH",
    "DS2_PATH",
    "DS2_SOTFS_PATH",
    "BB_PATH",
    "DS3_PATH",
    "SEK_PATH",
    "ER_PATH",
    "PARAMDEX_PATH",
    "LOG_PATH",
    "CONSOLE_LOG_LEVEL",
    "FILE_LOG_LEVEL",
]

import dataclasses
import json
import logging
import sys
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

_LOGGER = logging.getLogger(__name__)

_DEFAULT_STEAM_PATH = Path(r"C:/Program Files (x86)/Steam/steamapps/common")
_SOULSTRUCT_APPDATA = Path("~/AppData/Roaming/soulstruct").expanduser()


def _get_json_path() -> Path:
    """Return the canonical path to `soulstruct_config.json`."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys.executable).parent / "soulstruct_config.json"
    return _SOULSTRUCT_APPDATA / "soulstruct_config.json"


@dataclass
class SoulstructConfig:
    """Mirrors `soulstruct_config.json`.  The module-level singleton is ``Config``."""

    # --- Game roots ---
    DES_PATH: Path = field(default_factory=lambda: Path(r"C:/Demon's Souls/PS3_GAME/USRDIR"))
    DESR_PATH: Path = field(default_factory=lambda: Path(r"C:/Demon's Souls Remake/dvdroot_ps5"))
    PTDE_PATH: Path = field(default_factory=lambda: _DEFAULT_STEAM_PATH / "Dark Souls Prepare to Die Edition/DATA")
    DSR_PATH: Path = field(default_factory=lambda: _DEFAULT_STEAM_PATH / "DARK SOULS REMASTERED")
    DS2_PATH: Path = field(default_factory=lambda: _DEFAULT_STEAM_PATH / "Dark Souls II/Game")
    DS2_SOTFS_PATH: Path = field(
        default_factory=lambda: _DEFAULT_STEAM_PATH / "Dark Souls II Scholar of the First Sin/Game"
    )
    BB_PATH: Path = field(default_factory=lambda: Path("C:/Bloodborne/dvdroot_ps4"))
    DS3_PATH: Path = field(default_factory=lambda: _DEFAULT_STEAM_PATH / "DARK SOULS III/Game")
    SEK_PATH: Path = field(default_factory=lambda: _DEFAULT_STEAM_PATH / "Sekiro")  # TODO: 'Game'?
    ER_PATH: Path = field(default_factory=lambda: _DEFAULT_STEAM_PATH / "ELDEN RING/Game")

    # --- Misc paths ---
    PARAMDEX_PATH: Path | str = ""  # empty str → default to soulstruct package path

    # --- Logging ---
    AUTO_SETUP_LOG: bool = True
    LOG_PATH: Path = field(default_factory=lambda: _SOULSTRUCT_APPDATA / "soulstruct.log")
    CONSOLE_LOG_LEVEL: str = "INFO"
    FILE_LOG_LEVEL: str = "DEBUG"

    # ------------------------------------------------------------------
    # Serialisation helpers
    # ------------------------------------------------------------------

    def to_dict(self) -> dict[str, tp.Any]:
        """Return a JSON-serialisable dict (Path → str)."""
        result = {}
        for f in dataclasses.fields(self):
            v = getattr(self, f.name)
            result[f.name] = str(v) if isinstance(v, Path) else v
        return result

    @classmethod
    def from_dict(cls, data: dict[str, tp.Any]) -> "SoulstructConfig":
        """Construct from a raw dict, converting *_PATH keys to :class:`Path`."""
        kwargs: dict[str, tp.Any] = {}
        field_names = {f.name for f in dataclasses.fields(cls)}
        for k, v in data.items():
            if k not in field_names:
                continue  # ignore unknown / legacy keys
            if k.endswith("_PATH") and v:
                kwargs[k] = Path(v)
            else:
                kwargs[k] = v
        return cls(**kwargs)

    # ------------------------------------------------------------------
    # Load / save
    # ------------------------------------------------------------------

    @staticmethod
    def json_path() -> Path:
        """Return the canonical path to ``soulstruct_config.json``."""
        return _get_json_path()

    def load(self) -> None:
        """Load values from ``soulstruct_config.json``, updating this instance in-place.

        Missing keys fall back to the existing (default) field values.  A
        ``FileNotFoundError`` is raised only when running as a frozen executable
        and the file is absent; otherwise the defaults are silently kept.
        """
        _json_path = _get_json_path()
        if not _json_path.exists():
            if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
                raise FileNotFoundError(
                    f"Could not find 'soulstruct_config.json' next to Soulstruct executable."
                )
            return  # use defaults

        with _json_path.open("r") as fp:
            try:
                data = json.load(fp)
            except json.JSONDecodeError as ex:
                raise json.JSONDecodeError(
                    f"Error while loading 'soulstruct_config.json': {ex.msg}",
                    "soulstruct_config.json",
                    ex.lineno,
                )

        # Handle legacy key rename.
        if "ELDEN_RING_PATH" in data and "ER_PATH" not in data:
            data["ER_PATH"] = data.pop("ELDEN_RING_PATH")

        field_names = {f.name for f in dataclasses.fields(self)}
        for k, v in data.items():
            if k not in field_names:
                continue
            if k.endswith("_PATH") and v:
                object.__setattr__(self, k, Path(v))
            else:
                object.__setattr__(self, k, v)

    def save(self) -> None:
        """Write this instance to ``soulstruct_config.json``."""
        _json_path = _get_json_path()
        _json_path.parent.mkdir(parents=True, exist_ok=True)
        with _json_path.open("w") as fp:
            json.dump(self.to_dict(), fp, indent=4)

    def update(self, **kwargs: tp.Any) -> None:
        """Update one or more fields by name and save."""
        field_names = {f.name for f in dataclasses.fields(self)}
        invalid = [k for k in kwargs if k not in field_names]
        if invalid:
            raise KeyError(f"Invalid config key(s): {invalid}")
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
        self.save()

    # ------------------------------------------------------------------
    # Auto-logging
    # ------------------------------------------------------------------

    def setup_log(self) -> None:
        """Configure the ``soulstruct`` logger from the current settings."""
        from soulstruct.logging_utils import setup

        setup(
            console_level=self.CONSOLE_LOG_LEVEL,
            file_level=self.FILE_LOG_LEVEL,
            log_path=self.LOG_PATH,
            rich_tracebacks=True,
            clear_old_handlers=True,
        )


# ---------------------------------------------------------------------------
# Module-level singleton
# ---------------------------------------------------------------------------

Config = SoulstructConfig()

try:
    Config.load()
except FileNotFoundError:
    _LOGGER.info(
        "Creating default `soulstruct_config.json` file next to Soulstruct executable.\n"
        "Set your game directories and other Soulstruct settings in here."
    )
    Config.save()
    Config.load()
else:
    # If the on-disk file is missing any keys, rewrite it with full defaults.
    json_path = _get_json_path()
    if json_path.exists():
        with json_path.open("r") as _fp:
            _on_disk = json.load(_fp)
        if len(_on_disk) != len(dataclasses.fields(SoulstructConfig)):
            Config.save()


# ---------------------------------------------------------------------------
# Backward-compatible module-level aliases  (values fixed at import time)
# Use ``Config.<FIELD>`` for live, mutable access.
# ---------------------------------------------------------------------------

DES_PATH: Path = Config.DES_PATH
DESR_PATH: Path = Config.DESR_PATH
PTDE_PATH: Path = Config.PTDE_PATH
DSR_PATH: Path = Config.DSR_PATH
DS2_PATH: Path = Config.DS2_PATH
DS2_SOTFS_PATH: Path = Config.DS2_SOTFS_PATH
BB_PATH: Path = Config.BB_PATH
DS3_PATH: Path = Config.DS3_PATH
SEK_PATH: Path = Config.SEK_PATH
ER_PATH: Path = Config.ER_PATH
PARAMDEX_PATH: Path | str = Config.PARAMDEX_PATH
LOG_PATH: Path = Config.LOG_PATH
CONSOLE_LOG_LEVEL: str = Config.CONSOLE_LOG_LEVEL
FILE_LOG_LEVEL: str = Config.FILE_LOG_LEVEL


# ---------------------------------------------------------------------------
# Auto-log setup
# ---------------------------------------------------------------------------

if Config.AUTO_SETUP_LOG:
    Config.setup_log()

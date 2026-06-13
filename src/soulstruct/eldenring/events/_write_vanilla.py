from pathlib import Path

from soulstruct.eldenring.events import EventDirectory
from soulstruct.config import Config


def main():
    print("Loading vanilla events...")
    ed = EventDirectory.from_path(Config.ER_PATH / "event")
    print("Writing vanilla EVS scripts...")
    entitites_dir = Path(__file__).parent / "vanilla/enums"
    ed.write_evs(
        evs_directory="vanilla",
        enums_directory=entitites_dir if entitites_dir.is_dir() else None,
        warn_missing_enums=False,
        enums_module_prefix=".enums.",
    )

    # For fun.
    lines = 0
    for evs_file in Path("vanilla").glob("*.evs.py"):
        lines += len(evs_file.read_text().splitlines())

    # Test EVS read.
    EventDirectory.from_path("vanilla")
    print("ER `vanilla` events successfully written and re-read.")
    print(f"Total EVS line count: {lines}")


if __name__ == '__main__':
    main()

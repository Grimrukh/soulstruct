from pathlib import Path

from soulstruct.eldenring.events import EventDirectory
from soulstruct.config import ELDEN_RING_PATH

VANILLA_EVENT_PATH = Path(ELDEN_RING_PATH) / "../../ELDEN RING (Vanilla Unpacked)/Game/event"
ENTITIES_DIR = Path(__file__).parent / "vanilla/entities"


def main():
    print("Loading vanilla events...")
    ed = EventDirectory(VANILLA_EVENT_PATH)
    print("Writing vanilla EVS scripts...")
    ed.write_evs(
        "vanilla",
        entities_directory=ENTITIES_DIR if ENTITIES_DIR.is_dir() else None,
        warn_missing_enums=False,
        enums_module_prefix=".entities.",
    )

    # For fun.
    lines = 0
    for evs_file in Path("vanilla").glob("*.evs.py"):
        lines += len(evs_file.read_text().splitlines())

    # Test EVS read.
    EventDirectory("vanilla")
    print("ER `vanilla` events successfully written and re-read.")
    print(f"Total EVS line count: {lines}")


if __name__ == '__main__':
    main()

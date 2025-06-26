from soulstruct.darksouls1ptde.events.event_directory import EventDirectory
from soulstruct.config import PTDE_PATH


def main():
    ed = EventDirectory(PTDE_PATH / "event")
    ed.write_evs("vanilla")

    # For fun.
    from pathlib import Path
    lines = 0
    for evs_file in Path("vanilla").glob("*.evs.py"):
        lines += len(evs_file.read_text().splitlines())

    # Test EVS read.
    EventDirectory("vanilla")
    print("PTDE `vanilla` events successfully written and re-read.")
    print(f"Total EVS line count: {lines}")


if __name__ == '__main__':
    main()

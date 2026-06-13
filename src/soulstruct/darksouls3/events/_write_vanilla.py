from soulstruct.darksouls3.events import EventDirectory
from soulstruct.config import Config


def main():
    ed = EventDirectory(Config.DS3_PATH / "event")
    ed.write_evs("vanilla")

    # For fun.
    from pathlib import Path
    lines = 0
    for evs_file in Path("vanilla").glob("*.evs.py"):
        lines += len(evs_file.read_text().splitlines())

    # Test EVS read.
    EventDirectory(Path("vanilla"))
    print("DS3 `vanilla` events successfully written and re-read.")
    print(f"Total EVS line count: {lines}")


if __name__ == '__main__':
    main()

from pathlib import Path

from soulstruct.darksouls1r.events.event_directory import EventDirectory
from soulstruct.config import Config


def main():
    ed = EventDirectory(Config.DSR_PATH / "event")
    ed.write_evs(Path("vanilla"))

    # Test EVS read.
    EventDirectory(Path("vanilla"))
    print("DSR `vanilla` events successfully written and re-read.")


if __name__ == '__main__':
    main()

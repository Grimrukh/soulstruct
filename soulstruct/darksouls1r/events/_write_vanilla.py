from soulstruct.darksouls1r.events.emevd_directory import EventDirectory
from soulstruct.config import DSR_PATH


def main():
    ed = EventDirectory(DSR_PATH + "/event")
    ed.write_evs("vanilla")

    # Test EVS read.
    EventDirectory("vanilla")
    print("DSR `vanilla` events successfully written and re-read.")


if __name__ == '__main__':
    main()

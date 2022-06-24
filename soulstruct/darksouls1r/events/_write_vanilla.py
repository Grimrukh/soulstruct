from soulstruct.darksouls1r.events.emevd_directory import EMEVDDirectory
from soulstruct.config import DSR_PATH


def main():
    ed = EMEVDDirectory(DSR_PATH + "/event")
    ed.write_evs("vanilla")

    EMEVDDirectory("vanilla")


if __name__ == '__main__':
    main()

from soulstruct.darksouls1ptde.events.emevd_directory import EMEVDDirectory
from soulstruct.config import PTDE_PATH


def main():
    ed = EMEVDDirectory(PTDE_PATH + "/event")
    ed.write_evs("vanilla")

    EMEVDDirectory("vanilla")


if __name__ == '__main__':
    main()

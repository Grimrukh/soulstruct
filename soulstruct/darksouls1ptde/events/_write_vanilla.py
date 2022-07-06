from soulstruct.darksouls1ptde.events.emevd_directory import EMEVDDirectory
from soulstruct.config import PTDE_PATH


def main():
    ed = EMEVDDirectory(PTDE_PATH + "/event")
    ed.write_evs("vanilla")

    # Test EVS read.
    EMEVDDirectory("vanilla")
    print("PTDE `vanilla` events successfully written and re-read.")


if __name__ == '__main__':
    main()

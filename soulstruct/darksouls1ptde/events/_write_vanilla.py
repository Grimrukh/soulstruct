from soulstruct.darksouls1ptde.events.emevd_directory import EMEVDDirectory
from soulstruct.config import PTDE_PATH


def main():
    ed = EMEVDDirectory(PTDE_PATH + "/event")
    ed.write_evs("vanilla")

    ed.write_numeric("vanilla_numeric")

    re_ed = EMEVDDirectory("vanilla")
    re_ed.write_evs("re_vanilla")
    re_ed.write_numeric("re_vanilla_numeric")


if __name__ == '__main__':
    main()

from soulstruct.darksouls3.events import EMEVDDirectory
from soulstruct.config import DS3_PATH


def main():
    ed = EMEVDDirectory(DS3_PATH + "/event")
    ed.write_evs("vanilla")

    # Test EVS read.
    EMEVDDirectory("vanilla")
    print("DS3 `vanilla` events successfully written and re-read.")


if __name__ == '__main__':
    main()

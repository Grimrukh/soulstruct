from soulstruct.config import Config
from soulstruct.darksouls1r.params.draw_param import DrawParamDirectory


def main():
    dpd = DrawParamDirectory.from_path(Config.DSR_PATH / "param/DrawParam")
    print(dpd.a10.BakedLight_0)


if __name__ == '__main__':
    main()

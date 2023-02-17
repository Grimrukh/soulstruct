import matplotlib.pyplot as plt

from soulstruct.base.models.flver import FLVER


def draw_skeleton(flver: FLVER):
    """Figure out how to properly resolve bones in a nice way, with connected heads and tails, for Blender."""
    fig = plt.figure(figsize=(8, 8))
    axes = fig.add_subplot(111, projection="3d")

    bones = flver.bones

    for bone in bones:
        abs_translate = bone.get_absolute_translate(flver.bones)
        axes.scatter(abs_translate[0], abs_translate[2], abs_translate[1])

    for x in (-1.5, 1.5):
        for y in (-1.5, 1.5):
            for z in (0, 3):
                axes.scatter(x, y, z)

    plt.show()


def test():
    f = FLVER.from_path("resources/c2800.flver")
    draw_skeleton(f)


if __name__ == '__main__':
    test()

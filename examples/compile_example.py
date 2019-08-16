""" Run this script to compile our example DS1 EVS script, 'example.py'. """

from soulstruct.events.darksouls1 import EMEVD


def compile_evs():
    """ Feed our EVS script to the EMEVD() class.

    The EMEVD class can read packed '.events' resources, numeric '.txt' resources (in the format designed by
    HotPocketRemix), or Pythonic '.evs' / '.py' resources. You can then output the same EMEVD as any of those three file
    game_types.

    Note that the EMEVD class must be imported from the appropriate game sub-module, as each game changes the EMEVD
    structure and instruction set somewhat.

    The 'verbose' format used by HotPocketRemix is no longer supported here, because maintaining all these different
    formats is considerable work and EVS does a good impression of a verbose format anyway. You're obviously still free
    to use HotPocket's tools to generate those verbose outputs for inspection (you can use the same numeric files).
    """
    # Again, I've used the '.py' extension here for rather than '.evs' so that code is colored on GitHub.
    example_emevd = EMEVD('example.py')

    # We can convert our EMEVD file to numeric data (probably only useful for legacy reasons):
    example_emevd.write_numeric()  # If no file path is specified, the input path is used with a new extension.

    # And pack it to final EMEVD binary, ready to be moved to your Dark Souls 'event' folder. You can pass a specific
    # EMEVD file path to this method, but by default it will use your original EVS script path with the extension
    # changed to '.events'.
    example_emevd.write_emevd()

    # We can also decompile our script again to get a readable version back. If you see a bug, and suspect it's my
    # fault, this is a good way to check if the line-for-line instructions decompiled here are what you'd expect based
    # on the higher-level syntax in EVS.
    example_emevd.write_evs('re-example.py')

    # Now try replacing 'example.evs' above with 'example.events', and you should see the exact same output.


if __name__ == '__main__':
    compile_evs()

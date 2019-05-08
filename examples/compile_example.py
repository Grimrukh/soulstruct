
# Run this script to compile our example EVS script.

from soulstruct.emevd import EMEVD

if __name__ == '__main__':

    # Feed our script to the Emevd() class, which will read essentially anything you give it and convert it into a
    # fully transparent EMEVD structure. (Thank our EMEVD messiah, HotPocketRemix, for mapping the file structure.)
    example_emevd = EMEVD('example_evs.py')

    # We can convert our EMEVD file to numeric data (probably only useful for legacy reasons):
    print("\nNUMERIC:\n")
    print(example_emevd.to_numeric())
    example_emevd.write_numeric()

    # Or convert it to verbose, where you can see the final compiled instructions:
    print("\nVERBOSE:\n")
    print(example_emevd.to_verbose())
    example_emevd.write_verbose()

    # You can also 'decompile' your script and write it back to EVS, though only line-for-line instructions and tests
    # will be used (note the missing IF blocks, and so on):
    example_emevd.write_evs()

    # And pack it to final EMEVD binary, ready to be moved to your Dark Souls 'event' folder. You can pass a specific
    # EMEVD file path to this method, but by default it will use your original EVS script path with the extension
    # changed to '.emevd'.
    example_emevd.write_packed()

    # Now try replacing 'example.evs' above with 'example.emevd', and you should see the exact same output.

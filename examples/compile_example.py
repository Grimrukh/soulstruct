
# Run this script to compile our example EVS script.

from emevd import Emevd

if __name__ == '__main__':

    # Feed our script to the Emevd() class, which will read essentially anything you give it and convert it into a
    # fully transparent EMEVD structure. (Thank our EMEVD messiah, HotPocketRemix, for mapping the file structure.)
    example_emevd = Emevd('example.py')

    # We can convert our EMEVD file to numeric data (probably only useful for legacy reasons):
    print("NUMERIC:\n")
    print(example_emevd.to_numeric())

    # Write it to a text file. You can pass a specific file path to this method, but by default it will use your
    # original EVS/PY script path with the extension changed to 'numeric.txt'.
    example_emevd.write_numeric()

    # Or convert it to verbose, where you can see the final compiled instructions:
    print("VERBOSE:\n")
    print(example_emevd.to_verbose())

    # Write it to a text file. Defaults to '{script_name}.verbose.txt'.
    example_emevd.write_verbose()

    # And pack it to final EMEVD binary, ready to be moved to your Dark Souls 'event' folder. Name defaults to
    # '{script_name}.emevd'.
    example_emevd.write_packed()

    # Now try replacing 'example.py' above with 'example.emevd', and you should see the exact same output. You can
    # also replacing it with 'example.numeric.txt', but not the verbose file, which is output only (just like EVS is
    # input only).

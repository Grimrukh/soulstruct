# soulstruct
Python tools for inspecting and modding From Software games, including an "all-in-one" graphical interface.

**YouTube channel with tutorials: https://youtube.com/grimrukh**

**Like my stuff? Consider supporting me on Patreon <3 https://patreon.com/Grimrukh**

Game abbreviations used below and in package:
- **DS1PTDE**: Dark Souls: Prepare to Die Edition
- **DS1R**: Dark Souls Remastered
- **DS2**: Dark Souls II (either version)
- **BB**: Bloodborne
- **DS3**: Dark Souls III
- **SEK**: Sekiro: Shadows Die Twice

Features
--------

- Unified graphical application for modifying maps, events, parameters, text, AI, and talk scripts in *Dark Souls* 
  (both versions) and *Bloodborne*. Game data is imported as a **project**, edited in the window (or in Python if you 
  prefer), and exported back to game-ready files whenever you want. Keep track of map entities, quickly navigate between 
  data types, and view custom syntax highlighting for event scripts and AI scripts.
  - Supported games: DS1PTDE, DS1R, BB

- Event scripts (**EMEVD**) and EzState state machines (**ESD**) can be translated to and from valid Python-based 
languages with high-level programming features.
    - Supported games: DS1PTDE, DS1R, DS2 (ESD only), BB, DS3

- Map data (**MSB**), game parameters (**GameParam**), lighting parameters (**DrawParam**), text data (**FMG**) can be 
loaded into Python structures, edited, and repacked.
    - Supported games: DS1PTDE, DS1R, BB (map, game parameters, and text only), DS3 (map and text only)

- AI scripts in can be decompiled, edited, and recompiled.
    - Supported games: DS1PTDE (no decompiling), DS1R

- Unpack/repack **BND** archives and automatically manage **DCX** compression.
    - Supported games: all

- Includes some of my ongoing documentation for vanilla game IDs in *Dark Souls* and *Bloodborne*.

One-Click Executable
--------------------

Soulstruct can be downloaded as an executable, which is basically just a bundle that includes Python and runs
the `__main__.py` script when clicked (i.e. the command `python -m soulstruct`). You might find this easier to use, but
there will be a slight delay every time you run it as the bundle unpacks itself. Note that this executable will be 
updated less often than the main package and does not grant access to many of the utilities that can be imported in 
Python!

Important
---------

Soulstruct is very much a work in progress. Internal code structure should be fairly stable as of version 1.0.0 
(Feb 12, 2021, but it is still possible that changes will break backward compatibility with past versions of Soulstruct
for existing project files (**.ssp** files). If you update Soulstruct to a new major version, you may need to **export**
all game files from your old version's project first and **import** them into a new project created with the new 
Soulstruct, since the new Soulstruct version may not be able to read the old **.ssp** files. Luckily, this is 
straightforward.

Any event/ESD/AI scripts can be simply copied into the new project. If any EMEVD or ESD instruction/argument names have
been updated (as we constantly discover new things), the old names will be deprecated first and eventually removed. A
simple find-and-replace should fix any issues here.

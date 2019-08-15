from soulstruct.text import DarkSoulsText

PTD_VANILLA_DIR = 'G:/Steam/steamapps/common/Dark Souls Prepare to Die Edition/pre-doa-backup/msg/ENGLISH'
PTD_DOA_DIR = 'G:/Steam/steamapps/common/Dark Souls Prepare to Die Edition/PTD_DOA_DATA/msg/ENGLISH'
DSR_VANILLA_DIR = 'G:/Steam/steamapps/common/DARK SOULS REMASTERED/vanilla/msg/ENGLISH'
DSR_LIVE_DIR = 'G:/Steam/steamapps/common/DARK SOULS REMASTERED/msg/ENGLISH'

ELEMENTS = ('Crystal ', 'Voltaic ', 'Raw ', 'Magic ', 'Runic ', 'Blessed ', 'Profane ', 'Fire ', 'Chthonic ')


def doa_dsr_merge():
    """ Overwrites vanilla DSR text entries with DOA text entries. """
    ptd_doa = DarkSoulsText(PTD_DOA_DIR)
    dsr_vanilla = DarkSoulsText(DSR_VANILLA_DIR)
    for fmg_name, fmg in dsr_vanilla:
        fmg.update(ptd_doa[fmg_name])
    dsr_vanilla.write(msg_directory=DSR_LIVE_DIR, separate_patch=False, dcx=True)


def get_doa_changed_text(original_strings_only=True):
    ptd_vanilla = DarkSoulsText(PTD_VANILLA_DIR)
    ptd_doa = DarkSoulsText(PTD_DOA_DIR)
    changed = {}  # {fmg_name: text}

    for fmg_name, fmg_dict in ptd_doa:
        vanilla_fmg = ptd_vanilla[fmg_name]
        for entry_id, text in fmg_dict.items():
            # Strip newlines from end.
            text = text.rstrip('\n')
            vanilla_text = vanilla_fmg.get(entry_id, '').rstrip('\n')

            if vanilla_text != text:
                changed_fmg = changed.setdefault(fmg_name, {})

                # Check for carbon copy.
                existing_ids = [key for key in changed_fmg.keys() if changed_fmg[key] == text]
                if existing_ids:
                    changed_fmg[entry_id] = existing_ids[0]
                    continue

                # Check for copy with '+UpgradeNumber'.
                stripped_text = text.rstrip(' +0123456789')
                existing_ids_stripped = [key for key in changed_fmg.keys() if changed_fmg[key] == stripped_text]
                if existing_ids_stripped:
                    changed_fmg[entry_id] = (existing_ids_stripped[0], text.replace(stripped_text, ''))
                    continue

                # Check for copy with a weapon element at the front.
                for element in ELEMENTS:
                    if text.startswith(element):
                        stripped_text = text[len(element):]
                        existing_ids_stripped = [key for key in changed_fmg.keys() if changed_fmg[key] == stripped_text]
                        if existing_ids_stripped:
                            changed_fmg[entry_id] = (element, existing_ids_stripped[0])
                            continue

                # Otherwise, record full changed text.
                changed_fmg[entry_id] = text

    for fmg_name, changed_fmg in changed.items():
        print(f"{fmg_name}:")
        if original_strings_only:
            [print(f"    {k}: {repr(v)}") for k, v in changed_fmg.items() if isinstance(v, str)]
        else:
            [print(f"    {k}: {repr(v)}") for k, v in changed_fmg.items()]


if __name__ == '__main__':
    doa_dsr_merge()

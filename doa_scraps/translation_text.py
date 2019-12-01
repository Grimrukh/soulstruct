from soulstruct.text import DarkSoulsText

lang = 'JAPANESE'
version = 'DSR'

foreign_changes_paths = {
    'JAPANESE': 'C:/Users/seven/Downloads/DoA_Translations_FinalDraft.txt',
    'RUSSIAN': 'C:/Users/seven/Downloads/DoA - Russian.txt',
}

foreign_msg_paths = {
    'PTDE': f'C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA/MSG/{lang}',
    'DSR': f'C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Remastered/MSG/{lang}',
}

output = f'C:/Users/seven/Documents/Dark Souls/dump/MSG/DOA_{lang}_{version}'
# output = f'C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA/MSG/{lang}'


def get_translations():
    english = {}
    changes = {}
    with open(foreign_changes_paths[lang], encoding='utf-16le') as f:
        f.readline()  # Skip column labels.
        for i, line in enumerate(f):
            try:
                fmg, text_id, _, doa_english, new = line.rstrip('\n').split('\t')[:5]
                fmg = fmg.replace('Item', 'Good').replace('Magic', 'Spell').replace('Blood', 'Soapstone')
                fmg = fmg.replace('EventTexts', 'EventText').replace('Movie', 'Opening')
                new = new.strip('\"').replace('\\n', '\n')
                changes[fmg, int(text_id)] = new
                english[fmg, int(text_id)] = doa_english
            except ValueError:
                print(f'Error (line {i + 1}): {line}')
    return changes, english


def main():
    foreign_text = DarkSoulsText(foreign_msg_paths[version])
    r, e = get_translations()
    for fmg, text_id in r.keys():
        foreign_text[fmg][text_id] = r[fmg, text_id]

    foreign_text.save(output, description_word_wrap_limit=None, separate_patch=True)


if __name__ == '__main__':
    main()

from io import BytesIO
import os
from shutil import copyfile
from soulstruct.core import BinaryStruct, read_chars
from soulstruct.dcx import DCX


class BNDEntry(object):

    def __init__(self, entry_id: int, name: str, data: bytes):
        self.id = entry_id  # Index used by the game engine to access the packed data.
        self.name = name  # Full internal 'path'. Encoded in shift-jis and uses (escaped) backslashes in path.
        self.data = data  # Packed binary data, identical to what the unpacked file of this name would look like.

    @property
    def data_size(self):
        return len(self.data)

    @property
    def packed_name(self):
        """ Encodes name in Japanese and null-terminates. """
        return self.name.encode('shift-jis') + b'\x00'

    @property
    def basename(self):
        return os.path.basename(self.name)

    def __eq__(self, other_bnd_entry):
        return self.id == other_bnd_entry.id and self.name == other_bnd_entry.name and self.data == other_bnd_entry.data

    def copy(self):
        return BNDEntry(self.id, self.name, self.data)


class BND(object):

    HEADER_STRUCT = BinaryStruct(
        ('bnd_version', '4s', b'BND3'),
        ('bnd_signature', '8s'),  # Real signature may be shorter, but packing will pad it out.
        ('bnd_flag', 'i'),
        ('entry_count', 'i'),
        ('file_size', 'i'),
        '8x',
    )

    BND_ENTRY_HEADER = BinaryStruct(
        ('sep', 'i', 64),
        ('data_size', 'i'),
        ('data_offset', 'i'),
        ('entry_id', 'i'),
        ('name_offset', 'i'),
        ('data_size_repeat', 'i'),
    )

    BND_ENTRY_HEADER_0x70 = BinaryStruct(
        ('sep', 'i', 64),
        ('data_size', 'i'),
        ('data_offset', 'i'),
        ('entry_id', 'i'),
        ('name_offset', 'i'),
    )

    def __init__(self, bnd_source=None):
        """ Source can be a .*bnd file, an unpacked BND directory (or the 'bnd_manifest.txt' file inside it), or
        raw bytes or an open file stream. """

        self.bnd_path = ''  # Always a '.bnd' file path after the BND is loaded.
        self.bnd_version = b''
        self.bnd_signature = b''
        self.bnd_flag = None
        self._dcx_source = False

        self._entries = []

        if isinstance(bnd_source, str):
            if os.path.isfile(bnd_source) and os.path.basename(bnd_source) == 'bnd_manifest.txt':
                bnd_source = os.path.dirname(bnd_source)
            if os.path.isdir(bnd_source):
                if bnd_source.endswith('.unpacked'):
                    self.bnd_path = os.path.abspath(bnd_source)[:-len('.unpacked')]
                else:
                    self.bnd_path = os.path.abspath(bnd_source)
                self.open_from_unpacked_dir(bnd_source)
            else:
                self.bnd_path = os.path.abspath(bnd_source)
                if bnd_source.endswith('.dcx'):
                    self.unpack_from_data(DCX(bnd_source).data)
                    self._dcx_source = True
                else:
                    with open(bnd_source, 'rb') as file:
                        self.unpack_from_data(file)
        elif bnd_source is not None:
            self.unpack_from_data(bnd_source)

    def unpack_from_data(self, bnd_buffer):

        if isinstance(bnd_buffer, bytes):
            bnd_buffer = BytesIO(bnd_buffer)

        header = self.HEADER_STRUCT.unpack(bnd_buffer)
        self.bnd_version = header['bnd_version']
        self.bnd_signature = header['bnd_signature']
        self.bnd_flag = header['bnd_flag']

        self._entries = []

        if header.bnd_flag in (0x74, 0x54):
            entry_headers = self.BND_ENTRY_HEADER.unpack(bnd_buffer, count=header['entry_count'])
        elif header.bnd_flag == 0x70:
            entry_headers = self.BND_ENTRY_HEADER_0x70.unpack(bnd_buffer, count=header['entry_count'])
        else:
            raise ValueError(f"Unrecognized BND flag: {hex(header.bnd_flag)}. "
                             f"Should be 0x54, 0x70, or 0x74.")

        for entry in entry_headers:
            bnd_buffer.seek(entry.data_offset)
            entry_name = read_chars(bnd_buffer, offset=entry.name_offset, encoding='shift-jis')
            entry_data = bnd_buffer.read(entry.data_size)
            self.add_entry(BNDEntry(entry_id=entry.entry_id, name=entry_name, data=entry_data))

    def write(self, bnd_path=None):
        if bnd_path is None:
            bnd_path = self.bnd_path

        if not (bnd_path.endswith('bnd') or bnd_path.endswith('bnd.dcx')):
            # Note this doesn't check for '.bnd' as the exact extension (e.g. '.msgbnd' is valid).
            bnd_path += '.bnd'

        if not os.path.isfile(bnd_path + '.bak'):
            print(f"# INFO: Created '{bnd_path + '.bak'}' backup file.")
            copyfile(bnd_path, bnd_path + '.bak')

        packed = self.pack()

        if bnd_path.endswith('.dcx'):
            # Apply DCX compression.
            packed = DCX(packed).pack()

        with open(bnd_path, 'wb') as f:
            f.write(packed)

    def pack(self):

        if self.bnd_flag in (0x74, 0x54):
            ENTRY_HEADER_STRUCT = self.BND_ENTRY_HEADER
        elif self.bnd_flag == 0x70:
            ENTRY_HEADER_STRUCT = self.BND_ENTRY_HEADER_0x70
        else:
            raise ValueError(f"Unrecognized BND flag: {hex(self.bnd_flag)}. "
                             f"Should be 0x54, 0x70, or 0x74.")

        entry_headers = []
        packed_entry_headers = b''
        packed_entry_names = b''
        relative_entry_name_offsets = []
        packed_entry_data = b''
        relative_entry_data_offsets = []

        for entry in self._entries:

            entry_header_dict = {
                'data_size': entry.data_size,
                'data_offset': len(packed_entry_data),
                'entry_id': entry.id,
                'name_offset': len(packed_entry_names),
                'data_size_repeat': entry.data_size,
            }

            relative_entry_name_offsets.append(len(packed_entry_names))  # Relative to start of packed entry names.
            packed_entry_names += entry.packed_name
            relative_entry_data_offsets.append(len(packed_entry_data))
            packed_entry_data += entry.data
            entry_headers.append(entry_header_dict)

        # Compute table offsets.
        entry_header_table_offset = self.HEADER_STRUCT.size
        entry_name_table_offset = entry_header_table_offset + ENTRY_HEADER_STRUCT.size * len(self._entries)
        entry_packed_data_offset = entry_name_table_offset + len(packed_entry_names)
        bnd_file_size = entry_packed_data_offset + len(packed_entry_data)

        # Pack BND header.
        packed_header = self.HEADER_STRUCT.pack(
            bnd_signature=self.bnd_signature,
            bnd_flag=self.bnd_flag,
            entry_count=len(self._entries),
            file_size=bnd_file_size,
        )

        # Convert relative offsets to absolute and pack entry headers.
        for entry_header_dict in entry_headers:
            entry_header_dict['data_offset'] += entry_packed_data_offset
            entry_header_dict['name_offset'] += entry_name_table_offset
            if self.bnd_flag == 0x70:
                entry_header_dict.pop('data_size_repeat')
            packed_entry_headers += ENTRY_HEADER_STRUCT.pack(entry_header_dict)

        return packed_header + packed_entry_headers + packed_entry_names + packed_entry_data

    def open_from_unpacked_dir(self, directory):

        if not os.path.isdir(directory):
            raise ValueError('Could not find extracted path of that BND name.')

        with open(os.path.join(directory, 'bnd_manifest.txt'), 'rb') as f:

            version_and_signature = f.readline()
            self.bnd_version = version_and_signature[:4]
            self.bnd_signature = version_and_signature[4:]
            self.bnd_flag = int(f.readline())

            current_directory = None

            for line in f:
                line.strip(b'\r\n')
                if line.startswith(b' PATH: '):
                    current_directory = line[7:].replace(b'/', b'\\').decode('shift-jis').strip('\r\n')
                else:
                    entry_id, entry_basename = line.split(b': ')
                    entry_basename_jis = entry_basename.decode('shift-jis').strip('\r\n')
                    entry_name = '\\'.join((current_directory, entry_basename_jis))

                    with open(os.path.join(directory, entry_basename_jis), 'rb') as entry_file:
                        entry_data = entry_file.read()

                    self.add_entry(BNDEntry(entry_id=int(entry_id), name=entry_name, data=entry_data))

    @property
    def entries(self):
        return self._entries

    @property
    def entries_by_id(self):
        return {entry.id: entry for entry in self._entries}

    @property
    def entries_by_path(self):
        return {entry.name: entry for entry in self._entries}

    @property
    def entries_by_basename(self):
        """ You are technically allowed to have the same basename appear in multiple paths in a BND, but that will
        never happen naturally (AFAIK) and I don't recommend you ever let it happen. """
        entries = {}
        for entry in self._entries:
            basename = os.path.basename(entry.name)
            if basename in entries:
                raise ValueError(f"Basename '{basename}' appears in multiple BND entry paths.")
            entries[basename] = entry
        return entries

    def __getitem__(self, id_or_path_or_basename):
        """ Shortcut for access by ID (int) or path/basename (str). """
        if isinstance(id_or_path_or_basename, int):
            return self.entries_by_id[id_or_path_or_basename]
        elif isinstance(id_or_path_or_basename, str):
            try:
                return self.entries_by_path[id_or_path_or_basename]
            except KeyError:
                return self.entries_by_basename[id_or_path_or_basename]
        else:
            raise TypeError("Key should be an entry ID (int) or path/basename (str).")

    def __iter__(self):
        return iter(self._entries)

    def add_entry(self, entry: BNDEntry):
        if entry.id in self.entries_by_id:
            raise ValueError(f"Entry with ID {entry.id} already exists in BND.")
        if entry.name in self.entries_by_id:
            raise ValueError(f"Entry with path '{entry.name}' already exists in BND.")
        self._entries.append(entry)

    def remove_entry(self, id_or_path_or_basename):
        if isinstance(id_or_path_or_basename, int):
            entry = self.entries_by_id[id_or_path_or_basename]
        elif isinstance(id_or_path_or_basename, str):
            try:
                entry = self.entries_by_path[id_or_path_or_basename]
            except KeyError:
                entry = self.entries_by_basename[id_or_path_or_basename]
        else:
            raise TypeError("Entry to be removed should be a BND ID (int) or path/basename (str).")
        self._entries.remove(entry)

    def write_unpacked(self, directory=None):

        if directory is None:
            directory = self.bnd_path + '.unpacked'
        else:
            directory = os.path.join(directory, f'{os.path.basename(self.bnd_path)}.unpacked')

        current_directory = ''
        manifest_lines = []

        for entry in self._entries:

            entry_directory = os.path.dirname(entry.name).replace('\\', '/')  # File uses forward slashes.
            if entry_directory != current_directory:
                # Write new path group to file list.
                manifest_lines.append(f" PATH: {entry_directory}")
                current_directory = entry_directory

            manifest_lines.append(f"{entry.id}: {os.path.basename(entry.name)}")

            os.makedirs(directory, exist_ok=True)

            with open(os.path.join(directory, os.path.basename(entry.name)), 'wb') as f:
                f.write(entry.data)

        with open(os.path.join(directory, 'bnd_manifest.txt'), 'w', encoding='shift-jis') as f:
            f.write(f"BND3{self.bnd_signature.decode()}\n"
                    f"{self.bnd_flag}\n")
            f.write("\n".join(manifest_lines))

    @property
    def entry_count(self):
        return len(self._entries)


if __name__ == '__main__':
    item = BND('examples/item.msgbnd')

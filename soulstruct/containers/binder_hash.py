from __future__ import annotations

__all__ = ["BinderHashTable"]

from dataclasses import dataclass, field

from soulstruct.utilities.binary import *


@dataclass(slots=True)
class HashTableHeader(BinaryStruct):
    _pad1: bytes = field(init=False, **BinaryPad(8))
    path_hashes_offset: long
    hash_group_count: uint
    _unknown3: int = field(init=False, **Binary(asserted=0x00080810))


@dataclass(slots=True)
class PathHash(BinaryStruct):
    hashed_value: uint
    entry_index: int


@dataclass(slots=True)
class HashGroup(BinaryStruct):
    length: int
    index: int


class BinderHashTable:

    @classmethod
    def build_hash_table(cls, entries):
        """Some binder files include tables of hashed entry paths, which aren't needed to read file contents, but
        need to be re-hashed to properly pack the file in case any paths have changed (or the number of entries)."""

        # Group count set to first prime number greater than or equal to the number of entries divided by 7.
        for p in range(len(entries) // 7, 100000):
            if cls.is_prime(p):
                group_count = p
                break
        else:
            raise ValueError("Hash group count could not be determined.")

        hashes = []
        hash_lists = [[] for _ in range(group_count)]  # type: list[list[tuple[int, int]]]

        for entry_index, entry in enumerate(entries):
            hashes.append(cls.path_hash(entry.path))
            list_index = hashes[-1] % group_count
            hash_lists[list_index].append((hashes[-1], entry_index))

        for hash_list in hash_lists:
            hash_list.sort()  # Sort by hash value.

        hash_groups = []
        path_hashes = []

        total_hash_count = 0
        for hash_list in hash_lists:
            first_hash_index = total_hash_count
            for path_hash in hash_list:
                path_hashes.append(PathHash(hashed_value=uint(path_hash[0]), entry_index=path_hash[1]))
                total_hash_count += 1
            hash_groups.append(HashGroup(index=first_hash_index, length=total_hash_count - first_hash_index))

        packed_hash_groups = HashGroup.join_bytes(hash_groups)
        packed_hash_table_header = bytes(HashTableHeader(
            path_hashes_offset=long(HashTableHeader.get_size() + len(packed_hash_groups)),
            hash_group_count=uint(group_count),
        ))
        packed_path_hashes = PathHash.join_bytes(path_hashes)

        return packed_hash_table_header + packed_hash_groups + packed_path_hashes

    @staticmethod
    def path_hash(path_string: str):
        """Simple string-hashing algorithm used by FROM.

        Strings use forward-slash path separators and always start with a forward slash.
        """
        hashable = path_string.replace("\\", "/")
        if not hashable.startswith("/"):
            hashable = "/" + hashable
        h = 0
        for i, s in enumerate(hashable):
            h += i * 37 + ord(s)
        return h

    @staticmethod
    def is_prime(p):
        if p < 2:
            return False
        if p == 2:
            return True
        if (p % 2) == 0:
            return False
        for i in range(3, p // 2, 2):
            if (p % i) == 0:
                return False
            if i ** 2 > p:
                return True
        return True

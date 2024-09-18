from soulstruct.dcx import oodle


def test():
    oodle.LOAD_DLL()
    raw_data = b"11112222333344445555"
    compressed = oodle.compress(
        raw_data,
        oodle.Compressor.Kraken,
        oodle.CompressionLevel.Fast,
    )
    print(f"Compress test: {raw_data} -> {compressed}")
    decompressed = oodle.decompress(compressed, len(raw_data))
    print(f"    Decompress test: -> {decompressed}")
    print(f"    Test succeeded? {raw_data == decompressed}")

from io import BytesIO
from .wow_common_types import ChunkHeader
from .m2_format import *
from .m2_chunks import AFID, BFID


class SKL1:
    _size = 16

    def __init__(self, size=12):
        self.header = ChunkHeader(magic='SKL1')
        self.header.size = size
        self.unk1 = 0
        self.name = M2Array(char)
        self.unk2 = []

    def read(self, f):
        raw_data = f.read(self.header.size)

        with BytesIO(raw_data) as f2:
            self.unk1 = uint32.read(f2)
            self.name.read(f2)
            self.unk2 = [uint8.read(f2) for _ in range(4)]

    def write(self, f):
        self.header.size = len(self.unk2) + self.unk1 * 4 + self.name.n_elements * char.size_() + self._size
        self.header.write(f)

        with BytesIO() as f2:
            MemoryManager.mem_reserve(f2, self._size)
            self.name.write(f2)
            uint32.write(f2, self.unk1)

            for val in self.unk2:
                uint8.write(f2, val)

            f2.seek(0)

        f.write(f2.read())


class SKA1:
    _size = 16

    def __init__(self, size=0):
        self.header = ChunkHeader(magic='SKA1')
        self.header.size = size
        self.attachments = M2Array(M2Attachment)
        self.attachment_lookup_table = M2Array(uint16)

    def read(self, f):
        raw_data = f.read(self.header.size)

        with BytesIO(raw_data) as f2:
            self.attachments.read(f2)
            self.attachment_lookup_table.read(f2)

    def write(self, f):
        self.header.size = self.attachments.n_elements * M2Attachment.size() \
                           + self.attachment_lookup_table.n_elements * 2 + self._size
        self.header.write(f)

        with BytesIO() as f2:
            MemoryManager.mem_reserve(f2, self._size)
            self.attachments.write(f2)
            self.attachment_lookup_table.write(f2)
            f2.seek(0)

        f.write(f2.read())


class SKB1:
    _size = 16

    def __init__(self, size=0):
        self.header = ChunkHeader(magic='SKB1')
        self.header.size = size
        self.bones = M2Array(M2CompBone)
        self.key_bone_lookup = M2Array(uint16)

    def read(self, f):
        raw_data = f.read(self.header.size)

        with BytesIO(raw_data) as f2:
            self.bones.read(f2)
            self.key_bone_lookup.read(f2)

    def write(self, f):
        self.header.size = self.bones.n_elements * M2Attachment.size() + self.key_bone_lookup.n_elements * 2 + self._size
        self.header.write(f)

        with BytesIO() as f2:
            MemoryManager.mem_reserve(f2, self._size)
            self.bones.write(f2)
            self.key_bone_lookup.write(f2)
            f2.seek(0)

        f.write(f2.read())


class SKS1:
    _size = 32

    def __init__(self, size=0):
        self.header = ChunkHeader(magic='SKS1')
        self.header.size = size
        self.global_loops = M2Array(uint32)
        self.sequences = M2Array(M2Sequence)
        self.sequence_lookups = M2Array(uint16)
        self.unk = []

    def read(self, f):
        raw_data = f.read(self.header.size)

        with BytesIO(raw_data) as f2:
            self.global_loops.read(f2)
            self.sequences.read(f2)
            self.sequence_lookups.read(f2)

            self.unk = [uint8.read(f2) for _ in range(8)]

    def write(self, f):
        self.header.size = len(self.unk) + self.global_loops.n_elements * 4 + self.sequences.n_elements * \
                           M2Sequence.size() + self.sequence_lookups.n_elements * 2 + self._size
        self.header.write(f)

        with BytesIO() as f2:
            self.global_loops.write(f2)
            self.sequences.write(f2)
            self.sequence_lookups.write(f2)

            for val in self.unk:
                uint8.write(f2, val)

            f2.seek(0)

        f.write(f2.read())


class SKPD:

    def __init__(self, size=0):
        self.header = ChunkHeader(magic='SKPD')
        self.header.size = size
        self.parent_skel_file_id = 0

        self.unk1 = []
        self.unk2 = []

    def read(self, f):
        self.parent_skel_file_id = uint32.read(f)

        self.unk1 = [uint8.read(f) for _ in range(8)]
        self.unk2 = [uint8.read(f) for _ in range(4)]

    def write(self, f):
        self.header.size = len(self.unk1) + len(self.unk2) + self.parent_skel_file_id * 4

        for val in self.unk1:
            uint8.write(f, val)

        for val in self.unk2:
            uint8.write(f, val)

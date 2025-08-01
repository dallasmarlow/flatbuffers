# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StructOfStructsOfStructs(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 20

    # StructOfStructsOfStructs
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StructOfStructsOfStructs
    def A(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 0)
        return obj


def CreateStructOfStructsOfStructs(builder, a_a_id, a_a_distance, a_b_a, a_b_b, a_c_id, a_c_distance):
    builder.Prep(4, 20)
    builder.Prep(4, 20)
    builder.Prep(4, 8)
    builder.PrependUint32(a_c_distance)
    builder.PrependUint32(a_c_id)
    builder.Prep(2, 4)
    builder.Pad(1)
    builder.PrependInt8(a_b_b)
    builder.PrependInt16(a_b_a)
    builder.Prep(4, 8)
    builder.PrependUint32(a_a_distance)
    builder.PrependUint32(a_a_id)
    return builder.Offset()

import MyGame.Example.StructOfStructs
try:
    from typing import Optional
except:
    pass

class StructOfStructsOfStructsT(object):

    # StructOfStructsOfStructsT
    def __init__(
        self,
        a = None,
    ):
        self.a = a  # type: Optional[MyGame.Example.StructOfStructs.StructOfStructsT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        structOfStructsOfStructs = StructOfStructsOfStructs()
        structOfStructsOfStructs.Init(buf, pos)
        return cls.InitFromObj(structOfStructsOfStructs)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, structOfStructsOfStructs):
        x = StructOfStructsOfStructsT()
        x._UnPack(structOfStructsOfStructs)
        return x

    # StructOfStructsOfStructsT
    def _UnPack(self, structOfStructsOfStructs):
        if structOfStructsOfStructs is None:
            return
        if structOfStructsOfStructs.A(MyGame.Example.StructOfStructs.StructOfStructs()) is not None:
            self.a = MyGame.Example.StructOfStructs.StructOfStructsT.InitFromObj(structOfStructsOfStructs.A(MyGame.Example.StructOfStructs.StructOfStructs()))

    # StructOfStructsOfStructsT
    def Pack(self, builder):
        return CreateStructOfStructsOfStructs(builder, self.a.a.id, self.a.a.distance, self.a.b.a, self.a.b.b, self.a.c.id, self.a.c.distance)

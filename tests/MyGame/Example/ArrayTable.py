# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers

class ArrayTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsArrayTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArrayTable()
        x.Init(buf, n + offset)
        return x

    # ArrayTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayTable
    def A(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .ArrayStruct import ArrayStruct
            obj = ArrayStruct()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ArrayTableStart(builder): builder.StartObject(1)
def ArrayTableAddA(builder, a): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(a), 0)
def ArrayTableEnd(builder): return builder.EndObject()

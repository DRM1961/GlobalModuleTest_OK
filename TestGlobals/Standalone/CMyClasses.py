import MyGlobals as G
from random import randrange


class CMyClassData():
    def __init__(self):
        self.data = 1
        return

    def SetData(self, newdata):
        self.data = newdata
        return

    def GetData(self):
        return(self.data)


class CMyClassProcess():
    def __init__(self):
        self.ptr_passed_to_class = None
        self.ptr_taken_from_global = G.CData
        return

    def SetPointers(self, cdata):
        self.ptr_passed_to_class = cdata
        return

    def Process(self, startval):
        data = randrange(startval, startval+10)
        self.SetData(data)

    def SetData(self, newdata):
        self.ptr_passed_to_class.SetData(newdata)
        self.ptr_taken_from_global.SetData(newdata)
        return

    def GetData(self):
        return(self.ptr_passed_to_class.GetData(),\
               self.ptr_taken_from_global.GetData())

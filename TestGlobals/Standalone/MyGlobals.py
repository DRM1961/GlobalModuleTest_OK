
from CMyClasses import CMyClassProcess as myprocess
from CMyClasses import CMyClassData as mydata


CData = None
CProcess1 = None
CProcess2 = None

def InitMyGlobals():
    global CData
    global CProcess1
    global CProcess2

    CData = mydata()
    CProcess1 = myprocess()
    CProcess2 = myprocess()

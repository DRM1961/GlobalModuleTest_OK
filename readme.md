problems changing data in global instance of a class from within 2 other global instances of another class

CMyClasses.py: contains a data class and a process class that interacts with the data class
MyGlobals.py: instances of classes on global level
main.py : contains flow to changing data 

problem definition:
CMyClasses.CMyClassProcess has 2 pointers to an instance of CMyClassData defined in MyGlobals
- self.ptr_taken_from_global = taken from MyGlobals during init of class
- self.ptr_passed_to_class = passed from main in flow

Depending on the configuration, standalone or as a module, CMyClasses.CMyClassProcess.ptr_taken_from_global is 
not the same as self.ptr_passed_to_class (from the globals that main sees)

working configuration
files
C:\TestGlobals\Standalone\main.py ("import MyGlobals as G")
C:\TestGlobals\Standalone\CMyClasses.py ("import MyGlobals as G")
C:\TestGlobals\Standalone\MyGlobals.py ("import from CMyClasses...")

failing configuration
files
C:\TestGlobals\WithModule\main.py ("import MyModule.MyGlobals as G")
C:\TestGlobals\WithModule\MyModule\CMyClasses.py ("import MyModule.MyGlobals as G")
C:\TestGlobals\WithModule\MyModule\MyGlobals.py ("import from MyModule.CMyClasses...")


When running as module with Spyder, the first time after restarting the kernel, the values are the same.
But the second time, the values are different. 
What's more, the value from the "ptr_taken_from_global" is the last value from the previous run.

Why is the behaviour different for this assignment in CMyClassProcess: self.ptr_taken_from_global = G.CData
As standalone, G.CData is the same seen from main.py as from within a MyClassProcess instance.
As module, G.CData is different from main.py as seen from within a MyClassProcess instance.
As module, both instances of MyClassProcess do see the same G.CData


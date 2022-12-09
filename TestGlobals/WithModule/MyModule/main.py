import MyGlobals as G
from random import randrange

def ShowContent():
    print(f'read from global ({G.CData.data})')
    print(f'get through process1 class {G.CProcess1.GetData()}')
    print(f'get through process2 class {G.CProcess2.GetData()}\n')


print('init globals, sets data in dataclass to 1')
G.InitMyGlobals()
print('init pointer to data class in process classes')
G.CProcess1.SetPointers(G.CData)
G.CProcess2.SetPointers(G.CData)
ShowContent()

print('Set class data to 2')
G.CData.SetData(2)
ShowContent()

print('Process 1 and change data to 0..10')
G.CProcess1.Process(0)
ShowContent()
print('Process 2 and change data to 10..20')
G.CProcess2.Process(10)
ShowContent()

data = randrange(100, 110)
print('Set class data to {data} from main')
G.CData.SetData(data)
ShowContent()

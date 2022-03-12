import queue
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Dequeue:
    def __init__(self):
        self.data = queue.Queue()
        self.help = queue.Queue()
        self.count = 0
        
    def insertFront(self, val):
        if(self.count == 10):
            print(-1)
            return
        self.help.put(val)
        for _ in range(self.count):
            self.help.put(self.data.get())
        self.help, self.data = self.data, self.help                
        self.count += 1
        
    def insertRear(self, val):
        if(self.count == 10):
            print(-1)
            return
        self.data.put(val)
        self.count += 1
        
    def deleteFront(self):
        if(self.count == 0):
            print(-1)
            return
        self.data.get()
        self.count -= 1
    
    def deleteRear(self):
        if(self.count == 0):
            print(-1)
            return
        for _ in range(self.count - 1):
            self.help.put(self.data.get())
        temp = self.data.get()
        self.count -= 1
        self.data, self.help = self.help, self.data
    
    def getFront(self):
        if(self.count == 0):
            return -1
        temp = self.data.get()
        self.help.put(temp)
        for _ in range(self.count - 1):
            self.help.put(self.data.get())
        self.data, self.help = self.help, self.data
        return temp
    
    def getRear(self):
        if(self.count == 0):
            return -1
        for _ in range(self.count - 1):
            self.help.put(self.data.get())
        temp = self.data.get()
        self.help.put(temp)
        self.data, self.help = self.help, self.data
        return temp
    
d = Dequeue()
operations = [int(ele) for ele in input().split()]
i = 0
while(operations[i] != -1):
    if(operations[i] == 1):
        d.insertFront(operations[i+1])
        i += 1
    elif(operations[i] == 2):
        d.insertRear(operations[i+1])
        i += 1
    elif(operations[i] == 3):
        d.deleteFront()
    elif(operations[i] == 4):
        d.deleteRear()
    elif(operations[i] == 5):
        print(d.getFront())
    elif(operations[i] == 6):
        print(d.getRear())  
    i += 1

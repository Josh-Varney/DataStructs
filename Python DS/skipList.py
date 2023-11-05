import random

class SLNode:
    def __init__(self, val):
        self.val = val
        self.pointer = None
        
class SkipList:
    def __init__(self):
        self.arr = []
        self.skipIndex = 0
        self.indexNode = SLNode(None)
        
        
    def appendNode(self, val):
        if not self.arr:
            self.indexNode.pointer = SLNode(val)
            self.arr.append([0, self.indexNode])
            self.skipIndex+=1
        else:
            randint = random.randint(0, len(self.arr)-1)
            currentNode = self.arr[randint][1]
            while currentNode.pointer:
                currentNode = currentNode.pointer
            currentNode.pointer = SLNode(val)
    
    def appendSkip(self, val):
        if not self.arr:
            raise ValueError('Configure SkipList First')
        else:
            self.indexNode.pointer = SLNode(val)
            self.arr.append([self.skipIndex, self.indexNode])
            self.skipIndex+=1
            
            currentNode = self.arr[0][1]
            while currentNode.pointer:
                currentNode = currentNode.pointer
            currentNode.pointer = SLNode(val)
    
    def printSkip(self):
        print(self.arr)
        
            

if __name__== '__main__':
    myskip = SkipList()
    myskip.appendNode(1)
    myskip.appendSkip(2)
    myskip.appendSkip(3)
    myskip.printSkip()
    
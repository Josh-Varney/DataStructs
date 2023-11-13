import random


class Node:
    def __init__(self, val=None):
        self.val = val
        self.pointer = None
        self.prev = None

class skipList:
    def __init__(self):
        self.headIndex = 0
        self.head = []
        
    def appendHead(self, val):
        self.head.append([self.headIndex, Node(val)])
        self.headIndex+=1
        
    def appendNode(self, val):
        if random.randint(0, 3) == 3:
            self.appendHead(val)
        else:
            currentHeadIndex = random.randint(0,len(self.head))
            if not self.head:
                self.appendHead(val)
            else:
                prevNode = None
                newNode = Node(val)
                currentHead = self.head[currentHeadIndex-1]
                currentNode = currentHead[1]
                while currentNode.pointer:
                    if currentNode.val > val:
                        prevNode.pointer = newNode
                        newNode.pointer = currentNode
                        newNode.prev = prevNode
                        return # PrevNode has no pointer
                        
                    prevNode = currentNode
                    currentNode = currentNode.pointer
            
                currentNode.prev = prevNode
                currentNode.pointer = Node(val)
                
    def insertNode(self, currentHeadIndex, val):
        if currentHeadIndex == 0:
            return
        
        while currentHeadIndex:
            currentHead = self.head[currentHeadIndex-1]
            currentNode = currentHead[1]
            
            while currentNode.pointer:
                if currentNode.val > val:
                    temp = currentNode
                    currentNode = Node(val)
                    currentNode.pointer = temp
                    
                currentNode = currentNode.pointer
            currentHeadIndex-=1
        
        
                
    def searchNode(self, targetValue):
        for headIndex in self.head:    # Append the node into all parts of the indexes
            print(headIndex)
        
                
                
         
    def __str__(self):
        lString = ''
        for currentHead in range(self.headIndex):
            lString+=f'Level {currentHead}:'
            hNode = self.head[currentHead]
            currentNode = hNode[1]
            
            while currentNode:
                lString+=' '+str(currentNode.val)
                currentNode = currentNode.pointer 
            lString += '\n'
                
        return lString
                
    
                
        
        
if __name__ == '__main__':
    skip1 = skipList()
    skip1.appendNode(7)
    skip1.appendNode(8)
    skip1.appendNode(9)
    skip1.appendNode(10)
    skip1.appendNode(11)
    skip1.appendNode(8)
    print(skip1)
    
    
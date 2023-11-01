class Node:
    def __init__(self, val):
        self.val = val
        self.pointer = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def appendNode(self, nodeVal):
        if not self.head:
            self.head = Node(nodeVal)
        else:
            currentNode = self.head
            while currentNode.pointer:
                currentNode = currentNode.pointer
            currentNode.pointer = Node(nodeVal)

    
    def deleteNode(self, key):
        if not self.head:
            return None
        else:
            if self.head is key:
                self.head.val = key
            else:
                currentNode = self.head
                while currentNode.pointer:
                    currentNode = currentNode.pointer
                
                    
        
if __name__ == '__main__':
    linklist1 = LinkedList()
    linklist1.appendNode(8)
    linklist1.appendNode(7)
    linklist1.appendNode(6)
    linklist1.appendNode(9)

class Node:
    def __init__(self, val):
        self.val=val
        self.pointer=None
        
    def __str__(self):
        return f'Data: {self.val}, Pointer: {self.pointer}'
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def appendNode(self, nodeVal):
        if not self.head: self.head=Node(nodeVal)
        currentNode=self.head
        while currentNode.pointer:
            currentNode=currentNode.pointer
        currentNode.pointer=Node(nodeVal)

    
    def deleteNode(self, key):
        if not self.head:raise ValueError('Empty LinkedList')
        sentinel=Node(None)   # Dummy Node 
        sentinel.pointer=self.head
        currentNode=sentinel
        while currentNode.pointer:
            if currentNode.pointer.val==key:
                currentNode.pointer=currentNode.pointer.pointer
                return True
            currentNode=currentNode.pointer
        raise ValueError('Key Is Not A Node')
        
    def insertNode(self, key, val):
        if not self.head:raise ValueError('Empty LinkedList')
        new_node=Node(val)
        currentNode=self.head
        while currentNode:
            if currentNode.val==key:
                new_node.pointer=currentNode.pointer
                currentNode.pointer=new_node
                return True
            currentNode=currentNode.pointer
        raise ValueError('Key Is Not A Node')
                    
    def __str__(self):
        if not self.head:raise ValueError('Empty LinkedList')
        lString=''
        currentNode=self.head
        while currentNode:
            lString+=str(currentNode.val)+' '
            currentNode=currentNode.pointer
        return lString
                
                
                
                
if __name__ == '__main__':
    linklist1 = LinkedList()
    linklist1.appendNode(8)
    linklist1.appendNode(7)
    linklist1.appendNode(6)
    linklist1.appendNode(9)

    linklist1.insertNode(6,10)
    print(linklist1)
    
    linklist1.deleteNode(9)
    print(linklist1)
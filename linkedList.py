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
                
class circularLinked(LinkedList):
    def __init__(self):
        super().__init__()
        
    def appendNode(self, nodeVal):
        new_node=Node(nodeVal)
        if not self.head:
            self.head=new_node
            self.head.pointer=self.head
        currentNode=self.head
        while currentNode.pointer!=self.head:
            currentNode=currentNode.pointer
        currentNode.pointer=new_node
        new_node.pointer=self.head
    
    def deleteNode(self, key):
        if not self.head:return
        # Case: If head is only node
        if self.head.val==key and self.head.pointer==self.head:
            self.head=None 
            return
        # Case: Key in head node
        if self.head.val==key:
            currentNode=self.head
            while currentNode.pointer!=self.head:
                currentNode=currentNode.pointer
            currentNode.pointer=self.head.pointer
            self.head=self.head.pointer
        else:
            # Case: Key not in head node
            currentNode=self.head
            previousNode=None
            while currentNode.pointer!=self.head and currentNode.val!=key:
                previousNode=currentNode
                currentNode=currentNode.pointer
                
            if currentNode.val!=key:raise ValueError('Key Not In List') 
            
            previousNode.pointer=currentNode.pointer
    
    def __str__(self):
        currentNode=self.head
        cString=''
        while True:
            cString+=str(currentNode.val)+' '
            currentNode=currentNode.pointer
            if currentNode==self.head:
                break
        return cString

class DNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.prev = None
            
class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        
    def appendNode(self, val):
        # Case: Head Pointer is Null
        if not self.head:
            self.head = DNode(None)
            self.head.pointer = DNode(val)
            self.head.pointer.prev = self.head
        
        newNode = DNode(val)
        currentNode = self.head.pointer
        while currentNode:
            if currentNode.pointer is None:
                currentNode.pointer = newNode
                newNode.prev = currentNode
                newNode.pointer = self.head.pointer
                self.head.pointer.prev = newNode
                break
            # Another case to insert a node where the currentNode.next = self.head.pointer.prev
            if currentNode.pointer==self.head.pointer.prev:
                currentNode.pointer = newNode
                newNode.pointer = self.head.pointer.prev
                newNode.prev = currentNode
            currentNode = currentNode.pointer

        
    def __str__(self):
        if not self.head:return ValueError('Doubly Not Initialised')
        if not self.head.pointer: return ValueError("Empty Doubly List")
        
        currentNode = self.head.pointer
        dString=''
        while currentNode:
            dString+=str(currentNode.val)+' '
            currentNode = currentNode.pointer
            
            if currentNode.pointer==self.head.pointer:
                return dString
        return dString
            
            
        
        

            
        
                
if __name__ == '__main__':
    
    dLinkedList = DoublyLinkedList()
    dLinkedList.appendNode(1)
    dLinkedList.appendNode(2)
    print(dLinkedList)
    
    
    linklist1 = LinkedList()
    linklist1.appendNode(8)
    linklist1.appendNode(7)
    linklist1.appendNode(6)
    linklist1.appendNode(9)

    # linklist1.insertNode(6,10)
    # print(linklist1)
    
    # linklist1.deleteNode(9)
    # print(linklist1)
    
    clinklist1 = circularLinked()
    
    clist = [1,2,3,4,5,6,7,8]
    for num in clist:
        clinklist1.appendNode(num)
    # print(clinklist1)
    
    # clinklist1.appendNode(9)
    # print(clinklist1)
    
    # clinklist1.deleteNode(1)
    # print(clinklist1)
    
    
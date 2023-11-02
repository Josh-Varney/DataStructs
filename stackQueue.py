class Node:
    def __init__(self, val, content=None):
        self.val = val
        self.content = content
        
    def __str__(self):
        return f"{self.val}, {self.content}" if self.content else str(self.val)
        
class Stack:
    def __init__(self, size=None):
        self.arr = []
        self.cSize = 0
        self.max_size = size
        
    def isFull(self):
        return self.cSize==self.max_size
    
    def isEmpty(self):
        return self.cSize==0
        
    def push(self, value, content=None):
        if self.isFull() or not value:raise ValueError('Full Stack')
        else:
            self.cSize+=1
            self.arr.append(Node(value, content))
            
    def peek(self):
        if not self.isEmpty():return self.arr[-1]
        else:raise ValueError('Empty Stack')
                    
    def __pop(self):
        if self.isEmpty():raise ValueError('Empty Stack')
        else:
            itemP=self.arr.pop()
            self.cSize-=1
        return itemP
    
    def find(self, nFind):
            return any(node.val==nFind or (node.content and node.content['data']==nFind) for node in self.arr)
                    
    def __str__(self):
        return ' '.join(str(node.val)for node in self.arr)
    

class Queue(Stack):
    def __init__(self, size=None):
        super().__init__(size)
        self.head=0
        self.tail=-1

    def enqueue(self, value, content=None):
        super().push(value, content)
        self.tail+=1

    def dequeue(self):
        if self.isEmpty():raise ValueError('Queue is Empty')
        else:
            itemP=self.arr[self.head]
            self.head+=1
            self.cSize-=1
        return itemP
    
    def peek(self):
        if not self.isEmpty():return self.arr[self.head]
        else:raise ValueError('Queue is Empty')
                    
                    
            
class CircularQueue():
    def __init__(self, max_size=None):
        if max_size is None:
            raise ValueError('max_size must be specified for CircularQueue')
        self.arr=[None]*max_size
        self.max_size=max_size
        self.head=0
        self.tail=-1
        self.cSize=0

    def isFull(self):
        return self.cSize==self.max_size

    def isEmpty(self):
        return self.cSize==0
    
    def peek(self):
        if not self.isEmpty():return self.arr[self.head]
        else:raise ValueError('Queue is Full')

    def dequeue(self):
        if self.isEmpty():raise ValueError('Queue is Empty')
        else:
            itemP=self.arr[self.head]
            self.head=(self.head + 1)%self.max_size
            self.cSize-=1
        return itemP

    def enqueue(self, value, content=None):
        if self.isFull():raise ValueError('Queue is Full')
        elif not value:raise ValueError('No Value')
        else:
            self.tail=(self.tail + 1)%self.max_size
            self.arr[self.tail]=Node(value, content)
            self.cSize+=1
        
        
        
if __name__ == '__main__':
    stack1 = Stack()
    stack1.push(1, {'data': 'John'})
    stack1.push(2)
    stack1.push(3, {'data': 'Josh'})
    stack1.push(4)
    
    print(stack1.peek())
    
    
    queue1 = Queue()
    queue1.enqueue(1, {'data': 'James'})
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    
    print(queue1.peek())
    
    #print(queue1.dequeue())

    cqueue1 = CircularQueue(12)
    
    cqueue1.enqueue(1, {'data': 'large data'})
    cqueue1.enqueue(2)
    cqueue1.enqueue(3)
    cqueue1.enqueue(4)
    cqueue1.enqueue(5)
    cqueue1.enqueue(6)
    
    print(cqueue1.peek())
    #print(cqueue1.dequeue())
    #print(cqueue1.dequeue())
    
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
        if self.isFull() or not value:raise ValueError('Stack is Full')
        else:
            self.cSize+=1
            self.arr.append(Node(value, content))
                    
    def __pop(self):
        if self.isEmpty():raise ValueError('Empty Stack')
        else:
            itemP=self.arr.pop()
            self.cSize-=1
        return itemP
    
    def find(self, nFind):
            return any(node.val==nFind or (node.content and node.content['data']==nFind) for node in self.arr)
                    
    def __str__(self):
        return ' '.join(str(node.val) for node in self.arr)
    

class Queue(Stack):
    def __init__(self, size=None):
        super().__init__(size)
    
    # Override 
    def dequeue(self):
        if self.isEmpty(): return False
        else:
            itemP=self.arr.pop(0)
            self.cSize-=1
        return itemP
        
        
        
        
if __name__ == '__main__':
    stack1 = Stack()
    stack1.push(1, {'data': 'John'})
    stack1.push(2)
    stack1.push(3, {'data': 'Josh'})
    stack1.push(4)
    
    print(stack1._Stack__pop())
    
    queue1 = Queue()
    queue1.push(1, {'data': 'James'})
    queue1.push(2)
    queue1.push(3)
    queue1.push(4)
    
    print(queue1.dequeue())

    
    
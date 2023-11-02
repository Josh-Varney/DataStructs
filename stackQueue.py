class Node:
    def __init__(self, val, content=None):
        self.val = val
        self.content = content
        
    def __str__(self):
        if self.content: return f"{self.val}, {self.content}"
        else: return str(self.val)
        
        
class Stack:
    def __init__(self, size=None):
        self.stack = []
        self.cSize = 0
        self.mSize = size
        
    def isFull(self):
        return self.cSize==self.mSize
    
    def isEmpty(self):
        return self.cSize==0
        
    def push(self, value, content=None):
        if self.isFull(): return 'Stack is Full'
        else:
            if not self.mSize:
                self.cSize+=1
                self.stack.append(Node(value, content))
            else:
                if self.mSize==self.cSize:return None
                else:
                    self.cSize+=1
                    self.stack.append(Node(value, content))
                    
    def pop(self):
        if self.isEmpty(): return 'Empty Stack'
        else:
            itemP=self.stack.pop()
            self.cSize-=1
        return itemP
    
    
    def find(self, nFind):
        for currentNode in self.stack:
            if currentNode.val==nFind or (currentNode.content and currentNode.content['data'] == nFind):
                return True
        return False
            
                    
    def __str__(self):
        sString = ''
        for currentNode in self.stack:
            sString += str(currentNode.val) + ' '
        return sString
        
        
        
        
if __name__ == '__main__':
    stack1 = Stack()
    stack1.push(1, {'data': 'John'})
    stack1.push(2)
    stack1.push(3, {'data': 'Josh'})
    stack1.push(4)
    print(stack1)
    print(stack1.pop())
    print(stack1.find('Josh'))
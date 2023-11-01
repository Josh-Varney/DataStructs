class Node:
    def __init__(self, val):
        self.val = val
        self.pointer = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
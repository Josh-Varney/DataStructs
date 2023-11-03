class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
    
    
class Solution:
    def dfs(self,node):
        if not node:
            return
        print(node.val, end=" ")
        self.dfs(node.left)
        self.dfs(node.right)
        
    def inorder_traversal(self, node):
        if not node:
            return
        self.inorder_traversal(node.left)
        print(node.val, end=' ')
        self.inorder_traversal(node.right)
    
    def preoder_traversal(self, node):
        if not node:
            return
        self.preoder_traversal(node.left)
        self.preoder_traversal(node.right)
        print(node.val, end=' ')
            
    def breadthTraversal(self, node):
        if not node:
            return
        q = ([node])
        while q:
            currentNode = q.pop(0)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
            print(currentNode.val, end=' ')
    
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    solution_instance = Solution()
    
    solution_instance.breadthTraversal(root)
    
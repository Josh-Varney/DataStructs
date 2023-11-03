class Node:
    def __init__(self, val, content=None):
        self.val=val
        self.left=None
        self.right=None
        self.content=content
    
    
class Solution:
    def dfs(self,node):
        if not node:return
        print(node.val, end=" ")
        self.dfs(node.left)
        self.dfs(node.right)
        
    def inorder_traversal(self, node):
        if not node:return
        self.inorder_traversal(node.left)
        print(node.val,end=' ')
        self.inorder_traversal(node.right)
    
    def preoder_traversal(self, node):
        if not node:return
        self.preoder_traversal(node.left)
        self.preoder_traversal(node.right)
        print(node.val,end=' ')
            
    def breadthTraversal(self, node):
        if not node:return
        q = ([node])
        while q:
            currentNode = q.pop(0)
            if currentNode.left:q.append(currentNode.left)
            if currentNode.right:q.append(currentNode.right)
            print(currentNode.val,end=' ')
            
class BNode(Node):
    def __init__(self, val, content=None):
        super().__init__(val, content)
    
    def appendNode(self, val):
        if not self.val:raise ValueError('Enter a Value')
        if val<self.val:
            if self.left is None:self.left = BNode(val)
            else:self.left.appendNode(val)
        else:
            if self.right is None:self.right = BNode(val)
            else:self.right.appendNode(val)
    
    def deleteNode(self, key):
        if not self:raise ValueError('BST Empty')   # Error is the can't remove the root node 
        
        if self.val==key:
            # If key has zero children
            if not self.left and not self.right:return None
            # If key has one child
            if not self.left and self.right:return self.right
            if not self.right and self.left:return self.left
            # If key has two children
            point=self.right
            while point.left:point=point.left
            self.val=point.val
            self.right.deleteNode(self.right, self.val, key)
            
        elif self.val>key:
            self.left=self.left.deleteNode(key)  # return if there is a left node
        else:
            self.right=self.right.deleteNode(key) # reflects changes in the BST
            
        return self
    
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    solution_instance = Solution()
    
    # solution_instance.breadthTraversal(root)

    bsTree = BNode(1)
    bsTree.appendNode(2)
    bsTree.appendNode(5)
    bsTree.appendNode(7)
    bsTree.appendNode(3)
    bsTree.appendNode(8)
    bsTree.appendNode(0)
    bsTree.appendNode(9)
    
    bsTree.deleteNode(7)
    bsTree.deleteNode(2)
    solution_instance.dfs(bsTree)
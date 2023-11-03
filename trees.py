class TreeNode:
    def __init__(self, val, content=None):
        self.val=val
        self.content=content
        self.left=None
        self.right=None
        
class Tree:
    def __init__(self):
        self.root = None
    
    def appendNode(self, val, content=None, node=None):
        if not val: raise ValueError('Value Is Not Inputted')
        if not self.root:
            self.root = TreeNode(val, content)
            return 
        else:
            currentNode = self.root
            
            if currentNode.left is None and currentNode.right is None:
                if val < currentNode.val:
                    currentNode.left = TreeNode(val, content)
                else:
                    currentNode.right = TreeNode(val, content)
            
            if not currentNode.left:
                if val < currentNode.val:
                    currentNode.left = TreeNode(val, content)
                    
            if not currentNode.right:
                if val > currentNode.val:
                    currentNode.right = TreeNode(val, content)
                    
            node = currentNode.left
            self.appendNode(val, content, node)
            node = currentNode.right
            self.appendNode(val, content, node)
            
    
    def deleteNode(self, key):
        pass
    
    def dfs(self, node=None):
        if not self.root:raise ValueError('Tree is Empty')
        else:
            
            self.dfs()
        
        
        


if __name__ == '__main__':
    tree1 = Tree()
    tree1.appendNode(1)
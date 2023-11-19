class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.key = []
        self.children = []
        
class BTree:
    def __init__(self, degree):
        self.root = BTreeNode()
        # A degree which determines each children node keys(2t -1), or (2t) keys
        self.degree = degree  
        
    
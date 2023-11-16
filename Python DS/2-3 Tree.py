class TTNode:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

class TTTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TTNode(keys=[key])
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key in root.keys:
            return  # Ignore duplicate keys

        # If 2-Node then
        if len(root.keys) == 1:
            # Same as BST but inside node
            if key < root.keys[0]:
                root.keys.insert(0, key)
            else:
                root.keys.append(key)
        else:
            if key > root.keys[1]:
                self._insert(root.children[1], key)
            else:
                self._insert(root.children[0], key)

        # If 3-Node then
        if len(root.keys) == 2:
            middle_key = root.keys[1]
            leftChild = TTNode(keys=[root.keys[0]], children=[])
            rightChild = TTNode(keys=[root.keys[1]], children=[])
            root.keys = [middle_key]
            root.children = [leftChild, rightChild]


    def print_tree(self):
        self._print_tree(self.root, level=0)

    def _print_tree(self, root, level):
        # Shows the key levels and their children
        if root:
            print('Level:', level, 'Keys:', root.keys)
            for i, child in enumerate(root.children):
                print('Child', i + 1)
                self._print_tree(child, level + 1)


if __name__ == '__main__':
    tree = TTTree()
    keys_to_insert = [10, 5, 20, 15, 25, 15, 22,1,2, 1,2]

    for key in keys_to_insert:
        tree.insert(key)

    print("2-3 Tree:")
    tree.print_tree()



import java.util.ArrayList;
import java.util.List;

class TTNode {
    List<Integer> keys;
    List<TTNode> children;

    public TTNode(List<Integer> keys, List<TTNode> children) {
        this.keys = new ArrayList<>(keys);
        this.children = children;
    }

    public TTNode(List<Integer> keys) {
        this.keys = new ArrayList<>(keys);
        this.children = new ArrayList<>();
    }
}

class TTTree {
    private TTNode root;

    public TTTree() {
        this.root = null;
    }

    public void insert(int key) {
        if (root == null) {
            root = new TTNode(List.of(key));
        } else {
            _insert(root, key);
        }
    }

    private void _insert(TTNode root, int key) {
        if (root.keys.contains(key)) {
            return;  // Ignore duplicate keys
        }

        if (root.keys.size() == 1) {
            // Same as BST but inside the node
            if (key < root.keys.get(0)) {
                root.keys.add(0, key);
            } else {
                root.keys.add(key);
            }
        } else {
            if (key > root.keys.get(1)) {
                _insert(root.children.get(1), key);
            } else {
                _insert(root.children.get(0), key);
            }
        }

        // If 3-Node then
        if (root.keys.size() == 2) {
            int middleKey = root.keys.get(1);
            TTNode leftChild = new TTNode(List.of(root.keys.get(0)), new ArrayList<>());
            TTNode rightChild = new TTNode(List.of(root.keys.get(1)), new ArrayList<>());
            root.keys = new ArrayList<>(List.of(middleKey));
            root.children = new ArrayList<>(List.of(leftChild, rightChild));
        }
    }

    public void printTree() {
        _printTree(root, 0);
    }

    private void _printTree(TTNode root, int level) {
        // Shows the key levels and their children
        if (root != null) {
            System.out.println("Level: " + level + " Keys: " + root.keys);
            for (int i = 0; i < root.children.size(); i++) {
                System.out.println("Child " + (i + 1));
                _printTree(root.children.get(i), level + 1);
            }
        }
    }

    public static void main(String[] args) {
        TTTree tree = new TTTree();
        int[] keysToInsert = {10, 5, 20, 15, 25, 15, 22, 1, 2, 1, 2};

        for (int key : keysToInsert) {
            tree.insert(key);
        }

        System.out.println("2-3 Tree:");
        tree.printTree();
    }
}

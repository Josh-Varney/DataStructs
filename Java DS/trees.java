public class trees {
    TreeNode root;

    public static void main(String[] args) {
        trees btree = new trees();
        btree.appendNode(0);
        // Add more nodes if needed
        btree.appendNode(1);
        btree.appendNode(-1);
        // Print the tree
        btree.removeNode(btree.root, 1);
        btree.printTree(btree.root);
    }

    public trees(){
        this.root = null;
    }

    public void appendNode(int val){
        // No Node
        if (root == null){
            root = new TreeNode(val);
            return;
        }

        insertNode(root, val);
    }

    private void insertNode(TreeNode currentNode, int val) {
        // Key is less than currentVal
        if (val < currentNode.val) {
            if (currentNode.left == null) {
                currentNode.left = new TreeNode(val);
            } else {
                insertNode(currentNode.left, val);
            }
        // Key is greater than or equal to currentVal
        } else {
            if (currentNode.right == null) {
                currentNode.right = new TreeNode(val);
            } else {
                insertNode(currentNode.right, val);
            }
        }
    }

    private TreeNode removeNode(TreeNode node, int val) {
        // Error Checking
        if (node == null){
            throw new IllegalArgumentException("Empty Tree");
        }
        // Key is less than
        if (val < node.val){
            node.left = removeNode(node.left, val);
        // Key is greater than
        } else if (val > node.val){
            node.right = removeNode(node.right, val);
        } else{
            // Node with only one child or no children
            if (node.left == null){
                return node.right;
            } else if (node.right == null){
                return node.left;
            }
            
            // Node with two children
            node.val = minValue(node.right);
            // Delete the in-order successors
            node.right = removeNode(node.right, node.val);
        }

        return node;
        
    }

    private int minValue(TreeNode node){
        int minValue = node.val;
        while (node.left != null){
            minValue = node.left.val;
            node = node.left;
        }
        return minValue;
    }

    private int maxValue(TreeNode node){
        int maxValue = node.val;
        while(node.right != null){
            maxValue = node.right.val;
            node = node.right;
        }
        return maxValue;
    }

    public void printTree(TreeNode node) {
        // in-order traversal
        if (node != null) {
            printTree(node.left);
            System.out.print(node.val + " ");
            printTree(node.right);
        }
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

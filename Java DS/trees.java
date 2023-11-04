/**
 * trees
 */
public class trees {
    TreeNode root;

    public static void main(String[] args) {
        trees btree = new trees();
        btree.appendNode(0);
    }

    public trees(){
        this.root = null;
    }

    public void appendNode(int val){
        if (root == null){
            root = new TreeNode(val);
            return;
        }

        TreeNode currentNode = root;
        while (true){
            if (currentNode.val < val){
                if (currentNode.right == null){
                    currentNode.right = new TreeNode(val);
                    return;
                } else {
                    currentNode = currentNode.left;
                }
            } else{
                if (currentNode.left == null){
                    currentNode.left = new TreeNode(val);
                    return;
                } else {
                    currentNode = currentNode.right;
                }
            }
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
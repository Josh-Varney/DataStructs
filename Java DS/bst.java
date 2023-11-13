public class bst {
    protected TreeNode rootNode;
    public static void main(String[] args) {
        bst tree = new bst();
        System.out.println(tree);
    }

    public bst(){
        this.rootNode=null;
    }

    public void appendNode(int val){
        if (rootNode == null){
            rootNode = new TreeNode(val);
            return;
        }
        insertNode(rootNode, val);
    }

    private void insertNode(TreeNode node, int val){
        if (node.val > val){
            if (node.left == null){
                node.left = new TreeNode(val);
            } else{
                insertNode(node.left, val);
            }
        }else{
            if (node.val < val){
                node.right = new TreeNode(val);
            }else{
                insertNode(node, val);
            }
        }
    }

    public void deleteNode(int val){
        if (rootNode == null){
            rootNode = new TreeNode(val);
        }else{
            findNode(rootNode, val);
        }
    }

    private void findNode(TreeNode node, int val){
        if (node.val == val){
            
        }else{

        }

    }

    

    }

    




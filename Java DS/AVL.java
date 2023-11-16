public class AVL {
    protected AVLNode root;

    public static void main(String[] args) {
        AVL avl = new AVL();

        avl.insert(50);
        avl.insert(30);
        avl.insert(70);
        avl.insert(20);
        avl.insert(40);
        avl.insert(60);
        avl.insert(80);
        avl.insert(0);
        avl.insert(8);
        avl.insert(4);

        avl._print_inorder();
        
        System.out.println();

        int keyToSearch = 40;
        boolean isKeyPresent = avl._search(keyToSearch);
        System.out.println("Is key " + keyToSearch + " present: " + isKeyPresent);

        int keyToDelete = 30;
        avl.delete(keyToDelete);

        System.out.println("Inorder traversal after deletion:");
        avl._print_inorder();
    }

    public AVL(){
        root = null;
    }

    private int _get_height(AVLNode node){
        // Get Height of Node
        if (node == null){
            return 0;
        }else{
            return node.height;
        }
    }

    private int _update_height(AVLNode node){
        // Update Height of Node
        if (node == null){
            return 0;
        }else{
            // Maximum(Height of left subtree and Height of right subtree) + 1 for the root node
            return node.height = 1 + Math.max(_get_height(node.left), _get_height(node.right));
        }
    }
    
    private int _get_balance_factor(AVLNode node){
        // Gets BF of Node by tracersing heights of left and right subtree
        if (node == null){
            return 0;
        }
        return _get_height(node.left)-_get_height(node.right);
    }

    private AVLNode _rotate_right(AVLNode y){
        // Rotates using RR 
       AVLNode x = y.left;
       AVLNode T2 = x.right;
       x.right = y;
       y.left = T2;
       return x;
    }

    private AVLNode _rotate_left(AVLNode x){
        // Rotates using RL
        AVLNode y = x.right;
        AVLNode T2 = y.left;
        y.left = x;
        x.right = T2;
        _update_height(x);
        _update_height(y);
        return y;
    }

    public AVLNode _balance(AVLNode node){
        // Finds an unbalance in nodes and determines its rotation
        _update_height(node);
        int balance = _get_balance_factor(node);
        if (balance > 1){
            if (_get_balance_factor(node.left) < 0){
                node.left = _rotate_left(node.left);
            }
            return _rotate_right(node);
        }else if (balance < -1) {
            if (_get_balance_factor(node.right) > 0){
                node.right = _rotate_right(node.right);
            }
            return _rotate_left(node);
        }
        return node;
    }
    
    public void insert(int key){
        // Removes the head and views it as a normal node for recursive calls
        root = _insert_recursive(root,key);
    }

    private AVLNode _insert_recursive(AVLNode node, int key){
        // Same as BST Insertion
        if (node==null){
            return new AVLNode(key);
        } 
        if (key < node.key){
            node.left = _insert_recursive(node.left, key);
        }else{
            node.right = _insert_recursive(node.right, key);
        }
        // Balance the nodes after each insertion
        return _balance(node);
    }

    public boolean _search(int key){
        // BST search
        return _search_recursive(root, key);
    }

    private boolean _search_recursive(AVLNode node, int key){
        if (node == null){
            return false;
        }

        if (key == node.key){
            return true;
        }else if (key < node.key){
            return _search_recursive(node.left, key);
        }else{
            return _search_recursive(node.right, key);
        }
    }

    public void delete(int key){
        root = _delete_recursive(root, key);
    }

    private AVLNode _delete_recursive(AVLNode node, int key){
        // Find Key Node
        if (node==null){
            return node;
        } if (key<node.key){
            node.left = _delete_recursive(node.left,key);
        }else if (key>node.key){
            node.right = _delete_recursive(node.right, key);
        }else{
            if (node.right == null){
                return node.left;
            }else{
            AVLNode temp = _find_min_value_node(node.right);
            node.key = temp.key;
            node.right = _delete_recursive(node.right, temp.key);
            }
        }
        return _balance(node);
    }

    private AVLNode _find_min_value_node(AVLNode node){
        AVLNode current = node;
        while (current.left != null){
            current = current.left;
        }
        return current;
    }

    private void _inorder(AVLNode node){
        if (node!=null){
            _inorder(node.left);
            System.out.print(node.key + " ");
            _inorder(node.right);
        }
    }

    public void _print_inorder(){
        _inorder(root);
    }
}


class AVLNode {
    // Balance Factor can be calculated through the height
    int key;
    int height;
    AVLNode left;
    AVLNode right;

    public AVLNode(int key) {
        this.key=key;
        this.height=1;
        this.left=null;
        this.right=null;
    }
}
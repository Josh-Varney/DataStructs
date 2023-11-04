public class trees {
    private Node head;

    public trees(){
        this.head = null;
    }
}

class tNode {
    int val;
    Node left;
    Node right;

    public tNode(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
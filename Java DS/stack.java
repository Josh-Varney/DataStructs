public class stack {
    static SNode head;
    public static void main(String[] args) {
        stack stack1 = new stack();
        stack.append(1);
        stack.append(2);
        stack.append(3);
        stack1.printStack();
        stack1.pop();
        SNode node = stack1.pop();
        System.out.print(node.val);
        stack1.pop();
        stack1.printStack();
    }

    public stack(){
        head=null;
    }

    public static void append(int val){
        // Case: No Head Node
        if (head==null){
            head=new SNode(val);
            return;
        }

        SNode currentNode=head;
        while (currentNode.nextNode!=null) {
            currentNode=currentNode.nextNode;
        }

        currentNode.nextNode = new SNode(val);
    }

    public SNode pop() {
        // Check if the key is in Head
        if (head == null) {
            throw new IllegalArgumentException("Empty Stack");
        }

        SNode currentNode = head, prevNode = null;
        // Traverse the list to the second-to-last node
        while (currentNode.nextNode != null) {
            prevNode = currentNode;
            currentNode = currentNode.nextNode;
        }

        // If there's only one node, update head to null
        if (prevNode == null) {
            head = null;
        } else {
            // Update the nextNode reference of the second-to-last node
            prevNode.nextNode = null;
        }

        return currentNode;
    }

    public SNode peek(){
        if (head == null){
            throw new IllegalArgumentException("Empty Stack");
        }
        return head;
    }


    public void printStack() {
        SNode currentNode = head;
        while (currentNode != null){
            System.out.print(currentNode.val + " ");
            currentNode = currentNode.nextNode;
        }
        System.out.println();
    }
    

}

class SNode {
    int val;
    SNode nextNode;

    public SNode(int val){
        this.val = val;
        nextNode = null;
    }

    public void printNode(SNode node){
        System.out.println("Node: " + node.val);
    }
}
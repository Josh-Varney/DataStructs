/**
 * linkedList
 */
public class linkedList{
    private Node head;   //Head Node 
    public static void main(String[] args) {   //Start File
        linkedList manualList = new linkedList();  // Instance
        manualList.append(0);
        manualList.append(2);
        manualList.printList();
        manualList.remove(0);
        manualList.printList();
    }

    public void ManualLinkedList(){  // Constructor
        this.head = null;
    }

    public void append(int val){
        Node newNode = new Node(val);
        if (head == null){
            head = newNode;
            return;
        }

        Node current = head;
        while (current.nextNode != null){
            current = current.nextNode;
        }

        current.nextNode = newNode;
    }

    public void remove(int key){
        Node temp = head, prev = null;

        if (temp != null && temp.val == key){
            head = temp.nextNode;
            return;
        }

        while (temp != null && temp.val != key){
            prev = temp;
            temp = temp.nextNode;
        }

        if (temp == null) return;

        prev.nextNode = temp.nextNode;
    }
    
    public void printList(){
        Node current = head;
        while (current != null){
            System.out.print(current.val + " ");
            current = current.nextNode;
        }
        System.out.println();   // Prevent overlap with other methods
    }
}

class Node {
    int val;
    Node nextNode;

    public Node(int val){
        this.val = val;
        this.nextNode = null;
    }
}




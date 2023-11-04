/**
 * linkedList
 */
public class linkedList{
    protected Node head;   //Head Node 
    public static void main(String[] args) {   //Start File
        linkedList manualList = new linkedList();  // Instance
        manualList.append(0);
        manualList.append(2);
        manualList.printList();
        manualList.remove(0);
        manualList.printList();


        Circularlinkedlist cLinkedList = new Circularlinkedlist();
        cLinkedList.append(0);
        cLinkedList.append(1);
        cLinkedList.append(2);
        cLinkedList.append(3);

        cLinkedList.printList();

        cLinkedList.remove(2);

        cLinkedList.printList();
    }

    public void ManualLinkedList(){  // Constructor
        this.head = null;
    }

    public void append(int val){
        Node newNode = new Node(val);
        // Case: Head is Null
        if (head==null){
            head=newNode;
            return;
        }
        // Case: Head is not null
        Node current=head;
        while (current.nextNode!=null){
            current=current.nextNode;
        }

        current.nextNode=newNode;
    }

    public void remove(int key){
        Node temp=head, prev=null;
        // Case: Found the key 
        if (temp!=null && temp.val==key){
            head=temp.nextNode;
            return;
        }
        
        while (temp!=null && temp.val!=key){
            prev=temp;
            temp=temp.nextNode;
        }
        // Case: No head
        if (temp==null) return;

        prev.nextNode=temp.nextNode;
    }
    
    public void printList(){
        Node current=head;
        while (current!=null){
            System.out.print(current.val+" ");
            current = current.nextNode;
        }
        System.out.println();   // Prevent overlap with other methods
    }
}

class Circularlinkedlist extends linkedList{
    
    public Circularlinkedlist(){
        super();
    }

    @Override
    public void append(int val){
        Node newNode = new Node(val);
        // Case: Head is null
        if(head==null){
            head=newNode;
            head.nextNode=head;
            return;
        }

        Node currentNode=head;
        while (currentNode.nextNode!=head) {
            currentNode=currentNode.nextNode;
        }

        currentNode.nextNode=newNode;
        newNode.nextNode=head;
    }

    @Override
    public void remove(int key){
        Node temp=head, prev=null;
        if (temp!=null && temp.val==key){
            head=temp.nextNode;
            return;
        }

        while (temp!=null && temp.val!=key){
            prev=temp;
            temp=temp.nextNode;
        }

        if (temp==null) return;

        prev.nextNode=temp.nextNode;
        if (temp==head){
            head=temp.nextNode;
        }
    }

    @Override
    public void printList(){
        Node current=head;
        do {
            System.out.print(current.val+ " ");
            current=current.nextNode;
        } while (current!=head);
        System.out.println();
    }
}

class Node {
    int val;
    Node nextNode;

    public Node(int val){
        this.val=val;
        this.nextNode=null;
    }
}




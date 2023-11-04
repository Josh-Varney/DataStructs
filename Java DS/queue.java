

public class queue extends stack {
    public static void main(String[] args) {
        queue queue1 = new queue();
        queue1.enqueue(1);
        queue1.printQueue();
        queue1.enqueue(2);
        queue1.printQueue();
        queue1.dequeue();
        queue1.printQueue();
        queue1.dequeue();
        queue1.printQueue();
    }

    
    public queue(){
        super();
    }

    public void enqueue(int value){
        if (head == null){
            head = new SNode(value);
            return;
        }

        SNode currentNode = head;
        while (currentNode.nextNode != null){
            currentNode = currentNode.nextNode;
        }
        currentNode.nextNode = new SNode(value);
    }

    public SNode dequeue(){
        if (head == null){
            throw new IllegalArgumentException("Empty Queue");
        }

        SNode currentNode = head, prevNode = null;
        while (currentNode.nextNode != null){
            prevNode = currentNode;
            currentNode = currentNode.nextNode;
        } 
        if (prevNode == null){
            head = null;
        } else{
            prevNode.nextNode = null;
        }
        return currentNode;
    }

    public void printQueue(){
        SNode currentNode = head;
        while (currentNode != null) {
            System.out.print(currentNode.val + " ");
            currentNode = currentNode.nextNode;
        }
        System.out.println();
    }
    
}


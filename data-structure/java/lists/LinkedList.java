package lists;

public class LinkedList {
    private Node head;

    public void appendToHead(int value) {
        Node n = new Node(value);
        if (this.head == null) {
            this.head = n;
        } else {
            n.next = this.head;
            this.head = n;
        }
    }

    public Node removeFromHead() {
        if (this.head == null) {
            System.out.println("The list is empty");
            return null;
        }

        Node aux = this.head;
        this.head = aux.next;

        return aux;
    }

    public void show() {
        if (this.head == null) {
            System.out.println("The list is empty");
            return;
        }

        Node current = this.head;
        while (current != null) {
            System.out.println(current.value);
            current = current.next;
        }
    }

    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.appendToHead(3);
        ll.appendToHead(2);
        ll.appendToHead(1);
        ll.appendToHead(0);
        ll.show(); // 0 1 2 3
        ll.removeFromHead();
        ll.removeFromHead();
        ll.removeFromHead();
        ll.removeFromHead(); // the list is empty
    }
}

public class CircularQueue {
    private int capacity;
    private int values[];
    private int first = 0;
    private int last = -1;
    private int elemNumber = 0;

    public CircularQueue(int capacity) {
        this.capacity = capacity;
        this.values = new int[capacity];
    }

    private boolean empty() {
        return this.elemNumber == 0;
    }

    private boolean filled() {
        return this.elemNumber == this.capacity;
    }

    public void publish(int value) {
        if (this.filled()) {
            System.out.println("The array is already filled");
            return;
        }

        if (this.elemNumber < this.capacity) {
            if (this.last == this.capacity - 1) {
                this.last = -1;
            }
            this.last += 1;
            this.elemNumber += 1;
            this.values[this.last] = value;
        }
    }

    public void consume() {
        if (this.empty()) {
            System.out.println("The array is empty");
            return;
        }

        if (this.first == this.capacity - 1) {
            this.first = 0;
        }
        this.first += 1;
        this.elemNumber -= 1;
    }

    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(5);
        cq.publish(1);
        cq.publish(2);
        cq.publish(3);
        cq.publish(4);
        cq.publish(5);
        cq.consume();
        cq.consume();
        cq.consume();
        cq.publish(6);
        cq.publish(7);
        cq.publish(8);
        cq.consume();
        cq.consume();
        cq.publish(9);
        cq.publish(10);
        cq.consume();
        cq.publish(11);
    }
}

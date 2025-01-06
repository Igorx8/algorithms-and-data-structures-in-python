package queues;

public class PriorityQueue {
    private final int length;
    private final int[] values;
    private int elemNumber = 0;

    public PriorityQueue(int length) {
        this.length = length;
        this.values = new int[length];
    }

    private boolean isEmpty() {
        return this.elemNumber == 0;
    }

    private boolean isFull() {
        return this.elemNumber == this.length;
    }

    public void showList() {
        if (this.isEmpty()) {
            System.out.println("The queue is empty");
        }

        for (int i = 0; i < this.elemNumber; i++) {
            System.out.println(this.values[i]);
        }
    }

    public void add(int value) {
        if (this.isFull()) {
            System.out.println("Cannot add elements to a full queue");
            return;
        }

        int index = 0;

        while (index < this.elemNumber) {
            if (value > this.values[index]) {
                break;
            }
            index++;
        }

        int aux = this.elemNumber;
        while (index < aux) {
            this.values[aux] = this.values[aux - 1];
            aux--;
        }

        this.values[index] = value;
        this.elemNumber++;
    }

    public void remove() {
        if (this.isEmpty()) {
            System.out.println("Cannot remove from an empty array");
        }

        this.elemNumber--;
    }

    public static void main(String[] args) {
        PriorityQueue pq = new PriorityQueue(5);
        pq.add(1);
        pq.add(3);
        pq.add(2);
        pq.add(4);
        pq.add(5);
        pq.showList();
        pq.remove();
        pq.remove();
        pq.remove();
        pq.remove();
        pq.remove();
        pq.showList();
    }
}

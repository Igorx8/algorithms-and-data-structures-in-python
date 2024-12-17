public class UnorderedArray {
    private int capacity;
    private int lastPos = -1;
    private int values[];

    public UnorderedArray(int capacity) {
        this.capacity = capacity;
        this.values = new int[capacity];
    }

    private boolean empty() {
        return this.lastPos == -1;
    }

    private boolean filled() {
        return this.lastPos == this.capacity - 1;
    }

    public void print() {
        for (int i = 0; i <= this.lastPos; i++) {
            System.out.println(i + " -- " + this.values[i]);
        }
    }

    public void push(int value) {
        if (this.filled()) {
            System.out.println("The array is already filled");
            return;
        }

        this.lastPos += 1;
        this.values[this.lastPos] = value;
    }

    public void remove(int value) {
        if (this.empty()) {
            System.out.println("The array is empty");
            return;
        }

        int index = this.search(value);
        if (index == -1) {
            return;
        }

        while (index < this.lastPos) {
            this.values[index] = this.values[index + 1];
            index++;
        }
        this.lastPos -= 1;

    }

    public int search(int value) {
        if (this.empty()) {
            return -1;
        }

        int index = -1;

        for (int i = 0; i <= this.lastPos; i++) {
            if (this.values[i] == value) {
                index = i;
                break;
            }
        }

        return index;
    }

    public static void main(String[] args) {
        UnorderedArray u = new UnorderedArray(5);

        u.push(1);
        u.push(2);
        u.push(3);
        u.push(4);
        u.push(5);
        u.print();
        u.remove(1);
        u.remove(3);
        u.remove(5);
        u.push(0);
        u.print();
    }
}
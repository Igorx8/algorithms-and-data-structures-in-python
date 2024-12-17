public class OrderedArray {
    private int capacity;
    private int lastPos = -1;
    private int values[];

    public OrderedArray(int capacity) {
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

        int index = 0;

        for (int i = 0; i <= this.lastPos; i++) {
            index = i;
            if (this.values[i] > value) {
                break;
            }
            if (this.values[this.lastPos] < value) {
                index = this.lastPos + 1;
                break;
            }
            if (this.values[i] == value) {
                return;
            }

        }

        int aux = this.lastPos;
        while (index <= aux) {
            this.values[aux + 1] = this.values[aux];
            aux -= 1;
        }

        this.values[index] = value;
        this.lastPos += 1;

    }

    public void remove(int value) {
        if (this.empty()) {
            System.out.println("The array is empty");
            return;
        }

        int index = this.bSearch(value);
        if (index == -1) {
            return;
        }

        while (index < this.lastPos) {
            this.values[index] = this.values[index + 1];
            index++;
        }
        this.lastPos -= 1;

    }

    public int bSearch(int value) {
        if (this.empty()) {
            return -1;
        }

        int min = 0;
        int max = this.lastPos;
        int mid;

        while (min <= max) {
            mid = (min + max) / 2;

            if (this.values[mid] == value) {
                return mid;
            }
            if (this.values[mid] < value) {
                min = mid + 1;
            }
            if (this.values[mid] > value) {
                max = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        OrderedArray u = new OrderedArray(5);

        u.push(1);
        u.push(2);
        u.push(3);
        u.push(4);
        u.push(5);
        u.print();
        u.remove(5);
        u.remove(1);
        u.remove(3);
        u.push(6);
        u.push(0);
        u.print();

    }
}
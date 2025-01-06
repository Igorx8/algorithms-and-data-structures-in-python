public class Deque {
    private final int length;
    private final int[] values;
    private int leftElem = 0;
    private int rightElem = -1;

    private boolean isEmpty() {
        return this.rightElem == -1;
    }

    private boolean isFull() {
        return (this.rightElem == this.leftElem + 1) ||
                (this.rightElem == 0 && this.leftElem == this.length - 1);
    }

    public void showQueue() {
        if (!this.isEmpty()) {
            for (int i = 0; i < this.length; i++) {
                System.out.println(this.values[i]);
            }
        }
    }

    public void addLeft(int value) {
        if (this.isFull()) {
            System.out.println("The queue is already full");
            return;
        }

        if (this.isEmpty()) {
            this.leftElem = 0;
            this.rightElem = 0;
        } else {
            this.leftElem += 1;
        }

        this.values[this.leftElem] = value;
    }

    public void addRight(int value) {
        if (this.isFull()) {
            System.out.println("The queue is already full");
            return;
        }

        if (this.isEmpty()) {
            this.leftElem = 0;
            this.rightElem = 0;
        } else {
            if (this.rightElem == 0) {
                this.rightElem = this.length - 1;
            } else {
                this.rightElem -= 1;
            }
        }

        this.values[this.rightElem] = value;
    }

    public void removeLeft() {
        if (this.isEmpty()) {
            System.out.println("The queue is empty");
            return;
        }

        if (this.leftElem == this.rightElem) {
            this.leftElem = -1;
            this.rightElem = -1;
        } else if (this.leftElem > 0) {
            this.leftElem -= 1;
        } else {
            this.leftElem = this.length - 1;
        }

    }

    public void removeRight() {
        if (this.isEmpty()) {
            System.out.println("The queue is empty");
            return;
        }

        if (this.leftElem == this.rightElem) {
            this.leftElem = -1;
            this.rightElem = -1;
        } else if (this.rightElem == this.length - 1) {
            this.rightElem = 0;
        } else {
            this.rightElem += 1;
        }
    }

    public Deque(int length) {
        this.length = length;
        this.values = new int[length];
    }

    public static void main(String[] args) {
        Deque d = new Deque(5);
        d.addRight(6);
        d.addLeft(1);
        d.addLeft(7);
        d.addRight(2);
        d.addRight(3);
        d.showQueue();
        d.removeLeft();
        d.removeRight();
        d.removeLeft();
        d.removeRight();
        d.addLeft(4);
        d.addRight(5);
        d.showQueue();
    }
}

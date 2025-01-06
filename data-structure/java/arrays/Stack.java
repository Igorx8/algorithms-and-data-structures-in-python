public class Stack {
    private int capacity;
    private int top = -1;
    private int values[];

    public Stack(int capacity) {
        this.capacity = capacity;
        this.values = new int[capacity];
    }

    public void print() {
        for (int i = 0; i <= this.top; i++) {
            System.out.println(i + " -- " + this.values[i]);
        }
    }

    public void push(int value) {
        if (this.top == this.capacity - 1) {
            System.out.println("The array is already filled");
            return;
        }

        this.top += 1;
        this.values[this.top] = value;
    }

    public void pop() {
        if (this.top == -1) {
            System.out.println("The array is empty");
            return;
        }

        this.top -= 1;
    }

    public int getTop() {
        return this.values[this.top];
    }

    public static void main(String[] args) {
        Stack s = new Stack(5);
        s.push(5);
        s.push(3);
        s.push(1);
        s.push(4);
        s.push(2);
        s.print();
        s.pop();
        s.pop();
        s.pop();
        s.pop();
        s.pop();
        s.print();
        s.push(6);
        System.out.println(s.getTop());
    }
}

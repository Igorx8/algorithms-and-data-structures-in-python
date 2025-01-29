import { Node } from "./node";

class LinkedStack {
  private head: Node | null = null;
  private tail: Node | null = null;

  private isEmpty() {
    return this.head === null;
  }
  public show() {
    if (this.isEmpty()) {
      console.log("The stack is empty");
      return;
    }

    let current = this.head;

    while (current) {
      console.log(current.value);
      current = current.next;
    }
  }
  public push(value: number) {
    const node = new Node(value);

    if (this.isEmpty()) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail!.next = node;
      this.tail = node;
    }
  }
  public top() {
    if (this.isEmpty()) {
      console.log("The stack is empty");
      return;
    }

    return this.tail!.value;
  }
  public pop() {
    if (this.isEmpty()) {
      console.log("The stack is empty");
      return;
    }

    const removedValue = this.tail!.value;

    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
    } else {
      let current = this.head;
      while (current?.next !== this.tail) {
        current = current!.next;
      }
      this.tail = current;
      this.tail!.next = null;
    }
    return removedValue;
  }
}

const ls = new LinkedStack();
ls.show();
ls.push(1);
ls.push(2);
ls.push(3);
ls.push(4);
ls.pop();
ls.show();

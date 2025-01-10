export class Node {
  public value: number;
  public next: Node | null = null;
  public previous: Node | null = null;
  constructor(value: number) {
    this.value = value;
  }
}

class DoublyLinkedList {
  private head: Node | null = null;
  private tail: Node | null = null;

  private isEmpty() {
    return this.head === null;
  }

  public unshift(value: number) {
    const node = new Node(value);

    if (this.isEmpty()) {
      this.tail = node;
    } else {
      this.head!.previous = node;
      node.next = this.head;
    }

    this.head = node;
  }

  public push(value: number) {
    const node = new Node(value);

    if (this.isEmpty()) {
      this.head = node;
    } else {
      node.previous = this.tail;
      this.tail!.next = node;
    }
    this.tail = node;
  }

  public readLToR() {
    if (!this.isEmpty()) {
      let current = this.head;

      while (current) {
        console.log(current.value);
        current = current.next!;
      }
    }
  }

  public readRToL() {
    if (!this.isEmpty()) {
      let current = this.tail;

      while (current) {
        console.log(current.value);
        current = current.previous!;
      }
    }
  }

  public shift() {
    if (this.isEmpty()) {
      console.log("The array is empty");
      return;
    }

    if (this.head === this.tail) {
      const value = this.head!.value;
      this.head = null;
      this.tail = null;
      return value;
    }

    if (this.head?.next) this.head.next.previous = null;

    const value = this.head?.value;
    this.head = this.head!.next;
    return value;
  }

  public pop() {
    if (this.isEmpty()) {
      console.log("The array is empty");
      return;
    }

    if (this.head === this.tail) {
      const value = this.head!.value;
      this.head = null;
      this.tail = null;
      return value;
    }

    if (this.tail!.previous) this.tail!.previous.next = null;

    const value = this.tail?.value;
    this.tail = this.tail!.previous;
    return value;
  }

  public remove(value: number) {
    if (this.isEmpty()) {
      console.log("The array is empty");
      return;
    }

    if (this.head === this.tail) {
      const value = this.head!.value;
      this.head = null;
      this.tail = null;
      return value;
    }

    let current = this.head;
    while (current && current.value !== value) {
      current = current.next;
    }

    if (!current) return null;

    if (current === this.head) {
      this.shift();
    } else if (current === this.tail) {
      this.pop();
    } else {
      current.next!.previous = current.previous;
      current.previous!.next = current.next;
    }

    return current.value;
  }
}

const dl = new DoublyLinkedList();
dl.unshift(3);
dl.unshift(2);
dl.unshift(1);
dl.push(4);
dl.push(5);
dl.unshift(0);
dl.pop();
dl.shift();
dl.remove(4);
dl.readLToR();
dl.readRToL();

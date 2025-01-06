import { Node } from "./node";

class LinkedList {
  private head: Node | null = null;

  public appendToHead(value: unknown): void {
    const newNode = new Node(value);

    if (this.head !== null) {
      newNode.next = this.head;
    }

    this.head = newNode;
  }

  public removeFromHead(): Node | null {
    if (this.head === null) {
      console.log("The list is empty");
      return null;
    }

    let current = this.head;
    this.head = current.next;

    return current;
  }

  public show(): void {
    if (this.head === null) {
      console.log("The list is empty");
    }

    let current = this.head;
    while (current !== null) {
      console.log(current.value);
      current = current.next;
    }
  }
}

const ll = new LinkedList();
ll.appendToHead(3);
ll.appendToHead(2);
ll.appendToHead(1);
ll.show(); // 1 2 3
ll.removeFromHead();
ll.removeFromHead();
ll.removeFromHead();
ll.removeFromHead(); // the list is empty

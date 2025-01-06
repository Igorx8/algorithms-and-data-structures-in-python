import { Node } from "./node";

class SinglyLinkedList {
  private head: Node | null = null;
  private tail: Node | null = null;

  appendOnHead(value: number) {
    const newNode = new Node(value);

    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
  }

  appendOnTail(value: number) {
    const newNode = new Node(value);

    if (this.tail === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  show(): void {
    let current = this.head;

    if (current !== null) {
      while (current !== null) {
        console.log(current.value);
        current = current.next;
      }
    }
  }

  removeFromHead() {
    if (this.head === null) {
      console.log("The list is empty");
      return;
    }

    let aux = this.head;
    this.head = aux.next;

    return aux;
  }

  removeFromTail() {
    if (this.head === null) {
      console.log("The list is empty");
      return;
    }

    let previous: Node = this.head;
    if (previous.next === null) {
      this.head = null;
      this.tail = null;
    } else {
      while (previous.next!.value !== this.tail?.value) {
        previous = previous.next!;
      }
      previous.next = null;
      this.tail = previous;
    }

    return previous;
  }
}

const sll = new SinglyLinkedList();
sll.appendOnTail(1);
sll.appendOnTail(2);
sll.appendOnTail(3);
sll.appendOnHead(0);
sll.appendOnHead(-1);
sll.appendOnTail(6);
sll.show(); // -1 0 1 2 3 6
console.log(" ");
sll.removeFromHead();
sll.removeFromHead();
sll.removeFromTail();
sll.show(); // 1 2 3

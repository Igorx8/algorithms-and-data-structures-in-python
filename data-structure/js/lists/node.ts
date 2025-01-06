export class Node {
  public value: unknown;
  next: Node | null = null;

  constructor(value: unknown) {
    this.value = value;
  }
}

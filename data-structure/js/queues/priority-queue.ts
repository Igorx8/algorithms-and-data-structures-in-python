class PriorityQueue {
  private values: number[];
  private elemNumber: number = 0;
  private lenght: number;
  constructor(lenght: number) {
    this.lenght = lenght;
    this.values = new Array(lenght);
  }

  private isEmpty() {
    return this.elemNumber === 0;
  }

  private isFull() {
    return this.elemNumber === this.lenght;
  }

  public showList(): void {
    if (this.isEmpty()) {
      console.log("The queue is empty");
    }

    let strList = "";
    for (let i = 0; i < this.elemNumber; i++) {
      strList += `${this.values[i]}${i < this.elemNumber - 1 ? "," : ""}`;
    }

    console.log(strList);
  }

  public add(value: number): void {
    if (this.isFull()) {
      console.log("The queue is already full");
      return;
    }

    let index = 0;

    // considering an ordered queue from the higher to the lowest

    while (index < this.elemNumber) {
      if (value > this.values[index]) {
        break;
      }
      index++;
    }

    let aux = this.elemNumber;
    while (index < aux) {
      this.values[aux] = this.values[aux - 1];
      aux--;
    }

    this.values[index] = value;
    this.elemNumber++;
  }

  public remove() {
    if (this.isEmpty()) {
      console.log("Cannot remove from an empty array");
      return;
    }

    this.elemNumber--;
  }
}

const pq = new PriorityQueue(5);
pq.add(1);
pq.add(5);
pq.add(2);
pq.add(4);
pq.add(3);
pq.showList();
pq.remove();
pq.remove();
pq.remove();
pq.remove();
pq.remove();
pq.showList();

class UnorderedArray {
  private lastPos: number = -1;
  private values: number[];
  private length: number;

  constructor(length: number) {
    this.length = length;
    this.values = new Array(length);
  }

  print() {
    if (this.lastPos === -1) return console.log("The array is empty");

    for (let i = 0; i <= this.lastPos; i++) {
      console.log(`${i} -- ${this.values[i]} `);
    }
  }

  insert(value: number) {
    if (this.length === this.lastPos + 1)
      return console.error("Cannot insert, the array is already full");
    this.lastPos++;
    this.values[this.lastPos] = value;
  }

  find(value: number): number {
    for (let pos in this.values) {
      if (this.values[pos] === value) return Number(pos);
    }
    return -1;
  }

  remove(value: number) {
    const pos = this.find(value);
    if (pos === -1) return pos;

    for (let i = pos; i <= this.lastPos; i++) {
      this.values[i] = this.values[i + 1];
    }
    this.lastPos--;
  }
}

const unorderedArray = new UnorderedArray(5);

unorderedArray.print(); // [ ]
unorderedArray.insert(1);
unorderedArray.insert(2);
unorderedArray.insert(3);
unorderedArray.insert(4);
unorderedArray.insert(5);
unorderedArray.print(); // [1, 2, 3, 4, 5]
unorderedArray.insert(6); // cannot insert
console.log(unorderedArray.find(7)); // -1
console.log(unorderedArray.find(3)); // 2
console.log(unorderedArray.remove(6)); // -1
unorderedArray.remove(3);
unorderedArray.insert(6);
unorderedArray.print(); // [1, 2, 4, 5, 6]

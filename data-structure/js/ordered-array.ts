export class OrderedArray {
  lastPos: number = -1;
  capacity: number;
  values: number[];

  constructor(length: number) {
    this.capacity = length;
    this.values = new Array(length);
  }

  print() {
    if (this.lastPos === -1) return console.log("The array is empty");
    for (let index in this.values) {
      console.log(`${index} -- ${this.values[index]}`);
    }
    console.log(this.values);
  }

  insert(value: number) {
    if (this.lastPos + 1 === this.values.length)
      return console.log("The array is filled");

    let position = 0;
    for (let i = position; i < this.lastPos + 1; i++) {
      position = i;
      if (this.values[i] > value) break;
      if (this.lastPos === i) position = i + 1;
    }

    let x = this.lastPos;
    while (x >= position) {
      this.values[x + 1] = this.values[x];
      x--;
    }

    this.values[position] = value;
    this.lastPos++;
  }

  find(value: number) {
    for (let i = 0; i < this.lastPos + 1; i++) {
      if (this.values[i] > value) return -1;
      if (this.values[i] === value) return i;
      if (i === this.lastPos) return -1;
    }
    return -1;
  }

  remove(value: number) {
    const index = this.find(value);

    if (index === -1) return -1;

    for (let i = index; i <= this.lastPos; i++) {
      this.values[i] = this.values[i + 1];
    }

    this.lastPos--;
  }
}

const orderedArray = new OrderedArray(5);
orderedArray.print();
orderedArray.insert(5);
orderedArray.insert(3);
orderedArray.insert(6);
orderedArray.insert(1);
orderedArray.insert(8);
orderedArray.print();
console.log(orderedArray.find(5));
orderedArray.remove(5);
orderedArray.print();

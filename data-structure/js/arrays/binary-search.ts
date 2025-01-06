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

  bsearch(value: number) {
    if (this.lastPos === -1) return -1;

    let min = 0;
    let max = this.lastPos;

    while (min <= max) {
      let mid = Math.ceil((min + max) / 2);

      if (this.values[mid] === value) return mid;
      if (this.values[mid] > value) max = mid - 1;
      if (this.values[mid] < value) min = mid + 1;
    }

    return -1;
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
console.log(orderedArray.bsearch(3));
console.log(orderedArray.bsearch(8));
console.log(orderedArray.bsearch(5));
console.log(orderedArray.bsearch(1));

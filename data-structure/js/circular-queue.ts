class CircularQueue {
  private _first: number = 0;
  private _last: number = -1;
  private _values: number[];
  private _capacity: number;
  private _elemNumber: number = 0;
  constructor(capacity: number) {
    this._capacity = capacity;
    this._values = new Array(capacity);
  }

  _empty() {
    return this._elemNumber === 0;
  }

  _filled() {
    return this._capacity === this._elemNumber;
  }

  first() {
    return this._first;
  }

  last() {
    return this._last;
  }

  add(value: number) {
    if (this._filled()) {
      console.log("The array is already filled");
      return;
    }

    if (this._elemNumber < this._capacity) {
      if (this._last === this._capacity - 1) this._last = -1;
      this._last += 1;
      this._values[this._last] = value;
      this._elemNumber += 1;
    }
  }

  remove() {
    if (this._empty()) {
      console.log("The array is empty");
      return;
    }

    if (this._first === this._capacity - 1) {
      this._first = 0;
    }
    this._first += 1;
    this._elemNumber -= 1;
  }
}

const cQueue = new CircularQueue(5);
cQueue.add(1);
cQueue.add(2);
cQueue.add(3);
cQueue.add(4);
cQueue.add(5); // begin with [1,2,3,4,5]
cQueue.remove();
cQueue.remove();
cQueue.add(6);
cQueue.remove();
cQueue.add(7);
cQueue.add(8);
cQueue.remove();
cQueue.remove();
cQueue.remove();
cQueue.remove();
cQueue.remove();
cQueue.add(9);
cQueue.add(10);
cQueue.remove();

class Stack {
  private capacity: number;
  private top: number;
  private values: number[];
  constructor(capacity: number) {
    this.values = new Array(capacity);
    this.capacity = capacity;
    this.top = -1;
  }

  filled() {
    return this.top === this.capacity - 1;
  }

  empty() {
    return this.top === -1;
  }

  stack(value: number) {
    if (this.filled()) console.log("The stack is already filled");
    else {
      this.top++;
      this.values[this.top] = value;
    }
  }

  unstack() {
    if (this.empty()) console.log("The stack is empty");
    else {
      this.top--;
    }
  }

  getTop() {
    if (this.empty()) console.log("The stack is empty");
    else {
      return this.values[this.top];
    }
  }
}

const s = new Stack(5);
s.getTop();
s.stack(1);
s.stack(2);
s.stack(3);
s.stack(4);
s.stack(5);
s.unstack();
s.stack(6);
console.log(s.getTop());
s.unstack();
s.unstack();
s.unstack();
s.unstack();
s.unstack();
s.unstack();

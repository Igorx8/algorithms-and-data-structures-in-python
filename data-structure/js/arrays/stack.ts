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

  push(value: number) {
    if (this.filled()) console.log("The stack is already filled");
    else {
      this.top++;
      this.values[this.top] = value;
    }
  }

  pop() {
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
s.push(1);
s.push(2);
s.push(3);
s.push(4);
s.push(5);
s.pop();
s.push(6);
console.log(s.getTop());
s.pop();
s.pop();
s.pop();
s.pop();
s.pop();
s.pop();

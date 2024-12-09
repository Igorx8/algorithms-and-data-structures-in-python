const readline = require("readline");

const askQuestion = (question: string): Promise<string> => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise((resolve) => {
    rl.question(question, (response: string) => {
      resolve(response);
      rl.close();
    });
  });
};

class Stack {
  private capacity: number;
  private top: number;
  private values: string[];
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

  stack(value: string) {
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

  validate(text: string) {
    const openers = ["{", "[", "("];
    const closers = ["}", "]", ")"];
    for (let i = 0; i <= text.length; i++) {
      if (openers.includes(text[i])) {
        this.stack(text[i]);
      }
      if (closers.includes(text[i])) {
        switch (text[i]) {
          case "}":
            if (this.getTop() === "{") {
              this.unstack();
              continue;
            }
          case "]":
            if (this.getTop() === "[") {
              this.unstack();
              continue;
            }
          case ")":
            if (this.getTop() === "(") {
              this.unstack();
              continue;
            }
          default:
            throw new Error("Missing enclosing tag");
        }
      }
    }
    console.log("The text is validated ! ;)");
  }
}

askQuestion("Type the text to be validated: ").then((response: string) => {
  const s = new Stack(response.length);
  s.validate(response);
});

class Deque {
  private _capacity: number;
  private _values: number[];
  private _leftRef: number = 0;
  private _rightRef: number = -1;

  constructor(capacity: number) {
    this._capacity = capacity;
    this._values = new Array(capacity);
  }

  private _empty(): boolean {
    return this._rightRef === -1;
  }

  private _filled(): boolean {
    return (
      this._rightRef === this._leftRef + 1 ||
      (this._rightRef === 0 && this._leftRef === this._capacity - 1)
    );
  }

  public addLeft(value: number) {
    if (this._filled()) {
      console.log("The array is already filled");
      return;
    }

    if (this._empty()) {
      this._leftRef = 0;
      this._rightRef = 0;
    } else if (this._leftRef === this._capacity - 1) {
      this._leftRef = 0;
    } else {
      this._leftRef += 1;
    }

    this._values[this._leftRef] = value;
  }

  public addRight(value: number) {
    if (this._filled()) {
      console.log("The array is already filled");
      return;
    }

    if (this._empty()) {
      this._leftRef = 0;
      this._rightRef = 0;
    } else if (this._rightRef === 0) {
      this._rightRef = this._capacity - 1;
    } else {
      this._rightRef -= 1;
    }

    this._values[this._rightRef] = value;
  }

  public removeLeft(): void {
    if (this._empty()) {
      console.log("The array is empty");
      return;
    }

    if (this._leftRef === this._rightRef) {
      this._leftRef = -1;
      this._rightRef = -1;
    } else if (this._leftRef === 0) {
      this._leftRef = this._capacity - 1;
    } else {
      this._leftRef -= 1;
    }
  }

  public removeRight(): void {
    if (this._empty()) {
      console.log("The array is empty");
      return;
    }

    if (this._leftRef === this._rightRef) {
      this._leftRef = -1;
      this._rightRef = -1;
    } else if (this._rightRef === this._capacity - 1) {
      this._rightRef = 0;
    } else {
      this._rightRef += 1;
    }
  }
}

const d = new Deque(5);
d.addLeft(1);
d.addRight(5);
d.addLeft(2);
d.addRight(4);
d.addLeft(3);
d.removeRight();
d.addRight(6);
d.removeLeft();
d.addLeft(7);

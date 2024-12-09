var Stack = /** @class */ (function () {
    function Stack(capacity) {
        this.values = new Array(capacity);
        this.capacity = capacity;
        this.top = -1;
    }
    Stack.prototype.filled = function () {
        return this.top === this.capacity - 1;
    };
    Stack.prototype.empty = function () {
        return this.top === -1;
    };
    Stack.prototype.stack = function (value) {
        if (this.filled())
            console.log("The stack is already filled");
        else {
            this.top++;
            this.values[this.top] = value;
        }
    };
    Stack.prototype.unstack = function () {
        if (this.empty())
            console.log("The stack is empty");
        else {
            this.top--;
        }
    };
    Stack.prototype.getTop = function () {
        if (this.empty())
            console.log("The stack is empty");
        else {
            return this.values[this.top];
        }
    };
    return Stack;
}());
var s = new Stack(5);
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

var readline = require("readline");
var process = require("process");
var askQuestion = function (question) {
    var rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    return new Promise(function (resolve) {
        rl.question(question, function (response) {
            resolve(response);
            rl.close();
        });
    });
};
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
askQuestion("Digite o texto a ser validado: ").then(function (response) {
    var s = new Stack(response.length);
    console.log(response);
});

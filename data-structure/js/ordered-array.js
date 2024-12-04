"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.OrderedArray = void 0;
var OrderedArray = /** @class */ (function () {
    function OrderedArray(length) {
        this.lastPos = -1;
        this.capacity = length;
        this.values = new Array(length);
    }
    OrderedArray.prototype.print = function () {
        if (this.lastPos === -1)
            return console.log("The array is empty");
        for (var index in this.values) {
            console.log("".concat(index, " -- ").concat(this.values[index]));
        }
        console.log(this.values);
    };
    OrderedArray.prototype.insert = function (value) {
        if (this.lastPos + 1 === this.values.length)
            return console.log("The array is filled");
        var position = 0;
        for (var i = position; i < this.lastPos + 1; i++) {
            position = i;
            if (this.values[i] > value)
                break;
            if (this.lastPos === i)
                position = i + 1;
        }
        var x = this.lastPos;
        while (x >= position) {
            this.values[x + 1] = this.values[x];
            x--;
        }
        this.values[position] = value;
        this.lastPos++;
    };
    OrderedArray.prototype.find = function (value) {
        for (var i = 0; i < this.lastPos + 1; i++) {
            if (this.values[i] > value)
                return -1;
            if (this.values[i] === value)
                return i;
            if (i === this.lastPos)
                return -1;
        }
        return -1;
    };
    OrderedArray.prototype.remove = function (value) {
        var index = this.find(value);
        if (index === -1)
            return -1;
        for (var i = index; i <= this.lastPos; i++) {
            this.values[i] = this.values[i + 1];
        }
        this.lastPos--;
    };
    return OrderedArray;
}());
exports.OrderedArray = OrderedArray;
var orderedArray = new OrderedArray(5);
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

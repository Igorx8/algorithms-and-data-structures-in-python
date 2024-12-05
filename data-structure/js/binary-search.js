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
    OrderedArray.prototype.bsearch = function (value) {
        if (this.lastPos === -1)
            return -1;
        var min = 0;
        var max = this.lastPos;
        while (min <= max) {
            var mid = Math.ceil((min + max) / 2);
            if (this.values[mid] === value)
                return mid;
            if (this.values[mid] > value)
                max = mid - 1;
            if (this.values[mid] < value)
                min = mid + 1;
        }
        return -1;
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
console.log(orderedArray.bsearch(3));
console.log(orderedArray.bsearch(8));
console.log(orderedArray.bsearch(5));
console.log(orderedArray.bsearch(1));

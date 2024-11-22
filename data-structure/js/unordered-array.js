var UnorderedArray = /** @class */ (function () {
    function UnorderedArray(length) {
        this.lastPos = -1;
        this.length = length;
        this.values = new Array(length);
    }
    UnorderedArray.prototype.print = function () {
        if (this.lastPos === -1)
            return console.log("The array is empty");
        for (var i = 0; i <= this.lastPos; i++) {
            console.log("".concat(i, " -- ").concat(this.values[i], " "));
        }
    };
    UnorderedArray.prototype.insert = function (value) {
        if (this.length === this.lastPos + 1)
            return console.error("Cannot insert, the array is already full");
        this.lastPos++;
        this.values[this.lastPos] = value;
    };
    UnorderedArray.prototype.find = function (value) {
        for (var pos in this.values) {
            if (this.values[pos] === value)
                return Number(pos);
        }
        return -1;
    };
    UnorderedArray.prototype.remove = function (value) {
        var pos = this.find(value);
        if (pos === -1)
            return pos;
        for (var i = pos; i <= this.lastPos; i++) {
            this.values[i] = this.values[i + 1];
        }
        this.lastPos--;
    };
    return UnorderedArray;
}());
var unorderedArray = new UnorderedArray(5);
unorderedArray.print(); // [ ]
unorderedArray.insert(1);
unorderedArray.insert(2);
unorderedArray.insert(3);
unorderedArray.insert(4);
unorderedArray.insert(5);
unorderedArray.print(); // [1, 2, 3, 4, 5]
unorderedArray.insert(6); // cannot insert
console.log(unorderedArray.find(7)); // -1
console.log(unorderedArray.find(3)); // 2
console.log(unorderedArray.remove(6)); // -1
unorderedArray.remove(3);
unorderedArray.insert(6);
unorderedArray.print(); // [1, 2, 4, 5, 6]

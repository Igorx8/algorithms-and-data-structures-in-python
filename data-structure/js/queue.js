var CircularQueue = /** @class */ (function () {
    function CircularQueue(capacity) {
        this._first = 0;
        this._last = -1;
        this._elemNumber = 0;
        this._capacity = capacity;
        this._values = new Array(capacity);
    }
    CircularQueue.prototype._empty = function () {
        return this._elemNumber === 0;
    };
    CircularQueue.prototype._filled = function () {
        return this._capacity === this._elemNumber;
    };
    CircularQueue.prototype.first = function () {
        return this._first;
    };
    CircularQueue.prototype.last = function () {
        return this._last;
    };
    CircularQueue.prototype.add = function (value) {
        if (this._filled()) {
            console.log("The array is already filled");
            return;
        }
        if (this._elemNumber < this._capacity) {
            if (this._last === this._capacity - 1)
                this._last = -1;
            this._last += 1;
            this._values[this._last] = value;
            this._elemNumber += 1;
        }
    };
    CircularQueue.prototype.remove = function () {
        if (this._empty()) {
            console.log("The array is empty");
            return;
        }
        if (this._first === this._capacity - 1) {
            this._first = 0;
        }
        this._first += 1;
        this._elemNumber -= 1;
    };
    return CircularQueue;
}());
var cQueue = new CircularQueue(5);
cQueue.add(1);
cQueue.add(2);
cQueue.add(3);
cQueue.add(4);
cQueue.add(5);
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

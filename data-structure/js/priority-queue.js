var PriorityQueue = /** @class */ (function () {
    function PriorityQueue(lenght) {
        this.elemNumber = 0;
        this.length = lenght;
        this.values = new Array(lenght);
    }
    PriorityQueue.prototype.isEmpty = function () {
        return this.elemNumber === 0;
    };
    PriorityQueue.prototype.isFull = function () {
        return this.elemNumber === this.length;
    };
    PriorityQueue.prototype.showList = function () {
        if (this.isEmpty()) {
            console.log("The queue is empty");
        }
        var strList = "";
        for (var i = 0; i < this.elemNumber; i++) {
            strList += "".concat(this.values[i]).concat(i < this.elemNumber - 1 ? "," : "");
        }
        console.log(strList);
    };
    PriorityQueue.prototype.add = function (value) {
        if (this.isFull()) {
            console.log("The queue is already full");
            return;
        }
        var index = 0;
        // considering an ordered queue from the higher to the lowest
        while (index < this.elemNumber) {
            if (value > this.values[index]) {
                break;
            }
            index++;
        }
        var aux = this.elemNumber;
        while (index < aux) {
            this.values[aux] = this.values[aux - 1];
            aux--;
        }
        this.values[index] = value;
        this.elemNumber++;
    };
    PriorityQueue.prototype.remove = function () {
        if (this.isEmpty()) {
            console.log("Cannot remove from an empty array");
        }
        this.elemNumber--;
    };
    return PriorityQueue;
}());
var pq = new PriorityQueue(5);
pq.add(1);
pq.add(5);
pq.add(2);
pq.add(4);
pq.add(3);
pq.showList();
pq.remove();
pq.remove();
pq.remove();
pq.remove();
pq.remove();
pq.showList();

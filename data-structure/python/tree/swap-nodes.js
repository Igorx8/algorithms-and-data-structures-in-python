"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Node = void 0;
var Node = /** @class */ (function () {
    function Node(data, left, right) {
        if (left === void 0) { left = null; }
        if (right === void 0) { right = null; }
        this.data = data;
        this.left = left;
        this.right = right;
    }
    return Node;
}());
exports.Node = Node;
var indexes = [
    [2, 3],
    [-1, -1],
    [-1, -1],
];
var queries = [1, 1];
var createTree = function (indexes, root) {
    var queue = [root];
    for (var _i = 0, indexes_1 = indexes; _i < indexes_1.length; _i++) {
        var _a = indexes_1[_i], x = _a[0], y = _a[1];
        var currentNode = queue.shift();
        if (x !== -1) {
            currentNode.left = new Node(x);
            queue.push(currentNode.left);
        }
        if (y !== -1) {
            currentNode.right = new Node(y);
            queue.push(currentNode.right);
        }
    }
    return root;
};
var levelTraversalOrder = function (root) {
    if (!root)
        return;
    var queue = [root];
    while (queue.length > 0) {
        var currentNode = queue.shift();
        console.log(currentNode === null || currentNode === void 0 ? void 0 : currentNode.data);
        if (currentNode === null || currentNode === void 0 ? void 0 : currentNode.left)
            queue.push(currentNode.left);
        if (currentNode === null || currentNode === void 0 ? void 0 : currentNode.right)
            queue.push(currentNode.right);
    }
};
var swap = function (root, k, level, currentLvList) {
    if (root) {
        if (level % k === 0) {
            var tmp = root.left;
            root.left = root.right;
            root.right = tmp;
        }
        swap(root.left, k, level + 1, currentLvList);
        currentLvList.push(root.data);
        swap(root.right, k, level + 1, currentLvList);
    }
};
var swapNodes = function (indexes, queries) {
    var root = new Node(1);
    root = createTree(indexes, root);
    levelTraversalOrder(root);
    var result = [];
    for (var _i = 0, queries_1 = queries; _i < queries_1.length; _i++) {
        var k = queries_1[_i];
        var currentLv = [];
        swap(root, k, 1, currentLv);
        result.push(currentLv);
    }
    return result;
};
var swaped = swapNodes(indexes, queries);
console.log(swaped);

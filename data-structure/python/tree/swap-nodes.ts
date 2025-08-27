export class Node {
  constructor(
    public data: number | null,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

const indexes: number[][] = [
  [2, 3],
  [-1, -1],
  [-1, -1],
];

const queries: number[] = [1, 1];

const createTree = (indexes: number[][], root: Node) => {
  const queue = [root];

  for (let [x, y] of indexes) {
    const currentNode = queue.shift();

    if (x !== -1) {
      currentNode!.left = new Node(x);
      queue.push(currentNode!.left);
    }

    if (y !== -1) {
      currentNode!.right = new Node(y);
      queue.push(currentNode!.right);
    }
  }

  return root;
};

const levelTraversalOrder = (root: Node) => {
  if (!root) return;

  const queue = [root];
  while (queue.length > 0) {
    const currentNode = queue.shift();

    console.log(currentNode?.data);
    if (currentNode?.left) queue.push(currentNode.left);
    if (currentNode?.right) queue.push(currentNode.right);
  }
};

const swap = (
  root: Node,
  k: number,
  level: number,
  currentLvList: number[]
) => {
  if (root) {
    if (level % k === 0) {
      let tmp = root.left;
      root.left = root.right;
      root.right = tmp;
    }

    swap(root.left!, k, level + 1, currentLvList);
    currentLvList.push(root.data!);
    swap(root.right!, k, level + 1, currentLvList);
  }
};

const swapNodes = (indexes: number[][], queries: number[]) => {
  let root = new Node(1);
  root = createTree(indexes, root);
  levelTraversalOrder(root);

  const result: number[][] = [];

  for (let k of queries) {
    let currentLv: number[] = [];
    swap(root, k, 1, currentLv);
    result.push(currentLv);
  }

  return result;
};

const swaped = swapNodes(indexes, queries);
console.log(swaped);

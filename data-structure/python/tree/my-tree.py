class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BTree:
    def __init__(self, value=None):
        if value:
            node = Node(value)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.inorder_traversal(node.left)
        print(node.value, end='')
        if node.right:
            self.inorder_traversal(node.right)
            print(')', end='')

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.value)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hright + 1

bt = BTree(5)
bt.root.left = Node(4)
bt.root.left.left = Node(3)
bt.root.left.right = Node(2)
bt.root.right = Node(1)
bt.root.right.left = Node(0)

bt.inorder_traversal()
bt.postorder_traversal()
print(f"A altura da árvore é {bt.height()}")
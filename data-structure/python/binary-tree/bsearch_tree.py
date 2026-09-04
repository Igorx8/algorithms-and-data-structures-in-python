from node import Node


class BSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new = Node(value)
        if self.root == None:
            self.root = new
        else:
            current = self.root

            while True:
                parent = current
                if value < current.value:
                    current = current.left
                    if current == None:
                        parent.left = new
                        return
                if value > current.value:
                    current = current.right
                    if current == None:
                        parent.right = new
                        return

    def find(self, value: int):
        current = self.root

        while current is not None:
            if value == current.value:
                print(value)
                return current.value
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        print("Not found")
        return False


bst = BSearchTree()
bst.insert(3)
bst.insert(2)
bst.insert(5)
bst.insert(4)
bst.insert(1)
bst.find(3)
bst.find(6)
bst.find(0)
bst.find(1)
bst.find(5)
bst.find(4)

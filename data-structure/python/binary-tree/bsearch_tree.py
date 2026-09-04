from node import Node


class BSearchTree:
    def __init__(self):
        self.root = None
        self.list = []

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
                        self.list.append(f"{parent.value} -> {new.value}")
                        return
                else:
                    current = current.right
                    if current == None:
                        parent.right = new
                        self.list.append(f"{parent.value} -> {new.value}")
                        return

    def read(self):
        "Function to generate data for viz.js (tree preview)"
        for el in self.list:
            print(el)

    def find(self, value):
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

    def pre_order(self, current: Node | None):
        if current == None:
            return

        print(current.value)

        self.pre_order(current.left)
        self.pre_order(current.right)

    def in_order(self, current: Node | None):
        if current != None:
            self.in_order(current.left)
            print(current.value)
            self.in_order(current.right)


bst = BSearchTree()
bst.insert(53)
bst.insert(30)
bst.insert(72)
bst.insert(14)
bst.insert(9)
bst.insert(23)
bst.insert(39)
bst.insert(34)
bst.insert(49)
bst.insert(61)
bst.insert(84)
bst.insert(79)
bst.find(9)
bst.find(79)
bst.find(0)
bst.find(34)
bst.pre_order(bst.root)
bst.in_order(bst.root)

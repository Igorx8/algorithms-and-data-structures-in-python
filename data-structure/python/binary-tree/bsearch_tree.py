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
        if current != None:
            print(current.value)
            self.pre_order(current.left)
            self.pre_order(current.right)

    def in_order(self, current: Node | None):
        if current != None:
            self.in_order(current.left)
            print(current.value)
            self.in_order(current.right)

    def post_order(self, current: Node | None):
        if current != None:
            self.post_order(current.left)
            self.post_order(current.right)
            print(current.value)

    def get_substitute(self, node):
        previous = node
        current = node
        next = node.right

        while next != None:
            previous = current
            current = next
            next = next.left

        if current != node.right:
            previous.left = current.right
            current.right = node.right

        return current

    def remove(self, value: int):
        if self.root == None:
            return False
        else:
            current = self.root
            parent = self.root
            is_left = True

            while current.value != value:
                parent = current
                if value > current.value:
                    current = current.right
                    is_left = False
                else:
                    current = current.left
                    is_left = True
                if current is None:
                    return False

            if current.left is None and current.right is None:
                if current == self.root:
                    self.root = None
                elif is_left == True:
                    self.list.remove(str(parent.value) + " -> " + str(current.value))
                    parent.left = None
                else:
                    self.list.remove(str(parent.value) + " -> " + str(current.value))
                    parent.right = None
            elif current.left and current.right is None:
                if current == self.root:
                    self.list[self.list.index(f"{parent.value} -> {current.value}")] = (
                        f"{parent.value} -> {current.left.value}"
                    )
                    self.root = current.left
                elif is_left:
                    self.list[self.list.index(f"{parent.value} -> {current.value}")] = (
                        f"{parent.value} -> {current.left.value}"
                    )
                    self.list.remove(f"{current.value} -> {current.left.value}")
                    parent.left = current.left
                else:
                    self.list[self.list.index(f"{parent.value} -> {current.value}")] = (
                        f"{parent.value} -> {current.left.value}"
                    )
                    self.list.remove(f"{current.value} -> {current.left.value}")
                    parent.right = current.left
            elif current.right and current.left is None:
                if current == self.root:
                    self.list[self.list.index(f"{parent.value} -> {current.value}")] = (
                        f"{parent.value} -> {current.right.value}"
                    )
                    self.root = current.right
                elif is_left:
                    self.list[self.list.index(f"{parent.value} -> {current.value}")] = (
                        f"{parent.value} -> {current.right.value}"
                    )
                    self.list.remove(f"{current.value} -> {current.right.value}")
                    parent.left = current.right
                else:
                    self.list[self.list.index(f"{parent.value} -> {current.value}")] = (
                        f"{parent.value} -> {current.right.value}"
                    )
                    self.list.remove(f"{current.value} -> {current.right.value}")
                    parent.right = current.right
            else:
                substitute = self.get_substitute(current)

                if substitute == self.root:
                    self.root = substitute
                elif is_left:
                    parent.left = substitute
                else:
                    parent.right = substitute

                substitute.left = current.left

            return True


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
bst.post_order(bst.root)
bst.remove(9)
bst.remove(14)
bst.remove(72)
bst.in_order(bst.root)

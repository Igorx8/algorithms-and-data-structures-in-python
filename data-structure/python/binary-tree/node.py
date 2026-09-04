class Node:
    def __init__(self, value):
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None

    def show_node(self):
        print(self.value)

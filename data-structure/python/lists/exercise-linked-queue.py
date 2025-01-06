from node import Node

class LinkedQueue:
    def __init__ (self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None
    
    def add(self, value):
        n = Node(value)

        if self.is_empty():
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def show(self):
        if not self.is_empty():
            current = self.head

            while current != None:
                print(current.value)
                current = current.next

    def remove(self):
        if self.is_empty():
            print('The queue is empty')
            return
    
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        
        value = self.head.value
        self.head = self.head.next
        return value



lq = LinkedQueue()
lq.add(5)
lq.add(4)
lq.add(3)
lq.add(2)
lq.add(1)
lq.show()
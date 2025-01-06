from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addOnHead(self, value):
        novo = Node(value)
        novo.next = self.head

        if self.head == None:
            self.tail = novo
        self.head = novo

    def addOnTail(self, value):
        novo = Node(value)

        if self.head == None:
            self.head = novo
        else:
            self.tail.next = novo
        self.tail = novo

    def show(self):
        current = self.head
        while current != None:
            current.getNode()
            current = current.next

    def removeFromHead(self):
        if self.head == None:
            print("The list is empty")
            return None
        
        temp = self.head
        if self.head.next == None:
            self.tail = None

        self.head = self.head.next
        return temp

    def removeFromTail(self):
        if self.head == None:
            print("The list is empty")
            return None

        removed_value = self.tail.value
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            
            current.next = None
            self.tail = current

        return removed_value

    
    def remove(self, value):
        if self.head == None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
            return self.head
        
        current = self.head
        previous = None
        while current != None:
            if current.value == value:
                previous.next = current.next
                return current
            previous = current
            current = current.next

        return None

    
    def find(self, value):
        if self.head == None:
            return None
        
        temp = self.head
        while temp != None:
            if temp.value == value:
                return temp
            temp = temp.next

        return None

sll = SinglyLinkedList()
sll.addOnHead(2)
sll.addOnHead(1)
sll.addOnTail(3)
sll.addOnTail(4)
sll.addOnTail(5)
sll.addOnHead(0)
sll.show()
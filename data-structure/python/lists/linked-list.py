from node import Node

class LinkedList:
    def __init__ (self):
        self.head = None

    def addOnHead(self, value):
        novo = Node(value)
        novo.next = self.head
        self.head = novo

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
        
        self.head = self.head.next
        return temp
    
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

l = LinkedList()
l.addOnHead(1)
l.addOnHead(2)
l.addOnHead(3)
l.addOnHead(4)
l.addOnHead(5)
l.show()
l.find(3)
l.remove(5)
l.show()
l.removeFromHead()
l.removeFromHead()
l.removeFromHead()

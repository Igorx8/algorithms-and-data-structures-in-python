class Node:
    def __init__ (self, value):
        self.value = value
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None

    def addToHead(self, value):
        n = Node(value)

        if self.head == None:
            self.tail = n
        else:
            n.next = self.head
            self.head.previous = n
        self.head = n

    def addToTail(self, value):
        n = Node(value)

        if self.head == None:
            self.head = n
        else:
            n.previous = self.tail
            self.tail.next = n
        self.tail = n

    def showLtoR(self):
        if self.head == None:
            return None

        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def showRtoL(self):
        if self.head == None:
            return None

        current = self.tail
        while current != None:
            print(current.value)
            current = current.previous

    def removeFromHead(self):
        if self.head == None:
            print('The list is empty')
            return
        
        temp = self.head
        if self.head.next == None:
            self.tail = None
        else:
            temp.next.previous = None
            self.head = temp.next

        return temp
    
    def removeFromTail(self):
        if self.head == None:
            print('The list is empty')
            return
        
        temp = self.tail
        if self.tail.previous == None:
            self.head = None
        else:
            self.tail.previous.next = None

        self.tail = temp.previous
        return temp
    
    def remove(self, value):
        if self.head == None:
            print('The list is empty')
            return

        aux = self.head
        while aux and aux.value != value:
            aux = aux.next

        if aux is None:
            return None
        
        if aux == self.head:
            self.head = aux.next
            if self.head:
                self.head.previous = None

        if aux == self.tail:
            self.tail = aux.previous
            if self.tail:
                self.tail.next = None

        if aux.previous:
            aux.previous.next = aux.next
        if aux.next:
            aux.next.previous = aux.previous

        return aux.value
            


dll = DoublyLinkedList()
dll.addToHead(3)
dll.addToHead(2)
dll.addToHead(1)
dll.addToTail(4)
dll.remove(3)
dll.addToHead(0)
dll.addToTail(5)
dll.showLtoR()
print()
dll.showRtoL()
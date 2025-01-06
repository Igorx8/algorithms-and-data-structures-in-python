from node import Node

class LinkedStack:
    def __init__ (self):
        self.head = None
        self.__top = None

    def __is_empty(self):
        return self.__top == None
    
    def push(self, value):
        n = Node(value)
        if self.__is_empty():
            self.head = n
            self.__top = n
        else:
            self.__top.next = n
            self.__top = n

    def top(self):
        value = self.__top.value
        print(value)
        return value

    def pop(self):
        if self.__top == None:
            print('The stack is empty')
            return
        
        if self.head == self.__top:
            value = self.__top.value
            self.head = None
            self.__top = None
            return value
        
        current = self.head

        while current.next != self.__top:
            current = current.next
        
        temp = self.__top.value
        self.__top = current
        self.__top.next = None

        return temp
        

ls = LinkedStack()
ls.push(1)
ls.push(2)
ls.push(3)
ls.push(4)
ls.push(5)
ls.top()
ls.pop()
ls.top()
ls.pop()
ls.top()
ls.pop()
ls.top()
ls.pop()
ls.top()
ls.pop()
ls.pop() 
import numpy as np

class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__values = np.empty(capacity, dtype=int)
        self.__first = 0
        self.__last = -1
        self.__elem_number = 0

    def __empty(self):
        if self.__elem_number == 0:
            print('A fila está vazia')
            return True
        
    def __filled(self):
        if self.__elem_number == self.__capacity:
            print('A fila está cheia')
            return True
        
    def add(self, value):
        if self.__filled():
            return -1

        if self.__elem_number < self.__capacity:
                if(self.__last == self.__capacity -1):
                    self.__last = -1
                self.__last += 1
                self.__values[self.__last] = value
                self.__elem_number +=1
    
    def remove(self):
        if self.__empty():
            return -1
        
        self.__first += 1

        if self.__first == self.__capacity:
            self.__first = 0        

        self.__elem_number -= 1

    def first(self):
        return self.__first
    
    def last(self):
        return self.__last
        


queue = Queue(5)
queue.add(3)
queue.add(5)
queue.add(1)
queue.add(4)
queue.add(7)
print(queue.first())
print(queue.last())
queue.remove()
queue.remove()
queue.add(5)
queue.add(1)
queue.remove()
queue.remove()
queue.remove()
queue.remove()
queue.remove()
queue.add(1)
print(queue.first())
print(queue.last())

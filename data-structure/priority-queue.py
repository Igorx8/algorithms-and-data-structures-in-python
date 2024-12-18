import numpy as np

class PriorityQueue:
    def __init__ (self, capacity):
        self.__capacity = capacity
        self.__values = np.empty(capacity, dtype=int)
        self.__elem_number = 0

    def __empty(self):
        return self.__elem_number == 0
    
    def __filled(self):
        return self.__elem_number == self.__capacity
    
    def add(self, value):
        if self.__filled():
            print("The queue is already filled")
            return
        
        if self.__elem_number < self.__capacity:
            pos = 0

            while pos < self.__elem_number:  
                if self.__values[pos] <= value:
                    break
                pos += 1

            x = self.__elem_number
            while pos < x:
                self.__values[x] = self.__values[x-1]
                x-=1

            self.__values[pos] = value
            self.__elem_number += 1

    def process(self):
        if self.__empty():
            print("The queue is empty")
            return
        
        self.__elem_number -= 1

    def values(self):
        return self.__values


 

pq = PriorityQueue(5)
pq.add(3)
pq.add(5)
pq.add(2)
pq.add(1)
pq.add(4)
pq.process()
pq.process()
pq.add(5)
pq.add(6)
print(pq.values())
pq.add(7)
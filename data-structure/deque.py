import numpy as np

class Deque:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__values = np.empty(capacity, dtype=int)
        self.__start = 0        
        self.__end = -1

    def __empty(self):
        return self.__end == -1
    
    def __filled(self):
        return (self.__end == 0 and self.__start == self.__capacity -1) or self.__end == self.__start + 1
    
    def addRight(self, value):
        if(self.__filled()):
            print('The array is already filled')
            return
        
        if self.__empty():
            self.__end = 0
            self.__start = 0
        elif self.__end == 0:
            self.__end = self.__capacity - 1
        else:
            self.__end -= 1

        self.__values[self.__end] = value


    def addLeft(self, value):
        if(self.__filled()):
            print('The array is already filled')
            return
        
        if self.__empty():
            self.__end = 0
            self.__start = 0
        elif self.__start == self.__capacity - 1:
            self.__start = 0
        else:
            self.__start += 1

        self.__values[self.__start] = value

    def removeLeft(self):
        if(self.__empty()):
            print('The array is empty')
            return
        
        if self.__end == self.__start:
            self.__start = -1
            self.__end = -1
        elif self.__start == 0:
            self.__start = self.__capacity -1
        else:
            self.__start -= 1       

    def removeRight(self):
        if(self.__empty()):
            print("The array is empty")
            return
        
        if self.__end == self.__start:
            self.__start = -1
            self.__end = -1
        else:
            if self.__end == self.__capacity - 1:
                self.__end = 0
            else:
                self.__end += 1
        

d = Deque(5)
d.addLeft(30)
d.addLeft(40)
d.removeLeft()
d.addLeft(41)
d.addRight(10)
d.addRight(20)
d.addLeft(50)
d.removeLeft()
d.addLeft(60)
d.removeRight()
d.addRight(70)
d.removeRight()
d.addLeft(80)
d.removeRight()
d.removeRight()
d.removeLeft()
d.removeRight()
d.removeRight()
d.addLeft(1)
d.addLeft(1)
d.addLeft(1)
d.addRight(4)
d.addRight(5)
d.removeRight()
d.addRight(6)
d.removeLeft()
d.addLeft(7)
d.addLeft(8)
d.removeLeft()
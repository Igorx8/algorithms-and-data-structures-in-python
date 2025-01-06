import numpy as np

class OrderedArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_pos = -1
        self.values = np.empty(self.capacity, dtype=int)

    def print(self):
        if (self.last_pos == -1):
            return print('Array empty')
        
        for i in range(self.last_pos + 1):
            print(f"{i} -- {self.values[i]}")
    
    def insert(self, value):
        if self.last_pos + 1 == self.capacity:
            return print('Array already filled')
        
        position = 0
        for i in range(self.last_pos + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_pos:
                position = i + 1
        
        aux = self.last_pos

        while aux >= position:
            self.values[aux + 1] = self.values[aux]
            aux -= 1

        self.values[position] = value
        self.last_pos += 1
    
    def bsearch(self, value):
        if self.last_pos == -1:
            return -1
        
        min = 0
        max = self.last_pos

        while min <= max:
            mid = int((min + max) / 2 )
            if self.values[mid] == value:
                return mid
            if value > self.values[mid]:
                min = mid + 1
            if value < self.values[mid]:
                max = mid - 1
        
        return -1
            


        
ordered = OrderedArray(5)
ordered.print()
ordered.insert(5)
ordered.insert(3)
ordered.insert(6)
ordered.insert(8)
ordered.insert(1)
ordered.print()
print(ordered.bsearch(3))
print(ordered.bsearch(6))
print(ordered.bsearch(1))
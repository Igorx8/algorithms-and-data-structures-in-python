""" import numpy as np

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

bubble_sort(np.array([5,4,3,2,1], dtype=int)) """

import numpy as np

arr = np.array([5,4,3,2,1], dtype=int)

def bubble_sort(array):
    n = len(array)
    c = 0
    while c < n:
        i = 0
        while i < n - 1 - c:
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
            i+=1
        c+=1
    return array

bubble_sort(arr)
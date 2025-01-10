import numpy as np

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minorIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minorIndex]:
                minorIndex = j

            if minorIndex != i:
                step = arr[i]
                arr[i] = arr[minorIndex]
                arr[minorIndex] = step

    return arr


print(selection_sort(np.array([5,4,3,2,1], dtype=int)))
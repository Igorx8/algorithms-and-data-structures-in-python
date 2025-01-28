import numpy as np

def shell_sort(arr):
    interval = len(arr) // 2

    while interval > 0:
        for i in range(interval, len(arr)):
            temp = arr[i]
            j = i
            while j>= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j-=interval
            arr[j] = temp
        interval //=2
    print(arr)
    return arr


shell_sort(np.array([8,5,1,4,2,3], dtype=int))
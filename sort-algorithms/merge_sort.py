import numpy as np

def merge_sort(arr):
    if len(arr) > 1:
        div = len(arr)//2
        left = arr[:div].copy()
        right = arr[div:].copy()

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k +=1

    return arr

merge_sort(np.array([8,5,1,4,2,3], dtype=int))
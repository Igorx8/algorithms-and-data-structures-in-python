from timeit import timeit
from random import uniform

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort_non_recursive
import sys
sys.path.append('/home/igor-pc/Documents/personal/pythonProject/data-structure/python/arrays')
import ordered_array

def benchmark(sort_algorithm, array):
    return timeit(lambda: sort_algorithm(array), number=1) * 1e3

def insertOrderedArray(size):
    oa = ordered_array.VetorOrdenado(size)
    for i in range(size):
        oa.insere(i)

    return oa

def main():
    unordered_array = [uniform(0, 5000) for _ in range(5000)]

    print(f"Insert time: {timeit(lambda: insertOrderedArray(5000), number=1) * 1e3:.2f} ms")

    print(f"Bubble Sort: {benchmark(bubble_sort, unordered_array):.2f} ms")
    print(f"Insertion Sort: {benchmark(insertion_sort, unordered_array):.2f} ms")
    print(f"Selection Sort: {benchmark(selection_sort, unordered_array):.2f} ms")
    print(f"Merge Sort: {benchmark(merge_sort, unordered_array):.2f} ms")
    print(f"Quick Sort: {benchmark(quick_sort_non_recursive, unordered_array):.2f} ms")



main()
from timeit import timeit
from random import uniform

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


random_floats = [uniform(0, 1) for _ in range(5000)]

time_spent_bubble_sort = timeit(lambda: bubble_sort(random_floats.copy()), number=1)
print(f"Time spent for bubble_sort: {time_spent_bubble_sort * 1000:.2f} ms")

time_spent_insertion_sort = timeit(lambda: insertion_sort(random_floats.copy()), number=1)
print(f"Time spent for insertion_sort: {time_spent_insertion_sort * 1000:.2f} ms")

time_spent_selection_sort = timeit(lambda: selection_sort(random_floats.copy()), number=1)
print(f"Time spent for selection_sort: {time_spent_selection_sort * 1000:.2f} ms")

time_spent_merge_sort = timeit(lambda: merge_sort(random_floats.copy()), number=1)
print(f"Time spent for merge_sort: {time_spent_merge_sort * 1000:.2f} ms")

time_spent_quick_sort = timeit(lambda: quick_sort(random_floats.copy(), 0, len(random_floats) - 1), number=1)
print(f"Time spent for quick_sort: {time_spent_quick_sort * 1000:.2f} ms")

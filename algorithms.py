import numpy as np
import timeit

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Linear Search
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Vergleich der Leistung von Sortieralgorithmen
def compare_sorting(arr):
    arr_copy = arr.copy()
    t1 = timeit.timeit(lambda: bubble_sort(arr_copy), number=1)
    t2 = timeit.timeit(lambda: sorted(arr), number=1)
    t3 = timeit.timeit(lambda: np.sort(arr), number=1)
    return t1, t2, t3

# Vergleich der Leistung von Suchalgorithmen
def compare_search(arr, target):
    t1 = timeit.timeit(lambda: linear_search(arr, target), number=100)
    t2 = timeit.timeit(lambda: target in arr, number=100)
    t3 = timeit.timeit(lambda: np.where(np.array(arr) == target), number=100)
    return t1, t2, t3

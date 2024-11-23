"""
Pseudocede merge sort
MERGE_SORT(arr):
    If length of arr <= 1:
        Return arr
    Else:
        mid = length of arr / 2
        left = MERGE_SORT(arr[0:mid])
        right = MERGE_SORT(arr[mid:])
        Return MERGE(left, right)

MERGE(left, right):
    Create empty list result
    While left and right are not empty:
        If left[0] <= right[0]:
            Append left[0] to result
            Remove left[0] from left
        Else:
            Append right[0] to result
            Remove right[0] from right
    Append any remaining elements in left to result
    Append any remaining elements in right to result
    Return result

Pseudocode bubble sort
BUBBLE_SORT(arr):
    n = length of arr
    For i = 0 to n-1:
        For j = 0 to n-i-2:
            If arr[j] > arr[j+1]:
                Swap arr[j] and arr[j+1]

analisa Kompleksitas
merge sort
Big 0 (Worst-case)
    Devide : membagi array menjadi dua bagian membutuhkan waktu O(log n) karena setiap pembagian mengurangi ukuran array hingga ukuran 1.
    merge : penggabungan dua array membutuhkan waktu linear O(n).
    Kompleksitas total : O(n log n).
big Theta (Averge-case):
    pada kasus rata-rata, struktur rekursif yang sama berlaku. sehingga, kompleksitas rata-rata juga Θ(nlogn).
"""
import time
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generate random data
data = [random.randint(0, 1000) for _ in range(100)]

# Measure Merge Sort time
data_for_merge = data.copy()
start_time = time.time()
sorted_merge = merge_sort(data_for_merge)
merge_sort_time = time.time() - start_time

# Measure Bubble Sort time
data_for_bubble = data.copy()
start_time = time.time()
bubble_sort(data_for_bubble)
bubble_sort_time = time.time() - start_time

# Print Results
print("Original Data (First 10):", data[:10])
print("Merge Sort Result (First 10):", sorted_merge[:10])
print("Bubble Sort Result (First 10):", data_for_bubble[:10])
print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")




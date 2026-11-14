import random
import time
import sys

# Increase recursion depth just in case we hit the O(n^2) worst-case scenario
# on large, sorted arrays.
sys.setrecursionlimit(5000)

# ==========================================
# 1. DETERMINISTIC QUICKSORT (Hoare Partition)
# ==========================================

def hoare_partition(arr, p, r):
    """
    Partitions the array using Hoare's scheme.
    Always selects the first element in the current subarray as the pivot.
    """
    pivot = arr[p]
    i = p - 1
    j = r + 1
    
    while True:
        # Move the right pointer leftwards until an element <= pivot is found
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        # Move the left pointer rightwards until an element >= pivot is found
        i += 1
        while arr[i] < pivot:
            i += 1
            
        # If the pointers have not crossed, swap the elements
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            # Pointers have crossed; return the partition index
            return j


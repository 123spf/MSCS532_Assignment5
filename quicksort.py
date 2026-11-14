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

def quicksort_deterministic(arr, p, r):
    """
    Deterministic Quicksort algorithm.
    """
    if p < r:
        # q is the partition index
        q = hoare_partition(arr, p, r)
        
        # Recursively sort the sub-arrays. 
        # Note: Hoare partition includes the pivot in the left or right sub-array,
        # so we split at q and q+1 (unlike Lomuto which splits at q-1 and q+1).
        quicksort_deterministic(arr, p, q)
        quicksort_deterministic(arr, q + 1, r)

# ==========================================
# 2. RANDOMIZED QUICKSORT (Hoare Partition)
# ==========================================

def randomized_hoare_partition(arr, p, r):
    """
    Randomized Hoare partition. 
    Selects a random pivot, swaps it to the front, and then uses normal Hoare logic.
    """
    # Select a random index between p and r (inclusive)
    pivot_idx = random.randint(p, r)
    
    # Swap the random pivot with the first element
    arr[p], arr[pivot_idx] = arr[pivot_idx], arr[p]
    
    # Proceed with the standard Hoare partition
    return hoare_partition(arr, p, r)

def quicksort_randomized(arr, p, r):
    """
    Randomized Quicksort algorithm.
    """
    if p < r:
        q = randomized_hoare_partition(arr, p, r)
        quicksort_randomized(arr, p, q)
        quicksort_randomized(arr, q + 1, r)
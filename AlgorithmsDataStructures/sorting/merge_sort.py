# Implementation of MergeSort
def mergeSort(arr, s, e):
    """
    arr, starting_index, ending_index
    
    Merge sort recursively divides the input array in half until the sub-arrays contain only one element,
    which are considered sorted. Then, it merges these sorted sub-arrays back together, 
    comparing the elements and placing them in the correct order.
    """
    # base case = arr of size 1
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    mergeSort(arr, s, m)

    # Sort the right half
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)
    
    return arr



# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1



#### concise mergeSort ####
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
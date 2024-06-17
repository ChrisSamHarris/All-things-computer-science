### SELECTION SORT ###

def findSmallest(arr):
    """
    In each element of the array, find the smallest value
    """
    smallest_val = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_val:
            smallest_val = arr[i]
            smallest_index = i 
    return smallest_index

def selectionSort(arr):
    """
    Find the minimum element of the array 
    Swap the minimum element with the first unsorted element
    Repeat - using the boundary between the sorted and unsorted portions of the array one element to the right and repeat until the array is fully sorted.
    """
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest_index = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest_index))
    return newArr

print(selectionSort([5,3,6,2,10]))
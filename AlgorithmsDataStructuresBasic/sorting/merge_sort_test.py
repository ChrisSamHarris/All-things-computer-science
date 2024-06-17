def merge_sort(arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]
        
        #recursion 
        merge_sort(left)
        merge_sort(right)
        
        # merge 
        i = 0 # left array idnex
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        # consider the case we need to transfer all remaining elements from left or right
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
        return arr
        

arr_test = [5, 2, 3, 22, 1, 9, 4, 22, 7, 78, 2 ,3, 78, 99, 0, 1]
print(merge_sort(arr_test))
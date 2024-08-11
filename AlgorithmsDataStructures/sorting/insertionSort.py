def insertionSort(arr):
    for i in range(len(1, arr)):
        j = i-1
        
        # j index in loop | left index is greater than right index
        while j >= 0 and arr[j] > arr[j+1]:
            temp = j[i+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            
            # continue the loop until the left index is less than the right index
            j -= 1
            
    return arr
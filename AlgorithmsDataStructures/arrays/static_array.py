# Traverse through an array 
myArray = [1,2,3,4,5]
print('\nTraverse through an array [1,2,3,4,5]:')

for i in range(len(myArray)):
   print(myArray[i])
# OR
i = 0
while i < len(myArray):
   print(myArray[i])
   i += 1
   

#### Deleting from the end of an array #####
# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr):
    length = len(arr)
    if length > 0:
        # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0
    
    return arr
        
print('\nRemove End:')
print(removeEnd([1,2,3,4,5])) # [1,2,3,4,0]



##### Deleting at kth index of an array #####
# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i):
    """
    Shift starting from i + 1 to end.
    Replacing the ith value and remainder of the array.
    """
    length = len(arr)
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    
    # Return the array without the last element (as this will be duplicated)
    return arr[:-1]
    # No need to 'remove' arr[i], since we already shifted
    
print('\nRemove middle element:')
print(removeMiddle([1,2,3,4,5], 2))



#### Insert at the end of an array ####
# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n):
    length = len(arr)
    # if length < capacity:
    arr.append(n)
    
    return arr

print('\nInsert End:')
print(insertEnd([1,2,3,4,5], 6))


#### Insert at kth index of an array ####
# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n):
    """
    Shift starting from the end to i.
    At i insert the new value n.
    Opposite of removeMiddle, as we have to create space first prior to inserting.
    """
    length = len(arr)
    arr = arr + [0] # Increase the size of the array by 1, this allows our indexing to work
    for index in range(length-1, i-1, -1):
        arr[index + 1] = arr[index]
    
    # Insert at i
    arr[i] = n
    
    return arr
    
print('\nInsert middle element:')
print(insertMiddle([1,2,3,4,5], 2, 10))

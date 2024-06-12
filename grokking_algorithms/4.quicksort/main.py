#### Divide & Conquer Sample ####

test_arr = [2,4,6]

def sum(arr):
    total = 0 
    for x in arr:
        total += x
    return total

print(sum(test_arr))

def recursive_sum(arr):
    """
    Function to sum a list using recursion
    """
    # base case: empty array
    if arr == []:
        return 0
    return arr[0] + recursive_sum(arr[1:])
    
print(recursive_sum(test_arr))

def recursion_max_num(arr):
    """
    Function to find the maximum number in a list using recursion
    """
    # base case : arr of two values to compare 
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = recursion_max_num(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(recursion_max_num(test_arr))
test_arr_2 = [2,4,6,8,10,3,4,99,84,28]
print(recursion_max_num(test_arr_2))

def rec_inc_num(num,steps):
    """
    Function to increment a number using recursion until it reaches at least 10
    """
    if num <= 10:
        return num, steps
    return rec_inc_num(num -1, steps +1)
    
print(rec_inc_num(99,0))
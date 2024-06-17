# exponential
# f = abˣ

### Binary Search
def binary_search(arr, item):
    low = 0 
    high = len(arr) - 1
    num_guesses = 0
    
    while low <= high:
        mid = (low+high) // 2
        num_guesses += 1 
        
        if arr[mid] == item:
            return mid, num_guesses
        
        elif arr[mid] > item:
            high = mid-1 
        else:
            low = mid + 1
    return None, num_guesses

my_list = [i for i in range(129)]
target = 64

found, guesses = binary_search(my_list, target)

print(f"{found} found in {guesses} guesses")


### Travelling Salesperson 
# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/ 
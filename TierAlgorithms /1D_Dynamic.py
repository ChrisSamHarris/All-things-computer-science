# Optimised version of recursion. 
# Avoid repeating computation using memoization. 
# Top down approach is easier to write and understand, shown in the memoization function below. 

# Skelton = Base Case, Check Cache, Update cache with recursive case, return cache with initial value. 

def memoization(n, cache):
    """
    Using Fibonacci sequence as an example.
    """
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1) + memoization(n - 2)
    return cache[n]

def call(n):
    return memoization(n, {})
### Is Traingular 

def is_triangular(n):
    """ 
    n is an int > 0 
    Returns True if n is a triangular number,i.e. equals a continued summation of natural numbers
    and False otherwise.
    """
    total = 0 
    nums = []
    for i in range(n):
        total += i
        nums.append(i)
        if total == n:
            # return True
            calc_string = ' + '.join(map(str, nums[1:]))
            result = f"{n} is a TRIANGULAR number | {calc_string} = {n}"
            return result
    return False

# any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc.
print(is_triangular(6))


#### BISECTION 
def bisection_root(x):
    epsilion = 0.01
    low = 0
    high = x 
    ans = (high+low)/2.0

    while abs(ans**2 - x) >= epsilion:
        if ans**2 > x:
            # guess too high
            high = ans 
        else:
            # guess too low
            low = ans
        ans = (high+low)/2.0
    return ans

print(bisection_root(1331))


def count_nums_with_sqrt_close_to(n, epsilon):
    """
    n is an int > 0
    epsilon is a float > 0
    Returns the number of perfect squares close to n within epsilon
    """
    count = 0
    for i in range(n**3):
        sqrt = bisection_root(i)
        if abs(n-sqrt) < epsilon:
            # print(i, sqrt)
            count += 1
    return count

print(count_nums_with_sqrt_close_to(10,0.1))

print(count_nums_with_sqrt_close_to(10,1))

def sum_odd(a, b):
    """
    Return the sum of odd numbers between a and b.
    For example, sum_odd(1, 11) will equate 2,3,4,5,6,7,8,9,10
    """
    sum_of_odds = 0
    for i in range(a+1, b):
        if i % 2 == 0:
            sum_of_odds += i
    return sum_of_odds

print(sum_odd(1, 11))
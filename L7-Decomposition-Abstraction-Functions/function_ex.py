def is_even(i):
    """Return True if i is even, False otherwise."""
    if i % 2 == 0:
        return True
    else:
        return False
    
print(is_even(5))
print(is_even(6))

def is_even2(i):
    """Return True if i is even, False otherwise."""
    return i % 2 == 0

print(is_even2(5))
print(is_even2(6))


def div_by(n, d):
    """Return True if n is divisible by d, False otherwise."""
    return n % d == 0

print(div_by(10, 3))
print(div_by(195, 13))

# Abstraction
for i in range(1,100):
    if is_even2(i):
        print(i, 'even')
    else:
        print(i, 'odd')
        
        
def sum_odd(a, b):
    """
    Return the sum of odd numbers between a and b.
    For example, sum_odd(1, 11) will equate 2,3,4,5,6,7,8,9,10
    """
    sum = 0
    odd_nums = []
    for i in range(a+1, b):
        if not i % 2 == 0:
            sum += i
            odd_nums.append(i)
    # [print(i, " + ") for i in odd_nums]
    odd_nums_str = ' + '.join(map(str, odd_nums))
    results_str = f'sum_odd({a,b}) = {odd_nums_str} = {sum}'
    return results_str

print(sum_odd(1, 11))


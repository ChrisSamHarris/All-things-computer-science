#### LAMBDA ####

def is_even(x):
    return x % 2 == 0

print(is_even(8))
print((lambda x : x%2 == 0)(8))
print((lambda x : x%2 == 0)(5))


def do_twice(n, fn):
    return fn(fn(n))

print(do_twice(3, lambda x: x**2)) # 3 x 3 = 9 | 9 x 9 = 81

x = lambda a : a + 10
print(x(5))


#### TUPLES ####
print("\ntuples\n")
seq = (2,'a', 4, (1,2))
print(len(seq))
print(seq[3])
print(seq[-1])
print(seq[3][0])
#print(seq[4]) # will fail


# Return more than one value from a function
def quotient_and_remainder(x,y):
    """
    The quotient is the integer part of the result of a division operation. It is the result you get when you divide one number by another and discard any remainder. 
    
    Floor division = x \\ y -> divides the operands and then rounds down to the nearest whole number (towards negative infinity)
    Modulo = x % y -> returns the remainder of the division
    """
    q = x // y
    r = x % y
    return (q,r)

both = quotient_and_remainder(10, 3)
print(both)

(quotient, remainder) = quotient_and_remainder(10, 3)
print(quotient)
print(remainder)

def char_counts(s: str):
    """
    return a tuple where the first element is the number of voewls in s and the second element is the number of consonants in s
    """
    vowels = 'aeiou'
    # consonants = 'bcdfghjklmnpqrstvwxyz'
    
    (vowel_count, consonant_count) = (0, 0)

    for char in s.lower():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    return (vowel_count, consonant_count)

print(char_counts('hello'))


def mean(*args):
    tot = 0 
    for a in args:
        tot += a
    return tot/len(args)

print(mean(1,2,3,4,5,6))



#### Lists ####

#iterating over a list using a for loop

def sum_and_prod(l):
    """
    l is a list of numbers | 
    Rerun a tuple where the first value is the sum of all elements in l and the 
    second value is the product of all elements in l 
    """
    sum_l = sum(l)
    # prod_l = prod(l) - requires numpy.prod()
    
    num = 1
    for i in l:
        num *= i
    return (sum_l, num)
        
        
        



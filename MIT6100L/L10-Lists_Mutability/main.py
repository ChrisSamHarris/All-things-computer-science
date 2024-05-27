def make_ordered_list(n):
    """
    return a list of integers from 0 to n
    """
    result = []
    for i in range(n+1):
        result.append(i)
    return result

print(make_ordered_list(10))


def remove_el(ls, el):
    """
    remove element from a list
    """
    new_list = []
    for char in ls:
        if char != el:
            new_list.append(char)
    return new_list
            

print(remove_el([1,2,3, 3, 3, 3,3, 4,5], 3))


def count_words(sen):
    """
    Return the number of words in a sentence
    """
    words = sen.split(' ')
    return len(words)

print(count_words("I am a sentence with 7 words"))
    
    
def make_word(ls):
    """
    return a string from a list of characters
    """
    return ''.join(ls)


def sort_words(sen):
    """
    ---
    """
    l = sen.split(' ')
    l.sort()
    return l
    
    
print(sort_words("Look at this photograph"))


def square_list(ls):
    """
    return a list of the square of each element in ls
    """
    # return [i**2 for i in ls]
    for i in range(ls):
        ls[i] = ls[i]**2
    return ls

print(square_list([1,2,3,4,5]))


# Acquire the variable location in memory by using the id() function
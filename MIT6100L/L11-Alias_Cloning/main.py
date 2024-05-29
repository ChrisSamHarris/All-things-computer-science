from typing import List

def remove_all(L: List, e):
    LCopy = L[:]
    L.clear()
    
    for i in LCopy:
        if i != e:
            L.append(i)
            

L = [1,2,2,2,2]
remove_all(L,2)
print(L)




def remove_all2(L: List, e):
    while e in L:
        L.remove(e)
        
L = [1,2,2,2,2]
remove_all2(L,2)
print(L)

# `.remove()` -> Delete a specific element (if element occurs multiple times, it removes the first occurrence)
# `del(L[i])` -> Delete an element at a specific index 
# `.pop()` -> Removes the last item in a list (or at a specific index if `i` is supplied: `.pop(i)`)

def remove_duplicates_across_list(L1: List, L2: List) -> None:
    # wont work as we're mutating a list as we're mutating it, skipping over indicies 
    # for e in L1:
    #     if e in L2:
    #         L2.remove(e)
    
    L1C = L1[:]
    for e in L1C:
        if e in L2:
            L1.remove(e)
    
    # L1 = L1 + L2 
    # L1.sort()

L1 = [1,2,3,4,5,6,7, 8]
L2 = [3,4,5,7,9,10]

remove_duplicates_across_list(L1, L2)

print(L1)
print(L2)

# def remove_duplicates_merge(L1: List, L2: List) -> None:
#     L1C = L1[:]
#     for e in L1C:
#         if e in L2:
#             L1.remove(e)
    
#     L1 = L1 + L2 
#     L1.sort()
    
#     return L1

# L1 = [1,2,3,4,5,6,7,8]
# L2 = [3,4,5,7,9,10]

# remove_duplicates_merge(L1, L2)

# print(L1)

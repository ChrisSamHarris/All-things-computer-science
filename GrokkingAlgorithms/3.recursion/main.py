import time

# Recursion works so effectively due to the Call Stack/ Stack in memory
# The call stack manages function calls in a last-in, first-out (LIFO) manner, 
# where each recursive call adds a new frame to the stack until a base case is reached, 
# after which the stack unwinds as the function returns, resolving each call.

rocket= r"""
       !
       !
       ^
      / \
     /___\
    |=   =|
    |     |
    |     |
    |     |
    |     |
    |     |
   /|##!##|\
  / |##!##| \
 /  |##!##|  \
|  / ^ | ^ \  |
| /  ( | )  \ |
|/   ( | )   \|
    ((   ))
   ((  :  ))
   ((  :  ))
    ((   ))
     (( ))
      ( )
       .
       .
       .
"""
    

def countdown(i):
    if i > 0:
        print(i)
        time.sleep(0.5)
        countdown(i-1)
    else:
        print("Blastoff!")
        print(rocket)
        
    
# countdown(10)


def factoral(x):
    """
    Example: 
    3! = 3x2x1
    5! = 5x4x3x2x1
    """
    if x == 1:
        return 1
    else:
        return x * factoral(x-1)

print(factoral(3))
print(factoral(5))


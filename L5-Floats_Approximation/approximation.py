#We know that the square root of a number is the number which when multiplied 
# by itself gives the original number. In other words, if '3' is the square root of '9',
# it means that 3 × 3 = 9 and is expressed as √9 = 3. 

x=54321
epsilion = 0.01
num_guess = 0 
guess = 0.0 
# smaller increments means more values will be checked 
increment = 0.00001

while abs(guess**2 - x) >= epsilion and guess**2 <= x:
    # note as x increases as does the jump between our guesses, if we miss the epsilion, the loop will run forever
    guess += increment
    num_guess += 1
print(f'number of guesses = {num_guess}')
if abs(guess**2 - x) >= epsilion:
    # now reports failures 
    print(f'Failed to find the square root of {x}')
else:
    print(f'{guess} is close to the square root of {x}')
    print(f'The closest whole number for the square root of {x} is {round(guess)}')

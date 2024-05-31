# 23 million guesses using the approximation method
# in contrast 30 guesses using the bisection method, in the case where x = 54321

x=0.5
epsilion = 0.01
num_guess = 0 

if x > 1:
    low = 0
    high = x   
else:
    # Addressing `0 < x < 1`
    low = x 
    high = 1
guess = (high+low)/2.0

while abs(guess**2 - x) >= epsilion:
    if guess**2 > x:
        high = guess 
    else:
        low = guess
    guess = (high+low)/2.0
    num_guess += 1
    
print(f'number of guesses = {num_guess}')
print(f'{guess} is close to the square root of {x}')
# print(f'The closest whole number for the square root of {x} is {round(guess)}')
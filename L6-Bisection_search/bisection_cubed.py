cube = 1331
epsilion = 0.01
low = 0
high = cube 
num_guess = 0

guess = (high+low)/2.0

while abs(guess**3 - cube) >= epsilion:
    if guess**3 > cube:
        # guess too high
        high = guess 
    else:
        # guess too low
        low = guess
    guess = (high+low)/2.0
    num_guess += 1
    
print(f'number of guesses = {num_guess}')
print(f'{guess} is close to the cube root of {cube}')
print(f'The closest whole number for the cube root of {cube} is {round(guess)}')
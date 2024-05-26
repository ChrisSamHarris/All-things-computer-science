epsilion = 0.01
k = 24
guess = k/2.0
num_guess = 0 

while abs(guess*guess - k) >= epsilion:
    num_guess += 1
    guess = guess - (((guess**2)-k)/(2*guess))
print(f'number of guesses = {num_guess}')
print(f'{guess} is close to the square root of {k}')
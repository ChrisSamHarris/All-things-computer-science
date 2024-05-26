guess = 0
neg_value = False

x = int (input ("Enter an integer: ") )

if x < 0: 
    neg_value = True
    
while guess**2 < x:
    guess = guess + 1
    
if guess**2 == x:
    print ("Square root of", x, "is", guess)
else:
    print (x, "is not a perfect square")
    if neg_value:
        print ("Did you mean", x, "**2 ?")

# They are 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 
# 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 
# 841, 900 and 961.

##### Guess-and-Check #####
## poitive cubes
cube = int(input("Enter an integer: "))
for guess in range(cube+1):
    if guess**3 == cube:
        print(f"The cube root of {cube} is {guess}")
        break
    
## poitive & negative cubes
cube = int(input("Enter an integer: "))

# abs = absolute value of the number the user gave - positive value of the number
#abs = assumes the var cube is positive
for guess in range(abs(cube)+1):
    if guess**3 == cube:
        # converts the guess to a negative number if the cube is negative
        if cube < 0:
            guess = -guess
        print(f"The cube root of {cube} is {guess}")
        break

## break statements with p&n checks
cube = int(input("Enter an integer: "))
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
    if guess** 3 != abs(cube):
        print(f"{cube} is not a perfect cube")
    else:
        if cube < 0:
            guess = -guess
        print(f"The cube root of {cube} is {guess}")

    

        
# while loop to exit a path when the user goes left
where = input("Go left or right? ").lower()
n = 0

while where == 'right':
    n += 1
    if n > 1:
        print(":(")
    where = input("You're stuck! Go left or right? ").lower()
print('You found the treasure!')


# calculate factorial using a while loop
x = 4 
i = 1
factorial = 1 
while i <= x:
    factorial *= i
    i += 1
print(f'{x} factorial is {factorial}')
#In short, a factorial is a function that multiplies a number by every number 
# below it till 1. For example, the factorial of 3 represents the multiplication
# of numbers 3, 2, 1, i.e. 3! = 3 × 2 × 1 and is equal to 6.

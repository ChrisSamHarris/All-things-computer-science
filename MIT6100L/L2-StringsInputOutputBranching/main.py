# input output 
b = input("Give me verb: ")
print(f"I can {b} better than you " * 5, end='')

# branching using if/ else 
secret_num = 7
guess_num = int(input('Enter your guess number: '))
# print(secret_num == guess_num)

if guess_num > secret_num:
    print('Your guess is too high')
elif guess_num < secret_num:
    print('Your guess is too low')
else:
    print('You guessed it!')

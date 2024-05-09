#### EXCERCISE 1 ####
even_nums = 0 

for i in range(10):
    if i % 2 == 0:
        even_nums += 1
        print(i)
print(f"Total number of even numbers: {even_nums}")

#### EXCERCISE 2 ####
#  looping through strings 
s = "demo loops - fruit loops" 

# iterate through characters of s directly - dont need to use the index 
for char in s:
    if char == 'i' or char == 'u':
        print(f"there is an {char} in the string")

# iterates through characters of s directly - most "pythonic" solution 
for char in s:
    if char in 'iu':
        print(f"there is an {char} in the string")
        

#### EXCERCISE 3 ####
# Assume you are given a string of letters, count how many unique characters are in the string 
# e.g. "abca" = 3 

s = "abca"
string_var = ""

for char in s:
    if char not in string_var:
        # add char directly onto the string
        string_var += char
print(len(string_var))
# acquire the number of unique characters through length of string_var
    
#### EXCERCISE 4 ####
# Version 1 
secret_number = 5
for i in range(11):
    if i == secret_number:
        print("You guessed the secret number!")
    
# Version 2
secret_number = 11
seen_num = False # can also use a list - but booleans are useful for showing that something happened in your code 
for i in range(11):
    if i == secret_number:
        seen_num = True
        print(f"You guessed the secret number!: {i}")
if not seen_num:
    print("You did not guess the secret number...")
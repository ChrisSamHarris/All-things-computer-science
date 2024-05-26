n = 0 
while n < 5:
    print(n)
    n += 1
    
# shorthanded version using for loop
print('/n')
for n in range(5):
    print(n)

# `range(<start>,<stop>,<step>)`
for me in range(4,0,-1):
    print("$" * me)
    

mysum = 0 
for i in range(10):
    mysum += i
print(mysum)

# calculate factorial using a for loop 
x = 4 
factorial = 1 
for i in range(1,x+1):
    factorial *= i
print(f'{x} factorial is {factorial}')

#### motivation ####
x = 0 
for i in range(10):
	x += 0.1 
print(x == 1) # False
print(x) # 0.9999999999999999


#### converting to Binary ####
num = 1507

result = ''
if num == 0:
    result = '0'
while num > 0:
    # modulo '%' returns the remainder of the division - as we're using 2, it will return 0(even) or 1(odd)
    result = str(num % 2) + result
    num = num // 2
    
print(result)


#### converting to Binary - including negative numbers ####
num = 1507

if num < 0:
    neg_num = True
    num = abs(num)

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if neg_num:
    result = '-' + result
    
print(result)
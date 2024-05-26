# In numerical analysis, Newton's method, is a root-finding algorithm which produces 
# successively better approximations to the roots (or zeroes) of a real-valued function.
# The most basic version starts with a real-valued function f,
# its derivative f′, and an initial guess x0 for a root of f.

x = int(input('\n\nWhat x to find the cube root of? '))
g = int(input('What guess to start with? '))

print('current estimate cubed = ', g**3)
next_g = g - ((g**3 - x)/(3*g**2))
print('\nnext guess to try = ', next_g)

print('\n')
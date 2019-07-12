def fib(max):  
    a, b = 1, 1
    while a < max:  
        yield a  
        a, b = b, a + b  
  
for n in fib(15):  
    print(n)

# output:
# 1
# 1
# 2
# 3
# 5
# 8
# 13

m = fib(13)  
print(m)       # Print generator
print(next(m)) # Print the first value of generator
print(next(m)) # Print the second value of generator
print(next(m)) # Print the third value of generator

# Output:
# <generator object fib at 0x0563D378> 
# 1
# 1
# 2


# ----------------------------------------------------------------
a = 1
b = 2
a, b = b, a + b
print(b)

a = 1
b = 2
a = b
b = a + b
print(b)

# Output:
# 3
# 4
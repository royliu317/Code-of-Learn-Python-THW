# The rule of variable scopes: L（Local） –> E（Enclosing） –> G（Global） –>B（Built-in）
x1 = int(1)     # Bulit-in
x2 = 2          # global
def outer():
    x3 = 3      # Enclosing
    def inner():
        x4 = 4  # Local
        print(x1, x2, x3, x4)
    inner()
outer()



# Keywords: global, nonlocal
numbers = []
i = 0
def mywhile(j):
    global i
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)    
        i += 1    
        # If not use global in the function，it will raise UnboundLocalError: local variable 'a' referenced before assignment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

mywhile(3)
print("The numbers: ")
for num in numbers:
    print(num)

print(f"Now i is: {i}\nNow numbers is: {numbers}")
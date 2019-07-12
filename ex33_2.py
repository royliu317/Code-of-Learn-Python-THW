i = 0
numbers = []

def mywhile(j, k):
    global i
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)            
        i += k
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

a = int(input("Please input the stop number:"))
b = int(input("Please input the incremental number:"))
mywhile(a, b)

print("The numbers: ")

for num in numbers:
    print(num)



#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("Use for and range() to replace")

numbers = []
for i in range(0, 6):
    print(f"At the top i is {i}")
    numbers.append(i)            
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

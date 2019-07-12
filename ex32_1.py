the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    #variable named number is assigned the value of each element
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

print(">>>>after range(), i=", i) 

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

elements.append(the_count)
print(f"{the_count}\n{fruits}\n{change}\n{elements}")

#-------------------------------------------------------------------
print("-------------------------------------------------------------")

print("循环打印列表中的部分数据项")
for i in elements[1:3]: # go through index(1) ~ index(3-1)
    print(f"Part_Element was: {i}")
print("\n")

print("list()函数的用法")
a = range(0, 6)
print(a, type(a))
b = list(range(5, 0, -2))
print(b, type(b))


# range(start int, stop int[, step])
# range(0, 6) = range (int 0 ~ int 6-1) => 0, 1, 2, 3, 4, 5
# list[0:6] = list [index 0 ~ index 6-1] => -3, -2, -1, 0, 1, 2 (Supposing list = [-3, -2, -1, 0, 1, 2, 3, 4, 5]) 

# append(): list.append(obj)
# extend(): list.extend(seq)

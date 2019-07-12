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

print(">>>>after range(), i=", i) # 注意：变量i会保留最后一次循环时，在range()函数内赋给它的值

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


# range()函数 返回的是一个可迭代对象（类型是对象，一个整数序列的对象），而不是列表， 所以打印的时候不会打印列表。
# range(start int, stop int[, step])
# 参数start: 计数从start开始。默认是从0开始。例如range（5）等价于range（0，5）; 
# stop: 计数到stop结束，但不包括stop。例如：range（0，5）是[0, 1, 2, 3, 4]，不包括5；
# step：步长，默认为1（正1）。例如：range（0， 5） 等价于 range(0, 5, 1)。
# range(0, 6) = range (int 0 ~ int 6-1) => 0, 1, 2, 3, 4, 5
# list[0:6] = list [index 0 ~ index 6-1] => -3, -2, -1, 0, 1, 2 (假设list = [-3, -2, -1, 0, 1, 2, 3, 4, 5]) 
# 因此，range(0, 6)是建一个以0开始，以6-1结尾，且递增为1的整数序列对象；而list[0:6]是取列表中索引从0到6-1的数据项

# list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，转化后的对象为List类型。例如，list(range(0, 10, 2))，list(range(1, -5, -1))。即list()就是将range()对象列表化。


# append()方法 用于在列表末尾添加新的对象。
# list.append(obj)
# 参数obj：添加到列表末尾的对象。
# 返回值：该方法无返回值，但是会修改原来的列表。

# extend()函数 用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# list.extend(seq)
# 参数seq：元素列表。
# 返回值：该方法没有返回值，但会在已存在的列表中添加新的列表内容。

# extend 与 append 方法的相似之处在于都是将新接收到参数放置到已有列表的后面。而 extend 方法只能接收 list，且把这个 list 中的每个元素添加到原 list 中。而 append 方法可以接收任意数据类型的参数，并且简单地追加到 list 尾部。
# 列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。append() 方法向列表的尾部添加一个新的元素。
# 列表是以类的形式实现的。“创建”列表实际上是将一个类实例化。因此，列表有多种方法可以操作。extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。
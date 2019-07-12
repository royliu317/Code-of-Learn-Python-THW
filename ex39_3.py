# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。我们可以使用 list() 转换来输出列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。利用 * 号操作符 zip(*zip(a, b))，可以将元组反向解压回列表List。
# zip([iterable, ...])
# 参数iterable: 一个或多个迭代器
# 返回值: 返回一个对象


a1 = [1,2,3]
b1 = [4,5,6]
c1 = [4,5,6,7,8]
zipped1 = zip(a1, b1)       # 返回一个对象
print(zipped1, type(zipped1))    
print(list(zipped1))      # list()将zipped转换为列表

zipped2 = zip(a1, c1)
print(list(zipped2))    # 元素个数与最短的列表一致

d1 = zip(*zip(a1, b1))      # 与 zip 相反，zip(*)将元组反向解压回列表，返回二维矩阵式
print(list(d1))

e1, f1 = zip(*zip(a1,b1)) # 把解压回的列表的第1个元素给d1，第2个给d2（等同于for d in list的赋值方式）。对集合类型均可用此方式给变量赋值，但变量数量必须与list中的元素数量相同，详见下例。
print(list(e1), list(f1))


print("-------------------------------------------------------------")
a = [1, 2, 3, 4]    #List类型
b, c, d, e = a
print(b, c, d, e)

f = range(0, 2)     #range类型
g, h = f
print(g, h)

m = {'Name': 'Runoob', 'Age': 7, 'Gender': 'Nv', 'Test': 34}    #Dict类型
n, o, p, q = m
print(n, o, p, q)



print("-------------------------------------------------------------")
dict = {'Name': 'Runoob', 'Age': 7, 'Gender': 'Nv', 'Test': 34}

for i in dict:
	print(i)
#output: print key loop


for i in dict.keys():
	print(i)
#output: print key loop


for j in dict.values():
	print(j)
#output: print values loop


for i,j in dict.items():
	print(i, ":", j)
#output: print key:value loop


del dict['Name']    # 删除键 'Name'
print(dict)
dict.clear()        # 清空字典内容
print(dict)
del dict            # 删除字典，即该字典不再存在了
print(dict)


print("-------------------------------------------------------------")
print("使用字典的dict(**d1, **d2)方法合并字典")
x = {'a':1, 'b':2}
y = {'c':3, 'd':4}
z = {'e':5, 'f':6}
mydict = {**x, **y, **z}
print(mydict)

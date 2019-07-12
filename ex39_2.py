print("通过 values 取到 key 的方法:")
mydict = {'Name': 333 , 'Age': 666, 'Gender': 888, 'Test': 999}
a = list(mydict.values()).index(666)    #list(a).index(x) 用于返回列表a中元素x的索引值，即通过元素找索引
# mydict.values返回由字典的values所构成的一个迭代器（dict_values对象），再通过list()将其转换为列表[333, 666, 888, 999]，最后取元素为666的index值（即1）
    
b = list(mydict.keys())[a]
# mydict.keys返回由字典的keys所构成的一个迭代器（dict_keys对象），再通过list()将其转换为列表['Name', 'Age', 'Gender', 'Test']，最后取index为1的元素（即Age）

print(b)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("获取字典中最大的值，以及其所对应的键:")
prices = {
    'A':123,
    'B':450.1,
    'C':12,
    'E':444,
}

a = list(zip(prices.values(), prices.keys()))
print(a)

max_prices = max(zip(prices.values(), prices.keys()))
print(max_prices)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("调换字典的key和value（当然要注意原始value必须是不可变类型）:")
dic = {
    'a': 1,
    'b': 2,
    'c': 3,
}

reverse = {v: k for k, v in dic.items()}
# 如上等同于：
# for k, v in dic.items():
#     reverse = {v: k}

print(dic)
print(reverse)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("用字典记录学生名字和分数，再分级:")
students= {}
write = 1
while write :
    name = str(input('输入名字:'))
    grade = int(input('输入分数:'))
    students[name] = grade      #向字典内添加键值对元素
    write= int(input('继续输入？\n 1/继续  0/退出'))
print('Name  Rate'.center(20,'-'))
for key,value in students.items():
    if value >= 90:
        print(f'{key} {value} A Level'.center(20,'-'))
    elif 89 > value >= 60 :
        print(f'{key} {value} B Level'.center(20,'-'))
    else:
        print(f'{key} {value} C Level'.center(20,'-'))
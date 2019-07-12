print("**For List type**")
import copy
list1 = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
list2 = list1                 #赋值引用：传对象的引用，即list1和list2指向同一个对象
list3 = list1.copy()          #对象拷贝，浅拷贝：list1和list3是两个独立的对象，但他们的子对象还是引用同一对象。即完全拷贝父对象（一级目录），子对象（二级目录）不拷贝，仍为引用
# 如上也可替换为 list3 = copy.copy(list1) 或 list3 = list1[:]   
list4 = copy.deepcopy(list1)  #对象拷贝，深拷贝：list4完全拷贝list1的父对象及其子对象，两者完全独立。
 
list1.append(5)            #修改对象a
list1[4].append('c')       #修改对象a中的['a', 'b']数组对象
 
print( 'list1 = ', list1)
print( 'list2 = ', list2)
print( 'list3 = ', list3)
print( 'list4 = ', list4)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("**For Dictionary type**")
import copy

dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 赋值引用: dict1和dict2都指向同一个对象。
dict3 = dict1.copy()   # 对象拷贝，浅拷贝：dict1和dict3是两个独立的对象，但他们的子对象还是引用同一对象。即完全拷贝父对象（一级目录），子对象（二级目录）不拷贝，仍为引用
dict4 = copy.deepcopy(dict1) # 对象拷贝，深拷贝：完全拷贝父对象及其子对象，两者完全独立。

dict1['user']='root'
dict1['num'].remove(1)
 
print(dict1)
print(dict2)
print(dict3)
print(dict4)


# Python 直接赋值、浅拷贝和深度拷贝解析: http://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
# 直接赋值--同一对象，之后再修改也完全一样；浅拷贝--两个对象，之后再修改二级还一样；深拷贝--两个对象，之后再修改完全不一样
# 可更改(mutable)与不可更改(immutable)对象：http://www.runoob.com/python3/python3-function.html

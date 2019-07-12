##import sys           # import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
 
##print('命令行参数如下:')
##for i in sys.argv:   # sys.argv 是一个包含命令行参数的列表list(从命令行输入的参数的列表list)。
##   print(i)
 
##print('\n\nPython解释器的搜索路径包括：', sys.path, '\n')    # sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表list。
# 了解了搜索路径的概念之后，就可以在脚本中修改sys.path来引入一些不在搜索路径中的模块。


# import 与 from...import 
# http://www.runoob.com/python3/python3-basic-syntax.html
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule ，调用模块中的内容时需要加前缀(module.xxx)
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction ，调用时不需再加模块名作为前缀
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import * ， 调用时不需再加模块名作为前缀（大多数情况，Python程序员不使用这种方法，因为引入的其它来源的命名，很可能会覆盖已有的定义）
# from package import item 可以导入包、模块、类、函数、变量
# import item.subitem.subsubitem 只能导入包或模块


#-------------------------------------------------------------------
import ex25       # 模块，访问其内部，其实就是通过字典来驱动的（键:值-->属性名：属性值/代码块）
print("", ex25.__dict__)    
print()

print("", ex25.__dict__.keys())
print()

print(globals())     # globals() 函数会以字典类型返回当前位置的全部全局变量，包括所有导入的变量。参数: 无，返回值: 返回全局变量的字典dictionary。
print()              # 实际上python在其系统内部就是通过使用一个字典，来跟踪当前你所创建的变量。由此可以看到字典对python的重要性和广泛应用性（变量，字典，模块，类，对象，等等等等）

a = ex25.sort_sentence("this is a test")
print(a)

b = ex25.__dict__['sort_sentence']("this is a test")   # (用字典的方式)调用模块ex25的内部字典的'sort_sentence'键，所对应的代码快。该代码块即为sort_sentence()函数内容，所以能直接处理后续字符串
print(b)


# Python3 __dict__与dir()区别，对象中私有属性的访问
# https://blog.csdn.net/u011630575/article/details/53704539

# __dict__是用来存储对象属性的一个字典dictionary，键为属性名，值为属性值；dir()是一个函数，返回的是列表list。
# dir()函数会自动寻找一个对象的所有属性，包括__dict__中的属性。__dict__是dir()的子集，dir()包含__dict__中的属性。
# dir()函数可以找到模块内定义的所有名称，并以字符串列表list的形式返回
# 由于并不是所有对象都拥有__dict__属性。许多内建类型就没有__dict__属性，如list，所以这时就需要用dir()来列出对象的所有属性。

# 实例的__dict__仅存储与该实例相关的实例属性，正是因为实例的__dict__属性，每个实例的实例属性才会互不影响。
# 类的__dict__存储所有实例共享的变量和函数(类属性、方法等)，类的__dict__并不包含其父类的属性。

# dir()是Python提供的一个API函数，dir()函数会自动寻找一个对象的所有属性(包括从父类中继承的属性)。
# 一个实例的__dict__属性仅仅是那个实例的实例属性的集合，并不包含该实例的所有有效属性。所以如果想获取一个对象所有有效属性，应使用dir()。


#-------------------------------------------------------------------
print('-------------------------------------------------------------------')
print("__dict__与dir()的区别：")
class A(object):
    my_var = 1
    def __init__(self):
        self.my_name_var = 'xy'
        self.my_age_var = 2
 
    @property
    def my_num_func(self):          # 属性（而非方法）
        return self.my_age_var + 10
 
    def my_fun_func(self):pass      # 实例方法
    def my_static_f_func():pass     # 静态方法
    def my_class_f_func(cls):pass   # 类方法
 
if __name__ == '__main__':          #主程序
    a = A()
    print("实例a自己的实例属性:\n", a.__dict__)   # 输出结果：{'age': 2, 'name': 'xy'}  
    print("类A的__dict__的类属性、方法等(即所有实例共享的变量和函数):\n", A.__dict__)
    print("实例a的所有有效属性(包括从父类中继承的属性):\n", dir(a))  # 输出结果，与下一行相同，只是多了实例A自己的实例属性age、name
    print("类A的所有有效属性为:\n", dir(A))       


# A.__dict__ 输出结果，是类A的所有实例共享的变量和函数（类属性、方法等）：
# {
##'__dict__': <attribute '__dict__' of 'A' objects>,		
##'__doc__': None,								                          #class说明字符串
##'__init__': <function A.__init__ at 0x00000000021A89D8>,
##'__module__': '__main__',					                              #所处模块
##'__weakref__': <attribute '__weakref__' of 'A' objects>,
##'my_class_f_func': <function A.my_class_func at 0x00000000021A8BF8>,	  #类方法
##'my_fun_func': <function A.my_fun_func at 0x00000000021A8AE8>,		  #实例方法	
##'my_num_func': <property object at 0x0000000001D49A98>,		          #属性（而非方法）
##'my_static_f_func': <function A.my_static_func at 0x00000000021A8B70>,  #静态方法
##'my_var': 1
# }

# dir(A) 输出结果，是类A的所有有效属性（包括__dict__中的属性）:
# [
# '__class__',
# '__delattr__',
##'__dict__',
# '__dir__',
##'__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__gt__',
# '__hash__',
##'__init__',
# '__init_subclass__',
# '__le__',
# '__lt__',
##'__module__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__setattr__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
##'__weakref__',
##'my_class_f_func',
##'my_fun_func',
##'my_num_func',
##'my_static_f_func',
##'my_var',
# ]
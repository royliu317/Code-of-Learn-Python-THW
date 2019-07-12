# Python保留字详解
# https://weibo.com/ttarticle/p/show?id=2309404215256372118805
# https://blog.csdn.net/Already233/article/details/80383779
# https://blog.csdn.net/zxr15709447338/article/details/80872389


# Python中下划线的5种含义:
# https://zhuanlan.zhihu.com/p/36173202
# name mangling 名称修饰: 双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。即解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。
# 如果一个名字同时以双下划线开始和结束，则不会应用名称修饰。由双下划线前缀和后缀包围的变量不会被Python解释器修改。
# 但是，Python保留了有双前导和双末尾下划线的名称，用于特殊用途。 这样的例子有，__init__对象构造函数，或__call__它使得一个对象可以被调用。


# 深入理解Python中的 __new__ 和 __init__
# https://blog.csdn.net/luoweifu/article/details/82732313


# import 与 from...import 
# http://www.runoob.com/python3/python3-basic-syntax.html
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule ，调用模块中的内容时需要加前缀(module.xxx)
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction ，调用时不需再加模块名作为前缀
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import * ， 调用时不需再加模块名作为前缀（大多数情况，Python程序员不使用这种方法，因为引入的其它来源的命名，很可能会覆盖已有的定义）
# from package import item 可以导入包、模块、类、函数、变量
# import item.subitem.subsubitem 只能导入包或模块


# yield的用法 https://zhuanlan.zhihu.com/p/32178981 ：
def fib(max):  
    a, b = 1, 1
    while a < max:  
        yield a  
        a, b = b, a + b  
  
for n in fib(15):  
    print(n)

# 输出结果:
# 1
# 1
# 2
# 3
# 5
# 8
# 13

m = fib(13)  
print(m) #打印生成器  
print(next(m)) #打印生成器的第一个值  
print(next(m)) #打印生成器的第二个值   
print(next(m)) #打印生成器的第三个值

# 输出结果:
# <generator object fib at 0x0563D378> 
# 1
# 1
# 2


# ----------------------------------------------------------------
# 注意： a, b = b, a+b  不等于如下（在此，b并未赋值给a，a与b的赋值没有先后顺序）：
# a = b
# b = a + b 
a = 1
b = 2
a, b = b, a + b
print(b)

a = 1
b = 2
a = b
b = a + b
print(b)

# 输出结果:
# 3
# 4
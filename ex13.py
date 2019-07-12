from sys import argv    #通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
#read the WYSS section for how to run this.
script, first, second, third = argv #参数变量argv保存着你运行Python脚本时，传递给.py脚本的参数

print(">>>> argv=", repr(argv)) #添加调试打印用于排错，显示出python是如何“读”argv这个参数变量的

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Some extension based on above statement
third = input("third = ") #Is this variable "third" same as the one in argv? NO!

print(">>>> argv =", repr(argv)) #third in argv is still 3rd since it is within a list
print(">>>> third = ", repr(third)) #third in here is the inputed argument


#如果给参数变量argv设为需要传递3个参数（如上。script是系统默认，不算为一个需额外传递参数的变量），但如果在运行脚本时我们只输入/传递了2个命令行参数，则会报错：
#ValueError: not enough values to unpack (expected 4, got 3)
#如果给参数变量argv设为需要传递3个参数（如上，script是系统默认，不算为一个需额外传递参数的变量），但如果在运行脚本时我们输入/传递了4个命令行参数，则会报错：
#ValueError: too many values to unpack (expected 4)
#与input()类似，命令行参数也是将参数识别为字符串 


# import 与 from...import 
# http://www.runoob.com/python3/python3-basic-syntax.html
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule ，调用模块中的内容时需要加前缀(module.xxx)
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction ，调用时不需再加模块名作为前缀
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import * ， 调用时不需再加模块名作为前缀（大多数情况，Python程序员不使用这种方法，因为引入的其它来源的命名，很可能会覆盖已有的定义）
# from package import item 可以导入包、模块、类、函数、变量
# import item.subitem.subsubitem 只能导入包或模块
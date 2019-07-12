class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print(f"{self.name}说: 我 {self.age}岁, {self.__weight}厘米。")
 
# 实例化类
p = people('runoob',10, 30)
p.speak()
print(people.name, people.age, p.name, p.age)
# print(people.__weight, p.__weight)    # 私有属性，不能在类的外部被使用或直接访问，所以系统会报：xxx has no attribute '__weight'
print(people._people__weight, p._people__weight)    # 使用由python解释器进行名称修饰之后的变量名，才可访问类中的私有属性。


# 双下划线前缀(dunder scores)会导致Python解释器重写属性/方法的名称(object._class__property或method)，以避免子类中的命名冲突。
# 这也叫做名称修饰（name mangling） - 解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。
# 类的私有属性__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。


#-------------------------------------------------------------------
print("在python中，方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做'魔法'方法")
class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):           # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从这个方法中return的数据
        return f'这个人的名字是{self.name},已经有{self.age}岁了！'

a = people('孙悟空', 999)
print(a)


#-------------------------------------------------------------------
print("运算符重载的使用：")
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):           
      return f'Vector ({self.a}, {self.b})'
   
   def __add__(self,other):      # 运算符重载
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(3, 1)
v2 = Vector(5, -2)
print(v1 + v2)
print(v1)
print(v2)

# 类可重载所有Python表达式运算符（如加减运算），也可重载打印、函数调用、属性点号运算等内置运算。重载是通过提供特殊名称的类的方法来实现的（即__x__）。
# 运算符重载使我们的对象的行为，与内置对象的一样，Python在调用操作符时会自动调用这样的方法。
# 例如，如果类实现了__add__方法，当类的对象出现在+运算符中时，就会调用这个add方法。否则，系统是不会理解让两个对象相加是什么意思的。
# 当然，有些运算符是不能重载：赋值运算符、逻辑运算符。
# 对于反向运算符的重载，其实正向和反向调用使用的是同一系列方法。例如，对 == 来说，正向和反向调用都是 __eq__ 方法，只是把参数对调了。
# 例如，__add__运算符重载可以保证V+int的情况下不会报错，但是反过来int+V就会报错，所以通过反向运算符重载，可以解决此问题。
        

#-------------------------------------------------------------------
print("python为解释执行，程序在调用函数foo()之前，由于已先声明了bar和foo（函数bar和foo的声明/定义无顺序之分），所以不会报错")
def bar():
    print("in the bar")
def foo():
    print("in the foo")
    bar()
foo()

def foo():
    print("in the foo")
    bar()
def bar():
    print("in the bar")
foo()
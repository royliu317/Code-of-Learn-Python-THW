print('在Python的解释器内部，当我们调用t.prt()时，实际上Python解释成Test.prt(t)，也就是说把self替换成类的实例，即对于实例方法来说，self在定义时不可以省略')
class Test:
    def prt():
        print(self)

t=Test()
# t.prt()   运行该语句时会报错：prt在定义时没有参数，但是我们运行时强行传了一个参数。由于上面解释过了t.prt()等同于Test.prt(t)，所以程序提醒我们多传了一个参数t。


# ---------------------------------------------------------------------------------
print('\n\n如果我们的定义和调用时均不传实例self是可以的，这时它是简单函数，即不需要实例化类就可以调用的函数')      # 在类中定义简单函数，在Python中使用的比较少
class Test:
    def prt():
        print(__class__)

Test.prt()                 # 只能基于 类.方法 进行调用，不能基于 实例.方法 进行调用（因为会报错少传了一个self参数）


# ---------------------------------------------------------------------------------
print('\n\n在继承时，传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例')
class Parent:
    
    def pprt(self):
        print(self)

class Child(Parent):
    def cprt(self):
        print(self)

c = Child()
c.cprt()
c.pprt()    # c.pprt()等同于Child.pprt(c)，因此self指的仍是Child类的实例。由于self中未定义pprt()方法，所以沿着继承树往上找，发现在父类Parent中定义了pprt()方法，就会成功调用，并打印Child类的实例。

p = Parent()
p.pprt()


# 总结：
# self在定义实例的方法时是必须有的，虽然在调用时不必传入相应的参数（调用时会自动传入）
# self的名字并不是规定死的，但是最好还是按照约定是用self
# self总是指调用时的类的实例(注意：不是类本身)，这样当有多个实例化对象时，才不至于混淆不知道调用的是哪一个实例的方法或属性
# self只有在实例的方法中才会有，独立的函数或方法是不必带有self的。

# Python中self和__init__的含义与使用：
# https://blog.csdn.net/love666666shen/article/details/78189984


# Python 子类继承父类构造函数说明:
# http://www.runoob.com/w3cnote/python-extends-init.html


# 如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。
# 如果子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。
class Father(object):
    def __init__(self, name):
        self.name = name
        print("name: %s" %(self.name))
    def getName(self):
        return 'Father ' + self.name
 
class Son(Father):
    def getName(self):
        return 'Son '+ self.name
 
if __name__=='__main__':
    son=Son('runoob')
    print(son.getName())
    print()


# 如果子类重写了__init__ ，实例化子类时，就不会调用父类已经定义的 __init__
class Father(object):
    def __init__(self, name):
        self.name=name
        print ( "name: %s" %( self.name) )
    def getName(self):
        return 'Father ' + self.name
 
class Son(Father):
    def __init__(self, name):
        print ( "hi" )
        self.name =  name
    def getName(self):
        return 'Son '+self.name
 
if __name__=='__main__':
    son=Son('runoob')
    print( son.getName())
    print()



# 如果子类重写了__init__ ，但同时还想继承/调用父类的构造方法，可以使用 super 关键字
# super(子类，self).__init__(参数1，参数2，....)
# 或者一种经典写法： 父类名称.__init__(self,参数1，参数2，...)
class Father(object):
    def __init__(self, name):
        self.name=name
        print ( "name: %s" %( self.name))
    def getName(self):
        return 'Father ' + self.name
 
class Son(Father):
    def __init__(self, name):
        super(Son, self).__init__(name)
        print ("hi")
        self.name =  name
    def getName(self):
        return 'Son '+self.name
 
if __name__=='__main__':
    son=Son('runoob')
    print(son.getName())
    print()

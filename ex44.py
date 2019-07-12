# 继承的三种使用方式
class Parent(object):
    
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child1(Parent):

    def override(self):
        print("CHILD1 override()")

    def altered(self):
        print("CHILD1, BEFORE PARENT altered()")
        super(Child1, self).altered()
        print("CHILD1, AFTER PARENT altered()")

dad = Parent()
son = Child1()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()



print('\n\n-------------------------------------------------------')
# 组合的使用方式
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.property1 = Other()    # 给Child类创建一个属性，并将实例化的Other类赋予该属性

    def implicit(self):
        self.property1.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.property1.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
class Test:
    def prt():
        print(self)

t=Test()


# ---------------------------------------------------------------------------------
class Test:
    def prt():
        print(__class__)

Test.prt()  


# ---------------------------------------------------------------------------------
class Parent:
    
    def pprt(self):
        print(self)

class Child(Parent):
    def cprt(self):
        print(self)

c = Child()
c.cprt()
c.pprt() 

p = Parent()
p.pprt()

class people:
    # Basic attribute
    name = ''
    age = 0
    # Private attribute
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print(f"{self.name}: I am {self.age} years old, and my height is {self.__weight}cm。")
 
p = people('runoob',10, 30)
p.speak()
print(people.name, people.age, p.name, p.age)
print(people._people__weight, p._people__weight)    


#-------------------------------------------------------------------
print("Magic method：")
class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):           
        return f'Name is {self.name}, Age is {self.age}！'

a = people('Mike', 999)
print(a)


#-------------------------------------------------------------------
print("Operator overloading：")
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):           
      return f'Vector ({self.a}, {self.b})'
   
   def __add__(self,other):    
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(3, 1)
v2 = Vector(5, -2)
print(v1 + v2)
print(v1)
print(v2)
       

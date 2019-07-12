import ex25
print("", ex25.__dict__)    
print()

print("", ex25.__dict__.keys())
print()

print(globals()) 
print()          

a = ex25.sort_sentence("this is a test")
print(a)

b = ex25.__dict__['sort_sentence']("this is a test") 
print(b)


#-------------------------------------------------------------------
print('-------------------------------------------------------------------')
print("Different between __dict__ and dir() ：")
class A(object):
    my_var = 1
    def __init__(self):
        self.my_name_var = 'xy'
        self.my_age_var = 2
 
    @property
    def my_num_func(self):                                                                     # Property
        return self.my_age_var + 10
 
    def my_fun_func(self):pass                                                                 # Instance method
    def my_static_f_func():pass                                                                # Static method
    def my_class_f_func(cls):pass                                                              # Class method
 
if __name__ == '__main__':          
    a = A()
    print("Instance attribute of Instance a :\n", a.__dict__)                                  # Output：{'age': 2, 'name': 'xy'}  
    print("Class attribute and methods of class A's __dict__):\n", A.__dict__)
    print("All valid attributes of instance a(includes the inherited attributes):\n", dir(a))  # Output is same as below except the properites of age and name for instance A
    print("All valid attributes of class A:\n", dir(A))       
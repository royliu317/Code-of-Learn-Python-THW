def ChangeInt(myint):
    myint = 10
    print(myint) 
 
int1 = 2 
ChangeInt(int1)

print(int1) 


#-------------------------------------------------------------------
print("-------------------------------------------------------------")

def changeme(mylist):
   "Change the list passed in" 
   mylist.append([1,2,3,4])
   print("Get the value inside the function:", mylist) 
   return

list1 = [10,20,30]
changeme(list1)

print("Get the value ouside the function: ", list1) 


#-------------------------------------------------------------------
print("-------------------------------------------------------------")

def sum( arg1, arg2 ):
   mytotal = arg1 + arg2
   print ("Inside the funtion:", mytotal)
   return mytotal
 
total1 = sum( 10, 20 )
print ("Outside the function:", total1)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
# The four variable scopes
x = int(2.9)         # 1
 
g_count = 0          # 2   
def outer():
    o_count = 1      # 3
    def inner():
        i_count = 2  # 4


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
# Global and local variables
total = 0 # global variable

def sum(arg1, arg2):
    total = arg1 + arg2 # local variable
    print ("local variable : ", total)
    return total

sum(10, 20)
print ("global variable : ", total)



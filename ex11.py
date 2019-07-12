print("How old are you?", end=' ')
age = input() 
print("How tall are you?", end=' ' )
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
a = input("Please input a float number:")
print(type(a))                              # input() receives any types of input and will return with string type.
a = input("Please input a boolean value :")
print(type(a))


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Same effect as Line 8
print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight)) 


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("How old are you again?", end=' ') 
age = int(input())                          # Convert the input to other types in Line2. 
                                            # So if the input is NOT integar, then the convert can't work, thus the system will report "ValueError: invalid literal for int() with base 10: 'xxx'"
print(">> age=", repr(age))            
                                            
print("How tall are you again?", end=' ' )
height = input()
print("How much do you weigh again?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")







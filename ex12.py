age = input("How old are you? ")
height = input("How tall are you? ")        # "TypeError: input expected at most 1 arguments, got 2" will raise if more than 1 string is pu inside input()
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Some extension based on above statement
age = int(input("How old are you? "))
height = input(f"You are {age}? Nice. \nHow tall are you? ") 
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# python -m pydoc input
age = input("How old are you? ")
height = input("How tall are you? ") #input()内最多只能放入1个字符串，放入多个则会报错 “TypeError: input expected at most 1 arguments, got 2”
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Some extension based on above statement
age = int(input("How old are you? "))
height = input(f"You are {age}? Nice. \nHow tall are you? ") 
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


#调出input帮助信息：python -m pydoc input
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
print(type(a)) #函数 input() 用于接收任意属性输入，且默认为字符串处理，并返回字符串类型
a = input("Please input a boolean value :")
print(type(a))


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Same effect as Line 8
print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight)) 


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("How old are you again?", end=' ') 
age = int(input()) #Convert the input to other types in Line2. 
#So if the input is NOT integar, then the convert can't work, thus the system will report "ValueError: invalid literal for int() with base 10: 'xxx'"
print(">> age=", repr(age)) # 函数 repr(object) 用于将对象转化为供python解释器读取的形式，返回对象的string格式。但如果（）内为可执行的指令，则在呈现时指令仍会运行
#因此，假如age输入的是数字4，则呈现的就是4；如age是字符串test，则呈现的是带引号的"test"）
print("How tall are you again?", end=' ' )
height = input()
print("How much do you weigh again?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")







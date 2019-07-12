types_of_people = 10
x = f"There are {types_of_people} types of people." #使用 f-string 格式化字符串，即f"{}"，创建嵌入变量内容的字符串

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}" #大括号之间不能有空格，否则被识别为字符，造成.format()命令无效，错误提示为KeyError: ' '

print(joke_evaluation.format(hilarious)) #使用 .format() 语法，在已经创建的字符串/变量上应用格式化
print(">>>>", joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) #若将加号替换为逗号，则打印时w与e之间会有一个空格。用加号则不会有空格。


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Same result as above after changed Line17
print(joke_evaluation    .    format(hilarious)) #空格在很多情况下是被系统忽略的

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) #若将加号替换为逗号，则打印时w与e之间会有一个空格。用加号则不会有空格。

print("-------------------------------------------------------------")
#Same result as above after changed Line2
x = f"There are {10} types of people." #使用 f-string 格式化字符串，在 f"{}" 中不止可以用变量

print(x)
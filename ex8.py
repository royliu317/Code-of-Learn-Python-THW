formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) #该语句表示调用formatter的format函数，给format传递4个参数，与formatter中的4个{}匹配
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True)) #如果用小写开头，则不会被识别为布尔值
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Lack of one {} is fine, as the system will discard the additional arguments. 
formatter = "{} {} {}"

print(formatter.format(1, 2, 3, 4)) #该语句表示调用formatter的format函数，给format传递4个参数，与formatter中的4个{}匹配
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True)) 
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

#However, if there is no enough arguments for {}, then the system will prompt "IndexError: tuple index out of range".
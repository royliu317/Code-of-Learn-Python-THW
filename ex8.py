formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))                 #Call formatter.format() and pass the 4 parameters into it.
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))   #If use lowercase, then it will not be recognized as Boolean
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

print(formatter.format(1, 2, 3, 4)) 
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
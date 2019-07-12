from sys import argv    

script, first, second, third = argv 

print(">>>> argv=", repr(argv)) 

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Some extension based on above statement
third = input("third = ")           #Is this variable "third" same as the one in argv? NO!

print(">>>> argv =", repr(argv))    #third in argv is still 3rd since it is within a list
print(">>>> third = ", repr(third)) #third in here is the inputed argument

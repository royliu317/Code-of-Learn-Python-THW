types_of_people = 10
x = f"There are {types_of_people} types of people." # Use f-string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"   # No space is allowed inside {}，or it will be recognized as character and cause format() invalid and raise KeyError: ' '

print(joke_evaluation.format(hilarious))            
print(">>>>", joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)                                        # If use , to replace + then there will a space between w and e in the output


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Same result as above after changed Line17
print(joke_evaluation    .    format(hilarious))    

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)                                        

print("-------------------------------------------------------------")
#Same result as above after changed Line2
x = f"There are {10} types of people."              # use f-string. Not only varables can be put in f"{}"

print(x)
ten_things = "Apples Oranges Crows Telephone Light Sugar" 

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
"Corn", "Banana", "Girl", "Boy"]   

while len(stuff) != 10:
        next_one = more_stuff.pop()     # If no elements can be removed via pop, it will raise IndexError: pop from empty list
        print("Adding: ", next_one)
        stuff.append(next_one)
        print(f"THere are {len(stuff)} items now.")
    
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])                      # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))                # What? cool!
print('#'.join(stuff[3:5]))           # super stellar!


#-------------------------------------------------------------------
print("\n-------------------------------------------------------------")
print("Use for to replace above while")
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
"Corn", "Banana", "Girl", "Boy"]   

more_stuff.reverse()
for more in more_stuff:
    if len(stuff) != 10:
        print("Adding: ", more)
        stuff.append(more)
        print(f"There are {len(stuff)} items now.")
    else:
        break

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])                      # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))                # What? cool!
print('#'.join(stuff[3:5]))           # super stellar!
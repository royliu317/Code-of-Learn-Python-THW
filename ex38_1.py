ten_things = "Apples Oranges Crows Telephone Light Sugar" 

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
"Corn", "Banana", "Girl", "Boy"]    #可以在多行中给列表赋元素

while len(stuff) != 10:
        next_one = more_stuff.pop()     #移除列表中的一个元素（默认为最后一个元素，即index=-1），并且返回该元素的值。若循环过程中列表内已没元素可pop，则系统会报错IndexError: pop from empty list
        print("Adding: ", next_one)
        stuff.append(next_one)
        print(f"THere are {len(stuff)} items now.")
    
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])    # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # What? cool!
print('#'.join(stuff[3:5])) #super stellar!


#-------------------------------------------------------------------
print("\n-------------------------------------------------------------")
print("用for循环替换如上的while循环")
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
"Corn", "Banana", "Girl", "Boy"]    #可以在多行中给列表赋元素

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
print(stuff[-1])    # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # What? cool!
print('#'.join(stuff[3:5])) #super stellar!
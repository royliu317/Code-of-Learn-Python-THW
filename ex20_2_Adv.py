fo = open("ex20_sample.txt", "r+")
print ("File name: ", fo.name)

line = fo.readline()
print ("The date loaded: %s" %(line))

# rewind sets the pointer back to the beginning
fo.seek(0, 0)
line = fo.readline()
print (f"The date loaded: {line}") 

line = fo.readline()
print (f"The date loaded: {line}") 

fo.close()
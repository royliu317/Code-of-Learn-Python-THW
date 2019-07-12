# zip(): zip([iterable, ...])

a1 = [1,2,3]
b1 = [4,5,6]
c1 = [4,5,6,7,8]
zipped1 = zip(a1, b1)      
print(zipped1, type(zipped1))    
print(list(zipped1))      

zipped2 = zip(a1, c1)
print(list(zipped2))    

d1 = zip(*zip(a1, b1))  
print(list(d1))

e1, f1 = zip(*zip(a1,b1))
print(list(e1), list(f1))


print("-------------------------------------------------------------")
a = [1, 2, 3, 4]    # List type
b, c, d, e = a
print(b, c, d, e)

f = range(0, 2)     # range type
g, h = f
print(g, h)

m = {'Name': 'Runoob', 'Age': 7, 'Gender': 'Nv', 'Test': 34}    # Dict type
n, o, p, q = m
print(n, o, p, q)



print("-------------------------------------------------------------")
dict = {'Name': 'Runoob', 'Age': 7, 'Gender': 'Nv', 'Test': 34}

for i in dict:
	print(i)
#output: print key loop


for i in dict.keys():
	print(i)
#output: print key loop


for j in dict.values():
	print(j)
#output: print values loop


for i,j in dict.items():
	print(i, ":", j)
#output: print key:value loop


del dict['Name']    # Remove 'Name'
print(dict)
dict.clear()        # Clean up the content in the dictionary
print(dict)
del dict            # Delete the dictionary
print(dict)


print("-------------------------------------------------------------")
print("Use dict(**d1, **d2) to merge dicstionaries")
x = {'a':1, 'b':2}
y = {'c':3, 'd':4}
z = {'e':5, 'f':6}
mydict = {**x, **y, **z}
print(mydict)

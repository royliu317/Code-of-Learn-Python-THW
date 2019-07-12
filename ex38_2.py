jn1 = '-'
jn2 = '-----------'
mylist = ['a', 'b', 'c']
mystr = 'name'
myset = {'apple', 'banana', 'corn'}
mytup = ('amazon', 'google', 'microsoft')
mydic = {'key1':"jenny", 'key2':'juice', 'key3':'jump'}

print(jn1.join(mylist))
print(jn2.join(mylist)) 
print(jn1.join(mystr))  
print(jn2.join(mystr))
print(jn1.join(myset))
print(jn2.join(myset))
print(jn1.join(mytup))
print(jn2.join(mytup))
print(jn1.join(mydic))  
print(jn2.join(mydic))


# join(): str.join(sequence)
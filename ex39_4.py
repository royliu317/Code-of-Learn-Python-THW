import collections

print('Regular dictionary:')
d2={}
d2['a']='A'
d2['b']='B'
d2['c']='C'
  
d3={}
d3['c']='C'
d3['a']='A'
d3['b']='B'
 
print(d2, d3, d2 == d3)
 
print('\nOrderedDict:')
d4=collections.OrderedDict()
d4['a']='A'
d4['b']='B'
d4['c']='C'
 
d5=collections.OrderedDict()
d5['c']='C'
d5['a']='A'
d5['b']='B'

print(d4, d5, d4==d5)


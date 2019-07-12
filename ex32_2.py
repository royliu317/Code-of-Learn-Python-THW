# Difference between Assignment reference, copy and deepcopy

print("**For List type**")
import copy
list1 = [1, 2, 3, 4, ['a', 'b']] 
 
list2 = list1                 
list3 = list1.copy()          
# Above can be replaced as list3 = copy.copy(list1) or list3 = list1[:]   
list4 = copy.deepcopy(list1)  
 
list1.append(5)            
list1[4].append('c')       
 
print( 'list1 = ', list1)
print( 'list2 = ', list2)
print( 'list3 = ', list3)
print( 'list4 = ', list4)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("**For Dictionary type**")
import copy

dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          
dict3 = dict1.copy()   
dict4 = copy.deepcopy(dict1)

dict1['user']='root'
dict1['num'].remove(1)
 
print(dict1)
print(dict2)
print(dict3)
print(dict4)

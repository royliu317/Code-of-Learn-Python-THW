print("Get key from value:")
mydict = {'Name': 333 , 'Age': 666, 'Gender': 888, 'Test': 999}
a = list(mydict.values()).index(666)    
b = list(mydict.keys())[a]
print(b)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("Get maxium and its key:")
prices = {
    'A':123,
    'B':450.1,
    'C':12,
    'E':444,
}

a = list(zip(prices.values(), prices.keys()))
print(a)

max_prices = max(zip(prices.values(), prices.keys()))
print(max_prices)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("Exchange the key and value in the dictionary:")
dic = {
    'a': 1,
    'b': 2,
    'c': 3,
}

reverse = {v: k for k, v in dic.items()}
# Above equals to：
# for k, v in dic.items():
#     reverse = {v: k}

print(dic)
print(reverse)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("Use dictionary to record the name and score of students and then group by:")
students= {}
write = 1
while write :
    name = str(input('Name:'))
    grade = int(input('Score:'))
    students[name] = grade  
    write= int(input('Continue？\n 1/Yes  0/Exit'))
print('Name  Rate'.center(20,'-'))
for key,value in students.items():
    if value >= 90:
        print(f'{key} {value} A Level'.center(20,'-'))
    elif 89 > value >= 60 :
        print(f'{key} {value} B Level'.center(20,'-'))
    else:
        print(f'{key} {value} C Level'.center(20,'-'))
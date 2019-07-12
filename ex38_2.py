jn1 = '-'
jn2 = '-----------'
mylist = ['a', 'b', 'c']
mystr = 'name'
myset = {'apple', 'banana', 'corn'}
mytup = ('amazon', 'google', 'microsoft')
mydic = {'key1':"jenny", 'key2':'juice', 'key3':'jump'}

print(jn1.join(mylist))
print(jn2.join(mylist)) #使用多字符来连接序列
print(jn1.join(mystr))  #字符串也属于序列
print(jn2.join(mystr))
print(jn1.join(myset))
print(jn2.join(myset))
print(jn1.join(mytup))
print(jn2.join(mytup))
print(jn1.join(mydic))  #连接的序列是字典，会将所有key连接起来
print(jn2.join(mydic))


# join()方法函数 用于将序列中的元素以指定的字符连接生成一个新的字符串。
# str.join(sequence)方法函数 中的sequence必须是字符串str，否则会报错。
# 参数sequence：要连接的元素序列。
# 返回值：返回通过指定字符连接序列中元素后生成的新字符串str。

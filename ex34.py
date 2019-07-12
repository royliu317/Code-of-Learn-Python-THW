# List[start:end:step]
# start:起始索引。默认为0。
# end： 结束索引。默认为列表长度len(list)。
# step：步长。步长为正时，从左向右取值；步长为负时，从右向左取值。


# 内建函数reversed()
li =[1, 2, 3, 4, 5, 6]
a = list(reversed(li))
print (a)
#注意：reversed()函数返回的是一个迭代器，而不是一个List，所以需要list()函数转换一下


# 如果想创建一个占用十个元素空间，却不包括任何有用内容的列表，可以使用None
# None 是一个Python的内建值，它的确切含意是"这里什么也没有"。因此，如果想初始化个长度为10的列表，可以按照下面的例子来实现:
list_empty = [None]*10
print(list_empty)


hello = "This is a test."
print(hello.split())
# split()方法 通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
# str.split(str="", num=string.count(str))
# 参数str：分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。num：分割次数。
# 返回值：返回分割后的 字符串列表List 。
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
# OrderedDict是collections中的一个包，能够记录字典元素插入的顺序。常和排序函数sort等一起使用来生成一个排序的字典
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
# 补充：OrderedDict内部维护了一个双向链表，它会根据元素加入的顺序排列键的位置。第一个新加入的元素被放置在链表的末尾，之后对已存在的键做重新赋值不会改变键的顺序。
# 因此，OrderedDict的大小是普通字典的2倍，这是它额外创建的链表所致。所以在构建涉及大量数据的结构时要权衡其带来的好处与消耗的内存。

print("OrderedDict对象的字典对象，如果其顺序不同那么Python也会把他们当做是两个不同的对象：")
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



# 字典是Python语言中唯一的映射类型。
# 映射类型对象里哈希值（键，key）和指向的对象（值，value）是一对多的的关系，通常被认为是可变的哈希表。
# 字典对象是可变的，它是一个容器类型，能存储任意个数的Python对象，其中也可包括其他容器类型。

#字典类型与序列类型的区别：
# 1. 存取和访问数据的方式不同。
# 2. 序列类型只用数字类型的键（从序列的开始按数值顺序索引）；
# 3. 字典类型映射时可以用其他对象类型作键（如：数字、字符串、元祖，一般用字符串作键）
# 4. 和序列类型的键不同，映射类型的键直接或间接地和存储数据值相关联
# 5. 映射类型中的数据是无序排列的。这和序列类型是不一样的，序列类型是以数值序排列的。
# 6. 映射类型用键直接“映射”到值。
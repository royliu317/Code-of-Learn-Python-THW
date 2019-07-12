# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("NY State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cites dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
# 如上可以替换为：
# for state, abbrev in states.items():
# 实际上，用list(states.items())更慢，但有时为了测试排查目的，用list()可以让你更清楚的看到列表里面都有什么，而不是直接看一个dict_items()对象
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")



# python中del删除的是变量，而不是数据 https://weibo.com/ttarticle/p/show?id=2309404215256372118805
# mylist=[1,2,3,4,5]，列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]


# Python字典的 items() 方法以列表返回可遍历的(键, 值)元组数组。
# items()方法语法：dict.items()
# 参数: NA。
# 返回值: 返回可遍历的(键, 值) 元组数组。


# Python 字典 get() 函数返回指定键的值，如果值不在字典中则返回指定的默认值，如未指定默认值则返回None。
# get()方法语法：dict.get(key, default=None)
# 参数key：字典中要查找的键。default： 如果指定键的值不存在时，返回该指定的默认值，或返回None。
# 返回值：返回指定键的值，如果指定键的值不存在时，返回该指定的默认值，或返回None。


# 字典是支持无限极嵌套的。
# 字典列表，由列表组成的字典，即在列表中嵌套字典list[{dict1}, {dict2}, {dict3}]


# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
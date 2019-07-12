import random

print(random.random())               # 产生 0 到 1 之间的随机浮点数(包括0，不包括1)
print(random.randint(1, 10))         # 产生 1 到 10 之间的一个整数型随机数（包括1和10）  
print(random.uniform(1.1, 5.4))      # 产生 1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print(random.randrange(1, 100, 50))  # 生成 1 到 100 之间间隔为 50 的随机整数（结果只会为1或51）
print(random.choice('tomorrow'))     # 从序列中随机选取一个元素（字符串也是一个序列，它的每一个字符，其实就是序列中的一个元素/变量）
print(random.sample(range(100), 10)) # 从 0 到 100 之间随机选取10个整数，输出为一个列表list

a = [1,3,5,6,7]               
print(random.shuffle(a))             # 将序列a中的元素随机打乱



# 关于python帮助的用法：
# help('urllib')			        Help on package urllib
# help('urllib.request')		    Help on module urllib.request in urllib
# help('urllib.request.urlopen')	Help on function urlopen in urllib.request
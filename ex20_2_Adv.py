# 打开文件
fo = open("ex20_sample.txt", "r+")
print ("文件名为: ", fo.name)

line = fo.readline()
print ("读取的数据为: %s" %(line))

# 倒带，即将文件指针重新设置回开头
fo.seek(0, 0)
line = fo.readline()
print (f"读取的数据为: {line}") #打印第一行

line = fo.readline()
print (f"读取的数据为: {line}") #打印第二行

fo.close()
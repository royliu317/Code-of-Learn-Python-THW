from sys import argv

script, filename = argv #通过 argv 以命令行方式给filename赋值。filename可为文件完整路径，有无引号均可

print("filename:", repr(filename))

txt = open(filename)
print(">>>>", repr(filename)) #filename是储存文件路径的字符串
print(">>>>", repr(txt)) #txt是文件对象，python会将其识别为<_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='cp936'>

print(f"Here's your file {filename}:")
indata = txt.read()
print(indata, "\n>>>>", repr(indata))
txt.close() #关闭后的文件不能再进行读写操作，否则报错：ValueError: I/O operation on closed file.

print("Type the filename again:")
file_again = input("> ") #通过 input() 赋给filename的参数，可以包含文件完整路径，但必须不带引号

txt_again = open(file_again)

print(txt_again.read())
txt.close()

#在powershell中直接运行python命令，然后在提示符下一行一行输入如上命令，是不work的

print(txt) #print不是打印文件对象中的内容，而是打印文件对象的属性：<_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='cp936'>
print(txt_again) 


# fileObject.read(size)，#size：从文件中读取的字节数（int类型）；返回值：返回从字符串中读取的字节（str类型）。
#read()方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。

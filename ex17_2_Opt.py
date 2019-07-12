from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read() # fileObject.read(size) 从文件中读取字节数（int类型），返回读取的字节（str类型）。因此，indata为str类型。
#当如上命令替换为如下时，indata仍是文件对象类型，而非str，因为该命令只是指定了文件对象的打开模式为read模式而已。
#indata = open(from_file, 'r') 
#print(">>>>", repr(indata))


out_file = open(to_file, 'w').write(indata) # fileObject.write([str])，读取要写入的字符串（str类型），返回写入的字符长度(int类型)。因此，out_file为int类型。
#当如上命令替换为如下时，out_file的类型始终为文件对象类型，而非int。
#原因是out_file.write(indata)运行后，write函数的返回值（int）并没有返回给任何变量，即返回值未保存。
#注意：fileObject.write()命令运行时，write函数并不会转换fileObject本身的类型，所以如下命令中的out_file始终保持文件对象类型。
#out_file.write(indata)
#out_file = open(to_file, 'w')
#print(type(out_file))
#out_file.write(indata) 
#print(type(out_file)) 
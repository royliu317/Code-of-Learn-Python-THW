print("copy content from auto created ex23_sample_05.txt to ex23_sample_06.txt using 1 line only")
input('请在powershell中用 echo "This is a unicode Test." > ex23_sample_05.txt 自动创建一个文本文件。完成后请按回车')
#解码、编码方式都要设为utf-16，因为自动创建的文本默认为unicode的utf-16方式，而非手动创建文本时默认的ANSI(gbk)方式。
in_file = open('c:\\users\\roy\\lpthw\\ex23_sample_05.txt', encoding = 'utf-16').read()
out_file = open('c:\\users\\roy\\lpthw\\ex23_sample_06.txt', 'w', encoding = 'utf-16').write(in_file)
print("DONE!\n")

#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("copy content from languages.txt within ex23 to languages2.txt using 1 line only")
#解码、编码方式都要设为utf-8，因为languages.txt文件下载下来时，就是按这种方式保存的（除非手动修改为其他方式）。
in_file = open('c:\\users\\roy\\lpthw\\languages.txt', encoding = 'utf-8').read()
#When set encoding = utf-16 --> UnicodeDecodeError: 'utf-16-le' codec can't decode bytes in position 812-813: illegal UTF-16 surrogate，即编码时发现有的字节在该方式中是illegal的
#When set encoding = utf-16, errors = 'ignore' --> UnicodeError: UTF-16 stream does not start with BOM，即解码时发现文本中的字节不是以BOM开头进行编写的

out_file = open('c:\\users\\roy\\lpthw\\languages2.txt', 'w', encoding = 'utf-8').write(in_file)
# Before add encoding = utf-8 -->UnicodeEncodeError: 'gbk' codec can't encode character '\u0a73' in position 4: illegal multibyte sequence，即编码时发现有的字节在该方式中是illegal的
print("DONE!\n")



#复制一个文件的方式（源文件中的字节-->编码成字符串-->保存至变量-->变量中的字符串解码为字节-->保存到目的文件中）：
#1. 解码字节串：将源file内容（在计算机中是以字节bytes形式存在的，而非字符str）以utf-8方式解码为字符，并通过read()将字符串传给in_file变量
#2. 编码字符串：将in_file字符串以同样的utf-8方式编码为字节，并写入目的file中。

#encoding参数不要按字面意思，仅仅理解为“编码”之意，因为：
#open()中的encoding参数，同时有“编码”、“解码”之意。只是中文翻译统称为“编码格式”！
#str.decode()中的encoding参数，则为“解码”之意！

#对于源文件，解码方式必须为其所保存的方式，否则无法解码出字符串
#对于目的文件，编码方式应与解码方式一致，否则有可能部分字节无法解码或解码为错误字符（因为不同方式，bytes与str的对应关系不尽相同）。虽然对于常见字符来说可能不会报错，也可以解码为正确字符串，但扔不推荐。

#该中文操作系统的默认解码、编码方式为gbk（ANSI），而非unicode或UTF-xx（可以理解为打开、存储文本的方式默认为gbk）
#计算机内存的默认方式为unicode，但这并不是打开、存储文本的方式

#bytes can only contain ASCII literal characters.
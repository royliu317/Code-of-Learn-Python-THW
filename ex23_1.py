import sys
script, encoding_type, error_type = sys.argv 
#手动传给encoding的参数为"utf-8"，传给error的参数可为"strict"。它们用于在print_line()函数中为encode(), decode()指定编/解码类型、错误类型这两个参数。

def main(my_languages):
    line = my_languages.readline() #文件对象languages_fileObject会记录每次调用readline()后的读取位置，这样它就可以在下次被调用时读取接下来的一行了(即文件指针的变化会保存下来，即便它是在函数之内变化的)

    if line: #如果readline不返回空字符串，则为真
        print_line(line, encoding_type, error_type)
        return main(my_languages) #在main()函数中调用自己，形成循环，但通过if判断防止形成死循环（因为readline不会在到达文末时自动停止，它会持续输出空行）


def print_line(my_line, my_encoding_type, my_error_type):
    next_lang = my_line.strip() #把每行结尾的\n删掉而已，因为readline()所取的每行字符串也会包括行尾的\n (打印每行时会自动换行，没必要再多保留一个换行符)
    raw_bytes = next_lang.encode(encoding = my_encoding_type, errors = my_error_type) 
    cooked_string = raw_bytes.decode(my_encoding_type, my_error_type)

    print(raw_bytes, "<===>", cooked_string) #如下为用b''字节串取代UTF-8字符串反写代码的方式：
    #print(raw_bytes, b'\x22\x3C\x3D\x3D\x3D\x3E\x22'.decode().strip('"'), cooked_string)

languages_fileObject = open("languages.txt", encoding = "utf-8") #如下为用b''字节串取代UTF-8字符串反写代码的方式：
#languages_fileObject = open(b'\x22\x6C\x61\x6E\x67\x75\x61\x67\x65\x73\x2E\x74\x78\x74\x22'.decode().strip('"'), encoding = b'\x22\x75\x74\x66\x2D\x38\x22'.decode().strip('"'))
main(languages_fileObject)



#strip()方法语法：str.strip([chars])
#参数chars: 移除字符串头尾指定的字符序列。
#返回值: 返回移除字符串头尾指定的字符序列生成的新字符串。
#strip()如果不带参数，默认是清除两边的空白符，例如：/n, /r, /t, ' '等。

#encode()方法语法：str.encode(encoding='UTF-8', errors='strict')
#参数encoding：要使用的编码，如:UTF-8。errors：设置不同错误的处理方案，默认为'strict',意为编码错误引起一个UnicodeError，其他可能的值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
#返回值：该方法返回编码后的字节串(bytes)。

#decode()方法语法：bytes.decode(encoding="utf-8", errors="strict")
#参数encoding：要使用的编码，如:UTF-8。errors：设置不同错误的处理方案，默认为'strict',意为编码错误引起一个UnicodeError，其他可能的值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
#返回值: 该方法返回解码后的字符串(str)。

#当设置不适合的encoding方式时，系统会报错。但如果设置 errors = replace ，则系统不会再报错，而是把有错的地方替换为 ？
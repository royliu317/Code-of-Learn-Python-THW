#字符串编码
utf_string = "文言"
print(utf_string.encode(), type(utf_string), len(utf_string))  # str.encode(encoding="xxx", errors="xxx")

#字节串解码
raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80' # 用 b'...' 表示字节串类型(bytes)
print(raw_bytes.decode(), type(raw_bytes), len(raw_bytes)) # bytes.decode(encoding="xxx", errors="xxx")


raw_bytes = b'ABC' #赋值后的ABC对象为字节串类型，而非字符串类型
print(raw_bytes, raw_bytes.decode(encoding = 'utf-8'), type(raw_bytes), len(raw_bytes))
#When set raw_bytes = b'文言' --> SyntaxError: bytes can only contain ASCII literal characters.
#When set encoding = 'utf-16' --> UnicodeDecodeError: 'utf-16-le' codec can't decode byte 0x43 in position 2: truncated data (注: 0x43对应字母C)


print("Is raw_bytes == utf_string.encode() true? ", raw_bytes == utf_string.encode())
print("Is utf_string == raw_bytes.decode() true? ", utf_string == raw_bytes.decode())




#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print(chr(90))
print(ord('Z'))
print(0b1011010, 0o001, 0x00f) #进制转换：从2、8、16位进制数转为10位
print("\x0f") #字符转换：将十六进制值hh转换为对应字符


# chr(i)用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
# 参数i：可以是10进制也可以是16进制形式的数字。
# 返回值是当前整数对应的ascii字符。

# ord(c)函数是chr()函数（对于8位的ASCII字符串）的配对函数
# 它以1个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常。
# 参数c: 1个字符。
# 返回值: 返回值是对应的十进制整数。

#python:字符串转换成字节的三种方式
# str='zifuchuang'
# 第一种 b'zifuchuang'
# 第二种bytes('zifuchuang',encoding='utf-8')
# 第三种('zifuchuang').encode('utf-8')
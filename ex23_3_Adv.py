# string encode
utf_string = "文言"
print(utf_string.encode(), type(utf_string), len(utf_string))  # str.encode(encoding="xxx", errors="xxx")

# string decode
raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80' 
print(raw_bytes.decode(), type(raw_bytes), len(raw_bytes)) # bytes.decode(encoding="xxx", errors="xxx")


raw_bytes = b'ABC' 
print(raw_bytes, raw_bytes.decode(encoding = 'utf-8'), type(raw_bytes), len(raw_bytes))
#When set raw_bytes = b'文言' --> SyntaxError: bytes can only contain ASCII literal characters.
#When set encoding = 'utf-16' --> UnicodeDecodeError: 'utf-16-le' codec can't decode byte 0x43 in position 2: truncated data (0x43 <--> C)


print("Is raw_bytes == utf_string.encode() true? ", raw_bytes == utf_string.encode())
print("Is utf_string == raw_bytes.decode() true? ", utf_string == raw_bytes.decode())




#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print(chr(90))
print(ord('Z'))
print(0b1011010, 0o001, 0x00f) 
print("\x0f") 

#Three methos to transfer string to bytes in Python:
# str='zifuchuang'
# 1. b'zifuchuang'
# 2. bytes('zifuchuang',encoding='utf-8')
# 3. ('zifuchuang').encode('utf-8')
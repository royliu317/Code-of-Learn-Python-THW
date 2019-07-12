import sys
script, encoding_type, error_type = sys.argv 


def main(my_languages):
    line = my_languages.readline() 

    if line: 
        print_line(line, encoding_type, error_type)
        return main(my_languages) 


def print_line(my_line, my_encoding_type, my_error_type):
    next_lang = my_line.strip()                             #Strip the \n of each line since readline() also store the \n of each line
    raw_bytes = next_lang.encode(encoding = my_encoding_type, errors = my_error_type) 
    cooked_string = raw_bytes.decode(my_encoding_type, my_error_type)

    print(raw_bytes, "<===>", cooked_string)
    # Below is how to use b'' to replace UTF-8 string for reversing the code：                
    #print(raw_bytes, b'\x22\x3C\x3D\x3D\x3D\x3E\x22'.decode().strip('"'), cooked_string)

languages_fileObject = open("languages.txt", encoding = "utf-8") 
# Below is how to use b'' to replace UTF-8 string for reversing the code：    
# languages_fileObject = open(b'\x22\x6C\x61\x6E\x67\x75\x61\x67\x65\x73\x2E\x74\x78\x74\x22'.decode().strip('"'), encoding = b'\x22\x75\x74\x66\x2D\x38\x22'.decode().strip('"'))
main(languages_fileObject)



#strip(): str.strip([chars])
#encode()：str.encode(encoding='UTF-8', errors='strict')
#decode()：bytes.decode(encoding="utf-8", errors="strict")

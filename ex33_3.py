print("之前讲过的形成循环的方式，详见ex23_1.py")
import sys
script, encoding_type, error_type = sys.argv 

def main(my_languages):
    line = my_languages.readline()

    if line: #如果readline不返回空字符串，则为真
        print(line)
        return main(my_languages) #递归(recursion)，即在main()函数中再调用main()函数，从而形成循环。假如if判断，防止形成死循环（因为没有if的话，readline不会在到达文末时自动停止，它会持续输出空行）

languages_fileObject = open("languages.txt", encoding = "utf-8") #如下为用b''字节串取代UTF-8字符串反写代码的方式：
#languages_fileObject = open(b'\x22\x6C\x61\x6E\x67\x75\x61\x67\x65\x73\x2E\x74\x78\x74\x22'.decode().strip('"'), encoding = b'\x22\x75\x74\x66\x2D\x38\x22'.decode().strip('"'))
main(languages_fileObject)


# 递归(recursion)即便造成了死循环，由于它是有边界条件（bounded）的，所以过多/过深的递归会被系统终止并报错 RecursionError: maximum recursion depth exceeded
# 然而，while所造成的死循环，是无边界条件的(unbounded)，因此循环会持续进行，直到内存溢出
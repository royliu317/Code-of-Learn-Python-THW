import sys
script, encoding_type, error_type = sys.argv 

def main(my_languages):
    line = my_languages.readline()

    if line:
        print(line)
        return main(my_languages) # recursion

languages_fileObject = open("languages.txt", encoding = "utf-8")
main(languages_fileObject)

# Even if recursion causes endless loop, since it is bounded，so it will terminate and raises RecursionError: maximum recursion depth exceeded
# However，while is unbounded, so its endless loop won't terminate until it causes out of memory.
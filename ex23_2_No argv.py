def main(my_languages):
    line = my_languages.readline()

    if line:
        print_line(line, my_encoding_type = "utf-8", my_error_type = "strict")
        return main(my_languages)


def print_line(my_line, my_encoding_type, my_error_type):
    next_lang = my_line.strip()
    raw_bytes = next_lang.encode(encoding = my_encoding_type, errors = my_error_type) # Keywords parameter
    cooked_string = raw_bytes.decode(my_encoding_type, my_error_type) 

    print(raw_bytes, "<===>", cooked_string)

languages_fileObject = open("languages.txt", encoding = "utf-8")
main(languages_fileObject)
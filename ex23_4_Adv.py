print("copy content from auto created ex23_sample_05.txt to ex23_sample_06.txt using 1 line only")
input('In powershell: echo "This is a unicode Test." > ex23_sample_05.txt ')

in_file = open('c:\\users\\roy\\ex23_sample_05.txt', encoding = 'utf-16').read()
out_file = open('c:\\users\\roy\\ex23_sample_06.txt', 'w', encoding = 'utf-16').write(in_file)
print("DONE!\n")

#-------------------------------------------------------------------
print("-------------------------------------------------------------")
print("copy content from languages.txt within ex23 to languages2.txt using 1 line only")

in_file = open('c:\\users\\roy\\languages.txt', encoding = 'utf-8').read()
# When set encoding = utf-16 --> UnicodeDecodeError: 'utf-16-le' codec can't decode bytes in position 812-813: illegal UTF-16 surrogate
# When set encoding = utf-16, errors = 'ignore' --> UnicodeError: UTF-16 stream does not start with BOM

out_file = open('c:\\users\\roy\\languages2.txt', 'w', encoding = 'utf-8').write(in_file)
# Before add encoding = utf-8 -->UnicodeEncodeError: 'gbk' codec can't encode character '\u0a73' in position 4: illegal multibyte sequence
print("DONE!\n")


# bytes can only contain ASCII literal characters.
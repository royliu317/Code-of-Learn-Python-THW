print("copy content from ex17_sample_01.txt to ex17_sample_02.txt using 1 line only")
out_file = open('c:\\users\\roy\\lpthw\\ex17_sample_02.txt', 'w').write(open('c:\\users\\roy\\lpthw\\ex17_sample_01.txt').read())
#fileObject.read() --> str --> fileObject.write([str])
print("DONE!\n")
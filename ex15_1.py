from sys import argv

script, filename = argv 

print("filename:", repr(filename))

txt = open(filename)
print(">>>>", repr(filename)) 
print(">>>>", repr(txt))                # txt is file object, and python recognizes it as <_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='cp936'>

print(f"Here's your file {filename}:")
indata = txt.read()
print(indata, "\n>>>>", repr(indata))
txt.close()                             # After the file is closed it cannot be used to read/write, or it will raise ValueError: I/O operation on closed file.

print("Type the filename again:")
file_again = input("> ") 

txt_again = open(file_again)

print(txt_again.read())
txt.close()


print(txt)                              # Print the attribute of file object：<_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='cp936'>
print(txt_again) 



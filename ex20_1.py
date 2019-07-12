from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)   

def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) #文件对象f会记录每次调用readline()后的读取位置，这样它就可以在下次被调用时读取接下来的一行了。

current_line += 1
print_a_line(current_line, current_file) 

current_line += 1
print_a_line(current_line, current_file)
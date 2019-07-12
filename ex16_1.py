from sys import argv

script, filename =  argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r+') 

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.") 
target.write(f"""{line1}
{line2}
{line3}
""")
# Above can be replaced as: target.write(f"{line1}\n{line2}\n{line3}\n") 
# Or replaced as: target.write("{}\n{}\n{}\n".format(line1, line2, line3))
# Can NOT be replaced as: print("I'm going to write these to the file.", target.write(line1), target.write("\n"), target.write(line2), target.write("\n"), target.write(line3), target.write("\n"))


print("And finally, we close it.")
target.close()

print("\nThen we open it again and see what the latest content is.")
target_again = open(filename)   # read() should not run between write() and close() since it may leads the mess up of file's content.
print(target_again.read())
target_again.close()

# Before the file is closed or the buffer is flushed, the content stores in the buffer and you cannot see it in the file at that time.
# If file open mode includes b, then str parameter needs to use encode to transfer to bytes when writing into the file, otherwise, it will raise TypeError: a bytes-like object is required, not 'str'
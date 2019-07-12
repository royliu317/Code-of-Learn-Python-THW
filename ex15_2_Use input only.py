filename = input("> Please enter filename:") 

txt = open(filename, encoding = "utf-8")

print(">>>>filename: ", repr(filename))

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#在powershell中直接运行python命令，然后在提示符下一行一行输入如上命令，是可以work的


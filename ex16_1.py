from sys import argv

script, filename =  argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r+') #运行 r+ 时不删除文件原内容，新内容从头开始写入，覆盖同行内容。运行 w+ 时删除文件原内容（无论是否真的写入新内容）

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.") 
target.write(f"""{line1}
{line2}
{line3}
""")
#或替换为: target.write(f"{line1}\n{line2}\n{line3}\n") 
#或替换为: target.write("{}\n{}\n{}\n".format(line1, line2, line3))
#不能替换为: print("I'm going to write these to the file.", target.write(line1), target.write("\n"), target.write(line2), target.write("\n"), target.write(line3), target.write("\n"))
#因为会连同6个文件对象一起打印出来，因为write()返回值为int类型，是输入的str的字符个数。如line1为abc，则返回值为3。

print("And finally, we close it.")
target.close()

print("\nThen we open it again and see what the latest content is.")
target_again = open(filename) #不应在write()与close()之间再运行read()，因为很可能导致文件中的内容错乱。所以，若要读更新后的内容，应在文件close()之后
print(target_again.read())
target_again.close()

#用如上命令对文件进行操作的前提，是要确保该文件是关闭的，否则运行后可能会导致文件中的内容错乱

#fileObject.write([str]) ，参数str：要写入文件的字符串，即输入为字符串; 返回值：返回的是写入的字符长度，即返回值为int
#在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
#如果文件打开模式带b，那写入文件内容时，str(参数)要用encode方法转为bytes形式，否则报错 TypeError: a bytes-like object is required, not 'str'
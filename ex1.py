print("Hello World!") #语句运行后，默认自动换1行
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.') #单引号、双引号可混用，作用相同
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

#-------------------------------------------------------------------
print("-----------------------------------------------------------")
print() #运行结果是自动换1行
print(9)
print('\n' *2, end='8') #end''用来设定print命令如何结尾，因为默认值是换行符\n，所以语句运行后才会自动换1行。但如果设为其他字符，则会取消自动换行，并显示此字符
print('7') #因为上一命令取消了自动换行，所以本行的结果7会直接显示在8之后
print("\n") #运行结果是换2行：\n的默认值为换1行，语句运行后自动再换1行
print('1' *3)

print('\n' *2) #运行结果是换3行：先输出两次换行符即换2行，语句运行后自动再换1行
print(1*2*3)

print("\n" *0) #运行结果是换1行：\n设为运行0次即不换行，end默认换1行
print(5)

print('\n', end='') #运行结果是换1行：\n会换1行，end设为null时取消自动换行
s="It's me again"
print(s)

print('abc', end='') #end设为null时，取消自动换行，下一行结果会在该行结果之后继续显示
print('def')

for i in range(0,6):
    print(i)

for i in range(0,6):
    print(i, end='') #end设为null时，取消自动换行，下一行的内容会在该行中继续显示

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\"Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\"" #转义字符backslash出现后，系统就知道要处理特殊字符了
#因此 \ 后的一个字符，要么是用来输出特殊字符如 \" 双引号，要么是用来处理特殊要求如 \n 换行，此外它还可用来转义Unicode

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""") #用3个连续的双引号，可以打印长文本，包括回车、单双引号、空格等，都会原封不动的打印出来。打印结果会自动换2行（默认换1行，使用该方式会再换1行）

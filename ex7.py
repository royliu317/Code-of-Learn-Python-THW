print("Mary had a little lamb.")
print("Its fleece was while as {}.".format('snow')) #不用 f"{}"，变为用{}结合.format()，同样可以创建嵌入变量内容的字符串。另外，format()中不止可以用变量
print("And everywhere that Mary went.")
print("." *10) #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. Try removing it to see what happens
print(end1 + end2 + end3 +end4 +end5 +end6, end=' ')  #end=' '是设定print命令如何结尾，默认是换行符\n。此处设为空格，则取消换行，并输出空格
print(end7 + end8 + end9 + end10 + end11 + end12)


#-------------------------------------------------------------------
print("-------------------------------------------------------------")
#Same result as above after changed Line2
print(f"Its fleece was while as {'snow'}.")
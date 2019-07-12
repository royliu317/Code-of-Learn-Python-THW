tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line." #转义字符跟后面内容间不要有空格，否则打印时会多出该空格
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
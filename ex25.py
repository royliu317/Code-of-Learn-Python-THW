def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)



def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    

# sentence = input("Please input a sentence:")
# print_first_and_last(sentence)
# print_first_and_last_sorted(sentence)


# str.split(str="", num=string.count(str))
# 参数str: 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。num: 分割次数。
# 返回值: 返回分割后的字符串列表(list)。

# sorted(iterable, key=None, reverse=False)
# 参数iterable：可迭代对象。key：主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。reverse：排序规则，reverse = True 降序，reverse = False 升序（默认）。
# 返回值：返回重新排序的列表。
# sort 与 sorted 区别：sort 是应用在list上的方法，sorted 可对所有可迭代的对象进行排序操作。 list的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的list，而不是在原来的基础上进行的操作。

# list.pop([index=-1])
# 参数obj：可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
# 返回值：该方法返回从列表中移除的元素对象。
# list.pop([i])	
# 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
# 该方法中 i 两边的 方括号[] 表示这个参数是 可选的，而不是要求你输入一对方括号，你会经常在Python库参考手册中遇到这样的标记。
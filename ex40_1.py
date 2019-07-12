class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# Python中下划线的5种含义:
# https://zhuanlan.zhihu.com/p/36173202
# name mangling 名称修饰: 双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。即解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。
# 如果一个名字同时以双下划线开始和结束，则不会应用名称修饰。由双下划线前缀和后缀包围的变量不会被Python解释器修改。
# 但是，Python保留了有双前导和双末尾下划线的名称，用于特殊用途。 这样的例子有，__init__对象构造函数，或__call__它使得一个对象可以被调用。
# 单个下划线前缀的含义是告知其他程序员：以单个下划线开头的变量或方法仅供内部使用(但与如上不同，Python解释器对它是"无感"的)。


# Python3.5——模块定义、导入、优化详解
# https://blog.csdn.net/loveliuzz/article/details/78104349
# 模块是可以导入其他模块的。在一个模块（或者脚本，或者其他地方）的最前面使用 import 来导入一个模块，当然这只是一个惯例，而不是强制的。
# python脚本是通过 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
# 为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。


# 包package 是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
# 就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
# 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。

# 注：如下关于__init__.py的说明与用法，仅适用于Python2。对于Python3，即便没有该文件，也仍可以import，不过这毕竟是”项目骨架“，而且你可能会在该文件中写入代码，所以仍建议保留该文件。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
# 包package的定义：本质就是一个目录（文件夹），必须带有一个__init__.py文件，用来从逻辑上组织模块的。
# 包的导入其本质是：解释这个包下面的__init__.py文件。
# http://www.runoob.com/python3/python3-module.html


# 深入理解Python中的 __new__ 和 __init__
# https://blog.csdn.net/luoweifu/article/details/82732313
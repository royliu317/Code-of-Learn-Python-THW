# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问。



# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。局部变量只能在其 被声明的函数内部 访问，而全局变量可以在整个程序范围内访问。
# 对于变量作用域，变量的访问以 L（Local） –> E（Enclosing） –> G（Global） –>B（Built-in） 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，最后去内建中找。
x1 = int(1)  # 内建作用域
x2 = 2  # 全局作用域
def outer():
    x3 = 3  # 闭包函数外的函数中
    def inner():
        x4 = 4  # 局部作用域
        print(x1, x2, x3, x4)
    inner()
outer()



# 当内部作用域想 修改 外部作用域的变量时，就要用到global和nonlocal关键字了。但nonlocal只能修改外层函数的变量，而不能修改外层函数所引用的全局变量。
numbers = []
i = 0
def mywhile(j):
    global i
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)    
        i += 1    
        # 在函数内部修改变量i时，若不用global，则会报UnboundLocalError: local variable 'a' referenced before assignment
        # 即局部作用域引用错误，因为要修改的变量i未在函数内定义，且未声明要引用函数外的全局变量i
        # 但是，在函数内对外部作用域的List进行修改时，无需global声明
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

mywhile(3)
print("The numbers: ")
for num in numbers:
    print(num)

print(f"Now i is: {i}\nNow numbers is: {numbers}")
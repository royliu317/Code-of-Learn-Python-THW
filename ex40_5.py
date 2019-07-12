print("装饰起的简单应用：统计函数运行时间的装饰器")
import time

def deco(func):         # 装饰器函数    
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco         # @deco的本质就是 "func = deco(func)"。在Python中，可以使用"@"语法糖来精简装饰器的代码
def func():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':      # 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
    f = func    #这里f被赋值为func，执行f()就是执行func()
    f(3,4)      #func()
# 这里的deco函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数。其中作为参数的这个函数func()就在返回函数wrapper()的内部执行。
# 然后在函数func()前面加上@deco，func()函数就相当于被注入了计时功能，现在只要调用func()，它就已经变身为“新的功能更多”的函数了。



# python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。 
# 装饰器本质上是一个python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
# 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限验证等场景，装饰器是解决这类问题的绝佳设计。
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

# 装饰器：
#（1）本质：装饰器的本质是函数，其基本语法都是用关键字def去定义的。
#（2）功能：装饰其他函数，即：为其他函数添加附加功能。
#（3）原则：不能修改被装饰的函数的源代码，不能修改被装饰的函数的调用方式。即：装饰器对待被修饰的函数是完全透明的。

# __name__属性：1个模块被另1个程序第1次引入时，其主程序将运行。若想在模块被引入时，其内的某一程序块不执行，可用它来使该程序块仅在该模块自身运行时执行。
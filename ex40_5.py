print("decorator of counting the function's runtime")
import time

def deco(func):         
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco                        # Syntactic Sugar @deco means "func = deco(func)"
def func():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':      
    f = func  
    f(3,4)    

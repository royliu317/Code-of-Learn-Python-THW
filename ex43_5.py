class abc(object):

    scene_name = '111'          # 类属性，类似于全局变量，可以被实例共享的属性

    def __init__(self):         
        self.start_scene_name = '222'   # 实例属性1，各个实例独立拥有，不共享，在实例化对象时即创建该实例属性

    def next_scene(self):
        self.next_scene_name = '333'    # 实例属性2，各个实例独立拥有，不共享，在实例化对象时不创建，在调用该函数时才创建/添加该实例属性
        print(self.next_scene_name)

    def opening_scene(self):
        scene_name = '444'
        self.scene_name = '555'
        print(scene_name)
        print(self.scene_name)
        print(abc.scene_name)
        print(self.start_scene_name)
    #   print(self.next_scene_name)
                

a = abc()
print(abc.__dict__)                  # __dict__属性，类输出的是类函数、类变量等信息
print()
print(a.__dict__)                    # __dict__属性，实例输出的只是该实例自己拥有的变量、函数等信息    
print('\n')

a.next_scene()
print(abc.__dict__)
print()
print(a.__dict__)                    # 在调用next_scene()函数后，实例a新增了一个实例属性（next_scene_name）
print('\n')

a.opening_scene()                
print()

print(a.scene_name, abc.scene_name)  # 类属性可以通过 类.类属性 或 实例.类属性 访问
print()

print(a.start_scene_name)            # 实例属性只能通过 实例.实例属性 访问，不能通过 类.实例属性 访问  
print(a.next_scene_name)
##print(abc.start_scene_name)
##print(abc.next_scene_name)



# Python学习笔记 —— 类属性和实例属性的区别: https://blog.csdn.net/Leo_Coding/article/details/72935271
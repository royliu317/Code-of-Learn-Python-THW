class abc(object):

    scene_name = '111'          

    def __init__(self):         
        self.start_scene_name = '222'

    def next_scene(self):
        self.next_scene_name = '333' 
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
print(abc.__dict__)                  
print()
print(a.__dict__)                    
print('\n')

a.next_scene()
print(abc.__dict__)
print()
print(a.__dict__)                    
print('\n')

a.opening_scene()                
print()

print(a.scene_name, abc.scene_name)  
print()

print(a.start_scene_name)            
print(a.next_scene_name)
##print(abc.start_scene_name)
##print(abc.next_scene_name)

from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):     
                        
    def enter(self):
        print("This scene is not yet configured.Subclass it and implement enter().")
        exit(1)         


class Engine(object):
    
    def play(self):
        current_scene = Map.instantiate_scene('central_corridor')
        next_scene_code = None

        while next_scene_code != 'finished':                 
            next_scene_code = current_scene.enter()                   # 进入初始场景开始进行游戏，并根据该场景的游戏结果，告诉引擎下一步应该到哪个场景
            current_scene = Map.instantiate_scene(next_scene_code)    # 因为地图负责维护完整场景，所以引擎通过地图得到下一场景实例后，通过调用场景实例的enter()方法，进入下一场景继续游戏
            
        current_scene.enter()       # 当while为假（即到达了finished场景）时，进入finished场景，完成整个游戏


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
              You are the last surviving member and your last mission is to get the neutron destruct bomo from the Weapons Armory,
              put it in the bridge, and blow the ship up afer getting into an escape pod.

              You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, 
              and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.

              So what will you do now, shoot, dodge or tell a joke???
              """))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire it at the Gothen.
                  His clown costume is flowing and moving around his body, which throws off your aim.
                  Your laser hits his costume but missed him entirely.
                  This completely ruin s his brand new costume his mother bought him, 
                  which makes him fly into an insane rage and blast you repeatedly in the face until you are dead.
                  Then he eats you.
                  """))
            return 'death'
    
        elif action == "dodge":
            print(dedent("""
                  Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head.
                  In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out.
                  You wake up shortly after only to die as the Gothon stomps on your head and eats you.
                  """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                  Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know:
                  asdf  lasdfjlasfj l;ajsdfl jas;fljasfljs fljasdf asdfasdf.
                  The Gothon stops, tries not to laugh, then busts out laughing and can't move.
                  While he's laughing you run up and shoot him square in the head putting him down, then jump though the Weapon Armory door.
                  """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding.
              It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container.
              There's a keypad lock on the box and you need the code to get the bomb out.
              If you get the code wrong 3 times then the lock closes forever and you can't get the bomb.
              The code is 2 digits.
              """))
        
        code = f"{randint(1, 2)}{randint(1, 2)}"
        print('code= ', code)
        guess = input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 3:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                  The container clicks open and the seal breaks, letting gas out.
                  You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.
                  """))
            return 'the_bridge'
        else:
            print(dedent("""
                  The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. 
                  You decide to sit there, and finally the Gothons blow up the ship from their ship and you die
                  """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              You burst onto the Bridge with the netron destruct bomo under your arm and surprise 5 Gothons who are trying to take control of the ship.
              Each of them has an even uglier clown costume than the last. 
              They have't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off.

              So what will you do now, throw the bomb or slowly place the bomb?
              """))

        action = input("> ")

        if action == 'throw the bomb':
            print(dedent("""
                  In a panic you throw the bomb at the group of Gothons and make a leap for the door.
                  Right as you drop it a Gothon shoots you right in the back killing you.
                  As you die you see another Gothon frantically try to disarm the bomb.
                  You die knowing they will probably blow up when it goes off.
                  """))
            return 'death'
        
        elif action == 'slowly place the bomb':
            print(dedent("""
                  You point your blaster at the bomb under your arm and the Gothons put their hands up and star to sweat.
                  You in ch backward to the door, open it, and then carefully place the bomb on the floor, pointint your blaster at it.
                  You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out.
                  Now that the bomb is placed you run to the escape pod to get off this tin can.
                  """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'
       

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
              You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes.
              It seems like hardly any Gothons are on the ship, so your run is clear of interference.
              You get to the chamber with the escape pods, and now need to pick one to take.
              Some of them could be damaged but you don't have time to look.
              There's 2 pods, which one do you take?
              """))

        good_pod = randint(1, 2)
        print('good_pod= ', good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                  You jump into pod {guess} and hit the eject button.
                  The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.
                  """))
            return 'death'
        else:
            print(dedent("""
                  You jump into pod {guess} and hit the eject button.
                  The pod easily slides out into space heading to the planet below.
                  As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time.
                  You won!
                  """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You are the MAN! Good job.")
        return 'finished'


class Map(object):

    scenes = {                                                 # Map类维护的完整场景地图字典
        'central_corridor'      : CentralCorridor(),
        'laser_weapon_armory'   : LaserWeaponArmory(),
        'the_bridge'            : TheBridge(),
        'escape_pod'            : EscapePod(),
        'death'                 : Death(),
        'finished'              : Finished()
    }

    def instantiate_scene(scene_code):            # 未给该函数设置要传入self参数。因为在Python3中，不使用一个实例而调用一个方法没有问题，只要这个方法不期待一个实例，
        scene_object = Map.scenes.get(scene_code) # 并且你是通过类而非实例调用该方法（Python3中已经删除了无绑定方法的概念）。对于本例，因为并不需要实例化Map类，所以可用此方式定义该方法，
        return scene_object                       # 但本例中的其他方法不能这样写，因为它们都是需要通过实例对象进行调用的。
        

newgame = Engine()         
newgame.play()                  


# 类中的无绑定方法：https://images2018.cnblogs.com/blog/729758/201808/729758-20180809225746400-246028345.png
# Python类方法、静态方法与实例方法: https://www.cnblogs.com/blackmatrix/p/5606364.html 

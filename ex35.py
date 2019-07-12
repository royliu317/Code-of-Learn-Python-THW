from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    try:
        choice = int(input("> "))
    except:
        dead("Man, learn to type a number.")
    
    if choice < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("So how are you going to move the bear, take honey or taunt bear?")
    while True:   #此处表示循环会永远执行（因为判定条件永远为True），以确保最终能得到正确的回答。相应地，它的代码块及代码块中所调用的函数，其结尾必须用 exit(0)，否则该程序/循环永远不会终止。
        choice_1 = input("> ")
        if choice_1 == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice_1 == "taunt bear":
            print("The bear has moved from the door.")
            print("You can go throught it now. So waht do you want to do now, open door or taunt bear once again?")
            while True:   #此处继续用永久循环，以确保第二个问题也能最终得到正确的回答。
                choice_2 = input("> ")
                if choice_2 == "open door":
                    gold_room()
                elif choice_2 =="taunt bear":
                    dead("The bears gets pissed off and chews your leg off.")
                else:
                    print("I got no idea what that means, again!.")
        else:
            print("I got no idea what that means.")

    



def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
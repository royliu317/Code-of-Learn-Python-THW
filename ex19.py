def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("1. We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("2. OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("3. We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("4. And we can combine the two, variables and math:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("5. We can use input function to enter the amount")
amount_of_cheese = int(input("Please input the amount_of_cheese:"))
amount_of_crackers = int(input("Please input the amount_of_crackers:"))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("6. And We can combine to one line via keyword arguments")            # Keywords parameters, the sequence it passes in can be different compares with the ones defined in the function
cheese_and_crackers(cheese_count = float(input("Please input the amount_of_cheese:")), boxes_of_crackers = float(input("Please input the amount_of_crackers:")))

print("7. Or We can combine to one line via default arguments(默认参数)")   # # Keywords parameters, t the sequence it passes in must be the same compares with the ones defined in the function
cheese_and_crackers(int(input("Please input the amount_of_cheese:")), int(input("Please input the amount_of_crackers:")))

print("8. We can use argv to input the amount")
from sys import argv
script, amount_of_cheese, amount_of_crackers = argv
cheese_and_crackers(int(amount_of_cheese) + 5, int(amount_of_crackers) + 7)
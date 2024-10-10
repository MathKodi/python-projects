print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction = input('Type "left" or "right"\n').lower()
if direction == "left":
    print("You're come to a lake. There is an island in the middle of the lake.")
    direction = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if direction == "wait":
        print("You arrive at the island. There is a house with 3 doors\n One red, one yellow and one blue. Which color do you choose?")
        direction = input('Type "yellow", "red","blue"\n').lower()
        if direction == "yellow":
           print("You found the treasure!!! You Win =) ")
        elif direction == "blue":
            print("The room has nothing and you can't go back. Game Over")
        elif direction == "red":
            print("The room starts to get fire and you die. Game Over")
    else:
        print("You don't know how to swim... Game over.")
else:
    print("You fell into a hole. Game Over.")
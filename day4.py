import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock | 1 for Paper | 2 for Scissors\n"))
print(game[choice])
computerChoice = random.randint(0, 2)
print("Computer Chose:")
print(game[computerChoice])
if choice == computerChoice:
    print("It's a draw.")
elif choice == 0 and computerChoice == 2:
    print("You win.")
elif choice == 1 and computerChoice == 0:
    print("You win.")
elif choice == 2 and computerChoice == 1:
    print("You win.")
else:
    print("You lose.")
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
print('*** Welcome to Universal Decision Maker - Rock, Paper, Scissor ***')
choice = [rock, paper, scissors]
myChoice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissor\n"))
if myChoice > 2:
  print("Wrong Choice :( \nTry again")
else:
  print(choice[myChoice])
  computer_choice = random.randint(0, 2)
  print('Computer Chose: ')
  print(choice[computer_choice])
  if myChoice == computer_choice:
    print("Match Draw!!! Awww!!!")
  elif myChoice > computer_choice:
    if (myChoice == 2 and computer_choice == 0):
      print('Computer wins')
    else:
      print('You win!!!')
  else:
    if (myChoice == 0 and computer_choice == 2):
      print('You win!!!')
    else:
      print('Computer wins')
    
      

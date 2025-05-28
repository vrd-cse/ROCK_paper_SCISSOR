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

computer = [rock , paper , scissors]
user = int(input("enter a number from , 0 for rock , 1 for paper and 2 for scissors\n"))
user_output = [rock , paper , scissors]
computer_random_guess = random.randint(0 , 2)
print(f"Computer choose {computer_random_guess}")
print("You choose -->")
print(user_output[user])
print("Computer chosse -->")
print(computer[computer_random_guess])

if computer_random_guess == user :
    print("It's a draw !!!")
elif computer_random_guess > user:
    print("You loose!!!")
elif computer_random_guess < user:
    print("You win !!!")
elif computer_random_guess == 0 and user == 2:
    print("User loose1 !!!")
elif computer_random_guess == 2 and user == 0:
    print("User win !!!")
else :
    print("You typed an invalid number . You loose!!!")


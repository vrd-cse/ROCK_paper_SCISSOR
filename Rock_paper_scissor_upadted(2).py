import random
from art import paper , scissors , rock

random_dict = {
    "rock" :rock ,
    "paper" :paper ,
    "scissors" : scissors,
}
time_win = 0
total_played_games = 1
to_continue = True
while to_continue:
    
    #  user choice -->
    user = input("enter --> Rock , paper , scissors\n").lower()
    user_choice = random_dict[user]
    print("You choose this -->")
    print(user_choice)

    # computer choice -->
    computer_random_guess = random.choice(list(random_dict))
    print("computer choose this --> ")
    print(random_dict[computer_random_guess])

    # choosing who won -->
    if user == computer_random_guess:
        print("It's a draw!!!")
    elif user == "rock":
        if computer_random_guess == "paper" :
            print("You loose!!!")
        elif computer_random_guess == "scissors" : 
            print("You win!!!")
            time_win +=1 
    elif user == "paper":
        if computer_random_guess == "rock":
            print("You win!!!")
            time_win +=1 
        elif computer_random_guess == "scissors" : 
            print("You loose!!!")
    elif user == "scissors":
        if computer_random_guess == "paper" :
            print("You win!!!")
            time_win +=1 
        elif computer_random_guess == "rock":
            print("You loose!!!")
    
    # asking user to continue playing or not
    ask_uesr_to_continue = input("Type 'Yes '  to continue playing or 'No' to stop \n").lower()
    
    if ask_uesr_to_continue == "no" :
        to_continue == False
        print(f"You played {total_played_games} and won {time_win}")
        print("See you soon !!!")
    else :
        total_played_games += 1
    

    
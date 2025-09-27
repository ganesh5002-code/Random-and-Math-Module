import random
print("Lets play a game of rock, paper scissor\nYou have to beat the computer, what will you pick")
user_choice = (input("Enter your choice"))
possible_actions = ["rock", "paper", "scissor"]
computer_choice = random.choice(possible_actions)
print("Your choice is:", user_choice, "and the computer's choice is:", computer_choice )
if user_choice == computer_choice:
    print("It is a tie")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Paper covers rock, you lose")
    else:
        print("rock smashes the scissor, you win")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock, you win")
    else:
        print("scissor cuts through paper, you lose")
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("rock smashes scissor, you lose")
    else:
        print("scissor cuts through paper, you win")
else:
    print("invalid")

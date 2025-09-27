import random
playing = True
num = str(random.randint(50,53))
print("We will start a guessing game")
while playing:
    guess = (input("You will have to guess a number between 50 and 60 that the computer made:"))
    if num == guess:
        print("You have guessed the number")
        break
    else:
        print("Not quite right, keep going")

import random

choice = ['rock', 'paper', 'scissors']

computer = random.choice(choice)
player = None

while player not in choice:
    player = input("rock,paper,scissors :").lower()

if player == computer:
    print("player: ", player)
    print("computer: ", computer)
    print("Tie!")

elif player == "rock":
    if computer == "paper":
        print("player: ", player)
        print("computer: ", computer)
        print("You lose!")
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("You Win!")

elif player == "scissors":
    if computer == "rock":
        print("player: ", player)
        print("computer: ", computer)
        print("You lose!")
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("You Win!")
elif player == "paper":
    if computer == "scissors":
        print("player: ", player)
        print("computer: ", computer)
        print("You lose!")
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("You Win!")

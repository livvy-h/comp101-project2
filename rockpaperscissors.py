import random

options = ["Rock", "Paper", "Scissors"]

while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)

    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    else:
        print("Computer wins!")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")

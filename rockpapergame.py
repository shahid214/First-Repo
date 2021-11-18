# Rock Paper Scissors game in python 3

import random

def start_game():
    user_win = 0
    computer_win = 0


    options = ['rock', 'paper', 'scissors']
    t = 5
    while (t >= 0):
        t = t-1
        print("\n\n")
        print("rock/ paper/ scissors ? ")
        user_answer = input()

        if user_answer.lower() in options:
            i = random.randint(0, 2)
            computer_answer = options[i]

            if (user_answer == 'rock' and computer_answer == ' scissors') or (
                user_answer == 'paper' and computer_answer == 'rock') or (
                    user_answer == 'scissors' and computer_answer == 'paper'):

                print("Your choice : ", user_answer)
                print("Computer's choice : ", computer_answer)
                print("You won")
                user_win += 1
                continue


            elif user_answer == computer_answer:
                print("both got the same")
                continue
            
            else:
                print("Your choice : ", user_answer)
                print("Computer's choice : ", computer_answer)
                print("You lost! ")
                computer_win +=1
                continue
        else:
            print('type correctly! ')
            continue

        

    print("\n\n")
    print("Player : ",name)

    print("User wins ", user_win)
    print("Computer wins ", computer_win)

    if user_win == computer_win:
        print("You both got the same")

    if user_win > computer_win:
        print("You won")
    else:
        print("You lose")

    c =input()
    exit()



name = input("Enter your name : ")

print("wanna play rock paper scissors ? (yes/no) :  ")
a = input()
if a.lower() == 'yes':
    start_game()

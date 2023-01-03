import random
def start_game():
    global game_on
    game_on = True
    print("Welcome, Type Easy Difficult or Quit ")
    level = input()
    if level == "Easy":
        easy_difficulty()
    elif level == "Difficult":
        hard_difficulty()
    elif level == "Quit":
        game_on = False
        print("Thanks for playing, visit again")

def play_again():
    global play
    game_on = True
    play = input("Do you want to play again, Type Yes or No:  ")
    if play == "Yes":
        start_game()
    if play == "No":
        game_on = False
        print("Thanks for playing")
      
def easy_difficulty():
    global secret
    secret = random.randint(1,100)
    guess = int(input("Guess a number:  "))
    if guess > secret:
        print("The number is greater")
    elif guess < secret:
        print("The number is smaller")
    elif guess == secret:
        print("You guessed the right number")
    play_again()
    
def hard_difficulty():
    global secret
    global guesses
    guesses = 3
    secret = random.randint(1,100)
    for i in range(guesses):
        guess = int(input("Guess a number:  "))
        if i == 2:
            print("Too many guesses, play again")
            play_again()
        elif guess > secret:
            print("The number is greater")
        elif guess < secret:
            print("The number is smaller")
        elif guess == secret:
            print("You guessed the right number")
            play_again()
start_game()   
     

import random
import time

def intro():
    print("Hello! We are going to play a game of Guess The Number!!\nI will guess a number from 1 to 100 and will help you guess it too\nLet's see how many guesses it takes.")
    print("Your Name: ")
    sum_digits = 0
    global name 
    name = input()
    global n
    n = random.randint(1, 100)
    print("Thinking ...... ")
    time.sleep(3.1) #to trick user into thinking that the computer is thinking here
    print("I have guessed a number. I will now give you a few clues.")
    print("One sec ")
    time.sleep(0.81)
    if n % 2 == 0:
        print("     - The number is even")
    else:
        print("     - The number is odd")
    time.sleep(1.932)
    for i in str(n):
        sum_digits += int(i)
    print(f"     - The sum of the digits of the number is {sum_digits}")

def guess():
    g = -1
    guess_count = 0
    while g != n:
        time.sleep(1)  
        g = int(input("\nGuess a number: "))
        if g > 100 or g < 1:
            print(f"Invalid Guess. Guess a number between 1 and 100. Penalaty : {guess_count} (Guess Count) + 2")
            guess_count += 2
            continue
        guess_count += 1
        if n > g:
            print("Guesses :",guess_count)
            print(f"No, the number is actually greater than {g}.")
        elif n < g:
            print("Guesses :",guess_count)
            print(f"No, the number is actually smaller than {g}.")
        else:
            print(f"CONGRATS {name}! You guessed the number - {n} in {guess_count} guesses!")
            print("\nDo you want to play again? Input 'y' to continue and any other key to exit: ")
            y_n = input()
            if y_n.lower() == "y":
                intro()
                guess()
            else:
                exit()

intro()
guess()

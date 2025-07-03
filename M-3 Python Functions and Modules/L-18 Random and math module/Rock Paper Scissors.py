import random 
sh,sc = 0,0
while sh != 3 or sc != 3 :
    ch= input("Rock Paper Scissors\nChoose a object - Rock,Paper or Scissors : ")
    ch = ch.capitalize()
    choices = ["Rock","Paper","Scissors"]
    ch1 = random.choice(choices)
    print(f"You picked {ch}\nThe computer picked {ch1}")
    if ch == ch1 :
        print("Draw")
    elif (ch == "Rock" and ch1 == "Scissors") or (ch == "Paper" and ch1 == "Rock") or (ch == "Scissors" and ch1 == "Paper") :
        print("You Win !!")
        sh += 1
    else :
        print("Computer Wins :(  Better Luck Next Time")
        sc += 1
    print(f"{sh} ~ {sc}")
    if sh == 3 or sc == 3 :
        break

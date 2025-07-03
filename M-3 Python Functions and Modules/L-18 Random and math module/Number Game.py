import random
g = int(input("Guess a number between 1 to 10 : "))
g1 = random.randint(1,10)
print("The computer guessed ",g1,"\nYou guessed ",g)
if g1 == g :
    print("The numbers are matching .")
else :
    print("The numbers are not the same .")
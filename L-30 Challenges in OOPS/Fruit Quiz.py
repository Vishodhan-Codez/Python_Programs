import random
import time

a = 0
while a != 1:
    fruit_colors = { #redid this with dictionary
        "Apple": "Red","Banana": "Yellow","Orange": "Orange","Brinjal or Eggplant": "Purple","Pear": "Green","Spinach": "Green"}
    fruits = list(fruit_colors.keys())
    points = 0

    print("\nHello, welcome to the Fruits and Vegetables Quiz!")
    print("What is the color of these following fruits?\n\nPlease give only the basic color, not any specific color.\n")
    for i in range(5):
        fr1 = random.choice(fruits)
        fruits.remove(fr1)  
        correct_color = fruit_colors[fr1]
        answer = input(f"{fr1}: \n")
        if answer.strip().capitalize() == correct_color:
            points += 1
            print("\nCorrect ✓\n")
        else:
            print("\nWrong ×\n")

        time.sleep(1)

    print(f"\nThe Fruit Quiz is Over! Your final score is: {points}/5")
    if points != 5 :
        print("Better Luck Next Time :( ")
    a = int(input("Do you want to continue? Enter 1 to quit, or any other number to play again: "))

import random
import time
class flashcard() :
    def __init__(self,wrd,mng):
        self.wrd = wrd
        self.mng = mng
    def __str__(self):
        return self.wrd + " : "+ (self.mng)
flshcr = []
done = set()
while True :
    a = input("Enter the word of the flashcard : ")
    b = input("Enter it's meaning : ")
    print("Your flashcard is\n",a," : ",b)
    flshcr.append(flashcard(a,b))
    y_n = int(input("If you wish to continue adding flashcards, press 0 ,else press 1 : "))
    if y_n :
        break
for i in range(len(flshcr)) :
    m=random.choice(flshcr)
    if m in done :
        pass
    else : 
        done.add(m)
        print(m)
    time.sleep(1.1)
    

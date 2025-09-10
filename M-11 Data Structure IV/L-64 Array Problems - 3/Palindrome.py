# 2 min. length , palindrome
def palin2(a) :
    for i in a :
        if len(i) >= 3 :
            if i == i[::-1] :
                print(f"'{i}' is an PALINDROME !")
arr = ["happy","aa","racecar","maam","sad","rhymtotic","ubiquitous"]
print("In",arr,"\n")
palin2(arr)
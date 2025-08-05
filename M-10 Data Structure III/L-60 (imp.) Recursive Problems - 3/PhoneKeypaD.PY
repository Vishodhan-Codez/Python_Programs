keypad = ["","","abc","def","ghi","jkl",'mno',"pqrs","tuv","wxyz"]
def Combinations(comb,curr,out,n):
    if curr == n :
        print(*out,sep=",")
        return
    for i in range(len(keypad[comb[curr]])) :
        out.append(keypad[comb[curr]][i])
        Combinations(comb,curr+1,out,n)
        out.pop()
        if comb[curr] == 0 or comb[curr] == 1 :
            print("No 0 or 1")
            return
        
m = int(input("Enter the the first digit : "))
n = int(input("Enter the second digit : "))
p = int(input("Enter the last digit : "))
li1 = [m,n,p]
leng = len(li1)
Combinations(li1,0,[],leng)
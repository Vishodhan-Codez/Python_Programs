# I , V , X , L ,C , D , M 
n = str(input("Enter a roman numeral: "))
roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
result = 0
for i in range((len(n)-1)) :
        if roman[n[i]] < roman[n[i+1]] :
                result -= roman[n[i]]
        else :
                result += roman[n[i]]
result += roman[n[-1]]
print(f"{n} in numerical form is {result}")
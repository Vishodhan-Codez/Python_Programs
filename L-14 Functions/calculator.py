def add(a,b) :
    return a+b 
def sub(a,b) :
    return a-b 
def mul(a,b) :
    return a*b 
def div(a,b) :
    return a/b 
def exp(a,b) :
    return a**b 
def flor(a,b) :
    return a//b 
def mod(a,b) :
    return a%b 
c= float(input("Enter the first number : "))
d= float(input("Enter the second number : "))
op= input("Enter your desired operator :\n+ - * / ** // % ")
if op == "+" :
    print(add(c,d))
elif op == "-" :
    print(sub(c,d))
elif op == "*" :
    print(mul(c,d))
elif op == "/" :
    print(div(c,d))
elif op == "//" :
    print(flor(c,d))
elif op == "**" :
    print(exp(c,d))
elif op == "%" :
    print(mod(c,d))
else :
    print("Enter valid input !!")
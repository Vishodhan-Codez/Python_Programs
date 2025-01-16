def cube(num) :
    cube = num**3
    print(cube)
def div3(num) :
    if num%3 == 0 :
        cube(num)
    else :
        print(f"Since {num} is not divisible by 3 ,it will not be cubed")
n = float(input("Enter a number divisible by 3 to be cubed : "))
div3(n)
        
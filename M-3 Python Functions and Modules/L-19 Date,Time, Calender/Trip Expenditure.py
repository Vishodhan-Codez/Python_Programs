def aticket(price,persons) :
    return price*persons*2
def hotel(price,days,persons) :
    return (price*days)+(persons*price/4)
def shopping(price) :
    return price
def food(meals,days,price) :
    return meals*price*days
def trpo(price,distance,times) :
    return price*times*distance
def total() :
    people = int(input("Enter the number of people coming on the trip : "))
    pair = float(input("Enter the price of one aeroplane ticket :₹"))
    day = int(input("Enter the number of days you are staying for : "))
    ph = float(input("Enter the price of the hotel per day :₹"))
    ps = float(input("Enter the amount spent on shopping :₹"))
    pm = float(input("Enter the price of one meal :₹"))
    meals = int(input("Enter the number of times you eat per day : "))
    pt = float(input("Enter the price of transportation :₹"))
    dis = float(input("Enter the distance travelled : "))
    tim = int(input("Enter the number of times you travel per day : "))
    a = aticket(pair,people)
    b = hotel(ph,day,people)
    c = shopping(ps)
    d = food(meals,day,pm)
    e = trpo(pt,dis,tim)
    f = a+b+c+d+e
    print("The total amount spent is ₹",f)
total()
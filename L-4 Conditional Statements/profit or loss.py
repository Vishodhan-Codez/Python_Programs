num = int(input("Enter the number of oranges you are buying : "))
cp = float(input("Enter the price for which you bought 1 orange : "))
sp = float(input("Enter the price for which you sold one orange : "))
if cp > sp :
  print("You have occured a loss of Rs.",(cp-sp)*num)
elif sp > cp :
  print("You have occured a profit of Rs.",(sp-cp)*num)
else :
  print("You have occured no loss nor no profit")
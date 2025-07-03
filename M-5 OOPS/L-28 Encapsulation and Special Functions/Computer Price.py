class Comp :
    def __init__(self) :
        self.__mrp = 900
    def sell(self):
        print("The product of the price is {}".format(self.__mrp))
    def setmrp(self,mxp) :
        self.__mrp = mxp
foop = Comp()
foop.sell()
foop.__mrp = 1000 #will not work
foop.sell() # will print 900

foop.setmrp(int(input("Enter a max price : ")))
foop.sell()

 
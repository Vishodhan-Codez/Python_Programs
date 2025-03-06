class ind() :
    def cap(self) :
        print("The capital of India is New Delhi")
    def lan(self) :
        print("The National Language of India is Hindi")
    def siz(self) :
        print("India is the 7th largest country in tsa")
class usa() :
    def cap(self) :
        print("The capital of US is Washington D.C.")
    def lan(self) :
        print("The National Language US is American English")
    def siz(self) :
        print("India is the 4th largest country")
obj1 = ind()
obj2 = usa()
for i in (obj1,obj2):
    i.cap()
    i.lan()
    i.siz()
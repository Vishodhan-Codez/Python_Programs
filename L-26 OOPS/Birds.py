class bird :
    species = "bird"
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
birds = []
a = bird("Bos bubbulias",17,"Red and Blue")
b = bird("Bos indicus",15,"Yellow and Blue")
c = bird("Chmeleo mangatus",14,"Green-Yellow")
birds.append(a)
birds.append(b)
birds.append(c)
print("These are examples of some birds :")
for i in birds:
    print(f"Name: {i.name}\nAge: {i.age}\nColor: {i.color}\n")
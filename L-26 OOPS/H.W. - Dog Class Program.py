class Dog:
    animal = "Dog"
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

dog1 = Dog("Labrador", "Black")
dog2 = Dog("Beagle", "Brown")

print(f"{dog1.animal} - Breed: {dog1.breed}, Color: {dog1.color}")
print(f"{dog2.animal} - Breed: {dog2.breed}, Color: {dog2.color}")

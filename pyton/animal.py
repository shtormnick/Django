class Animal():

    def __init__(self):
        print("Animal Created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("EATING")

class Mamal(Animal):

    def __init__(self):
        print("Maml Created")
    def burning(self):
        print("Born")
    def feeding(self):
        print("Milk feeding")

class Amphibinas(Animal):

    def __init__(self):
        print("Amphibinas")
    def burning(self):
        print("Lay eggs")
    def feeding(self):
        print("Else Feeding")

class Dog(Mamal):

    def __init__(self):
        print("Dog Created")
    def bark(self):
        print("Woof")

class Rabbit(Mamal):

    def __init__(self):
        print("Rabbit was Created")
    def bark(self):
        print("Sniff")

class Triton(Amphibinas):
    def __init__(self):
        print("Triton was Created")
    def bark(self):
        print("Snikk")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.burning()
mydog.feeding()
mydog.bark()

mydog = Triton()
mydog.whoAmI()
mydog.eat()
mydog.burning()
mydog.feeding()
mydog.bark()

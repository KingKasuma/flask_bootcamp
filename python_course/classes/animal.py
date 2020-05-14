class Animal():

    def __init__(self, fur):
        self.fur = fur

    def report(self):
        print("Animal")
    
    def eat(self):
        print('Eating!')

#Heredando de la clase animal
class Dog(Animal):

    def __init__(self, fur):
        Animal.__init__(self, fur) #Inicializando el constructor de la clase padre
        print("Dog Created!")
    
    def report(self):
        print("I am a dog")

d = Dog('Fuzzy')
d.eat()
d.report()
print(d.fur)
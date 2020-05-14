class Dog():

    # CLASS OBJECT ATTRIBUTES
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sam = Dog('Huskie', 'Sammy')

print(sam.breed)
print(sam.name)
print(sam.species)
# Creating class animal with common attributes
class Animal:
    def __init__ (self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self._health_status = "Healthy"
    # Creating placeholder method for further modification
    def make_sound(self):
        pass
# Creating specific animal class for elephant
class Elephant(Animal):
    def __init__(self, name, age, species, color):
        super().__init__(name, age, species)
        self.color = color
    def make_sound(self):
        return "Trumpet"
# Creating specific animal class for lion
class Lion(Animal):
    def __init__(self, name, age, species, color, weight):
        super().__init__(name, age, species)
        self.color = color
        self.weight = weight
    def make_sound(self):
        return "Roar"
# Creating class for zookeeper who takes care for animals
class Zookeeper:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

    def give_medication_to_animal(self, animal):
        print(f"{self.name} is giving medication to {animal.name}.")
# Class for enclosures representing different areas within the zoo where animals are housed and storing the list of animals
class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = [] 
    def add_animal(self, animal):
        self.animals.append(animal)

# Instantiating objects from
chomper = Elephant("Chomper", 8, "Palaeoloxodon falconeri", "Gray")
zuriko = Lion("Zuriko", 3, "Asiatic", "Gold", 250)
irakli = Zookeeper("Irakli", 203423)
irakli.feed_animal(chomper)
enclosure2 = Enclosure("Second enclosure")
enclosure2.add_animal(zuriko)
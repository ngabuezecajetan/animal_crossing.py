# animal_crossing.py

class Animal:
    def __init__(self, name, species, personality):
        self.name = name
        self.species = species
        self.personality = personality

class Villager(Animal):
    def __init__(self, name, species, personality):
        super().__init__(name, species, personality)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def greet(self):
        print(f"Hello, I'm {self.name} the {self.species} with a {self.personality} personality")

    def show_items(self):
        if self.items:
            print(f"{self.name} has the following items:")
            for item in self.items:
                print(f"- {item}")
        else:
            print(f"{self.name} has no items")

class Player(Villager):
    def __init__(self, name, species

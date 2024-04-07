class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attackes {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving to {new_form}!")
        self.name = new_form

# Creation of Pikachu object
pikachu = Pokemon('Pickachu', "Electric", 100)

# Usage of methods
pikachu.attack(Pokemon('Charmander', "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")

print(pikachu.name, pikachu.type, pikachu.health)
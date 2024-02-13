# Players
# Player classes
# Weapons
# Armor
# Spells
# Monsters

class Player:
    def __init__(self, race, sex, name):
        self.race = race
        self. sex = sex
        self.name = name

# Weapons, armor, spells, characters, monsters; all have a type and level. 
class LevelType:
    def __init__(self, type, level):
        self.type = type
        self.level = level

class CharClasses:
    def __init__(self):
        LevelType.__init__(self, type = ["Wizard", "Fighter", "Healer"], level = 1)

class Weapons:
    def __init__(self):
        LevelType.__init__(self, type = ["Staff", "Sword", "Dagger"], level = 1)

class Armor:
    def __init__(self):
        LevelType.__init__(self, type = ["Helm", "Cloak", "Boots"], level = 1)

class Spells:
    def __init__(self):
        LevelType.__init__(self, type = ["Attack", "Defense", "Heal"], level = 1)

# The creatures we'll battle
# Do I need to hardcode some of this in?
class Monster(LevelType):
    def __init__(self, name, special, weakness):
        super().__init__(type = "Enemy", level = 1)
        # What are their special attacks and weaknesses?
        self.name = name
        self.special = special
        self.weakness = weakness

# Create an opponent and set their level
Vampire = Monster(name = "Dracula", special = "Hypnotic blast", weakness = "Wooden stakes")
Vampire.level = 5

print("Your first opponent is " + str(Vampire.name) + ", a level " + str(Vampire.level) + " " + str(Vampire.type) + ".")

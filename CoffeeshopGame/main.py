# Clydebank Coffee Shop Simulator 4000
# Copyright (C) 2024 Clydebank Media, All Rights Reserved

# Import all functions from the utilties module
from utilities import *

# Import the game class from teh coffee_shop_simulator module
# Causing errors and not needed?!
from coffee_shop_simulator import CoffeeShopSimulator

# Print welcome message
welcome()

# Get name and store name
# Variables with t_ in front are temporary as used by teacher
t_name = prompt("Like, what's your name bro? ", True)
t_shop_name = prompt("What you want to call your coffee shop? ", True)

# Create the game object
game = CoffeeShopSimulator(t_name, t_shop_name)

game.run()

# Say goodbye!
print("\nThanks for playing. Have a great day, player!\n")
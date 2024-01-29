# Clydebank Coffee Shop Simulator 4000
# Copyright (C) 2024 Clydebank Media, All Rights Reserved

# Import from the random module
import random


# Welcome message function
def welcome():
	print("Clydebank Coffee Shop Simulator 4000, Version 1.1\n")
	print("Copyright (C) 2024 ClydeBank Media, All Rights Reserved.\n")
	print("Let's collect some information before we start the game.\n")
	

# Function to handle prompts
def prompt(display="Please input a string", require=True):
	if require:
		s = False
		while not s:
			s = input(display + " ")
	else:
		s = input(display + " ")
	return s
	
	
# Function to convert a string to a float. 
# If conversion fails, assign it to 0
def convert_to_float(s):
	try:
		f = float(s)
	except ValueError:
		f = 0
	return f
	
	
# Unsure of what this function is for yet
def x_of_y(x, y):
	num_list = []
	# Return a list of x numbers of y
	for i in range(x):
		num_list.append(y)
	return num_list
	
	
class CoffeeShopSimulator:

	# Minimum and maximum temperatures
	TEMP_MIN = 45
	TEMP_MAX = 85
	
	def __init__(self, player_name, shop_name):

		# Set player and coffee shop names
		self.player_name = player_name
		self.shop_name = shop_name
		
		# Current day number
		self.day = 1
		
		# Cash on hand at start
		self.cash = 100.00
		
		# Inventory at start
		self.coffee_inventory = 100
		
		# Sales list
		self.sales = []
		
		# Possible temperatures
		self.temps = self.make_temp_distribution()
		
	def run(self):
		print("\nOk, let's get started. Have fun!")
		
		# The main game loop
		running = True
		while running:
			# Display the day and add a "fancy" text effect
			self.day_header()
			
			# Get the weather
			temperature = self.weather
			
			# Display the cash and the weather
			self.daily_stats(temperature)
			
			# Get the price of a cup of coffee
			cup_price = float(
				prompt("What do you want to charge per cup of coffee? "))
			
			# Get advertising spend
			print("\nYou can buy advertising to help promote sales.")
			advertising = prompt(
				"How much advertising do you want to buy (0 for none)?", False)
			
			# Convert advertising into a float. If it fails, assign it to 0
			advertising = convert_to_float(advertising)
			
			# Deduct advertising from cash on hand. 
			self.cash -= advertising
			
			# Make sales
			cups_sold = self.simulate(temperature, advertising, cup_price)
			gross_profit = cups_sold * cup_price
			
			# Display the results
			print("You sold " + str(cups_sold) + " cups of coffee today.\n")
			print("You made $" + str(gross_profit) + ". \n")
			
			# Bank the profit
			self.cash += gross_profit
			
			# Subtract inventory
			self.coffee_inventory -= cups_sold
			
			# Before we loop around, add a day
			self.increment_day()
			
	def simulate(self, temperature, advertising, cup_price):
		# Find out how many cups were sold
		cups_sold = self.daily_sales(temperature, advertising)
		
		# Save the sales data for today
		self.sales.append({
			"day": self.day,
			"coffee_inv": self.coffee_inventory,
			"advertising": advertising,
			"temp": temperature,
			"cup_price": cup_price,
			"cups_sold": cups_sold
		})
		
		# We technically don't need this, but why make the next step
		# to read from the sales list when we have the data right here?
		return cups_sold
	
	# Faux temp distributions. We'll do this better
	# later with a bell curve, but for now a quick hack
		
	def make_temp_distribution(self):
		# This is not a good bell curve, but it will do for now until
		# we get to more advanced maths
		temps = []
		
		# First, find the average between TEMP_MIN and TEMP_MAX
		avg = (self.TEMP_MIN + self.TEMP_MAX) / 2
		
		# Find the distance between TEMP_MAX and the average
		max_dist_from_avg = self.TEMP_MAX - avg
		
		# Loop through all possible temperatures
		for i in range(self.TEMP_MIN, self.TEMP_MAX):
		
			# How far away is the temperature from average?
			# abs() gives us the absolute value
			dist_from_avg = abs(avg - i)
			
			# How far away is the dist_from_avg from the maximum?
			# This will be lower for temps at the extremes
			dist_from_max_dist = max_dist_from_avg - dist_from_avg
			
			# If the value is zero, make it one
			if dist_from_max_dist == 0:
				dist_from_max_dist = 1
				
			# Append the output of x_of_y to temps
			for t in x_of_y(int(dist_from_max_dist), i):
				temps.append(t)
		return temps
			
	def increment_day(self):
		self.day += 1
		
	def daily_stats(self, temperature):
		print("You have $" + str(self.cash) + 
			" cash and it's " + str(temperature) + " degrees. ")
		print("You have enough beans in stock to make " + 
			str(self.coffee_inventory) + " cups of coffee.\n")
		
	def day_header(self):
		print("\n-----| Day" + str(self.day) + 
			" @ " + self.shop_name + " |-----")
		
	# Huh?!
	def daily_sales(self, temperature, advertising):
		return int((self.TEMP_MAX - temperature) * (advertising * 0.5))
		
	@property
	def weather(self):
		# Generate a random temp between 60 and 75°
		# TODO: Set up seasons later on
		return random.choice(self.temps)
	
# End of class CoffeeShopSimulator


# Print welcome message
welcome()


# Get name and store name
t_name = prompt("Like, what's your name bro? ", True)
t_shop_name = prompt("What you want to call your coffee shop? ", True)

# Create the game object
game = CoffeeShopSimulator(t_name, t_shop_name)

# Run the game
game.run()
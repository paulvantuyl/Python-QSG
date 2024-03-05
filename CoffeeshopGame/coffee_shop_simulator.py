# Import needed modules
import random
import re
from utilities import *

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
		welcome_message = "Ok, let's get started. Have fun!"
		print(f"\n{welcome_message}")
		
		# The main game loop
		running = True
		while running:
			# Display the day and add a "fancy" text effect
			self.day_header()
			
			# Get the weather
			temperature = self.weather
			
			# Display the cash and the weather
			self.daily_stats(temperature)
			
			# Get the price of a cup of coffee (but provide an escape hatch)
			response = prompt("What do you want to charge per cup of coffee? (type exit to quit)")
			if re.search("^exit", response, re.IGNORECASE):
				running = False
				continue
			else:
				cup_price = int(response)

			# Do they want to buy more coffee inventory?
			response = prompt("Want to buy more coffee? (hit ENTER for none or enter the number)", False)
			if response:
				if not self.buy_coffee(response):
					print("Could not buy additional coffee.")

			# TODO: Force user to buy coffee if they are out of inventory
			# Could be an evaluation of the coffee sold previously
			# if self.coffee_inventory <= 0:
			# 	print("\n( GAME OVER! You ran out of coffee. )")
			# 	running = False
			# 	continue
	
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

			if self.cash < 0:
				print("\n( GAME OVER! You ran out of cash. )")
				running = False
				continue
			
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
	
	# Restock inventory
	def buy_coffee(self, amount):
		try:
			i_amount = int(amount)
		except ValueError:
			return False
		
		if i_amount <= self.cash:
			self.coffee_inventory += i_amount
			self.cash -= i_amount
			return True
		else:
			return False
		
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
			
	# Add a day
	def increment_day(self):
		self.day += 1
		
	# Daily stats
	def daily_stats(self, temperature):
		print("You have $" + str(self.cash) 
			  + " cash and it's " + str(temperature) + " degrees. ")
		print("You have enough beans in stock to make " 
			  + str(self.coffee_inventory) + " cups of coffee.\n")
		
	def day_header(self):
		print("\n-----| Day" + str(self.day) + 
			" @ " + self.shop_name + " |-----")
		
	# Huh?!
	def daily_sales(self, temperature, advertising):
		return int((self.TEMP_MAX - temperature) * (advertising * 0.5))
		if sales > self.coffee_inventory:
			sales = self.coffee_inventory
			print("You would have sold more coffee but you ran out. Be sure to buy additional inventory.")
		
	@property
	def weather(self):
		# Generate a random temp between 60 and 75°
		# TODO: Set up seasons later on
		return random.choice(self.temps)
	
# End of class CoffeeShopSimulator

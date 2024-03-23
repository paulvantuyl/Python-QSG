# Import needed modules
import random
import re
import numpy
from utilities import *


class CoffeeShopSimulator:

	# Minimum and maximum temperatures
	TEMP_MIN = 20
	TEMP_MAX = 90

	# Length of temperature list
	# Higher produces more realistic curve
	SERIES_DENSITY = 300
	

	def __init__(self, player_name, shop_name):

		# Set player and coffee shop names
		self.player_name = player_name
		self.shop_name = shop_name
		
		# Current day number
		self.day = 1
		
		# Cash on hand at start
		self.cash = 100.00
		
		# Inventory at start
		# What is this definition? 100 servings?
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
			response = prompt(
				"What do you want to charge per cup of coffee? (type exit to quit)")
			if re.search("^exit", response, re.IGNORECASE):
				running = False
				continue
			else:
				cup_price = int(response)


			# Do they want to buy more coffee inventory?
			print(
				"\nIt costs $1 for the necessary inventory to make a cup of coffee.")
			response = prompt(
				"Want to buy more coffee? (hit ENTER for none or enter the number)", False)

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
			print("\nYou sold " + str(cups_sold) + " cups of coffee today.")
			print("\nYou made $" + str(gross_profit) + ".")
			
			# Bank the profit
			self.cash += gross_profit
			
			# Subtract inventory
			self.coffee_inventory -= cups_sold

			if self.cash < 0:
				print("\n:( GAME OVER! You ran out of cash.")
				running = False
				continue
			
			# Before we loop around, add a day
			self.increment_day()


	def simulate(self, temperature, advertising, cup_price):

		# Find out how many cups were sold
		cups_sold = self.daily_sales(temperature, advertising, cup_price)
		
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


	def make_temp_distribution(self):

		# Create a series of numbers between TEMP_MIN and TEMP_MAX
		series = numpy.linspace(self.TEMP_MIN, self.TEMP_MAX, self.SERIES_DENSITY)

		# Obtain the mean and standard deviation from the series
		mean = numpy.mean(series)
		std_dev = numpy.std(series)

		# Calculate probability density and return the list it creates
		return (numpy.pi * std_dev) * numpy.exp(-0.5 * ((series - mean) / std_dev) ** 2) 


	# Add a day
	def increment_day(self):

		self.day += 1


	# Daily stats
	def daily_stats(self, temperature):

		print("You have $" + str(self.cash) 
			  + " cash and it's " + str(temperature) + " degrees. ")
		
		print("You have enough beans in stock to make " 
			  + str(self.coffee_inventory) + " cups of coffee.\n")


	# Interface that's reused
	def day_header(self):

		print("\n-----| Day" + str(self.day) + 
			" @ " + self.shop_name + " |-----")


	# Daily sales calculations
	def daily_sales(self, temperature, advertising, cup_price):

		# Randomize advertizing effectiveness
		adv_coefficient = random.randint(20,80) / 100

		# Higher priced coffee doesn't sell as well
		price_coefficient = int((cup_price * (random.randint(50, 250) / 100)))

		# Run the sales figures
		sales = int((self.TEMP_MAX - temperature) * (advertising * adv_coefficient))
		
		# If the price is too high, we don't sell anything 
		if price_coefficient > sales:
			sales = 0
		else:
			sales -= price_coefficient

		if sales > self.coffee_inventory:
			sales = self.coffee_inventory
			print("You would have sold more coffee but you ran out. Be sure to buy additional inventory.")

		return sales
		
	@property
	def weather(self):

		# Generate a random temp between 60 and 75°
		# TODO: Set up seasons later on
		return random.choice(self.temps)
	
# End of class CoffeeShopSimulator

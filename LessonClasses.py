# The parent Furniture class
class Furniture:
	def __init__(self, width = 0, height = 0, material = "Wood"):
		self.width = width
		self.height = height
		self.material = material

# First child, the Chair class
class Chair(Furniture):
	# By defining an __init__ method in Chair we override the
	# __init__ method in Furniture
	def __init__(self, material, width = 0, height = 0, arms = True, back = True):

		super().__init__(width, height, material)
		self.arms = arms
		self.back = back
		
class Bench(Chair):
	pass

sofa = Bench("Metal")

# vars is useful for testing and debugging
# Providing it an object for its argument returns
# the dictionary for the object, which contains
# all the mutable (writable) attr and their values.
print(vars(sofa))

# Multiple inheritance
# When a child class with multiple parents shares
# attributes of multiple parents.

class FurnitureTwo:
	def __init_(self, width, height, material):
		self.width = width
		self.height = height
		self.material = material

class Surface:
	def __init__(self, flat):
		self.flat = flat

class Table(FurnitureTwo, Surface):
	def __init__(self, width = 0, height = 0, material = "Wood", flat = True):

		Furniture.__init__(self, width, height, material)
		Surface.__init__(self, flat)
		self.legs = 4

# Two tables with no parameters and only defaults.
a = Table()
b = Table()

# Then the weird table
fred = Table(flat = False)
#print(vars(a))

class FurnitureThree:
	pass

class ChairTwo(FurnitureThree):
	pass

class Stool(ChairTwo):
	def __init__(self, number):
		self.number = number

# Create an empty list named bar
bar = []

# Add 8 stools to the bar
for i in range(8):
	bar.append(Stool(i))
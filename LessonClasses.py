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

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


# Return a list of x numbers of y
def x_of_y(x, y):
	num_list = []
	
	for i in range(x):
		num_list.append(y)
	return num_list
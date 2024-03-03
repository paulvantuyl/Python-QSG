import zlib

# Define the name
name = "Paul"

# Print a friendly message
print("\nHello, {}!".format(name))

# Define our greeting
greeting = "\nHello, {name}! It's currently {temp} and the time is {time}."

# Print the greeting by passing keyword arguments to the format method
print(greeting.format(name = "Paul", temp = "54 F", time = "6:55 AM"))

total = 6.9565
message = "\nYour total is ${:.2f}."
print(message.format(total))

# F strings
first_day = "Monday"
second_day = "Wednesday"
print(f"\nWe are closed this week from {first_day} until {second_day}.")

# We can run evaluations within F strings (shrug)
print(f"\nTesting evaluations in f-strings: {3 * 9}")

# We can use functions also
word = "cool!"
print(f"Testing functions in f-strings: {word.upper()}")

# Compress some data
data = """To compress data, we'll need a long string.
    Not a short string. No, that would be too small. 
    To get any meaningful benefit from compression, 
    you must use a decent length of data or else the overhead of compression 
    isn't worth the gains.
    This will be enough data, containing enough redudant
    patterns, to be
    compressible."""

# encoded_data = data.encode()
compressed_data = zlib.compress(data.encode())

# Display stats
data_len = len(data)
compressed_data_len = len(compressed_data)
print("Length of uncompressed data: " + str(data_len))
print("Length of compressed data: " + str(compressed_data_len))

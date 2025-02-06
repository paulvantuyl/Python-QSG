# String to write
data = "The lazy red fox slept instead of jumpimg over the dog."

# Write the data
with open("fox.txt", mode="w", encoding="utf-8") as f:
    f.write(data)

# Read the file
with open("fox.txt", mode="rb") as f:
    while (c := read_data = f.read(32)):
		# do something but book didnt give example

# Display the results
print("Original: " + data)
print("From disk: " + read_data)

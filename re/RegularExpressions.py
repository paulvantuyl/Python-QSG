# Import the regular expression engine
import re

# 
# Regular expressions
# 

print("\nREGEX -----------------------------------\n")

text = "Hello, WORLD"

# re.IGNORECASE is a regex flag (option) that can be shortened to re.I
if re.search("hello", text, re.IGNORECASE):
    print("hello is in the string.\n")
else:
    print("hello isn't in the string.\n")

#  Does the string begin with the letter H?
if re.search("^H", text):
    print("The string begins with H.\n")
else:
    print("The string does not begin with H.\n")

# Does the string end in an exclamation point?
if re.search("\!$", text):
    print("The string ends with an exclamation point!\n")
else:
    print("The string does NOT end with an exlamation point.\n")

# Find and match using regex
content = "The quick gray fox jumps over the lazy dog!\n"
match   = re.search("(gray|grey)", content, re.IGNORECASE)

# Object returned by match
print(match.group(0))
# Where exactly the match starts and ends
print(str(match.span()))

# Match postion of a string and replace
blurb  = "The quick gray fox jumped over the lazy dog!"
mblurb = re.search("(gray|grey)", blurb, re.IGNORECASE)

# Get start and end of match blurb (mblurb)
match_start  = mblurb.span()[0]
match_end    = mblurb.span()[1]
replace_text = "grey"
new_blurb    = blurb[:match_start] + replace_text + blurb[match_end:]

# Display the results
print("\nOld text: " + blurb)
print("\nNew text: " + new_blurb + "\n")

# Metacharacters \b \w
text2 = "This is the the house. It has red red paint."

# Regex to find duplicate words
# Use prefix r before to treat as raw (unescaped) string
# This prevents the regex from turning \b into backspace
regex = r"\b(\w+)\s+\1\b"

# Find any duplicate words
# re.findall returns a dictionary of the matches it finds
matches = re.findall(regex, text2, re.IGNORECASE)

# Print the duplicate words
for matching in matches:
    print(matching)
    print(len(matches))

# A multiline string
# A regex that can match the exact beginning of multiple lines is \A
# \Z will match the end of a multiline
# re.search("\AThis", text)
multiLineText = """This is a multiline string.
    It has multiple lines to it. So, fittingly, it's called a multiline string.
    When you type a string and hit ENTER, 
    a special character is inserted into the string.
    That special character is a backslash followed by a n."""

# 
# Match function
# 

print("\nMatch function --------------------------\n")

test = "Hello, World!"

# Match
if re.match("e", test):
    print("re.match says it has an e in it.")
else:
    print("re.match says there's no e at the beginning.")

# Search
if re.search("e", test):
    print("re.search says it has an e in it.")

# 
# Regex splitting and sustitution
# 

print("\nRegex splitting and substitution --------\n")

test_split = "The quick brown fox is fast!"

# Split by spaces using the \s metacharacter
# Since we want to account for multiple spaces, we add + 
space_split = re.split("\s+", test_split)
print(space_split)

# Split by word using the non-word metacharacter
# Since we want to account for multiple non-word characters, we ad +
word_split = re.split("\W+", test_split)
print(word_split)

# Substitute spaces with +
plus_test = re.sub("\s+", "+", test_split)
print(plus_test)

# 
# Find and replace
# 

print("\nFIND AND REPLACE ------------------------\n")

# Create a string
a = "Hello, World!"

# Search for "World" in the string
if a.find("World") != -1:
    # Replace "World" with "Reader"
    b = a.replace("World", "Reader")

    # Display the results
    print(a)
    print("… was replaced with …")
    print(b)

c = "Hello, House"

# Search for "House" in the string
if c.find("House") != -1:
    print(c)
    print("… was replaced with…")
    print(c.replace("House", "Reader"))

# 
# Case changes
# 

print("\nCASE CHANGES ----------------------------\n")

# Create our string
title = "Python QuickStart Guide"

# Display it in all uppercase
print(title.upper())

# Display it in all lower
print(title.lower())

tongue_twister = "She sells seashells by the seashore."

# Count the number of 's' in the tongue_twister and display it
print("There are " + str(tongue_twister.count("s")) + " of the letter s in:")
print(tongue_twister)

#
# String modifications
#

print("\nSTRING MODIFICATIONS --------------------\n")
# A simple string
fox = "The quick brown fox jumps over the lazy dog."

# Split the string
fox_list = fox.split()

# Display the resulting list
print(fox_list)

# An obvi fake ID number
id = "123-455-6789"

# Split ID by a dash character
id_segments = id.split("-")

# Display it
print(id_segments)

# New glossary terms
glossary = "delimiter, module, package, class, object"

# Split by comma, then by space
glossary_list = glossary.split(", ")
print(glossary_list)

glossary_two = ['delimiter', 'module', 'package', 'class', 'object']
glossary_string = ", ".join(glossary_two)
print(glossary_string)

#
# Working with user inputs
#

print("\nUSER INPUT STUFF ------------------------\n")
# Ask user for a value
value = input("Please enter a value: ")

# Check if every character is a number
# "3102" - True
# "384575848327347" - True
# "04/04/2024" - Fale
# "1600 Pensylvania Ave" - FAlse
if value.isnumeric():
    print("It's a number.")

# Check if every character is a letter
# Spaces, punctuation, and numbers don't count
# "Yes" - True
# "Yes " - False
# "Yes 3" - False
# "Yes!" - False
if value.isalpha():
    print("It is filled with alphabet characters only.")

# Check if the string is alphanumberic – letters and numbers
# 1600 Pennsylvania Avenue – False
# Washington, D.C. – False
# Washington – True
if value.isalnum():
    print("It's alphanumeric.")
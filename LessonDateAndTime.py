import datetime
from datetime import date

# Get the current time and date
now = datetime.datetime.now()

# Display it
print(now)

# Display the year
print(now.year)

# Display the month
print(now.month)

# Display date and time in a custom formate
# There are format codes associated with strftime
print(now.strftime("%A, %B %d, %Y at %I:%M %p"))

# Create a delta of 18 hours and 49 minutes
delta = datetime.timedelta(hours = 18, minutes = 49)

# Subtract delta and store in previous_time 
previous_time = now - delta

# Display time and time minus the delta
print("\n")
print(now)
print(previous_time)

print("\n")

my_birthday = date(2024, 4, 15)
date_today = date.today()
birthday_delta = my_birthday - date_today
print(birthday_delta)

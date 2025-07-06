from datetime import datetime

# Exercises: Day 16

# Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(
    f"Current date and time; {day}/{month}/{year}, {hour}:{minute}. Timestamp: {timestamp}"
)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

current_datetime = now.strftime("$d/%m/%Y, %H:%M:%S")
print(current_datetime)

# Today is 5 December, 2019. Change this time string to time.
today = "1 january, 1986"
date_object = datetime.strptime(today, "%d %B, %Y")
print(date_object)

# Calculate the time difference between now and new year.
t1 = datetime.now()
t2 = datetime(year=2026, month=1, day=1, hour=00, minute=00, second=1)
time_difference = t2 - t1
print(f"Time difference = {time_difference}")

# Calculate the time difference between 1 January 1970 and now.

t1 = datetime(year=1970, month=1, day=1)
t2 = datetime.now()
time_difference = t2 - t1
print(f"Time difference = {time_difference}")

# Think, what can you use the datetime module for? Examples:

# Time series analysis
"""To analyze data tha has been collected at regular intervals over time. Daily temperature, hourly traffic, prices of actions per hour, number of sales per month, cardiac rhythm per second."""

# To get a timestamp of any activities in an application
"""To get the response time"""

# Adding posts on a blog
"""To coordinate the time of posting something in a blog"""

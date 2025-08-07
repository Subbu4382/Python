from datetime import datetime, timedelta

#  Get the current date and time
print("Current datetime:", datetime.now())

# Parsing strings to datetime using strptime
print(datetime.strptime("01/01/2020", "%d/%m/%Y"))       
print(datetime.strptime("january/10/03", "%B/%d/%y"))    
print(datetime.strptime("01/12/1999", "%d/%m/%Y"))      

#  Formatting datetime to string using strftime
now = datetime.now()
print(now.strftime("%b/%d/%y %A %H:%M"))   
print(now.strftime("%H:%S :%M %a"))          

#  Format reference:
# %Y - Full year       | %y - Short year
# %B - Full month name | %b - Short month name
# %m - Month number    | %d - Day of month
# %A - Full weekday    | %a - Abbreviated weekday
# %H - Hours (24h)     | %I - Hours (12h)
# %M - Minutes         | %S - Seconds

#  Replace parts of a datetime (set a new date/time)
cur = datetime.now()
print("Custom datetime with replace:", cur.replace(2024, 1, 1, 23, 55, 32))

#  Modify a birthday date and check weekday
my_bday = datetime.strptime("2003/11/29", "%Y/%m/%d")
my_bday = my_bday.replace(2003, 8, 9)  # Replacing a date
print("Weekday :", my_bday.weekday())       
print("Today’s weekday:", datetime.now().weekday())
print("Today’s ISO weekday (1=Monday):", datetime.now().isoweekday())

#  Add and subtract time using timedelta
print("28 days from now:", datetime.now() + timedelta(days=28))
print("90 days, 10 hours, 50 seconds ago:", datetime.now() - timedelta(days=90, hours=10, seconds=50))

#  More datetime operations
print("ISO format datetime:", datetime.now().isoformat())
print("Just the date:", datetime.now().date())
print("Time after 100 hours:", (datetime.now() + timedelta(hours=100)).time())

#  Find difference between now and a past datetime
past_date = datetime.strptime("1/1999/12", "%d/%Y/%m")
print("Time difference since 1999:", datetime.now() - past_date)

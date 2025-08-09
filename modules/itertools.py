from itertools import count
# count(start, step) creates an infinite counter
# This starts at 5 and increases by 2 each time
for num in count(5, 2):  # Start=5, step=2
    print(num)
    if num >= 15:
        break

# cycle() repeats the list endlessly
from itertools import cycle
colors = ["Red", "Green", "Blue"]
for i, color in enumerate(cycle(colors), 1):  # Keep a counter starting at 1
    print(color) 
    if i == 6:  
        break


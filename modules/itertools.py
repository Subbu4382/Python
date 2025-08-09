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

# repeat(value, times) repeats the same item a set number of times
from itertools import repeat
for val in repeat("Python", 3):
    print(val) 

# combinations(iterable, r) → All unique groups of length r
from itertools import combinations
items = ["A", "B", "C"]
for combo in combinations(items, 2):
    print(combo)

# permutations(iterable, r) → All possible arrangements of length r
from itertools import permutations
items = ["A", "B", "C"]
for perm in permutations(items, 2):
    print(perm)



import math , random 

#  Generate a Random Float between 0 and 1
import random
print("Random float between 0 and 1:", random.random())

# Generate a Random Integer within a Range
print("Random integer between 10 and 50:", random.randint(10, 50))

# Generating a OTP
digits=4 
otp=""
for i in range(digits):
    num= math.floor(random.random()*10 ) 
    otp+=str(num)   
print(otp)

# Simulate a Dice Roll
dice = random.randint(1, 6)
print("Dice rolled:", dice)

# Randomly Select an Item from a List
names = ["arjun", "kalyan", "ram", "mahesh"]
print("Randomly selected name:", random.choice(names))

# Randomly Select Multiple Items
colors = ["Red", "Blue", "Green", "Yellow"]
print("3 random colors:", random.choices(colors, k=3))

# Shuffle a List
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled cards:", cards)


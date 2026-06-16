import math

x = pow(4, 3) # 4 ** 3
print(x)

# ---
x = math.sqrt(64)
print(x)
# ---

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

# --
x = math.pi
print(x)

# ---
import random
random.random()   # 0.374...
random.random()   # 0.891...
random.random()   # 0.012... (0, 1)

random.randint(1, 10)   # включительно
random.randint(1, 6)
random.randint(0, 100)

# ---

colors = ["red", "green", "blue", "yellow"]

random.choice(colors)   # 'blue'
random.choice(colors)   # 'red'
random.choice(colors)   # 'blue'

# ---
cards = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(cards)
print(cards)  # [5, 2, 8, 1, 6, 3, 7, 4]
random.shuffle(cards)
print(cards)  # [3, 7, 1, 8, 2, 6, 4, 5]

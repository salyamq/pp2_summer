import math

# 1
n = float(input())
print(n * math.pi / 180)

# 2

h = float(input())
a = float(input())
b = float(input())

area = (a + b) / 2 * h
print(area)

# 3
n = int(input())
s = float(input())

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print(area)

# 4
a = float(input())
b = float(input())

area = a * b
print(area)


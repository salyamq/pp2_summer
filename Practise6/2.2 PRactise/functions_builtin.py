# Use map() and filter() on lists
# Aggregate with reduce() (from functools)
# Use enumerate() and zip() for paired iteration
# Demonstrate type checking and conversions
from functools import reduce

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
print(squared, even)

total = reduce(lambda x, y: x + y, nums)
print(total)

fruits = ["apple", "banana", "cherry"]
numes = [1, 2, 3]
for i, fruit in enumerate(fruits):
    print(i, fruit)


for num, fruit in zip(numes, fruits):
    print(num, fruit)

print(type(total))
numes_str = [str(i) for i in numes]
print(numes_str)
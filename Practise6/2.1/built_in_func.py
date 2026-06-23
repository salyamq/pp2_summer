len([1,2,3])            # 3
sum([1,2,3])            # 6
min([1,2,3])            # 1
max([1,2,3])            # 3

# map(), filter(), reduce(), enumerate(), zip(), sorted()
map_ = list(map(lambda x: x*2, [1,2,3]))     # [2,4,6], map returns generator object
filter_ = list(filter(lambda x: x>1, [1,2,3])) # [2,3], filter returns generator object

# -----------------------------------------

from functools import reduce
reduce_ = reduce(lambda a,b: a+b, [1,2,3])       # 6
# firstly lambda 1, 2: 3
# then, THIS 3 will be x, and sequence[2] (3) will be y

# -----------------------------------------

letters = ['A', 'B', 'C']
print(list(enumerate(letters))) # [(0, 'A'), (1, 'B'), (2, 'C')

for x, y in enumerate(letters):
    print(x, y) # 0, A; 1, B; 2, C

# -----------------------------------------

players = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
print(list(zip(players, scores))) # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

for player, score in zip(players, scores):
    print(f"Player: {player} | Score: {score}")
# Player: Alice | Score: 85
# Player: Bob | Score: 92
# Player: Charlie | Score: 78

# -----------------------------------------

numbers = [3, 1, 4, 2]
sorted_nums = sorted(numbers)
print(sorted_nums) # [1, 2, 3, 4]
print(numbers)     # [3, 1, 4, 2]

letters = ['A', 'C', 'B']
print(sorted(letters, reverse=True)) # ['C', 'B', 'A']

words = ['apple', 'kiwi', 'banane', 'orange']
print(sorted(words, key=len))
# ['kiwi', 'apple', 'banane', 'orange']

results = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

print(sorted_results) # sorted only by numbers, due to x[1]
# [('Bob', 92), ('Alice', 85), ('Charlie', 78)]


# 1
def sq(n):
    for i in range(n + 1):
        yield i * i

N = 10

for i in sq(10):
    print(i)

# 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(x) for x in even_numbers(n)))

# 3

def div34(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for x in div34(n):
    print(x)

# 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for i in squares(3, 8):
    print(i)

# 5

def minus(n):
    for i in range(n, -1, -1):
        yield i

for x in minus(10):
    print(x)

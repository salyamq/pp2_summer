mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# ---- creating an iterator

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# ---- yield

def count_up():
    yield 1
    yield 2
    yield 3

gen = count_up()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# --- function generators

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# ---

# List comprehension
lst = [x**2 for x in range(5)]
type(lst)  # <class 'list'>

gen = (x**2 for x in range(5))
type(gen)  # <class 'generator'>
next(gen)  # 0
next(gen)  # 1
next(gen)  # 4
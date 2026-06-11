print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

x = "Hello"
y = 15

print(bool(x)) # true cuz string in non empty
print(bool(y)) # true cuz 15 is not zero

# all false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def myFunction() :
  return True

print(myFunction()) # True

x = 200
print(isinstance(x, int)) # true
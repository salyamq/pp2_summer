thislist = ["apple", "banana", "cherry"]
print(thislist) # list

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # access list items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # changing list items

# ---
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# ---

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # deleting second item, if pop is empty deleting the last
print(thislist)
# ---

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# ---

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # list comprehension

# --- (funcitons)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)



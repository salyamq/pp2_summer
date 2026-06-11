thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} # key: value

# --
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")

# --

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# --

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# --

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) # deleted last key:value and returned this deleted

# --

for x in thisdict:
  print(x) # keys

for x in thisdict:
  print(thisdict[x]) # values

for x in thisdict.values():
  print(x) # values

for x in thisdict.keys():
  print(x) # keys

for x, y in thisdict.items():
  print(x, y) # keys and values

# --

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# --
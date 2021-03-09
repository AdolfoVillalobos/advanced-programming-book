dogs = {"bc": "border-collie", "lr": "labrador retriever", "pg": "pug"}
telephones = {23545344: 'John', 23545340: 'Trinity', 23545342: 'Taylor'}
tuples = {('23545344', 0): 'office', ('2353445340', 1): 'admin'}

print(dogs)
print(tuples)


print(dogs["bc"])
print(telephones[23545344])

# Dictionaries are not sorted

d = {1: 'first key', '2': 'second key', 23.0: 'third key',
             (23, 5): 'fourth key'}
print(d)


# Dictionaries are mutable

dogs["te"] = "terrier"
print(dogs)

dogs["pg"] = "pug-pug"

print(dogs)


# Delete

del dogs["te"]
print(dogs)


print("pg" in dogs)
print("te" in dogs)


# get() method

print(dogs.get("pg", False))
print(dogs.get("te", 2))
print(dogs.get("te", "the dog does not exist"))


currency = {'Chile': 'Peso', 'Brazil': 'Real',
         'Peru': 'Sol', 'Spain': 'Euro', 'Italy': 'Euro'}

print(currency.keys())
print(currency.values())
print(currency.items())


print("This dictionary has the following keys:")

for k in currency:
    print(k)

print("The dictionary has the following keys")
for k in currency.keys():
    print(k)

print("The values in the dictionary: ")
for v in currency.values():
    print(v)


print("The pairs key-value: ")

for k,v in currency.items():
    print(f"The currency in {k} is {v}")

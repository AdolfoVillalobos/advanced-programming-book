msg = 'supercalifragilisticexpialidocious'
vowels = dict()

for v in msg:
    if v not in "aeiou":
        continue

    if v not in vowels:
        vowels[v] = 0

    vowels[v] += 1

print(vowels)

from collections import deque

# Deque

d = deque()

# Append

d.append("r")
d.append("a")
d.append("d")
d.append("a")
d.append("r")
d.append("e")
d.append("s")

print(d)
print(len(d))

# First and last items
print(d[0], d[-1])


# Rotate k= 3
d.rotate(3)
print(d)


# Extract first and last

first = d.popleft()
last = d.pop()
print(first, last)
print(d)

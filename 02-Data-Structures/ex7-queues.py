from collections import deque

q = deque()

# Enqueue

q.append("orange")
q.append("apple")
q.append("pear")

print(q)

# dequeue

print(f"Remove the first item: {q.popleft()}")
print(q)

# Add new element

q.append("strawberry")


# First element

print(f"The first element is: {q[0]}")


# Len

print(f"The que has {len(q)} elements.")

# is-empty and clear a queue

q.clear()

if len(q) == 0:
    print("The queue is empty")

stack = []

# Push method. 

stack.append(1)
stack.append(12)
stack.append(10)

print(stack)

# Pop method

stack.pop()
print("pop(): {0}".format(stack))


# Top Method

stack.append(25)
print(f"top(): {stack[-1]}")


# Len Method

print(f"The stack have {len(stack)} elements.")


# Is_empty method

stack =[]
if len(stack) == 0:
    print("the stack is empty :(")


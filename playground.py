stacks = []
word = "hello world"
for s in word:
    stacks.append(s)

while len(stacks) != 0:
    s = stacks.pop()
    print(s)
    
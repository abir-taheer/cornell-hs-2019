first = int(input())
inputs = []
for x in range(first):
    y = int(input())
    if y != 0:
        inputs.append(y)
c = 0
for i in inputs:
    c += int(i - 1)

print(c+1)

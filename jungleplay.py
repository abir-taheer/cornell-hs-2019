inp = 0
data = [input(), input()]
numbers = []
letters = ""
second = data[1]
offset = 1
max_index = 0
masterlist = []
tries = 0
for x in data[0].split(" "):
    numbers.append(int(x))

for x in range(numbers[0]):
    letters += chr(x + 97)

for z, x in enumerate(second):
    if numbers[2] > tries:
        print(-1)
        exit()
    if len(masterlist) == len(letters):
        # check for distractions
        if numbers[1] > 0:
            numbers[1] -= 1
            masterlist = []
        else:
            print(z)
            exit()
    if x in masterlist:
        continue
    else:
        masterlist.append(x)
    tries += 1

if len(masterlist) != len(letters):
    print(-1)
    exit()


samp = []

x = input()
while x != "all the birds":
    samp.append(x)
    x = input()

stop = False
musthaves = ["night night", "all the birds"]
kermits = ["Kermit", "Kermit Kermit Kermit", "Kermit Kermit"]
answer = []
for elements in musthaves:
    if elements not in samp:
        print("Im-parrot-ator!")
        stop = True
        break
if "awwww kitty" in samp:
    answer.append("There was a cat or a small dog")
if "mmmmmm" in samp:
    answer.append("He had walnuts")
if stop == False:
    for phrase in samp:
        if "Hi" in phrase:
            if phrase == "Hi Roger":
                answer.append("He saw Daniel")
                continue
            if phrase == "Hi Daniel":
                print("Im-parrot-ator!")
                stop = True
                break
            else:
                answer.append("He saw " + phrase[(phrase.find(" ") + 1):])
                continue
        if phrase == "what are you doing?":
            if samp.index(phrase) > samp.index("night night"):
                stop = True
                print("Im-parrot-ator!")
                break
            else:
                answer.append("His humans worked from home")
        if "Kermit" in phrase:
            if phrase not in kermits:
                stop = True
                print("Im-parrot-ator!")
                break

        if phrase == "night night":
            if samp.index(phrase) > samp.index("mmmmmm"):
                stop = True
                print("Im-parrot-ator!")
                break

if stop == False:
    print("Could be Kermit")
    for m in sorted(set(answer)):
        print(m)


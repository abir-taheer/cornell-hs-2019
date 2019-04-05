samp = []
x = input()
while x != "all the birds":
    samp.append(x)
    x = input()
stop = False
answer = []
samp.append('all the birds')
musthaves = ['night night', 'all the birds']
kermits = ['Kermit', 'Kermit Kermit', 'Kermit Kermit Kermit']
universal = ["Kermit", "Kermit Kermit", "Kermit Kermit Kermit", "awwww kitty", "mmmmmm", "what are you doing", "all the birds", "night night"]
for elements in musthaves:
    if elements not in samp:
        print("Im-parrot-ator!")
        stop = True
        exit()
    if "what are you doing" in samp:
        if 'mmmmmm' in samp:
            if samp.index("what are you doing") > samp.index("mmmmmm"):
                stop = True
        elif "night night" in samp:
            if samp.index("what are you doing") > samp.index('night night'):
                stop = True
        else:
            answer.append("His human worked from home")
    if "mmmmmm" in samp:
        if samp.index("mmmmmm") < samp.index("night night"):
            stop = True
        else:
            answer.append("He had walnuts")

    if stop == False:
        for phrase in samp:
            if not phrase.startswith("Hi"):
                if phrase not in universal:
                    stop = True
                    break
            if phrase.startswith('Hi'):
                if phrase == 'Hi Daniel':
                    stop = True
                    break
                elif phrase == 'Hi Roger':
                    answer.append("He saw Daniel")
                else:
                    answer.append("He saw " + phrase[(phrase.find(" ") + 1):])
            if "Kermit" in phrase:
                if phrase not in kermits:
                    stop = True
                    break

if stop == True:
    print("Im-parrot-ator!")
elif stop == False:
    if "awwww kitty" in samp:
        answer.append("There was a cat or a small dog")
    print("Could be kermit")
    for i in sorted(set(answer)):
        print(i)


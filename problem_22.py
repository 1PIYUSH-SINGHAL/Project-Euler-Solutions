f = open("names.txt").read()
names = f.replace('"','').split(',')
names.sort()

total = 0
i = 0
while i < len(names):
    name = names[i]
    score = 0
    j = 0
    while j < len(name):
        score += ord(name[j]) - ord('A') + 1
        j += 1
    total += score * (i + 1)
    i += 1

print(total)

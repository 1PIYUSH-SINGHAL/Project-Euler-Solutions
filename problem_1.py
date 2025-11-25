x = []
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        if i in x:
            continue
        else:
            x.append(i)

print(sum(x))

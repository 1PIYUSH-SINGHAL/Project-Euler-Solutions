n = 1
i = 1
while i <= 100:
    n *= i
    i += 1

s = 0
for c in str(n):
    s += int(c)

print(s)

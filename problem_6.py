n = 1
s1 = 0
s2 = 0

while n <= 100:
    s1 = s1 + n
    s2 = s2 + n*n
    n += 1

res = s1*s1 - s2
print(res)

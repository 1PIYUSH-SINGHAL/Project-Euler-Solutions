a = 1
ans = 0

while a < 1000:
    b = a + 1
    while b < 1000:
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            ans = a * b * c
            break
        b += 1
    if ans:
        break
    a += 1

print(ans)

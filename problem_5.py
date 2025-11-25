x = 1
i = 1

while i <= 20:
    a = x
    b = i

    while b != 0:
        t = b
        b = a % b
        a = t

    x = x * i // a
    i += 1

print(x)

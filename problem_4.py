def p(n):
    n = str(n)
    r = ""
    for c in n:
        r = c + r
    if n == r:
        return True
    else:
        return False

m = 0
a = 100
while a < 1000:
    b = 100
    while b < 1000:
        x = a * b
        if p(x):
            if x > m:
                m = x
        b += 1
    a += 1

print(m)

n = 600851475143
a = 2

while a**2 <= n:
    if n % a == 0:
        n = n // a
    else:
        a += 1

print(n)

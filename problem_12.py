def divcount(n):
    c = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            c += 2
        if i*i == n:
            c -= 1
        i += 1
    return c

n = 1
tri = 1

while divcount(tri) <= 500:
    n += 1
    tri += n

print(tri)

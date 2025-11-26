def fact(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f

n = 20
ans = fact(2*n) // ((fact(n))**2)
print(ans)

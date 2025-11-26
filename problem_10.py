def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = 2
ans = 0

while n < 2000000:
    if prime(n):
        ans += n
    n += 1

print(ans)

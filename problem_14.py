def collatz_len(n):
    l = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        l += 1
    return l

maxlen = 0
ans = 0
i = 1

while i < 1000000:
    l = collatz_len(i)
    if l > maxlen:
        maxlen = l
        ans = i
    i += 1

print(ans)

maxlen = 0
ans = 0
d = 2

while d < 1000:
    n = 1
    pos = 0
    seen = {}
    while n != 0 and n not in seen:
        seen[n] = pos
        n = (n * 10) % d
        pos += 1
    cycle = pos - seen.get(n, pos)
    if cycle > maxlen:
        maxlen = cycle
        ans = d
    d += 1

print(ans)

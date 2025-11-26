def div_sum(n):
    s = 1
    i = 2
    while i*i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    return s

ab = []
i = 12
while i <= 28123:
    if div_sum(i) > i:
        ab.append(i)
    i += 1

can = [True] * 28124
i = 0
while i < len(ab):
    j = i
    while j < len(ab):
        s = ab[i] + ab[j]
        if s <= 28123:
            can[s] = False
        j += 1
    i += 1

total = 0
i = 1
while i <= 28123:
    if can[i]:
        total += i
    i += 1

print(total)

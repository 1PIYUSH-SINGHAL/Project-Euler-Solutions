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

i = 2
total = 0
while i < 10000:
    j = div_sum(i)
    if j != i and div_sum(j) == i:
        total += i
    i += 1

print(total)

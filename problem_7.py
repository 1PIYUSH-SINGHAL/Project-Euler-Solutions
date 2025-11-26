def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

count = 0
num = 1

while count < 10001:
    num += 1
    if prime(num):
        count += 1

print(num)

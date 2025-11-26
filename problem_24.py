import math

digits = [0,1,2,3,4,5,6,7,8,9]
n = 999999
perm = []

while digits:
    f = math.factorial(len(digits)-1)
    i = n // f
    perm.append(digits[i])
    digits.pop(i)
    n = n % f

s = ""
i = 0
while i < len(perm):
    s += str(perm[i])
    i += 1

print(s)

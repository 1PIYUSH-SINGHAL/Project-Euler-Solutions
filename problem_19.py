y = 1901
m = 1
day = 2
count = 0

while y <= 2000:
    if day == 0:
        count += 1

    if m in [1,3,5,7,8,10,12]:
        dm = 31
    elif m in [4,6,9,11]:
        dm = 30
    elif y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        dm = 29
    else:
        dm = 28

    day = (day + dm) % 7
    m += 1
    if m > 12:
        m = 1
        y += 1

print(count)

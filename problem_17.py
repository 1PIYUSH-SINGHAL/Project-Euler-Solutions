ones = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
         "seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

total = 0
n = 1
while n <= 1000:
    letters = 0
    if n == 1000:
        letters = len("onethousand")
    else:
        h = n // 100
        r = n % 100
        if h > 0:
            letters += len(ones[h]) + len("hundred")
            if r:
                letters += len("and")
        if r >= 20:
            letters += len(tens[r//10]) + len(ones[r%10])
        elif r >= 10:
            letters += len(teens[r-10])
        else:
            letters += len(ones[r])
    total += letters
    n += 1

print(total)

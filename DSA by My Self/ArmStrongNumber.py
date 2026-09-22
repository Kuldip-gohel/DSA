n = 1634
num = n
digit = len(str(n))
total = 0

while num > 0:
    ld = num % 10
    total = (ld ** digit) + total
    num = num // 10
    result = total == n

print(result)
    




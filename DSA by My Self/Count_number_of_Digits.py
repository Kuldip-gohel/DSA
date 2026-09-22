n = 5873
num = n
count = 0

while num > 0 :
    count += 1
    num = num // 10

print(count)

# Alternative way

from math import *
print(int(log10(5873)+1))
    
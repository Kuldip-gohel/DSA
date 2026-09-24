n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

# How many time values of m occure in n , print it.
for i in m:
    count = 0
    for j in n:
        if j == i:
            count += 1
    print(count)            # TC -> O(N * M)  ,  SC -> O(1)


# Another Method

hash_list = [0]*11
for i in n:
    hash_list[i] += 1

print(hash_list)

for i in m:
    if i<0 or i>10:
        print(0)
    else:
        print(hash_list[i])


# Using Dictnory
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]


hash_mapp = dict()

for i in range(0, len(n)):
    if n[i] in hash_mapp:
        hash_mapp[n[i]] += 1
    else:
        hash_mapp[n[i]] = 1

print(hash_mapp)

for j in m:
    count = hash_mapp.get(j, 0)
    print(count)


# Character hashing

s = "azyxyyzaaaa"
q = ["d","a","y","x"]
hash_list = [0] * 26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])
    
print(hash_list)